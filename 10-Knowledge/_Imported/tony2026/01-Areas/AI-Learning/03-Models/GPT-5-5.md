---
title: GPT-5.5
type: model
status: active
tags:
  - ai/model
  - organization/openai
created: 2026-04-29
updated: 2026-04-29
organization: "[[OpenAI]]"
family: GPT
modality:
  - text
  - multimodal
  - computer-use
---

# GPT-5.5

## 定位

`GPT-5.5` 是 OpenAI 在 `2026-04` 推出的 frontier work model。

在当前知识拓扑里，它不应该只被理解成“GPT-5.4 之后的又一个旗舰”，而应该被放进这条线：

> [[GPT 系列]] -> frontier work model -> [[../09-Systems/OpenAI API|OpenAI API]] / [[../09-Systems/Codex|Codex]] -> [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]] -> task-level eval。

## 为什么重要

- 它继续把 OpenAI 的模型路线推向 `coding / computer use / knowledge work / science / long-horizon tasks`
- 它强化了 [[../06-Topics/Reasoning Models|Reasoning Models]]、[[../06-Topics/Coding Agents|Coding Agents]] 和 [[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]] 的交叉区域
- 它让模型评估从“会不会回答”更明显地转向“能不能完成工作”

## 学习时重点看什么

1. 它如何服务高强度 coding 和 knowledge work
2. 它和 [[../09-Systems/Codex|Codex]]、[[../09-Systems/OpenAI Sandbox Agents|OpenAI Sandbox Agents]] 的 runtime 关系
3. 它是否改变 OpenAI 模型层级：日常模型、低延迟模型、coding 模型、frontier work model
4. 它如何倒逼 [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]] 变成必要工程资产

## 判断框架

看 `GPT-5.5` 时，优先问四个问题：

- 它解决的是真实工作负载，还是聊天体验？
- 它依赖哪些 action surface：tool、browser、shell、computer use、remote MCP？
- 它是否需要 sandbox / approval / artifact / audit 这类 harness 能力才能安全释放？
- 它的升级价值能否被任务级 eval 证明？

## 相关系统

- [[../09-Systems/OpenAI API|OpenAI API]]
- [[../09-Systems/Codex|Codex]]
- [[../09-Systems/OpenAI Sandbox Agents|OpenAI Sandbox Agents]]
- [[../09-Systems/ChatGPT|ChatGPT]]

## 相关主题

- [[GPT 系列]]
- [[../06-Topics/Reasoning Models|Reasoning Models]]
- [[../06-Topics/Coding Agents|Coding Agents]]
- [[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]

## 相关补线

- [[../11-Recent-Supplements/2026-04-07 至 2026-04-29 AI 拓扑补线：Frontier Work Models、Sandbox Agents 与 Enterprise Model Lifecycle|2026-04-07 至 2026-04-29 AI 拓扑补线]]
- [[../11-Recent-Supplements/截至 2026-04-07 的 2026 新模型刷新|截至 2026-04-07 的 2026 新模型刷新]]

## 官方资料

- [OpenAI: Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [OpenAI Platform: GPT-5.5](https://platform.openai.com/docs/models/gpt-5.5)
