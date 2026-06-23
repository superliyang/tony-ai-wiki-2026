---
title: AI 架构师岗位能力画像
type: topic
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# AI 架构师岗位能力画像

> 这页回答：如果一个人要被称为 AI 时代的架构师，岗位能力应该长什么样。

## 一句话画像

AI 架构师是能把 `业务场景、模型能力、数据知识、工程平台、安全治理、成本性能、组织落地` 串成可生产运行系统的人。

## 三类岗位形态

### 1. AI 应用架构师

关注：

- RAG、Agent、Workflow、Copilot、业务系统集成。
- 模型能力如何嵌入具体业务流程。
- AI 功能如何从 POC 变成可上线产品。

典型产物：

- AI 应用架构设计。
- RAG / Agent workflow。
- 工具调用权限矩阵。
- 业务指标和评测方案。

### 2. AI 平台架构师

关注：

- LLMOps、AgentOps、模型网关、评测平台、观测、发布、成本治理。
- 多团队、多模型、多供应商、多应用的统一平台能力。

典型产物：

- 模型网关架构。
- Prompt / Model / Dataset / Eval registry。
- AI 发布门槛。
- AI 平台运营指标。

### 3. AI 治理架构师

关注：

- AI Security、AI Governance、数据治理、风险管理、审计、合规。
- 模型行为、工具调用、权限边界和人机责任。

典型产物：

- AI 风险评审机制。
- AI 安全威胁模型。
- AI 上线审批流。
- AI 事件响应和审计证据。

## 能力雷达

| 能力域 | L3 可独立设计 | L4 可治理 | L5 可带团队 |
|---|---|---|---|
| 业务与场景 | 能选择 AI 场景并定义任务边界 | 能管理 use case portfolio | 能推动组织 AI adoption |
| 模型与模式 | 能选择 prompt/RAG/agent/fine-tuning | 能定义模型策略和上线门槛 | 能建立企业 AI 技术路线 |
| 数据与知识 | 能设计 RAG 和权限过滤 | 能治理知识质量和数据使用 | 能建设企业知识平台 |
| 工程平台 | 能设计 LLMOps / AgentOps | 能治理发布、观测、成本 | 能建设 AI 平台团队 |
| 安全治理 | 能做 AI threat model | 能建立红队、审计、incident 流程 | 能建立企业 AI governance |
| 组织表达 | 能写清架构方案 | 能做跨团队评审 | 能影响管理层和业务决策 |

## 和传统架构师的连续性

传统架构能力不是被替代，而是迁移：

- API Gateway -> Model Gateway / Tool Gateway
- 数据平台 -> Knowledge Platform / Eval Dataset
- 服务治理 -> Agent Runtime / Workflow Governance
- 可观测性 -> Prompt/Retrieval/Tool Trace
- 测试发布 -> Eval Gate / Shadow Rollout
- 安全合规 -> AI Trust Boundary / AI Governance

## 面试中的高信号表现

高信号候选人会说：

- “这个场景不一定需要 agent，workflow + human approval 更稳。”
- “RAG 质量要拆成 retrieval quality 和 answer faithfulness。”
- “工具调用要做权限分级、审批、幂等、回滚和审计。”
- “AI 上线门槛要包括 eval、安全、成本、延迟和人工接管。”
- “POC 成功不代表生产可用，关键是持续评测和运营闭环。”

低信号候选人常说：

- “接个大模型 API 就行。”
- “RAG 就是向量库。”
- “Agent 会自己规划。”
- “Prompt 调好就稳定了。”
- “先上线再慢慢看。”

## 关联

- [[./AI 时代架构师能力全景|AI 时代架构师能力全景]]
- [[./传统互联网架构师转型 AI 架构师路线|传统互联网架构师转型 AI 架构师路线]]
- [[../10-Interview-Kit/AI 架构师面试专题总览|AI 架构师面试专题总览]]

