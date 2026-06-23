---
title: Mac AI 专家 90 天路径
status: learning
created: 2026-03-26
updated: 2026-05-15
---

# Mac AI 专家 90 天路径

## 使用方式

这条 90 天路径现在有两种用法：

- 学习模式：按章节顺序读，适合系统补基础
- 实验模式：按 [[Mac AI 系统化实验路线图]] 的 `E0-E12` 做，适合边玩边学

每周至少复制一次 [[Mac AI 实验记录模板]]，否则这条路线很容易变成“看过很多、留下很少”。

## 第 1-30 天：打牢本地实验底座

### 第 1 周

- 先看 [[Mac AI 工作台：从今天开始]]
- 完成 [[第 0 章：环境与工具链搭建]]
- 验证 `PyTorch MPS`、`Ollama`、`MLX-LM` 至少两条路线可运行
- 输出：环境记录与最小脚本

### 第 2 周

- 完成 [[第 1 章：本地推理与模型运行]]
- 比较 `Ollama`、`llama.cpp`、`MLX-LM`
- 输出：runtime 对比表
- 对应实验：[[Mac AI 系统化实验路线图]] 的 `E1-E3`

### 第 3 周

- 学完 [[第 2 章：PyTorch MPS 与训练基础]]
- 跑一个最小训练任务
- 输出：`CPU vs MPS` 观察笔记

### 第 4 周

- 回顾 [[../../07-Topics/Apple Silicon、Metal 与本地 AI 开发|Apple Silicon、Metal 与本地 AI 开发]]
- 补齐基础薄弱处
- 输出：个人知识空白清单

## 第 31-60 天：进入原生实验与微调

### 第 5-6 周

- 完成 [[第 3 章：MLX 与 Apple Silicon 原生实验]]
- 输出：`MLX vs PyTorch MPS` 对比笔记

### 第 7-8 周

- 完成 [[第 4 章：微调、LoRA 与评测]]
- 输出：一次完整 LoRA / SFT 实验

## 第 61-90 天：把模型变成系统

### 第 9-10 周

- 完成 [[第 5 章：RAG、Agent 与本地应用开发]]
- 输出：本地 RAG 或 agent 原型

### 第 11 周

- 加上 trace / eval / bad-case 集合
- 输出：最小 observability 与 eval 记录

### 第 12 周

- 完成 [[第 6 章：从 Mac 实验室到云上系统]]
- 输出：一份云上迁移设计文档
- 对应实验：[[Mac AI 系统化实验路线图]] 的 `E12`

## 90 天之后的延伸

- `AI Security`
- `MLOps / LLMOps`
- `Inference Serving`
- `Agent Platform`

这些都已经在现有 AI 体系里准备好了，你可以继续回到：

- [[../../../AI-Learning/专题总览|AI Learning]]
- [[../../专题总览|AI-Engineering]]
