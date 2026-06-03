---
title: Inference Serving
type: topic
status: learning
tags:
  - ai/topic
  - ai/inference
  - ai/serving
created: 2026-03-25
updated: 2026-03-25
---

# Inference Serving

## 这里说的不是“模型上线”四个字

`Inference Serving` 指的是：模型如何被加载、调度、缓存、路由、观测、扩缩容，并以稳定 API 或工作流能力的方式交付出去。

在大模型时代，很多产品真正的竞争点已经从“谁有模型”变成了：

- 谁能更稳地提供响应
- 谁能更低成本地提供响应
- 谁能在长上下文、多租户、流式输出和高峰并发下继续提供响应

## 为什么这一层越来越像独立系统

因为一个真实的推理系统通常至少包含：

- API gateway
- request router
- scheduler
- runtime
- KV cache / state management
- autoscaling / admission control
- observability / cost telemetry

所以 serving 已经不再只是“包装个 API”，而是一个完整的数据面与控制面问题。

## 三个最关键的技术支点

### 1. prefill / decode 被拆开看

长输入和逐 token 生成的资源特征完全不同，所以很多系统开始把：

- prefill
- decode
- queueing
- batch scheduling

当成单独优化对象。

### 2. KV cache 变成一等公民

很多线上系统的瓶颈不是裸算力，而是：

- 显存
- cache 生命周期
- cache 复用
- cache 迁移
- 长上下文的 cache 占用

### 3. router 与 runtime 的边界越来越重要

成熟系统会开始区分：

- control plane
- routing plane
- serving data plane
- backend runtime

这也是为什么 `NVIDIA Dynamo`、`vLLM`、`SGLang` 这些名字会开始一起出现。

## 你应该怎么理解主要玩家

- `CoreWeave Cloud`：更偏 AI-native cloud + cluster substrate
- `GroqCloud`：更偏低时延推理平台
- `Fireworks Inference Cloud`：更偏模型托管和部署抽象层
- `NVIDIA Dynamo`：更偏 inference data plane / distributed serving framework
- `vLLM` / `SGLang` / `TensorRT-LLM`：更偏 runtime / backend / optimization engine

## 推荐继续往下读

1. [[AI 基础设施与 GPU Cloud]]
2. [[../09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]]
3. [[../09-Systems/CoreWeave Cloud|CoreWeave Cloud]]
4. [[../09-Systems/GroqCloud|GroqCloud]]
5. [[../09-Systems/Fireworks Inference Cloud|Fireworks Inference Cloud]]
6. [[../../AI-Engineering/07-Topics/Inference Optimization|Inference Optimization]]
7. [[../../AI-Engineering/07-Topics/Serving and Scaling|Serving and Scaling]]
8. [[../../AI-Engineering/07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]]
9. [[../../AI-Engineering/07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]

## 一个先给出的判断

在 2026 年这个时间点，`inference serving` 正在变成和模型本身同等重要的竞争层。很多公司真正的分化点，已经不是参数量，而是：

- 运行时效率
- 调度与路由
- 云平台承载
- API / deployment 体验
- 成本曲线

## 相关地图

- [[../07-Maps/AI Infra 与推理服务生态图|AI Infra 与推理服务生态图]]
- [[../../AI-Engineering/08-Maps/Inference and Serving Map|Inference and Serving Map]]

## 资料

- [Groq Docs Overview](https://console.groq.com/docs/overview)
- [Fireworks AI Docs](https://docs.fireworks.ai/getting-started/introduction)
- [NVIDIA Dynamo Architecture](https://docs.nvidia.com/dynamo/design-docs/overall-architecture)
- [vLLM Docs](https://docs.vllm.ai/en/latest/)
- [SGLang Docs](https://docs.sglang.ai/)
- [TensorRT-LLM Docs](https://nvidia.github.io/TensorRT-LLM/)
