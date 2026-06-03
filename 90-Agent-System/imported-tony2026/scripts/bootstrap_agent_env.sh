#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

PYTHON_BIN="${PYTHON_BIN:-/usr/bin/python3}"

"$PYTHON_BIN" -m pip install -r requirements.txt

echo "Agent automation dependencies installed for: $("$PYTHON_BIN" -V)"
echo "Use: $PYTHON_BIN scripts/feishu_bot_ws.py"
