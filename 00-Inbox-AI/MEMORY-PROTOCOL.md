---
title: "AI Shared Memory Protocol"
created: 2026-06-03
updated: 2026-06-03
status: active
tags:
  - ai-first
  - memory
  - protocol
---

# AI Shared Memory Protocol

This file defines how Codex, Hermes, ChatGPT Desktop, Obsidian, GitHub, and future agents share durable memory.

## Source Of Truth

```text
00-Inbox-AI/agent-memory/ is the canonical shared memory layer.
Agent-specific memories are projections.
Memory candidates require review.
```

## Memory Flow

```text
Tony decision or durable preference
-> Codex writes canonical shared memory
-> Hermes syncs shared memory into Soul.md
-> Hermes observations become memory candidates
-> Tony/Codex review candidates
-> accepted items update canonical shared memory
```

## Canonical Shared Memory

Use:

- `00-Inbox-AI/agent-memory/profile.md`
- `00-Inbox-AI/agent-memory/preferences.md`
- `00-Inbox-AI/agent-memory/learning-themes.md`
- `00-Inbox-AI/agent-memory/negative-signals.md`
- `00-Inbox-AI/agent-memory/memory-changelog.md`
- `00-Inbox-AI/agent-memory/candidates/`
- `00-Inbox-AI/agent-memory/projections/`

## Hermes Projection

Hermes may maintain a local `Soul.md`, but it is a derived runtime projection.

It must not overwrite canonical shared memory automatically.

The reviewable projection copy lives at:

```text
00-Inbox-AI/agent-memory/projections/hermes-soul.md
```

## Review Triggers

Update canonical memory when Tony says:

- "记住这个"
- "以后按这个来"
- "这是我的偏好"
- "这很重要"

If Hermes infers a preference without explicit confirmation, write a candidate instead of changing canonical memory.
