---
title: CoreWeave Cloud
type: system
status: learning
tags:
  - ai/system
  - ai/cloud
  - ai/infra
created: 2026-03-25
updated: 2026-03-25
---

# CoreWeave Cloud

## 它是什么

`CoreWeave Cloud` 是一个围绕 AI workload 构建的云平台组合。它不是单一产品，而更像：

- AI-native GPU cloud
- managed Kubernetes substrate
- storage / networking / cluster platform
- training and inference hosting base

## 为什么它值得单独看

因为它代表了 AI 时代 cloud platform 的一个很重要变化：平台不再只是通用 IaaS，而是越来越像“为训练与推理定制的 capacity system”。

## 它最值得抓住的几个点

### 1. AI-native cloud 是它最关键的定位

官方平台页把重点放在 AI platform、capacity、performance 和 reliability，而不是传统云那种完整通用服务面。

### 2. Kubernetes 仍然是关键承载层

如果你在研究 AI infra，这一点很重要：AI cloud 并没有绕开 Kubernetes，反而在很多地方把它变成了更强的 workload substrate。

### 3. 它把训练与推理放在同一平台语境里

这让我们更容易理解：未来很多 AI infra 公司的竞争，不会只在 `train` 或 `serve` 某一头，而是会在整条 capacity / deployment lifecycle 上。

## 在整个生态里，我会把它放在哪

- 比 `Fireworks Inference Cloud` 更靠近底层 cloud substrate
- 比 `GroqCloud` 更像通用 AI cloud，而不是低时延推理专线
- 比 `NVIDIA Dynamo` 更靠近云平台，而不是 serving data plane

## 推荐继续往下读

- [[../01-Companies/CoreWeave|CoreWeave]]
- [[../06-Topics/AI 基础设施与 GPU Cloud|AI 基础设施与 GPU Cloud]]
- [[../../AI-Engineering/07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]]
- [[../../AI-Engineering/07-Topics/Serving and Scaling|Serving and Scaling]]

## 资料

- [CoreWeave Platform](https://www.coreweave.com/platform)
- [CoreWeave Docs](https://docs.coreweave.com/)
