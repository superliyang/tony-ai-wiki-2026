---
title: 2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use
type: guide
status: active
updated: 2026-04-03
---

# 2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use

> 这页是对 [[../../近五年关键 AI 论文与路线映射（2021-2025）|近五年关键 AI 论文与路线映射（2021-2025）]] 的继续补线。前一页解决的是主干，这一页解决的是 `2024-2026` 里把主干真正拉宽的三条路线。

## 先说边界

- 这里的 `2026` 不是完整年份，而是截至 `2026-04-03` 的补线视角。
- 这页不追求把所有新论文收全，而是只挑能真正改变最近两年系统形态和产品形态的锚点。
- 这轮最值得补的三条线是：`long context`、`multimodal productization`、`computer use / browser agents`。

## 一页总表

| 论文 / 报告 | 年份 | 它真正补上的东西 | 模型路线 | 系统路线 | 产品路线 |
| --- | --- | --- | --- | --- | --- |
| [[../04-Papers/Gemini 1-5：Unlocking multimodal understanding across millions of tokens of context|Gemini 1.5：Unlocking multimodal understanding across millions of tokens of context]] | 2024 | 把 `million-token context` 从口号变成模型主能力 | [[../03-Models/Gemini 系列|Gemini 系列]] | [[../09-Systems/Gemini CLI|Gemini CLI]]、[[../09-Systems/Google Agent Development Kit（ADK）|Google Agent Development Kit（ADK）]] | 长文档助手、代码库级助手、超长上下文工作台 |
| [[../04-Papers/GPT-4o System Card|GPT-4o System Card]] | 2024 | 把 `omni multimodal` 变成真实产品能力和安全叙事 | [[../03-Models/GPT 系列|GPT 系列]] | [[../09-Systems/ChatGPT|ChatGPT]]、[[../09-Systems/OpenAI API|OpenAI API]]、[[../09-Systems/ChatGPT Agent|ChatGPT Agent]] | 实时多模态助手、voice / vision / chat 一体化产品 |
| [[../04-Papers/ScreenAI：A Vision-Language Model for UI and Infographics Understanding|ScreenAI：A Vision-Language Model for UI and Infographics Understanding]] | 2024 | 把 UI / infographic / document understanding 收成感知层基础能力 | [[../03-Models/Gemini 系列|Gemini 系列]] | [[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]]、[[../06-Topics/OCR 与 Document AI|OCR 与 Document AI]] | 界面理解、文档理解、computer use 感知底座 |
| [[../04-Papers/WebVoyager：Building an End-to-End Web Agent with Large Multimodal Models|WebVoyager：Building an End-to-End Web Agent with Large Multimodal Models]] | 2024 | 把 browser agent 从 demo 概念推进到真实网站环境 | [[../06-Topics/Agent|Agent]] | [[../09-Systems/ChatGPT Agent|ChatGPT Agent]]、[[../09-Systems/OpenClaw|OpenClaw]] | browser agent、cloud task agent、网页执行代理 |
| [[../04-Papers/Qwen2-5-VL Technical Report|Qwen2.5-VL Technical Report]] | 2025 | 把 open multimodal 往 document / diagram / visual agent 路线推进 | [[../03-Models/Qwen 系列|Qwen 系列]] | [[../06-Topics/Multimodal Models|Multimodal Models]]、[[../06-Topics/OCR 与 Document AI|OCR 与 Document AI]] | 开放多模态模型、document AI、视觉工作流产品 |

## 路线一：Long Context 从“窗口更大”变成系统能力

这一条线最关键的锚点是：

1. [[../04-Papers/Gemini 1-5：Unlocking multimodal understanding across millions of tokens of context|Gemini 1.5]]
2. [[../06-Topics/Long Context|Long Context]]
3. [[../09-Systems/Kimi|Kimi]]
4. [[../09-Systems/Gemini CLI|Gemini CLI]]

这条线最该建立的判断是：

- `long context` 不再只是“能塞更多 token”，而是直接改变代码、文档、知识工作和 agent 的工作集大小
- 一旦上下文窗口进入 `million-token` 量级，系统设计会开始改变：哪些信息直接放进上下文，哪些仍交给检索、记忆和工具层
- 这会反过来影响 coding assistant、document AI、enterprise knowledge assistant 的产品形态

## 路线二：Multimodal 从“会看图”变成产品主界面

这一条线最关键的锚点是：

1. [[../04-Papers/GPT-4o System Card|GPT-4o System Card]]
2. [[../04-Papers/Gemini 1-5：Unlocking multimodal understanding across millions of tokens of context|Gemini 1.5]]
3. [[../04-Papers/Qwen2-5-VL Technical Report|Qwen2.5-VL Technical Report]]
4. [[../06-Topics/Multimodal Models|Multimodal Models]]

这条线真正补上的，不只是“多一个模态”，而是：

- voice、vision、text 越来越被收进一个统一交互面
- multimodal 不再只是展示能力，而是开始进入 `document AI`、`screen understanding`、`agent action surface`
- 产品的主界面会因此改变，从 `chat box` 走向 `see + hear + speak + act`

## 路线三：Computer Use 从动作想象变成工程面

这一条线最关键的锚点是：

1. [[../04-Papers/ScreenAI：A Vision-Language Model for UI and Infographics Understanding|ScreenAI]]
2. [[../04-Papers/WebVoyager：Building an End-to-End Web Agent with Large Multimodal Models|WebVoyager]]
3. [[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]]
4. [[../../AI-Engineering/07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]]

这条线真正补上的判断是：

- `computer use` 不是单一模型能力，而是 `perception + grounding + action + recovery + safety` 的组合问题
- 你现在看到的 browser agent / cloud agent 产品，不是凭空冒出来的，而是建立在 UI 理解、网页导航、动作闭环和安全边界这些研究之上
- 所以它同时是视觉问题、agent runtime 问题、也是 product governance 问题

## 这一轮补线后，最近两年的结构怎么理解

- `2021-2023` 更像是在把通用大模型、后训练、reasoning、tool use 和 open-weight 主干立起来
- `2024-2026（截至 2026-04-03）` 更像是在把这些主干真正推向 `长工作集`、`多模态主界面` 和 `browser / computer-use` 这几个真实动作面

## 最短回顾顺序

1. [[../../近五年关键 AI 论文与路线映射（2021-2025）|近五年关键 AI 论文与路线映射（2021-2025）]]
2. [[../04-Papers/Gemini 1-5：Unlocking multimodal understanding across millions of tokens of context|Gemini 1.5]]
3. [[../04-Papers/GPT-4o System Card|GPT-4o System Card]]
4. [[../04-Papers/ScreenAI：A Vision-Language Model for UI and Infographics Understanding|ScreenAI]]
5. [[../04-Papers/WebVoyager：Building an End-to-End Web Agent with Large Multimodal Models|WebVoyager]]
6. [[../04-Papers/Qwen2-5-VL Technical Report|Qwen2.5-VL Technical Report]]
7. [[../06-Topics/Long Context|Long Context]]
8. [[../06-Topics/Multimodal Models|Multimodal Models]]
9. [[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]]

## 读完这页后你应该能自己回答

- 为什么最近两年的 frontier 竞争越来越像 `长上下文 + 原生多模态 + computer use`
- 为什么 `long context`、`multimodal`、`computer use` 会直接改变 coding assistant、cloud agent、document AI 的系统形态
- 为什么今天看产品路线，不能只看模型强不强，还要看它是不是把感知面、动作面和治理面一起拉起来了

## 关联

- [[../../近五年关键 AI 论文与路线映射（2021-2025）|近五年关键 AI 论文与路线映射（2021-2025）]]
- [[../../我想通过作者、论文与时间线理解 AI|我想通过作者、论文与时间线理解 AI]]
- [[../04-Papers/论文索引|论文索引]]
- [[../06-Topics/Long Context|Long Context]]
- [[../06-Topics/Multimodal Models|Multimodal Models]]
- [[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]]
- [[2024-2026 AI 新路线补线：Voice、Realtime 与语音工作流|2024-2026 AI 新路线补线：Voice、Realtime 与语音工作流]]
- [[2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流|2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流]]
