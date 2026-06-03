---
title: ChatGPT Agent
type: system
status: learning
tags:
  - ai/system
  - ai/agent
  - ai/product
  - organization/openai
created: 2026-03-22
updated: 2026-04-03
---

# ChatGPT Agent

## 简介

`ChatGPT Agent` 可以理解成 OpenAI 在 `ChatGPT` 产品里的 agent mode。按 OpenAI Help Center 的说法，`Operator` 的能力已经并入 `ChatGPT agent mode`，它代表的是 ChatGPT 从“对话助手”继续走向“可执行任务代理”的方向。

## 为什么重要

- 它说明主流通用 assistant 产品正在把 agent 能力纳入主入口
- 它让 “chat + browse + act” 逐渐收敛到同一个产品体验里
- 它很适合作为“云端通用 agent 产品”的代表案例

## 官方定位里最值得记住的点

- `Operator` 已经并入 `ChatGPT agent mode`
- agent mode 可以访问网站、采取动作，并在需要时请求你接管
- 它属于 ChatGPT 主产品的一部分，而不是独立 runtime

## 你可以把它当成什么来理解

- `ChatGPT` 是通用 assistant 主入口
- `ChatGPT Agent` 是它的执行能力增强层

所以它不是完全独立的新系统，更像：

- ChatGPT 的 agent 化能力层
- cloud-hosted general-purpose agent experience

## 学习时重点看什么

- 它和普通 ChatGPT 对话模式的边界是什么
- 它的 agent 能力是怎么被产品化、治理和限制的
- 它为什么很适合拿来理解 `browser / computer use` 这条动作面
- 它和 `Manus` 这种更强调 autonomous completion 的产品差别在哪里
- 它和 `OpenClaw` 这种 self-hosted runtime 的差别在哪里

## 动作面特征

- `ChatGPT Agent` 更接近 cloud-hosted browser / connector style agent
- 它很适合帮助理解：什么时候 agent 通过网页和应用连接完成任务，而不是直接 shell 或自托管 runtime
- 它也说明高风险动作往往仍然需要 `take over` 或显式确认

## 它和 OpenClaw 的关键差异

- `ChatGPT Agent` 更像云端托管的 agent 产品能力
- `OpenClaw` 更像自托管的 runtime / gateway

一个更偏：

- 一体化产品体验
- OpenAI 主产品入口
- 平台侧治理

另一个更偏：

- 本地控制权
- 多渠道存在
- workspace / memory / hooks / heartbeat 级别的系统可塑性

## 它和 Claude Code 的关键差异

- `Claude Code` 更专注代码工作流
- `ChatGPT Agent` 更偏广义任务执行

## 它和 Manus 的关键差异

- `ChatGPT Agent` 更强依赖 ChatGPT 这个统一入口
- `Manus` 的产品叙事更偏“自主完成任务并交付结果”

## 相关系统

- [[ChatGPT]]
- [[Manus]]
- [[Claude Code]]
- [[OpenClaw]]
- [[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]]
- [[../../AI-Engineering/07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]]
- [[AI Agent Systems 对比：OpenClaw、ChatGPT Agent、Claude Code、Manus]]

## 论文 / 技术锚点

- [[GPT-4o System Card]]
- [[WebVoyager：Building an End-to-End Web Agent with Large Multimodal Models]]

## 官方资料

- 官方帮助文档: [ChatGPT agent](https://help.openai.com/en/articles/11752874-chatgpt-agent)
- ChatGPT 帮助中心: [ChatGPT Collection](https://help.openai.com/en/collections/3742473-chatgpt)
