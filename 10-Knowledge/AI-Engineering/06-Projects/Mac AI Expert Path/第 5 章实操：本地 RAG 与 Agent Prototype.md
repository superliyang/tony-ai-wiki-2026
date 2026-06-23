---
title: 第 5 章实操：本地 RAG 与 Agent Prototype
status: learning
created: 2026-03-27
updated: 2026-03-27
---

# 第 5 章实操：本地 RAG 与 Agent Prototype

## 本章目标

这一章开始把模型真正装进应用里。我们不追求大而全，而是追求做出两个最小可运行系统：

- 一个本地 RAG 原型
- 一个本地 agent prototype

## 为什么这一步关键

到这里为止，你已经练过：

- runtime
- 训练
- 微调
- 评测

但这些还都是“模型层能力”。真正的系统能力，要从这里开始建立：

- 外部知识怎么接进去
- 工具怎么接进去
- 错误怎么处理
- trace 怎么记录
- 什么叫 bad cases

## Part A：本地 RAG 原型

### 最小目标

做一个本地文档问答系统，能对你自己的技术文档或笔记做问答。

### 最小组件

- 文档切分
- embedding
- 向量检索
- prompt 组装
- 本地模型回答

### 你要比较的点

- chunk 太小会不会丢信息
- chunk 太大是否影响检索质量
- embedding 选择是否明显影响结果
- retrieved context 对答案有没有真实帮助

### 输出物

- 一份小文档集
- 一组固定问题
- 一份 bad-case 集合
- 一张 `chunk / retrieval / answer quality` 观察表

## Part B：本地 Agent Prototype

### 最小目标

做一个带工具调用的本地 agent。

工具数量不需要多，先 `2` 个就够，比如：

- 文件读取
- 简单计算
- 本地搜索
- 文档检索

### 最小关注点

- agent 什么时候该调用工具
- 调错工具时如何失败
- 工具结果如何拼回上下文
- 是否需要 memory
- 什么时候需要 approval gate

### 输出物

- 一个最小 agent 脚本或服务
- 至少两条成功轨迹
- 至少三条失败轨迹
- 一份错误分类笔记

## RAG 与 Agent 共同要做的事

### 1. 保留 bad cases

这一步特别重要。你至少要保存：

- 检索错了的样本
- 回答幻觉的样本
- 工具调用错误的样本
- 规划路径走偏的样本

### 2. 加最小可观测性

不要求一上来接全套平台，但至少要能看到：

- 输入
- 中间上下文
- 检索结果
- 工具调用
- 最终输出

### 3. 写一份边界说明

你要明确这两个 prototype 的边界：

- 它们适合内部实验，不适合直接生产
- 哪些问题是内容问题
- 哪些问题是 retrieval / tool / orchestration 问题

## 这章最重要的收获

完成后，你应该能真正开始回答：

- 什么时候应该做 RAG
- 什么时候需要 agent
- 什么时候 agent 只是“复杂化”
- 什么时候 trace / eval / observability 必须补上

## 本章输出物

- 一个本地 RAG prototype
- 一个本地 agent prototype
- 一份 bad-case 集合
- 一份 RAG vs agent 适用边界总结

## 常见误区

- RAG 一跑通就觉得系统可用了
- agent 一会调工具就觉得已经智能
- 没保留失败轨迹，导致完全无法迭代
- 不区分“检索问题”和“模型问题”

## 下一步

- [[第 6 章：从 Mac 实验室到云上系统]]
- [[../../07-Topics/Mac 上的 RAG、Agent 与本地应用开发|Mac 上的 RAG、Agent 与本地应用开发]]
- [[../../07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]
