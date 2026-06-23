---
title: Cube Studio
status: learning
created: 2026-06-21
updated: 2026-06-21
type: project
domain: ai-open-source
category: AI 基础设施与 MLOps 平台
source_status: verified-2026-06-21
tags:
  - knowledge
  - ai-open-source
  - ai-infrastructure
  - mlops
  - kubernetes
---

# Cube Studio

## 一句话定位

`Cube Studio` 是一个开源云原生一站式机器学习 / 深度学习 / 大模型 AI 平台，覆盖多租户、算力调度、Notebook、镜像构建、Pipeline、分布式训练、超参搜索、模型服务、模型市场、私有知识库和异构算力支持。

它适合放进你的知识库，是因为它不是单点工具，而是一个“AI 基础设施平台”的综合样本。

## 为什么值得学

如果未来要快速接手新的 AI 平台、MLOps 平台、训推平台或 MaaS 平台，最重要的不是记住某个按钮，而是看懂：

```text
用户 / 租户 / 项目
  -> 资源组 / 集群 / GPU / RDMA
  -> 镜像 / Notebook / 数据 / Pipeline
  -> 训练 / 微调 / 评测
  -> 模型仓库 / 模型服务 / API / 应用
  -> 监控 / 运维 / 成本 / 权限
```

`Cube Studio` 把这些层都摆在一个平台里，适合用来训练“平台视角”。

## Stack Position

| 层 | Cube Studio 体现出来的问题 |
|---|---|
| Platform Shell | 多租户、SSO、RBAC、项目组、资源组、菜单权限 |
| Compute Plane | 多集群、GPU / vGPU、国产 CPU/GPU/NPU、RDMA、边缘集群 |
| Dev Workspace | Notebook、Web shell、在线构建镜像、镜像仓库 |
| Workflow Plane | 拖拉拽 Pipeline、任务编排、超参搜索、分布式训练 |
| Model Plane | AIHUB 模型仓库、模型部署、模型推理、模型微调、模型二次开发 |
| Serving Plane | 推理服务、VGPU、vLLM / Ollama / MindIE 等大模型推理适配 |
| Knowledge / App Plane | 私有知识库、AI 应用商店、模型一键开发 / 推理 / 微调 |
| Ops Plane | 多集群运维、资源监控、任务 Pod 分布、权限和审计 |

## 关键抽象

### 1. 多租户和项目组

平台不是给单个 notebook 用户用的。它需要处理公司账号体系、项目空间、角色权限、资源组绑定、集群隔离和用户删除等问题。

### 2. 算力调度

AI 平台的底座不是“有 GPU”，而是资源如何被项目组申请、隔离、复用、虚拟化、调度和观测。

### 3. 镜像与工作环境

Cube Studio 的在线构建镜像能力很有代表性：平台试图降低算法工程师写 Dockerfile 的门槛，让用户可以通过 Web shell 调试环境并保存镜像。

### 4. Pipeline 与训练

拖拉拽 Pipeline、分布式训练、超参搜索和一键微调说明它瞄准的是完整算法链路，而不是单次脚本执行。

### 5. 模型资产和服务

AIHUB 提供模型仓库和模型市场视角：模型可以被部署、推理、微调和二次开发。这是从“训练作业”走向“模型资产运营”的关键变化。

## 和类似平台的关系

| 平台 / 系统 | 主要定位 | 和 Cube Studio 的关系 |
|---|---|---|
| [[10-Knowledge/AI-Open-Source/03-Projects/Kubeflow]] | Kubernetes 上的 AI / ML reference platform | Kubeflow 更社区化、模块化；Cube Studio 更像产品化的一站式平台 |
| [[10-Knowledge/AI-Open-Source/03-Projects/KServe]] | Kubernetes-native inference platform | KServe 聚焦 serving；Cube Studio 覆盖更大的训推和平台管理面 |
| [[10-Knowledge/AI-Open-Source/03-Projects/Ray]] | 分布式计算 / AI runtime | Ray 更像计算运行时；Cube Studio 更像平台控制面 |
| [[10-Knowledge/AI-Open-Source/03-Projects/vLLM]] | LLM serving 数据面 | vLLM 是推理后端之一；Cube Studio 是承载推理后端的平台 |
| MLflow / W&B | experiment tracking / model registry | 更偏实验和模型生命周期组件；Cube Studio 覆盖租户、资源、训练和服务 |
| Airflow / Argo / Flyte | workflow / pipeline 编排 | 可作为任务编排底座或相邻系统；Cube Studio 把 pipeline 包进平台体验 |

## 快速学习顺序

1. 先读官方 README 的功能清单，建立模块全貌。
2. 再读 AIHUB，理解模型仓库、部署、推理、微调和开发链路。
3. 再读构建镜像，理解平台如何降低环境构建门槛。
4. 再读模型管理和服务，补模型资产、服务和生命周期。
5. 最后和 Kubeflow / KServe 对比，抽象出平台边界。

## 下一步实验

| 实验 | 目的 |
|---|---|
| 画 Cube Studio 架构图 | 搞清 control plane、compute plane、workflow plane、serving plane |
| 和 Kubeflow 对照 | 判断“一站式平台”和“模块化平台”的差异 |
| 和 KServe 对照 | 判断模型 serving 子系统边界 |
| 梳理企业接入清单 | SSO、RBAC、项目组、资源组、镜像仓库、GPU、监控、审计 |

## 风险和边界

- 功能覆盖很广，学习时容易被菜单淹没，必须按平台层次拆。
- 开源版和企业版边界需要单独确认，不能把企业版能力默认当成开源能力。
- 国内异构算力、RDMA、边缘集群等能力很有现实意义，但需要通过部署文档和实际环境验证成熟度。
- 一站式平台对接企业流程会涉及权限、成本、运维、镜像安全和数据安全，不只是算法功能。

## Sources

- [Cube Studio GitHub](https://github.com/data-infra/cube-studio)
- [Cube Studio Wiki](https://github.com/data-infra/cube-studio/wiki)
- [Cube Studio AIHUB](https://github.com/data-infra/cube-studio/wiki/aihub)
- [Cube Studio 模型管理和服务](https://github.com/data-infra/cube-studio/wiki/%E6%A8%A1%E5%9E%8B%E7%AE%A1%E7%90%86%E5%92%8C%E6%9C%8D%E5%8A%A1)
- [Cube Studio 构建镜像](https://github.com/data-infra/cube-studio/wiki/%E6%9E%84%E5%BB%BA%E9%95%9C%E5%83%8F)
- [Cube Studio 企业版 vs 开源版](https://github.com/data-infra/cube-studio/wiki/%E4%BC%81%E4%B8%9A%E7%89%88vs%E5%BC%80%E6%BA%90%E7%89%88)

## Related

- [[10-Knowledge/AI-Engineering/07-Topics/AI 基础设施平台学习框架]]
- [[10-Knowledge/AI-Engineering/07-Topics/Enterprise MLOps 与 LLMOps Vendor Tradeoffs]]
- [[10-Knowledge/AI-Engineering/07-Topics/Open-Source、Self-Hosting 与 Managed LLMOps]]
- [[10-Knowledge/AI-Engineering/05-Deployment/部署索引]]

