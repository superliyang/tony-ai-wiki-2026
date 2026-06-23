---
title: 第 5 章：RAG、Agent 与本地应用开发
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# 第 5 章：RAG、Agent 与本地应用开发

## 本章目标

把模型变成真正的系统，而不是停留在 notebook 里。

## 这章要解决的问题

- 模型怎么接入外部知识
- 模型怎么接工具
- agent 如何维护状态
- 本地应用如何做 trace、eval、logging
- 什么情况下本地 RAG / agent 已经够用，什么情况下要开始考虑云上服务

## 推荐项目顺序

### 项目 1：本地 RAG 文档问答

目标：理解 retrieval、chunking、embedding、reranking、answer quality。

### 项目 2：带工具调用的本地 agent

目标：理解 tool use、planning、memory、error handling。

### 项目 3：最小 observability 接入

目标：理解 trace、span、prompt version、eval sample。

## 本章输出物

- 一个本地 RAG 原型
- 一个本地 agent 原型
- 一份失败查询 / bad cases 集合
- 一份最小 trace / eval 记录

## 常见误区

- 把 RAG 当成“只要能搜就行”
- 把 agent 当成“会自动调用工具就够了”
- 没有 bad-case 集合，导致系统无法迭代

## 继续阅读

- [[第 6 章：从 Mac 实验室到云上系统]]
- [[../../07-Topics/Mac 上的 RAG、Agent 与本地应用开发|Mac 上的 RAG、Agent 与本地应用开发]]
- [[../../07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]
