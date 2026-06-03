---
title: "Codex Hermes Memory Sync"
created: 2026-06-03
updated: 2026-06-03
status: active
tags:
  - workflow
  - memory
  - codex
  - hermes
---

# Codex Hermes Memory Sync

## Principle

```text
Shared Agent Memory is the source of truth.
Hermes Soul.md is a runtime projection.
Memory candidates require review before becoming canonical.
```

## Memory Types

| Type | Path | Owner | Trust |
|---|---|---|---|
| Canonical shared memory | `00-Inbox-AI/agent-memory/*.md` | Codex after Tony approval | Source of truth |
| Hermes projection | `00-Inbox-AI/agent-memory/projections/hermes-soul.md` and Hermes local `Soul.md` | Hermes sync job | Derived context |
| Memory candidates | `00-Inbox-AI/agent-memory/candidates/` or `00-Inbox-AI/review-queue/pending/` | Hermes, Codex, ChatGPT | Needs review |
| Recent working context | `00-Home/当前主线.md` | Codex or reviewed automation | Short-term orientation |

## Sync Direction

```text
Codex -> canonical memory
canonical memory -> Hermes Soul projection
Hermes observations -> memory candidates
Tony/Codex review -> canonical memory
```

## Codex Responsibilities

- Write durable memory when Tony explicitly says something should be remembered.
- Update `memory-changelog.md` when canonical memory changes.
- Keep memory concise, reviewable, and free of secrets.
- Treat Hermes proposals as candidates, not automatic truth.

## Hermes Responsibilities

- Read shared memory before scheduled scouting or review.
- Generate or refresh its Soul projection from shared memory.
- Write new inferred preferences as candidates.
- Avoid rewriting canonical shared memory directly.

## Soul Projection Contents

Hermes `Soul.md` should contain:

- identity and role;
- Tony profile summary;
- current learning themes;
- recommendation preferences;
- negative signals;
- tool boundaries;
- active threads from `00-Home/当前主线.md`;
- do-not-do rules.

## Review Trigger

Update canonical shared memory when Tony says:

- "记住这个"
- "以后按这个来"
- "这是我的偏好"
- "这很重要"

Architecture or boundary changes should also update `00-Home/当前主线.md` and a decision record under `90-Agent-System/decisions/`.
