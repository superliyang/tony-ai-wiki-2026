#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../backend"
uv venv
source .venv/bin/activate
uv pip install -e .
