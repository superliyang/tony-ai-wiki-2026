---
title: "Review Queue Triage"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - workflow
  - review-queue
  - triage
  - automation
---

# Review Queue Triage

这个 workflow 用来把 `review-queue/pending/` 变成 Tony 能快速判断的小面板。

## Goal

```text
pending review items
  -> daily triage
  -> top decisions for Tony
```

Triage 不替 Tony 做最终判断，只降低阅读成本。

## Reads

- `00-Inbox-AI/review-queue/pending/`
- `00-Inbox-AI/review-queue/accepted/`
- `00-Inbox-AI/learning-tasks/`
- `00-Inbox-AI/codex-requests/`
- `90-Agent-System/当前状态.md`

## Writes

- `00-Inbox-AI/review-queue/triage/`

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

