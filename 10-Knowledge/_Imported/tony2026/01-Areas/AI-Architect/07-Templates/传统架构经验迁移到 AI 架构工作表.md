---
title: 传统架构经验迁移到 AI 架构工作表
type: template
status: active
domain: AI-Architect
created: 2026-05-09
updated: 2026-05-09
---

# 传统架构经验迁移到 AI 架构工作表

> 目标：把已有的互联网架构经验，翻译成 AI 架构师能识别的能力证据。不是“重新做人”，是把旧能力接到新问题上。

## 一句话原则

传统架构师不缺底层能力，常缺的是 AI 语境下的表达：

`稳定性 -> AI SLO / fallback / incident`

`权限系统 -> RAG ACL / tool permission / trust boundary`

`数据平台 -> knowledge pipeline / eval dataset / data governance`

`网关平台 -> model gateway / routing / quota / cost`

`DevOps -> LLMOps / AgentOps / release gate`

## 1. 经验盘点

| 传统项目 | 我的角色 | 规模/复杂度 | 核心问题 | 可迁移能力 |
|---|---|---|---|---|
|  |  | QPS / 用户 / 数据量 / 团队规模 |  |  |

优先选择这类项目：

- 高并发网关。
- 权限和多租户系统。
- 数据平台 / 搜索 / 推荐 / 知识库。
- 流程审批 / 工作流 / 低代码平台。
- SRE / 稳定性 / 监控告警。
- DevOps / 平台工程 / 发布系统。
- 安全合规 / 风控 / 审计系统。

## 2. 迁移映射表

| 传统经验 | AI 架构表达 | 可证明能力 |
|---|---|---|
| API Gateway | Model Gateway / Tool Gateway | 鉴权、限流、路由、审计、fallback |
| 搜索系统 | RAG Retrieval Layer | 召回、排序、索引、相关性、权限过滤 |
| 权限系统 | Trust Boundary / RAG ACL / Tool Permission | 最小权限、身份透传、越权防护 |
| 数据平台 | Knowledge Pipeline / Eval Dataset | 数据质量、血缘、元数据、版本、Owner |
| 监控平台 | AI Observability / Trace | 模型、prompt、retrieval、tool、cost 复盘 |
| 发布系统 | AI Release Gate | prompt/model/index/policy 灰度和回滚 |
| 稳定性治理 | AI SLO / Incident | 质量、安全、成本、延迟、可用性 |
| 成本治理 | AI FinOps | token、模型路由、cache、预算、归因 |
| 工作流系统 | Bounded Agent Workflow | 状态机、人审、工具编排、幂等 |
| 安全系统 | AI Threat Model | prompt injection、tool abuse、数据泄露 |

## 3. 项目改写公式

把旧项目改写成 AI 架构证据，用这个公式：

> 我过去解决的是 `传统系统问题`，本质上训练了 `可迁移架构能力`。在 AI 系统里，这个能力可以迁移到 `AI 架构问题`，具体体现为 `生产化证据`。

示例：

> 我过去做过 API 网关，解决的是服务鉴权、限流、路由、熔断和审计问题。这个能力可以迁移到 AI 的 model gateway 和 tool gateway：控制哪些应用能调用哪些模型和工具，如何做配额、fallback、成本归因和高风险工具审计。

## 4. 项目证据提取

每个传统项目至少提取 5 类证据：

| 证据 | 问题 |
|---|---|
| 业务目标 | 当时为什么做这个系统？ |
| 架构复杂度 | 流量、数据、团队、依赖、风险在哪里？ |
| 关键取舍 | 你做过哪些技术或组织取舍？ |
| 生产化能力 | 稳定性、监控、灰度、回滚、安全、成本怎么做？ |
| 复盘能力 | 出过什么问题，如何修复，如何制度化？ |

## 5. 迁移到 AI 作品集

| 目标作品集 | 可迁移旧经验 | 如何改写 |
|---|---|---|
| 企业知识库 RAG | 搜索、知识库、数据平台、权限系统 | 强调知识治理、检索质量、权限、引用、eval |
| 审批型 Agent | 工作流、审批系统、权限、审计 | 强调 bounded agent、tool gateway、人审、幂等、回滚 |
| 企业 LLMOps 平台 | API 网关、DevOps、SRE、平台工程 | 强调 model gateway、prompt registry、eval gate、trace、FinOps |
| AI 安全治理 | 安全合规、风控、审计 | 强调 threat model、risk register、策略、红队和上线阻断 |
| AI 成本优化 | 成本平台、网关、容量治理 | 强调模型路由、cache、quota、budget、cost per task |

## 6. 个人能力画像改写

### 旧表达

> 我做过高并发后端和微服务治理。

### AI 架构表达

> 我具备平台化和生产化治理经验，可以迁移到 AI model gateway、tool gateway、LLMOps 和 AgentOps：包括鉴权、限流、路由、fallback、trace、成本归因、灰度和回滚。

### 旧表达

> 我做过数据平台。

### AI 架构表达

> 我理解数据质量、元数据、血缘、权限和治理，这可以迁移到 RAG knowledge pipeline 和 eval dataset 设计：确保模型依据可信、可追溯、可更新的知识工作。

### 旧表达

> 我做过稳定性保障。

### AI 架构表达

> 我能把传统 SRE 方法迁移到 AI 系统：不仅关注 availability，还关注 quality、safety、cost、latency，并设计 trace、release gate、fallback、incident 和 bad case 回灌。

## 7. 面试自检

回答前问自己：

- 我讲的是工具，还是架构问题？
- 我有没有说清楚业务目标？
- 我有没有说清楚 AI 的新增风险？
- 我有没有把旧经验迁移到 eval、trace、安全、成本、上线？
- 我有没有失败案例和复盘？

## 8. 工作表

| 我的传统项目 | 可迁移能力 | 对应 AI 架构问题 | 可包装作品集 | 缺的证据 |
|---|---|---|---|---|
|  |  |  |  |  |

## 关联

- [[../11-Case-Library/案例库索引|案例库索引]]
- [[../09-Portfolio/作品集样例索引|作品集样例索引]]
- [[../10-Interview-Kit/AI 架构师 STAR 项目表达样例|AI 架构师 STAR 项目表达样例]]
- [[./AI 架构师作品集模板|AI 架构师作品集模板]]
