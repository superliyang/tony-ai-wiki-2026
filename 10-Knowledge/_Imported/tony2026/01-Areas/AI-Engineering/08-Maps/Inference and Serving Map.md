---
title: Inference and Serving Map
type: map
status: learning
tags:
  - ai/maps
created: 2026-03-13
updated: 2026-03-28
---

# Inference and Serving Map

```mermaid
flowchart TD
  A["Infrastructure (GPU-TPU)"] --> B["Inference Optimization"]
  B --> C["Serving and Scaling"]
  B --> D["KV Cache / Prefill-Decode / Continuous Batching"]
  C --> E["Disaggregated Serving 与推理数据面"]
  D --> E
  C --> F["训练与推理成本工程"]
  E --> F
  F --> G["Cost, Latency, and Safety Tradeoffs"]
  A --> H["分布式基础设施与推理平台案例"]
  E --> H
  F --> H

  subgraph backends["Backend Runtimes"]
    V["[[../02-Frameworks/vLLM|vLLM]]"]
    S["[[../02-Frameworks/SGLang|SGLang]]"]
    T["[[../02-Frameworks/TensorRT-LLM|TensorRT-LLM]]"]
  end

  subgraph systems["Platforms / Data Plane"]
    DY["[[../../AI-Learning/09-Systems/NVIDIA Dynamo|NVIDIA Dynamo]]"]
    CC["[[../../AI-Learning/09-Systems/CoreWeave Cloud|CoreWeave Cloud]]"]
    GC["[[../../AI-Learning/09-Systems/GroqCloud|GroqCloud]]"]
    FI["[[../../AI-Learning/09-Systems/Fireworks Inference Cloud|Fireworks Inference Cloud]]"]
  end

  V --> E
  S --> E
  T --> E
  DY --> E
  CC --> C
  GC --> G
  FI --> F
```

## 怎么读这张图

- 左边主线：从 infra、runtime、serving 到 data plane 的工程主线。
- 中间新增：把成本工程和 cost-latency-safety tradeoff 接到 serving 主线里。
- 右侧案例：用 `Dynamo / Groq / Fireworks / CoreWeave` 把抽象层落回真实平台。

## 推荐阅读顺序

1. [[../07-Topics/Infrastructure (GPU-TPU)|Infrastructure (GPU-TPU)]]
2. [[../07-Topics/Inference Optimization|Inference Optimization]]
3. [[../07-Topics/Serving and Scaling|Serving and Scaling]]
4. [[../07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]
5. [[../07-Topics/训练与推理成本工程|训练与推理成本工程]]
6. [[../07-Topics/Cost, Latency, and Safety Tradeoffs|Cost, Latency, and Safety Tradeoffs]]
7. [[../07-Topics/分布式基础设施与推理平台案例：Cloud TPU、TorchTitan、Dynamo、Groq、Fireworks|分布式基础设施与推理平台案例：Cloud TPU、TorchTitan、Dynamo、Groq、Fireworks]]
