---
title: Inference Optimization
type: topic
status: learning
tags:
  - ai/engineering
created: 2026-03-13
updated: 2026-03-25
---

# Inference Optimization

## 为什么重要

- 推理成本决定规模化部署能力
- 模型能不能广泛可用，很多时候不是 benchmark 决定的，而是推理经济性决定的

## 系统视角

训练决定模型能做什么，推理优化决定这些能力能不能被广泛、稳定、低成本地用起来。推理优化关心的是：

- 每次请求要花多少算力和显存
- 延迟能不能满足交互体验
- 吞吐能不能支撑并发业务
- 不同上下文长度、不同输出长度下系统是否还能保持可预测

## 关键问题

- 延迟与吞吐如何权衡
- 量化与蒸馏的边界在哪
- 推理栈的瓶颈来自模型还是系统
- 为什么 prefill / decode 经常要分开看
- 为什么 KV cache 管理会成为主瓶颈之一

## 关键手段

- 量化、蒸馏、裁剪
- KV cache 优化
- continuous batching
- prefill / decode 分离
- kernel / backend 优化
- 路由与请求整形

## 优化通常发生在哪几层

- 模型层：量化、蒸馏、结构裁剪
- runtime 层：kernel 优化、图编译、cache 管理
- 调度层：batching、prefill/decode 调度、资源分配
- 产品层：请求合并、上下文截断、缓存命中、API 形态设计

## 现在最值得看懂的新变化

### 1. runtime 已经成为独立竞争层

`vLLM`、`SGLang`、`TensorRT-LLM` 说明推理优化很多时候发生在 runtime，而不是模型结构本身。

### 2. 推理数据面正在独立出来

`NVIDIA Dynamo` 这类系统说明未来很多优化，不只在单个 backend，而会发生在 router / data plane / disaggregated serving 这一层。

### 3. 优化目标不再只是“跑更快”

真正的目标是：

- 更低成本
- 更稳 latency
- 更高利用率
- 更少 tail latency 爆炸
- 更好的多租户承载

## 常见工程权衡

- 更低延迟 vs 更高吞吐
- 更高模型质量 vs 更低显存占用
- 更长上下文 vs 更高单次成本
- 更强兼容性 vs 更激进的硬件专用优化

## 学习这页时最该记住什么

- 推理优化不是“压榨模型”，而是“让能力可交付”
- 很多模型路线最终能否胜出，取决于它的推理经济性
- AI infra 的竞争，本质上会不断回到 inference optimization

## 相关主题

- [[Serving and Scaling]]
- [[Infrastructure (GPU-TPU)]]
- [[KV Cache、Prefill-Decode 与 Continuous Batching]]
- [[Disaggregated Serving 与推理数据面]]
- [[Model Registry and Deployment]]

## 相关实体

- [[../01-Stacks/LLM Inference Stack|LLM Inference Stack]]
- [[../02-Frameworks/vLLM|vLLM]]
- [[../02-Frameworks/SGLang|SGLang]]
- [[../02-Frameworks/TensorRT-LLM|TensorRT-LLM]]
- [[../../AI-Learning/09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]]

## 资料

- [vLLM Docs](https://docs.vllm.ai/en/latest/)
- [SGLang Docs](https://docs.sglang.ai/)
- [TensorRT-LLM Docs](https://nvidia.github.io/TensorRT-LLM/)
