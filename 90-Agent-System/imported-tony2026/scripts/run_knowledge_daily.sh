#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

PYTHON_BIN="${PYTHON_BIN:-/usr/bin/python3}"

"$PYTHON_BIN" -u scripts/knowledge_daily.py "$@"

if [[ "${KNOWLEDGE_SKIP_GIT_SYNC:-0}" != "1" ]]; then
  scripts/git_checkpoint.sh "chore: sync daily knowledge automation"
fi
