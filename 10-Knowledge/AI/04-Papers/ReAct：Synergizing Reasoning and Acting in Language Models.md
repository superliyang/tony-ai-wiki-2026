---
title: ReAct：Synergizing Reasoning and Acting in Language Models
type: paper
status: draft
tags:
  - ai/paper
  - ai/agent
aliases: []
authors: []
organization:
  - Google Research
year: 2023
venue: ICLR / arXiv
related_models:
  - "[[GPT 系列]]"
  - "[[Claude 系列]]"
related_people: []
related_topics:
  - "[[Agent]]"
  - "[[Tool Use]]"
  - "[[Planning and Control]]"
source: https://arxiv.org/abs/2210.03629
created: 2026-04-03
updated: 2026-04-03
---

# ReAct：Synergizing Reasoning and Acting in Language Models

## 简介

`ReAct` 是最近几年最值得反复读的 agent 论文之一，因为它把 `reasoning` 和 `acting` 合成了一个更像真实工作流的循环。

## 核心想法

与其只让模型思考，或者只让模型调用动作，不如让模型在同一条轨迹里交替地产生推理和行动。

## 为什么重要

- 它是今天很多 `tool-using agent loop` 的论文祖先之一
- 它把 reasoning 从“更会答题”推进到“更会完成任务”
- 它也让 agent 轨迹更可解释、更容易被人审查和纠偏

## 相关模型 / 系统

- [[LangGraph]]
- [[ChatGPT Agent]]
- [[Claude Code]]

## 相关主题

- [[Agent]]
- [[Tool Use]]
- [[Planning and Control]]

## 后续可补充

- 它和 [[Chain-of-Thought Prompting Elicits Reasoning in Large Language Models]] 的关系
- 它为什么会进入 browser agent、computer use 和 workflow agent 设计
- 它的 failure mode 和轨迹可解释性

## 相关

- [[Toolformer：Language Models Can Teach Themselves to Use Tools]]
- [[Chain-of-Thought Prompting Elicits Reasoning in Large Language Models]]
- [[../../AI-Engineering/07-Topics/Agent、Workflow、Runtime 与 Harness：边界与组合关系|Agent、Workflow、Runtime 与 Harness：边界与组合关系]]
