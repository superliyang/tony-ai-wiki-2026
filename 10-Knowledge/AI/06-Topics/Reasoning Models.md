---
title: Reasoning Models
type: topic
status: active
tags:
  - ai/topic
  - ai/reasoning
created: 2026-03-01
updated: 2026-04-07
---

# Reasoning Models

## 这个主题是什么

`Reasoning Models` 关注的不是普通对话能力，而是模型在复杂任务中进行分步推理、问题求解、规划、验证和修正的能力。

## 为什么重要

- 它决定模型能否处理更复杂的知识工作
- 它和 agent、tool use、coding、数学推导等场景高度相关
- 它已经成为各家 frontier-model 公司竞争的关键方向

## 过去半年这条线为什么更关键了

在 `2025-09-25` 到 `2026-03-25` 之间，reasoning 已经从“模型能力的一项指标”变成“平台与产品的核心卖点”：

- [[OpenAI]] 用 `GPT-5.2-Codex`、`GPT-5.3-Codex`、`GPT-5.4` 把 reasoning 直接接到 coding 和 professional agent 任务上
- [[Anthropic]] 用 `Claude Sonnet 4.5`、`4.6` 和 [[../03-Models/Claude Opus 4-6|Claude Opus 4.6]] 把 reasoning、computer use、memory 和 tool use 拉到一个更统一的系统里
- [[Google DeepMind]] 用 [[../03-Models/Gemini 3 Deep Think|Gemini 3 Deep Think]] 把 specialized reasoning mode 明确做成独立路线
- [[DeepSeek]] 在 `V3.2` 官方叙事里直接强调 `reasoning-first models built for agents`
- [[Zhipu AI]]、[[MiniMax]]、[[Moonshot AI]] 也都把 reasoning 明确接到了长程 agent、coding、tool use 和工作流场景里

## 你先要抓住什么

- reasoning 不只是“回答得像在推理”，而是模型在复杂任务中能否进行分解、计划、验证和修正
- 它通常会带来更高成本、更高延迟，但也可能带来更高任务完成率
- reasoning 常和 tool use、代码执行、检索增强一起出现
- 最近半年一个明显趋势是：reasoning 不再单独存在，而是被嵌进 coding workbench、agent runtime 和多模态系统里

## 关键问题

- 什么才算真正的推理能力，而不只是 fluent output
- reasoning 能力来自模型规模、训练方法，还是推理时策略
- 为什么 reasoning 会显著影响 coding、agent 和 research assistant 场景
- reasoning 和 tool use、memory、approval、latency 之间如何平衡

## 典型观察点

- 多步问题拆解
- 自我检查与修正
- 数学、代码、规划任务表现
- 成本与延迟变化
- 与 tool use / computer use 的结合程度

## 当前值得重点观察的公司

- [[OpenAI]]
- [[Anthropic]]
- [[DeepSeek]]
- [[Google DeepMind]]
- [[Zhipu AI]]
- [[MiniMax]]

## 当前值得重点观察的模型

- [[GPT 系列]]
- [[../03-Models/GPT-5-4|GPT-5.4]]
- [[Claude 系列]]
- [[../03-Models/Claude Opus 4-6|Claude Opus 4.6]]
- [[../03-Models/Claude Sonnet 4-6|Claude Sonnet 4.6]]
- [[DeepSeek-R1]]
- [[DeepSeek-V3]]
- [[Gemini 系列]]
- [[../03-Models/Gemini 3 Deep Think|Gemini 3 Deep Think]]
- [[Grok]]

## 当前值得问的问题

- 什么样的能力才算 reasoning，而不只是 fluent output
- reasoning 能力如何改变产品和工作流设计
- reasoning 与 cost、latency、tool use 之间是什么关系
- frontier 公司为什么都在把 reasoning 嵌入 coding / agent / multimodal 的产品层

## 相关

- [[Foundation Models]]
- [[Agent]]
- [[Coding Agents]]
- [[AI Coding Workbench]]
- [[AI Safety]]
- [[Open-Weight Models]]
- [[China AI Ecosystem]]
- [[过去半年全球 AI 前沿动态（2025-09-25 至 2026-03-25）]]
- [[../07-Maps/AI 前沿主题演化图|AI 前沿主题演化图]]
