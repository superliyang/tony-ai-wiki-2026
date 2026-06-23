---
title: KV Cache、Prefill-Decode 与 Continuous Batching
type: topic
status: learning
tags:
  - ai/engineering
  - ai/inference
created: 2026-03-25
updated: 2026-03-25
---

# KV Cache、Prefill-Decode 与 Continuous Batching

## 为什么这页是推理系统的核心

很多人理解大模型推理时，只记得“生成 token”。但真实系统最关键的效率问题，常常都集中在：

- `prefill`
- `decode`
- `KV cache`
- `batching`

这四件事上。

## 先把四个词分开

### Prefill

把整段输入上下文吃进去，生成第一批注意力状态。它通常：

- 计算密度高
- 对输入长度敏感
- 更像一次“把历史都读完”的重负载阶段

### Decode

在已有上下文状态上逐 token 生成输出。它通常：

- 迭代次数多
- 对 token 级 latency 更敏感
- 更依赖 cache 生命周期与调度

### KV Cache

是推理系统重复利用历史注意力状态的核心机制。它决定：

- 显存占用
- 长上下文成本
- 多轮对话效率
- 请求能否被继续复用

### Continuous Batching

不是等一整批请求凑齐再跑，而是在推理过程中动态把请求插进 batch。它的价值在于提高利用率，但也会引入更复杂的调度问题。

## 为什么这四者要一起看

因为真实系统里，它们互相拉扯：

- prefill 和 decode 资源特征不同
- cache 管理直接决定显存边界
- batching 影响吞吐和 tail latency
- 长上下文会把 cache 和 prefill 成本一起放大

## 现在的工程变化

### 1. KV cache 已经是一等资源

现代推理系统不是“先用满算力”，而常常是“先碰到 cache / memory / bandwidth 边界”。

### 2. prefill / decode 越来越被拆开优化

这也是为什么 `disaggregated serving` 变成热点：它承认两类阶段根本不是同一种负载。

### 3. continuous batching 是现代 serving 的基本功

没有 batching，吞吐上不去；但 batching 太激进，又会伤害交互 latency。真正难的是平衡。

## 这页和哪些系统最相关

- [[../02-Frameworks/vLLM|vLLM]]
- [[../02-Frameworks/SGLang|SGLang]]
- [[../02-Frameworks/TensorRT-LLM|TensorRT-LLM]]
- [[../../AI-Learning/09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]]

## 学习这页时最该记住什么

- 推理时代的核心资源，很多时候不是 FLOPs，而是 `memory + cache + scheduler`
- 现代 serving system 的很多创新，实际上都在围绕这四件事重写数据面

## 资料

- [vLLM Docs](https://docs.vllm.ai/en/latest/)
- [SGLang Docs](https://docs.sglang.ai/)
- [TensorRT-LLM Docs](https://nvidia.github.io/TensorRT-LLM/)
