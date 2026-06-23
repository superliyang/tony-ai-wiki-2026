---
title: vLLM
type: framework
status: seed
tags:
  - ai/framework
organization: open source
license: Apache-2.0
language: Python/CUDA
focus: LLM inference and serving
repo: https://github.com/vllm-project/vllm
release_date:
related_topics:
  - "[[../07-Topics/Inference Optimization|Inference Optimization]]"
  - "[[../07-Topics/Serving and Scaling|Serving and Scaling]]"
created: 2026-03-13
updated: 2026-03-13
---

# vLLM

## 简介

vLLM 是大模型推理与服务化领域的重要开源 runtime，重点解决吞吐、KV cache 和 serving 效率问题。

## 为什么它值得单独看

- 它代表了大模型时代 runtime 层正在成为独立竞争点
- 很多推理成本和吞吐问题，并不是换个模型就能解决，而是要靠 runtime

## 适用场景

- LLM 在线推理
- 多请求 batching
- 高吞吐服务化

## 核心模块

- PagedAttention
- runtime scheduling
- serving interface

## 优势与局限

- 优势是推理效率高、生态活跃
- 局限是仍需结合更完整的生产运维体系才能稳定上线

## 真正要看懂的地方

- vLLM 的价值不只是某个技术名词，而是它如何把内存管理、KV cache 和调度做成系统优化
- 它能帮你理解推理优化为什么是 runtime 与 serving 的共同问题

## 学习这页时最该记住什么

- 推理时代的重要创新很多发生在 runtime，而不是模型结构本身

## 相关

- [[../01-Stacks/LLM Inference Stack|LLM Inference Stack]]
- [[../07-Topics/Inference Optimization|Inference Optimization]]
