---
title: LLM Inference Stack
type: stack
status: learning
tags:
  - ai/engineering
  - ai/inference-stack
created: 2026-03-13
updated: 2026-03-25
---

# LLM Inference Stack

## 简介

`LLM Inference Stack` 聚焦模型上线后的推理系统，包括模型加载、调度、缓存、服务化和可观测性。

## 为什么要单独学它

- 很多 AI 产品的真正成本和稳定性，不在训练阶段，而在推理阶段
- 模型上线之后，问题会从“怎么训出来”转成“怎么高效稳定地服务用户”
- 在今天这个阶段，inference stack 已经不是附属层，而是 AI infra 的主战场之一

## 关键层次

- 模型表示：权重、quantization、KV cache
- 推理后端：`vLLM`、`SGLang`、`TensorRT-LLM`
- 数据面：router、KV-aware scheduling、disaggregated serving、`NVIDIA Dynamo`
- 平台层：`CoreWeave Cloud`、`GroqCloud`、`Fireworks Inference Cloud`
- 服务层：API、鉴权、限流、监控
- 反馈层：日志、质量监控、成本分析

## 一条典型链路

- 请求进入服务层
- router / scheduler 决定由哪个 backend 或 deployment 处理
- runtime 完成 prefill / decode、cache 管理和 batch 调度
- 响应被流式或一次性返回给调用方
- 日志、成本和质量指标进入监控系统

## 真正的工程难点

- 不同请求长度差异大，导致 batch 很难稳定
- 上下文、KV cache 和显存是核心约束
- 峰值流量、超时与失败重试会迅速放大系统压力
- runtime、router、cloud substrate 分层之后，边界管理反而更复杂

## 学习这页时最该记住什么

- 推理栈是能力交付系统
- 运行时和调度方式，往往比模型名字更决定产品成本结构
- 现在看 inference stack，必须同时看 backend、data plane 和 platform layer

## 学习时重点看什么

- 推理系统优化的目标是吞吐、延迟和成本的平衡
- 工程重点常在 runtime 和调度，而不只是模型本身
- 平台差异越来越体现在 `data plane + serving abstraction + cloud substrate`

## 相关

- [[../07-Topics/Inference Optimization|Inference Optimization]]
- [[../07-Topics/Serving and Scaling|Serving and Scaling]]
- [[../07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]]
- [[../07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]
- [[../02-Frameworks/vLLM|vLLM]]
- [[../02-Frameworks/SGLang|SGLang]]
- [[../02-Frameworks/TensorRT-LLM|TensorRT-LLM]]
- [[../../AI-Learning/09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]]
