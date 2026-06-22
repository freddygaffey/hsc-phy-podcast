#!/usr/bin/env bash
#
# Upload episode audio (content/**/*.m4a) to Cloudflare R2 via wrangler — no rclone,
# no S3 keys; it uses your `wrangler login`. Objects land keyed as
# <episode>/<voice>.m4a, exactly what the deployed manifest points at.
#
#   ./tools/upload-audio.sh            # upload new/changed audio now, then exit
#   ./tools/upload-audio.sh --watch    # background daemon: upload audio as it's
#                                      #   generated, then refresh manifest + deploy
#   ./tools/upload-audio.sh --force    # re-upload everything
#
# Env: R2_BUCKET (default hsc-phy-podcast), UPLOAD_JOBS (default 4).
exec python3 "$(cd "$(dirname "$0")" && pwd)/upload_audio.py" "$@"
