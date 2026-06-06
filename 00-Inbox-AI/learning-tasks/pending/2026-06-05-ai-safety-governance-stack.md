---
title: "AI 安全治理栈：从白宫行政令到企业安全实践的工程映射"
created: "2026-06-05"
updated: "2026-06-05"
status: pending
owner: hermes
priority: P2
domain: "AI-Safety"
review_after: "2026-06-19"
tags:
  - learning-task
  - hermes
  - ai-safety
  - governance
  - regulation
  - security-architecture
---

# AI 安全治理栈：从白宫行政令到企业安全实践的工程映射

## Why Now

2026 年 6 月第一周，AI 安全治理的多层信号在同一时间窗内密集出现：

1. **白宫 AI 创新与安全行政令（6/2）**：建立「覆盖前沿模型」分类评估流程（NSA 主导）、AI 网络安全清算所、自愿性预发布审查框架。政策基调：创新优先 + 安全协作，而非监管先行。
2. **Anthropic 全球放缓呼吁（6/5）**：Jack Clark 公开呼吁紧急刹车，强调人类必须保持对越来越强大 AI 系统的控制。
3. **NSA 评估 Anthropic Mythos 用于网络作战**（上周）：从国家安全的实操层面验证了对前沿模型能力的具体担忧。
4. **递归自我改进的生产现实**（6/5 下午，见独立 P1 任务）：自我改进的 Agent 模型让安全治理的紧迫性从「远期风险」变为「当下问题」。

这四条信号从四个层级（政策框架 → 企业自律 → 国家安全 → 技术现实）构成一个完整的安全治理栈。Tony 关注「安全架构」——理解这个治理栈的每一层及其工程映射，对于设计 Agent 系统的安全边界有直接参考价值。

核心问题：**AI 安全治理正在形成一个多层体系 — 从政策到代码，每一层对 Agent 架构师意味着什么？**

## Source

- URL: https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/
- URL: https://www.today.com/video/anthropic-issues-urgent-warning-for-slowdown-of-ai-development-264594501629
- URL: https://www.cnbc.com/2026/06/05/softbank-masayoshi-son-openai-model-super-intelligence.html (交叉引用：递归自我改进上下文)
- 交叉信号: NSA Mythos 安全评估 (上周)
- Source note: 2026-06-05 curated-scout 下午增量 + 本周追踪信号
- Captured evidence: `00-Inbox-AI/hermes/curated-scout/20260605-170000-afternoon-digest.md` (第4条 + 追踪信号段)

## Suggested Domain

`AI-Safety` — 安全治理的多层结构直接影响 Agent 系统的安全架构设计，尤其当 Hermes 接入更强大模型时。

## Desired Output

- **learning package**:
  - 四层治理栈解析：政策层（白宫 EO 核心条款及对开发者的实际要求）→ 企业自律层（Anthropic RSP、OpenAI Preparedness Framework 等自愿性框架的异同）→ 国家安全层（NSA 模型评估的实际操作和关注点）→ 工程实现层（如何在 Agent 系统中落地安全护栏）
  - 对 Agent 架构师的启示：如果 Hermes 接入一个「前沿模型」，需要什么样的安全层？
  - 治理趋势预判：自愿性框架 vs 强制监管的未来走向

- **comparison map**: 三大 AI 实验室安全框架对比 — Anthropic RSP / OpenAI Preparedness Framework / Google DeepMind Frontier Safety Framework

- **decision memo**: Hermes 当前的安全边界是否足够？如果接入更强模型（如 Anthropic Mythos 级），需要新增哪些安全层？

## Proposed Canonical Destination

`10-Knowledge/Security/05-Topics/` 或 `30-Playbooks/Security/`

## Codex Handoff Contract

- Hermes writes this task only in `00-Inbox-AI/learning-tasks/pending/`.
- Hermes may attach drafts in `00-Inbox-AI/hermes/`.
- Hermes must not write directly into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, or `90-Agent-System/`.
- Codex researches, restructures, and prepares the learning package.
- Tony reviews before canonical promotion.

## Suggested Review Date

`2026-06-19` — P2 优先级，两周期限，与递归自我改进 P1 任务错开一周

## Safety Notes

- ⚠️ 本任务不涉及 Tony 系统配置的敏感数据，但研究过程中可能接触到前沿模型的安全评估方法论——注意区分公开信息和需要 NDA 的内部安全审计信息。
- 安全治理的政策分析应保持技术中立，不预设监管立场。
- 对 Hermes 安全边界的评估仅作为技术讨论，不应在 Tony review 前直接修改任何 Agent 配置。

## Hermes Recommendation

- Decision: `study`
- Rationale: 安全治理是递归自我改进（P1）的互补视角——P1 关注「技术现实是什么」，本任务关注「治理体系如何响应」。Tony 关注「安全架构」，而安全架构不能只看代码层——从白宫政策到企业 RSP 到工程护栏，每一层都会影响 Agent 系统应该接入哪些模型、如何控制权限、如何审计行为。P2 优先级（低于递归自我改进），但与 Agent 记忆架构的隐私安全维度形成互补。
