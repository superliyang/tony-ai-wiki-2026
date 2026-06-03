---
title: KServe
type: project
status: learning
tags:
  - cloud-native/project
  - cloud-native/ai
  - cloud-native/serving
created: 2026-03-25
updated: 2026-03-25
---

# KServe

## 定位

`KServe` 是一个构建在 Kubernetes 之上的模型服务平台，目标是把模型部署、推理扩缩容和推理 runtime 管理提升到平台层。

## 它解决什么问题

- 统一模型服务的部署抽象
- 支持 autoscaling 和 serverless-style 推理场景
- 管理 model runtime、predictor、transformer 等推理角色
- 把模型服务接入 Kubernetes 原生控制面和平台治理

## 为什么它重要

KServe 很适合作为“AI 时代云原生推理平台”的代表项目。它说明，模型服务已经不再只是应用服务的特例，而是需要专门平台抽象的 workload 类型。

## 学习重点

- 为什么 KServe 不是简单的 API 包装器
- 它和 Knative、Kubernetes、AI inference runtime 之间是什么关系
- 它在平台层提供了哪些比通用 Deployment 更有价值的抽象

## 来源

- [KServe Overview](https://kserve.github.io/website/latest/)
- [KServe Model Serving](https://kserve.github.io/website/latest/modelserving/)

## 相关

- [[../03-Topics/模型服务与推理平台|模型服务与推理平台]]
- [[Knative]]
- [[Kubernetes]]
