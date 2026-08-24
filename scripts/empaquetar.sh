#!/usr/bin/env bash
# Empaqueta el plugin revos como .plugin (zip), excluyendo repo, docs y scripts.
# Construye en /tmp y copia por encima (algunos mounts no permiten unlink).
# v4.3.1: valida antes de empaquetar — si el validador encuentra errores, no se genera el .plugin.
set -e
cd "$(dirname "$0")/.."

echo "→ Validando higiene del plugin…"
python3 scripts/validar_revos.py . || { echo "✗ Validación fallida — no se empaqueta. Corrige los errores y reintenta."; exit 1; }

TMPDIR=$(mktemp -d /tmp/revos-XXXX)
TMP="$TMPDIR/revos.plugin"
zip -rq "$TMP" . -x "*.DS_Store" -x ".git/*" -x "docs/*" -x "scripts/*" -x ".gitignore" -x "*.plugin"
python3 -c "import zipfile,sys; zipfile.ZipFile(sys.argv[1]).testzip() and sys.exit(1)" "$TMP" || { echo "✗ ZIP inválido"; rm -rf "$TMPDIR"; exit 1; }
cp "$TMP" revos.plugin
rm -rf "$TMPDIR"
echo "✓ revos.plugin generado ($(du -h revos.plugin | cut -f1))"
