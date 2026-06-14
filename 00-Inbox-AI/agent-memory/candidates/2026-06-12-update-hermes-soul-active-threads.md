---
title: "Memory Candidate: 更新 hermes-soul.md Active Threads — vault 不再 clean"
created: 2026-06-12
status: pending-review
source: memory-review-scout
type: replace
target: "00-Inbox-AI/agent-memory/projections/hermes-soul.md"
---

# Candidate: 更新 hermes-soul.md Active Threads 区段

## 建议操作

**replace** — 将 `hermes-soul.md` 的 "Active Threads" 区段从：
```
- Vault is clean and ready — staging directories are empty, no legacy tasks carried over
- Focus: build from current state, not replay old review-queue
```
替换为：
```
- learning-tasks backlog: 32+ pending + 5 in-progress (偏高 🔴)
- memory candidates: 5 pending-review（最早 06/05，已 7 天未决策）
- review-queue: pending 内容需清理（6/4-6/6 创建的 15 个任务中有重复项）
- Focus: 优先批量处理 pending candidates 和 backlog 清理，再继续创建新任务
```

## 变更理由

1. **当前状态已过时**: 06/03 clean-slate 后 vault 已积累大量 staging 内容（42+ 项），"clean and ready" 会误导 agent。

2. **实际影响**: agent 读取 hermes-soul.md 的 Active Threads 后可能认为 vault 有余量继续创建新候选，而实际上 backlog 已达到严重偏高水平。这在 06/11-06/12 多次被标记。

3. **与 C3 互补而非重复**: C3 (2026-06-05) 提议全面重新生成 hermes-soul.md（Scout 状态 + Active Threads 等）。本候选只聚焦 Active Threads 这一项即时修复——即使 C3 等待 Tony 全局审核，这项至少应先更新以避免 agent 继续误判。

4. **Operational safety**: projection 的 Active Threads 充当 agent 的"当前状态快速摘要"，保留过时信息相当于让 agent 基于错误前提做决策。

## 关联发现

memory-review-2026-06-12 的 F1

## 备注

- 与 pending candidate C3 不冲突——本候选是 C3 的子集，可作为快速修复先行合并
- 接受后应同步更新到 Hermes 的 runtime context（如 system prompt 中的 Active Threads）
