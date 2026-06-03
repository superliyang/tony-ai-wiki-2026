---
title: FSDP
type: training
status: seed
tags:
  - ai/training
organization: PyTorch
created: 2026-03-13
updated: 2026-03-13
---

# FSDP

## 简介

FSDP 是 PyTorch 的全分片数据并行方案，用于降低显存压力并扩展大模型训练。

## 为什么它重要

- 它把分片能力带进了 PyTorch 原生生态
- 对大量已经基于 PyTorch 构建训练系统的团队来说，FSDP 是很自然的扩展路径

## 关键能力

- parameter sharding
- optimizer state sharding
- memory-efficient training

## 它主要解决什么问题

- 单机多卡训练时显存不够
- 希望尽量保持原生 PyTorch 工作流，不想过度依赖外部训练系统

## 真正要看懂的地方

- FSDP 不是简单并行，而是通过分片改变参数在设备上的驻留方式
- 它适合放在“PyTorch 原生分布式路线”里理解

## 学习这页时最该记住什么

- FSDP 代表了训练系统逐步走向原生集成化的趋势

## 适用场景

- 基于 PyTorch 的大模型训练
- 需要与原生 `torch.distributed` 紧密结合的团队

## 相关

- [[../02-Frameworks/PyTorch|PyTorch]]
- [[DeepSpeed]]
- [[../07-Topics/Distributed Training|Distributed Training]]
