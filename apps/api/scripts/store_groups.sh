#!/usr/bin/env bash
set -euo pipefail

OUT="${1:-groups.json}"

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd -- "${SCRIPT_DIR}/.." && pwd)"

cd "$ROOT_DIR"
python -m scripts.store_groups "$OUT"
