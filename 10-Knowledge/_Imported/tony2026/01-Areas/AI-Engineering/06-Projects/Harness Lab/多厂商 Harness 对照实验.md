---
title: 多厂商 Harness 对照实验
type: project-doc
status: learning
created: 2026-03-28
updated: 2026-03-28
---

# 多厂商 Harness 对照实验

## 对照维度

| 维度 | Codex | Claude Code | OpenClaw | Gemini CLI | Grok Agent Tools API |
| --- | --- | --- | --- | --- | --- |
| 主入口 | app / cloud / CLI | terminal | self-hosted runtime / apps | terminal + workflow | API |
| 主要动作面 | shell、computer、remote MCP | shell、MCP | typed tools、browser、exec、nodes | CLI、extensions、ADK-adjacent | search、code execution、remote MCP |
| 扩展面 | skills、apps、connectors | commands、subagents、hooks | skills、plugins、bundles、ClawHub | extensions、GEMINI.md | tool API + remote MCP |
| 自动化面 | automations、background tasks | hooks、GitHub Actions、SDK | hooks、heartbeat、cron、webhooks | GitHub Action | server-side multi-agent |
| 最像什么 | cloud coding harness | terminal coding harness | assistant operating layer | CLI workflow bridge | API-first agent tool surface |

## 真实任务切片

### 任务 1：Repo 修复

- 读代码库
- 修一个小 bug
- 跑测试
- 解释 diff

### 任务 2：Browser / desktop 操作

- 打开网页
- 搜索信息
- 完成点击流程
- 回传结果与依据

### 任务 3：Recurring ops

- issue / CI 摘要
- 每日 brief
- webhook 或 schedule 触发的例行任务

## 记录问题

### 1. 谁的入口最顺

- 第一次上手最顺的是谁
- 第三次复用时最顺的是谁

### 2. 谁的扩展面最清楚

- 规则文件是否好理解
- skills / commands / plugins / extensions 是否成体系

### 3. 谁的自动化面最成熟

- 触发机制有没有统一心智
- 失败后是否可回放
- 有没有明显的 release gate / approval 边界

### 4. 谁最适合哪类任务

- coding
- browser task
- assistant runtime
- long-running automation
- server-side tool orchestration

## 记录输出

- setup 时间
- 首次成功率
- 失败恢复方式
- 结果投递方式
- 你愿不愿意长期把它放进团队流程

## 实验结论模板

- `我最喜欢的入口模式`：
- `我最信任的自动化模式`：
- `最适合团队长期使用的系统`：
- `最适合个人 assistant runtime 的系统`：
- `最适合云上 tool orchestration 的系统`：

## 关联

- [[项目总览|Harness Lab]]
- [[最小 Harness Lab：从 CLI 到 Browser 的学习计划]]
- [[../../07-Topics/Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI|Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI]]
- [[../../07-Topics/Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel|Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]
- [[Harness Lab 第一轮：Repo 修复、Browser 操作与 Daily Ops]]
- [[../../07-Topics/Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel|Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
- [[../../07-Topics/Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环|Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环]]
