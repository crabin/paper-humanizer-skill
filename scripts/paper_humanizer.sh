#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   ./bin/paper_humanizer.sh examples/zh_input.txt > composed_prompt.md

TEXT_FILE="${1:-}"
if [[ -z "${TEXT_FILE}" ]]; then
  echo "Usage: $0 <text-file>" >&2
  exit 1
fi

python3 bin/paper_humanizer.py \
  --text-file "${TEXT_FILE}" \
  --language auto \
  --field "computer science" \
  --audience "academic" \
  --tone formal \
  --blacklist-level high