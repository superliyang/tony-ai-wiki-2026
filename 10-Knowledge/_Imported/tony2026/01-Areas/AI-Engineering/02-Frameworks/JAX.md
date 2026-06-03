---
title: JAX
type: framework
status: seed
tags:
  - ai/framework
organization: Google
license: Apache-2.0
language: Python/XLA
focus: numerical computing and compiled ML workloads
repo: https://github.com/jax-ml/jax
release_date:
related_topics:
  - "[[../07-Topics/Frameworks (PyTorch-JAX-TensorFlow)|Frameworks (PyTorch-JAX-TensorFlow)]]"
created: 2026-03-13
updated: 2026-03-13
---

# JAX

## 简介

JAX 强调函数式编程、自动微分和编译优化，常被用于高性能训练与研究实验。

## 为什么它值得学

- JAX 把“数值计算 + 程序变换 + 编译优化”结合得很紧
- 它特别适合帮助你理解模型训练背后的系统化优化思路

## 适用场景

- 需要编译优化的训练任务
- 研究与系统协同设计

## 核心模块

- `jit`
- `grad`
- `vmap` / `pmap`
- XLA compilation

## 优势与局限

- 优势是编译和变换能力强，适合系统化优化
- 局限是上手门槛比 PyTorch 更高，生态广度略弱

## 真正要看懂的地方

- JAX 的价值不只在性能，而在于它鼓励你从“程序变换”视角看训练系统
- 它更像一套思维方式：把计算图、并行和自动微分统一起来

## 学习这页时最该记住什么

- JAX 更适合作为“理解高性能训练系统”的窗口
- 它不一定最适合每个团队，但很适合理解另一种工程哲学

## 相关

- [[../07-Topics/Distributed Training|Distributed Training]]
- [[../07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]]
