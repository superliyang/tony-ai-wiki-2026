---
title: OCR 与 Document AI
type: topic
status: active
tags:
  - ai/topic
  - ai/document-ai
created: 2026-03-25
updated: 2026-04-03
---

# OCR 与 Document AI

## 这个主题是什么

`OCR 与 Document AI` 关注模型如何理解扫描文档、复杂版式、表格、票据、合同和企业文档流。

## 为什么重要

最近两年，一个非常容易被“通用模型新闻”遮住的趋势是：`document AI` 再次成为前沿竞争的重要分支。

原因很直接：

- 企业落地并不只需要聊天和 coding
- 大量真实工作仍然围绕 PDF、合同、表格、票据和复杂版式展开
- OCR + reasoning + tool use 结合后，会直接推动 enterprise workflow automation

## 最近半年最值得关注的信号

- [[Mistral OCR 3]] 让 `document-to-markdown/json` 进入真正的产品面
- [[Qwen2-5-VL Technical Report|Qwen2.5-VL Technical Report]] 把 open multimodal 往 document / diagram / visual agent 方向推进
- [[Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing|PaddleOCR-VL]] 把 document parsing 推向 `coarse-to-fine + high-resolution efficiency`
- [[ScreenAI：A Vision-Language Model for UI and Infographics Understanding|ScreenAI]] 说明 UI / infographic / document understanding 正在收成统一感知层

## 你先要抓住什么

- OCR 不再只是字符识别
- 新一代 document AI 更像：`视觉理解 + 结构理解 + 语义抽取 + reasoning + action`
- 所以 document AI 正在从“识别模块”变成“agent workflow 入口”
- 真正高价值的系统输出，也越来越不是纯文本，而是 `markdown / html / json / structured fields`

## 典型任务

- contract extraction
- invoice / receipt parsing
- table understanding
- knowledge ingestion
- document Q&A
- workflow triggering
- document-to-markdown / json

## 最近两年最值得记住的论文 / 系统锚点

- [[ScreenAI：A Vision-Language Model for UI and Infographics Understanding]]
- [[Qwen2-5-VL Technical Report|Qwen2.5-VL Technical Report]]
- [[Mistral OCR 3]]
- [[Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing|PaddleOCR-VL]]
- [[../11-Recent-Supplements/2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流|2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流]]

## 它为什么值得放进 AI 主线里

因为 document AI 是一个非常典型的“从多模态能力走向 agent 落地”的桥：

- 底座来自 [[Multimodal Models]]
- 可靠性来自 [[Reasoning Models]]
- 业务价值落在 [[AI Industry]] 和 agent workflows

## 相关

- [[Multimodal Models]]
- [[Reasoning Models]]
- [[AI Industry]]
- [[Mistral OCR 3]]
- [[../11-Recent-Supplements/2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流|2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流]]
- [[Sovereign AI]]
- [[过去半年全球 AI 前沿动态（2025-09-25 至 2026-03-25）]]
- [[../07-Maps/AI 前沿主题演化图|AI 前沿主题演化图]]
