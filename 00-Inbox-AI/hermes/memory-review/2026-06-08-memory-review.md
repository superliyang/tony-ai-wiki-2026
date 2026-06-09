---
title: "Memory Review Scout — 2026-06-08"
created: 2026-06-08
status: complete
source: memory-review-scout
tags:
  - memory-review
  - hermes
---

# 🧠 Memory Review Scout — 2026-06-08

> 扫描范围：`00-Inbox-AI/agent-memory/` 全量 6 个 canonical 文件 + 1 个 projection + Hermes 运行时 MEMORY.md
> 对照：`MEMORY-PROTOCOL.md` + 当前 system prompt + 上次审查 (2026-06-07)
> 产出：1 个新 memory candidate（3 个 6/5 pending 候选仍然有效）

---

## 一、与前次审查 (2026-06-07) 的差异

| 维度 | 6/7 状态 | 6/8 当前状态 | 变化 |
|---|---|---|---|
| Canonical memory 文件 | 6 文件，无变更 | 6 文件，无变更 | **无变化** |
| hermes-soul.md projection | 过期 (6/3) | 过期 (6/3) | **无变化** |
| Hermes 运行时 MEMORY.md | 含 2 条过时 scout 信息 | 含 2 条过时 scout 信息 | **无变化** |
| 3 个 candidate (6/5) | pending-review | pending-review | **未处理 (3d+)** |
| Tony 主动会话 | 无 (6/5 后) | 无 (6/5 后) | **无新偏好** |
| curated-scout 产出 | 6/6-6/7 活跃 | 6/8 继续产出 | **确认稳定运行** |

## 二、一致性检测

### ✅ 通过项

| 检查项 | 结果 |
|---|---|
| Canonical 文件内部一致性 | ✅ 6 文件互不冲突 |
| Vault 路径引用 | ✅ 全部指向 `tony-ai-wiki-2026` |
| 语言偏好 | ✅ 统一：中文 + 保留英文术语 |
| Hermes write boundary | ✅ 所有文件正确记录 |
| 重复/冲突条目 | ✅ 未发现实质冲突 |

### ⚠️ 仍存在的问题（无变化，自 6/5 起）

| # | 问题 | 状态 | 已有候选 |
|---|---|---|---|
| F1 | `hermes-soul.md` 含 3 条过时 scout 状态 | ❌ 未修复 | `2026-06-05-regenerate-hermes-soul.md` |
| F2 | `learning-themes.md` 缺少广告投放 | ❌ 未修复 | `2026-06-05-add-advertising-to-learning-themes.md` |
| F3 | Scout 命名 3 套不一致 | ❌ 未修复 | `2026-06-05-align-scout-naming.md` |

### 🆕 新发现 (6/8)

| # | 问题 | 严重度 | 状态 |
|---|---|---|---|
| F4 | Tony 职业画像仅在 `hermes-soul.md` projection 中存在，canonical `profile.md` 和 `user-profile-and-ai-cognitive-system.md` 均缺失（角色、技术栈、行业） | ⚠️ 中 | → 新增候选 |

## 三、Hermes 运行时内存 vs Canonical 对照

| 运行时 MEMORY.md 声称 | Canonical / 实际状态 | 判断 |
|---|---|---|
| `curated-ai-scout 缺 LLM API key` | 6/4-6/8 有完整 curated-scout 产出 | ⚠️ 过时 (与 F1 同源) |
| `curated-ai-scout cron: 0 9,15,21 * * *` | 实际: `daily-ai-learning-scout` (08:30) + `curated-scout` (09/15/21) 两套脚本 | ⚠️ 命名不对齐 (与 F3 同源) |
| `cua-driver 0.5.1 / Codex CLI 0.125.0` | 未在 canonical 中记录（合理：skill 级操作细节） | ✅ 合理放置 |
| `exa 优先, Camofox 降级` | system prompt 中已编码 | ✅ 一致 |

## 四、F4 详细分析：Tony 职业画像缺失

### 现状

`hermes-soul.md` 包含 Tony 详细职业画像（仅 projection）：
- 角色：偏架构/平台/工程效率/组织落地的技术管理者，负责基础架构团队
- 技术栈：Java/Go/Spring Boot/MyBatis/Dubbo/APISIX/Nginx/K8s/AWS/Redis/Kafka/RocketMQ
- 行业：skill gaming / casual gaming
- AI 理念：AI 从个人工具推进成组织级工程能力
- 学习风格：系统化学习、输出倒逼输入、Obsidian/Cursor 管理知识

### 问题

Canonical 的 `profile.md` 和 `user-profile-and-ai-cognitive-system.md` 仅描述 Tony 在「AI knowledge system builder」这个单一维度，完全没有记录其职业角色、技术背景、行业。对 agent（尤其是 Codex/Claude Code/新 agent）而言：
- 无法基于行业背景判断学习任务的相关性
- 无法基于技术栈偏好做工程推荐（如推荐 Go 还是 Python 方案）
- 无法理解推荐的「落地性」——Tony 需要的是 team-level 可推行的方案，不仅是个人的开源实验

### 来源追踪

hermes-soul.md 中的 Tony Profile 信息来源未明确标注。推测来自早期对话或手动注入，但在 vault migration 时未回流到 canonical。

## 五、系统健康

- **Scout 策展活跃**：6/7-6/8 curated-scout 继续产出，信号质量正常
- **决策停滞持续**：8 天无 Tony 判断，3 个 memory candidate 已等 3 天
- **memory-review-scout 运行**：每日 08:00 正常触发
- **命名混用**：内存审查产出文件名混用 `YYYY-MM-DD-memory-review.md` 和 `memory-review-YYYY-MM-DD.md` 两种格式

## 六、产出汇总

| # | 文件 | 行数 | 状态 |
|---|---|---|---|
| profile.md | 37 | ⚠️ 缺少职业画像 |
| preferences.md | 50 | ✅ |
| learning-themes.md | 38 | ⚠️ 缺少广告投放 (F2) |
| negative-signals.md | 29 | ✅ |
| user-profile-and-ai-cognitive-system.md | 243 | ⚠️ 缺少职业画像 (F4) + Scout命名不一致 (F3) |
| memory-changelog.md | 40 | ✅ |
| hermes-soul.md (projection) | 118 | ❌ 过期 (F1) |
| Hermes runtime MEMORY.md | 10 | ⚠️ 2 条过时 |

**新 candidates**: 1（F4：Tony 职业画像回流 canonical）
**现有 pending 共 4**: 3 个 (6/5) + 1 个 (6/8)

---

*Hermes memory-review-scout | 2026-06-08 | 无自动化修改 | 1 新候选*
