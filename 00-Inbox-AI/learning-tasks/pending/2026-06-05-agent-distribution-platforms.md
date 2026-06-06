---
title: "Agent 分发渠道的平台化：Apple/Google/Microsoft 三极格局的 Agent 入口策略"
created: 2026-06-05
updated: 2026-06-05
status: pending
owner: hermes
priority: P2
domain: "AI-Platform-Economics"
review_after: "2026-06-14"
tags:
  - learning-task
  - hermes
  - agent-distribution
  - platform-economics
  - app-store
---

# Agent 分发渠道的平台化：Apple/Google/Microsoft 三极格局的 Agent 入口策略

## Why Now

**2026-06-04，Apple 批准首个第三方 AI Agent (Poke) 进入 Messages for Business** — 这是 "Agent App Store" 的破冰时刻，类比 2008 年 App Store 对移动应用的催化作用。

交叉信号：
- **WWDC 2026 Siri LLM 重构** — 苹果生态全面拥抱 Agent
- **Apple Intelligence 更新** — 将 AI 能力嵌入 Messages / Siri / 第一方应用
- **Google Cloud GCS MCP Server** — Google 将存储产品标准化为 Agent 可调用工具
- **Microsoft Foundry** — 从 Agent 开发平台到分发管道的完整链路

"Agent 怎么分发" 正在成为一个与 "Agent 怎么构建" 同等重要的问题。平台级分发决定：
- Agent 的可达用户规模 (consumer vs enterprise)
- Agent 的能力边界 (平台对工具调用/数据访问的权限控制)
- Agent 的商业模式 (IAP？订阅？API 按调用计费？)

核心问题：**Apple/Google/Microsoft 三家的 Agent 分发策略有何差异化？这对 Agent 开发者意味着什么？**

## Source

- URL: https://techcrunch.com/2026/06/04/apple-approves-poke-as-the-first-ai-agent-on-its-messages-for-business-platform/
- URL: https://techcrunch.com/2026/06/04/what-to-expect-from-wwdc-2026-siris-highly-anticipated-revamp-and-apple-intelligence-updates/
- URL: https://cloud.google.com/blog/topics/developers-practitioners/build-ai-agents-faster-with-gcs-google-cloud-storage-mcp-server
- URL: https://devblogs.microsoft.com/foundry/agent-service-build2026/ (参考)
- Source note: Apple Poke Agent 是 2026-06-04 下午增量扫描的头条，信号质量极高
- Captured evidence: `00-Inbox-AI/hermes/curated-scout/20260604-170000-afternoon-digest.md` (#2), `20260604-090044-digest.md` (#3, #8)

## Suggested Domain

`AI-Platform-Economics` — Agent 分发渠道的平台化涉及平台经济学、开发者生态和商业模式设计，与 Tony 对 AI 商业和战略的关注高度吻合。

## Desired Output

- **comparison map**: Apple vs Google vs Microsoft Agent 分发策略对比 (5 个维度: 分发渠道类型、开发者准入门槛、工具调用/数据访问权限、分成/商业模式、生态锁定策略)
- **learning package**:
  - App Store 类比分析: Agent App Store 与 2008 App Store 的异同
  - 平台级 Agent 分发的关键设计决策 (权限模型、审核机制、分发范围)
  - 对 Agent 开发者的战略启示: 应该先押注哪个平台？多平台策略的风险？
  - 附带: Tony 如果做 Agent 产品，分发策略的初步建议

## Suggested Review Date

`2026-06-14` — WWDC 2026 将于 6/9 举行，此后 Siri 重构和 Apple Intelligence 的更详细信息将出炉

## Safety Notes

- 关注平台级 Agent 分发的隐私和安全审核机制 (Apple 可能最为严格)
- 关注平台锁定 (vendor lock-in) 风险 — Agent 依赖特定平台的 MCP Server/API 后难以迁移

## Hermes Recommendation

- Decision: `study`
- Rationale: Agent 分发的平台化是"基础设施工具化"(已有 MCP P1) 和"平台工业化"(已有 Foundry P1) 之后的自然延伸。如果说 MCP 是"协议层"、Foundry 是"开发层"，那 Apple Poke + Google Cloud MCP 就是"分发层"。理解三层的全貌，才能在 Agent 生态中找到正确的定位。P2 优先级低于 Agent 记忆和模型架构，但 WWDC 前完成为佳。
