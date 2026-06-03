---
title: Self-Improving-Agent（ClawHub Skill）
type: system
status: learning
tags:
  - ai/system
  - ai/openclaw
  - ai/agent
  - ai/memory
  - ai/skills
  - ai/self-improvement
created: 2026-03-29
updated: 2026-03-29
---

# Self-Improving-Agent（ClawHub Skill）

## 这页先把边界说清楚

`Self-Improving-Agent` 不是目前 `OpenClaw` 核心文档里一个一等公民的内置模块名。更准确地说，它是 `ClawHub` 上的一个 community skill，用 `OpenClaw` 已有的 `workspace + hooks + memory + skills + sessions` 能力，拼出一条“可控自改进”工作流。

这点非常重要，因为它决定了我们研究它时，不应该把它理解成“OpenClaw 已经自带 AutoSkill 内核”，而应该理解成：

- `OpenClaw core` 提供底座
- `Self-Improving-Agent` 在这个底座上实现 learnings、promotion、skill extraction

## 它到底在做什么

这条 skill 的核心不是“模型自己学会了新能力”，而是把运行中的经验沉淀成显式文件，然后把高价值经验逐步升级。

它默认关注三类日志：

- `.learnings/LEARNINGS.md`
- `.learnings/ERRORS.md`
- `.learnings/FEATURE_REQUESTS.md`

这些文件记录：

- 非显而易见的经验
- 错误与修复
- 用户反复提出的能力诉求

然后再根据适用范围，把内容升级到更稳定的工作文件：

- `AGENTS.md`
- `TOOLS.md`
- `SOUL.md`
- 在其他 agent 环境里也可能是 `CLAUDE.md`、`.github/copilot-instructions.md`

## 为什么它在 OpenClaw 里成立

因为 `OpenClaw` 本身已经有这些底座：

- workspace 中的规则文件和 durable memory
- `Skills` 的加载、优先级和覆盖规则
- `ClawHub` 作为安装与分发入口
- `Hooks` 做事件触发
- `sessions_*` 工具做跨 session 传递

也就是说，`Self-Improving-Agent` 并不是把“自我进化”做成一团黑箱，而是把这条链路拆成可见的系统对象。

## 一条最实用的工作流

### 1. 捕获 learning

任务中出现：

- 错误
- 用户纠正
- 新的 project convention
- 更好的处理模式

先写入 `.learnings/`。

### 2. 做分类与状态管理

skill 页面给了比较细的条目格式：

- `Priority`
- `Status`
- `Area`
- `Source`
- `Related Files`
- `See Also`
- `Pattern-Key`
- `Recurrence-Count`

这让它不只是记流水账，而更像可检索、可升级的 learning ledger。

### 3. 升级到 durable workspace rules

当一条 learning 已经验证、并且跨任务都有价值时，才推广到：

- `AGENTS.md`：流程和工作方法
- `TOOLS.md`：工具使用坑点
- `SOUL.md`：行为原则
- 其他 agent 文件：项目约束与长期规则

### 4. 再进一步抽成 skill

Skill 页面明确提到 `Automatic Skill Extraction`：

- recurring
- verified
- non-obvious
- broadly applicable
- user-flagged

满足这些条件时，可以用 helper 把 learning 抽成新的 `skill`。

## 这是不是 AutoSkill

如果你说的 `AutoSkill` 指的是“系统自动把高价值经验提炼成复用 skill”，那它在这条 skill 里确实有非常明确的实现方向。

但如果你说的是“OpenClaw 官方核心里有个正式模块就叫 AutoSkill”，我目前没有查到官方文档证据。

更稳的表述是：

`Self-Improving-Agent` 提供了一条从 learnings 到 skill extraction 的 workflow。

## 为什么它很值得学

因为它把很多人嘴里的“自进化 agent”落到了真正能讨论的工程面：

- 日志格式
- 提升条件
- 目标文件
- hook 触发
- 跨 session 传播
- skill quality gate

这让我们可以把“自我进化”从 hype 拉回到：

`memory-driven self-maintenance + controlled skill promotion`

## 风险点

### 1. 经验污染

如果把错误结论写进 `.learnings/`，后续 promotion 就会把污染扩大。

### 2. 过早 promotion

一条只在单次任务中有效的 workaround，不应该被提升成 `AGENTS.md` 或 skill。

### 3. prompt injection / adversarial contamination

如果不对来源做治理，恶意输入也可能被当成“学习成果”沉淀下来。

### 4. skill 抽取后缺乏评测

能跑出一个 `SKILL.md` 并不等于它真的稳定、泛化、可复用。

## 它和别的系统怎么比较

- `OpenClaw`：更适合把 learnings、workspace files、hooks、skill extraction 串成一个 self-hosted operating layer
- `Claude Code`：更适合 project memory、hooks、repo-local conventions，但 skill promotion 更偏工程团队工作流
- `Codex`：更适合从 task/workbench/harness 角度做 reusable workflows，不一定把 durable learnings 明确做成 `.learnings/`
- `LangMem`：更像 memory pipeline 抽象，而不是 workspace-native skill promotion 系统

## 推荐继续读

- [[OpenClaw]]
- [[OpenClaw 的准自进化工作流]]
- [[OpenClaw 的分层记忆设计]]
- [[../06-Topics/从 Learnings 到 AutoSkill：技能自提炼|从 Learnings 到 AutoSkill：技能自提炼]]
- [[../../AI-Engineering/07-Topics/Learnings、Promotion 与 Skill Extraction Pipeline|Learnings、Promotion 与 Skill Extraction Pipeline]]
- [[../../AI-Engineering/07-Topics/记忆评测、污染、遗忘与纠偏|记忆评测、污染、遗忘与纠偏]]
- [[../../AI-Engineering/06-Projects/Memory Lab/Self-Improving-Agent 与 AutoSkill 实验|Self-Improving-Agent 与 AutoSkill 实验]]

## 官方资料

- [Self Improving Agent — ClawHub](https://clawhub.ai/skills/self-improvement)
- [OpenClaw Hooks](https://docs.openclaw.ai/automation/hooks)
- [OpenClaw Memory](https://docs.openclaw.ai/concepts/memory)
- [OpenClaw Skills](https://docs.openclaw.ai/tools/skills)
- [OpenClaw ClawHub](https://docs.openclaw.ai/tools/clawhub)
