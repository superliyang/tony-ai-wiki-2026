---
title: "NSA MCP 安全架构指南：国家级 Agent 基础设施安全审查"
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
  - mcp-security
  - nsa
  - agent-infrastructure
  - security-architecture
  - compliance
---

# NSA MCP 安全架构指南：国家级 Agent 基础设施安全审查

## Why Now

2026-06-05，美国国家安全局（NSA）发布了 **基于 MCP 设计 AI 系统的安全指南** — 这是全球首个国家级情报/安全机构针对 MCP 协议的正式安全指导文件。

这个信号的重要性远超一篇技术博文：
- **权威性**：NSA 是美国顶级信号情报和网络安全机构，其安全评估具有事实上的行业标准效应
- **时机**：正值 MCP 2026-07-28 Release Candidate 和 Streamable HTTP v2.1 发布 — NSA 在协议定稿前介入，可能影响最终安全模型
- **生态影响**：NSA 背书意味着 MCP 进入「合规需求」视野 — 政府、金融、医疗等受监管行业采用 MCP 时需要回答「是否符合 NSA 指南」

**为什么独立于已有的 MCP Protocol Evolution 任务**：`mcp-protocol-evolution` 覆盖的是协议架构演进（Streamable HTTP、无状态化、性能提升）和 `webmcp-standard` 覆盖 WebMCP 标准。NSA 安全指南是一个全新的维度 — **安全审查与合规**，对 Tony 的 Hermes（重度依赖 MCP）有直接的架构影响。

## Source

- URL: https://www.reedsmith.com/our-insights/blogs/viewpoints/102mvg9/nsa-publishes-security-guidance-on-designing-ai-systems-with-model-context-protoc/
- Source note: 2026-06-06 上午 curated-scout digest #9
- Captured evidence: `00-Inbox-AI/hermes/curated-scout/20260606-090023-digest.md` #47-#49

## Suggested Domain

`Security-Architecture`

## Desired Output

decision memo

## Proposed Canonical Destination

- `10-Knowledge/Security/05-Topics/mcp-security-guidance.md`
- `20-Maps/security-threat-model.md`（更新 MCP 安全部分）

## Codex Handoff Contract

- Hermes writes this task only in `00-Inbox-AI/learning-tasks/pending/`.
- Hermes may attach drafts in `00-Inbox-AI/hermes/`.
- Hermes must not write directly into `10-Knowledge/`, `20-Maps/`, `30-Playbooks/`, `40-Projects/`, `60-Agents/`, or `90-Agent-System/`.
- Codex researches, restructures, and prepares the learning package.
- Tony reviews before canonical promotion.

## 研究路径建议

1. 获取并精读 NSA 安全指南原文（通过 ReedSmith 法律分析博客或直接搜索 NSA 公开文件）
2. 提炼 NSA 关注的 MCP 安全维度：
   - 传输层安全（Streamable HTTP vs stdio 的风险差异）
   - 工具权限模型（MCP Server 的 capability 声明与验证）
   - 数据流安全（Agent ↔ MCP Server 之间的数据泄露风险）
   - 供应链安全（第三方 MCP Server 的信任模型）
3. 对照 Hermes 当前的 MCP 使用模式，逐条评估合规性与风险
4. 对比其他安全框架（OWASP LLM Top 10、NIST AI RMF）的覆盖差异
5. 产出：Hermes MCP 安全评估 + 改进建议优先级列表

## Suggested Review Date

`2026-06-13`

## Safety Notes

本任务涉及对 NSA 公开安全指南的分析，不涉及机密或受限信息。研究结论用于强化 Tony 个人 Agent 系统的安全设计。

## Hermes Recommendation

- Decision: `study`
- Rationale: Tony 的 Hermes 重度依赖 MCP（exa 搜索、Camofox 浏览器、文件系统访问等）。NSA 的介入意味着 MCP 安全不再是「社区最佳实践」而是「国家级安全标准」。理解这份指南对 Hermes 的 MCP 安全架构设计有直接参考价值。与 `mcp-protocol-evolution`（协议演进）和 `webmcp-standard`（Web 标准化）形成 MCP 三角研究。

## Follow-Up Proposal

- Suggested review cadence: 2 周（MCP RC 正式发布前重新评估）
- Suggested spaced review prompt: 「NSA MCP 安全指南中，哪一条对 Hermes 当前架构影响最大？」
