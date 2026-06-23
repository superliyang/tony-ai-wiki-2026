---
title: TensorRT-LLM
type: framework
status: learning
tags:
  - ai/framework
  - ai/inference
organization: NVIDIA
license: Apache-2.0
focus: LLM optimization and inference on NVIDIA GPUs
repo: https://github.com/NVIDIA/TensorRT-LLM
created: 2026-03-25
updated: 2026-03-25
---

# TensorRT-LLM

## 简介

`TensorRT-LLM` 是 NVIDIA 提供的 LLM optimization 与 serving 相关开源库，官方定位强调它适合在 NVIDIA GPU 上进行模型优化、部署和高性能推理。

## 为什么它值得单独看

- 它是 NVIDIA 把硬件优势继续向 runtime / inference software 延伸的重要抓手。
- 它帮助你理解硬件生态如何反过来塑造 serving 方案。
- 它常常不是单独存在，而是会和 `NVIDIA Dynamo`、`Triton`、企业推理平台一起出现。

## 最值得抓住的几个点

### 1. 它不是通用云平台，而是硬件贴近层的优化库

这意味着它的价值更多体现在：

- kernel / graph / quantization optimization
- NVIDIA GPU-specific performance path
- serving backend integration

### 2. 它说明 inference software stack 正在专业化

模型公司不再只关心 API，基础设施团队也不再只关心 GPU；中间这层 runtime / optimization software 已经成为独立竞争面。

### 3. 它和 open runtime 生态是互补也是竞争

和 `vLLM`、`SGLang` 相比，它更强调 NVIDIA 生态深度优化；但在真实平台里，它常常会和其他 serving layer 一起组合。

## 推荐继续往下读

- [[vLLM]]
- [[SGLang]]
- [[../07-Topics/Inference Optimization|Inference Optimization]]
- [[../07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]
- [[../../AI-Learning/09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]]

## 资料

- [TensorRT-LLM Docs](https://nvidia.github.io/TensorRT-LLM/)
- [TensorRT-LLM GitHub](https://github.com/NVIDIA/TensorRT-LLM)
