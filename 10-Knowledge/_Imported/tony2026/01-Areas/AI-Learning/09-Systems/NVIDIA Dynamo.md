---
title: NVIDIA Dynamo
type: system
status: learning
tags:
  - ai/system
  - ai/inference
  - ai/infra
created: 2026-03-25
updated: 2026-03-25
---

# NVIDIA Dynamo

## 它是什么

`NVIDIA Dynamo` 是 NVIDIA 推出的 open inference framework / serving data plane，官方定位强调它适合在分布式环境里服务生成式 AI 和 reasoning 模型。

如果把 `TensorRT-LLM` 看成更靠近 backend optimization 的层，那么 `Dynamo` 更像：

- 推理数据面
- 分布式 serving 连接层
- routing / cache / backend orchestration 层

## 为什么它值得单独看

因为它代表了一个很重要的行业变化：

`inference` 不再只是“挑一个 runtime 跑起来”，而是在往 **分层数据面** 演进。

这里会开始明确区分：

- request ingress
- routing
- KV-aware scheduling
- disaggregated prefill / decode
- backend runtimes

## 它最值得抓住的 4 个点

### 1. 它强调的是 distributed inference

这意味着目标不再只是“单机跑更快”，而是把 inference 当成集群级系统来设计。

### 2. 它把 disaggregated serving 当成核心方向

随着长上下文和 reasoning model 变重，prefill / decode 的资源特征分化越来越明显，`Dynamo` 这一层就是在回应这种系统分化。

### 3. 它想做 backend-agnostic integration layer

官方架构里明确把不同 runtime 看成可接入后端，这一点很关键。它说明未来竞争可能不是单一 runtime 吃掉一切，而是：

- runtime 继续竞争
- data plane / router / orchestration 再独立成一层

### 4. 它代表 NVIDIA 正在把影响力从“硬件”延伸到“推理控制面”

这对理解 AI infra 很重要，因为它意味着 NVIDIA 正在继续向 stack 上层延伸。

## 推荐继续往下读

- [[../01-Companies/NVIDIA|NVIDIA]]
- [[../06-Topics/Inference Serving|Inference Serving]]
- [[../../AI-Engineering/07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]
- [[../../AI-Engineering/02-Frameworks/TensorRT-LLM|TensorRT-LLM]]
- [[../../AI-Engineering/08-Maps/Inference and Serving Map|Inference and Serving Map]]

## 关联

- [[CoreWeave Cloud]]
- [[GroqCloud]]
- [[Fireworks Inference Cloud]]
- [[../../AI-Engineering/07-Topics/Serving and Scaling|Serving and Scaling]]
- [[../../AI-Engineering/07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]]
- [[../../AI-Engineering/07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]

## 资料

- [NVIDIA Dynamo Architecture](https://docs.nvidia.com/dynamo/design-docs/overall-architecture)
- [NVIDIA AI](https://www.nvidia.com/en-us/ai/)
