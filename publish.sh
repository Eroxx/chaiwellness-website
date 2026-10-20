#!/bin/bash
# Publishes this folder to github.com/Eroxx/chaiwellness-website, which GitHub Pages
# serves at https://eroxx.github.io/chaiwellness-website/ (and at a custom domain once
# a CNAME file is added here). The source of truth is this folder in the ChaiWellness
# repo; the website repo only ever holds what this script copies into it.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
git clone --quiet https://github.com/Eroxx/chaiwellness-website.git "$TMP/site"
rsync -a --delete --exclude .git --exclude publish.sh --exclude .claude --exclude scripts "$HERE/" "$TMP/site/"
cd "$TMP/site"
git add -A
if git diff --cached --quiet; then echo "Nothing changed."; exit 0; fi
git commit --quiet -m "${1:-Update site}"
git push --quiet origin main
echo "Pushed. Live in a minute at https://eroxx.github.io/chaiwellness-website/"
