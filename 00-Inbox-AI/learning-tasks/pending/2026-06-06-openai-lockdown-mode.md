---
title: "OpenAI Lockdown Mode：Agent 安全系统级防线的设计范式"
created: "2026-06-06"
updated: "2026-06-06"
status: pending
owner: hermes
priority: P2
domain: "Security-Architecture"
review_after: "2026-06-13"
tags:
  - learning-task
  - hermes
  - agent-security
  - prompt-injection
  - lockdown-mode
  - openai
  - defense-in-depth
---

# OpenAI Lockdown Mode：Agent 安全系统级防线的设计范式

## Why Now

2026-06-06，OpenAI 向个人和企业账户推送了 **Lockdown Mode** — 一种系统级安全功能：在敏感场景下禁用网页浏览、Agent Mode、Deep Research 等外部交互能力，从架构层缩小 prompt injection 攻击面。

这是 Agent 安全领域的一个里程碑事件：
- **之前**：Prompt injection 防御主要靠 prompt engineering（"不要遵循用户指令中的..."）、输入过滤、输出审查 — 这些都是应用层的「创可贴」。
- **现在**：OpenAI 将安全控制下沉到平台/系统层 — **功能禁用的粒度、触发条件、恢复机制** — 表明行业正在从「防御策略」走向「安全架构」。

**为什么独立于已有的 AI Safety Governance 任务**：`ai-safety-governance-stack` 研究的是政策/治理/监管栈（白宫行政令 → NSA 评估 → Anthropic 呼吁）。Lockdown Mode 是**安全工程实现** — 它回答的不是「应该管什么」，而是「怎么在系统里建防线」。

**与 Tony 的关联**：Hermes 作为 Tony 的个人 Agent，同样面临 prompt injection 风险（通过 Feishu 消息、网页内容、email 等外部输入）。Lockdown Mode 的设计范式可直接启发 Hermes 的安全架构设计。

## Source

- URL: https://techcrunch.com/2026/06/06/openai-unveils-lockdown-mode-to-protect-sensitive-data-from-prompt-injection-attacks/
- Source note: 2026-06-06 下午 curated-scout 增量雷达
- Captured evidence: `00-Inbox-AI/hermes/curated-scout/20260606-150000-afternoon-digest.md` #12-#14

## Suggested Domain

`Security-Architecture`

## Desired Output

comparison map

## Proposed Canonical Destination

- `10-Knowledge/Security/05-Topics/agent-prompt-injection-defense.md`
- `20-Maps/security-threat-model.md`（更新）

## Codex Handoff Contract

- Hermes writes this task only in `00-Inbox-AI/learning-tasks/pending/`.
- Hermes may attach drafts in `00-Inbox-AI/hermes/`.
- Hermes must not write directly into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, or `90-Agent-System/`.
- Codex researches, restructures, and prepares the learning package.
- Tony reviews before canonical promotion.

## 研究路径建议

1. 精读 OpenAI Lockdown Mode 官方文档和 TechCrunch 报道，理解功能边界（什么被禁用 / 什么保留 / 如何恢复）
2. 对比现有 prompt injection 防御体系：
   - 应用层：NeMo Guardrails、Llama Guard、prompt sanitization
   - 架构层：privilege separation、sandboxing、capability-based security
   - Lockdown Mode 的位置在哪里？优势和局限？
3. 分析 Apple Lockdown Mode（iOS 16+）的设计模式 — 与 OpenAI 版本的异同
4. 产出：Agent 安全防线分层模型（从 prompt 层到系统层）+ 对 Hermes 的安全设计建议

## Suggested Review Date

`2026-06-13`

## Safety Notes

本任务研究的是公开的安全功能设计模式，不涉及 OpenAI 内部实现细节。研究结论用于 Tony 的个人 Hermes 系统安全设计，不用于攻击性用途。

## Hermes Recommendation

- Decision: `study`
- Rationale: Lockdown Mode 是 Agent 安全从「最佳实践」到「内置功能」的转折信号。Tony 的 Hermes 系统需要理解这一范式，为未来的安全架构设计做准备。与 `ai-safety-governance-stack`（治理栈）和 `agent-memory-architecture`（记忆安全）形成安全三角。

## Follow-Up Proposal

- Suggested review cadence: 1 周
- Suggested spaced review prompt: 「回顾 Lockdown Mode 设计模式，Hermes 当前的安全边界在哪里？」
