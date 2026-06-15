---
title: "Knowledge Gardener Weekly"
created: 2026-06-14
updated: 2026-06-14
status: active
tags:
  - workflow
  - knowledge-gardener
  - vault-health
  - automation
---

# Knowledge Gardener Weekly

这个 workflow 是 Tony AI Wiki 的知识卫生周检。

## Goal

```text
scan inbox / maps / queues / domains
  -> find clutter and stale surfaces
  -> propose small cleanup batches
```

Knowledge Gardener 不追热点，不做深研究，只维护知识系统的可读性和可复用性。

## Reads

- `00-Home/`
- `10-Knowledge/`
- `20-Maps/`
- `30-Playbooks/`
- `40-Projects/`
- `00-Inbox-AI/`
- `90-Agent-System/当前状态.md`

## Writes

- `00-Inbox-AI/gardener/weekly/`

## Weekly Checks

- `00-Inbox-AI/` 是否堆积；
- `review-queue/pending/` 是否停滞；
- `codex-requests/pending/` 是否有坏 request；
- `20-Maps/` 是否有过期入口；
- 哪些领域还是 seed；
- 哪些 done request 有输出但没有挂到地图；
- 哪些飞书输出应该回链到 source note；
- 哪些旧库入口值得下一轮提升。

## Output Shape

```text
week:
vault_health:
top_clutter:
broken_or_confusing_entries:
promotion_candidates:
map_updates_needed:
recommended_cleanup_batch:
```

## Guardrails

- 默认只写周检报告；
- 不批量移动旧库内容；
- 不自动删除；
- 不直接改 canonical note，除非 Tony 明确要求；
- 每周只建议一个小批次，避免把整理本身变成负担。

