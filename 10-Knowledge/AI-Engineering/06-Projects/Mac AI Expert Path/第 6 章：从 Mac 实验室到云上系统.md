---
title: 第 6 章：从 Mac 实验室到云上系统
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# 第 6 章：从 Mac 实验室到云上系统

## 本章目标

把本地学到的能力映射到真正的生产世界。

## 你要学会回答的 4 个问题

### 1. 什么应该继续留在本地

- 个人实验
- prompt / eval 试验
- 小规模 RAG / agent 原型
- 小团队内部工具

### 2. 什么必须迁到云上

- 需要更大吞吐和更强 SLA 的 serving
- 多用户共享系统
- 长期运行的 workflow / agent
- 更严格的 observability、security、cost control

### 3. 云上之后，问题为什么会完全变样

因为一旦进入生产，你会面对：

- deployment
- autoscaling
- serving data plane
- secret management
- security review
- cost / latency / reliability tradeoff

### 4. 本地实验应该如何翻译成设计文档

你至少要把这些写清楚：

- 目标用户
- 请求路径
- 模型和工具选择
- 评测方式
- 失败处理
- observability
- 安全边界
- 成本假设

## 本章输出物

- 一份“本地原型 -> 云上系统”的设计草图
- 一张本地与生产差异清单
- 一套你自己的迁移判断标准

## 继续阅读

- [[../../07-Topics/Serving and Scaling|Serving and Scaling]]
- [[../../07-Topics/Disaggregated Serving 与推理数据面|Disaggregated Serving 与推理数据面]]
- [[../../07-Topics/Enterprise MLOps 与 LLMOps Vendor Tradeoffs|Enterprise MLOps 与 LLMOps Vendor Tradeoffs]]
