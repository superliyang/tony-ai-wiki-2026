---
title: 2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime
type: guide
status: active
updated: 2026-04-13
---

# 2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime

> 这页补的是另一条过去容易被低估、但从 `2025` 到 `2026-04-13` 已经明显改变 AI 系统形态的主线：`research agent`、`memory / context management`、以及 `agent runtime` 的标准化。

## 先说边界

- 这里关注的不是“又多了几个模型名字”，而是 `模型怎么被装进长任务系统`。
- 这条线的核心变化不是单轮回答更强，而是：`异步研究`、`跨会话记忆`、`上下文压缩`、`MCP / A2A` 这几层开始一起成熟。
- 这里的 `2026` 是截至 `2026-04-13` 的视角，不是假装全年已经结束。

## 一页总表

| 锚点 | 时间 | 它真正补上的东西 | 你该如何理解 |
| --- | --- | --- | --- |
| [[../04-Papers/Deep Research System Card|Deep Research System Card]] | 2025-02-25 | 把 `multi-step web research` 做成正式 agent 能力 | research agent 不再只是 browse demo，而是长任务产品 lane |
| [OpenAI MCP docs](https://developers.openai.com/api/docs/mcp) | 2025-2026 | 把 `ChatGPT apps / deep research / API integrations` 接到同一套 remote MCP 入口 | MCP 已从“协议概念”进入主流产品与 API surface |
| [OpenAI Memory FAQ](https://help.openai.com/en/articles/8590148-memory-faq) | 2025-2026 | 把 `saved memories`、`chat history`、`top-of-mind prioritization`、`nightly pulse` 讲成产品内长期记忆系统 | consumer/product memory 已经不只是静态偏好栏 |
| [Claude Code memory docs](https://code.claude.com/docs/en/memory) | 2025-2026 | 把 `CLAUDE.md`、`auto memory`、`path-scoped rules`、`per working tree` 落成正式机制 | coding agent 的 project memory 已经工程化 |
| [Anthropic context windows docs](https://platform.claude.com/docs/en/build-with-claude/context-windows) | 2025-2026 | 把 `compaction`、`context editing`、`thinking block stripping`、`context awareness` 讲成一整套 context management | 上下文不再只是窗口大小，而是运行时设计问题 |
| [ADK A2A intro](https://adk.dev/a2a/intro/) + [Google Cloud donates A2A to Linux Foundation](https://developers.googleblog.com/google-cloud-donates-a2a-to-linux-foundation/) | 2025-06-23 | 把 remote agent interop 从框架功能推进到中立治理的开放标准 | A2A 不是概念玩具，而是在往产业协议走 |

## 路线一：Research Agent 从“会搜网页”变成“能跑长任务”

这条线最该抓的不是 `search`，而是 `research workflow`：

- 拆问题
- 多步检索
- 读网页、PDF、图像与文件
- 过程中动态转向
- 写报告、给 citation
- 在安全边界内做 code execution

这也是为什么 `2025-02-25` 的 [[../04-Papers/Deep Research System Card|Deep Research System Card]] 值得单独记住。它明确把 deep research 定义成 `multi-step research on the internet for complex tasks`，并且把 `web browsing + file reading + python analysis + synthesis` 放进同一个 agentic capability 里。

更重要的是，这条线会直接改变你对下面这些概念的理解：

- `RAG` 不再等于全部知识增强
- `browser agent` 不再等于全部长任务 agent
- `research agent` 的关键不只是能不能搜，而是能不能 `长时间保持目标、过滤来源、组织证据、形成报告`

## 路线二：Memory 开始从偏好功能变成一等运行时层

最近这波变化真正值得记住的，不是“产品终于有 memory”，而是 memory 被拆得更清楚了：

- `saved memories`
- `reference chat history`
- `project memory`
- `auto memory`
- `context compaction`
- `background / asynchronous memory maintenance`

[OpenAI Memory FAQ](https://help.openai.com/en/articles/8590148-memory-faq) 现在已经明确区分：

- `Reference saved memories`
- `Reference chat history`
- `top-of-mind prioritization`
- `nightly, asynchronous research` 的 `ChatGPT pulse`

而 [Claude Code memory docs](https://code.claude.com/docs/en/memory) 则把另一条线讲得更清楚：

- `CLAUDE.md` 是人写的 persistent instructions
- `auto memory` 是 Claude 自己沉淀的 learnings
- 作用域可以分到 `project / user / org / working tree`

这说明 memory 的核心问题已经从“要不要记”升级成：

- 谁写
- 写到哪一层
- 跨多大边界生效
- 什么时候压缩
- 什么时候过期或回滚

## 路线三：Context management 成为 agent runtime 的主问题

`2024` 的很多讨论还停在 “window 变大了”。

但到了 `2025-2026`，更成熟的官方文档已经在讲：

- `server-side compaction`
- `context editing`
- `thinking block stripping`
- `context awareness`
- `tool-result handling`

[Anthropic context windows docs](https://platform.claude.com/docs/en/build-with-claude/context-windows) 甚至把一个很关键的工程事实讲透了：

- `extended thinking` 会计费、会占当轮 token
- 但旧的 thinking blocks 可以在后续轮次被自动剥离
- 长任务能否稳定，不只看窗口多大，还看 runtime 怎么管理上下文

这会直接改变你对 `上下文工程` 的理解：

- 上下文不只是“塞多少”
- 更是 `如何裁剪、如何压缩、如何在 tool cycle 里保真`

## 路线四：Agent runtime 正在协议化，而不是只靠单一框架

最近两年还有一个经常被忽略的结构性变化：

- `MCP` 更像工具 / 资源接入标准
- `A2A` 更像 remote agent 协作标准
- `local sub-agents` 仍然是同进程内部组织方式

[OpenAI MCP docs](https://developers.openai.com/api/docs/mcp) 已经把 remote MCP server 直接接到：

- ChatGPT apps
- deep research
- API integrations

并且文档明确写到 `2025-12-17`，ChatGPT 把 connectors 更名为 apps。

而 Google 这边：

- [ADK A2A intro](https://adk.dev/a2a/intro/) 明确把 `A2A` 定义成 remote agent communication standard
- `2025-06-23` 的 [Google Cloud donates A2A to Linux Foundation](https://developers.googleblog.com/google-cloud-donates-a2a-to-linux-foundation/) 又把它推进到 Linux Foundation 下的中立治理

所以这条线最该形成的判断是：

- 不要把 `MCP`、`A2A`、`local sub-agent` 混成一个东西
- 真正成熟的 agent runtime 会同时区分 `tool integration`、`remote agent interoperability`、`context/memory management` 和 `approval / governance`

## 这一轮补线后，你应该怎么重排自己的 AI 图谱

如果之前你把近两年 AI 变化主要理解成：

- long context
- multimodal
- voice
- OCR
- computer use

那现在应该再补进这一层：

- `deep research / long-horizon agent`
- `product memory / project memory / runtime memory`
- `context compaction / editing / awareness`
- `MCP / A2A / runtime standardization`

也就是说，最近这波真正的新东西已经不只是 `模态变多`，而是 `系统开始长期运行并越来越像工作台`。

## 最短回顾顺序

1. [[../../近五年关键 AI 论文与路线映射（2021-2025）|近五年关键 AI 论文与路线映射（2021-2025）]]
2. [[截至 2026-04-07 的 2026 新模型刷新|截至 2026-04-07 的 2026 新模型刷新]]
3. [[../04-Papers/Deep Research System Card|Deep Research System Card]]
4. [[../06-Topics/Deep Research 与 Research Agents|Deep Research 与 Research Agents]]
5. [[../06-Topics/Agent Memory|Agent Memory]]
6. [[../06-Topics/上下文工程|上下文工程]]
7. [[../06-Topics/MCP（Model Context Protocol）|MCP（Model Context Protocol）]]
8. [[../06-Topics/A2A（Agent-to-Agent）与协作协议|A2A（Agent-to-Agent）与协作协议]]
9. [[../06-Topics/Agent 平台|Agent 平台]]

## 读完这页后你应该能自己回答

- 为什么 `research agent` 不是简单的 search + summary
- 为什么 memory 已经分化成产品记忆、项目记忆和 runtime 记忆
- 为什么 context engineering 现在必须包含 `compaction / editing / awareness`
- 为什么 `MCP` 和 `A2A` 解决的是不同层的问题

## 关联

- [[截至 2026-04-07 的 2026 新模型刷新|截至 2026-04-07 的 2026 新模型刷新]]
- [[最近半年最值得重投入学习的 AI 主线（截至 2026-04-07）|最近半年最值得重投入学习的 AI 主线（截至 2026-04-07）]]
- [[2025-2026 AI 治理补线：Model Spec、Preparedness、Transparency 与 AI Act|2025-2026 AI 治理补线：Model Spec、Preparedness、Transparency 与 AI Act]]
- [[../04-Papers/Deep Research System Card|Deep Research System Card]]
- [[../06-Topics/Deep Research 与 Research Agents|Deep Research 与 Research Agents]]
- [[../06-Topics/Agent|Agent]]
- [[../06-Topics/Agent Memory|Agent Memory]]
- [[../06-Topics/上下文工程|上下文工程]]
- [[../06-Topics/MCP（Model Context Protocol）|MCP（Model Context Protocol）]]
- [[../06-Topics/A2A（Agent-to-Agent）与协作协议|A2A（Agent-to-Agent）与协作协议]]
