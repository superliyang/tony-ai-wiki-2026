---
title: Training language models to follow instructions with human feedback
type: paper
status: draft
tags:
  - ai/paper
  - ai/alignment
aliases: []
authors: []
organization:
  - OpenAI
year: 2022
venue: arXiv
related_models:
  - "[[GPT 系列]]"
related_people:
  - "[[Sam Altman]]"
related_topics:
  - "[[Alignment]]"
  - "[[AI Assistant]]"
  - "[[API Economy]]"
source: https://arxiv.org/abs/2203.02155
created: 2026-04-03
updated: 2026-04-03
---

# Training language models to follow instructions with human feedback

## 简介

这篇论文通常被直接当成 `InstructGPT` 的代表论文，也是理解“为什么语言模型会变成助手”的第一张关键卡片。

## 核心想法

它把“预测下一个 token 的通用模型”进一步推向“能听指令、按偏好回答、像助手一样工作”的后训练路线。

## 为什么重要

- 它开启了现代 `post-training` 的主叙事
- 它让 `instruction-following + human feedback` 变成了产品能力，而不只是研究技巧
- 如果没有这篇论文，后来的 [[ChatGPT]] 和很多助手型产品都很难被现在这种方式理解

## 相关模型 / 系统

- [[GPT 系列]]
- [[ChatGPT]]
- [[OpenAI API]]

## 相关主题

- [[Alignment]]
- [[AI Assistant]]
- [[API Economy]]

## 后续可补充

- RLHF pipeline 的具体拆解
- 它和 [[Direct Preference Optimization：Your Language Model is Secretly a Reward Model]] 的关系
- 它如何从研究结果变成产品体验

## 相关

- [[Language Models are Few-Shot Learners]]
- [[GPT-4 Technical Report]]
- [[Constitutional AI]]
