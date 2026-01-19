#!/usr/bin/env bash
set -euo pipefail

# Demo script to show how to use paper-humanizer
# Run from the project root directory

echo "=== Paper Humanizer Demo ==="
echo ""
echo "Processing Chinese example..."
echo "---"
./bin/paper_humanizer.sh examples/zh_input.txt

echo ""
echo "==="
echo ""
echo "Processing English example..."
echo "---"
./bin/paper_humanizer.sh examples/en_input.txt