---
title: 2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流
type: guide
status: active
updated: 2026-04-03
---

# 2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流

> 这页把最近两年 `multimodal` 里最容易被忽略、但最接近企业真实价值的一条线单独拉出来：`OCR / document AI`。

## 先说边界

- 这里的 `2026` 不是完整年份，而是截至 `2026-04-03` 的补线视角。
- 这页不追传统 OCR 全史，而是只抓最近两年把 document understanding 拉成独立产品路线的锚点。
- 真正要记住的是：`OCR` 正在从“字符识别模块”变成 `document-to-markdown/json -> extraction -> workflow trigger -> agent context` 的入口层。

## 一页总表

| 论文 / 报告 / 系统 | 年份 | 它真正补上的东西 | 模型路线 | 系统路线 | 产品路线 |
| --- | --- | --- | --- | --- | --- |
| [[../04-Papers/ScreenAI：A Vision-Language Model for UI and Infographics Understanding|ScreenAI]] | 2024 | 把界面 / infographic / document 感知收成统一视觉理解问题 | [[../06-Topics/Multimodal Models|Multimodal Models]] | [[../06-Topics/OCR 与 Document AI|OCR 与 Document AI]]、[[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]] | 文档理解、界面理解、computer use 感知底座 |
| [[../04-Papers/Qwen2-5-VL Technical Report|Qwen2.5-VL Technical Report]] | 2025 | 把 open multimodal 推向 document / diagram / visual agent 方向 | [[../03-Models/Qwen 系列|Qwen 系列]] | [[../06-Topics/Multimodal Models|Multimodal Models]]、[[../06-Topics/OCR 与 Document AI|OCR 与 Document AI]] | document AI、diagram understanding、视觉工作流 |
| [[../09-Systems/Mistral OCR 3|Mistral OCR 3]] | 2025 | 把 `document-to-markdown/json` 做成真正的企业产品面 | 文档专用 OCR / Document AI | [[../06-Topics/OCR 与 Document AI|OCR 与 Document AI]] | invoice / form parsing、knowledge ingestion、enterprise document pipelines |
| [[../04-Papers/Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing|PaddleOCR-VL]] | 2026 | 把 document parsing 推向 `coarse-to-fine + high-resolution efficiency` | document-specialized VLM | [[../06-Topics/OCR 与 Document AI|OCR 与 Document AI]] | 高分辨率文档解析、多语言文档解析、低成本批量处理 |

## 路线一：从 OCR 走向结构化 document understanding

这一条线最关键的锚点是：

1. [[../04-Papers/ScreenAI：A Vision-Language Model for UI and Infographics Understanding|ScreenAI]]
2. [[../09-Systems/Mistral OCR 3|Mistral OCR 3]]
3. [[../06-Topics/OCR 与 Document AI|OCR 与 Document AI]]

这条线最该建立的判断是：

- 新一代 document AI 不只是识别字符
- 它要保留结构、表格、段落层级、图像与版式
- 它输出的也不只是纯文本，而是更适合 agent 和 downstream system 消费的 `markdown / html / json / structured fields`

## 路线二：从 general multimodal 走向 document-specialized 路线

这一条线最关键的锚点是：

1. [[../04-Papers/Qwen2-5-VL Technical Report|Qwen2.5-VL Technical Report]]
2. [[../04-Papers/Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing|PaddleOCR-VL]]
3. [[../06-Topics/Multimodal Models|Multimodal Models]]

这条线真正补上的判断是：

- 通用多模态底座很重要，但文档解析有自己独立的效率约束与精度约束
- 文档不是普通图片，它有高分辨率、复杂布局、多列、多表格、多语言和结构保真的要求
- 所以 document AI 会自然长出一条更 specialized 的模型路线

## 路线三：Document AI 进入真实企业工作流

这一条线最值得记住的工作流入口是：

- contract / policy extraction
- invoice / receipt parsing
- enterprise archive digitization
- technical report ingestion
- knowledge base construction
- agent context preparation

所以 document AI 最该被理解成：

- `multimodal` 的高价值落地方向
- `enterprise workflow automation` 的高频入口
- `agent` 在进入真实组织前最常见的数据整理层

## 这一轮补线后，文档主线怎么理解

- `ScreenAI` 代表的是 perception 底座
- `Qwen2.5-VL` 代表的是 open multimodal 往文档和视觉代理方向扩张
- `Mistral OCR 3` 代表的是 document AI 的产品化与企业化
- `PaddleOCR-VL` 代表的是 2026 年开始更明显出现的 `document-specialized efficiency race`

## 最短回顾顺序

1. [[../../近五年关键 AI 论文与路线映射（2021-2025）|近五年关键 AI 论文与路线映射（2021-2025）]]
2. [[2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use|2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use]]
3. [[../04-Papers/ScreenAI：A Vision-Language Model for UI and Infographics Understanding|ScreenAI]]
4. [[../04-Papers/Qwen2-5-VL Technical Report|Qwen2.5-VL Technical Report]]
5. [[../09-Systems/Mistral OCR 3|Mistral OCR 3]]
6. [[../04-Papers/Boosting Document Parsing Efficiency and Performance with Coarse-to-Fine Visual Processing|PaddleOCR-VL]]
7. [[../06-Topics/OCR 与 Document AI|OCR 与 Document AI]]
8. [[../06-Topics/Multimodal Models|Multimodal Models]]

## 读完这页后你应该能自己回答

- 为什么 document AI 是多模态里最接近真实企业价值的分支之一
- 为什么 OCR 现在更像 `文档理解 + 结构保真 + workflow entry`，而不是单一识别模块
- 为什么最近两年 document AI 同时在走两条线：`general multimodal extension` 和 `document-specialized model`

## 关联

- [[../../近五年关键 AI 论文与路线映射（2021-2025）|近五年关键 AI 论文与路线映射（2021-2025）]]
- [[2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use|2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use]]
- [[2024-2026 AI 新路线补线：Voice、Realtime 与语音工作流|2024-2026 AI 新路线补线：Voice、Realtime 与语音工作流]]
- [[../../我想通过作者、论文与时间线理解 AI|我想通过作者、论文与时间线理解 AI]]
- [[../04-Papers/论文索引|论文索引]]
- [[../06-Topics/OCR 与 Document AI|OCR 与 Document AI]]
- [[../06-Topics/Multimodal Models|Multimodal Models]]
- [[../09-Systems/Mistral OCR 3|Mistral OCR 3]]
