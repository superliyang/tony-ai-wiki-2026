#!/usr/bin/env bash
set -euo pipefail

REPO=""
REMOTE="origin"
BRANCH=""
MESSAGE=""
DRY_RUN=0
NO_PUSH=0
NO_FETCH=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo)
      REPO="$2"
      shift 2
      ;;
    --remote)
      REMOTE="$2"
      shift 2
      ;;
    --branch)
      BRANCH="$2"
      shift 2
      ;;
    --message)
      MESSAGE="$2"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    --no-push)
      NO_PUSH=1
      shift
      ;;
    --no-fetch)
      NO_FETCH=1
      shift
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

if [[ -z "$REPO" ]]; then
  echo "--repo is required" >&2
  exit 2
fi

cd "$REPO"
git rev-parse --is-inside-work-tree >/dev/null

if [[ -z "$BRANCH" ]]; then
  BRANCH="$(git rev-parse --abbrev-ref HEAD)"
fi

if [[ "$NO_FETCH" -eq 0 ]]; then
  git fetch "$REMOTE" "$BRANCH"
fi

if git rev-parse --verify "$REMOTE/$BRANCH" >/dev/null 2>&1; then
  LOCAL="$(git rev-parse HEAD)"
  REMOTE_HEAD="$(git rev-parse "$REMOTE/$BRANCH")"
  BASE="$(git merge-base HEAD "$REMOTE/$BRANCH")"

  if [[ "$LOCAL" == "$REMOTE_HEAD" ]]; then
    :
  elif [[ "$LOCAL" == "$BASE" ]]; then
    echo "Branch is behind $REMOTE/$BRANCH. Pull or rebase manually before checkpointing." >&2
    exit 3
  elif [[ "$REMOTE_HEAD" == "$BASE" ]]; then
    :
  else
    echo "Branch has diverged from $REMOTE/$BRANCH. Resolve manually before checkpointing." >&2
    exit 4
  fi
fi

git add -A
if [[ -e .obsidian || -d .obsidian ]]; then
  git restore --staged .obsidian >/dev/null 2>&1 || true
fi

if git diff --cached --quiet; then
  echo "No meaningful staged changes."
  exit 0
fi

if [[ -z "$MESSAGE" ]]; then
  MESSAGE="Vault checkpoint $(date '+%Y-%m-%d %H:%M')"
fi

if [[ "$DRY_RUN" -eq 1 ]]; then
  echo "Dry run only. Proposed commit: $MESSAGE"
  git diff --cached --stat
  git reset --quiet
  exit 0
fi

git commit -m "$MESSAGE"

if [[ "$NO_PUSH" -eq 0 ]]; then
  git push "$REMOTE" "$BRANCH"
fi
