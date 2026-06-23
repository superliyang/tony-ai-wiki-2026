---
title: Prompt 到 Context：任务表达、工作集与失败诊断
type: topic
status: learning
tags:
  - ai/engineering
  - ai/prompt
  - ai/context
created: 2026-04-03
updated: 2026-04-03
---

# Prompt 到 Context：任务表达、工作集与失败诊断

## 这页回答什么

很多 agent 失败都被粗暴归因为“模型不行”。

但工程上更常见的情况是：

- `prompt` 没把任务表达清楚
- `context` 没把工作集装对
- 或两者同时有问题

## Prompt 负责什么

`prompt` 负责：

- instruction
- role
- priority
- output format
- immediate boundaries

典型失败：

- 任务描述含混
- 优先级冲突
- 输出结构不稳定
- 安全边界没写清

## Context 负责什么

`context` 负责：

- 哪些文件被看到
- 哪些历史被保留
- 哪些 memory 被召回
- 哪些 tool result 被注入
- 哪些信息应该被裁剪

典型失败：

- 关键文件缺失
- 历史过长导致噪声
- 检索内容进错位置
- 旧 memory 污染当前任务

## 一个实用诊断顺序

当结果不好时，按这个顺序排：

1. 任务有没有说清楚
2. 输出目标有没有定义清楚
3. 模型有没有看到关键文件/状态
4. 不该出现的旧信息有没有被带进来
5. tool returns 有没有进入下一轮推理

## 为什么这条线要先于 harness

如果 `prompt/context` 没稳住，就很容易把后面问题都误诊成：

- tool 问题
- runtime 问题
- harness 问题

实际上很多系统是先在最内层就开始漏了。

## 推荐继续读

- [[../../AI-Learning/06-Topics/提示词工程|提示词工程]]
- [[../../AI-Learning/06-Topics/上下文工程|上下文工程]]
- [[记忆架构：State、Memory、Artifact 与 Context]]
- [[Prompt、Context、Tools、CLI、Skills、Plugins 与 Harness 的工程分层]]
