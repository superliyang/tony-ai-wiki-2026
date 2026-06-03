---
title: 从 Symbolic AI 到 LLM Agent：旧问题的新形式
type: guide
status: active
updated: 2026-04-03
---

# 从 Symbolic AI 到 LLM Agent：旧问题的新形式

## 这页解决什么问题

很多人看今天的 agent、memory、tool use、eval，会误以为这些都是全新的问题。

更稳的看法是：

很多问题都不是新的，只是从旧范式换到了新的系统外壳里。

## 五组最值得反复对照的映射

### 1. Search / Planning -> agent planning loop

旧问题：

- [[AI-Foundations/05-Topics/Search and Planning|Search and Planning]]

新形式：

- planning loop
- task decomposition
- tool selection
- state machine

关键理解：

- agent 并没有让 planning 问题消失，只是让它从经典算法形式转成了生成式、workflow 化和 runtime 化

### 2. Knowledge Representation -> RAG / memory / tool schema

旧问题：

- [[AI-Foundations/05-Topics/Knowledge Representation|Knowledge Representation]]

新形式：

- RAG
- structured context
- memory
- tool schema

关键理解：

- “知识如何被表示和调用”今天仍然决定系统是否可更新、可解释、可追责

### 3. Symbolic AI -> workflow / policy / guardrail

旧问题：

- [[AI-Foundations/05-Topics/Symbolic AI|Symbolic AI]]

新形式：

- bounded workflow
- guardrail
- release gate
- policy-as-code / policy-as-data

关键理解：

- 今天很多最可靠的 AI 系统，仍然靠显式结构来兜底

### 4. Connectionism -> LLM / multimodal / latent reasoning

旧问题：

- [[AI-Foundations/05-Topics/Connectionism|Connectionism]]

新形式：

- LLM
- multimodal model
- latent representation
- reasoning model

关键理解：

- 大模型是 connectionism 的超级放大版，不是脱离历史的新范式

### 5. Statistical Learning -> eval / generalization / drift

旧问题：

- [[AI-Foundations/05-Topics/Statistical Learning|Statistical Learning]]

新形式：

- benchmark
- offline eval
- online eval
- drift
- reliability

关键理解：

- agent 和 LLM 系统再复杂，也仍然逃不开 generalization、distribution shift 和 error cost

## 这页最该怎么用

不要把它当“比喻表”。

更好的用法是：

- 遇到一个今天的系统问题，先问它对应的是哪个旧问题
- 然后回到 Foundations 看它的老版本是怎么被提出和处理的
- 最后再回现代工程页判断哪些部分变了，哪些其实没变

## 最常见的 4 个误区

### 误区 1：agent 是全新物种

不是。

它是旧问题在新算力、新接口和新模型上的重组。

### 误区 2：有了大模型就不需要结构

不对。

越进真实世界，结构、边界和治理越重要。

### 误区 3：RAG / memory 只是工程补丁

它背后其实是老的 knowledge representation 问题。

### 误区 4：eval 是新世界才有的需求

它本质上仍然是在回答 statistical learning 时代就存在的泛化和误差问题。

## 关联

- [[哪些 AI Foundations 争论今天还活着]]
- [[AI-Foundations/专题总览|AI-Foundations]]
- [[AI-Engineering/专题总览|AI-Engineering]]
