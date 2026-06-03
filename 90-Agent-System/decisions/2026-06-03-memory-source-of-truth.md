---
title: "Memory Source Of Truth"
created: 2026-06-03
updated: 2026-06-03
status: active
tags:
  - decision
  - memory
  - codex
  - hermes
---

# Memory Source Of Truth

## Context

Codex and Hermes both need durable context about Tony, current learning directions, preferences, negative signals, and operating boundaries.

Hermes also needs a compact runtime `Soul.md` file for recall and scheduled jobs.

## Decision

`00-Inbox-AI/agent-memory/` is the canonical shared memory layer.

Hermes `Soul.md` is a derived projection, not a source of truth.

Hermes may propose memory updates, but canonical memory changes require Tony approval or Codex review.

## Consequences

- Shared memory remains visible, reviewable, and Git-backed.
- Hermes can stay effective without creating a second hidden truth.
- Memory drift is controlled through candidates and review.
- Codex remains the main crystallization agent for durable memory changes.
