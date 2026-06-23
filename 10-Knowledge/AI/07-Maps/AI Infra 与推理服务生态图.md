---
title: AI Infra 与推理服务生态图
type: map
status: learning
tags:
  - ai/map
  - ai/infra
  - ai/inference
created: 2026-03-25
updated: 2026-03-25
---

# AI Infra 与推理服务生态图

```mermaid
flowchart TD
  T["AI 基础设施与 GPU Cloud"] --> I["Inference Serving"]

  subgraph companies["公司"]
    NV["[[../01-Companies/NVIDIA|NVIDIA]]"]
    CW["[[../01-Companies/CoreWeave|CoreWeave]]"]
    GQ["[[../01-Companies/Groq|Groq]]"]
    FW["[[../01-Companies/Fireworks AI|Fireworks AI]]"]
  end

  subgraph systems["系统 / 平台"]
    DY["[[../09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]]"]
    CC["[[../09-Systems/CoreWeave Cloud|CoreWeave Cloud]]"]
    GC["[[../09-Systems/GroqCloud|GroqCloud]]"]
    FI["[[../09-Systems/Fireworks Inference Cloud|Fireworks Inference Cloud]]"]
  end

  subgraph engineering["工程抽象"]
    INF["[[../../AI-Engineering/07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]]"]
    OPT["[[../../AI-Engineering/07-Topics/Inference Optimization|Inference Optimization]]"]
    SS["[[../../AI-Engineering/07-Topics/Serving and Scaling|Serving and Scaling]]"]
    KV["[[../../AI-Engineering/07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]]"]
    DS["[[../../AI-Engineering/07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]"]
    VLLM["[[../../AI-Engineering/02-Frameworks/vLLM|vLLM]]"]
    SGL["[[../../AI-Engineering/02-Frameworks/SGLang|SGLang]]"]
    TRT["[[../../AI-Engineering/02-Frameworks/TensorRT-LLM|TensorRT-LLM]]"]
  end

  NV --> DY
  NV --> TRT
  CW --> CC
  GQ --> GC
  FW --> FI

  T --> NV
  T --> CW
  T --> GQ
  T --> FW
  I --> DY
  I --> GC
  I --> FI

  DY --> DS
  DY --> SS
  CC --> INF
  CC --> SS
  GC --> SS
  FI --> SS
  I --> OPT
  I --> KV
  I --> DS
  DS --> VLLM
  DS --> SGL
  DS --> TRT
  OPT --> KV
  INF --> SS
```

## 怎么读这张图

- `AI 基础设施与 GPU Cloud` 看的是供给与平台底座
- `Inference Serving` 看的是能力如何被稳定、低成本地交付
- 公司页回答“谁在这个市场里占位”
- 系统页回答“它们把能力包装成了什么平台或数据面”
- 工程页回答“这些平台背后的真正系统问题是什么”

## 推荐顺序

1. [[../06-Topics/AI 基础设施与 GPU Cloud|AI 基础设施与 GPU Cloud]]
2. [[../06-Topics/Inference Serving|Inference Serving]]
3. [[../01-Companies/NVIDIA|NVIDIA]]
4. [[../01-Companies/CoreWeave|CoreWeave]]
5. [[../01-Companies/Groq|Groq]]
6. [[../01-Companies/Fireworks AI|Fireworks AI]]
7. [[../09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]]
8. [[../09-Systems/CoreWeave Cloud|CoreWeave Cloud]]
9. [[../09-Systems/GroqCloud|GroqCloud]]
10. [[../09-Systems/Fireworks Inference Cloud|Fireworks Inference Cloud]]
11. [[../../AI-Engineering/08-Maps/Inference and Serving Map|Inference and Serving Map]]

## 关联

- [[AI Ecosystem Map]]
- [[AI Company-Systems Map]]
- [[../../AI-Engineering/08-Maps/Inference and Serving Map|Inference and Serving Map]]
