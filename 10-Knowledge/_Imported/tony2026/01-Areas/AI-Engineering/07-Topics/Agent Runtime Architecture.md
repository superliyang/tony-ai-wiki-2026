---
title: Agent Runtime Architecture
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent-runtime
created: 2026-03-22
updated: 2026-03-28
---

# Agent Runtime Architecture

## 为什么它必须从 seed 升级成主线页

很多 agent demo 看起来已经会：

- 调工具
- 调浏览器
- 调 shell
- 跑一个 workflow

但真正一落地，问题往往不是模型够不够聪明，而是 runtime 根本不完整：

- 任务谁接住
- 状态谁保存
- 工具谁执行
- 权限谁约束
- 失败谁恢复
- 结果谁交付

所以 `Agent Runtime` 不是模型外面的一层薄包装，而是把 agent 从“会回答”推进到“能持续工作”的正式系统层。

## 用系统视角看，runtime 至少有 9 层

1. ingress：chat、API、bot、event source、scheduler
2. identity and session：用户、会话、线程、工作目录、tenant 映射
3. planner / executor：任务分解、执行循环、停止条件
4. tool bus：MCP、shell、browser、SDK tools、remote nodes
5. state and memory：request state、session state、durable memory、artifacts
6. execution environments：本地、托管容器、沙箱、worktree、远程 node
7. control plane：policy、permission、approval、quota、budget
8. observability：trace、events、artifacts、audit、regression signals
9. lifecycle：background execution、retry、cancel、handoff、promotion

## 一个成熟 runtime 的最小闭环

最小可用闭环通常是：

1. 收到任务
2. 创建或恢复 session
3. 决定执行模式：同步 / 后台 / 多 agent
4. 选择动作面：CLI / browser / MCP / SDK
5. 运行工具并记录中间状态
6. 根据结果继续计划、停下、请求审批或回退
7. 交付最终结果与 artifacts
8. 把关键事件写进 trace / audit / memory

如果缺其中任意一层，系统就容易退化成一次性脚本或易碎 demo。

## runtime 和 assistant、workflow、harness 的边界

### runtime 不是 assistant UI

assistant 更关心交互体验；runtime 更关心行为是否连续、可控、可恢复。

### runtime 不是单纯 workflow engine

workflow engine 偏“固定流程执行”；agent runtime 需要容纳：

- 动态计划
- 工具选择
- 错误恢复
- 人工接管
- 多任务并发

### runtime 也不等于 harness

harness 更像围绕 runtime 的完整工作台，包括：

- repo / environment
- review gates
- regression loops
- automation plane

runtime 是 harness 的核心执行内核之一。

## 现在业内几条典型实现路线

### `OpenAI Responses + tools`

这一线很强调：

- `background` 异步执行
- `computer use`
- `shell`
- remote MCP

更像“以统一 API 和工具面为中心”的 runtime 路线。

### `Claude Code`

这一线很强调：

- permissions
- subagents
- hooks
- memory files
- repo-local execution

更像“以 coding workflow 和受控执行”为中心的 runtime 路线。

### `OpenClaw`

这一线很强调：

- gateway
- channels
- nodes
- skills / plugins / automations
- node.invoke 与 companion device surfaces

更像“以长期运行、跨渠道、跨设备 control plane”为中心的 runtime 路线。

### `Google ADK`

这一线很强调：

- session / state / events
- callbacks
- artifacts
- context compaction
- evaluation

更像“以 agent framework primitives 为中心”的 runtime 路线。

## 设计 runtime 时最该问的 7 个问题

### 1. Source of truth 在哪里

是 response object、session service、event log，还是 gateway state？

### 2. 状态按什么粒度切

- request
- invocation
- session
- user
- project
- tenant

如果不切清楚，记忆和恢复会越来越乱。

### 3. 动作面如何统一

CLI、browser、MCP、channel commands、SDK tools 本质上都需要同一套：

- schema
- permission
- timeout
- cancel
- audit

### 4. 后台执行和同步执行如何共存

复杂任务不应该都走同步模式；但后台任务也不能变成不可见黑箱。

### 5. 失败恢复做到什么粒度

- tool retry
- step retry
- task resume
- human takeover
- full replay

### 6. 结果怎么交付

- 文本答案
- diff / patch
- artifact
- browser outcome
- channel push
- PR / review handoff

### 7. 运行时如何持续学习

好的 runtime 会把：

- traces
- evals
- failure modes
- human corrections
- memory updates

收进下一轮系统改进，而不是只停留在一次执行上。

## 典型失败模式

### 1. session 和 memory 混成一层

结果就是：该忘的不忘，该记的没记住。

### 2. 工具层没有统一 envelope

不同工具返回风格不一致，模型很难稳定消费结果。

### 3. 后台任务不可观察

用户把任务交出去以后，只剩“等结果”，中途完全不可见。

### 4. 安全控制贴在最外层

没有进入 runtime 主循环的 permission / approval，最后都会被绕过或遗漏。

### 5. trace 很多，但没有恢复路径

能看到日志不等于能接管、继续、修复。

## 学这一页最该形成的判断力

### 判断 1：这个产品到底有没有 runtime

如果系统不能：

- 保存状态
- 恢复任务
- 管权限
- 管动作面

那它更像 tool-using chat，而不是 runtime。

### 判断 2：运行时瓶颈在模型，还是在系统层

很多失败不是模型不行，而是：

- session 设计差
- 工具 envelope 差
- background / approval 机制缺失
- trace 和 handoff 做得差

### 判断 3：当前 runtime 更像哪一派

- API-centric
- coding-centric
- channel-centric
- framework-centric

不同路线会决定后续系统怎么长。

## 推荐怎么连着读

1. [[Tool Calling and Action Execution]]
2. [[Session and Memory Design]]
3. [[Background Agents]]
4. [[Delegation and Task-Oriented Agents]]
5. [[Multi-Agent Coding Workflow]]
6. [[Computer Use Runtime and Safety]]
7. [[Harness Engineering]]

## 相关主题

- [[Tool Calling and Action Execution]]
- [[Session and Memory Design]]
- [[Background Agents]]
- [[Delegation and Task-Oriented Agents]]
- [[Multi-Agent Coding Workflow]]
- [[Computer Use Runtime and Safety]]
- [[Harness Engineering]]
- [[Agent Security、Sandbox 与 Approval Architecture]]

## 资料

- [OpenAI Background mode](https://developers.openai.com/api/docs/guides/background)
- [OpenAI Computer use](https://developers.openai.com/api/docs/guides/tools-computer-use)
- [OpenAI Shell tool](https://developers.openai.com/api/docs/guides/tools-shell)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code memory](https://code.claude.com/docs/en/memory)
- [Claude Code permissions](https://code.claude.com/docs/en/team)
- [OpenClaw Gateway Architecture](https://docs.openclaw.ai/concepts/architecture)
- [OpenClaw Plugin Internals](https://docs.openclaw.ai/plugins/architecture)
- [ADK Technical Overview](https://google.github.io/adk-docs/get-started/about/)
- [ADK State](https://google.github.io/adk-docs/sessions/state/)
- [ADK Context Compaction](https://google.github.io/adk-docs/context/compaction/)
- [ADK Artifacts](https://google.github.io/adk-docs/artifacts/)
