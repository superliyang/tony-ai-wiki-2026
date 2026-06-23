---
title: Rook
type: project
status: learning
tags:
  - cloud-native/project
  - cloud-native/storage
created: 2026-03-25
updated: 2026-03-25
---

# Rook

## 定位

`Rook` 是一个云原生存储 orchestrator，它把 Ceph 这样的分布式存储能力以更原生的方式接到 Kubernetes 和云原生环境里。

## 它解决什么问题

- 在 Kubernetes 中操作化 block / file / object storage
- 把复杂的分布式存储生命周期纳入云原生控制面
- 让持久化与 stateful workload 更接近平台化能力，而不是纯手工运维

## 为什么它重要

Rook 很适合作为“云原生世界里的存储平台化”代表项目。它提醒我们：云原生不只是 stateless app，状态与数据层同样可以被编排和治理。

## 学习重点

- Ceph 在这里扮演什么角色
- Rook 为什么更像存储 orchestrator，而不是单一存储引擎
- 它如何和 StorageClass、CSI、stateful workload 这些概念连接起来

## 来源

- [Rook Overview](https://rook.io/docs/rook/latest-release/Getting-Started/intro/)
- [Storage Classes | Kubernetes](https://kubernetes.io/docs/concepts/storage/storage-classes/)

## 相关

- [[../03-Topics/云原生存储与状态管理|云原生存储与状态管理]]
- [[Kubernetes]]
