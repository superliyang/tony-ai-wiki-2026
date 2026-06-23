---
title: 从 Learnings 到 AutoSkill：技能自提炼
type: topic
status: learning
tags:
  - ai/topic
  - ai/agent
  - ai/memory
  - ai/skills
  - ai/self-improvement
created: 2026-03-29
updated: 2026-03-29
---

# 从 Learnings 到 AutoSkill：技能自提炼

## 这页想解决什么

很多人一说 `self-improving agent`，很容易直接跳到“模型会自己长技能”。

但从工程上看，更稳、也更可交付的路径其实是：

1. 先捕获 learnings
2. 再筛选哪些值得 promotion
3. 再把极少数真正稳定的模式提炼成 reusable skill

也就是说，这页讨论的不是神话式自进化，而是：

`从经验日志到 durable rules，再到 skill extraction 的工程路径。`

## 先把 4 层对象分清

### 1. `learning entry`

一条经验、错误、纠正、功能诉求。

它强调：

- 原始上下文
- 原因与修复
- 是否 recurring
- 是否已验证

### 2. `promoted rule`

从 learning 中提炼出来的长期规则。

它可能进入：

- `AGENTS.md`
- `TOOLS.md`
- `SOUL.md`
- `CLAUDE.md`
- 其他项目级 instruction files

### 3. `skill`

当某种模式足够稳定、广泛、可复用，才值得抽成 skill。

它强调：

- 自包含
- 可被其他任务复用
- 不依赖原始事故上下文
- 能明确教会 agent 一套方法

### 4. `plugin / app / automation`

再往上一层，才是把 skill 变成插件、应用能力或自动化工作流。

所以 skill 不是最高层，只是“复用工作方法”的一个中间层。

## 一条更稳的自提炼路径

### 第 1 步：记录 learnings

不要一有想法就写 skill。

先记：

- 这件事到底发生了什么
- 为什么不显而易见
- 是否已经验证
- 会不会重复出现

### 第 2 步：做 promotion

如果一条经验已经可以提升团队或 agent 的默认行为，就先 promotion 到项目规则或 workspace rules。

这里的重点是：

- 优先做 rule promotion
- 不要一上来就做 skill extraction

### 第 3 步：筛 skill 候选

只有当一条模式满足这些条件时，才考虑变成 skill：

- recurring
- verified
- non-obvious
- broadly applicable
- user-flagged

这组条件很重要，因为它天然在阻止“把一次性补丁包装成 skill”。

### 第 4 步：做质量门槛

一个合格 skill 至少要满足：

- 没有硬编码项目细节
- 目标明确
- 输入输出边界清楚
- 能在新的 session 里独立理解
- 能被验证

### 第 5 步：评测和 release gate

skill 提炼后，不能直接当成永久真理。

还要看：

- 是否真的减少重复错误
- 是否污染 context
- 是否和现有 skill 冲突
- 是否引入新的误导

## 为什么这条线和 OpenClaw 很合拍

`OpenClaw` 很适合这件事，因为它已经有：

- durable workspace files
- hooks
- sessions
- skills
- ClawHub

这让“learning -> promotion -> skill extraction”很容易找到明确落点。

## 为什么这条线不只属于 OpenClaw

虽然 `Self-Improving-Agent` 是在 `OpenClaw` 生态里很具体地做出来的，但这条路径本身并不只属于 OpenClaw。

它同样可以映射到：

- `Claude Code` 的 project memory + hooks
- `Codex` 的 reusable skills / harness workflows
- `LangMem` 的 memory pipeline
- 自己做的 agent runtime / internal SDK

所以它其实是一个很值得单独学习的抽象主题。

## 这条线最容易踩的坑

- 把未验证的经验直接 promotion
- 把 project-specific workaround 抽成 supposedly reusable skill
- 没有 provenance
- 没有 forgetting / demotion 机制
- 没有对 skill extraction 做评测

## 更稳的一句话理解

`AutoSkill` 最值得学的，不是“自动”，而是“升级路径有没有 discipline”。

## 推荐继续读

1. [[AI 记忆设计]]
2. [[自我进化与持续学习的记忆设计]]
3. [[../09-Systems/OpenClaw 的准自进化工作流|OpenClaw 的准自进化工作流]]
4. [[../09-Systems/Self-Improving-Agent（ClawHub Skill）|Self-Improving-Agent（ClawHub Skill）]]
5. [[../../AI-Engineering/07-Topics/Learnings、Promotion 与 Skill Extraction Pipeline|Learnings、Promotion 与 Skill Extraction Pipeline]]
6. [[../../AI-Engineering/06-Projects/Memory Lab/Self-Improving-Agent 与 AutoSkill 实验|Self-Improving-Agent 与 AutoSkill 实验]]
