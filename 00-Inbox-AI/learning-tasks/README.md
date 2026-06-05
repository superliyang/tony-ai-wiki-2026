---
title: "Learning Tasks"
created: 2026-06-04
updated: 2026-06-04
status: active
tags:
  - inbox
  - learning-tasks
  - hermes
  - codex
---

# Learning Tasks

`learning-tasks/` is the handoff queue between Hermes and Codex.

Hermes discovers, reminds, and creates learning tasks here. Codex turns reviewed tasks into learning packages. Tony reviews the package before it becomes canonical knowledge.

## Folders

| Folder | Owner | Meaning |
|---|---|---|
| `pending/` | Hermes | New learning tasks waiting for Codex or Tony attention |
| `in-progress/` | Codex | Tasks currently being researched and packaged |
| `accepted/` | Codex | Packages accepted or promoted |
| `deferred/` | Tony / Codex | Worth revisiting later |
| `discarded/` | Tony / Codex | Not worth continuing |
| `follow-up/` | Hermes | Spaced review reminders after promotion |
| `templates/` | Codex | Task and package templates |

## Rules

- Hermes writes `pending/` and `follow-up/`.
- Codex writes `in-progress/`, `accepted/`, `deferred/`, and review queue items.
- Canonical knowledge must still go through review before entering `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, or `90-Agent-System/`.

## Workflow

- [[90-Agent-System/workflows/hermes-codex-learning-chain]]
- [[30-Playbooks/知识提升流程]]
- [[00-Inbox-AI/review-queue/README]]
