---
title: Voice、Realtime 与语音工作流
type: topic
status: active
tags:
  - ai/topic
  - ai/voice
  - ai/realtime
created: 2026-04-03
updated: 2026-04-03
---

# Voice、Realtime 与语音工作流

## 这个主题是什么

`Voice、Realtime 与语音工作流` 关注模型如何以低延迟方式进行听、说、打断、接工具，并把语音交互真正接入工作流。

## 为什么重要

- 语音是最自然的人机交互表面之一
- 一旦进入 `realtime`，系统设计重点就不再只是“答得对不对”，还包括延迟、打断、节奏和连续性
- 这条线会直接影响 customer support、language learning、phone agent、accessibility 和 hands-free assistant

## 最近两年这条线真正发生了什么

1. 从 `ASR -> LLM -> TTS` pipeline 走向更原生的 speech-to-speech
- [[Moshi：a speech-text foundation model for real-time dialogue]]
- [[Qwen2-5-Omni Technical Report|Qwen2.5-Omni Technical Report]]

2. 从模型能力走向 API 与系统面
- [[GPT-4o System Card]]
- [[OpenAI Realtime API]]

3. 从语音 demo 走向 production voice agent
- 工具调用
- phone / SIP 集成
- 多模态输入
- 生产化 guardrails

## 你先要抓住什么

- `voice` 不只是输入输出模态，而是交互主界面
- `realtime` 不只是流式返回，而是完整的低延迟会话系统
- 真正可用的语音 agent，必须把 `speech + timing + tool use + safety` 一起处理

## 关键问题

- 语音系统为什么容易在延迟上失败
- `full-duplex` 和普通 turn-based voice assistant 有什么差别
- 什么时候应该用端到端 speech-to-speech，什么时候仍然适合 pipeline
- voice agent 为什么天然会接到 function calling、MCP、SIP 和治理问题

## 典型能力

- speech-to-speech conversation
- interruption handling
- turn-taking
- streaming transcription
- function calling in live sessions
- phone / call-center integration
- multimodal grounding during conversation

## 最近两年最值得记住的论文 / 系统锚点

- [[GPT-4o System Card]]
- [[Moshi：a speech-text foundation model for real-time dialogue]]
- [[Qwen2-5-Omni Technical Report|Qwen2.5-Omni Technical Report]]
- [[OpenAI Realtime API]]
- [[../11-Recent-Supplements/2024-2026 AI 新路线补线：Voice、Realtime 与语音工作流|2024-2026 AI 新路线补线：Voice、Realtime 与语音工作流]]

## 当前关联公司 / 模型

- [[OpenAI]]
- [[Qwen 系列]]
- [[GPT 系列]]
- [[ChatGPT]]
- [[OpenAI API]]

## 相关

- [[Multimodal Models]]
- [[AI Assistant]]
- [[Tool Use]]
- [[OpenAI Realtime API]]
- [[OCR 与 Document AI]]
- [[../11-Recent-Supplements/2024-2026 AI 新路线补线：Voice、Realtime 与语音工作流|2024-2026 AI 新路线补线：Voice、Realtime 与语音工作流]]
