---
title: "Memory Review 2026-06-06"
created: 2026-06-06
status: pending-review
source: memory-review-scout-v1
tags: [memory-review, internal, hermes]
---

# Memory Review Candidates — 2026-06-06

## Candidate 1: 决策停滞 — 7 天未做任何判断
- Type: idle_judge
- Detail: pending 积压 6 件，但近期无 accepted/discarded。建议花 2 分钟扫一遍 review-queue。

## 判断指令

```
清理 pending      → 移除积压候选
跟进 memory N     → 触发 Codex 结晶
忽略 memory N     → 跳过本轮
修复              → 处理自洽性问题
```
