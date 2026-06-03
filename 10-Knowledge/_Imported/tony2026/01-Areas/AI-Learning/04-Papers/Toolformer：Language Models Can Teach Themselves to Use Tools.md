---
title: Toolformer：Language Models Can Teach Themselves to Use Tools
type: paper
status: draft
tags:
  - ai/paper
  - ai/agent
aliases: []
authors: []
organization:
  - Meta AI
year: 2023
venue: arXiv
related_models:
  - "[[GPT 系列]]"
  - "[[Gemini 系列]]"
related_people:
  - "[[Yann LeCun]]"
related_topics:
  - "[[Tool Use]]"
  - "[[Agent]]"
  - "[[API Economy]]"
source: https://arxiv.org/abs/2302.04761
created: 2026-04-03
updated: 2026-04-03
---

# Toolformer：Language Models Can Teach Themselves to Use Tools

## 简介

`Toolformer` 是理解“为什么 tool use 会从外挂能力逐渐变成模型默认能力叙事”的关键论文。

## 核心想法

它展示了一条重要方向：模型不只可以回答问题，还可以学会在合适的位置调用外部工具来扩展能力边界。

## 为什么重要

- 它把 `tool use` 从 prompt 技巧推进到模型能力路线
- 今天很多 function calling、tool calling、agent runtime 的直觉，都能在这条线上找到来源
- 它让“模型不是孤立大脑，而是带工具的工作单元”这件事更容易被系统化表达

## 相关模型 / 系统

- [[GPT 系列]]
- [[Gemini 系列]]
- [[LangGraph]]

## 相关主题

- [[Tool Use]]
- [[Agent]]
- [[API Economy]]

## 后续可补充

- 它和 function calling 的关系
- 它和 [[ReAct：Synergizing Reasoning and Acting in Language Models]] 的差异
- 为什么产品里还要额外设计 tool gateway 和 policy layer

## 相关

- [[ReAct：Synergizing Reasoning and Acting in Language Models]]
- [[../../AI-Engineering/07-Topics/Tool Gateway、MCP Servers 与 SDK Tools|Tool Gateway、MCP Servers 与 SDK Tools]]
- [[../../AI-Engineering/07-Topics/Tool Calling and Action Execution|Tool Calling and Action Execution]]
