---
title: "Memory Review — 2026-06-06"
created: 2026-06-06
status: complete
tags:
  - memory-review
  - hermes
---

# 🧠 Memory Review Scout — 2026-06-06

> 扫描范围：`00-Inbox-AI/agent-memory/` 全量 7 个文件 + 1 个 projection + 全部 15 个 cron jobs
> 对照：`MEMORY-PROTOCOL.md` + Hermes 当前 system prompt + 实际 cron job 配置
> 上次审查：2026-06-05（产出 3 个 candidate，全部仍为 pending-review）

---

## 一、上次审查跟进

| # | Candidate | 状态 | 距今 |
|---|---|---|---|
| C1 | 重新生成 hermes-soul.md projection | ⏳ pending-review | 1 天 |
| C2 | 添加「广告投放」到 learning-themes | ⏳ pending-review | 1 天 |
| C3 | 对齐 Scout cron job 命名 | ⏳ pending-review | 1 天 |

**状态**：3 个 candidate 均未被执行，仍在 `candidates/` 目录中等待 Tony/Codex review。

---

## 二、今日一致性检测

### ✅ 保持通过项

| 检查项 | 状态 |
|---|---|
| Canonical 5 文件内部一致性 | ✅ 无变化，无新冲突 |
| Vault 路径引用 | ✅ 全部正确 |
| Hermes write boundary | ✅ 记录完整 |
| 语言偏好 | ✅ 统一 |
| memory-sync-scout 运行 | ✅ 6/6 08:00 正常完成 |
| curated-ai-scout 运行 | ✅ 6/5 全天 4 轮正常产出 |

### ⚠️ 持续存在项（已有对应 candidate）

| # | 问题 | 对应 Candidate | 状态 |
|---|---|---|---|
| F1 | hermes-soul.md projection 过期 | C1 | pending |
| F2 | 广告投放未入 learning-themes | C2 | pending |
| F3 | Scout 命名 3 套并存 | C3 | pending |

### 🆕 今日新发现

**F4: System prompt "Your Cron Jobs" 节引用的 cron job 名与 jobs.json 实际配置不一致**

当前 system prompt 的"Your Cron Jobs"节声称：
- `hourly-ai-scout` — 每小时运行，使用 Exa
- `daily-ai-learning-scout` — 每日 08:30，RSS-based

但 `jobs.json` 中实际注册的 15 个 cron job 中**不包含** `hourly-ai-scout` 和 `daily-ai-learning-scout`。这两个脚本文件存在于 `~/.hermes/scripts/` 但未被注册为 cron job。

实际活跃的 external signal cron jobs 是：
- `curated-ai-scout` — `0 9,15,21 * * *` (script-based, 每天 3 轮)
- `hermes-growth-*` 系列 — `30 8 * * 1-6` (agent-based, 每日一个领域)

**影响**：运行时的 Hermes agent 读取 system prompt 后可能认为 `hourly-ai-scout` 在运行，但实际不存在此 cron job。这与 F3（Scout 命名不一致）同源，但还额外涉及 system prompt 硬编码问题。

**归属判断**：此问题可视为 F3 的深层根因 — 不仅是命名不一致，而是整个 system prompt 的 Cron Jobs 描述与运行时脱节。建议 Tony 决定是否将此发现合并到 C3 或作为独立修复项。

---

## 三、当前 Cron Job 全貌（参考）

### Script-based (no_agent)
| Job 名 | 调度 | 脚本 |
|---|---|---|
| `curated-ai-scout` | `0 9,15,21 * * *` | `curated-scout.sh` |
| `memory-sync-scout` | `0 8 * * *` | `memory-sync.sh` |
| `daily-git-push` | `0 22 * * *` | `daily-git-push.sh` |

### Agent-based
| Job 名 | 调度 | 角色 |
|---|---|---|
| `hermes-core-radar-morning` | `0 8 * * *` | 上午雷达摘要 |
| `hermes-core-radar-afternoon` | `0 15 * * *` | 下午增量扫描 |
| `hermes-memory-review` | `0 8 * * *` | 记忆审查（本 job） |
| `hermes-learning-task-generator` | `0 19 * * *` | 学习任务生成 |
| `hermes-follow-up-review` | `30 19 * * *` | 间隔复习提醒 |
| `hermes-weekly-synthesis` | `0 17 * * 0` | 周度合成 |
| `hermes-growth-industry` | `30 8 * * 1` | 周一：行业理解 |
| `hermes-growth-product` | `30 8 * * 2` | 周二：产品思维 |
| `hermes-growth-management` | `30 8 * * 3` | 周三：管理能力 |
| `hermes-growth-eq-communication` | `30 8 * * 4` | 周四：情商/沟通 |
| `hermes-growth-business` | `30 8 * * 5` | 周五：商业/战略 |
| `hermes-growth-deepdive` | `30 8 * * 6` | 周六：深度专题 |

---

## 四、产出汇总

| # | 文件 | 行数 | 状态 |
|---|---|---|---|
| profile.md | 37 | ✅ 一致 |
| preferences.md | 50 | ✅ 一致 |
| learning-themes.md | 38 | ⚠️ 缺广告投放（C2 pending） |
| negative-signals.md | 29 | ✅ 一致 |
| user-profile-and-ai-cognitive-system.md | 243 | ⚠️ Scout 命名不一致（C3 pending） |
| memory-changelog.md | 40 | ✅ 一致 |
| hermes-soul.md (projection) | 118 | ❌ 过期（C1 pending） |
| System prompt | — | 🆕 Cron Jobs 节与 jobs.json 脱节 |

**新 memory candidates 产出**: 0 个（所有已知问题已被 6/5 的 3 个 candidate 覆盖）

---

## 五、建议

1. **优先 review 6/5 的 3 个 pending candidates** — C1（projection 重新生成）和 C2（广告投放）是最直接的修复，C3（命名对齐）需要 Tony 决策
2. **F4（system prompt 脱节）可合并到 C3** — 或在 C3 执行时一并修复
3. **hermes-soul.md 中的 "⚠️ curated-ai-scout 缺 LLM API key" 警告已可移除** — 6/4-6/5 的 curated-scout 有完整产出

---

*Hermes memory-review-scout | 2026-06-06 | 无自动化修改*
