#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

REPO_ROOT="$(pwd)"
LAUNCH_AGENT_DIR="$HOME/Library/LaunchAgents"
LOG_DIR="$REPO_ROOT/90-Agent-System/logs/launchd"
PYTHON_BIN="${PYTHON_BIN:-/usr/bin/python3}"

BOT_LABEL="com.tony2026.knowledge-feishu-bot"
DAILY_LABEL="com.tony2026.knowledge-daily"
WEEKLY_LABEL="com.tony2026.knowledge-weekly"
RECOVERY_LABEL="com.tony2026.knowledge-recovery"

BOT_PLIST="$LAUNCH_AGENT_DIR/$BOT_LABEL.plist"
DAILY_PLIST="$LAUNCH_AGENT_DIR/$DAILY_LABEL.plist"
WEEKLY_PLIST="$LAUNCH_AGENT_DIR/$WEEKLY_LABEL.plist"
RECOVERY_PLIST="$LAUNCH_AGENT_DIR/$RECOVERY_LABEL.plist"

usage() {
  cat <<'USAGE'
Usage: scripts/launchd_agent.sh <command>

Commands:
  install     Install launchd services and start the Feishu bot
  uninstall   Stop and remove launchd services
  start       Start the Feishu bot service
  stop        Stop the Feishu bot service
  restart     Restart the Feishu bot service
  status      Show launchd service status
  logs        Tail recent service logs
  doctor      Check local service prerequisites
  privacy     Open macOS Full Disk Access settings

Services:
  com.tony2026.knowledge-feishu-bot  KeepAlive WebSocket bot
  com.tony2026.knowledge-daily       Daily digest at 08:30 local time
  com.tony2026.knowledge-weekly      Weekly digest Monday 09:00 local time
  com.tony2026.knowledge-recovery    Catch up missed current-period jobs after login
USAGE
}

doctor() {
  echo "Repo: $REPO_ROOT"
  echo "LaunchAgent dir: $LAUNCH_AGENT_DIR"
  echo "Log dir: $LOG_DIR"
  echo

  if [[ "$REPO_ROOT" == "$HOME/Documents/"* || "$REPO_ROOT" == "$HOME/Desktop/"* || "$REPO_ROOT" == "$HOME/Downloads/"* ]]; then
    cat <<EOF
macOS privacy note:
  This repo is under a protected folder. launchd may fail with:
    Operation not permitted

Fix options:
  1. System Settings -> Privacy & Security -> Full Disk Access
     Add and enable:
       /bin/bash
       /usr/bin/python3
  2. Or move the vault to a non-protected folder such as:
       $HOME/Developer/tony2026

After changing permissions, run:
  scripts/launchd_agent.sh install
EOF
  else
    echo "Repo is not under Documents/Desktop/Downloads; launchd filesystem access should be simpler."
  fi

  echo
  echo "Dependency check:"
  /usr/bin/python3 - <<'PY'
mods = ["feedparser", "yaml", "requests", "lark_oapi"]
for mod in mods:
    try:
        __import__(mod)
        print(f"  {mod}: ok")
    except Exception as exc:
        print(f"  {mod}: missing ({exc})")
PY
}

open_privacy_settings() {
  open "x-apple.systempreferences:com.apple.preference.security?Privacy_AllFiles"
}

write_plists() {
  mkdir -p "$LAUNCH_AGENT_DIR" "$LOG_DIR"

  cat > "$BOT_PLIST" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>$BOT_LABEL</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>$REPO_ROOT/scripts/run_feishu_bot.sh</string>
  </array>
  <key>WorkingDirectory</key>
  <string>$REPO_ROOT</string>
  <key>KeepAlive</key>
  <true/>
  <key>RunAtLoad</key>
  <true/>
  <key>StandardOutPath</key>
  <string>$LOG_DIR/feishu-bot.out.log</string>
  <key>StandardErrorPath</key>
  <string>$LOG_DIR/feishu-bot.err.log</string>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PYTHONUNBUFFERED</key>
    <string>1</string>
    <key>PYTHON_BIN</key>
    <string>$PYTHON_BIN</string>
  </dict>
</dict>
</plist>
PLIST

  cat > "$DAILY_PLIST" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>$DAILY_LABEL</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>$REPO_ROOT/scripts/run_knowledge_daily.sh</string>
  </array>
  <key>WorkingDirectory</key>
  <string>$REPO_ROOT</string>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Hour</key>
    <integer>8</integer>
    <key>Minute</key>
    <integer>30</integer>
  </dict>
  <key>StandardOutPath</key>
  <string>$LOG_DIR/daily.out.log</string>
  <key>StandardErrorPath</key>
  <string>$LOG_DIR/daily.err.log</string>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PYTHONUNBUFFERED</key>
    <string>1</string>
    <key>PYTHON_BIN</key>
    <string>$PYTHON_BIN</string>
  </dict>
</dict>
</plist>
PLIST

  cat > "$WEEKLY_PLIST" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>$WEEKLY_LABEL</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>$REPO_ROOT/scripts/run_knowledge_weekly.sh</string>
  </array>
  <key>WorkingDirectory</key>
  <string>$REPO_ROOT</string>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Weekday</key>
    <integer>1</integer>
    <key>Hour</key>
    <integer>9</integer>
    <key>Minute</key>
    <integer>0</integer>
  </dict>
  <key>StandardOutPath</key>
  <string>$LOG_DIR/weekly.out.log</string>
  <key>StandardErrorPath</key>
  <string>$LOG_DIR/weekly.err.log</string>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PYTHONUNBUFFERED</key>
    <string>1</string>
    <key>PYTHON_BIN</key>
    <string>$PYTHON_BIN</string>
  </dict>
</dict>
</plist>
PLIST

  cat > "$RECOVERY_PLIST" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>$RECOVERY_LABEL</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>$REPO_ROOT/scripts/run_startup_recover.sh</string>
  </array>
  <key>WorkingDirectory</key>
  <string>$REPO_ROOT</string>
  <key>RunAtLoad</key>
  <true/>
  <key>StandardOutPath</key>
  <string>$LOG_DIR/recovery.out.log</string>
  <key>StandardErrorPath</key>
  <string>$LOG_DIR/recovery.err.log</string>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PYTHONUNBUFFERED</key>
    <string>1</string>
    <key>PYTHON_BIN</key>
    <string>$PYTHON_BIN</string>
  </dict>
</dict>
</plist>
PLIST
}

bootout_if_loaded() {
  local label="$1"
  launchctl bootout "gui/$(id -u)/$label" >/dev/null 2>&1 || true
}

bootstrap_plist() {
  local plist="$1"
  launchctl bootstrap "gui/$(id -u)" "$plist" 2>/dev/null || true
}

kickstart_label() {
  local label="$1"
  launchctl kickstart -k "gui/$(id -u)/$label"
}

install_services() {
  write_plists
  bootout_if_loaded "$BOT_LABEL"
  bootout_if_loaded "$DAILY_LABEL"
  bootout_if_loaded "$WEEKLY_LABEL"
  bootout_if_loaded "$RECOVERY_LABEL"
  bootstrap_plist "$BOT_PLIST"
  bootstrap_plist "$DAILY_PLIST"
  bootstrap_plist "$WEEKLY_PLIST"
  bootstrap_plist "$RECOVERY_PLIST"
  kickstart_label "$BOT_LABEL"
  echo "Installed launchd services."
  status_services
}

uninstall_services() {
  bootout_if_loaded "$BOT_LABEL"
  bootout_if_loaded "$DAILY_LABEL"
  bootout_if_loaded "$WEEKLY_LABEL"
  bootout_if_loaded "$RECOVERY_LABEL"
  rm -f "$BOT_PLIST" "$DAILY_PLIST" "$WEEKLY_PLIST" "$RECOVERY_PLIST"
  echo "Removed launchd services."
}

start_bot() {
  if [[ ! -f "$BOT_PLIST" ]]; then
    write_plists
    bootstrap_plist "$BOT_PLIST"
  fi
  kickstart_label "$BOT_LABEL"
}

stop_bot() {
  bootout_if_loaded "$BOT_LABEL"
}

status_services() {
  echo "LaunchAgents:"
  for label in "$BOT_LABEL" "$DAILY_LABEL" "$WEEKLY_LABEL" "$RECOVERY_LABEL"; do
    if launchctl print "gui/$(id -u)/$label" >/dev/null 2>&1; then
      echo "  $label: loaded"
      launchctl print "gui/$(id -u)/$label" | awk '/state =|pid =|last exit code =/ {print "    " $0}'
    else
      echo "  $label: not loaded"
    fi
  done
}

tail_logs() {
  mkdir -p "$LOG_DIR"
  echo "== Feishu bot stdout =="
  tail -n 80 "$LOG_DIR/feishu-bot.out.log" 2>/dev/null || true
  echo "== Feishu bot stderr =="
  tail -n 80 "$LOG_DIR/feishu-bot.err.log" 2>/dev/null || true
  echo "== Daily stderr =="
  tail -n 40 "$LOG_DIR/daily.err.log" 2>/dev/null || true
  echo "== Weekly stderr =="
  tail -n 40 "$LOG_DIR/weekly.err.log" 2>/dev/null || true
  echo "== Recovery stderr =="
  tail -n 40 "$LOG_DIR/recovery.err.log" 2>/dev/null || true
}

command="${1:-}"

case "$command" in
  install) install_services ;;
  uninstall) uninstall_services ;;
  start) start_bot ;;
  stop) stop_bot ;;
  restart) stop_bot; write_plists; bootstrap_plist "$BOT_PLIST"; kickstart_label "$BOT_LABEL" ;;
  status) status_services ;;
  logs) tail_logs ;;
  doctor) doctor ;;
  privacy|open-privacy) open_privacy_settings ;;
  ""|-h|--help|help) usage ;;
  *) usage; exit 2 ;;
esac
