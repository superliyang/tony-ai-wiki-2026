---
title: Fireworks Inference Cloud
type: system
status: learning
tags:
  - ai/system
  - ai/inference
  - ai/cloud
created: 2026-03-25
updated: 2026-03-25
---

# Fireworks Inference Cloud

## 它是什么

`Fireworks Inference Cloud` 是 Fireworks AI 提供的模型托管与推理平台。官方文档把它描述成一个可以支持：

- serverless inference
- on-demand / dedicated deployments
- open-model serving
- 更完整 deployment 生命周期

的服务层。

## 为什么它值得单独看

因为它代表了 AI infra 里很重要的一种产品形态：

- 不自己发明硬件
- 不一定自己做底层云
- 但把 inference deployment experience 做成产品

这对很多应用团队来说反而是最直接可用的一层。

## 它最值得抓住的几个点

### 1. 它是 platform abstraction，不是单个 runtime

这能帮助你区分：

- `vLLM` / `SGLang` / `TensorRT-LLM` 是 runtime / backend
- `Fireworks Inference Cloud` 是部署与服务抽象层

### 2. serverless 与 dedicated 是一条很重要的产品边界

它们分别对应：

- 更快上手
- 更强控制 / 隔离 / 稳定性

### 3. open-model era 需要新的 deployment layer

模型越来越多、权重越来越开放，很多团队并不想自己维护完整 serving stack，所以会出现这种独立平台层。

## 推荐继续往下读

- [[../01-Companies/Fireworks AI|Fireworks AI]]
- [[../06-Topics/Inference Serving|Inference Serving]]
- [[../../AI-Engineering/07-Topics/Serving and Scaling|Serving and Scaling]]
- [[../../AI-Engineering/08-Maps/Inference and Serving Map|Inference and Serving Map]]

## 资料

- [Fireworks AI Docs](https://docs.fireworks.ai/getting-started/introduction)
- [Fireworks Deployments](https://docs.fireworks.ai/deployments/what-are-deployments)
