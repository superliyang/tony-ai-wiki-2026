---
title: Codex Skills 与 Plugins
type: system
status: learning
tags:
  - ai/system
  - ai/agent
  - ai/coding-agent
  - ai/plugins
  - ai/skills
  - organization/openai
created: 2026-03-31
updated: 2026-04-03
---

# Codex Skills 与 Plugins

## 为什么这一层值得单独记

如果只把 `Codex` 理解成一个会调用工具的 coding agent，会漏掉一个很关键的扩展面：

- `skills`
- `plugins`
- `hooks`
- `apps`
- `automations`

其中最值得拆开的两层就是：

- `skills`：方法与资源的复用层
- `plugins`：安装、启用、hooks、脚本编排和更稳定壳层

在本地 `self-improving-memory-lab` 实验里，我们后续还把 marketplace policy 调成了 `INSTALLED_BY_DEFAULT`，因为仅仅“出现在 marketplace”并不能保证当前 session 不会落在 `plugin is not installed`。

## `skill` 和 `plugin` 分别是什么

### `skill`

`skill` 更像：

- instruction bundle
- references
- helper scripts
- narrow methodology

它最适合承载：

- 工作方法
- promotion rubric
- eval gate
- rollback discipline
- 领域学习路径

在我们本地环境里，典型落点是：

- `/Users/tony/.codex/skills/self-improving-learning-ledger`
- `/Users/tony/.codex/skills/knowledge-vault-research-sync`
- `/Users/tony/.codex/skills/ai-agent-learning-system`

### `plugin`

`plugin` 更像：

- packaging layer
- capability enablement layer
- hook orchestration layer
- installation / discovery layer

它最适合承载：

- `.codex-plugin/plugin.json`
- `hooks.json`
- `skills/`
- `scripts/`
- 以后可能再加 `mcp` / `apps`

在我们本地环境里，最具体的样本就是：

- `/Users/tony/plugins/self-improving-memory-lab`

## 在本机上它们怎么接起来

### 技能侧

- 本地 skill 目录：`/Users/tony/.codex/skills`
- plugin bundled skill cache：
  - `/Users/tony/.codex/plugins/cache/tony-local/self-improving-memory-lab/local/skills/self-improving-learning-ledger`

### 插件侧

- 本地 marketplace：
  - `/Users/tony/.agents/plugins/marketplace.json`
- 本地插件源码：
  - `/Users/tony/plugins/self-improving-memory-lab`
- 已安装路径兼容层：
  - `/Users/tony/.agents/plugins/plugins/self-improving-memory-lab`
- Codex 启用配置：
  - `/Users/tony/.codex/config.toml`

## 安装态和运行态不是一回事

对 plugin 来说，至少要区分：

- listed in marketplace
- installed for the session
- loaded by runtime
- hooks actually fired

这也是我们为什么后来开始单独记录：

- `AVAILABLE` 和 `INSTALLED_BY_DEFAULT` 的差别
- live cache 与 source path 的差别
- skill 被发现和 hook 真触发的差别

## 我们这次最重要的一个认识

`skill` 不是 `plugin` 的低配版，`plugin` 也不是 `skill` 的替代品。

更准确地说：

- `skill` 负责方法
- `plugin` 负责壳层
- `hooks` 负责事件入口
- `scripts` 负责稳定动作

所以更稳的路线通常不是：

- 直接造一个很自动的 plugin

而是：

1. 先把方法收成 `skill`
2. 再把 hooks / orchestration 包成 `plugin`
3. 最后才考虑更自动的 rollout

## 我们这次本地实验对应到什么

### `skill`

- `self-improving-learning-ledger`
  - 负责：
    - learnings
    - promotion review
    - candidate skill stub
    - eval gate
    - rollback discipline

### `plugin`

- `self-improving-memory-lab`
  - 负责：
    - `UserPromptSubmit`
    - `PostToolUse`
    - shadow review
    - consolidation review
    - manual verification
    - incident pack replay

## 什么时候优先研究这一层

- 你想理解 `Codex` 为什么不只是终端里的模型
- 你想做本地 plugin / skill 实验
- 你想研究 `self-improving workflow` 怎么做得可控、可回滚
- 你想把 `skills + plugins + hooks + scripts` 做成一个更像 harness 的系统

## 推荐继续读

- [[Codex]]
- [[self-improving-learning-ledger 技能]]
- [[Self-Improving Memory Lab Plugin]]
- [[../../AI-Engineering/07-Topics/Plugin 安装、发现与 Runtime Reality|Plugin 安装、发现与 Runtime Reality]]
- [[Self-Improving-Agent（ClawHub Skill）]]
- [[OpenClaw 的技能、插件、应用与自动化生态]]
- [[../../AI-Engineering/07-Topics/技能、插件、应用与自动化：Harness 的扩展面|技能、插件、应用与自动化：Harness 的扩展面]]
- [[../../AI-Engineering/07-Topics/Learnings、Promotion 与 Skill Extraction Pipeline|Learnings、Promotion 与 Skill Extraction Pipeline]]
- [[../../AI-Engineering/06-Projects/Memory Lab/Self-Improving Memory Lab 插件实战|Self-Improving Memory Lab 插件实战]]
