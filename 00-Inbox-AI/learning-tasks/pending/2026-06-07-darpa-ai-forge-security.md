---
title: "DARPA AI Forge：国家安全视角的 AI Agent 挑战与安全架构映射"
created: 2026-06-07
updated: 2026-06-07
status: pending
owner: hermes
priority: P1
domain: "Security"
review_after: "2026-06-21"
tags:
  - learning-task
  - hermes
  - ai-safety
  - national-security
  - darpa
  - agent-security
  - threat-modeling
  - security-architecture
---

# DARPA AI Forge：国家安全视角的 AI Agent 挑战与安全架构映射

## Why Now

2026-06-07 早间扫描捕获到 DARPA 官方发布的 **《AI Forge：国家安全面临的重大 AI 挑战》** 报告。这是美国国防高级研究计划局对 AI Agent 在国家安全领域的权威评估，明确了 Agent 在**鲁棒性、安全性、可解释性**三个维度的核心挑战。

**为什么这是一个独立的新信号，而不是已有 AI Safety 任务的子项：**

1. **视角不同**：`ai-safety-governance-stack` 关注的是「政策框架 → 企业自律 → 技术现实」的治理栈，以白宫行政令和 Anthropic 自律呼吁为主线。DARPA 报告是从**国家安全威胁建模**的角度出发——它关心的不是「如何监管 AI」，而是「AI Agent 作为攻击面和新威胁向量该如何防御」。

2. **工程映射价值不同**：治理栈告诉你「应该在什么层面设防」，DARPA 报告告诉你「敌人会怎么用 Agent 攻击你」。对 Tony 关注的安全架构来说，后者是更直接的威胁建模输入。

3. **与 NSA MCP 安全指南的互补**：pending 的 `nsa-mcp-security-guidance` 聚焦 MCP 协议层的安全，DARPA 报告聚焦 Agent 系统层面的安全——两者构成「协议层安全 + 系统层安全」的完整拼图。

## Source

- URL: https://www.darpa.mil/sites/default/files/attachment/2026-06/ai-forge-report.pdf
- Source note: `00-Inbox-AI/hermes/curated-scout/20260607-090045-digest.md` (条目 #5)
- Captured evidence: DARPA 官方 PDF 报告，来源权威性极高。同日还有 NSA 评估 Anthropic Mythos 用于网络作战的延续信号。

## Suggested Domain

`Security` / `AI-Safety`

## Desired Output

- learning package

## Proposed Canonical Destination

Hermes 建议但不写入：
- `10-Knowledge/Security/05-Topics/DARPA AI Forge — Agent 国家安全威胁建模.md`
- `30-Playbooks/Agent 安全威胁建模清单.md`
- `20-Maps/AI Agent 安全全景图.md`（更新条目）

## Codex Handoff Contract

- Hermes writes this task only in `00-Inbox-AI/learning-tasks/pending/`.
- Hermes may attach drafts in `00-Inbox-AI/hermes/`.
- Hermes must not write directly into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, or `90-Agent-System/`.
- Codex researches, restructures, and prepares the learning package.
- Tony reviews before canonical promotion.

## Suggested Review Date

`2026-06-21`（2 周，DARPA 报告需要较长时间消化）

## Safety Notes

- DARPA 报告为公开文件，无涉密风险。
- 学习包产出不涉及任何机密或受控信息。
- 如果研究过程中引用 NSA 或其他情报机构材料，确认均为公开来源。

## Hermes Recommendation

- Decision: `study`
- Rationale: DARPA 是全球 AI 安全研究的最权威机构之一。这份报告从攻击者视角出发，是对 Tony 安全架构知识体系的稀缺补充。建议 Codex：(1) 提取报告核心威胁模型；(2) 映射到 Tony 当前 Agent 系统（Hermes/OpenHuman/Codex/ECC）的潜在攻击面；(3) 与 NSA MCP 安全指南交叉引用，形成「Agent 安全双层防御视图」。

## Follow-Up Proposal

- Suggested review cadence: 2 周后 review
- Suggested spaced review prompt: 「DARPA 识别的 AI Agent 安全威胁中，哪些对 Tony 的 Cognitive OS 最 relevant？防御优先级如何排序？」
