---
title: KubeRay AI Platform on Kubernetes Case
type: case-study
status: learning
tags:
  - cloud-native/case-study
  - cloud-native/ai
  - cloud-native/distributed
created: 2026-03-25
updated: 2026-03-25
---

# KubeRay AI Platform on Kubernetes Case

## 为什么看这个案例

这个案例适合帮助我们理解：当 AI workload 从单机训练和单点推理走向 distributed execution 时，为什么 Ray 需要一个 Kubernetes-native 的平台承接层，而不是直接裸跑集群。

## 这个案例最有代表性的点

- KubeRay 把 Ray cluster、RayJob、autoscaling 和运维入口接到 Kubernetes 控制面
- 官方文档已经围绕 Kubernetes 给出了 job、dashboard、autoscaling 这些平台能力
- Anyscale on Kubernetes 的官方叙述说明，企业会希望把 Ray workload 放进已有 Kubernetes 治理、身份、网络与观测体系内

## 你应该从中看到什么

- 分布式 AI 执行框架最终也会走向 platformization，而不是长期停留在临时脚本和一次性集群上
- AI 时代的云原生不只需要训练平台和推理平台，还需要 distributed compute 平台
- KubeRay 是把 distributed Python / AI runtime 真正接入 Kubernetes 的代表路径之一

## 来源

- [KubeRay on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html)
- [RayJob Quickstart](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/rayjob-quick-start.html)
- [KubeRay Autoscaling](https://docs.ray.io/en/latest/cluster/kubernetes/user-guides/configuring-autoscaling.html)
- [Anyscale on Kubernetes](https://www.anyscale.com/blog/announcing-anyscale-on-kubernetes-k8s)

## 相关

- [[../03-Topics/GPU 调度与加速器编排|GPU 调度与加速器编排]]
- [[../03-Topics/AI 训练工作负载与编排|AI 训练工作负载与编排]]
- [[../02-Projects/KubeRay|KubeRay]]
- [[../../AI-Engineering/07-Topics/Distributed Training|Distributed Training]]
