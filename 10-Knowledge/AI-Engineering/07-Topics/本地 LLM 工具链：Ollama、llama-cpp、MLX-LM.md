---
title: 本地 LLM 工具链：Ollama、llama.cpp、MLX-LM
type: topic
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# 本地 LLM 工具链：Ollama、llama.cpp、MLX-LM

## 为什么要把它们放一起

因为对本地学习来说，这三者刚好对应 3 层：

- `Ollama`：最容易上手的本地服务层
- `llama.cpp`：最值得理解的底层 runtime 层
- `MLX-LM`：最适合 Apple silicon 的原生实验层

## 该怎么学

### 先学 `Ollama`

目标：

- 快速跑通本地模型
- 用 API 接应用
- 用最小成本进入 RAG / agent

### 再学 `llama.cpp`

目标：

- 理解 quantization
- 理解 runtime tradeoff
- 理解本地推理为什么快/慢

### 最后学 `MLX-LM`

目标：

- 把 Apple silicon 路线学扎实
- 跑本地 fine-tuning 与原生实验

## 资料

- [Ollama Docs](https://docs.ollama.com/)
- [llama.cpp GitHub](https://github.com/ggml-org/llama.cpp)
- [MLX-LM](https://github.com/ml-explore/mlx-lm)
