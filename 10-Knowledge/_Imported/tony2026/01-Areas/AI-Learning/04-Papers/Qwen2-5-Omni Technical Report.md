---
title: Qwen2-5-Omni Technical Report
type: paper
status: active
tags:
  - ai/paper
  - ai/multimodal
  - ai/voice
aliases:
  - Qwen2.5-Omni Technical Report
authors: []
organization:
  - Alibaba Cloud
year: 2025
venue: arXiv
related_models:
  - "[[Qwen 系列]]"
related_people: []
related_topics:
  - "[[Multimodal Models]]"
  - "[[Voice、Realtime 与语音工作流]]"
source: https://arxiv.org/abs/2503.20215
created: 2026-04-03
updated: 2026-04-03
---

# Qwen2-5-Omni Technical Report

## 简介

`Qwen2.5-Omni Technical Report` 是 open multimodal 路线里很值得记住的一份技术锚点，因为它把 `text + image + audio + video + streaming speech` 收成了一个端到端 omni model 叙事。

## 核心想法

它的关键不是“支持更多模态”这么简单，而是要让不同模态能够以 streaming 方式一起进来，并且能够同时输出文本和自然语音。

## 为什么重要

- 它说明 open multimodal 路线也开始认真补 `voice / realtime` 这一面
- 它把语音生成、语音理解、视觉输入和文本推理收进同一套系统里
- 它让 `omni model` 不再只是 OpenAI 的路线表达

## 最值得记住的技术点

- 它提出 `Thinker-Talker` 架构：`Thinker` 负责文本生成，`Talker` 负责语音 token 生成
- 为了支持 streaming multimodal input，它对音频和视觉编码都采用 block-wise 处理
- 为了同步视频和音频时间戳，它提出 `TMRoPE`

## 这篇报告真正改了哪条路线

- 模型路线：把 Qwen 从 open text / VL 路线推进到 omni multimodal
- 系统路线：把 multimodal assistant 拉向 streaming speech + end-to-end response
- 产品路线：让开放生态也有可能形成更完整的 voice-first assistant / realtime interaction 方案

## 相关模型 / 系统

- [[Qwen 系列]]
- [[Multimodal Models]]
- [[Voice、Realtime 与语音工作流]]

## 后续可补充

- Qwen2.5-Omni 和 Qwen2.5-VL 的边界
- open omni model 在产品化和部署层的真实限制
- 和 GPT-4o / gpt-realtime 的路线比较

## 相关

- [[Qwen2-5-VL Technical Report|Qwen2.5-VL Technical Report]]
- [[Moshi：a speech-text foundation model for real-time dialogue]]
- [[Voice、Realtime 与语音工作流]]
