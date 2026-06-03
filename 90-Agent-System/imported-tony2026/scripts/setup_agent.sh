#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

PYTHON_BIN="${PYTHON_BIN:-/usr/bin/python3}"
ENV_FILE="90-Agent-System/.env.local"
ENV_EXAMPLE="90-Agent-System/.env.example"

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "This one-command installer currently targets macOS launchd." >&2
  echo "On Linux, install requirements.txt and run the scripts with systemd/cron until a Linux installer is added." >&2
  exit 2
fi

if [[ ! -f "$ENV_FILE" ]]; then
  cp "$ENV_EXAMPLE" "$ENV_FILE"
  echo "Created $ENV_FILE."
  echo "Fill FEISHU_WEBHOOK_URL, FEISHU_APP_ID, FEISHU_APP_SECRET and DEEPSEEK_API_KEY, then rerun this command."
  exit 1
fi

missing="$("$PYTHON_BIN" - <<'PY'
from pathlib import Path

required = ["FEISHU_WEBHOOK_URL", "FEISHU_APP_ID", "FEISHU_APP_SECRET", "DEEPSEEK_API_KEY"]
values = {}
for line in Path("90-Agent-System/.env.local").read_text(encoding="utf-8").splitlines():
    if "=" not in line or line.lstrip().startswith("#"):
        continue
    key, value = line.split("=", 1)
    values[key.strip()] = value.strip().strip('"').strip("'")
print(" ".join(key for key in required if not values.get(key)))
PY
)"
if [[ -n "$missing" ]]; then
  echo "Fill required values in $ENV_FILE before installing services: $missing" >&2
  exit 1
fi

echo "[setup] installing Python dependencies."
PYTHON_BIN="$PYTHON_BIN" scripts/bootstrap_agent_env.sh

echo "[setup] validating Feishu bot configuration."
"$PYTHON_BIN" scripts/feishu_bot_ws.py --dry-run

if git remote get-url origin >/dev/null 2>&1; then
  echo "[setup] checking Git remote access."
  git fetch origin "$(git rev-parse --abbrev-ref HEAD)"
else
  echo "[setup] no origin remote configured; automated Git sync will be unavailable." >&2
fi

echo "[setup] installing macOS services."
scripts/launchd_agent.sh install
echo "[setup] validating installed automation."
"$PYTHON_BIN" scripts/automation_doctor.py --network
echo "[setup] installed. Use scripts/launchd_agent.sh status or logs to inspect the running services."
