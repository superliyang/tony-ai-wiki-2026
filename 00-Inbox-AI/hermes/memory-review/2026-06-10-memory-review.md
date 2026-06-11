---
title: "Memory Review Scout — 2026-06-10"
created: 2026-06-10
status: complete
source: memory-review-scout
tags:
  - memory-review
  - hermes
---

# 🧠 Memory Review Scout — 2026-06-10

> 扫描范围：`00-Inbox-AI/agent-memory/` 全量 6 canonical + 1 projection + Hermes 运行时 MEMORY.md
> 对照：`MEMORY-PROTOCOL.md` + 当前 system prompt + 上次审查 (2026-06-09)
> 产出：0 个新 memory candidate（5 个现有 candidate 覆盖所有已知问题）

---

## 一、与前次审查 (2026-06-09) 的差异

| 维度 | 6/9 状态 | 6/10 当前状态 | 变化 |
|---|---|---|---|
| Canonical memory 文件 | 6 文件，无变更 | 6 文件，无变更 | **无变化** |
| hermes-soul.md projection | 过期 (6/3)，已 6 天 | 过期 (6/3)，已 7 天 | **无变化** |
| Hermes 运行时 MEMORY.md | 含 1 条过时 API key 警告 | 含 1 条过时 API key 警告 | **无变化** |
| 5 个 pending candidate | pending-review | pending-review | **未处理 (1-5d)** |
| Tony 主动会话 | 无 (6/7 "搞搞LLM推理优化" 后) | 无 | **无新偏好/决策** |
| curated-scout 运行 | 活跃 (6/9 全天 4 轮) | 活跃 (6/10 上午版正常) | **确认稳定** |

---

## 二、一致性检测

### ✅ 通过项

| 检查项 | 结果 |
|---|---|
| Canonical 文件内部一致性 | ✅ 6 文件互不冲突 |
| Vault 路径引用 | ✅ 全部指向 `tony-ai-wiki-2026` |
| 语言偏好 | ✅ 统一：中文 + 保留英文术语 |
| Hermes write boundary | ✅ 所有文件正确记录 |
| 重复/冲突条目 | ✅ 未发现实质冲突 |

### ⚠️ 仍存在的问题（无变化）

| # | 问题 | 严重度 | 已有候选 | 停留天数 |
|---|---|---|---|---|
| F1 | `hermes-soul.md` 含 3 条过时 scout 状态 + API key 警告 | ⚠️ 中 | `2026-06-05-regenerate-hermes-soul.md` | **5d** |
| F2 | `learning-themes.md` 缺少「广告投放」 | ⚠️ 中 | `2026-06-05-add-advertising-to-learning-themes.md` | **5d** |
| F3 | Scout 命名 3 套不一致 | ⚠️ 中 | `2026-06-05-align-scout-naming.md` | **5d** |
| F4 | Tony 职业画像仅在 projection、不在 canonical | ⚠️ 高 | `2026-06-08-add-tony-professional-profile-to-canonical.md` | **2d** |
| F5 | `learning-themes.md` 缺少「LLM 推理优化工程」 | ⚠️ 中 | `2026-06-09-add-llm-inference-to-learning-themes.md` | **1d** |

---

## 三、Hermes 运行时 MEMORY.md 对照

`~/.hermes/memories/MEMORY.md` 共 11 行（6 个 § 分隔的压缩条目），存在以下过时内容：

| 运行时 MEMORY.md 声称 | 实际状态 | 归属 |
|---|---|---|
| `⚠️ curated-ai-scout 缺 LLM API key` | 6/4-6/10 有完整 curated-scout 产出 | ← F1 子类（projection 同步过时） |
| `curated-ai-scout (cron: 0 9,15,21 * * *, job: 24c8c8dff64d)` | 命名不一致（system prompt 用 `daily-ai-learning-scout`） | ← F3 子类 |
| 其余条目（vault 路径、偏好、搜索架构、桌面工具、领域学习） | ✅ 一致 | — |

> **注**: Hermes 运行时 MEMORY.md 的过时内容是 F1 + F3 的下游影响。当 F1 (projection 重新生成) 和 F3 (命名对齐) 执行时，MEMORY.md 应同步更新。不建议为 MEMORY.md 创建独立候选。

---

## 四、系统健康

- **Canonical memory 冻结**: 7 天无更新（最后修改 6/3）
- **决策停滞持续**: 8 天零 Tony 判断（accepted=0, discarded=0）
- **Candidate 积压**: 5 个 memory candidates pending，最长 5 天
- **review-queue**: 13 pending，7 件 >72h
- **curated-ai-scout**: ✅ 稳定运行（6/9 全天 4 轮，6/10 上午版正常）
- **learning-tasks**: 26 pending + 4 in-progress — 容量饱和
- **Tony 活跃信号**: 6/7 "搞搞LLM推理优化工程" — 最近一次主动学习行为

---

## 五、Gap 扩大趋势

Canonical memory 与实际状态之间的 gap 在扩大：

| 维度 | Canonical 记录 | 实际 |
|---|---|---|
| 活跃学习领域 | 无广告投放、无 LLM 推理优化 | Tony 已完成广告投放深钻 (~60K 字) + LLM 推理优化 Phase 1 (24KB) |
| Tony 职业背景 | 仅描述「AI system builder」 | 实际是基础架构负责人，含完整技术栈和行业 |
| Scout 状态 | `hourly-ai-scout` paused / LLM API key 缺失 | Scout 已恢复运行，API key 正常 |

---

## 六、产出汇总

| # | 文件 | 行数 | 状态 |
|---|---|---|---|
| profile.md | 37 | ⚠️ 缺少职业画像 (F4) |
| preferences.md | 50 | ✅ |
| learning-themes.md | 38 | ⚠️ 缺广告投放 (F2) + LLM推理优化 (F5) |
| negative-signals.md | 29 | ✅ |
| user-profile-and-ai-cognitive-system.md | 243 | ⚠️ 缺职业画像 (F4) + Scout命名 (F3) |
| memory-changelog.md | 40 | ✅ |
| hermes-soul.md (projection) | 118 | ❌ 过期 7 天 (F1) |
| Hermes runtime MEMORY.md | 11 | ⚠️ 1 条过时 (F1/F3 影响) |

**本次新 candidates**: **0**（5 个现有 candidate 覆盖所有已知问题，无新发现）

---

*Hermes memory-review-scout | 2026-06-10 | 无自动化修改 | 0 新候选 | 5 prior pending*
