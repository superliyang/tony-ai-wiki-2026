---
title: AI 基础设施与 GPU Cloud
type: topic
status: learning
tags:
  - ai/topic
  - ai/infra
  - ai/gpu-cloud
created: 2026-03-25
updated: 2026-03-25
---

# AI 基础设施与 GPU Cloud

## 这里说的是什么

这条线讨论的不是“哪家模型更强”，而是 **这些模型靠什么样的算力、网络、存储、集群编排和云平台被训练、部署和服务出来**。

在 `foundation model` 和 `agent` 之后，AI 竞争越来越明显地进入了另一层：

- 谁能更快拿到和调度 GPU
- 谁能把 GPU 集群做成稳定平台
- 谁能把训练、推理、存储、网络和 Kubernetes 组合成真正可交付的 AI cloud

## 为什么它在 2026 年尤其重要

因为 frontier AI 的竞争已经不只是模型路线竞争，而是：

- `model quality`
- `training throughput`
- `inference economics`
- `deployment sovereignty`
- `developer access speed`

这些变量一起竞争。

换句话说，很多团队今天感受到的 AI 差距，已经不是“模型参数差多少”，而是“基础设施与服务化能力差多少”。

## 这一层可以分成哪三块

### 1. GPU cloud

这一层更像 AI 时代的底座：

- GPU / accelerator 供给
- 集群拓扑
- 高速网络
- 对象存储 / checkpoint / 数据面
- managed Kubernetes / bare metal / capacity control

代表玩家会更像 `NVIDIA`、`CoreWeave` 这样的基础设施路线。

### 2. inference platform

这一层解决的是“模型怎么以 API 或服务形态稳定交付”：

- serverless / dedicated deployments
- autoscaling
- routing
- tenant isolation
- latency / throughput / cost balancing

代表路线更像 `GroqCloud`、`Fireworks Inference Cloud`、`CoreWeave Cloud`。

### 3. serving runtime / data plane

这一层解决的是最底层的推理执行问题：

- prefill / decode
- KV cache
- continuous batching
- disaggregated serving
- backend integration

代表系统更像 `vLLM`、`SGLang`、`TensorRT-LLM`、`NVIDIA Dynamo`。

## 你真正要学懂的判断

### 不是所有 AI infra 公司都在同一层竞争

- `NVIDIA` 更像 stack setter：从 GPU 到 runtime 都在影响行业默认值
- `CoreWeave` 更像 AI-native cloud：强调集群、网络、Kubernetes、训练与推理承载
- `Groq` 更像 special-purpose inference company：强调低时延和推理体验
- `Fireworks AI` 更像 inference platform：强调模型托管、serverless / dedicated serving 和开发者接入

### “AI cloud” 不等于“普通云上多挂几张 GPU”

真正的 AI cloud 会把这些做成系统：

- 容量与配额
- 高速互联
- 存储吞吐
- 调度与恢复
- 训练/推理双栈
- 平台控制面

### inference economics 已经变成平台级竞争点

今天很多产品能不能成立，不取决于“能不能调一个模型”，而取决于：

- 单位 token 成本
- latency 稳定性
- 并发峰值处理
- 长上下文和 KV cache 开销
- 多租户隔离

## 推荐学习顺序

1. [[Inference Serving]]
2. [[../01-Companies/NVIDIA|NVIDIA]]
3. [[../01-Companies/CoreWeave|CoreWeave]]
4. [[../01-Companies/Groq|Groq]]
5. [[../01-Companies/Fireworks AI|Fireworks AI]]
6. [[../09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]]
7. [[../09-Systems/CoreWeave Cloud|CoreWeave Cloud]]
8. [[../09-Systems/GroqCloud|GroqCloud]]
9. [[../09-Systems/Fireworks Inference Cloud|Fireworks Inference Cloud]]
10. [[../../AI-Engineering/07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]]
11. [[../../AI-Engineering/07-Topics/Inference Optimization|Inference Optimization]]
12. [[../../AI-Engineering/07-Topics/Serving and Scaling|Serving and Scaling]]
13. [[../../AI-Engineering/07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]]
14. [[../../AI-Engineering/07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]
15. [[../../AI-Engineering/02-Frameworks/vLLM|vLLM]]
16. [[../../AI-Engineering/02-Frameworks/SGLang|SGLang]]
17. [[../../AI-Engineering/02-Frameworks/TensorRT-LLM|TensorRT-LLM]]

## 和其他主题的关系

- 它和 [[API Economy]] 相连：因为推理平台最终会长成 API 产品
- 它和 [[AI Coding Workbench]] 相连：因为 coding/product agent 的体验，最后也会被 inference stack 反向约束
- 它和 [[Sovereign AI]] 相连：因为主权化部署往往首先是 infra 与 deployment boundary 问题
- 它和 [[../../AI-Engineering/07-Topics/Agent 平台架构（LangGraph、Langfuse、ADK）|Agent 平台架构（LangGraph、Langfuse、ADK）]] 相连：agent platform 最后也要依赖 inference platform

## 相关地图

- [[../07-Maps/AI Infra 与推理服务生态图|AI Infra 与推理服务生态图]]
- [[../../AI-Engineering/08-Maps/Inference and Serving Map|Inference and Serving Map]]

## 资料

- [CoreWeave Platform](https://www.coreweave.com/platform)
- [NVIDIA AI](https://www.nvidia.com/en-us/ai/)
- [Groq](https://groq.com/)
- [Groq Docs Overview](https://console.groq.com/docs/overview)
- [Fireworks AI Docs](https://docs.fireworks.ai/getting-started/introduction)
- [NVIDIA Dynamo Architecture](https://docs.nvidia.com/dynamo/design-docs/overall-architecture)
