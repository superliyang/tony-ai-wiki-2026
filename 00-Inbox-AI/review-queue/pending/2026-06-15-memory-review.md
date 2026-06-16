---
title: "Memory Review 2026-06-15"
created: 2026-06-15
status: pending-review
source: memory-review-scout-v1
tags: [memory-review, internal, hermes]
---

# Memory Review Candidates — 2026-06-15

## Candidate 1: 处理积压候选 `2026-06-12-memory-review.md`
- Type: review-queue backlog
- Signal: pending 72.0h，超过 72h 阈值
- Title: Memory Review 2026-06-12

## Candidate 2: 处理积压候选 `2026-06-11-memory-review.md`
- Type: review-queue backlog
- Signal: pending 96.0h，超过 72h 阈值
- Title: Memory Review 2026-06-11

## Candidate 3: 处理积压候选 `2026-06-10-memory-review.md`
- Type: review-queue backlog
- Signal: pending 120.0h，超过 72h 阈值
- Title: Memory Review 2026-06-10

## Candidate 4: 处理积压候选 `2026-06-09-memory-review.md`
- Type: review-queue backlog
- Signal: pending 144.0h，超过 72h 阈值
- Title: Memory Review 2026-06-09

## Candidate 5: 处理积压候选 `2026-06-08-memory-review.md`
- Type: review-queue backlog
- Signal: pending 168.0h，超过 72h 阈值
- Title: Memory Review 2026-06-08

## Candidate 6: 处理积压候选 `2026-06-07-weekly-synthesis-actions.md`
- Type: review-queue backlog
- Signal: pending 182.8h，超过 72h 阈值
- Title: Hermes 周度综合 — 需 Tony 关注事项

## Candidate 7: 处理积压候选 `2026-06-07-memory-review.md`
- Type: review-queue backlog
- Signal: pending 192.0h，超过 72h 阈值
- Title: Memory Review 2026-06-07

## Candidate 8: 处理积压候选 `2026-06-06-memory-review.md`
- Type: review-queue backlog
- Signal: pending 216.0h，超过 72h 阈值
- Title: Memory Review 2026-06-06

## Candidate 9: 处理积压候选 `2026-06-05-memory-review.md`
- Type: review-queue backlog
- Signal: pending 240.0h，超过 72h 阈值
- Title: Memory Review 2026-06-05

## Candidate 10: 处理积压候选 `2026-06-04-memory-review.md`
- Type: review-queue backlog
- Signal: pending 264.0h，超过 72h 阈值
- Title: Memory Review 2026-06-04

## Candidate 11: 处理积压候选 `2026-06-03-memory-review.md`
- Type: review-queue backlog
- Signal: pending 288.0h，超过 72h 阈值
- Title: Memory Review 2026-06-03

## Candidate 12: 无丢弃记录
- Type: no_discard
- Detail: 已接受 7 个候选，但 discarded/ 和 deferred/ 均为空。是不感兴趣的内容没进来，还是没行使判断？

## Candidate 13: agent-memory 自洽性
- Type: self_consistency
- Detail: - 角色冲突：preferences 说 Hermes 负责 recall/scout，negative-signals 禁止 Hermes 写 canonical 笔记
- 重复主题：Active 和 Candidate 同时包含 Agent Memory 相关内容
- 规则矛盾：preferences 允许 Hermes 做 recall，negative-signals 限制 Hermes 

## Candidate 14: 自洽性 — 角色冲突：preferences 说 Hermes 负责 recall/scout，negative-signals 禁
- Type: self-consistency
- Detail: 角色冲突：preferences 说 Hermes 负责 recall/scout，negative-signals 禁止 Hermes 写 canonical 笔记

## Candidate 15: 自洽性 — 重复主题：Active 和 Candidate 同时包含 Agent Memory 相关内容
- Type: self-consistency
- Detail: 重复主题：Active 和 Candidate 同时包含 Agent Memory 相关内容

## Candidate 16: 自洽性 — 规则矛盾：preferences 允许 Hermes 做 recall，negative-signals 限制 Herm
- Type: self-consistency
- Detail: 规则矛盾：preferences 允许 Hermes 做 recall，negative-signals 限制 Hermes 写笔记

## 判断指令

```
清理 pending      → 移除积压候选
跟进 memory N     → 触发 Codex 结晶
忽略 memory N     → 跳过本轮
修复              → 处理自洽性问题
```
