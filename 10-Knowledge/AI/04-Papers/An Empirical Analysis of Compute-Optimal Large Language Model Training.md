---
title: An Empirical Analysis of Compute-Optimal Large Language Model Training
type: paper
status: draft
tags:
  - ai/paper
  - ai/pretraining
aliases: []
authors: []
organization:
  - Google DeepMind
year: 2022
venue: arXiv
related_models:
  - "[[Gemini 系列]]"
  - "[[Llama 系列]]"
related_people:
  - "[[Demis Hassabis]]"
related_topics:
  - "[[Pretraining]]"
  - "[[Foundation Models]]"
  - "[[Inference Efficiency]]"
source: https://arxiv.org/abs/2203.15556
created: 2026-04-03
updated: 2026-04-03
---

# An Empirical Analysis of Compute-Optimal Large Language Model Training

## 简介

这篇论文通常就是大家说的 `Chinchilla scaling`，也是最近几年最影响 frontier model 训练经济学的一篇论文之一。

## 核心想法

它最重要的结论不是“模型要更大”，而是“在固定算力预算下，模型参数和训练数据应该怎样更优地配比”。

## 为什么重要

- 它重写了很多人对 scaling 的直觉
- 它把 pretraining 从“单纯堆参数”拉回到“算力、数据和部署一起算”的问题
- 后来的 frontier model 竞争，很大程度上都绕不开它留下的训练经济学框架

## 相关模型 / 系统

- [[Gemini 系列]]
- [[Llama 系列]]
- [[../../AI-Engineering/07-Topics/Serving and Scaling|Serving and Scaling]]

## 相关主题

- [[Pretraining]]
- [[Foundation Models]]
- [[Inference Efficiency]]

## 后续可补充

- 它和旧 scaling law 的差异
- 对 closed frontier route 与 open-weight route 的不同影响
- 为什么它也会影响部署与 serving 成本

## 相关

- [[GPT-4 Technical Report]]
- [[Gemini Technical Report]]
- [[Llama 2：Open Foundation and Fine-Tuned Chat Models]]
