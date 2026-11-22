#!/usr/bin/env bash
set -euo pipefail
artigo_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
python3 "$artigo_dir/scripts/verificar.py"
cd "$artigo_dir"
if command -v tectonic >/dev/null 2>&1; then
  tectonic --keep-logs main.tex
elif command -v latexmk >/dev/null 2>&1; then
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
else
  echo 'Instale tectonic ou latexmk para compilar o modelo SBC.' >&2
  exit 1
fi
python3 scripts/validar_pdf.py main.pdf
