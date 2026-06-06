---
title: "Memory Candidate: 对齐 Scout cron job 命名"
created: 2026-06-05
status: pending-review
source: memory-review-scout
type: replace
target: "00-Inbox-AI/agent-memory/user-profile-and-ai-cognitive-system.md"
---

# Candidate: 对齐 Scout cron job 命名与实际运行状态

## 建议操作

**replace** — 在 `user-profile-and-ai-cognitive-system.md` 和 `hermes-soul.md` 中统一 Scout cron job 命名，使其与实际运行时一致。

## 变更理由

当前存在 3 套不同的 Scout 命名：

| 来源 | 外部 Scout 名 | 内部 Scout 名 |
|---|---|---|
| `user-profile-and-ai-cognitive-system.md` (canonical) | `curated-ai-scout` | `memory-review-scout` |
| `hermes-soul.md` (projection) | `curated-ai-scout` | `memory-sync-scout` |
| System prompt (实际 cron) | `hourly-ai-scout` / `daily-ai-learning-scout` | (无独立 cron job 名；通过 memory_sync.py 运行) |

这导致：
1. Agent 读 canonical memory 时看到 `curated-ai-scout`，但运行时实际触发的是 `daily-ai-learning-scout`
2. `memory-review-scout` vs `memory-sync-scout` 指同一件事但用了不同名字
3. `hourly-ai-scout` 在 canonical memory 中完全没有被记录

## 建议对齐方案

以下统一命名供参考（需要 Tony 确认）：

| 用途 | 统一命名 | 说明 |
|---|---|---|
| 外部信号 Scout（高频） | `hourly-ai-scout` | 已在 system prompt 中运行 |
| 外部信号 Scout（策展） | `daily-ai-curated-scout` | 对应 system prompt 中的 `daily-ai-learning-scout` |
| 内部记忆审查 | `memory-review-scout` | 已在 canonical memory 中使用 |

在 `user-profile-and-ai-cognitive-system.md` 的 "Two Scout loops" 部分更新命名，并在 `hermes-soul.md` 重新生成时同步。

## 关联发现

memory-review-2026-06-05 的 F3
