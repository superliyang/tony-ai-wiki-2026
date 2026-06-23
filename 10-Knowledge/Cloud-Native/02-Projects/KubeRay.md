---
title: KubeRay
type: project
status: learning
tags:
  - cloud-native/project
  - cloud-native/ai
  - cloud-native/distributed
created: 2026-03-25
updated: 2026-03-25
---

# KubeRay

## 定位

`KubeRay` 是 Ray 在 Kubernetes 上的运行与管理层，帮助分布式 AI / data workload 以更原生的方式接到 Kubernetes 平台中。

## 它解决什么问题

- 在 Kubernetes 上运行和管理 Ray cluster
- 把分布式任务、训练、推理和 data workload 纳入平台视角
- 协调作业执行、集群生命周期和资源使用

## 为什么它重要

KubeRay 让我们看到，AI 时代的云原生不只是“训练”和“推理”两端，还包括 distributed execution framework 如何与 Kubernetes 真正结合。

## 学习重点

- Ray 本身和 KubeRay 的边界是什么
- 为什么 AI workload 需要比普通 Deployment 更高阶的 distributed runtime 抽象
- KubeRay 如何和 GPU scheduling、batch queueing、training orchestration 连接起来

## 来源

- [KubeRay on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html)
- [Ray Documentation](https://docs.ray.io/en/latest/)

## 相关

- [[../03-Topics/AI 训练工作负载与编排|AI 训练工作负载与编排]]
- [[../03-Topics/GPU 调度与加速器编排|GPU 调度与加速器编排]]
- [[Kubernetes]]
