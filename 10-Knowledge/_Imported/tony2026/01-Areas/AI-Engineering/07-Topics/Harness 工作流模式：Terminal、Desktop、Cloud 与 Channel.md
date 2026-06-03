---
title: Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/harness
  - ai/workflow
created: 2026-03-28
updated: 2026-03-28
---

# Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel

## 为什么要按工作流模式来理解 harness

很多人问“哪个 agent 最强”，但从 `Harness Engineering` 视角看，更好的问题通常是：

- 它的主工作入口是什么
- 它把人放在什么位置
- 它更适合 repo、browser、desktop 还是 message channels
- 它的自动化和治理边界在哪里

所以这页不按厂商宣传词分类，而按更稳定的 4 种工作流模式来整理：

- `terminal-first`
- `desktop / browser-first`
- `cloud-first`
- `channel-first`

## 1. Terminal-first

这类 harness 的默认假设是：

- 用户就在 repo 和 shell 里工作
- diff、命令、日志、测试是第一现场
- 人机协作更像 pair programming

典型代表：

- `Claude Code`
- `Gemini CLI`
- `Codex CLI`

这条模式通常最强在：

- repo 理解
- shell 操作
- patch / review / commit loop
- local feedback 快

它的风险也很清楚：

- 对非工程用户不够友好
- 权限边界容易和本机环境纠缠
- 很多可视化上下文不如 desktop-first 直观

## 2. Desktop / Browser-first

这类 harness 的默认假设是：

- 任务很多发生在网页、桌面应用和图形界面中
- agent 需要“看见页面”和“代替人点击”
- human takeover、approval、interruption 很关键

典型代表：

- `ChatGPT agent`
- OpenAI `computer_use`
- Anthropic `computer use`
- `OpenClaw` 的 macOS app / WebChat / nodes

它的强项在：

- 跨工具工作流
- 处理没有正式 API 的界面
- 更贴近真实办公和浏览器任务

它的代价则是：

- 速度慢于直接 API / shell
- 需要更严格的安全隔离和录屏式可回放能力
- UI 变化会让稳定性下降

## 3. Cloud-first

这类 harness 的默认假设是：

- agent 可以在服务器端或云端长期运行
- 人不一定守在会话前面
- session、artifacts、logs、replay 和 background execution 是一等公民

典型代表：

- `Codex app` / cloud tasks / `App Server`
- `Grok Agent Tools API`
- 一部分 `ChatGPT agent` 的托管工作流

它的强项在：

- 长时任务
- server-side observability
- 更容易做 org-level governance

它的代价是：

- 本地上下文接入更难
- user trust boundary 更敏感
- 如果产品没有设计好 replay / approval，就更容易黑箱化

## 4. Channel-first

这类 harness 的默认假设是：

- agent 不一定活在 IDE 或网页里
- 它可能活在聊天渠道、通知流、机器人入口或多端 companion 里
- 关键是“进入用户原本就在的地方”

典型代表：

- `OpenClaw` 的 nodes / WebChat / mobile surfaces
- `ChatGPT` 的 apps / connectors / MCP connectors
- 各类 bot / webhook / channel adapter 形态

这类模式强在：

- 分发自然
- 更适合个人 assistant 或团队协作入口
- 能把自动化结果推回日常工作流

但它也容易遇到：

- 上下文切碎
- 能力表面太多，治理复杂度变高
- channel UX 很容易弱于专门 app

## 一张对比表

| 模式 | 典型代表 | 最适合 | 最怕什么 |
| --- | --- | --- | --- |
| `terminal-first` | `Claude Code`、`Gemini CLI`、`Codex CLI` | coding、repo 工作、快速 patch loop | 非工程用户、视觉任务、权限泄漏 |
| `desktop / browser-first` | `ChatGPT agent`、OpenAI / Anthropic `computer use`、`OpenClaw` apps | 跨网页工具任务、office workflow、GUI automation | UI 脆弱、速度慢、安全边界模糊 |
| `cloud-first` | `Codex app`、`App Server`、`Grok Agent Tools API` | 长时任务、后台任务、组织级治理 | 本地上下文弱、黑箱感强 |
| `channel-first` | `OpenClaw` nodes、apps / connectors、bots | assistant 分发、异步协作、通知回路 | 上下文碎片化、体验不连贯 |

## 学 Harness 时最值得记住的判断

1. 先判断任务在哪个工作流模式里最自然。
2. 再判断该模式下动作面是什么：`CLI`、`browser`、`computer`、`MCP`、`SDK`。
3. 最后再看厂商具体实现好不好。

所以真正稳定的比较方式不是：

`谁更像 AGI`。

而是：

`谁把哪一种工作流模式做得最顺。`

## 关联

- [[Harness Engineering]]
- [[MCP 与 CLI 模式]]
- [[Computer Use Runtime and Safety]]
- [[技能、插件、应用与自动化：Harness 的扩展面]]
- [[Hooks、Cron、CI 与 Background Agents：Harness 自动化闭环]]
- [[Harness 工程案例：Codex、Claude Code、OpenClaw、Gemini CLI]]
- [[../08-Maps/Harness 工作流与自动化模式图|Harness 工作流与自动化模式图]]
- [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/Gemini CLI|Gemini CLI]]
- [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]
- [[../../AI-Learning/09-Systems/Grok Agent Tools API|Grok Agent Tools API]]

## 资料

- [ChatGPT agent](https://help.openai.com/en/articles/11752874-chatgpt-agent)
- [Developer mode and full MCP connectors in ChatGPT beta](https://help.openai.com/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt-beta)
- [Computer use | OpenAI API](https://platform.openai.com/docs/guides/tools-computer-use)
- [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Anthropic computer use](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [OpenClaw Platforms](https://docs.openclaw.ai/platforms)
- [OpenAI Codex app](https://openai.com/index/introducing-the-codex-app/)
- [Grok 4.1 Fast and Agent Tools API](https://x.ai/news/grok-4-1-fast/)
