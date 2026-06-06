---
title: "Memory Candidate: 重新生成 hermes-soul.md projection"
created: 2026-06-05
status: pending-review
source: memory-review-scout
type: replace
target: "00-Inbox-AI/agent-memory/projections/hermes-soul.md"
---

# Candidate: 重新生成 Hermes Soul Projection

## 建议操作

**replace** — 从 canonical memory + 实际运行时状态重新生成 `hermes-soul.md`

## 变更理由

当前的 `hermes-soul.md` (最后更新 2026-06-03) 存在以下过期/不一致内容：

1. **Scout 状态过期**: 
   - 声称 `hourly-ai-scout` "currently paused" → 实际当前 system prompt 中它正常运行（每小时）
   - 声称 `curated-ai-scout` 以 cron `0 9,15,21 * * *` 运行 → 当前实际 cron job 名是 `daily-ai-learning-scout`
   - 声称 "⚠️ curated-ai-scout 缺 LLM API key" → 6/4-6/5 的 curated-scout 产出目录有完整产出，说明 API key 问题已解决或不再阻塞

2. **Canonical memory 已更新但 projection 未同步**:
   - `memory-changelog.md` 新增了 2026-06-03 的 3 条记录（write boundary / language preference / clean slate）但 projection 未体现
   - `hermes-soul.md` 中的 "Active Threads" 未反映当前 vault 的实际状态

3. **Vault 路径引用**:
   - 虽然 vault 路径已更新，但 projection 的 "Dependencies" 引用列表可能需要验证所有 `wiki/` → `10-Knowledge/` 的映射

## 建议的新内容方向

重新生成时应：
- 从 canonical 5 个文件重新派生
- 更新 Scout 工具状态为实际运行时状态
- 移除或确认 LLM API key 警告
- 同步 memory-changelog 的最新条目
- 保持 "Active Threads" 与当前 vault 状态对齐

## 关联发现

memory-review-2026-06-05 的 F1
