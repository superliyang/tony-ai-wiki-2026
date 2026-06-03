---
title: Knative
type: project
status: learning
tags:
  - cloud-native/project
  - cloud-native/serverless
  - cloud-native/eventing
created: 2026-03-25
updated: 2026-03-25
---

# Knative

## 定位

`Knative` 是构建在 Kubernetes 之上的 serverless 平台与中间层集合，重点是把 request-driven service、event-driven workflow 和 function-style 开发体验提升到更高抽象。

## 它解决什么问题

- 简化 Kubernetes 上的 serverless workload 交付
- 提供自动扩缩容与 scale to zero
- 把事件路由与 event-driven 架构能力产品化
- 在 Kubernetes 之上提供更贴近开发者的高层抽象

## 为什么它重要

Knative 很适合帮助我们理解：云原生不是只有编排和平台工程，运行模型也会继续往上抽象。它把 Kubernetes 的复杂底层藏在背后，让团队更关注 service、event 和 trigger。

## 学习重点

- `Serving`、`Eventing`、`Functions` 是怎么分工的
- 为什么 Knative 既是 serverless 平台，也是 Kubernetes 生态的一部分
- 什么场景适合用 Knative，什么场景更适合直接用 Deployment / Service

## 来源

- [Knative Overview](https://knative.dev/docs/)
- [Knative Serving](https://knative.dev/docs/serving/)
- [Knative Eventing](https://knative.dev/docs/eventing/)

## 相关

- [[../03-Topics/Serverless 与事件驱动|Serverless 与事件驱动]]
- [[Kubernetes]]
- [[Istio]]
