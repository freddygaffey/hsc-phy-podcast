#!/usr/bin/env python3
"""Upload episode audio (content/**/*.m4a) to Cloudflare R2 using wrangler.

Objects are keyed <episode>/<voice>.m4a — exactly what the deployed manifest
points at (AUDIO_BASE_URL/<episode>/<voice>.m4a). Uses your `wrangler login`,
so there's no rclone and no S3 keys to configure.

Modes:
  python3 tools/upload_audio.py            # one-shot: upload new/changed, then exit
  python3 tools/upload_audio.py --watch    # daemon: upload audio as it's generated,
                                           #   then refresh the manifest + deploy once
                                           #   uploads go quiet

Flags:
  --force        re-upload everything, ignoring the upload cache
  --no-deploy    (watch) don't auto-deploy after uploads settle
  --no-manifest  (watch) don't regenerate the manifest after uploads settle

Env: R2_BUCKET (default hsc-phy-podcast), AUDIO_BASE_URL
     (default https://audio.phy.pebnum.com), PAGES_PROJECT (default hsc-phy-podcast),
     UPLOAD_JOBS (default 4 concurrent uploads).
"""
import argparse
import json
import os
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
STATE_FILE = ROOT / "tools" / ".upload-state.json"
WRANGLER = ["node", str(ROOT / "node_modules" / "wrangler" / "bin" / "wrangler.js")]
BUCKET = os.environ.get("R2_BUCKET", "hsc-phy-podcast")
JOBS = int(os.environ.get("UPLOAD_JOBS", "4"))
POLL = 5     # seconds between scans in --watch
QUIET = 20   # seconds with no new uploads before manifest+deploy in --watch

_state_lock = threading.Lock()


def load_state() -> dict:
    try:
        return json.loads(STATE_FILE.read_text())
    except Exception:
        return {}


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state))


def m4a_files() -> list[Path]:
    return sorted(CONTENT.glob("*/*.m4a"))


def key_for(path: Path) -> str:
    return str(path.relative_to(CONTENT))  # <episode>/<voice>.m4a


def upload_one(path: Path, key: str) -> None:
    subprocess.run(
        WRANGLER + ["r2", "object", "put", f"{BUCKET}/{key}",
                    "--file", str(path), "--remote", "--content-type", "audio/mp4"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def upload_changed(state: dict, force: bool = False) -> int:
    """Upload every new/changed .m4a (concurrently). Returns the count uploaded."""
    todo = []
    for path in m4a_files():
        st = path.stat()
        sig = [int(st.st_mtime), st.st_size]
        key = key_for(path)
        if not force and state.get(key) == sig:
            continue
        todo.append((path, key, sig))
    if not todo:
        return 0

    uploaded = 0

    def work(item):
        path, key, sig = item
        upload_one(path, key)
        return key, sig

    with ThreadPoolExecutor(max_workers=max(1, JOBS)) as ex:
        futures = {ex.submit(work, it): it for it in todo}
        for fut in as_completed(futures):
            path, key, sig = futures[fut]
            try:
                fut.result()
            except subprocess.CalledProcessError:
                print(f"  ! failed: {key}", file=sys.stderr)
                continue
            with _state_lock:
                state[key] = sig
                save_state(state)
            uploaded += 1
            print(f"  ↑ {key}")
    return uploaded


def refresh_and_deploy(manifest: bool, deploy: bool) -> None:
    env = dict(os.environ)
    env.setdefault("AUDIO_BASE_URL", "https://audio.phy.pebnum.com")
    env.setdefault("PAGES_PROJECT", "hsc-phy-podcast")
    if manifest:
        print("  → refreshing manifest.json")
        subprocess.run(["python3", "tools/generate_manifest.py"],
                       cwd=ROOT, env=env, check=False)
    if deploy:
        print("  → deploying to Pages")
        env["PATH"] = f"{ROOT / 'node_modules' / '.bin'}:{env.get('PATH', '')}"
        subprocess.run(["bash", "tools/deploy.sh"], cwd=ROOT, env=env, check=False)


def main() -> None:
    ap = argparse.ArgumentParser(description="Upload episode audio to R2 via wrangler.")
    ap.add_argument("--watch", action="store_true", help="run as a background daemon")
    ap.add_argument("--force", action="store_true", help="re-upload everything")
    ap.add_argument("--no-deploy", action="store_true", help="(watch) skip auto-deploy")
    ap.add_argument("--no-manifest", action="store_true", help="(watch) skip manifest refresh")
    args = ap.parse_args()

    state = load_state()

    if not args.watch:
        n = upload_changed(state, force=args.force)
        print(f"Uploaded {n} file(s) to R2 bucket '{BUCKET}'.")
        return

    print(f"Watching {CONTENT} for new audio → R2 '{BUCKET}'  (Ctrl-C to stop)")
    n = upload_changed(state, force=args.force)
    if n:
        print(f"[init] uploaded {n} file(s)")
    dirty = n > 0
    last_change = time.time()
    try:
        while True:
            time.sleep(POLL)
            n = upload_changed(state)
            if n:
                dirty = True
                last_change = time.time()
                print(f"[update] uploaded {n} new file(s)")
            elif dirty and (time.time() - last_change) >= QUIET:
                refresh_and_deploy(manifest=not args.no_manifest, deploy=not args.no_deploy)
                dirty = False
                print("[idle] in sync — waiting for more audio")
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
