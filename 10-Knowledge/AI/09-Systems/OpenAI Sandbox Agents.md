---
title: OpenAI Sandbox Agents
type: system
status: active
tags:
  - ai/system
  - ai/agent
  - organization/openai
created: 2026-04-29
updated: 2026-04-29
organization: "[[OpenAI]]"
---

# OpenAI Sandbox Agents

## 定位

`OpenAI Sandbox Agents` 不是一个单独聊天产品，而是 OpenAI Agents SDK / API 侧围绕 sandbox、shell、文件系统和执行环境形成的 agent runtime 能力面。

在知识拓扑里，它应该接在：

> [[OpenAI API]] -> agent tools -> sandbox / shell / filesystem -> [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]] -> [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]。

## 为什么重要

- 它说明 agent 竞争点正在从 `tool calling` 转向 `safe execution`
- 它把 shell、filesystem、network、artifact、approval、credential boundary 这些“脏活”推到架构中心
- 它让 [[../09-Systems/Codex|Codex]]、[[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]] 和 [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]] 可以用同一套 runtime 语言解释

## 两层架构

### 1. Harness control plane

负责：

- user intent
- task state
- approvals
- policy
- tool routing
- logs / trace
- artifact review

### 2. Sandbox execution plane

负责：

- shell command
- filesystem mutation
- package install
- network access
- generated artifacts
- temporary secrets boundary

这两层不能混在一起。混在一起后，agent 就很难被审计、回滚和限制权限。

## 学习时重点看什么

1. sandbox 的生命周期：创建、执行、产物、销毁
2. shell tool 的权限边界：命令、网络、文件、环境变量
3. approval gate 放在 harness 侧还是 sandbox 侧
4. artifact 如何从执行环境回到用户可审查界面
5. eval 如何覆盖实际执行行为，而不是只覆盖模型输出

## 典型风险

- prompt injection 诱导 shell 执行危险命令
- agent 误读文件边界，修改不该修改的内容
- 网络访问泄露 token 或私有数据
- 产物没有审计链，导致错误难复盘
- 自动化任务缺少 human approval，导致小错放大

## 相关模型

- [[../03-Models/GPT-5-5|GPT-5.5]]
- [[../03-Models/GPT 系列|GPT 系列]]

## 相关系统

- [[OpenAI API]]
- [[Codex]]
- [[ChatGPT Agent]]

## 相关主题

- [[../06-Topics/Agent|Agent]]
- [[../06-Topics/Tool Use|Tool Use]]
- [[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]
- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]

## 相关补线

- [[../11-Recent-Supplements/2026-04-07 至 2026-04-29 AI 拓扑补线：Frontier Work Models、Sandbox Agents 与 Enterprise Model Lifecycle|2026-04-07 至 2026-04-29 AI 拓扑补线]]

## 官方资料

- [OpenAI Platform: Agents sandboxes](https://developers.openai.com/api/docs/guides/agents/sandboxes)
- [OpenAI Platform: Shell tool](https://developers.openai.com/api/docs/guides/tools-shell)
