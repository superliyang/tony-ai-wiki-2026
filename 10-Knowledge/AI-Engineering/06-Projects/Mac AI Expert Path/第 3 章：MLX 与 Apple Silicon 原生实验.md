---
title: 第 3 章：MLX 与 Apple Silicon 原生实验
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# 第 3 章：MLX 与 Apple Silicon 原生实验

## 本章目标

把 Apple silicon 的原生路线学扎实，让你真正理解为什么 `MLX` 值得单独学习。

## 这章重点不是“换个框架”

真正重点是：

- 理解 unified memory 对模型实验的影响
- 理解 `MLX` 为什么对 Apple silicon 用户更自然
- 学会用 `MLX-LM` 跑模型、测生成、做最小改造

## 建议实验

### 实验 1：用 MLX-LM 跑一个 instruction model

记录：

- 模型加载体验
- 生成速度
- 和 `Ollama` / `llama.cpp` 的差异

### 实验 2：改 prompt 模板并观察输出稳定性

目标：让你把 runtime 和模型行为联系起来。

### 实验 3：做一个最小 LoRA 或 adapter 实验

目标：为下一章微调做好准备。

## 你应该建立的判断

- 什么时候用 `PyTorch MPS`
- 什么时候用 `MLX`
- 什么时候本地原生路线比通用框架更顺手

## 本章输出物

- 一个 `MLX-LM` 最小推理脚本
- 一份 `MLX vs PyTorch MPS` 的对比笔记
- 一个可复用的实验模板

## 继续阅读

- [[第 4 章：微调、LoRA 与评测]]
- [[../../07-Topics/MLX 与 Apple Silicon 原生大模型实践|MLX 与 Apple Silicon 原生大模型实践]]
- [[../../../AI-Learning/09-Systems/MLX|MLX]]
