---
title: Serverless 与事件驱动
type: topic
status: learning
tags:
  - cloud-native/topic
  - cloud-native/serverless
  - cloud-native/eventing
created: 2026-03-25
updated: 2026-03-25
---

# Serverless 与事件驱动

## 一句话理解

`Serverless` 在云原生里不是“没有服务器”，而是把运行、扩缩容和基础设施管理尽可能从开发者视角抽走，让团队更聚焦代码、事件和业务触发。

## 为什么它在云原生里值得单独学

在 Kubernetes 之后，很多团队已经能运行容器，但仍然要自己处理：

- service 暴露
- scale up / scale down
- 空闲资源浪费
- 事件触发链路
- workload 生命周期管理

Serverless 和 event-driven 平台就是在这层之上，继续提升抽象。

## 这条主线通常包括什么

- request-driven service
- event-driven workloads
- scale to zero
- function-style developer experience
- trigger、broker、source、sink 这类事件路由概念

## 学习重点

- `serverless` 是一类运行模型，不等于某一家云厂商产品
- 在云原生世界里，Knative 这类项目把 serverless 建在 Kubernetes 之上
- `event-driven` 往往不是附属能力，而是 serverless 体验的重要组成部分

## 来源

- [Serverless | Cloud Native Glossary](https://glossary.cncf.io/serverless/)
- [Knative Overview](https://knative.dev/docs/)

## 相关

- [[什么是云原生]]
- [[容器运行时与节点抽象]]
- [[云原生存储与状态管理]]
- [[../02-Projects/Knative|Knative]]
