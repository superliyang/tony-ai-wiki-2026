---
title: Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
type: paper
status: draft
tags:
  - ai/paper
  - ai/reasoning
aliases: []
authors: []
organization:
  - Google Research
year: 2022
venue: arXiv
related_models:
  - "[[GPT 系列]]"
  - "[[Claude 系列]]"
  - "[[DeepSeek-R1]]"
related_people: []
related_topics:
  - "[[Reasoning Models]]"
  - "[[提示词工程]]"
  - "[[Planning and Control]]"
source: https://arxiv.org/abs/2201.11903
created: 2026-04-03
updated: 2026-04-03
---

# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

## 简介

这篇论文是近几年 `reasoning` 讨论的起爆点之一，也是很多“让模型先想一想”工作流的源头。

## 核心想法

它说明当模型规模上去之后，显式给出中间推理轨迹 `reasoning trace`，会显著改变模型在复杂任务上的表现。

## 为什么重要

- 它把 `reasoning` 从隐含能力变成了可以工程化利用的接口
- 后来的 `ReAct`、reasoning models、许多 eval 和工作流设计都在延续这条线
- 它改变了大家看 prompt 的方式，不再只是“提问”，而是“组织思考过程”

## 相关模型 / 系统

- [[GPT 系列]]
- [[Claude 系列]]
- [[DeepSeek-R1]]

## 相关主题

- [[Reasoning Models]]
- [[提示词工程]]
- [[Planning and Control]]

## 后续可补充

- 它和 zero-shot reasoning 的关系
- 为什么它后来会演化成 prompt 技术、reasoning model 和 agent loop 三条分支
- reasoning trace 的收益和幻觉风险

## 相关

- [[ReAct：Synergizing Reasoning and Acting in Language Models]]
- [[DeepSeek-R1 Technical Report]]
- [[Training language models to follow instructions with human feedback]]
