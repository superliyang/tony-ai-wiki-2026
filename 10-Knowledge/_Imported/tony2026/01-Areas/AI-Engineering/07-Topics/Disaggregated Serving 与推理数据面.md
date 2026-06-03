---
title: Disaggregated Serving 与推理数据面
type: topic
status: learning
tags:
  - ai/engineering
  - ai/inference
  - ai/data-plane
created: 2026-03-25
updated: 2026-03-25
---

# Disaggregated Serving 与推理数据面

## 这里说的是什么

`Disaggregated Serving` 指的是把推理链路里不同负载特征的阶段拆开，让它们在不同资源、不同节点、甚至不同 backend 上运行。

在今天最典型的语境里，这通常意味着：

- 把 `prefill` 与 `decode` 分离
- 把 `router / scheduler` 从 backend runtime 中再分出来
- 把 `KV cache`、backend selection、request routing 视为数据面问题

## 为什么它最近会成为热点

因为 reasoning model、长上下文、多租户和高峰流量，让传统“一个 runtime 一把梭”的方式越来越难同时兼顾：

- latency
- throughput
- cost
- cache locality
- 扩缩容复杂度

## 什么叫“推理数据面”

如果类比网络系统，推理系统现在也越来越像分层系统：

- `control plane`：部署、策略、资源、容量
- `routing plane`：请求路由、backend 选择、tenant 分流
- `data plane`：prefill / decode 执行、cache 生命周期、结果流式返回
- `backend runtime`：vLLM、SGLang、TensorRT-LLM 等

`NVIDIA Dynamo` 这类系统之所以值得看，就是因为它试图把这层 data plane 显式做出来。

## 为什么这件事比“换一个更快 runtime”更重要

因为成熟平台真正难的地方是：

- 怎么把不同请求分给不同 backend
- 怎么维持 cache 的命中和迁移
- 怎么控制 tail latency
- 怎么在多租户和大规模集群下保持稳定

这些问题都超过了单一 runtime 的边界。

## 这页最值得抓住的判断

### 1. serving stack 正在从“单体 runtime”走向“组合式数据面”

### 2. runtime 仍然重要，但越来越成为 backend 角色

### 3. router、cache、prefill/decode 拆分、backend orchestration 会成为新的平台差异点

## 关联

- [[Inference Optimization]]
- [[Serving and Scaling]]
- [[KV Cache、Prefill-Decode 与 Continuous Batching]]
- [[../02-Frameworks/vLLM|vLLM]]
- [[../02-Frameworks/SGLang|SGLang]]
- [[../02-Frameworks/TensorRT-LLM|TensorRT-LLM]]
- [[../../AI-Learning/09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]]

## 资料

- [NVIDIA Dynamo Architecture](https://docs.nvidia.com/dynamo/design-docs/overall-architecture)
- [SGLang Docs](https://docs.sglang.ai/)
- [vLLM Docs](https://docs.vllm.ai/en/latest/)
