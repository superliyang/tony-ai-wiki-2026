#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

REMOTE="${KNOWLEDGE_GIT_REMOTE:-origin}"
BRANCH="${KNOWLEDGE_GIT_BRANCH:-$(git rev-parse --abbrev-ref HEAD)}"
MESSAGE="${1:-chore: sync automated knowledge outputs}"

if ! git diff --cached --quiet; then
  echo "[git-sync] staged changes already exist; skip automated checkpoint." >&2
  exit 2
fi

unexpected="$(git status --porcelain --untracked-files=all -- . ':(exclude)00-Agent-Inbox' ':(exclude)90-Agent-System/logs' ':(exclude)90-Agent-System/reports' ':(exclude).obsidian' ':(exclude).p_obsidian')"
if [[ -n "$unexpected" ]]; then
  echo "[git-sync] non-generated worktree changes exist; skip automated checkpoint." >&2
  echo "$unexpected" >&2
  exit 2
fi

git fetch "$REMOTE" "$BRANCH"

if git rev-parse --verify "$REMOTE/$BRANCH" >/dev/null 2>&1; then
  local_head="$(git rev-parse HEAD)"
  remote_head="$(git rev-parse "$REMOTE/$BRANCH")"
  base="$(git merge-base HEAD "$REMOTE/$BRANCH")"
  if [[ "$local_head" == "$base" && "$local_head" != "$remote_head" ]]; then
    echo "[git-sync] local branch is behind $REMOTE/$BRANCH; pull before the next automated run." >&2
    exit 3
  fi
  if [[ "$local_head" != "$base" && "$remote_head" != "$base" ]]; then
    echo "[git-sync] local branch diverged from $REMOTE/$BRANCH; resolve manually." >&2
    exit 4
  fi
fi

# Automated jobs own Inbox and generated reports, not editor state or authored notes.
git add -A -- 00-Agent-Inbox 90-Agent-System/logs 90-Agent-System/reports

if git diff --cached --quiet; then
  echo "[git-sync] no generated changes to checkpoint."
  exit 0
fi

git commit -m "$MESSAGE"
git push "$REMOTE" "$BRANCH"
echo "[git-sync] pushed automated checkpoint to $REMOTE/$BRANCH."
