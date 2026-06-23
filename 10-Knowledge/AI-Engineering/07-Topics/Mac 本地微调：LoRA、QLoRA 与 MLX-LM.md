---
title: Mac 本地微调：LoRA、QLoRA 与 MLX-LM
type: topic
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# Mac 本地微调：LoRA、QLoRA 与 MLX-LM

## 先说现实判断

在 `Mac M4 Max` 上，本地微调是可以学、也值得学的。

但学习重点应该是：

- 微调方法
- 数据组织
- 评测方式
- 训练稳定性

而不是追求“在本地训出最强模型”。

## 最推荐的路线

### 1. 先学 LoRA

- adapter 是什么
- 为什么它比 full fine-tuning 更现实
- 怎么看 loss、过拟合、数据质量

### 2. 再理解 QLoRA 的思想

- 它解决什么问题
- 为什么量化和可训练 adapter 要配合
- 哪些路径在 Mac 上不如 CUDA 生态成熟

### 3. 在 Apple silicon 上优先看 `MLX-LM`

因为它更贴近本机环境，也更适合本地实验。

## 最适合的练习

- 做小数据集 instruction tuning
- 做 domain adaptation
- 做评测前后对比

## 关联

- [[LoRA and PEFT]]
- [[Evaluation and Benchmarks]]
- [[Prompt Registry、Datasets 与 Evals]]
- [[MLX 与 Apple Silicon 原生大模型实践]]
