---
title: 最小 Harness Lab：从 CLI 到 Browser 的学习计划
type: project-doc
status: learning
created: 2026-03-28
updated: 2026-03-28
---

# 最小 Harness Lab：从 CLI 到 Browser 的学习计划

## 目标

用最小成本亲手体验 4 类 harness：

- terminal-first
- desktop / browser-first
- cloud-first
- channel-first

## 实验 1：Terminal-first

观察对象：

- `Claude Code`
- `Gemini CLI`
- `Codex CLI`

观察问题：

- 项目级规则文件怎样影响行为
- shell 执行、diff、review loop 哪个最顺
- hooks / subagents / extensions 的安装和调用心智如何

## 实验 2：Desktop / Browser-first

观察对象：

- `ChatGPT agent`
- OpenAI / Anthropic `computer use`
- `OpenClaw` 的 app / chat surface

观察问题：

- 人工接管在哪一步最自然
- GUI 任务和 browser 任务哪类更适合 computer use
- replay、approval、screenshot memory 是否足够清楚

## 实验 3：Cloud-first

观察对象：

- `Codex app`
- `App Server` 风格 runtime
- `Grok Agent Tools API`

观察问题：

- 后台任务是怎样排队、继续和回放的
- cloud task 相比本地 CLI 有什么体验差异
- server-side tools 是否让系统更容易治理

## 实验 4：Automation plane

观察对象：

- `OpenClaw hooks / cron / heartbeat`
- `Claude Code GitHub Actions`
- `run-gemini-cli`
- `Codex automations`

观察问题：

- 触发方式是谁控制的
- 失败后如何回看和重跑
- 哪一种最适合长期运转，而不只是演示

## 先读这一页

- [[../../07-Topics/Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel|Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]

## 你要记下来的结果

- 最顺的入口模式
- 最自然的自动化模式
- 最适合做 coding harness 的系统
- 最适合做 assistant runtime 的系统
- 最适合做 server-side tool harness 的系统

## 关联

- [[多厂商 Harness 对照实验]]
- [[Harness Lab 第一轮：Repo 修复、Browser 操作与 Daily Ops]]
- [[项目总览|Harness Lab]]
- [[../../07-Topics/Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel|Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
- [[../../07-Topics/Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环|Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环]]
