---
title: Kubeflow Trainer
type: project
status: learning
tags:
  - cloud-native/project
  - cloud-native/ai
  - cloud-native/training
created: 2026-03-25
updated: 2026-03-25
---

# Kubeflow Trainer

## 定位

`Kubeflow Trainer` 是 Kubeflow 体系里面向训练作业编排的重要能力，帮助平台在 Kubernetes 上管理分布式训练和训练 job 生命周期。

## 它解决什么问题

- 把训练作业抽象成可管理、可重复的 workload
- 支持分布式训练框架和训练任务编排
- 让训练过程更容易和 Kubernetes 资源、调度和平台治理集成

## 为什么它重要

Kubeflow Trainer 很适合作为“AI 训练进入云原生控制面”的代表项目。它说明训练平台不是普通 CI job，也不是单次脚本执行，而是需要专门调度和编排能力的系统。

## 学习重点

- 训练作业为什么需要 operator / trainer 抽象
- 它和 Kubeflow 更大平台体系的关系是什么
- 它如何和 distributed training、queueing、GPU scheduling 联动

## 来源

- [Kubeflow Overview](https://www.kubeflow.org/docs/started/introduction/)
- [Kubeflow Trainer](https://www.kubeflow.org/docs/components/trainer/)

## 相关

- [[../03-Topics/AI 训练工作负载与编排|AI 训练工作负载与编排]]
- [[Kubernetes]]
- [[KubeRay]]
