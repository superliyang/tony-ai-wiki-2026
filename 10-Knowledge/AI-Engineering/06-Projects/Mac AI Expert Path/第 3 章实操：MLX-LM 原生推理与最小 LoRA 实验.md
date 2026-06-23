---
title: 第 3 章实操：MLX-LM 原生推理与最小 LoRA 实验
status: learning
created: 2026-03-27
updated: 2026-03-27
---

# 第 3 章实操：MLX-LM 原生推理与最小 LoRA 实验

## 本章目标

把 `MLX` / `MLX-LM` 真正跑起来，并且开始建立 Apple silicon 原生实验直觉。

## 为什么这一步重要

如果 `PyTorch MPS` 让你理解“训练基本功”，那么 `MLX-LM` 会让你理解：

- Apple silicon 原生路线为什么值得单独学
- 本地大模型实验为什么不一定非要沿着通用 CUDA 思路来组织
- 量化、prompt cache、LoRA 在本机实验里如何组合

## 最小推理实验

官方最容易跑通的入口是 `mlx_lm.generate`。

```bash
python -m pip install mlx mlx-lm
mlx_lm.generate --prompt "Explain what unified memory means for local LLM work."
```

你至少要记录：

- 使用的模型
- 加载速度
- 首 token 体验
- 长回复时的稳定性

## Python API 最小示例

```python
from mlx_lm import load, generate

model, tokenizer = load('mlx-community/Llama-3.2-3B-Instruct-4bit')
prompt = 'Give me three practical uses of local LLMs on a Mac.'
text = generate(model, tokenizer, prompt=prompt, verbose=True)
print(text)
```

## 第一个对比实验

拿同一个 prompt 比较：

- `Ollama`
- `llama.cpp`
- `MLX-LM`

重点记录：

- 速度
- 主观流畅度
- 模型切换难易度
- Python 集成顺手程度

## 第二个实验：prompt cache 或长上下文体验

`mlx-lm` 官方支持 prompt caching 和长 prompt 工具。你可以用这一步开始建立一个很重要的工程直觉：

- 同样的上下文，能否高效复用
- 长 prompt 代价到底体现在哪

## 第三个实验：最小 LoRA / fine-tune

这一步不求大而全，只求“真的做过一次”。

目标：

- 选择一个足够小的 instruction model
- 准备一个很小、可解释的数据集
- 做一次最小 LoRA 或 fine-tuning
- 跑一次前后对比

## 你至少要记录的材料

- 基础模型
- 数据集来源与大小
- 训练配置
- 前测结果
- 后测结果
- 明显失败样例

## 你会建立什么判断

完成这一步后，你应该能开始判断：

- 什么时候 `MLX-LM` 比 `Ollama` 更适合实验
- 什么时候 `MLX-LM` 比通用 PyTorch 路线更顺手
- 什么时候本地实验已经到边界，需要迁移到云上更强资源

## 本章输出物

- 一个 `scripts/run_mlx_lm.py`
- 一份 `MLX-LM vs Ollama vs llama.cpp` 对比表
- 一次最小 LoRA / fine-tune 记录
- 一份前后效果对比

## 官方资料入口

- [MLX Quick Start](https://ml-explore.github.io/mlx/build/html/usage/quick_start.html)
- [MLX GitHub](https://github.com/ml-explore/mlx)
- [MLX-LM GitHub](https://github.com/ml-explore/mlx-lm)

## 下一步

- [[第 4 章：微调、LoRA 与评测]]
- [[../../07-Topics/MLX 与 Apple Silicon 原生大模型实践|MLX 与 Apple Silicon 原生大模型实践]]
- [[../../07-Topics/Mac 本地微调：LoRA、QLoRA 与 MLX-LM|Mac 本地微调：LoRA、QLoRA 与 MLX-LM]]
