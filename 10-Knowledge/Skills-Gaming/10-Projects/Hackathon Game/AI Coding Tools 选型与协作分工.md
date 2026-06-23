---
title: AI Coding Tools 选型与协作分工
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# AI Coding Tools 选型与协作分工

## 先说结论

对你们这次 `Word Sprint Duel V1`，最稳的不是只选一个工具，而是：

- `Google AI Studio` 负责创意、文案、视觉、语音、宣传
- 选一个主 coding cockpit
- 再用一个擅长长任务或后台任务的 agent 做补位

## 我推荐的默认组合

### 组合 A：最稳

- `Cursor`：主 IDE / 主 coding cockpit
- `Claude Code`：终端式仓库分析、后端/API、批处理修改
- `Google AI Studio`：内容与素材生成

这组最适合：

- 你要快速做 demo
- 需要 IDE 内高频来回改
- 同时又想让一部分仓库级任务交给更偏 agentic 的工具

### 组合 B：更偏云端代理

- `Cursor` 或 `Windsurf`：主 IDE
- `Codex`：云端并行任务、异步修复、文档/测试任务
- `Google AI Studio`：创意与资产层

这组更适合：

- 你想把一些非阻塞任务后台并发出去
- 你愿意接受更明显的“本地 IDE + 云端 agent”分工

### 组合 C：更偏 Google 生态

- `Gemini Code Assist`
- `Google AI Studio`
- 可选 `Unity AI` / `Roblox Assistant`

这组更适合：

- 团队本来就在 Google 工具链里
- 你更看重 Gemini 生态的一致性
- 但它不一定是这次 hackathon 最强默认解

## 各工具怎么分工

### `Cursor`

适合：

- Unity 客户端高频实现
- UI / state machine 小步迭代
- IDE 内局部重构
- 需要随时接管的开发节奏

官方点：

- `background agents`
- GitHub app + remote machine
- isolated VM

### `Claude Code`

适合：

- 终端内对整个 repo 做分析
- API、脚本、后端逻辑
- 批量修改、文档整理、release notes
- 可组合 shell workflow

官方点：

- terminal-first
- 可以 edit files / run commands / create commits
- `MCP` 可接更多外部数据源

### `Codex`

适合：

- 云端后台任务
- 并行文档、测试、修复
- 需要异步 delegation 的任务

官方点：

- cloud task
- sandboxed cloud container
- can work on many tasks in parallel

### `Windsurf`

适合：

- AI-native IDE 体验
- 喜欢 `Cascade` / memory / MCP / terminal 协同的团队
- 需要“上下文一直在线”的编辑器工作感

官方点：

- `Cascade`
- `Memories`
- `MCP`
- terminal / workflows / context awareness

### `Gemini Code Assist`

适合：

- IDE 内编码辅助
- agent mode
- 更看重 source citations
- 更贴近 Gemini / Google Cloud 生态

官方点：

- Gemini 2.5
- IDE assistance + agent mode
- source citations
- code customization（Enterprise）

## 对这次项目的实际建议

### 主工具只选 1 个

不要让团队同时把：

- `Cursor`
- `Windsurf`
- `Claude Code`
- `Codex`
- `Gemini Code Assist`

都当主工具。

最容易乱。

### 我建议的主次分配

- 主 IDE：`Cursor`
- 终端/仓库级补位：`Claude Code`
- 云端并行补位：`Codex`（可选）
- 内容与素材：`Google AI Studio`

## 对你这个角色最适合的用法

你作为中间件架构师 / 技术总监，最适合把工具这样分：

- 你自己拍板：玩法规则、score、fairness、scope
- `Cursor`：Unity 客户端和 UI 实现
- `Claude Code`：服务端、事件、日志、脚本、文档
- `Codex`：异步做不阻塞主线的子任务
- `Google AI Studio`：brief、copy、素材、旁白、宣传视频

## 一句话判断

不要问“哪个工具最强”。

更该问：

- 哪个是主 cockpit
- 哪个负责后台 delegation
- 哪个负责内容生成

## 资料

- [Cursor Background Agents](https://docs.cursor.com/en/background-agents)
- [Cursor GitHub integration](https://docs.cursor.com/en/github)
- [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Codex cloud](https://platform.openai.com/docs/codex)
- [Windsurf Docs](https://docs.windsurf.com/windsurf)
- [Gemini Code Assist overview](https://developers.google.com/gemini-code-assist/docs/overview)
- [Gemini Code Assist agent mode](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer)
