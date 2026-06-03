---
title: Amazon EKS Containerd Migration Case
type: case-study
status: learning
tags:
  - cloud-native/case-study
  - cloud-native/runtime
  - cloud-native/containerd
created: 2026-03-25
updated: 2026-03-25
---

# Amazon EKS Containerd Migration Case

## 为什么看这个案例

这个案例很适合帮助我们理解：`containerd` 之所以重要，不只是因为它是一个更轻量的 runtime，而是因为 Kubernetes 生态正在把 runtime 层重新收敛到 `CRI` 这一套更干净的边界上。

## 这个案例最有代表性的点

- `dockershim` 移除后，EKS 从 Kubernetes `1.24` 开始把 `containerd` 作为默认 runtime
- 迁移的难点不是“容器能不能跑”，而是围绕 Docker socket、日志格式、安全代理、观测代理的生态依赖
- 这说明 runtime migration 本质上是平台兼容性治理，而不是单纯节点升级

## 你应该从中看到什么

- 云原生 runtime 层最终会从“隐形底座”变成平台团队必须管理的兼容性边界
- `CRI` 的价值在于把 Kubernetes 核心和底层 runtime 解耦
- 真实组织在 runtime 升级时，最怕的不是应用本身，而是周边 agent、logging、security tooling 的隐性耦合

## 来源

- [All you need to know about moving to containerd on Amazon EKS](https://aws.amazon.com/blogs/containers/all-you-need-to-know-about-moving-to-containerd-on-amazon-eks/)
- [Amazon EKS 1.21 containerd support](https://aws.amazon.com/blogs/containers/amazon-eks-1-21-released/)

## 相关

- [[../03-Topics/容器运行时与节点抽象|容器运行时与节点抽象]]
- [[../02-Projects/containerd|containerd]]
- [[../04-Maps/运行时与状态案例图|运行时与状态案例图]]
