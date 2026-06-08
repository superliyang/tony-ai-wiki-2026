---
title: "Memory Review — 2026-06-07"
created: 2026-06-07
status: complete
source: memory-review-scout
tags:
  - memory-review
  - hermes
---

# 🧠 Memory Review Scout — 2026-06-07

> 扫描范围：`00-Inbox-AI/agent-memory/` 全量 7 个 canonical 文件 + 1 个 projection + Hermes 运行时 MEMORY.md
> 对照：`MEMORY-PROTOCOL.md` + 当前 system prompt + 上次审查 (2026-06-05)
> 产出：0 个新 memory candidate（3 个 pending 候选仍然有效）

---

## 一、与前次审查 (2026-06-05) 的差异

| 维度 | 6/5 状态 | 6/7 当前状态 | 变化 |
|---|---|---|---|
| Canonical memory 文件 | 6 文件，无变更 | 6 文件，无变更 | **无变化** |
| hermes-soul.md projection | 过期 (6/3) | 过期 (6/3) | **无变化** |
| Hermes 运行时 MEMORY.md | 含 3 条过时 scout 信息 | 含 3 条过时 scout 信息 | **无变化** |
| 3 个 candidate (6/5) | pending-review | pending-review | **未处理** |
| Tony 主动会话 | 无 (6/3 后) | 无 (6/5 后) | **无新偏好** |
| curated-scout 产出 | 6/4-6/5 | 6/6 新增 3 次产出 | **确认 LLM API key 正常** |

## 二、一致性检测

### ✅ 通过项

| 检查项 | 结果 |
|---|---|
| Canonical 文件内部一致性 | ✅ 6 文件互不冲突 |
| Vault 路径引用 | ✅ 全部指向 `tony-ai-wiki-2026` |
| 语言偏好 | ✅ 统一：中文 + 保留英文术语 |
| Hermes write boundary | ✅ 所有文件正确记录 |
| 重复/冲突条目 | ✅ 未发现 |

### ⚠️ 仍存在的问题（无变化，自 6/5 起）

| # | 问题 | 状态 | 已有候选 |
|---|---|---|---|
| F1 | `hermes-soul.md` 含 3 条过时 scout 状态 | ❌ 未修复 | `2026-06-05-regenerate-hermes-soul.md` |
| F2 | `learning-themes.md` 缺少广告投放 | ❌ 未修复 | `2026-06-05-add-advertising-to-learning-themes.md` |
| F3 | Scout 命名 3 套不一致 | ❌ 未修复 | `2026-06-05-align-scout-naming.md` |

## 三、Hermes 运行时内存 vs Canonical 对照

| 运行时 MEMORY.md 声称 | Canonical / 实际状态 | 判断 |
|---|---|---|
| `curated-ai-scout 缺 LLM API key` | 6/4-6/6 有完整 curated-scout 产出 | ⚠️ 过时 |
| `hourly-ai-scout` — "currently paused" | system prompt 中列为活跃 cron | ⚠️ 过时 |
| cua-driver 0.5.1 / Codex CLI 0.125.0 | 未在 canonical 中记录（合理：属于 skill 级操作细节） | ✅ 合理放置 |
| ChatGPT WKWebView AX 限制 | 未在 canonical 中记录（合理：技术 quirk） | ✅ 合理放置 |

## 四、系统健康

- **Scout 策展活跃**：6/6 产出 3 次 curated-scout digest（09:01 / 15:01 / 21:01），信号质量正常
- **决策停滞**：7 天无 Tony 判断（pending 7 件，accepted 0，discarded 0）
- **memory-review-scout 运行**：每日 08:00 正常触发
- **cron 命名**：`daily-ai-learning-scout` 实际产出物写入 `curated-scout/` 目录，命名与目录不一致

## 五、产出汇总

| # | 文件 | 行数 | 状态 |
|---|---|---|---|
| profile.md | 37 | ✅ |
| preferences.md | 50 | ✅ |
| learning-themes.md | 38 | ⚠️ 缺少广告投放 |
| negative-signals.md | 29 | ✅ |
| user-profile-and-ai-cognitive-system.md | 243 | ⚠️ Scout 命名不一致 |
| memory-changelog.md | 40 | ✅ |
| hermes-soul.md (projection) | 118 | ❌ 过期 |
| Hermes runtime MEMORY.md | 10 | ⚠️ 3 条过时 |

**新 candidates**: 0（3 个 pending 候选覆盖所有已知问题）

---

*Hermes memory-review-scout | 2026-06-07 | 无自动化修改 | 无新候选*
