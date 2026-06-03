# Workflow Reference

## Update Checklist

1. Identify the correct area and layer.
2. Update the note itself.
3. Update the nearest index or map if topology changed.
4. Update `学习进度.md` and `恢复笔记.md` when the learning path changed.
5. Run `check_obsidian_wikilinks.py` on touched areas.
6. Run `safe_git_checkpoint.sh` if the user wants a checkpoint or the task is running under automation.

## Commit Message Style

Prefer short, topical messages:

- `Add AI coding agent systems comparison`
- `Refactor AI learning systems topology`
- `Expand international payments expert system`
- `Update AI engineering agent workflow notes`

## Git Safety Rules

- Do not force-push automatically.
- Exclude `.obsidian` from automatic checkpoints.
- If remote is behind or diverged, stop and report instead of trying to recover automatically.
- Prefer one meaningful checkpoint after a coherent batch of note updates.
