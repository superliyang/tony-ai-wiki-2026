---
title: GPT 系列
type: model
status: draft
tags:
  - ai/model
  - organization/openai
aliases: []
organization: "[[OpenAI]]"
modality:
  - text
  - multimodal
family: GPT
related_papers:
  - "[[Language Models are Few-Shot Learners]]"
  - "[[Training language models to follow instructions with human feedback]]"
  - "[[GPT-4 Technical Report]]"
related_people:
  - "[[Sam Altman]]"
created: 2026-03-01
updated: 2026-04-29
---

# GPT 系列

## 简介

`GPT` 是 OpenAI 最核心的模型家族之一，也是理解现代大语言模型产品化路径的重要入口。

## 你可以把这个模型家族当成什么来理解

可以把 `GPT 系列` 当成 OpenAI 在通用模型能力上的主线演进：

- 一端连接研究能力
- 一端连接 API 和产品
- 一端连接行业对“通用模型”能力边界的想象

## 为什么重要

- 是商业化 LLM 讨论中的核心参照系
- 模型代际演进会直接影响开发者生态和产品设计
- 经常作为其他公司对标的能力基线

## 这条路线代表什么

- 它代表了通用大模型从研究样品走向大众产品和开发平台的过程
- GPT 的影响不只在模型能力本身，也在于它把“模型即平台”这件事做成了现实

## 你学习这个模型家族时，最该看什么

- GPT 从早期文本生成走向通用助手的演进
- 预训练能力、后训练能力和产品体验分别扮演什么角色
- 为什么同一条模型路线可以同时支撑 `ChatGPT` 和 `OpenAI API`

## 学习时重点看什么

- 不同代际之间的能力变化
- 从 text-only 到 multimodal 的扩展
- 与 [[ChatGPT]] 和 [[OpenAI API]] 的关系

## 截至 2026-04-07 最值得记住的 2026 节点

- [[GPT-5-3-Codex|GPT-5.3-Codex]]：把 frontier coding、computer use 和 professional work 收成单独模型 lane
- `GPT-5.3-Codex-Spark`：把 low-latency coding 单独做成一个 tier
- `GPT-5.3 Instant`：把 everyday chat 和高频工具工作流继续往高性价比层推进
- [[GPT-5-4|GPT-5.4]]：把 `1M context + tool search + native computer use` 收成通用旗舰

这意味着 `GPT 系列` 到了 `2026` 更像一个完整分层：

- default chat tier
- coding flagship
- ultra-low-latency coding tier
- long-horizon general flagship

## 2026-04-07 之后的新节点

- [[GPT-5-5|GPT-5.5]]：更明确地进入 `frontier work model` 路线，重点看 coding、computer use、knowledge work、science 和 long-horizon tasks
- [[../09-Systems/OpenAI Sandbox Agents|OpenAI Sandbox Agents]]：把 GPT 能力接到 sandbox / shell / filesystem / approval 这类真实执行边界

这说明 GPT 路线的下一步不只是模型能力，而是 `model + runtime + eval + governance` 的组合能力。

## 关键理解框架

- 先把 GPT 看成 foundation model 的代表
- 再把 ChatGPT 看成 GPT 的产品封装
- 再把 OpenAI API 看成 GPT 的平台化分发方式

## 所属组织

- [[OpenAI]]

## 相关产品

- [[ChatGPT]]
- [[OpenAI API]]
- [[GPT-5-5|GPT-5.5]]
- [[GPT-5-4|GPT-5.4]]
- [[GPT-5-3-Codex|GPT-5.3-Codex]]

## 相关主题

- [[Foundation Models]]
- [[Reasoning Models]]
- [[Multimodal Models]]
- [[AI Safety]]

## 相关论文

- [[Language Models are Few-Shot Learners]]
- [[Training language models to follow instructions with human feedback]]
- [[GPT-4 Technical Report]]

## 相关

- [[Claude 系列]]
- [[Gemini 系列]]
- [[DeepSeek-V3]]
- [[DeepSeek-R1]]
- [[../11-Recent-Supplements/截至 2026-04-07 的 2026 新模型刷新|截至 2026-04-07 的 2026 新模型刷新]]
- [[../11-Recent-Supplements/2026-04-07 至 2026-04-29 AI 拓扑补线：Frontier Work Models、Sandbox Agents 与 Enterprise Model Lifecycle|2026-04-07 至 2026-04-29 AI 拓扑补线]]
