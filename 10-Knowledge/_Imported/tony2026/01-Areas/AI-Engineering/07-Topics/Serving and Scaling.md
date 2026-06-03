---
title: Serving and Scaling
type: topic
status: learning
tags:
  - ai/engineering
created: 2026-03-13
updated: 2026-03-25
---

# Serving and Scaling

## 为什么重要

- 直接决定真实用户体验与成本曲线
- 决定推理能力能不能变成长期稳定的产品能力

## 系统视角

`serving` 关心的是“单个请求怎么跑”，`scaling` 关心的是“成千上万个请求同时来时怎么稳”。它们共同决定：

- 用户是否觉得快
- 系统是否能扛住峰值
- 单位请求成本是否可接受
- 多租户环境里是否还能维持隔离与公平

## 关键问题

- SLA 如何定义与监控
- 多租户与隔离如何实现
- 峰值、队列与超时如何处理
- runtime、router 和 data plane 的边界怎么划
- serverless、on-demand、dedicated 分别适合什么 workload

## 关键模块

- 路由与负载均衡
- batching / queueing
- cache 与状态管理
- autoscaling
- model / deployment routing
- 监控与告警

## 真实系统里还要处理什么

- 模型冷热启动
- 多模型路由和 fallback
- 租户隔离与配额
- 流式输出和超时控制
- 长上下文请求对整个集群的拖累
- 多 backend runtime 混用

## 现在最值得看懂的新变化

### 1. inference platform 正在分层

- `CoreWeave Cloud` 更像底层 AI-native cloud
- `Fireworks Inference Cloud` 更像 serving abstraction layer
- `GroqCloud` 更像 latency-oriented inference product
- `NVIDIA Dynamo` 更像 data plane / serving framework

### 2. scaling 问题越来越像系统数据面问题

随着 reasoning 和 long-context workload 变重，单纯“扩更多副本”已经不够，必须一起考虑：

- queue discipline
- prefill / decode 分离
- cache locality
- backend selection

### 3. 产品形态本身也是 serving strategy

serverless、dedicated、BYOC、managed Kubernetes，不只是售卖方式，而是完全不同的运维和成本边界。

## 常见失败模式

- 高峰期队列堆积，延迟失控
- 某个模型实例热点过高，负载不均
- 上游 prompt 或上下文长度异常，拖垮整个集群
- 线上版本切换不平滑，出现质量回退
- 多租户 noisy neighbor 导致 tail latency 爆炸

## 学习这页时最该记住什么

- 服务化不是“把模型包个 API”这么简单
- 真正难的是在成本、稳定性、隔离和体验之间找平衡
- 现在的 serving and scaling，已经越来越接近“推理数据面设计”

## 相关主题

- [[Inference Optimization]]
- [[KV Cache、Prefill-Decode 与 Continuous Batching]]
- [[Disaggregated Serving 与推理数据面]]
- [[Model Registry and Deployment]]
- [[Security and Privacy]]

## 相关实体

- [[../01-Stacks/LLM Ops Stack|LLM Ops Stack]]
- [[../01-Stacks/LLM Inference Stack|LLM Inference Stack]]
- [[../02-Frameworks/vLLM|vLLM]]
- [[../02-Frameworks/SGLang|SGLang]]
- [[../02-Frameworks/TensorRT-LLM|TensorRT-LLM]]
- [[../../AI-Learning/09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]]
- [[../../AI-Learning/09-Systems/GroqCloud|GroqCloud]]
- [[../../AI-Learning/09-Systems/Fireworks Inference Cloud|Fireworks Inference Cloud]]

## 资料

- [Groq Docs Overview](https://console.groq.com/docs/overview)
- [Fireworks AI Docs](https://docs.fireworks.ai/getting-started/introduction)
- [NVIDIA Dynamo Architecture](https://docs.nvidia.com/dynamo/design-docs/overall-architecture)
