---
title: Mac AI 专家验收清单
status: learning
created: 2026-03-26
updated: 2026-05-15
---

# Mac AI 专家验收清单

## Workbench

- 我有一个稳定的 Mac AI 实验工作流，而不是每次从搜索引擎重新开始
- 我能用 [[Mac AI 实验记录模板]] 记录问题、假设、命令、结果、bad cases 和判断
- 我能按 [[Mac AI 系统化实验路线图]] 选择下一步实验

## Foundations

- 我能解释 transformer、tokenization、pretraining、fine-tuning、RAG、agent
- 我能说清 instruction tuning、LoRA、eval 的关系

## Local Runtime

- 我能跑通 `Ollama`、`llama.cpp`、`MLX-LM` 至少两条路线
- 我能解释它们的核心差异与适用边界
- 我能解释 `GGUF`、quantization、context window、sampling 参数如何影响本地推理体验

## Training

- 我能在 `PyTorch MPS` 上做一个最小训练实验
- 我能解释 `mps` 和 `cuda` 的差异

## Fine-tuning

- 我能完成一次 LoRA / SFT，并做前后评测
- 我能解释为什么一次微调有效或无效

## Applications

- 我能做一个本地 RAG 或本地 agent 应用
- 我能给系统保留 trace、bad cases 和最小 eval 记录
- 我能把自己的知识库、游戏资料或安全资料接入本地 AI 工具链

## Engineering

- 我能解释 eval、observability、deployment、security 的基本边界
- 我能把本地实验总结成可复用工程经验

## Architecture

- 我能说清本地实验与云上生产的差异
- 我能把一个本地原型迁移成云上设计文档

## 最终标准

如果上面每一项你都能独立完成，并且能向别人解释 tradeoff，而不是只会重复命令，那么你已经进入真正的“AI / 大模型专家成长轨道”。
