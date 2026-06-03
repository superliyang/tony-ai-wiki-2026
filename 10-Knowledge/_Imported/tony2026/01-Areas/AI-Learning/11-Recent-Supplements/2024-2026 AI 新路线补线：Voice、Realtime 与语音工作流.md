---
title: 2024-2026 AI 新路线补线：Voice、Realtime 与语音工作流
type: guide
status: active
updated: 2026-04-03
---

# 2024-2026 AI 新路线补线：Voice、Realtime 与语音工作流

> 这页继续补 [[../../近五年关键 AI 论文与路线映射（2021-2025）|近五年关键 AI 论文与路线映射（2021-2025）]] 和 [[2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use|2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use]] 之后还没单独拉开的那条线：`voice / realtime`。

## 先说边界

- 这里的 `2026` 不是完整年份，而是截至 `2026-04-03` 的补线视角。
- 这里不追语音模型全史，只抓住最近两年真正改变系统形态和产品形态的锚点。
- 这条线真正值得记住的，不是“模型开始会说话”，而是：`低延迟 + 双工对话 + 工具调用 + 生产化语音代理` 开始收成一条完整路线。

## 一页总表

| 论文 / 报告 / 系统 | 年份 | 它真正补上的东西 | 模型路线 | 系统路线 | 产品路线 |
| --- | --- | --- | --- | --- | --- |
| [[../04-Papers/GPT-4o System Card|GPT-4o System Card]] | 2024 | 把 `omni multimodal` 收成统一交互界面 | [[../03-Models/GPT 系列|GPT 系列]] | [[../09-Systems/ChatGPT|ChatGPT]]、[[../09-Systems/OpenAI API|OpenAI API]] | Advanced Voice、voice-first assistant、多模态主入口 |
| [[../04-Papers/Moshi：a speech-text foundation model for real-time dialogue|Moshi]] | 2024 | 把 `speech-to-speech + full-duplex` 做成研究锚点 | 实时 spoken foundation model | [[../06-Topics/Voice、Realtime 与语音工作流|Voice、Realtime 与语音工作流]] | 实时语音助手、低延迟对话、可打断对话系统 |
| [[../09-Systems/OpenAI Realtime API|OpenAI Realtime API]] | 2024-2025 | 把 realtime voice 从 demo 能力推进到开发者系统面 | [[../03-Models/GPT 系列|GPT 系列]] | [[../09-Systems/OpenAI API|OpenAI API]]、[[../09-Systems/ChatGPT|ChatGPT]] | customer support agents、language tutors、phone agents |
| [[../04-Papers/Qwen2-5-Omni Technical Report|Qwen2.5-Omni Technical Report]] | 2025 | 把 open multimodal 往 `text + image + audio + video + streaming speech` 推进 | [[../03-Models/Qwen 系列|Qwen 系列]] | [[../06-Topics/Multimodal Models|Multimodal Models]]、[[../06-Topics/Voice、Realtime 与语音工作流|Voice、Realtime 与语音工作流]] | 开放多模态助手、实时语音交互、多语言语音代理 |

## 路线一：从 ASR -> LLM -> TTS pipeline，走向端到端语音交互

这一条线最关键的锚点是：

1. [[../04-Papers/Moshi：a speech-text foundation model for real-time dialogue|Moshi]]
2. [[../04-Papers/Qwen2-5-Omni Technical Report|Qwen2.5-Omni Technical Report]]
3. [[../06-Topics/Voice、Realtime 与语音工作流|Voice、Realtime 与语音工作流]]

这条线最该建立的判断是：

- 过去的语音系统往往是 `ASR -> text model -> TTS` 串起来的 pipeline
- 最近两年的 frontier 更像是在追求 `native speech interaction`
- 一旦系统开始直接处理语音输入、语音输出、打断、重叠说话和非语言信号，产品形态就不再只是“会读出来的 chatbot”

## 路线二：Realtime 不再只是模型能力，而是 API 与 runtime surface

这一条线最关键的锚点是：

1. [[../04-Papers/GPT-4o System Card|GPT-4o System Card]]
2. [[../09-Systems/OpenAI Realtime API|OpenAI Realtime API]]
3. [[../09-Systems/OpenAI API|OpenAI API]]
4. [[../09-Systems/ChatGPT|ChatGPT]]

这条线真正补上的判断是：

- `voice / realtime` 不是一个“语音特性”，而是新的系统表面
- 这里的关键问题不只是模型懂不懂语音，而是系统能不能低延迟、能不能打断、能不能继续对话、能不能接工具
- `2024-10-01` OpenAI 公开 Realtime API beta，`2025-08-28` 又把它推进到 GA，并补上 `remote MCP server`、`image input` 和 `SIP phone calling`，这说明语音代理已经开始走向生产环境

## 路线三：Voice 开始进入真实工作流

这一条线最值得记住的不是 benchmark，而是工作流入口：

- customer support agents
- language learning assistants
- phone agents
- hands-free productivity
- multimodal field assistants

所以这条线应该被理解成：

- `voice` 是交互入口
- `realtime` 是系统要求
- `tool use / MCP / function calling` 是可执行能力
- `safety / privacy / disclosure` 是生产化边界

## 这一轮补线后，语音主线怎么理解

- `GPT-4o` 代表的是统一多模态主界面
- `Moshi` 代表的是 research side 对 `full-duplex spoken dialogue` 的明确推进
- `OpenAI Realtime API` 代表的是把语音能力收成可部署系统面
- `Qwen2.5-Omni` 代表的是 open multimodal 路线往 streaming speech 和 end-to-end omni model 继续扩张

## 最短回顾顺序

1. [[../../近五年关键 AI 论文与路线映射（2021-2025）|近五年关键 AI 论文与路线映射（2021-2025）]]
2. [[2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use|2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use]]
3. [[../04-Papers/GPT-4o System Card|GPT-4o System Card]]
4. [[../04-Papers/Moshi：a speech-text foundation model for real-time dialogue|Moshi]]
5. [[../09-Systems/OpenAI Realtime API|OpenAI Realtime API]]
6. [[../04-Papers/Qwen2-5-Omni Technical Report|Qwen2.5-Omni Technical Report]]
7. [[../06-Topics/Voice、Realtime 与语音工作流|Voice、Realtime 与语音工作流]]
8. [[../09-Systems/OpenAI API|OpenAI API]]
9. [[../09-Systems/ChatGPT|ChatGPT]]

## 读完这页后你应该能自己回答

- 为什么 `voice / realtime` 不是附属功能，而是一条独立系统路线
- 为什么最近两年语音路线的关键不只是 TTS，而是 `speech-to-speech + low latency + tool use`
- 为什么 production voice agent 会自然接到 `API、MCP、phone calling、guardrails` 这些系统层问题

## 关联

- [[../../近五年关键 AI 论文与路线映射（2021-2025）|近五年关键 AI 论文与路线映射（2021-2025）]]
- [[2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use|2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use]]
- [[2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流|2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流]]
- [[../../我想通过作者、论文与时间线理解 AI|我想通过作者、论文与时间线理解 AI]]
- [[../04-Papers/论文索引|论文索引]]
- [[../06-Topics/Voice、Realtime 与语音工作流|Voice、Realtime 与语音工作流]]
- [[../06-Topics/Multimodal Models|Multimodal Models]]
- [[../09-Systems/OpenAI Realtime API|OpenAI Realtime API]]
