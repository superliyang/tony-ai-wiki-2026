---
title: Mistral OCR 3
type: system
status: active
tags:
  - ai/system
  - ai/document-ai
  - ai/ocr
  - organization/mistral
aliases: []
organization: "[[Mistral AI]]"
modality:
  - api
  - document
family: Mistral OCR
related_papers:
  - "[[ScreenAI：A Vision-Language Model for UI and Infographics Understanding]]"
  - "[[Qwen2-5-VL Technical Report|Qwen2.5-VL Technical Report]]"
  - "[[Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing|PaddleOCR-VL]]"
related_people: []
created: 2026-04-03
updated: 2026-04-03
---

# Mistral OCR 3

## 简介

`Mistral OCR 3` 是 Mistral AI 把 document AI / OCR 路线收成真实企业系统面的关键产品。

## 为什么重要

- 它说明 `OCR` 正在从识别模块变成 `document-to-markdown/json` 的工作流入口
- 它把复杂表格、手写内容、低质量扫描、多语言文档这些企业高频痛点直接产品化
- 它让 document AI 从“多模态可以做的一件事”变成“企业愿意为之部署的一条系统路线”

## 官方定位里最值得记住的点

- `2025-12-15`：Mistral 将 `OCR 3` 作为独立模型家族发布
- 它支持把文档解析成结构保真的 `markdown`、`HTML tables` 和更适合程序消费的输出
- 官方同时把它接进 `Document AI Playground` 和 API，说明 Mistral 想把它做成既可交互也可批量处理的系统面

## 你可以把它当成什么来理解

- `Mistral OCR 3` 不是传统 OCR SDK 的简单升级
- 更准确地说，它是 `document understanding + structured extraction + workflow entry layer`

所以它特别适合用来理解：

- 企业文档如何进入 agent 工作流
- 文档结构保真为什么和模型能力同样重要
- 为什么 document AI 会重新成为多模态竞争的高价值分支

## 学习时重点看什么

- 为什么 `markdown / html / structured fields` 输出形式很关键
- 为什么 forms、tables、handwriting 和 low-quality scans 是真实价值所在
- 为什么企业会关心 self-hosting、API、playground 和批量处理能力

## 所属组织

- [[Mistral AI]]

## 相关主题

- [[OCR 与 Document AI]]
- [[Multimodal Models]]
- [[AI Industry]]

## 相关路线页

- [[../11-Recent-Supplements/2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流|2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流]]

## 资料

- [Mistral OCR 3](https://legal.mistral.ai/ai-governance/models/mistral-ocr-3)
- [Introducing Mistral OCR 3](https://mistral.ai/it/news/mistral-ocr-3)
- [Document AI - OCR Processor](https://docs.mistral.ai/capabilities/document_ai/basic_ocr)
