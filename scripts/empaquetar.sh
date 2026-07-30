#!/usr/bin/env bash
# Empaqueta el plugin revos como .plugin (zip), excluyendo repo, docs y scripts.
# Construye en /tmp y copia por encima (algunos mounts no permiten unlink).
set -e
cd "$(dirname "$0")/.."
TMP=$(mktemp -u /tmp/revos-XXXX.plugin)
zip -rq "$TMP" . -x "*.DS_Store" -x ".git/*" -x "docs/*" -x "scripts/*" -x ".gitignore" -x "*.plugin"
cp "$TMP" revos.plugin
echo "revos.plugin generado ($(du -h revos.plugin | cut -f1))"
