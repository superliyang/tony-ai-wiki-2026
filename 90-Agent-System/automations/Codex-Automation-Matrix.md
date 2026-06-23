---
title: "Codex Automation Matrix"
created: 2026-06-14
updated: 2026-06-16
status: active
tags:
  - codex
  - automation
  - ai-first
---

# Codex Automation Matrix

这页记录 Codex 侧正在运行或应当被关注的自动化任务。

## Active Jobs

| Job | Type | Schedule | Output | Boundary |
|---|---|---:|---|---|
| Daily Codex Learning Task Gate | heartbeat | 09:15 daily | working vault `20-Review-Queue/pending/` | 只处理 learning task gate，不替代人工判断 |
| Codex Request Quality Gate | cron | 09:25 daily | working vault `40-Logs/quality-reports/` | 只检查请求质量，不移动、不发布、不提升 |
| Codex Request Consumer | heartbeat | 09:35 daily | working vault review item updates | 每次最多处理一个请求 |
| Review Queue Triage | cron | 09:50 daily | working vault `40-Logs/review-queue-triage/` | 只生成决策面板，不 accept/discard |
| Knowledge Gardener Weekly | cron | 10:30 Sunday | working vault `40-Logs/gardener/weekly/` | 只提出清理和提升批次，不直接改 canonical notes |

## Portable Export

- [[90-Agent-System/automations/codex-automation-export.yaml]]

## Historical Dry Run Reports

- [[00-Inbox-AI/codex-requests/quality-reports/2026-06-14-quality-gate-dry-run]]
- [[00-Inbox-AI/review-queue/triage/2026-06-14-review-queue-triage-dry-run]]
- [[00-Inbox-AI/gardener/weekly/2026-06-14-knowledge-gardener-dry-run]]

## Intended Flow

```text
Hermes produces requests
  -> Codex Request Quality Gate checks request quality
  -> Codex Request Consumer handles one approved-sized request
  -> Review Queue Triage keeps Tony's decision surface small
  -> Knowledge Gardener Weekly protects the vault from drift
```

## Operating Rules

- Canonical notes still require review before promotion.
- Feishu publishing uses `output-feishu/` as the clean intermediate layer.
- Cron jobs are workspace-level background jobs.
- Heartbeat jobs are conversation-attached follow-ups and should stay few.
