---
title: 第 4 章：微调、LoRA 与评测
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# 第 4 章：微调、LoRA 与评测

## 本章目标

理解“调模型”真正意味着什么，并建立最小可复用的微调与评测流程。

## 你要掌握的事情

- 任务定义：到底要改什么能力
- dataset curation：什么数据值得进训练集
- `LoRA` / `QLoRA` / `PEFT` 的基本思想
- pre-eval / post-eval 为什么是必需步骤
- failure analysis：为什么一次微调看起来成功、实际上却失败

## 推荐最小工作流

1. 定义一个小任务
2. 选一个够小的模型
3. 准备一个干净、可解释的数据集
4. 先做 baseline eval
5. 跑一次 LoRA / SFT
6. 再做 post-eval
7. 分析输出差异和副作用

## 你应该保存的材料

- dataset 版本
- prompt 模板
- 微调参数
- 基线评测结果
- 微调后评测结果
- 失败样例列表

## 本章输出物

- 一次完整 LoRA / SFT 实验记录
- 一份前后对比评测
- 一份失败案例分析

## 常见误区

- 没做 baseline
- 数据集太脏或目标太混乱
- 只看几条样例就宣布“效果很好”
- 不分析副作用，比如风格漂移、幻觉变化、工具调用退化

## 继续阅读

- [[第 5 章：RAG、Agent 与本地应用开发]]
- [[../../07-Topics/Mac 本地微调：LoRA、QLoRA 与 MLX-LM|Mac 本地微调：LoRA、QLoRA 与 MLX-LM]]
- [[../../07-Topics/Evaluation and Benchmarks|Evaluation and Benchmarks]]
- [[../../07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]
