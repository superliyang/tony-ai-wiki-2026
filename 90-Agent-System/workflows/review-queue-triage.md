---
title: "Review Queue Triage"
created: 2026-06-14
updated: 2026-06-16
status: active
tags:
  - workflow
  - review-queue
  - triage
  - automation
---

# Review Queue Triage

这个 workflow 用来把 working vault `20-Review-Queue/pending/` 变成 Tony 能快速判断的小面板。

## Goal

```text
pending review items
  -> daily triage
  -> top decisions for Tony
```

Triage 不替 Tony 做最终判断，只降低阅读成本。

## Reads

- `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/pending/`
- `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/20-Review-Queue/accepted/`
- `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/10-Generated/learning-tasks/`
- `90-Agent-System/当前状态.md`

## Writes

- `/Users/tony/Vault/tony-wiki-space/tony-ai-working-vault/40-Logs/review-queue-triage/`

## Triage Buckets

| Bucket | Meaning |
|---|---|
| `decide-now` | 建议 Tony 今天看 |
| `batch-later` | 可以合并批处理 |
| `stale` | 长期 pending，需要归档、合并或重写 |
| `duplicate` | 和已有 accepted / pending 重复 |
| `needs-codex-request` | 应转成 Codex Request |
| `discard-candidate` | 可能可以丢弃 |

## Output Shape

```text
date:
pending_count:
top_3:
stale_items:
recommended_actions:
```

## Guardrails

- 不移动 review items；
- 不替 Tony 标记 accepted/discarded；
- 可以建议，但不直接改变判断状态；
- 每次最多推荐 3 个 Tony 需要看的项目。
