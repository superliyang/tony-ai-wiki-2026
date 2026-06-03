---
title: Megatron-LM
type: training
status: seed
tags:
  - ai/training
organization: NVIDIA
created: 2026-03-13
updated: 2026-03-13
---

# Megatron-LM

## 简介

Megatron-LM 是面向超大规模 Transformer 训练的核心系统之一，强调张量并行和流水并行。

## 为什么它重要

- 它帮助很多团队把超大规模 Transformer 训练真正推到多机多卡层面
- 在理解张量并行、流水并行这些概念时，它是非常典型的工程样本

## 关键能力

- tensor parallelism
- pipeline parallelism
- large-scale transformer training

## 它主要解决什么问题

- 模型参数规模已经大到数据并行不够用
- 需要把模型内部计算拆散到更多设备上

## 真正要看懂的地方

- Megatron-LM 更偏“模型并行系统”
- 它和 DeepSpeed 常被放在一起讨论，但侧重点并不相同

## 学习这页时最该记住什么

- Megatron-LM 代表了超大模型训练里“模型内部切分”的思路

## 适用场景

- 多机多卡大模型训练
- 与 NVIDIA 生态深度配合的训练场景

## 相关

- [[DeepSpeed]]
- [[FSDP]]
- [[../07-Topics/Distributed Training|Distributed Training]]
