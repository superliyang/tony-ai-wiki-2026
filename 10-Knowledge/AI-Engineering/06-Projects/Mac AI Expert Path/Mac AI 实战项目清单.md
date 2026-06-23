---
title: Mac AI 实战项目清单
status: learning
created: 2026-03-26
updated: 2026-05-15
---

# Mac AI 实战项目清单

## 项目 0：个人 AI 实验工作台

目标：让学习过程可复盘，而不是只留下安装痕迹。

输出：

- 一套本地环境记录
- 至少 3 篇基于 [[Mac AI 实验记录模板]] 的实验记录
- 一份 `Ollama / llama.cpp / MLX-LM / PyTorch MPS` 默认选型规则

## 项目 1：本地聊天应用

目标：理解模型运行、prompt 控制、UI / API 封装。

输出：

- 一个能切换模型和 system prompt 的本地聊天应用
- 一份 prompt 实验记录

## 项目 2：本地 RAG 文档问答

目标：理解 retrieval pipeline。

输出：

- 本地文档问答原型
- bad-case 样本集
- chunking / embedding 对比记录

## 项目 3：本地 LoRA 微调实验

目标：理解数据、微调参数和评测。

输出：

- 一次完整 LoRA 训练
- baseline vs tuned 对比结果

## 项目 4：本地 agent + tool use 原型

目标：理解 tools、memory、planning、error handling。

输出：

- 一个带至少两个工具的本地 agent
- 一份失败路径分析

## 项目 5：从本地原型迁移到云上设计文档

目标：把个人实验翻译成团队能接手的设计。

输出：

- 一份系统设计文档
- 一份风险与成本说明

## 项目 6：面向真实资料的个人知识助手

目标：把自己的知识库、游戏资料、安全资料或 AI 学习资料接成本地助手。

输出：

- 一个可选择资料目录的本地 RAG / agent 原型
- 一组固定 eval questions
- 一份 bad-case library
- 一份“哪些资料适合本地，哪些需要云上或团队平台”的判断

## 建议顺序

严格按 0 -> 6 做，不要反过来。

因为你真正需要的是：

- 先把系统跑起来
- 再把评测和治理补上
- 最后再谈架构与生产化
