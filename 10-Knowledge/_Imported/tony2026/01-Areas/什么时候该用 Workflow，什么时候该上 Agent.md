---
title: 什么时候该用 Workflow，什么时候该上 Agent
type: guide
status: active
updated: 2026-04-03
---

# 什么时候该用 Workflow，什么时候该上 Agent

## 一句先判断

如果流程大体固定、分支有限、审批清楚，先用 `workflow`。

如果任务需要动态理解、临场决策、工具选择和中途纠偏，再上 `agent`。

## 最实用的判断表

| 你面对的问题 | 更适合先上什么 | 为什么 |
| --- | --- | --- |
| 步骤稳定、顺序明确、合规要求高 | `workflow` | 可审计、可审批、可回放 |
| 任务边界模糊、信息不完整、执行路径经常变化 | `agent` | 需要动态计划和策略调整 |
| 主流程稳定，但某几个节点需要灵活判断 | `workflow + agent` | workflow 管骨架，agent 管局部智能 |
| 高风险行业、证据链要求强 | `workflow` 优先 | 先把控制面立住，再让 agent 进局部节点 |
| coding / research / browser task 这类开放任务 | `agent` 优先 | 任务天然不是固定脚本 |

## 什么时候不要急着上 Agent

- 你现在连标准作业流程都还没讲清楚
- 真正要解决的是审批、责任边界和 handoff，不是智能不足
- 每一步都必须稳定、可解释、可追责
- 团队还没有 eval、回滚、review 机制

这时候先把 `workflow` 做清楚，通常比“先上一个看起来更聪明的 agent”更稳。

## 什么时候 workflow 已经不够了

- 同一个任务每次输入都不一样
- 需要去网页、文档、代码库、工具里边看边做
- 中途经常要根据结果重排下一步
- 固定规则开始写成一坨 if-else
- 你发现团队真正缺的是“动态执行能力”，不是流程图

## 一个更稳的组合打法

### 1. 先 workflow，后 agent

适合：

- 企业后台流程
- 高信任行业
- 需要先把审批、证据和交付面立住

做法：

- workflow 先管主流程
- agent 只进入少数高价值节点

### 2. 先 agent，后 workflow

适合：

- research
- coding
- browser automation
- internal knowledge work

做法：

- 先验证 agent 真能做成任务
- 再把高频路径 workflow 化和门禁化

### 3. workflow 管骨架，agent 管局部动态节点

这是很多成熟系统最后的形态。

最常见的拆法是：

- workflow 管入口、审批、handoff、交付
- agent 管研究、生成、检索、诊断、局部执行

## 最常见的 4 个误区

### 误区 1：把 workflow 当成“落后的东西”

不是。

很多真正生产可用的 AI 系统，恰恰是因为 workflow 先把控制面搭好了。

### 误区 2：上了 agent 就自然更高级

不是。

很多时候只是让系统变得更难解释、更难评测。

### 误区 3：workflow 和 agent 二选一

很多真实系统更像：

- workflow for control
- agent for adaptation

### 误区 4：流程固定就永远不需要 agent

也不是。

流程固定的系统里，仍然可能有少量高价值节点很适合 agent。

## 读完这页后你应该能自己回答

- 你当前问题更像流程问题，还是动态执行问题
- 是该先画 workflow，还是该先做 agent prototype
- 哪些节点值得 agent 化，哪些节点必须留在 workflow 里

## 推荐继续往下读

1. [[AI 问题导航|AI 问题导航]]
2. [[AI-Engineering/07-Topics/Agent、Workflow、Runtime 与 Harness：边界与组合关系|Agent、Workflow、Runtime 与 Harness：边界与组合关系]]
3. [[AI-Applications/03-Workflows/Research Agent Workflow|Research Agent Workflow]]
4. [[AI-Applications/03-Workflows/Coding Agent Workflow|Coding Agent Workflow]]
5. [[AI-Applications/03-Workflows/工作流索引|工作流索引]]
6. [[AI-Engineering/07-Topics/Planning Loops and State Machines|Planning Loops and State Machines]]
7. [[AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]

## 关联

- [[AI 决策导航|AI 决策导航]]
- [[AI-Engineering/07-Topics/Agent、Workflow、Runtime 与 Harness：边界与组合关系|Agent、Workflow、Runtime 与 Harness：边界与组合关系]]
- [[AI-Applications/03-Workflows/工作流索引|工作流索引]]
