---
title: 第 2 章：PyTorch MPS 与训练基础
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# 第 2 章：PyTorch MPS 与训练基础

## 本章目标

在 Mac 上真正理解训练，不只是看别人画图。

## 你要拿下的核心概念

- tensor、autograd、loss、optimizer
- batch size、gradient accumulation、sequence length
- `mps` 设备是什么，以及它和 `cuda` 的不同
- fallback 为什么存在，以及它为什么会影响实验稳定性

## 最小训练练习建议

### 练习 1：一个玩具分类任务

目的：理解训练循环本身。

### 练习 2：一个最小文本任务

目的：让你理解 tokenizer、sequence、padding、loss。

### 练习 3：比较 `cpu` 与 `mps`

记录：

- 速度差异
- 内存压力
- 哪些算子出现 fallback

## 你必须建立的直觉

- `MPS` 很适合学习训练和做小实验
- `MPS` 不等于“Mac 版 CUDA”
- 训练能不能跑，不只取决于模型，还取决于数据尺寸、op 支持和 batch 设计

## 本章输出物

- 一个最小训练脚本
- 一份 `mps` 实验记录
- 一张 `CPU vs MPS` 的观察表

## 常见误区

- 以为 `mps` 跑不快就是自己配置错了
- 没有缩小实验规模，一上来就跑太大的模型
- 不记录 fallback 情况，导致后面无法解释结果

## 继续阅读

- [[第 3 章：MLX 与 Apple Silicon 原生实验]]
- [[../../07-Topics/PyTorch MPS 实战|PyTorch MPS 实战]]
