---
title: LLMOps 与 AgentOps 架构师视角
type: topic
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# LLMOps 与 AgentOps 架构师视角

> LLMOps / AgentOps 的本质是：让模型、prompt、数据、工具、评测、发布和反馈进入可治理的软件工程体系。

## 架构师要回答的问题

- prompt、model、dataset、eval、tool 和 workflow 是否有版本？
- AI 输出质量如何回归？
- AI 线上行为如何观测？
- 模型或 prompt 变更如何灰度、回滚、审计？
- 成本、延迟和质量如何一起治理？

## 平台能力分层

| 层 | 能力 |
|---|---|
| Gateway | model routing、fallback、quota、policy |
| Registry | prompt、model、dataset、eval、tool、workflow |
| Eval | offline eval、regression、red team、human review |
| Observability | trace、retrieval、tool call、cost、latency |
| Release | canary、shadow、A/B、rollback、approval |
| Feedback | user feedback、incident、annotation、fine-tuning candidates |
| Governance | audit、policy、risk、compliance evidence |

## 关键设计决策

### 是否需要模型网关

需要模型网关的信号：

- 多模型、多供应商、多团队共用。
- 需要统一鉴权、限流、审计和成本分摊。
- 需要 fallback、routing、cache 和 policy。

### Eval 放在哪里

- 开发阶段：prompt / chain / tool 的本地回归。
- CI 阶段：关键 golden set 必过。
- 发布阶段：shadow / canary 观察。
- 线上阶段：采样人工 review 和 incident-fed eval。

### Trace 要记录什么

- user request
- prompt version
- retrieved chunks
- model version
- tool calls
- latency / token / cost
- policy decision
- final output
- human feedback

## 常见失败模式

- prompt 直接写在代码里，没有版本和回滚。
- 只做离线 eval，不看线上反馈。
- trace 只记录最终答案，看不到 retrieval 和 tool call。
- 模型切换没有回归测试。
- 成本失控后才开始做预算。

## 架构师交付物

- LLMOps / AgentOps 平台架构
- AI release gate
- eval registry 设计
- prompt/model/dataset 版本策略
- observability dashboard
- incident-fed eval 流程

## 关联

- [[../../AI-Engineering/08-Maps/MLOps 与 LLMOps 工程图|MLOps 与 LLMOps 工程图]]
- [[../../AI-Engineering/08-Maps/Agent Evaluation and Governance Map|Agent Evaluation and Governance Map]]
- [[../../AI-Engineering/06-Projects/Enterprise LLMOps/项目总览|Enterprise LLMOps]]
- [[../../AI-Engineering/04-Evaluation/评测索引|评测索引]]

