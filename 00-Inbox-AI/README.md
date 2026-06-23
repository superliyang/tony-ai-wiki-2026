---
title: "AI Inbox Boundary"
created: 2026-06-03
updated: 2026-06-16
status: frozen
tags:
  - inbox
  - staging
  - ai-first
---

# AI Inbox Boundary

`00-Inbox-AI/` is the historical staging area for AI-generated, automated, imported, or externally captured material.

> [!important] 2026-06-16 boundary update
> This directory is now frozen for new Hermes output. Hermes writes to the working vault:
> `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/`.
>
> Keep existing files here as historical evidence until they are reviewed, promoted, archived, or discarded through [[90-Agent-System/plans/main-vault-cleanup-plan]].

## Rule

```text
Historical AI staging stays here.
New Hermes material goes to the working vault.
Canonical knowledge requires review before promotion.
```

## Allowed Writes

Avoid new automated writes here.

Allowed exceptions:

- Tony / Codex may update README, maps, migration notes, or review decisions.
- Codex may promote, archive, or summarize historical files in bounded reviewed batches.
- Manual emergency capture is allowed only when the working vault is unavailable; add a note explaining why.

For new unreviewed material, use:

- Hermes automatic output: `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/10-Generated/`
- Hermes review queue: `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/`
- Manual material: `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/00-Human-Inbox/`

Historical targets in this directory:

- `signals/`: raw external evidence and captured signals.
- `candidates/`: AI-selected topics, projects, skills, or sources.
- `task-intents/`: Tony natural-language requests classified by intent before becoming Codex work.
- `learning-tasks/`: old Hermes-to-Codex task handoff.
- `codex-requests/`: old Hermes-to-Codex request queue.
- `gardener/`: knowledge hygiene reports and cleanup proposals.
- `project-companion/`: old project candidates, blockers, next-action drafts, and project continuity notes.
- `feishu-publishing/`: Feishu publication records, pending operations, and failed attempts.
- `review-queue/`: old items that need Tony's decision.
- `reports/`: daily, weekly, or monthly summaries.
- `agent-memory/`: old shared durable memory and memory candidates.
- `hermes/`: old Hermes-specific run artifacts.

## Boundary

Do not store secrets, tokens, OAuth state, cookies, account files, or local runtime credentials here.

Do not treat material in this directory as canonical knowledge until it is promoted into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, or `90-Agent-System/`.

Do not use this directory as the active Hermes memory or task queue after 2026-06-16.

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
