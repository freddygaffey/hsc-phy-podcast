#!/usr/bin/env bash
#
# One-command publish: refresh the manifest, commit + push, and deploy to Pages.
#
#   ./tools/publish.sh "Add M7 light episodes"
#
# Works with your local `wrangler login` — no GitHub secret required. (Once the
# CLOUDFLARE_API_TOKEN repo secret is set, `git push` alone also auto-deploys via
# .github/workflows/deploy.yml; this script just makes a manual publish one step.)
#
# Audio: render with ./generate_all_voices.sh and upload with ./tools/upload-audio.sh
# first if you want sound — the manifest then picks up voices/durations here.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

export AUDIO_BASE_URL="${AUDIO_BASE_URL:-https://audio.phy.pebnum.com}"
export PAGES_PROJECT="${PAGES_PROJECT:-hsc-phy-podcast}"

echo "==> Refreshing manifest.json"
python3 tools/generate_manifest.py

git add -A
if git diff --cached --quiet; then
  echo "==> No tracked changes to commit (continuing to deploy current state)"
else
  git commit -m "${1:-Update episodes}"
  echo "==> Pushing to GitHub"
  git push
fi

echo "==> Deploying to Cloudflare Pages"
PATH="$ROOT/node_modules/.bin:$PATH" ./tools/deploy.sh

echo "==> Published. Live at https://phy.pebnum.com (and hsc-phy-podcast.pages.dev)"
