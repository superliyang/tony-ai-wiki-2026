---
title: SGLang
type: framework
status: learning
tags:
  - ai/framework
  - ai/inference
organization: open source
license: Apache-2.0
focus: LLM serving and runtime optimization
repo: https://github.com/sgl-project/sglang
created: 2026-03-25
updated: 2026-03-25
---

# SGLang

## 简介

`SGLang` 是当前大模型推理与服务化里非常重要的开源 runtime / serving framework。官方文档把重点放在：

- 高性能 serving
- structured generation
- router / disaggregation
- 与现代 LLM workload 更贴近的系统优化

## 为什么它值得单独看

- 它是 `vLLM` 之外最值得持续跟踪的 open runtime 之一。
- 它让我们看到推理 runtime 的竞争已经从“能不能跑”进入“在什么 workload 上更优”的阶段。
- 它和 `NVIDIA Dynamo`、`vLLM`、`TensorRT-LLM` 一起，构成了今天 inference data plane 的关键后端生态。

## 最值得抓住的几个点

### 1. runtime 竞争已经进入 workload-specific 优化

SGLang 的价值不只在某一个 feature，而在于它把 runtime 做成了更贴近实际 serving workload 的系统。

### 2. 它持续强调 prefill / decode、router 和 disaggregation 这类系统问题

这说明行业焦点已经从单机 kernel 优化，推进到更完整的数据面问题。

### 3. 它帮助你理解“开放 runtime 生态为什么不会只剩一个赢家”

不同团队、不同 GPU、不同模型和不同服务形态，会让 runtime 生态长期保持多样化。

## 推荐继续往下读

- [[vLLM]]
- [[TensorRT-LLM]]
- [[../07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]]
- [[../07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]
- [[../08-Maps/Inference and Serving Map|Inference and Serving Map]]

## 资料

- [SGLang Docs](https://docs.sglang.ai/)
- [SGLang GitHub](https://github.com/sgl-project/sglang)
