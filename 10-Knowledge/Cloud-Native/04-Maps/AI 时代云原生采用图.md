---
title: AI 时代云原生采用图
type: map
status: learning
tags:
  - cloud-native/maps
  - cloud-native/ai
  - cloud-native/adoption
created: 2026-03-25
updated: 2026-03-25
---

# AI 时代云原生采用图

```mermaid
flowchart LR
    A["AI 时代云原生采用路径"] --> B["Experimentation"]
    A --> C["Shared Infrastructure"]
    A --> D["Guarded Platform Services"]
    A --> E["AI Platform Operating Model"]
    E --> F["AI 工作负载平台团队工作方式"]
    F --> G["AI 平台团队采用推进工作流"]
    D --> H["KServe Enterprise LLM Serving Case"]
    E --> I["Kubeflow AI Platform Reference Case"]
    B --> J["OpenAI Kubernetes Experimentation Boundary Case"]
    E --> K["Cloudchipr AI Copilot Platform Scaling Case"]
```

## 解读

- adoption path 不是先把所有 AI 能力都平台化，而是从试验和 shared services 开始
- `KServe` 更像 serving 平台化阶段的代表案例
- `Kubeflow` 更像 AI platform team operating model 开始成型后的代表案例
- `OpenAI` 更像实验与平台边界如何划分的代表案例
- `Cloudchipr` 更像 AI copilot 企业平台进入治理与成本闭环的代表案例
