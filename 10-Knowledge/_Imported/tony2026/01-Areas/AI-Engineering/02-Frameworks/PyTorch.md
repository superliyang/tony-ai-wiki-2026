---
title: PyTorch
type: framework
status: seed
tags:
  - ai/framework
organization: Meta
license: BSD-style
language: Python/C++
focus: deep learning research and production training
repo: https://github.com/pytorch/pytorch
release_date:
related_topics:
  - "[[../07-Topics/Frameworks (PyTorch-JAX-TensorFlow)|Frameworks (PyTorch-JAX-TensorFlow)]]"
  - "[[../07-Topics/Distributed Training|Distributed Training]]"
created: 2026-03-13
updated: 2026-03-13
---

# PyTorch

## 简介

PyTorch 是当前最重要的深度学习框架之一，也是大模型训练生态里最常见的基础层。

## 为什么它是事实标准之一

- 大量前沿模型训练代码首先在 PyTorch 生态里出现
- 它在研究灵活性和工程可扩展性之间取得了比较好的平衡
- `torch.distributed`、FSDP、生态库和社区经验让它适合快速迭代

## 适用场景

- 研究原型开发
- 大模型训练
- 与分布式训练库协同

## 核心模块

- tensor 与 autograd
- `torch.distributed`
- FSDP
- ecosystem libraries

## 优势与局限

- 优势是生态广、调试友好、社区成熟
- 局限是部分极致优化需要额外依赖编译与运行时工具

## 真正要看懂的地方

- PyTorch 本身不是“大模型训练方案”的全部，而是承载大量训练方案的基础平台
- 它的优势不只是 API，而是围绕它形成的训练、微调、分布式和部署生态

## 学习这页时最该记住什么

- 如果你只学一个训练框架，PyTorch 往往是最合适的起点
- 学 PyTorch 时要连同 `distributed`、生态库和训练工具一起学

## 相关

- [[../03-Training/FSDP|FSDP]]
- [[../03-Training/DeepSpeed|DeepSpeed]]
- [[../03-Training/Megatron-LM|Megatron-LM]]
