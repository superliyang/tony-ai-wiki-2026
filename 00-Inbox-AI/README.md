---
title: "AI Inbox Boundary"
created: 2026-06-03
updated: 2026-06-14
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
- `task-intents/`: Tony natural-language requests classified by intent before becoming Codex work.
- `learning-tasks/`: Hermes-to-Codex task handoff for deeper learning packages.
- `codex-requests/`: Hermes-to-Codex request queue for learning, map maintenance, project companion, promotion, and Feishu publishing work.
- `gardener/`: knowledge hygiene reports and cleanup proposals.
- `project-companion/`: project candidates, blockers, next-action drafts, and project continuity notes.
- `feishu-publishing/`: Feishu publication records, pending operations, and failed attempts. Publish-ready content lives in `output-feishu/`.
- `review-queue/`: items that need Tony's decision.
- `reports/`: daily, weekly, or monthly summaries.
- `agent-memory/`: shared durable memory and memory candidates.
- `hermes/`: Hermes-specific run artifacts.

## Boundary

Do not store secrets, tokens, OAuth state, cookies, account files, or local runtime credentials here.

Do not treat material in this directory as canonical knowledge until it is promoted into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, or `90-Agent-System/`.

## Learning Task Chain

- [[00-Inbox-AI/task-intents/README]]
- [[00-Inbox-AI/learning-tasks/README]]
- [[00-Inbox-AI/codex-requests/README]]
- [[90-Agent-System/workflows/hermes-codex-learning-chain]]
- [[90-Agent-System/workflows/hermes-codex-feishu-pipeline]]

## Intent And Feedback Loop

- [[00-Home/Tony-Command-Center]]
- [[90-Agent-System/workflows/task-intent-routing]]
- [[00-Inbox-AI/feedback-log/README]]

## Project Companion Chain

- [[00-Inbox-AI/project-companion/README]]
- [[90-Agent-System/workflows/project-companion]]

## Knowledge Hygiene

- [[90-Agent-System/workflows/knowledge-gardener-weekly]]
- [[90-Agent-System/workflows/codex-request-quality-gate]]
- [[90-Agent-System/workflows/review-queue-triage]]

## Feishu Publishing Chain

- [[00-Inbox-AI/feishu-publishing/README]]
- [[90-Agent-System/workflows/feishu-publishing]]
- [[output-feishu/README]]
