---
title: QLoRA：Efficient Finetuning of Quantized LLMs
type: paper
status: draft
tags:
  - ai/paper
  - ai/open-weight
aliases: []
authors: []
organization: []
year: 2023
venue: arXiv
related_models:
  - "[[Llama 系列]]"
  - "[[Qwen 系列]]"
related_people: []
related_topics:
  - "[[Open-Weight Models]]"
  - "[[Inference Efficiency]]"
  - "[[AI Industry]]"
source: https://arxiv.org/abs/2305.14314
created: 2026-04-03
updated: 2026-04-03
---

# QLoRA：Efficient Finetuning of Quantized LLMs

## 简介

`QLoRA` 是 open-weight 生态里一张特别关键的卡，因为它直接改变了“谁有资格做高质量微调”这件事。

## 核心想法

它把量化和参数高效微调结合起来，让更少的硬件预算也能做出相当有用的模型定制。

## 为什么重要

- 它显著降低了 open-weight 模型微调门槛
- 它让很多团队不必先拥有 frontier 训练能力，也能参与模型定制
- 它直接推动了本地 AI、私有部署和行业模型定制的扩散

## 相关模型 / 系统

- [[Llama 系列]]
- [[Qwen 系列]]
- [[Ollama]]
- [[llama-cpp]]

## 相关主题

- [[Open-Weight Models]]
- [[Inference Efficiency]]
- [[AI Industry]]

## 后续可补充

- QLoRA 与 LoRA、full finetuning 的成本差异
- 它如何影响本地部署与私有模型路线
- 为什么它会和 [[Llama 2：Open Foundation and Fine-Tuned Chat Models]] 形成组合拳

## 相关

- [[Llama 2：Open Foundation and Fine-Tuned Chat Models]]
- [[Llama 3 Herd of Models]]
- [[Open-Weight Models]]
