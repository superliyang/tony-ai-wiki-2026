---
title: "Memory Candidate: 记录 Tony 的批量决策偏好到 preferences"
created: 2026-06-12
status: pending-review
source: memory-review-scout
type: add
target: "00-Inbox-AI/agent-memory/preferences.md"
---

# Candidate: 记录 Tony 的批量决策偏好

## 建议操作

**add** — 在 `preferences.md` 的 "Positive Preferences" 或 "Operating Rules" 中添加：

> - Prefer batched review over real-time, per-item judgment: Tony tends to review memory candidates, learning tasks, and scout signals in batches (e.g., weekly) rather than individually as they arrive. The system should accumulate candidates and present a consolidated review surface rather than sending per-item decision prompts.

同时可选：在 `negative-signals.md` 中添加对应的避免项：

> - Do not send repeated "decision stagnation" notifications when Tony hasn't reviewed in a short window (e.g., 1-2 days). Escalate only after a configured threshold (e.g., 7 days) or when the accumulation reaches a critical mass.

## 变更理由

1. **Recurring pattern**: 从 06/05 至今 7 天，Tony 未对任何 memory candidate、学习任务或 review-queue 做出判断。06/11 和 06/12 连续两次 memory review 标记了"决策停滞"。这不是一次性事件——它是 Tony 的工作模式。

2. **减少无效通知**: 如果不记录此偏好，系统会继续每 1-2 天发送"决策停滞"警告，消耗 Feishu/WeChat 通知额度且不产生行动。记录后，系统可以调整为：每周推送一次汇总，仅在 backlog 达到 critical mass 时发送告警。

3. **提高候选质量**: 如果系统知道 Tony 偏好批量审查，它可以：
   - 在推送前对候选做一次自检（去重、优先级排序、冲突检测）
   - 提供"本周候选汇总"而非单个候选推送
   - 在汇总中包含决策辅助信息（如 "这 3 个候选互不冲突，可一次全部接受"）

4. **类比 precedent**: preferences 已记录 "Prefer curated learning radar over high-frequency search-result streams" — 这是内容层面的"批量 > 逐项"。本候选将同一原则扩展到决策节奏层面。

## 关联发现

memory-review-2026-06-12 的 F3

## 备注

- 此偏好是 **推断**，非 Tony 明确声明。如 Tony 实际上是因忙碌而非偏好，可 discard 本候选。
- 如果接受，建议同步调整 Hermes 的 memory-review-scout 节奏：从每日改为每周 2 次（如周三+周日），减少重复警告。
- 如果 discard，建议 Tony 明确偏好的决策节奏（如 "每天花 2 分钟扫 pending"），系统据此调整推送。
