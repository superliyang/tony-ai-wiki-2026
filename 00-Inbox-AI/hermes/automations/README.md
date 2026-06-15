---
title: "Hermes Automations"
created: 2026-06-04
updated: 2026-06-04
status: active
tags:
  - hermes
  - automations
  - cron
---

# Hermes Automations

This directory documents the scheduled Hermes jobs for Tony's AI First vault.

The design principle is:

```text
Split by purpose, frequency, and output contract.
Do not put radar, growth learning, review, and reminders into one job.
```

## Current Matrix

- [[00-Inbox-AI/hermes/automations/hermes-cron-matrix]]
- `00-Inbox-AI/hermes/automations/hermes-cron-matrix.yaml`

## Output Areas

| Output | Path |
|---|---|
| Raw discovery and summaries | `00-Inbox-AI/hermes/` |
| Signals | `00-Inbox-AI/signals/` |
| Candidates | `00-Inbox-AI/candidates/` |
| Task intents | `00-Inbox-AI/task-intents/pending/` |
| Project companion candidates | `00-Inbox-AI/project-companion/` |
| Learning tasks | `00-Inbox-AI/learning-tasks/pending/` |
| Follow-up reminders | `00-Inbox-AI/learning-tasks/follow-up/` |
| Review items | `00-Inbox-AI/review-queue/pending/` |
| Memory candidates | `00-Inbox-AI/agent-memory/candidates/` |

## Rule

Hermes first classifies Tony's task intent, then creates tasks and reminders. Codex creates learning packages, crystallized notes, project updates, and publishable outputs. Tony approves canonical promotion.
