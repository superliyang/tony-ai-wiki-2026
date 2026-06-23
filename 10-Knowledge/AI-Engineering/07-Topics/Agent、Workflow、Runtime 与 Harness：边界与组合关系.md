---
title: Agent、Workflow、Runtime 与 Harness：边界与组合关系
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/runtime
  - ai/harness
  - ai/comparison
created: 2026-04-03
updated: 2026-04-03
---

# Agent、Workflow、Runtime 与 Harness：边界与组合关系

## 为什么这 4 个词必须放在一起看

现在很多 AI 讨论一上来就说：

- 我们要做一个 agent
- 我们想接一个 workflow
- 我们需要一个 runtime
- 我们还要有 harness

但如果这 4 个词不拆开，最后很容易出现 3 类混乱：

- 把 `agent` 当成整个系统
- 把 `workflow` 当成 runtime
- 把 `runtime` 当成 harness

这页要解决的不是术语洁癖，而是工程判断。

## 一张先抓住差异的表

| 概念 | 它最核心在回答什么 | 最像什么 | 最适合什么时候先做 | 最容易被误解成什么 |
| --- | --- | --- | --- | --- |
| `Agent` | 任务如何被动态理解、分解、选择动作 | 会思考和决策的执行单元 | 任务不完全固定、需要推理和选择时 | 整个产品或整套平台 |
| `Workflow` | 一组步骤如何被稳定串起来 | 显式流程图或状态流 | 流程稳定、分支有限、合规要求高时 | 真正的 agent intelligence |
| `Runtime` | 任务如何被接住、执行、恢复、交付 | 执行内核 | 系统已经开始接工具、状态、权限、后台任务时 | 只是一层 API 包装 |
| `Harness` | agent 在什么工作台里工作、扩展、被治理 | 完整工作环境 | 进入团队协作、长期运行、评测和回滚阶段时 | “很多 feature 的大合集” |

## 更实用的边界理解

### 1. Agent

`Agent` 是能力单元，不是全系统。

它主要负责：

- 任务理解
- 动态计划
- 工具选择
- 根据反馈调整下一步

它最强的时候，是任务还不完全固定、需要边看边做、边做边纠偏。

### 2. Workflow

`Workflow` 是流程单元，不是智能本体。

它主要负责：

- 固定顺序
- 显式分支
- 规则化 handoff
- 稳定的审计与审批

它最强的时候，是流程稳定、风险高、要可追责。

### 3. Runtime

`Runtime` 是执行系统，不是“会思考”的那一层。

它主要负责：

- session / state
- tool bus
- approval / permission
- background execution
- retry / resume / cancel
- artifact / audit

没有 runtime，很多 agent 都只是会调几个工具的 demo。

### 4. Harness

`Harness` 是工作台，不只是 runtime 的别名。

它主要把这些东西一起收起来：

- task environment
- action surfaces
- extension surfaces
- control plane
- automation plane
- feedback / release gate

所以 `harness` 关注的是：这个系统怎样被真正拿来工作、扩展、治理和回滚。

## 这 4 层在真实系统里通常怎么组合

### 组合 1：Workflow + Agent

适合：

- 有主流程，但中间某些节点需要 agent 自由判断
- 想把灵活性限定在几个受控点里

典型理解：

- workflow 管主骨架
- agent 管局部动态决策

### 组合 2：Agent + Runtime

适合：

- 已经开始接 shell、browser、MCP、SDK tools
- 需要 state、memory、approval、artifact

典型理解：

- agent 决定怎么做
- runtime 负责把它做成可持续执行的系统

### 组合 3：Runtime + Harness

适合：

- 团队协作
- coding / review / eval / rollback
- background jobs / automations
- 多入口工作台

典型理解：

- runtime 是内核
- harness 是外层工作环境与治理面

### 组合 4：Workflow + Agent + Runtime + Harness

这是比较完整的产品化形态。

最常见于：

- coding agent
- enterprise assistant runtime
- high-trust workflow systems

## 最常见的 4 个误区

### 误区 1：有 workflow 就等于有 runtime

不是。

workflow 只说明步骤怎么串，runtime 还要解决：

- 谁来执行
- 状态怎么存
- 失败怎么恢复
- 权限怎么控

### 误区 2：能调 tools 就叫 runtime

不是。

tool use 只是 runtime 的一部分。

### 误区 3：harness 只是“命令行 + 一堆工具”

不是。

harness 更像受控工作台，重点在：

- 环境
- 扩展
- 自动化
- 反馈
- 治理

### 误区 4：agent 越多越高级

不是。

很多时候，问题不是“要不要多 agent”，而是：

- 单 agent + workflow 是否已经足够
- runtime 是否稳定
- harness 是否支持审计、评测和回滚

## 如果你只想抓住一句判断

- `Agent` 让系统会动态做事
- `Workflow` 让流程稳定可控
- `Runtime` 让行为真正能持续执行
- `Harness` 让整套系统进入可工作、可扩展、可治理状态

## 推荐怎么继续读

1. [[Harness Engineering]]
2. [[Agent Runtime Architecture]]
3. [[Prompt、Context、Tools、CLI、Skills、Plugins 与 Harness 的工程分层]]
4. [[Planning Loops and State Machines]]
5. [[Tool Gateway、MCP Servers 与 SDK Tools]]
6. [[Agent Security、Sandbox 与 Approval Architecture]]
7. [[../../AI-Applications/05-Topics/Agent Productization|Agent Productization]]

## 关联

- [[Harness Engineering]]
- [[Agent Runtime Architecture]]
- [[Planning Loops and State Machines]]
- [[Tool Calling and Action Execution]]
- [[Tool Gateway、MCP Servers 与 SDK Tools]]
- [[Agent Security、Sandbox 与 Approval Architecture]]
- [[../../AI-Learning/06-Topics/从提示词到 Harness：Agent 能力的渐进式主线|从提示词到 Harness：Agent 能力的渐进式主线]]
