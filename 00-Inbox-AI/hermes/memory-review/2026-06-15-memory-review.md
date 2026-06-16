---
title: "Hermes Memory Review 2026-06-15"
created: 2026-06-15
source: hermes-memory-review-scout
type: memory-review
status: generated
tags:
  - memory-review
  - agent-memory
  - consistency-check
---

# Hermes Memory Review — 2026-06-15

## Executive Summary

- **审查文件数**: 12 canonical + 8 projections/candidates + 1 runtime
- **发现问题**: 5 (3 high, 2 medium)
- **产出候选**: 3
- **结论**: Canonical memory 在经历 06/14 batch review 后进入关键转折点——Tony 首次通过 review gate 做了批量决策，但 canonical memory 尚未同步这一重大事件。

---

## 全面审计发现

### F1 (HIGH): 06/14 Batch Review 是重大系统事件，但 canonical memory 未记录

Tony 通过 Codex review gate triage panel 在 2026-06-14 做出了 5 项批量决策：
- Agent Memory → accept → build
- Agent Model → accept → build
- MCP → watch → build-checklist
- RSI → watch → governance-gate
- Advertising → accept-with-verification

这是系统运行 12 天以来第一次 review queue 流动。`memory-changelog.md`（最后更新 06/14）**未记录此事件**。`profile.md` 的 Open Questions 仍问"哪些学习领域优先级最高"，但 Tony 已通过 batch 决策给出了隐含优先级。

**影响**: 新 agent 读取 canonical memory 仍会认为系统处于"等待首次 review"状态，而实际上 review gate 已启动。

---

### F2 (HIGH): hermes-soul.md projection 严重过时（12 天未更新）

`projections/hermes-soul.md` 生成于 06/03，当前包含多条过期信息：

| 声称 | 实际 |
|---|---|
| "hourly-ai-scout: currently paused" | System prompt 中正常运行（每小时） |
| "⚠️ curated-ai-scout 缺 LLM API key" | 06/04-06/05 curated-scout 产出存在 |
| "Vault is clean and ready — staging directories are empty" | ~49 learning-tasks + 8 memory candidates + 27 review-queue items |
| 仅 recording `curated-ai-scout` / `memory-sync-scout` | 实际 cron 名是 `daily-ai-learning-scout` / `hourly-ai-scout` |

**影响**: Agent 读取 projection 后会基于错误前提做决策。此问题已在 C3 (06/05) 和 F1 (06/12) 中标记，至今未处理。

---

### F3 (HIGH): learning-themes.md 缺失 2 个 Tony 主动发起的活跃学习领域

`learning-themes.md` 最后更新 06/03。此后 Tony 明确发起了两个领域学习：

1. **广告投放** (06/05): ~60K 字深度产出，Tony 确认"方向没问题"，内容已写入 `10-Knowledge/advertising/`
2. **LLM 推理优化工程** (06/07-06/09): Tony 说"搞搞LLM推理优化工程"，Phase 1 全貌图已完成（24KB）

两项均有 pending candidate（06/05 和 06/09），但 6-10 天未审核。两个主题代表了 Tony 的技术角色自然延伸，不应在 canonical memory 中保持不可见。

---

### F4 (MEDIUM): 5 of 8 pending memory candidates 可能被 06/14 batch review 部分覆盖

06/14 的 batch review 改变了多个假设：

- `batch-review-preference` (06/12): 假设"Tony 从不 review"——现已不成立，Tony 在 06/14 做了批量决策
- `update-hermes-soul-active-threads` (06/12): 状态的"积压"描述需要更新——06/14 batch 后，5 个 accepted package 已进入执行队列
- `add-tony-professional-profile-to-canonical` (06/08): Agent Memory gate（06/14 P1）将定义 memory schema，影响职业画像是否应进 canonical

这些 candidate 可能仍 valid，但前提条件已变更。

---

### F5 (MEDIUM): preferences.md 有 task-intent routing 正偏好，但缺少对应的 negative-signals 条目

`preferences.md` L28 记录了 "Prefer a task-intent layer before research: Tony's requests should be routed as research, project, organize, writing, learning, reflection, or publish instead of defaulting every request to research."

但 `negative-signals.md` 中没有对应的 "Do not default every request to research"。按系统设计惯例，正偏好应有对应的负信号配对，防止 agent 理解为"软建议"而非"路由规则"。

---

## 发现清单

| ID | Severity | 描述 | 关联 Candidate |
|---|---|---|---|
| F1 | HIGH | 06/14 batch review 未记录到 memory-changelog + profile | C1 (new) |
| F2 | HIGH | hermes-soul.md projection 12天未更新 | 已有 C3 (06/05) |
| F3 | HIGH | learning-themes 缺失广告投放 + LLM推理 | C2 (new) |
| F4 | MEDIUM | 5/8 pending candidates 前提条件变更 | 见 Report |
| F5 | MEDIUM | task-intent routing 缺少 negative-signals 配对 | 见 Report（低优先级） |

---

## 已存在但待审核的 Candidate 状态

| Candidate | 日期 | 状态 | 06/14 后的影响 |
|---|---|---|---|
| C1: 广告投放→学习主题 | 06/05 | pending | 广告投放已被 Tony accept-with-verification (06/14)，主题更应进 learning-themes |
| C2: Scout 命名对齐 | 06/05 | pending | 仍 valid，未受 06/14 影响 |
| C3: 重新生成 hermes-soul | 06/05 | pending | **更紧急**: 06/14 batch 后 projection 与实际差距更大 |
| C4: Tony 职业画像→canonical | 06/08 | pending | Agent Memory gate (P1) 将定义 schema，可能影响此候选的形式 |
| C5: LLM 推理→学习主题 | 06/09 | pending | 仍 valid，与 F3 一致 |
| C6: batch-review-preference | 06/12 | pending | **需重新评估**: 06/14 Tony 做了 batch review，假设变更 |
| C7: Scout 命名记录 | 06/12 | pending | 与 C2 互补，需 Tony 二选一 |
| C8: hermes-soul active-threads | 06/12 | pending | 06/14 batch 后需更新描述（backlog 部分已开始流动） |

---

## 建议

1. **优先接受本日 C1**: 06/14 batch review 是系统转折点，应使 canonical memory 可感知
2. **优先接受本日 C2**: 合并两个 6-10 天老的 candidate，减少积压
3. **Tony 批量处理 C2+C3+C5**: Scout 命名和 hermes-soul 更新应一起做，避免分散 review
4. **Tony 明确 memory-review 节奏**: 当前 pending 12 memory reviews (06/03→06/15) 形成 noise backlog。06/14 batch decision 已定：daily review 留在 hermes 层，高置信候选才入 review queue。执行此规则后，多数旧 memory review 可 discard
