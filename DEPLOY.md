# Deploying the Podcast app to Cloudflare

This app is a **100% static PWA** — there is **no server, no database, no API**.
Every feature (progress, quizzes, stats, theme, queue) runs in the browser and is
stored in `localStorage`. So the whole thing is just files on a CDN.

We split it across two Cloudflare products:

| What | Where | Why |
|------|-------|-----|
| App shell + per-episode markdown/quiz (~a few MB) | **Cloudflare Pages** | Fast static hosting, unlimited bandwidth |
| Episode audio — one `.m4a` per voice per episode (a few GB) | **Cloudflare R2** | Object storage with **zero egress fees**; too big for git |

```
  podcast.example.com  ──►  Pages   (index.html, app.js, style.css, sw, content/*.md, *.json, manifest.json)
  audio.example.com    ──►  R2      (<episode>/<voice>.m4a)
```

> ### This deployment (live values)
> | | |
> |---|---|
> | App URL | **https://phy.pebnum.com** (also `hsc-phy-podcast.pages.dev`) |
> | Audio URL | **https://audio.phy.pebnum.com** |
> | Pages project | `hsc-phy-podcast` |
> | R2 bucket | `hsc-phy-podcast` |
> | Zone (`pebnum.com`) ID | `3e74b5dcb0bbd3fe813ff013715abc0e` |
> | Cloudflare account | `ac128818b294f0f51e44cb7082804bca` (fredgaffey08@gmail.com) |
>
> **Redeploy the app** (after changing content/code):
> ```bash
> AUDIO_BASE_URL=https://audio.phy.pebnum.com PAGES_PROJECT=hsc-phy-podcast ./tools/deploy.sh
> ```
> **Re-upload audio** (after rendering new `.m4a`): see §1d, or the wrangler loop in that section.

> **Do I need the Flask/Docker server?** No. The app makes zero backend calls — a
> server would sit idle. The *only* thing a backend could add is syncing your listening
> progress across devices (right now each browser keeps its own). If you ever want that,
> do it with a tiny Cloudflare Worker + D1 database — stay on one platform, skip Flask.

---

## 0. Prerequisites (one time)

1. A **Cloudflare account** (free), with your domain added to it (Cloudflare is your
   DNS — the domain's nameservers point at Cloudflare). The two hostnames used below,
   `podcast.example.com` and `audio.example.com`, are just examples — pick your own.
2. **Wrangler** (Cloudflare's CLI) — install via **npm**, not Homebrew (the `brew`
   formula named `wrangler` is an unrelated, disabled package). Node is already installed:
   ```bash
   npm install -g wrangler
   wrangler login          # opens a browser to authorise
   ```
3. **rclone** for the bulk audio upload:
   ```bash
   brew install rclone
   ```
4. **ffmpeg/ffprobe** (you already have it — used to read audio durations when building
   the manifest):
   ```bash
   brew install ffmpeg     # if missing
   ```

Run every command below from the `podcast/` directory.

---

## 1. Create the R2 bucket and upload the audio

### 1a. Create the bucket
```bash
wrangler r2 bucket create hsc-phy-podcast
```

### 1b. Make it public on a custom domain
In the Cloudflare dashboard: **R2 → `hsc-phy-podcast` → Settings → Public access →
Custom Domains → Connect Domain** → enter `audio.example.com`. Cloudflare adds the DNS
record and a TLS cert automatically. (This is what makes the audio reachable and gives
you HTTP Range / `206` responses, which iOS Safari requires to play `<audio>`.)

> CLI alternative (needs the Zone ID — find it on the domain's dashboard Overview page):
> ```bash
> wrangler r2 bucket domain add hsc-phy-podcast --domain audio.example.com --zone-id <ZONE_ID>
> ```

### 1c. Configure rclone for R2
Create an **R2 API token**: dashboard → **R2 → API → Manage API Tokens → Create** (Object
Read & Write). Note the **Access Key ID**, **Secret Access Key**, and your **Account ID**.

```bash
rclone config
# n) new remote
# name>     hsc-r2
# Storage>  s3
# provider> Cloudflare
# access_key_id>     <from the R2 token>
# secret_access_key> <from the R2 token>
# endpoint> https://<ACCOUNT_ID>.r2.cloudflarestorage.com
# (leave region/other blank)
```

### 1d. Upload the audio (a few GB)
```bash
./tools/upload-audio.sh
```
This runs `rclone copy content hsc-r2:hsc-phy-podcast --include '*.m4a'`, so objects
land keyed as `<episode>/<voice>.m4a` — exactly what the manifest will point at. It's
**resumable and idempotent**: safe to re-run; it only uploads what changed.

> No rclone? Fallback loop using only Wrangler (slower, one file at a time). The
> **`--remote` flag is mandatory** — without it Wrangler writes to a local sandbox, not
> your real bucket:
> ```bash
> find content -name '*.m4a' | while read -r f; do
>   key="${f#content/}"
>   wrangler r2 object put "hsc-phy-podcast/$key" --file "$f" --remote
> done
> ```

---

## 2. Create the Pages project

```bash
wrangler pages project create hsc-phy-podcast --production-branch main
```

---

## 3. Build and deploy the app

```bash
AUDIO_BASE_URL=https://audio.example.com ./tools/deploy.sh
```

`tools/deploy.sh` does three things:
1. Assembles a clean `dist/` — app shell + `content/**/{script.md,supplementary.md,quiz.json}`.
   **No audio, no venv, no scripts, no stray `.wav`.**
2. Regenerates `dist/manifest.json` so each voice's audio URL is
   `https://audio.example.com/<episode>/<voice>.m4a` (your repo `manifest.json`,
   which uses relative paths for local dev, is left untouched).
3. Runs `wrangler pages deploy dist --project-name hsc-phy-podcast`.

When it finishes, Wrangler prints a `*.pages.dev` URL — open it to smoke-test.

> Prefer the project name or audio host as defaults? Set `PAGES_PROJECT` /
> `AUDIO_BASE_URL` once in your shell profile and just run `./tools/deploy.sh`.

---

## 4. Point your custom domain at the app

Dashboard: **Workers & Pages → `hsc-phy-podcast` → Custom domains → Set up a custom domain**
→ `podcast.example.com`. DNS + cert are automatic.

> **Must be at the domain root.** The service worker registers at `/service-worker.js`
> and caches `/`, `/index.html`, … as absolute paths, and the PWA `start_url` is `/`. So
> serve the app at `podcast.example.com/` (a subdomain root), **not** under a sub-path
> like `example.com/podcast/`.

---

## 5. Verify

- Visit `https://podcast.example.com` → the library renders; modules expand.
- Play an episode. Open DevTools → **Network**, filter `m4a`: requests go to
  `audio.example.com` and return **`206 Partial Content`**. ✅ (the iOS-critical check)
- Open an episode → **Script / References / Quiz** tabs all load (markdown + quiz come
  from Pages).
- Toggle **offline** (DevTools → Network → Offline) and reload → the app shell still
  loads from the service-worker cache.
- On a phone, **Add to Home Screen** → it installs and launches full-screen at `/`.
- Spot-check an R2 object directly:
  ```bash
  curl -I https://audio.example.com/case_ligo_detects_gravitational_waves/af_heart.m4a
  # expect: 200, content-type: audio/mp4, accept-ranges: bytes
  ```

---

## 6. Publishing new episodes later

After you render audio for new episodes into `content/` (see the main `README.md`):

```bash
./tools/upload-audio.sh                                   # push new .m4a to R2
AUDIO_BASE_URL=https://audio.example.com ./tools/deploy.sh # rebuild manifest + redeploy
```

The app polls `manifest.json`, so once redeployed the new episodes appear automatically.

---

## 7. Continuous deployment (GitHub Actions)

`.github/workflows/deploy.yml` auto-deploys to Pages on every push to `main`
(project `hsc-phy-podcast`). It ships the app shell, per-episode text, and the
**committed `manifest.json`** — it does **not** rebuild the manifest, because the
audio (`*.m4a`) lives in R2, not git, so CI can't probe durations.

**One-time setup:** add a repository secret so the Action can deploy:
1. Cloudflare dashboard → **My Profile → API Tokens → Create Token** → use the
   **"Cloudflare Pages — Edit"** template (scoped to this account). Copy the token.
2. GitHub → repo **Settings → Secrets and variables → Actions → New repository secret**
   → name `CLOUDFLARE_API_TOKEN`, value = the token.

**Day-to-day:** after rendering + uploading new audio, regenerate and commit the
manifest so the deploy points at the right audio, then push:
```bash
./generate_all_voices.sh                                        # render audio
./tools/upload-audio.sh                                         # push .m4a to R2
AUDIO_BASE_URL=https://audio.phy.pebnum.com python3 tools/generate_manifest.py
git add manifest.json content && git commit -m "Add/update episodes" && git push
```
The push triggers the Action, which redeploys `phy.pebnum.com` automatically.

> Audio upload stays a local step (`upload-audio.sh`) — CI never touches R2.

---

## Notes & gotchas

- **Free tier is plenty.** Pages: unlimited requests & bandwidth, up to 20,000 files and
  25 MiB/file per deploy (a typical `.m4a` is well under that, and the Pages bundle is
  only a few hundred tiny files). R2: 10 GB storage + zero egress on the free plan.
- **Excluded from the deploy automatically:** the `.tts-venv/`, stray `.wav` files,
  `_research/`, `_not_needed/`, generation scripts, and authoring docs. `deploy.sh` also
  hard-fails if any audio sneaks into `dist/`.
- **Offline audio caching is limited.** The service worker caches the app shell and
  markdown for offline use, but audio comes cross-origin from R2 and is fetched via
  Range requests, which the SW intentionally passes straight to the browser — so audio
  isn't cached for offline playback. The app and read-along content still work offline.
- **Local dev is unchanged.** Run `python3 tools/serve.py` as before; with no
  `AUDIO_BASE_URL` set, the manifest keeps relative `content/...` audio paths served
  locally.
