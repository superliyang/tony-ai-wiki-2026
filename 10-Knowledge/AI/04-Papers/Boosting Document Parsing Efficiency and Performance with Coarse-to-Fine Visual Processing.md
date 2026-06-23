---
title: Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing
type: paper
status: active
tags:
  - ai/paper
  - ai/document-ai
  - ai/ocr
aliases:
  - PaddleOCR-VL
authors: []
organization:
  - PaddlePaddle
year: 2026
venue: CVPR 2026
related_models: []
related_people: []
related_topics:
  - "[[OCR 与 Document AI]]"
  - "[[Multimodal Models]]"
source: https://arxiv.org/abs/2603.24326
created: 2026-04-03
updated: 2026-04-03
---

# Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing

## 简介

这篇论文更适合作为 `PaddleOCR-VL` 来记，因为它代表的是 document AI 在 `2026-03-25` 已经明显走向专门化模型路线。

## 核心想法

它把 document parsing 的主要难题明确成：高分辨率文档会带来很高的视觉 token 成本，而大量背景区域其实是冗余的。

所以它的解法不是继续暴力堆更大视觉输入，而是做：

- `coarse-to-fine` 文档解析
- 有效区域筛选
- 小而强的 `0.9B` 文档 VLM

## 为什么重要

- 它说明 document AI 已经不只是通用 VLM 的副产品
- 它把高分辨率、多元素、多语言文档解析收成一个独立优化目标
- 它把 `efficiency race` 正式带进 document AI 这条线

## 最值得记住的点

- 论文提出 `VRFM` 去识别语义相关区域，压低无效视觉 token
- 它强调 page-level parsing 和 element-level recognition 同时都要强
- 这类路线对企业场景很关键，因为大规模文档处理里成本和吞吐往往与精度同样重要

## 这篇论文真正改了哪条路线

- 模型路线：从通用 multimodal 走向 document-specialized VLM
- 系统路线：从“能读文档”走向“可大规模解析复杂文档”
- 产品路线：把 document AI 推向更可负担、更适合批量企业工作流的方向

## 相关主题

- [[OCR 与 Document AI]]
- [[Multimodal Models]]

## 相关系统

- [[Mistral OCR 3]]

## 相关

- [[ScreenAI：A Vision-Language Model for UI and Infographics Understanding]]
- [[Qwen2-5-VL Technical Report|Qwen2.5-VL Technical Report]]
- [[OCR 与 Document AI]]
