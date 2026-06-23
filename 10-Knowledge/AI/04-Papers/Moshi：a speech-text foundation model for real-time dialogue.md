---
title: Moshi：a speech-text foundation model for real-time dialogue
type: paper
status: active
tags:
  - ai/paper
  - ai/voice
  - ai/realtime
aliases:
  - Moshi
authors: []
organization:
  - Kyutai
year: 2024
venue: arXiv
related_models: []
related_people: []
related_topics:
  - "[[Voice、Realtime 与语音工作流]]"
  - "[[Multimodal Models]]"
  - "[[AI Assistant]]"
source: https://arxiv.org/abs/2410.00037
created: 2026-04-03
updated: 2026-04-03
---

# Moshi：a speech-text foundation model for real-time dialogue

## 简介

`Moshi` 是最近两年最值得记住的语音锚点之一，因为它把 `full-duplex spoken dialogue` 清楚地立成了一条独立研究路线。

## 核心想法

它不再把语音助手理解成 `ASR -> text model -> TTS` 的三段式流水线，而是直接把 spoken dialogue 当成 `speech-to-speech generation` 问题来做。

## 为什么重要

- 它明确指出传统 pipeline 在延迟、情感保真和打断处理上都有限制
- 它把 `overlap`、`interruptions`、`interjections` 这些真实对话现象收进模型视野
- 它让 `realtime voice agent` 从产品直觉变成研究上可指认的主线

## 最值得记住的技术点

- 它把自身语音和用户语音建成并行流
- 它引入 `Inner Monologue`，先预测 time-aligned text token，再继续生成 audio token
- 论文给出的 latency 目标已经进入实时对话级别：理论 `160ms`、实践约 `200ms`

## 这篇论文真正改了哪条路线

- 模型路线：从 text-centric multimodal 继续走向原生 spoken model
- 系统路线：从 turn-based voice assistant 走向 full-duplex realtime dialogue
- 产品路线：把语音助手从“可说话的 chatbot”拉向“更接近真人节奏的对话系统”

## 相关主题

- [[Voice、Realtime 与语音工作流]]
- [[Multimodal Models]]
- [[AI Assistant]]

## 相关系统

- [[OpenAI Realtime API]]
- [[ChatGPT]]

## 后续可补充

- Moshi 和 GPT-4o / gpt-realtime 的对照
- full-duplex voice system 的 eval 和 safety
- realtime dialogue 为什么天然接到工具调用与 runtime 设计

## 相关

- [[GPT-4o System Card]]
- [[Qwen2-5-Omni Technical Report|Qwen2.5-Omni Technical Report]]
- [[Voice、Realtime 与语音工作流]]
