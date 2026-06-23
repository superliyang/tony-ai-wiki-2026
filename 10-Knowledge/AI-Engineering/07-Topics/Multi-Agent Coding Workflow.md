---
title: Multi-Agent Coding Workflow
type: topic
status: learning
tags:
  - ai/engineering
  - ai/coding-agent
  - ai/workflow
created: 2026-03-22
updated: 2026-03-28
---

# Multi-Agent Coding Workflow

## 为什么多 agent 不是“并行多开窗口”

单个 coding agent 已经能提高效率，但真正进入团队工作流后，问题会变成：

- 一个任务如何拆成多个可并行子任务
- 多个 agent 如何避免改到同一片区域
- 每个 agent 的产物如何汇合到 review / CI / merge 流程

所以多 agent workflow 的难点不在“能否并行”，而在：

- 写集隔离
- 假设同步
- 结果聚合
- 失败恢复
- ownership 清晰

## 最常见的角色分工

- implementer agent：负责改代码
- reviewer agent：负责查 bug、提测试建议
- investigator agent：负责读代码、查依赖、做根因分析
- maintainer agent：负责升级依赖、修文档、批量修改
- integrator agent：负责合并结果、协调冲突、整理 final patch

## 多 agent 真正高风险的地方

### 1. scope overlap

两个 agent 改同一块逻辑，冲突只是表面，更大的问题是结论可能互相矛盾。

### 2. hidden dependency

看起来可拆，实际上共享底层类型、schema、接口或测试基线。

### 3. assumption drift

每个 agent 根据不同上下文做了不同假设，最后很难汇合。

### 4. review debt

并行度上去以后，最后 review 成本反而爆炸。

## 一个更稳的多 agent 拆法

### 1. 按写集切

优先切成不同目录、模块、文件集，而不是只按“功能名称”切。

### 2. 明确接口先行

先定义：

- 输入输出
- schema
- shared contracts
- 不可变约束

### 3. 结果不要直接进主线

每个 agent 的产物先进入 review / test / integration 层。

### 4. 用 reviewer 或 integrator 统一收口

如果没有集中收口角色，多 agent 很容易做成一堆局部最优 patch。

## 什么时候适合多 agent

- 代码库较大，存在清晰模块边界
- 任务可拆成互相独立的写集
- 有明确测试和 review 机制
- 结果可以异步汇总

## 什么时候不适合多 agent

- 需求还没定清楚
- 重构核心共享抽象
- 所有改动都在同一文件 / 同一模块
- 集成成本远高于并行带来的收益

## 学这一页最该形成的判断力

### 判断 1：任务是不是“可并行”，还是只是“看上去能拆”

### 判断 2：当前系统有没有足够的 integration layer

### 判断 3：并行带来的收益，是否真的大于 review / merge / context 成本

## 推荐怎么连着读

1. [[Delegation and Task-Oriented Agents]]
2. [[Background Agents]]
3. [[Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]
4. [[Agent Runtime Architecture]]

## 相关主题

- [[Delegation and Task-Oriented Agents]]
- [[Background Agents]]
- [[Agent Runtime Architecture]]
- [[Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]
- [[Eval Harness 与 Regression Suites]]

## 资料

- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code permissions](https://code.claude.com/docs/en/team)
