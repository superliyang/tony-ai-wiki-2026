---
title: AI 成本、延迟与容量架构师视角
type: topic
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# AI 成本、延迟与容量架构师视角

> AI 系统的成本和延迟不是上线后优化项，而是架构设计的一部分。

## 架构师要回答的问题

- 每次成功任务的成本是多少？
- 用户可接受的 p95 延迟是多少？
- 哪些请求需要大模型，哪些可以小模型、缓存、规则或搜索解决？
- 峰值容量、并发、token 预算如何估算？
- 成本失控时如何降级？

## 成本构成

| 成本项 | 说明 |
|---|---|
| 输入 token | 用户输入、系统提示、上下文、检索内容 |
| 输出 token | 模型生成内容 |
| embedding | 文档索引和查询向量化 |
| rerank | 检索后重排 |
| tool calls | 外部 API、数据库、浏览器、代码执行 |
| inference infra | GPU/CPU、模型服务、缓存 |
| observability | trace、日志、评测、存储 |
| human review | 人工审核、标注、反馈 |

## 延迟构成

| 链路 | 优化方向 |
|---|---|
| 鉴权与路由 | 就近路由、缓存权限、减少同步调用 |
| 检索 | 索引优化、metadata filter、top-k 控制、rerank 策略 |
| 模型调用 | 模型选择、streaming、并行调用、fallback |
| 工具调用 | 并发、超时、幂等、异步任务 |
| 输出后处理 | structured output、校验、异步审计 |

## 架构优化手段

- prompt 压缩和上下文裁剪。
- query classification：简单问题走小模型或搜索。
- semantic cache / response cache。
- embedding cache。
- retrieval top-k 和 rerank 策略优化。
- streaming 降低体感延迟。
- batch / async workflow。
- 模型路由和 fallback。
- 任务拆分和后台执行。

## 关键指标

- cost per request
- cost per successful task
- p50 / p95 / p99 latency
- tokens per request
- retrieval latency
- tool latency
- cache hit rate
- fallback rate
- timeout rate

## 常见失败模式

- POC 用少量请求很便宜，上线后 token 和日志成本暴涨。
- 把长文档全部塞进 context。
- 所有任务都用最大模型。
- 没有缓存、没有降级、没有预算。
- 只看单次请求成本，不看成功任务成本。

## 架构师交付物

- AI cost model
- latency budget
- capacity plan
- model routing policy
- caching strategy
- degradation plan

## 关联

- [[../../AI-Engineering/07-Topics/Cost, Latency, and Safety Tradeoffs|Cost, Latency, and Safety Tradeoffs]]
- [[../../AI-Engineering/07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]]
- [[../../AI-Engineering/08-Maps/Inference and Serving Map|Inference and Serving Map]]

