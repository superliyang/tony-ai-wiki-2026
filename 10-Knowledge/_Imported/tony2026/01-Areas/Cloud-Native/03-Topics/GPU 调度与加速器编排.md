---
title: GPU 调度与加速器编排
type: topic
status: learning
tags:
  - cloud-native/topic
  - cloud-native/ai
  - cloud-native/gpu
created: 2026-03-25
updated: 2026-03-25
---

# GPU 调度与加速器编排

## 一句话理解

在 AI 时代，Kubernetes 不再只调度 CPU 和内存，平台还必须理解 GPU、加速器、设备插件和资源隔离，否则 AI workload 无法高效运行。

## 为什么这层重要

AI workload 往往受限于加速器资源，而不是普通计算资源。平台如果不理解这一层，就会出现：

- GPU 资源碎片化
- 训练作业排队低效
- 推理服务和训练作业争抢资源
- 节点能力与 workload 需求不匹配

## 这条主线通常包括什么

- device plugins
- GPU scheduling
- taints / tolerations / node labels
- batch queueing and priority
- accelerator-aware workload placement

## 学习重点

- Kubernetes 为什么把 GPU 当成扩展资源来处理
- device plugin 是加速器接入集群的重要边界
- AI 平台的挑战不只是“有 GPU”，而是“GPU 被怎样组织、分配和治理”

## 来源

- [Schedule GPUs in Kubernetes](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)
- [Device Plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
- [KubeRay on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html)

## 相关

- [[AI 时代的云原生]]
- [[AI 训练工作负载与编排]]
- [[模型服务与推理平台]]
- [[../02-Projects/KubeRay|KubeRay]]
- [[../../AI-Engineering/07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]]
