---
title: "Agent Memory"
created: 2026-06-03
updated: 2026-06-03
status: active
tags:
  - agent-memory
  - ai-first
  - protocol
---

# Agent Memory

This directory is the canonical shared memory layer for Codex, Hermes, ChatGPT, Cursor, Claude Code, and future agents.

## Rule

```text
Shared memory is the source of truth.
Agent-specific memories are projections.
Memory candidates require review.
```

## Files

- `profile.md`: durable profile of Tony.
- `preferences.md`: output and recommendation preferences.
- `learning-themes.md`: current learning directions.
- `negative-signals.md`: what to avoid or down-rank.
- `user-profile-and-ai-cognitive-system.md`: fuller system memory.
- `memory-changelog.md`: canonical memory change log.
- `candidates/`: proposed memory updates.
- `projections/`: derived agent-specific memory snapshots.

## Related

- [[90-Agent-System/workflows/memory-sync]]
- [[90-Agent-System/decisions/2026-06-03-memory-source-of-truth]]
