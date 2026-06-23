---
title: AI 时代的云原生
type: topic
status: learning
tags:
  - cloud-native/topic
  - cloud-native/ai
created: 2026-03-25
updated: 2026-03-25
---

# AI 时代的云原生

## 一句话理解

AI 时代的云原生，指的是把训练、推理、GPU 资源、分布式作业和模型服务纳入云原生平台视角，而不只是把 AI workload 当成普通容器任务来运行。

## 为什么这条线值得单独学

传统云原生更常围绕：

- stateless service
- CI/CD
- observability
- platform engineering

但 AI workload 会引入新的平台问题：

- GPU / accelerator 调度
- 训练作业与 batch queue
- 模型服务和在线推理
- 大规模 distributed execution
- 数据、模型、运行时和平台治理的耦合

## 这条主线通常包括什么

- accelerator-aware scheduling
- distributed training orchestration
- inference serving
- AI workload queueing 和 priority
- 在 Kubernetes 之上的 AI platform layer

## 学习重点

- AI workload 不是简单的“再跑一个 Deployment”
- Kubernetes 仍然是底座，但 AI 时代会长出 KServe、Kubeflow、KubeRay 这类更高层平台能力
- AI 时代的云原生，强调的不只是可部署性，而是资源利用率、训练效率和推理服务能力

## 来源

- [Cloud Native AI whitepaper](https://tag-app-delivery.cncf.io/whitepapers/cloud-native-artificial-intelligence-whitepaper/)
- [KServe Overview](https://kserve.github.io/website/latest/)
- [Kubeflow Overview](https://www.kubeflow.org/docs/started/introduction/)

## 相关

- [[Serverless 与事件驱动]]
- [[GPU 调度与加速器编排]]
- [[模型服务与推理平台]]
- [[AI 训练工作负载与编排]]
- [[../../AI-Engineering/07-Topics/Distributed Training|Distributed Training]]
- [[../../AI-Engineering/07-Topics/Serving and Scaling|Serving and Scaling]]
