---
title: 记忆污染、Memory Poisoning 与自改进风险
type: topic
status: learning
tags:
  - ai/topic
  - ai/memory
  - ai/security
  - ai/self-improvement
created: 2026-03-29
updated: 2026-03-29
---

# 记忆污染、Memory Poisoning 与自改进风险

## 这页想解决什么

一旦 agent 允许把运行中的经验写入 memory、再 promotion 成 durable rules、甚至继续抽成 skill，风险就不再只是“回答错了一次”。

它会变成：

- 错误被长期保存
- 错误被跨 session 复用
- 错误被跨 agent 扩散
- 错误被包装成“系统自己的经验”

所以 `self-improving system` 最关键的前提，不是写得更快，而是 **污染不会轻易升级成永久行为**。

## 什么是 memory poisoning

这里说的 `memory poisoning`，不是只指训练阶段的数据投毒。

在 agent runtime 里，它更常见的形态是：

- 不可信内容诱导 agent 写下错误 memory
- 错误总结在 compaction / consolidation 时被“净化”成看起来合理的规则
- 跨 scope 的 shared memory 把局部经验误推广成团队默认
- 一次性 workaround 被 promotion 成 durable rule
- 未评测的 skill extraction 把污染变成 reusable method

## 为什么自改进系统更容易放大它

一条普通错误消息，最多污染一次回答。

但在 `learning -> promotion -> skill extraction` 这条链路里，同样的错误可能经历：

1. 被记录到 `.learnings/*`
2. 被 promotion 到 `MEMORY.md` / `AGENTS.md` / `TOOLS.md`
3. 被抽成 `SKILL.md`
4. 被更多 session、更多 agent、更多项目复用

这就是为什么这条线的核心不是“自动成长”，而是 **bounded self-improvement**。

## 5 类最常见的污染入口

### 1. 不可信检索结果 / 网页 / 邮件内容

这是最典型的 `indirect prompt injection` 场景。

agent 在读取网页、ticket、邮件、知识库或第三方 MCP 资源时，把其中的恶意 instruction 当成了可信指导，甚至把它写进后续 memory。

### 2. compaction 与 summary 失真

压缩上下文时，如果把“这条结论尚未验证”压缩成“结论成立”，就会让 uncertainty 消失。

这类污染不是来自外部攻击，而是来自整理过程本身。

### 3. shared memory scope 设计过宽

如果用户级、项目级、团队级、全局级 memory 没有清楚分层，局部经验会越界。

看起来像“记忆共享”，实际上更像“默认污染扩散”。

### 4. tool / plugin / MCP 元数据污染

工具不仅输出结果，也会带 prompt、schema、resource、tool description。

如果第三方扩展不可信，它既可能污染动作层，也可能污染记忆层。

### 5. skill extraction 过早升级

最危险的不是一条坏 learning，而是把它过早抽成 skill。

因为一旦进入 `SKILL.md`，它在新的 session 里会被读成“成熟方法”，而不再像一次事故记录。

## 更稳的治理原则

### `log first, promote later`

先记账，不要一出问题就改长期规则。

### `promotion before extraction`

先把模式 promotion 成可 review 的 rule，再决定值不值得做成 skill。

### `scope is a security boundary`

session、project、user、team、tenant 不是组织便利性问题，而是安全边界。

### `every write needs provenance`

一条 memory 必须能回答：

- 来自哪里
- 谁触发的
- 是否已验证
- 何时该失效

### `every durable change needs rollback`

promotion 和 skill extraction 都必须允许 demotion。

## 和几家系统的对应关系

- `OpenClaw`：强调 memory 写到 Markdown 文件才算真正持久化，`MEMORY.md` 只在 main private session 加载，这天然就是 boundary control。来源：[OpenClaw Memory](https://docs.openclaw.ai/concepts/memory)
- `Claude Code`：把 `CLAUDE.md` 和 auto memory 分开，scope 也分 project / user / org，以及 per working tree 的 auto memory。来源：[Claude Code Memory](https://code.claude.com/docs/en/memory)
- `LangMem / LangGraph`：强调 namespace，把 memory 放进明确的 store namespace，而不是一锅端共享。来源：[LangMem Memory Tools API](https://langchain-ai.github.io/langmem/reference/tools/)
- `ChatGPT agent`：为了减少 prompt injection 对 memory 的利用，在 system card 中明确写了 memory 在 launch 时被关闭。来源：[ChatGPT Agent System Card](https://cdn.openai.com/pdf/6bcccca6-3b64-43cb-a66e-4647073142d7/chatgpt_agent_system_card_launch.pdf)

## 推荐继续读

1. [[AI 记忆设计]]
2. [[自我进化与持续学习的记忆设计]]
3. [[从 Learnings 到 AutoSkill：技能自提炼]]
4. [[../07-Maps/Self-Improving Memory 风险与治理图|Self-Improving Memory 风险与治理图]]
5. [[../../AI-Engineering/07-Topics/共享记忆边界：用户、项目、多 Agent 与租户隔离|共享记忆边界：用户、项目、多 Agent 与租户隔离]]
6. [[../../AI-Engineering/07-Topics/自改进记忆的 Incident Library、Poisoning 与 Failure Cases|自改进记忆的 Incident Library、Poisoning 与 Failure Cases]]
7. [[../../AI-Engineering/07-Topics/自改进 Skill 的 Eval Gate、Release Gate 与 Rollback|自改进 Skill 的 Eval Gate、Release Gate 与 Rollback]]
