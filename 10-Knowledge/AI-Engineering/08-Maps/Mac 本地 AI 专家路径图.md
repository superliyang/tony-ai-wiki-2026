---
title: Mac 本地 AI 专家路径图
type: map
status: learning
created: 2026-03-26
updated: 2026-05-15
---

# Mac 本地 AI 专家路径图

```mermaid
flowchart TB
  Start["Mac AI 工作台"] --> Lab["实验记录闭环"]

  subgraph Foundation["基础与本地运行"]
    Env["环境体检"]
    Runtime["Ollama / llama.cpp"]
    Quant["GGUF / 量化 / 上下文"]
  end

  subgraph Native["Apple Silicon 原生"]
    MPS["PyTorch MPS"]
    MLX["MLX / MLX-LM"]
    Memory["Unified Memory"]
  end

  subgraph Build["模型到系统"]
    Data["任务与数据"]
    Lora["LoRA / SFT"]
    RAG["本地 RAG"]
    Agent["本地 Agent"]
  end

  subgraph Govern["评测与工程化"]
    Eval["Eval / Bad Cases"]
    Trace["Trace / Observability"]
    Cloud["云上映射"]
  end

  Lab --> Env --> Runtime --> Quant
  Quant --> MPS --> MLX --> Memory
  Memory --> Data --> Lora --> Eval
  Eval --> RAG --> Agent --> Trace --> Cloud
  Cloud -.复盘.-> Lab

  classDef foundation fill:#e8f3ff,stroke:#4f8cc9,color:#0b253f;
  classDef native fill:#e9f8ee,stroke:#4a9f65,color:#10351d;
  classDef build fill:#fff3d6,stroke:#d99a1e,color:#3a2600;
  classDef govern fill:#f1e9ff,stroke:#8b61d1,color:#261344;
  class Start,Lab foundation;
  class Env,Runtime,Quant foundation;
  class MPS,MLX,Memory native;
  class Data,Lora,RAG,Agent build;
  class Eval,Trace,Cloud govern;
```

## 阅读入口

- [[../06-Projects/Mac AI Expert Path/Mac AI 工作台：从今天开始|Mac AI 工作台：从今天开始]]
- [[../06-Projects/Mac AI Expert Path/Mac AI 系统化实验路线图|Mac AI 系统化实验路线图]]
- [[../06-Projects/Mac AI Expert Path/Mac AI 专家 90 天路径|Mac AI 专家 90 天路径]]
