---
title: AI 时代架构师能力全景
type: topic
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# AI 时代架构师能力全景

> 这页沉淀我们的第一轮讨论：AI 时代，架构师应该具备哪些能力。

## 一句话定义

AI 架构师不是“会调模型 API 的后端架构师”，也不是“会训练模型的算法工程师”。

AI 架构师要能把 `业务流程、模型能力、数据知识、工具系统、评测反馈、安全治理、成本性能和组织落地` 设计成一个可运行、可演进、可审计的智能系统。

## 传统架构师与 AI 架构师的差异

| 维度 | 传统互联网架构师 | AI 时代架构师 |
|---|---|---|
| 核心对象 | 服务、数据库、缓存、消息、流量 | 模型、上下文、工具、记忆、评测、反馈 |
| 系统性质 | 相对确定性 | 概率性、涌现性、不稳定性 |
| 质量保障 | 单元测试、集成测试、压测、监控 | eval、golden set、人工反馈、红队、在线观测 |
| 数据重点 | 交易数据、行为数据、日志、指标 | 训练数据、知识库、向量索引、prompt、反馈数据 |
| 失败模式 | 超时、宕机、数据不一致、容量不足 | 幻觉、越权、误调用工具、上下文污染、数据泄露 |
| 治理重点 | SLA、成本、稳定性、安全、合规 | 模型行为、权限边界、审计、风险、上线门槛 |

## 七层能力模型

### 1. 业务重构能力

AI 架构师首先要能判断：什么业务流程值得 AI 化。

关键问题：

- 哪些任务是问答、搜索、生成、总结、分类、抽取、规划、执行？
- 哪些流程适合 Copilot，哪些适合 Agent？
- 哪些环节必须 human-in-the-loop？
- AI 带来的是效率提升、质量提升、体验提升，还是新业务能力？

典型输出：

- AI use case portfolio
- ROI / 风险 / 数据准备度评估
- AI 工作流改造图

### 2. 模型理解能力

架构师不一定要训练 foundation model，但必须理解模型能力边界。

必须理解：

- token、context window、embedding、multimodal
- prompt、system message、tool calling、structured output
- RAG、fine-tuning、LoRA、distillation 的适用边界
- 幻觉、偏见、能力不稳定、上下文遗忘

典型判断：

- 这个问题应该 prompt 解决、RAG 解决、fine-tuning 解决，还是流程重构解决？
- 什么时候选大模型，什么时候选小模型，什么时候用规则/搜索/传统 ML？

### 3. AI 应用架构能力

AI 应用架构的核心不只是调用模型，而是设计 `model + context + tools + workflow + memory + permission`。

必须掌握：

- RAG 架构：chunking、embedding、retrieval、rerank、grounding、citation
- Agent 架构：planning、tool use、state、memory、approval、rollback
- Workflow 架构：确定性流程与模型判断如何组合
- Tool Gateway：工具注册、权限、审计、限流、审批
- Human-in-the-loop：何时人工确认、何时自动执行

典型输出：

- RAG 架构图
- Agent workflow 图
- 工具调用权限矩阵
- 上下文与记忆设计

### 4. 数据与知识架构能力

AI 系统的数据架构不只是数据仓库，还包括知识、上下文和反馈。

必须掌握：

- 数据质量、数据血缘、权限和敏感数据治理
- 文档知识库、向量库、metadata、权限过滤
- eval dataset、golden set、online feedback
- 数据新鲜度、grounding、引用和可追溯

典型判断：

- 企业知识库是否能支持 RAG？
- 向量检索为什么召回错？
- 用户是否有权限看到被检索出来的内容？
- 反馈数据能否用于改进模型或 prompt？

### 5. AI 工程平台能力

传统架构师最容易迁移成功的地方，是工程化和平台化。

必须掌握：

- 模型网关、路由、fallback、限流、缓存
- prompt registry、model registry、dataset registry
- LLMOps / AgentOps：eval、observability、trace、cost、latency
- 灰度、回滚、shadow rollout、A/B testing
- 推理服务：batching、KV cache、prefill/decode、GPU/CPU 成本

典型输出：

- LLMOps 平台架构
- AI observability 指标体系
- 模型/Prompt 发布门禁
- 成本与延迟优化方案

### 6. 安全与治理能力

AI 系统把安全边界从接口扩展到了模型行为、上下文、工具和数据。

必须掌握：

- prompt injection、jailbreak、data exfiltration
- tool abuse、agent 越权、memory poisoning
- 隐私、版权、合规、审计、模型行为治理
- AI red teaming、safety eval、security eval
- approval、audit、policy、release gate

典型输出：

- AI 安全威胁模型
- 工具调用审批策略
- AI 上线门槛
- AI 事件响应流程

### 7. 组织与架构领导力

AI 架构师最终要能推动组织转型。

必须掌握：

- AI use case portfolio 管理
- 平台团队、业务团队、数据团队、安全法务的协作边界
- AI 项目从 POC 到生产的阶段门
- 组织学习、开发者体验和变更管理

典型输出：

- AI adoption roadmap
- AI platform operating model
- AI governance council / review board
- 架构评审机制

## 能力矩阵

| 能力 | L1 知道 | L2 能做 | L3 能设计 | L4 能治理 | L5 能带团队 |
|---|---|---|---|---|---|
| 模型能力 | 知道基本概念 | 会调用模型 | 能选型和组合 | 能设上线门槛 | 能定义企业模型策略 |
| RAG | 知道向量检索 | 能做原型 | 能设计权限和评测 | 能运营知识质量 | 能建设知识平台 |
| Agent | 知道 tool calling | 能做 workflow | 能设计状态/权限/审批 | 能治理风险和回滚 | 能建设 Agent 平台 |
| LLMOps | 知道 eval/trace | 能接观测 | 能设计发布流程 | 能运营指标和成本 | 能建设平台团队 |
| AI 安全 | 知道注入/泄露 | 能做基础防护 | 能威胁建模 | 能红队和审计 | 能建立治理体系 |
| 业务落地 | 能识别场景 | 能做 POC | 能设计端到端方案 | 能度量 ROI | 能推动组织采用 |

## 最重要的架构师心智变化

### 从 API thinking 到 capability thinking

不是“接一个模型 API”，而是引入一个不稳定但强大的能力系统。

### 从 request-response 到 workflow-runtime

AI 应用不是一次请求一次响应，而是多步推理、工具调用、状态流转和人工确认。

### 从 testing 到 evaluation

AI 系统需要持续评测，而不是只做传统测试。

### 从 permission 到 trust boundary

AI 系统的权限边界包括数据、上下文、工具、记忆、模型输出和人工审批。

### 从上线到持续治理

AI 系统上线后会因为模型、数据、prompt、业务和用户行为变化而持续漂移。

## 关联

- [[../06-Maps/AI 架构师迁移地图|AI 架构师迁移地图]]
- [[./传统互联网架构师转型 AI 架构师路线|传统互联网架构师转型 AI 架构师路线]]
- [[../../AI-Engineering/08-Maps/AI Engineering Stack Map|AI Engineering Stack Map]]
- [[../../AI-Engineering/08-Maps/MLOps 与 LLMOps 工程图|MLOps 与 LLMOps 工程图]]
- [[../../AI-Engineering/08-Maps/AI Security Engineering Map|AI Security Engineering Map]]

