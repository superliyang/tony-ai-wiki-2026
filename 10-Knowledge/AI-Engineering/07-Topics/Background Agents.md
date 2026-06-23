---
title: Background Agents
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent-ops
  - ai/coding-agent
created: 2026-03-22
updated: 2026-03-28
---

# Background Agents

## 为什么它不是“把请求放进队列”那么简单

`Background Agent` 标志着 agent 从“同步对话助手”走向“异步任务执行系统”。

很多 coding agent、research agent、ops agent 的真正价值，不在于当面回答得多快，而在于能否：

- 在用户不盯着的时候持续推进
- 把中间状态保住
- 在结束时稳定交付结果

所以背景执行不只是调度问题，而是 runtime、permissions、handoff、cost control 一起发生变化。

## 一个后台任务真正需要哪些能力

至少要有 6 件事：

1. detached execution：脱离当前对话继续跑
2. isolated environment：本地、云端、沙箱、worktree 或 node 环境隔离
3. progress reporting：能报告状态，而不是黑盒执行
4. resumability：失败或中断后可恢复
5. controls：timeout、budget、approval、network policy
6. handoff：结果能回到 review / chat / artifact / PR 流程

## 同步 agent 和 background agent 的本质差别

### 同步 agent 更像

- 你问我答
- 一轮轮对话
- 用户一直在回路中

### background agent 更像

- 你把任务正式委托出去
- 系统在后台推进
- 中途以事件、日志、产物和审批回到你面前

所以产品体验从 `conversation` 变成了 `delegation + progress + review`。

## 常见实现路线

### API background mode

典型代表是 `OpenAI Responses background mode`。

这条路线的特点是：

- 任务异步启动
- 状态可轮询
- 可取消
- 可与流式事件结合

优点：

- 很适合长 reasoning、长报告、离线分析
- 客户端掉线也不影响后台执行

代价：

- 默认不是强 workflow 系统
- 环境、工具、审批和 artifact 仍需你自己补齐

### coding / review background workers

典型代表是 `Codex` 一类后台 worker 与 `Claude Code` 的 async hooks / subagents 组合思路。

这条路线的特点是：

- 任务边界更工程化
- 更容易和 repo、review、diff、tests 结合
- 适合 implementation / review / maintenance 子任务

### channel / gateway background automation

典型代表是 `OpenClaw` 的 gateway + nodes + automations。

这条路线的特点是：

- 长期在线
- 多渠道可触发
- 结果可回到消息渠道或 node surfaces
- 更像 personal / team runtime

## 真正高频的设计问题

### 1. 后台任务运行在哪

- 本地：权限强、环境真实，但安全和可携带性差
- 托管容器：更可控，但环境准备成本更高
- worktree / sandbox：适合 coding tasks
- remote node：适合跨设备动作

### 2. 任务怎么被观察

如果只有最终结果，没有：

- 阶段性状态
- 关键事件
- 产物预览
- 失败原因

用户会很快失去信任。

### 3. 如何避免“后台偷偷花钱”

后台任务一旦没人盯，就更需要：

- budget
- timeouts
- max steps
- rate limits
- cancel / stop hooks

### 4. 何时必须让用户回到回路里

高风险动作通常应该在以下时刻回人：

- 发出真实外部动作前
- 修改关键配置前
- 访问高敏感数据前
- 大范围写代码或大规模删除前

## 后台 agent 最容易失败的地方

### 1. 黑盒化

用户把任务交出去后只知道“还在跑”，不知道为什么慢、做到哪一步、是否已经卡住。

### 2. 环境漂移

本地和云端、不同 worktree、不同 node 环境不一致，导致结果不可复现。

### 3. 结果无法自然回流

任务虽然跑完了，但无法自然回到：

- PR
- 代码审查
- 会话上下文
- artifact store

### 4. 后台任务和记忆系统没分开

一次任务的临时状态被误写成长久记忆，后面会污染别的任务。

## 学这一页最该形成的判断力

### 判断 1：这个任务真的适合后台化吗

适合后台化的通常是：

- 时间长
- 中途不需要高频交互
- 可以清楚定义交付物
- 可允许阶段性汇报而非每步确认

### 判断 2：后台 agent 的真正价值是什么

不是“异步”本身，而是：

- 环境隔离
- 状态持续
- 中途可观察
- 结果可接管

### 判断 3：后台系统该怎么和主工作流连接

好的 background agent 最终一定要接到：

- review
- approval
- merge / deploy
- channel notify
- trace / eval

## 推荐怎么连着读

1. [[Delegation and Task-Oriented Agents]]
2. [[Session and Memory Design]]
3. [[Multi-Agent Coding Workflow]]
4. [[Long-Running Agent Operations]]
5. [[Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
6. [[Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环]]

## 相关主题

- [[Agent Runtime Architecture]]
- [[Delegation and Task-Oriented Agents]]
- [[Session and Memory Design]]
- [[Multi-Agent Coding Workflow]]
- [[Long-Running Agent Operations]]
- [[Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
- [[Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环]]

## 资料

- [OpenAI Background mode](https://developers.openai.com/api/docs/guides/background)
- [Claude Code hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [OpenClaw Gateway Architecture](https://docs.openclaw.ai/concepts/architecture)
- [OpenClaw Nodes](https://docs.openclaw.ai/nodes)
