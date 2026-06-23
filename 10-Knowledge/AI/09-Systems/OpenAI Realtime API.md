---
title: OpenAI Realtime API
type: system
status: active
tags:
  - ai/platform
  - ai/realtime
  - ai/voice
  - organization/openai
aliases: []
organization: "[[OpenAI]]"
modality:
  - api
  - audio
  - realtime
family: GPT
related_papers:
  - "[[GPT-4o System Card]]"
related_people:
  - "[[Sam Altman]]"
created: 2026-04-03
updated: 2026-04-03
---

# OpenAI Realtime API

## 简介

`OpenAI Realtime API` 是 OpenAI 把低延迟语音交互、实时多模态会话和工具调用收成开发者系统面的关键接口。

## 为什么重要

- 它把 `voice / realtime` 从产品能力推进成开发者可集成的系统能力
- 它说明 production voice agent 已经不再只是 demo，而是可以接 `tool calling`、`MCP`、`image input` 和 `SIP phone calling`
- 它把 OpenAI 的多模态路线进一步推进成 `assistant -> platform -> production agent` 这条链

## 官方时间线里最值得记住的点

- `2024-10-01`：OpenAI 首次公开 `Realtime API` beta，把低延迟 speech-to-speech 和实时会话正式开放给付费开发者
- `2025-08-28`：OpenAI 宣布 Realtime API `GA`，同时加入 `remote MCP server support`、`image input` 和 `SIP phone calling`

## 你可以把它当成什么来理解

- `ChatGPT` 里的 Advanced Voice 更像产品表面
- `OpenAI API` 是平台主入口
- `OpenAI Realtime API` 则是语音和实时交互这条线的专门系统表面

所以它不是独立于 OpenAI API 的另一家公司路线，而是 OpenAI 平台化的一次再分层。

## 学习时重点看什么

- 它为什么比传统 `ASR -> LLM -> TTS` pipeline 更适合低延迟对话
- 为什么 `persistent session`、`interruptions` 和 `function calling` 是实时语音系统的关键能力
- 为什么 `MCP`、`SIP` 和 image input 会让 voice agent 更像真正的工作流入口

## 这个系统为什么有代表性

- 它把 realtime 从“模态特性”提升成 `runtime / session / tool orchestration` 问题
- 它说明生产化语音代理需要的不只是语音模型，还要有工具接入、会话控制和治理边界
- 它很适合拿来理解 voice agent 如何从聊天产品路线走向企业工作流路线

## 所属组织

- [[OpenAI]]

## 相关模型 / 产品

- [[GPT 系列]]
- [[ChatGPT]]
- [[OpenAI API]]

## 相关主题

- [[Voice、Realtime 与语音工作流]]
- [[Multimodal Models]]
- [[AI Assistant]]
- [[Tool Use]]

## 相关论文 / 技术报告

- [[GPT-4o System Card]]

## 资料

- [Introducing the Realtime API](https://openai.com/index/introducing-the-realtime-api/)
- [Introducing gpt-realtime and Realtime API updates for production voice agents](https://openai.com/index/introducing-gpt-realtime/)
