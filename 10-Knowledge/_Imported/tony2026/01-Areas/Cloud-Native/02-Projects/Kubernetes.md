---
title: Kubernetes
type: project
status: learning
tags:
  - cloud-native/project
  - cloud-native/kubernetes
created: 2026-03-24
updated: 2026-03-24
---

# Kubernetes

## 定位

`Kubernetes` 是云原生世界里最重要的编排平台之一。它不是简单的 deployment tool，而是一套以 API、控制器、调度器和声明式资源模型为核心的控制平面。

## 它解决什么问题

- container workload 的调度与运行
- 服务发现和负载均衡
- rollout / rollback
- self-healing
- secrets、config、storage 等运行时资源管理

## 学 Kubernetes 时最该抓的点

- 它是一个声明式系统，不只是命令集合
- 它通过 control loops 持续把当前状态收敛到期望状态
- 它不是全能 PaaS，而是平台构建的基础层

## 推荐学习视角

1. API object 是什么
2. Pod / Deployment / Service / ConfigMap / Secret 这些资源为什么存在
3. scheduler、controller、reconciliation 分别在做什么
4. 它如何成为 GitOps、platform engineering 和 observability 的基础设施底座

## 来源

- [Kubernetes Overview](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/)
- [Kubernetes Concepts](https://kubernetes.io/docs/concepts/index.html)

## 相关

- [[../01-Foundations/容器、编排与声明式系统|容器、编排与声明式系统]]
- [[../03-Topics/什么是云原生|什么是云原生]]
- [[../03-Topics/GitOps|GitOps]]
- [[../03-Topics/平台工程|平台工程]]
