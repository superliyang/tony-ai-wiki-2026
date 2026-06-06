---
title: "Memory Review — 2026-06-05"
created: 2026-06-05
status: complete
tags:
  - memory-review
  - hermes
---

# 🧠 Memory Review Scout — 2026-06-05

> 扫描范围：`00-Inbox-AI/agent-memory/` 全量 6 个 canonical 文件 + 1 个 projection
> 对照：`MEMORY-PROTOCOL.md` + Hermes 当前 system prompt + 最近对话 (session_search)
> 产出：3 个 memory candidate

---

## 一、一致性检测

### ✅ 通过项

| 检查项 | 结果 |
|---|---|
| Canonical 文件内部一致性 | ✅ profile ↔ preferences ↔ learning-themes ↔ negative-signals ↔ user-profile 互不冲突 |
| Memory sync state 最新 | ✅ 2026-06-05 15:00 UTC 运行正常，hash 匹配 |
| Vault 路径引用正确 | ✅ 全部指向 `/Users/tony/Vault/tony-ai-wiki-2026` |
| Hermes write boundary 明确 | ✅ 所有文件记录了 "Hermes 写 candidates/projections，不直接写 canonical" |
| 语言偏好一致 | ✅ 所有文件统一：中文 + 保留英文术语 |

### ⚠️ 发现 3 个需关注项

---

## 二、发现详情

### F1: `hermes-soul.md` projection 过期且 Scout 状态与运行时不一致

**Projection 声称** (最后更新 2026-06-03):
- `curated-ai-scout`: cron `0 9,15,21 * * *` — active
- `hourly-ai-scout`: — "currently paused"
- `memory-sync-scout`: cron `0 8 * * *` — active
- ⚠️ "curated-ai-scout 缺 LLM API key"

**实际运行时** (当前 system prompt + cron 产出):
- `hourly-ai-scout` 在 system prompt 中列出为活跃 cron job（每小时）
- `daily-ai-learning-scout` 在 system prompt 中列出为活跃 cron job（08:30 daily）
- `curated-ai-scout` 产出目录 (`curated-scout/`) 有 6/4-6/5 的实际产出（说明 LLM API key 问题可能已解决）
- `memory-sync-scout` 通过 `memory-sync-state.json` 确认每日正常运行

**冲突**: projection 说 `hourly-ai-scout` paused → 实际在运行；projection 列出 `curated-ai-scout` 为 cron job → 实际 system prompt 列的是 `daily-ai-learning-scout`。

**建议**: 重新从 canonical memory + 实际 runtime state 生成 hermes-soul.md。

### F2: 新学习领域「广告投放」未反映到 learning-themes.md

**最近对话** (2026-06-05 cli session `mq0z70s5fdqiyn`):
- Tony 用「领域专家感学习法」对「广告投放」领域做了完整深钻
- 产出：领域全貌图 + 10 问深答 + 一页复习卡 + 新手误区 vs 高手权衡 + 专题总览 MOC
- 5 个产出文件已写入 vault
- Tony 确认"方向没问题"

**当前 `learning-themes.md`** 未提及广告投放/advertising technology 作为活跃学习方向。

**建议**: 添加「广告投放/advertising technology」到 learning-themes 或 candidate themes。

### F3: Scout cron job 命名与实际运行不一致

**规范文件中的命名**:
- `hermes-soul.md`: `curated-ai-scout`, `memory-sync-scout`
- `user-profile-and-ai-cognitive-system.md`: `curated-ai-scout` (外部) + `memory-review-scout` (内部)

**System prompt 中的实际 cron job 名**:
- `hourly-ai-scout`
- `daily-ai-learning-scout`

在 `user-profile-and-ai-cognitive-system.md` 中提到的两种 scout loop（`curated-ai-scout` + `memory-review-scout`）与 system prompt 中列出的实际 cron job 名不一致。这可能导致候选推荐混乱。

---

## 三、产出汇总

| # | 文件 | 行数 | 状态 |
|---|---|---|---|
| profile.md | 37 | ✅ 一致 |
| preferences.md | 50 | ✅ 一致 |
| learning-themes.md | 38 | ⚠️ 缺失广告投放 |
| negative-signals.md | 29 | ✅ 一致 |
| user-profile-and-ai-cognitive-system.md | 243 | ⚠️ Scout 命名不一致 |
| memory-changelog.md | 40 | ✅ 一致 |
| hermes-soul.md (projection) | 118 | ❌ 过期，需要重新生成 |
| memory-sync-state.json | 117 | ✅ 最新 |

**Memory candidates 产出**: 3 个

---

*Hermes memory-review-scout | 2026-06-05 | 无自动化修改*
