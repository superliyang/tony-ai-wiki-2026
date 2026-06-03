---
title: Gemini 1.5：Unlocking multimodal understanding across millions of tokens of context
type: paper
status: draft
tags:
  - ai/paper
  - ai/long-context
  - ai/multimodal
aliases: []
authors: []
organization:
  - Google DeepMind
year: 2024
venue: arXiv
related_models:
  - "[[Gemini 系列]]"
related_people:
  - "[[Demis Hassabis]]"
related_topics:
  - "[[Long Context]]"
  - "[[Multimodal Models]]"
  - "[[Foundation Models]]"
source: https://arxiv.org/abs/2403.05530
created: 2026-04-03
updated: 2026-04-03
---

# Gemini 1.5：Unlocking multimodal understanding across millions of tokens of context

## 简介

这篇论文是最近两年 `long context` 最值得反复看的锚点之一，因为它把 `million-token context` 从参数表里的数字，推进成了真正影响系统设计的主能力。

## 核心想法

它最重要的地方，不只是上下文更长，而是把 `long context + multimodal understanding` 一起拉到了同一条模型路线里。

## 为什么重要

- 它让大家重新思考：什么时候应该靠超长上下文，什么时候仍然应该靠检索、记忆和工具层
- 它解释了为什么后来的 coding assistant、document assistant 和 agent workbench 会越来越重视“工作集规模”
- 它把 Gemini 路线和 `long context` 深度绑定了起来

## 相关模型 / 系统

- [[Gemini 系列]]
- [[Gemini CLI]]
- [[Google Agent Development Kit（ADK）]]

## 相关主题

- [[Long Context]]
- [[Multimodal Models]]
- [[Foundation Models]]

## 后续可补充

- 它和 Kimi、Claude 长上下文产品路线的关系
- 超长上下文与 RAG / memory 的边界
- 为什么 long context 也会直接影响 agent runtime 设计

## 相关

- [[Gemini Technical Report]]
- [[GPT-4o System Card]]
- [[Long Context]]
