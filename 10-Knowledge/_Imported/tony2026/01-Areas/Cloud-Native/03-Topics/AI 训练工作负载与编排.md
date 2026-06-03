---
title: AI 训练工作负载与编排
type: topic
status: learning
tags:
  - cloud-native/topic
  - cloud-native/ai
  - cloud-native/training
created: 2026-03-25
updated: 2026-03-25
---

# AI 训练工作负载与编排

## 一句话理解

AI 训练工作负载与编排关注的是：如何把 batch、distributed training、作业队列和资源调度纳入云原生平台，而不是只让训练脚本“能跑起来”。

## 为什么这件事和普通应用编排不同

训练 workload 更常面对：

- 长时间运行
- 多机多卡协同
- 作业排队与优先级
- checkpoint 与恢复
- 对网络、存储、GPU 的强依赖

这意味着训练平台不只是部署系统，而是 workload orchestration 系统。

## 这条主线通常包括什么

- training operators
- job-style orchestration
- distributed execution frameworks
- queueing and priority
- experiment / artifact / model lifecycle integration

## 学习重点

- Kubeflow Trainer 和 KubeRay 这类项目为什么会出现
- AI 训练在 Kubernetes 上不是直接把 Python job 包一层 YAML 就结束
- training orchestration 和 AI-Engineering 的 distributed training 是强耦合关系

## 来源

- [Kubeflow Overview](https://www.kubeflow.org/docs/started/introduction/)
- [Kubeflow Trainer](https://www.kubeflow.org/docs/components/trainer/)
- [KubeRay on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html)

## 相关

- [[AI 时代的云原生]]
- [[GPU 调度与加速器编排]]
- [[模型服务与推理平台]]
- [[../02-Projects/Kubeflow Trainer|Kubeflow Trainer]]
- [[../02-Projects/KubeRay|KubeRay]]
- [[../../AI-Engineering/07-Topics/Distributed Training|Distributed Training]]
