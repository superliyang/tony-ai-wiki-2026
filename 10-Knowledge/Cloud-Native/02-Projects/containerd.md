---
title: containerd
type: project
status: learning
tags:
  - cloud-native/project
  - cloud-native/runtime
created: 2026-03-25
updated: 2026-03-25
---

# containerd

## 定位

`containerd` 是云原生世界里最重要的容器运行时之一，强调 simplicity、robustness 和 portability。它更多处在执行层，而不是编排层。

## 它解决什么问题

- 管理镜像拉取与存储
- 管理容器生命周期
- 作为节点上的 container runtime 与 kubelet 协作
- 为高层平台提供稳定的执行基础

## 为什么它重要

很多“学 Kubernetes”的路径会把 runtime 隐藏起来，但真正理解 node 行为、runtime 配置、cgroup 与 CRI，离不开 containerd 这一层。

## 学习重点

- 为什么 Kubernetes node 需要 CRI-compatible runtime
- containerd 和 kubelet 是如何协作的
- runtime 问题为什么常常会影响资源管理、稳定性和节点配置

## 来源

- [containerd](https://containerd.io/)
- [Container Runtimes | Kubernetes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)

## 相关

- [[../03-Topics/容器运行时与节点抽象|容器运行时与节点抽象]]
- [[Kubernetes]]
