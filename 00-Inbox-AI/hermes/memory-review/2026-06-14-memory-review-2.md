# 🧠 Memory Review — 2026-06-14 第2轮

> Tony AI Cognitive System | Capture → Recall → Judge → Crystallize → Reuse
> Hermes = Recall / Scout | 向内看 · 记忆审查 · 上午复核
> 第1轮 (08:01) 产出: `memory-review-2026-06-14.md` | 本报告: 二次审查 + 修正

## 📋 上轮 Review (08:01) 遗留问题复核

### 🔍 自洽性标记 #1: "Active 和 Candidate 同时包含 Agent Memory 相关主题"

**复审结论: 误报 (FALSE POSITIVE)**

| 层级 | 条目 | 含义 |
|---|---|---|
| Active (line 17) | "Autonomous agents and persistent memory" | 学习**领域**本身 — Tony 在学 Agent 技术 |
| Candidate (line 32) | "Accepted/discarded Scout v2 candidate feedback loop" | 系统**基础设施** — 反馈机制的工程化 |
| Candidate (line 33) | "Review Queue and decision memory" | 系统**基础设施** — 决策记录机制 |

三者处于不同抽象层：Active 是"学什么"，Candidate 是"系统怎么建"。不存在语义冲突，无需合并或删除。

### 🔍 自洽性标记 #2: "preferences 说 prefer 共享 Markdown 记忆，但 negative-signals 禁止多个工具独立写 canonical 知识"

**复审结论: 误报 (FALSE POSITIVE)**

- `preferences.md` line 24: **正向偏好** — "使用共享 Markdown 记忆，因为 agent 默认不共享私密记忆"
- `negative-signals.md` line 20: **负向约束** — "不要让多个工具**独立**（未经 review）写入 canonical"

两条规则是**互补**而非矛盾：一个说"用什么"，一个说"怎么用"。核心语义一致：共享 Markdown 是好实践，但必须经过 review gate。

---

## 📊 当前 Canonical Memory 全貌

| 文件 | 更新日期 | 状态 | 行数 |
|---|---|---|---|
| `profile.md` | 2026-06-14 | ✅ 当前 | 39 |
| `preferences.md` | 2026-06-14 | ✅ 当前 | 55 |
| `learning-themes.md` | 2026-06-03 | ⚠️ 冻结 12d | 40 |
| `negative-signals.md` | 2026-06-03 | ⚠️ 冻结 12d | 30 |
| `user-profile-and-ai-cognitive-system.md` | 2026-06-03 | ⚠️ 冻结 12d | 244 |
| `memory-changelog.md` | 2026-06-14 | ✅ 当前 | 47 |

### 📐 Hermes Soul Projection

| 文件 | 更新日期 | 状态 |
|---|---|---|
| `projections/hermes-soul.md` | 2026-06-03 | ❌ 过期 12d |

**Gap 摘要:**

1. **Scout 状态错误**: 声称 `hourly-ai-scout` "currently paused" — 实际正常运行
2. **Scout 命名错误**: 声称 `curated-ai-scout` cron `0 9,15,21` — 实际 cron job 名是 `daily-ai-learning-scout`，system prompt 显示 08:30
3. **LLM API key 警告过时**: 声称缺 key，但 curated scout 产出正常
4. **Active Threads 虚假**: 声称 "Vault is clean and ready" — 实际有 8 个 pending candidates + review-queue backlog
5. **06/14 preferences 未同步**: access-layer split + task-intent routing 两项新偏好未反映

## 📦 Memory Candidates 现状 (8 pending)

| # | 候选 (创建日) | 天数 | 操作 | 优先级 |
|---|---|---|---|---|
| F4 | Tony 职业画像回流 canonical (06/08) | 7d | add → profile.md | 🔴 高 |
| F1 | 重新生成 hermes-soul.md (06/05) | 10d | replace | 🟡 高 |
| F5 | LLM推理优化 → learning-themes (06/09) | 6d | add | 🟡 中 |
| F2 | 广告投放 → learning-themes (06/05) | 10d | add | 🟡 中 |
| C1 | 批量决策偏好 (06/12) | 3d | add → preferences | 🟡 中 |
| F3 | Scout 命名对齐 (06/05) | 10d | replace | 🔵 低 |
| C2 | 记录实际 Scout 名 (06/12) | 3d | add | 🔵 低 |
| C3 | 更新 soul Active Threads (06/12) | 3d | replace | 🔵 低 |

> **C2/C3 是 F1/F3 的子集，接受 F1+F3 后自动失效。**

## ⚠️ 新发现

### F0: learning-themes.md 活跃主题 "Security as a newly promoted support domain" — "newly" 过期

`learning-themes.md` line 28:
> Security as a **newly promoted** support domain for AI cognitive system safety...

该条目自 06/03 起在 Active Themes 中，已过 12 天。"newly promoted" 描述已过时 — 应改为 "active support domain" 或评估是否需要转入 Candidate。

**未生成 candidate**: 此问题与 F4 (职业画像回流) 属于同一类"canonical 冻结 12d"问题。接受 F1 (重新生成 soul) + F4 后，整个 canonical review wave 会自然覆盖。单独为此生成 candidate 会加剧 backlog。

### F0b: memory-changelog 06/14 条目标题不完整

06/14 changelog 标题为 "(access-layer split)"，但实际包含 3 项变更：access-layer split + `今日入口` 路径 + feishu 命名。`preferences.md` 可能在此批次中新增了 task-intent routing preference (line 28)，但 changelog 未列出。

**未生成 candidate**: changelog 补充属于 housekeeping，不应单独占用 review gate。可在下次批量处理时一并修正。

---

## 📌 建议

1. **无需新 candidate** — 现有 8 个 candidates 覆盖所有结构性 issue
2. **优先批量处理**: F4 (职业画像) + F1 (重新生成 soul) + F2+F5 (learning themes) 可一次接受
3. **06/14 早间 review 的 2 个自洽性标记已被本报告澄清为误报** — 无需额外行动

---

*Memory Review Scout v1 | 2026-06-14 第2轮 | 0 个新 candidate | 修正上轮 2 个误报*
