---
title: "Agent 身份与治理基础设施：NewCore + MCP 权限模型"
created: 2026-06-15
updated: 2026-06-15
status: pending
owner: hermes
priority: P2
domain: "AI-Engineering"
review_after: "2026-07-06"
tags:
  - learning-task
  - hermes
  - agent-identity
  - agent-governance
  - mcp-security
  - agent-authorization
  - iam
  - newcore
sources:
  - "https://techcrunch.com/2026/06/15/ai-agents-are-becoming-employees-newcore-emerges-with-66m-to-give-them-identities/"
  - "https://www.ndnanalytics.com/blog/mcp-protocol-enterprise-ai-agents"
  - "https://venturebeat.com/orchestration/mcp-solved-tool-calling-a2a-solved-coordination-what-solves-transport"
---

# Agent 身份与治理基础设施：NewCore + MCP 权限模型

## Why Now

AI Agent 正从"工具"演化为"数字员工"，但缺少统一的身份、权限和治理基础设施。两个关键信号在 2026-06-15 同时出现：

**信号 1：NewCore $66M 融资 — Agent 身份基础设施赛道成型**
- NewCore 提供 Agent 的身份（identity）、访问权限（access control）和合规管理（compliance）
- 核心洞察：Agent 进入企业时需要的不是 API key，而是类似人类员工的 IAM（身份与访问管理）体系
- $66M 融资规模表明这不是边缘赛道——资本在押注 Agent 治理将成为下一个基础设施层

**信号 2：MCP/A2A 之后的下一层 — 传输层与安全模型**
- MCP 解决了工具调用标准化，A2A 解决了 Agent 间协调
- VentureBeat 指出下一个瓶颈是跨 Agent 的安全数据传输和权限模型
- NDN Analytics 深入分析 MCP 在企业落地的安全模型

**对 Tony/Hermes 的影响：**
- **直接关联主题**：安全架构 + 多 Agent 编排 — Tony 的五大核心主题之二
- Hermes/Codex/OpenHuman 的 Agent 链需要统一的身份和权限模型：谁可以写 wiki？谁可以发通知？谁可以改 cron？
- 当前 Hermes 的权限是隐式的（通过文件系统目录约束），但缺少可审计、可扩展的显式治理层
- 与 `trust-aware-agent-memory`（pending P1）互补：记忆治理 + 身份治理 = Agent 治理的完整两面

## Source

- URL: 见 frontmatter sources
- Source note: TechCrunch（NewCore 报道）、NDN Analytics（MCP 企业分析）、VentureBeat（传输层/安全模型分析）
- Captured evidence: `00-Inbox-AI/hermes/curated-scout/20260615-061431-summary.md` #3 (NewCore), `20260615-150056-summary.md` #6 (传输层), `20260615-090009-summary.md` #6 (MCP 企业分析)

## Suggested Domain

`AI-Engineering`

## Desired Output

learning package + decision memo

具体应覆盖：
1. Agent 身份与治理的完整问题空间：Identity → AuthN/AuthZ → Audit → Compliance
2. NewCore 架构解析：Agent 如何获得"员工级"身份、权限边界、合规审计
3. MCP 安全模型：当前 MCP 的认证授权机制、与 OAuth/OIDC 的集成路径
4. Agent 治理的行业现状：Anthropic/OpenAI/Google 各自的 Agent 权限方案对比
5. 对 Hermes Cognitive OS 的启示：是否需要显式的 Agent IAM 层？当前目录约束是否足够？
6. 安全边界设计：Agent 权限的"最小权限原则"如何在不影响能力的前提下实施

## Proposed Canonical Destination

- `10-Knowledge/AI-Cognitive-System/05-Topics/Agent 身份与治理基础设施.md`
- `90-Agent-System/decisions/2026-06-xx-agent-iam-design.md`（如需架构决策）

## Codex Handoff Contract

- Hermes writes this task only in `00-Inbox-AI/learning-tasks/pending/`.
- Hermes may attach drafts in `00-Inbox-AI/hermes/`.
- Hermes must not write directly into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, or `90-Agent-System/`.
- Codex researches, restructures, and prepares the learning package.
- Tony reviews before canonical promotion.

## Suggested Review Date

`2026-07-06`

## Safety Notes

- Agent 权限模型的任何变更都可能影响 Hermes 的写入能力——研究阶段只分析不实施
- NewCore 处于早期阶段（$66M A 轮），产品可能不稳定——产出应标注成熟度
- MCP 安全模型仍在演进中（Streamable HTTP + 无状态化后 auth 模式可能变化）
- 如涉及对 Hermes 权限做生产变更，需 Tony 审核 + Codex ADR 后执行

## Hermes Recommendation

- Decision: `study`
- Rationale: Agent 身份与治理是 Agent 从"个人工具"走向"组织生产力"的必经之路。NewCore 的融资规模（$66M）和 MCP 在企业落地的安全需求形成了双信号共振。Tony 的 Cognitive OS 已经有 3+ 个 Agent（Hermes/Codex/OpenHuman）在协作，权限模型目前靠目录约束隐式管理——这个话题不是"要不要做"而是"什么时候做"。与 `trust-aware-agent-memory`（记忆可信检索）互补构成 Agent 治理的完整两面。

## Follow-Up Proposal

- Suggested review cadence: 4 周后扫描 NewCore 产品进展 + MCP auth 规范更新
- Suggested spaced review prompt: 「NewCore 是否有公开的 Agent IAM 设计文档？MCP 的认证授权规范是否进入 RC？Agent 治理领域是否有新的开源框架或标准？」
