---
title: MLX 与 Apple Silicon 原生大模型实践
type: topic
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# MLX 与 Apple Silicon 原生大模型实践

## 为什么它是这条路径的核心

因为 `MLX` 代表的不是“再学一个框架”，而是：

- 站在 Apple silicon 原生视角理解本地 AI

## 最值得做的 3 类实验

### 1. 本地推理

- 跑 instruction model
- 比较不同模型尺寸
- 比较不同 context length 与响应速度

### 2. LoRA / fine-tuning

- 在小数据集上做 LoRA
- 理解 adapter-based tuning
- 比较本地训练成本和收益

### 3. 本地 app / pipeline

- 用 `MLX-LM` 跑本地模型
- 接一个简单 RAG
- 接一个简单 agent

## 为什么这条线特别适合 Mac 用户

因为它让你：

- 更快碰到真实模型实验
- 更少被 CUDA 特有问题绊住
- 更容易形成“本地 AI lab”感觉

## 资料

- [MLX Docs](https://ml-explore.github.io/mlx/build/html/index.html)
- [MLX-LM](https://github.com/ml-explore/mlx-lm)
