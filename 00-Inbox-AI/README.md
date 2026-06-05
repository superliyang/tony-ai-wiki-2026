---
title: "AI Inbox Boundary"
created: 2026-06-03
updated: 2026-06-03
status: active
tags:
  - inbox
  - staging
  - ai-first
---

# AI Inbox Boundary

`00-Inbox-AI/` is the staging area for AI-generated, automated, imported, or externally captured material.

## Rule

```text
AI may write staging.
Canonical knowledge requires review.
```

## Allowed Writes

Hermes, ChatGPT, Codex, scripts, and future ingestion tools may write here when the output is not yet reviewed.

Recommended targets:

- `signals/`: raw external evidence and captured signals.
- `candidates/`: AI-selected topics, projects, skills, or sources.
- `learning-tasks/`: Hermes-to-Codex task handoff for deeper learning packages.
- `review-queue/`: items that need Tony's decision.
- `reports/`: daily, weekly, or monthly summaries.
- `agent-memory/`: shared durable memory and memory candidates.
- `hermes/`: Hermes-specific run artifacts.

## Boundary

Do not store secrets, tokens, OAuth state, cookies, account files, or local runtime credentials here.

Do not treat material in this directory as canonical knowledge until it is promoted into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, or `90-Agent-System/`.

## Learning Task Chain

- [[00-Inbox-AI/learning-tasks/README]]
- [[90-Agent-System/workflows/hermes-codex-learning-chain]]
