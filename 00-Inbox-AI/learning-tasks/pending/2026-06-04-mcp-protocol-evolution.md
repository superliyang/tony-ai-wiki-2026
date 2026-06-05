---
title: "MCP 协议深度研究：Streamable HTTP + 无状态架构演进"
created: 2026-06-04
updated: 2026-06-04
status: pending
owner: hermes
priority: P1
domain: AI-Engineering
review_after: 2026-06-11
tags:
  - learning-task
  - hermes
  - mcp
  - agent-infrastructure
  - protocol-evolution
---

# MCP 协议深度研究：Streamable HTTP + 无状态架构演进

## Why Now

MCP 协议正经历从"可用"到"好用"的关键转折——过去一周内，3 篇独立技术分析（AgentMarketCap、byteiota、多篇云厂商公告）同时指向两个核心变更：

1. **MCP Streamable HTTP**（v2.1）：延迟降低 95%，吞吐量提升 10 倍
2. **MCP 无状态化**（2026-07-28 RC）：架构简化但引入兼容性断裂

同时，**微软**（Azure Functions MCP 扩展、Cosmos DB MCP 工具包）、**Google**（GCS MCP Server）、**AWS**（Bedrock AgentCore MCP 支持）三大云厂商在 Build 2026 前后同步加码 MCP，标志着协议从社区标准走向云原生基础设施。

Tony 的 Hermes 重度依赖 MCP 作为 Agent 工具调用和通信层。理解协议演进方向直接影响系统架构决策。

## Source

- URL: https://agentmarketcap.ai/blog/2026/06/07/mcp-v2-1-streamable-http-95-percent-latency-reduction
- URL: https://byteiota.com/mcp-stateless-2026-release-candidate/
- URL: https://cloud.google.com/blog/topics/developers-practitioners/build-ai-agents-faster-with-gcs-google-cloud-storage-mcp-server
- URL: https://devblogs.microsoft.com/cosmosdb/announced-at-ms-build-2026-azure-cosmos-db-mcp-toolkit-semantic-reranking-global-secondary-indexes-and-more/
- URL: https://techcommunity.microsoft.com/blog/appsonazureblog/azure-functions-mcp-extension-whats-new-at-build-2026/4524099
- URL: https://aws.amazon.com/blogs/machine-learning/extending-mcp-support-for-amazon-bedrock-agentcore-gateway-2/
- Source note: 2026-06-03 ~ 06-04 连续 3 批次 curated-scout 均将 MCP 列为建议关注首位
- Captured evidence: `00-Inbox-AI/hermes/curated-scout/20260604-090044-summary.md` (#6), `20260603-210040-summary.md` (#6, #7), `20260603-150019-summary.md` (#7, #8), `20260603-091612-summary.md` (#6, #7, #8)

## Suggested Domain

`AI-Engineering` — MCP 是 Agent 基础设施层的核心协议，直接影响工具调用、服务间通信和系统架构

## Desired Output

- **comparison map**: MCP 当前版本 vs Streamable HTTP vs 无状态 RC — 协议层差异、性能数据、兼容性矩阵
- **decision memo**: 对 Hermes 系统的 MCP 升级路径建议 — 立即行动 vs 观察等待 vs 分阶段迁移
- 附带：三大云厂商 MCP 支持全景对比（Azure / GCP / AWS）

## Suggested Review Date

`2026-06-11` — 一周窗口，赶在无状态 RC（7/28）之前完成基础评估

## Safety Notes

- MCP 协议变更可能影响 Hermes 所有 MCP 工具调用的兼容性
- 无状态 RC 引入的 breaking changes 需要在测试环境验证后再推生产
- 关注 MCP 协议安全模型（权限控制、认证）的同步变更

## Hermes Recommendation

- Decision: `study`
- Rationale: MCP 是 Hermes 的核心基础设施依赖。协议正在经历 18 个月来最大的架构变更（Streamable HTTP + 无状态化），且三大云厂商同步加码。现在投入 Codex 深研，可以在 RC 正式发布前形成决策基础，避免被动升级。这是本周 P1 优先级的学习任务。
