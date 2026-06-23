---
title: 哪些 AI Foundations 争论今天还活着
type: guide
status: active
updated: 2026-04-03
---

# 哪些 AI Foundations 争论今天还活着

## 这页解决什么问题

很多人会把 Foundations 当成“历史前情提要”。

但更准确的说法是：

很多今天最重要的 AI 争论，其实都是旧争论的新版本。

## 第一组：规则还是学习

历史版本：

- [[AI-Foundations/05-Topics/Symbolic AI|Symbolic AI]]
- [[AI-Foundations/05-Topics/Connectionism|Connectionism]]

今天的版本：

- 结构化 workflow vs 开放式 agent
- rules / policy / guardrails vs end-to-end learned behavior
- tool routing / orchestration vs “让模型自己决定”

为什么还活着：

- 因为“显式结构”和“隐式学习”始终是在 trade off，不会只剩一边

## 第二组：推理到底是什么

历史版本：

- [[AI-Foundations/05-Topics/Search and Planning|Search and Planning]]
- [[AI-Foundations/05-Topics/Knowledge Representation|Knowledge Representation]]

今天的版本：

- reasoning model 到底是在推理，还是在更强的 pattern completion
- planning loop 是真实规划，还是生成式近似
- agent 的“思考链”到底应不应该外显成 state machine

为什么还活着：

- 因为一旦系统要跨步骤、跨工具、跨状态运行，search / planning 问题就会重新出现

## 第三组：知识应该怎样表示

历史版本：

- [[AI-Foundations/05-Topics/Knowledge Representation|Knowledge Representation]]

今天的版本：

- knowledge graph / rules / schema
- embedding / latent representation
- RAG、memory、tool schema、structured context

为什么还活着：

- 因为“知识放在哪里、以什么形式被系统使用”依然决定可解释性、更新成本和失败模式

## 第四组：泛化到底来自哪里

历史版本：

- [[AI-Foundations/05-Topics/Statistical Learning|Statistical Learning]]
- [[AI-Foundations/02-Foundations/AI 基础双语术语表|AI 基础双语术语表]] 里的 `generalization / overfitting / inductive bias`

今天的版本：

- scale 能不能自动带来更好的 generalization
- benchmark 分数是否等于真实世界泛化
- eval、online eval、drift、OOD 到底怎么理解

为什么还活着：

- 因为“大模型很强”并没有让泛化问题消失，只是把它放大了

## 第五组：能力和可控性怎么平衡

历史版本：

- [[AI-Foundations/05-Topics/Philosophy of AI|Philosophy of AI]]
- [[AI-Foundations/04-Papers/Computing Machinery and Intelligence（1950）|Computing Machinery and Intelligence（1950）]]

今天的版本：

- alignment
- AI safety
- approval gates
- rollback
- model autonomy / agent autonomy

为什么还活着：

- 因为一旦 AI 进入真实组织，问题就不再只是“会不会做”，而是“谁负责、怎么控”

## 一条更稳的读法

1. 先看 [[AI 历史主时间线：从符号主义到大模型]]
2. 再看 [[从 Symbolic AI 到 LLM Agent：旧问题的新形式]]
3. 然后回 [[AI-Foundations/03-Paradigms/范式索引|范式索引]]
4. 最后去现代专题页验证这些争论今天长成什么样

## 关联

- [[我想通过作者、论文与时间线理解 AI]]
- [[AI-Foundations/专题总览|AI-Foundations]]
