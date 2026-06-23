---
title: Direct Preference Optimization：Your Language Model is Secretly a Reward Model
type: paper
status: draft
tags:
  - ai/paper
  - ai/alignment
aliases: []
authors: []
organization: []
year: 2023
venue: arXiv
related_models:
  - "[[Claude 系列]]"
  - "[[GPT 系列]]"
  - "[[Llama 系列]]"
related_people: []
related_topics:
  - "[[Alignment]]"
  - "[[AI Safety]]"
source: https://arxiv.org/abs/2305.18290
created: 2026-04-03
updated: 2026-04-03
---

# Direct Preference Optimization：Your Language Model is Secretly a Reward Model

## 简介

`DPO` 是最近几年对齐线里最值得记住的一篇论文，因为它把很多人眼里的复杂 `RLHF pipeline` 变得更直接、更容易落地。

## 核心想法

它把偏好学习重新表述成一个更直接的优化目标，让模型可以不必完整显式地经过 reward model + RL 这整套复杂流程。

## 为什么重要

- 它影响了很多后训练与偏好优化的工程习惯
- 它让 open-weight 模型和闭源模型都更容易迭代对齐策略
- 它是理解“为什么最近几年 post-training 速度会更快”的关键节点之一

## 相关模型 / 系统

- [[Claude 系列]]
- [[GPT 系列]]
- [[Llama 系列]]

## 相关主题

- [[Alignment]]
- [[AI Safety]]

## 后续可补充

- 它和传统 RLHF 的具体差异
- 它在企业工作流、拒答行为、风格控制里的作用
- 它为什么会和 open-weight 社区快速结合

## 相关

- [[Training language models to follow instructions with human feedback]]
- [[Constitutional AI]]
- [[../../AI-Engineering/07-Topics/RLHF and Preference Optimization|RLHF and Preference Optimization]]
