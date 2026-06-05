---
title: "Hermes Cron Matrix"
created: 2026-06-04
updated: 2026-06-04
status: active
tags:
  - hermes
  - cron
  - learning-automation
---

# Hermes Cron Matrix

This is the split-task schedule for Hermes. It is intentionally not one giant cron.

## Task Groups

| Group | Purpose | Cadence | Writes |
|---|---|---|---|
| Core Radar | Track important external changes | 3-5 times/day | `00-Inbox-AI/hermes/curated-scout/`, `00-Inbox-AI/signals/` |
| Topic Scout | Watch high-priority domains | daily or 2-3 times/week | `00-Inbox-AI/candidates/` |
| Growth Track | Build Tony's product, industry, management, EQ, and business judgment | weekdays | `00-Inbox-AI/learning-tasks/pending/` |
| Learning Task Generator | Convert valuable signals into Codex-ready tasks | daily | `00-Inbox-AI/learning-tasks/pending/` |
| Follow-Up Review | Remind Tony to revisit accepted packages | daily | `00-Inbox-AI/learning-tasks/follow-up/` |
| Memory Review | Detect durable preference or context changes | daily | `00-Inbox-AI/hermes/memory-review/`, `00-Inbox-AI/agent-memory/candidates/` |
| Weekly Synthesis | Summarize what happened and what to do next | weekly | `00-Inbox-AI/reports/`, `00-Inbox-AI/review-queue/pending/` |

## Proposed Jobs

| Job ID | Frequency | Role | Output Contract |
|---|---|---|---|
| `hermes-core-radar-morning` | Daily morning | Curated AI/system radar | One digest, max 12 items, max 3 learning-task suggestions |
| `hermes-core-radar-afternoon` | Daily afternoon | Catch late updates and GitHub/project changes | One short update, only high-signal deltas |
| `hermes-memory-review` | Daily | Review memory consistency and candidates | Memory review report and candidate items only |
| `hermes-growth-industry` | Monday | One industry a day/week slice | One learning task about an industry and business model |
| `hermes-growth-product` | Tuesday | Product thinking | One product principle, case, anti-pattern, practice prompt |
| `hermes-growth-management` | Wednesday | Management and org capability | One management learning task with checklist |
| `hermes-growth-eq-communication` | Thursday | EQ, communication, influence | One applied communication task |
| `hermes-growth-business` | Friday | Business, strategy, finance, operations | One business judgment task |
| `hermes-learning-task-generator` | Daily evening | Convert strong candidates into tasks | 0-3 Codex-ready learning tasks |
| `hermes-follow-up-review` | Daily evening | Spaced review reminders | Due reminder items only |
| `hermes-weekly-synthesis` | Sunday | Weekly synthesis and next-week planning | Weekly report plus top 5 decisions |

## Growth Track Output Shape

Every growth task should answer:

```text
Today's theme:
Why it matters:
3 core concepts:
1 real case:
1 counterintuitive point:
How it connects to Tony:
Practice action:
Should Codex go deep:
```

## Noise Controls

- A job may write "no high-signal update" instead of generating filler.
- Each growth job creates at most one learning task.
- The daily task generator creates at most three tasks.
- Hermes should not create duplicate tasks if a similar pending task exists.
- Hermes should prefer `watch` over `promote` when confidence is weak.

## Codex Handoff

Codex consumes:

- `00-Inbox-AI/learning-tasks/pending/`
- [[90-Agent-System/workflows/hermes-codex-learning-chain]]

Codex should process at most one high-priority task per scheduled run until the queue quality is proven.
