---
title: DeepSpeed
type: training
status: seed
tags:
  - ai/training
organization: Microsoft
created: 2026-03-13
updated: 2026-03-13
---

# DeepSpeed

## 简介

DeepSpeed 是面向大规模训练和推理优化的系统库，常用于降低显存占用并提升训练效率。

## 为什么它重要

- 它是大模型训练从“勉强能跑”走向“可扩展训练”的代表工具之一
- 很多团队第一次训练更大模型，靠的不是改模型结构，而是引入 DeepSpeed 这类系统工具

## 关键能力

- ZeRO
- distributed training optimization
- memory efficiency

## 它主要解决什么问题

- 参数、梯度和优化器状态太大，单卡显存扛不住
- 扩卡之后通信与显存压力迅速上升
- 大模型训练需要更精细的显存和吞吐管理

## 真正要看懂的地方

- DeepSpeed 本质上是在做“资源分片和执行优化”
- 它不是替代框架，而是贴在框架之上的训练系统层

## 学习这页时最该记住什么

- DeepSpeed 的代表意义在于把训练可行性往更大规模推进了一步

## 适用场景

- 超大模型训练
- 资源受限下的扩展训练

## 相关

- [[FSDP]]
- [[Megatron-LM]]
- [[../07-Topics/Distributed Training|Distributed Training]]
