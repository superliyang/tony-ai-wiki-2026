---
title: AI 工作负载接入工作流
type: workflow
status: learning
tags:
  - cloud-native/workflow
  - cloud-native/ai
created: 2026-03-25
updated: 2026-03-25
---

# AI 工作负载接入工作流

## 简介

`AI 工作负载接入工作流` 关注的是：一个 AI 团队要把训练或推理任务接到云原生平台时，平台应该如何判断它属于训练、推理还是 distributed execution 路径，并配上合适的资源与治理方式。

## 输入

- workload 是 training 还是 inference
- 是否需要 GPU / accelerator
- 是否需要分布式执行
- 对延迟、吞吐、成本和优先级的要求
- 对模型版本、运行时和平台治理的要求

## 步骤

1. 明确 workload 属于训练、推理，还是统一的分布式任务
2. 评估 GPU 与加速器需求，以及队列和优先级策略
3. 推理场景优先评估 KServe / serving path
4. 训练和 distributed 场景评估 Kubeflow Trainer、KubeRay 或其他作业编排路径
5. 将运行时、模型、资源和平台治理边界纳入标准平台 workflow

## 输出

- AI workload classification
- serving / training / distributed path decision
- resource and scheduling requirements
- platform integration requirements

## 评估

- AI workload 是否进入了合适的平台抽象层
- 资源约束、运行模式和治理边界是否提前说清
- 是否避免把 AI workload 硬塞进不合适的普通应用路径

## 来源

- [KServe Overview](https://kserve.github.io/website/latest/)
- [Kubeflow Trainer](https://www.kubeflow.org/docs/components/trainer/)
- [KubeRay on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/index.html)
- [Schedule GPUs in Kubernetes](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)

## 相关

- [[../03-Topics/AI 时代的云原生|AI 时代的云原生]]
- [[../03-Topics/GPU 调度与加速器编排|GPU 调度与加速器编排]]
- [[../03-Topics/模型服务与推理平台|模型服务与推理平台]]
- [[../03-Topics/AI 训练工作负载与编排|AI 训练工作负载与编排]]
