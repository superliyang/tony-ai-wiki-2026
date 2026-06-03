---
title: Delegation and Task-Oriented Agents
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent-runtime
  - ai/coding-agent
created: 2026-03-22
updated: 2026-03-28
---

# Delegation and Task-Oriented Agents

## 为什么这页需要补深

agent 产品正在从“协作式问答”走向“任务委托式执行”。

这不是换个说法，而是改变了整套系统设计：

- prompt 不再只是提示词，而是任务契约
- context 不再只是聊天历史，而是任务边界与执行条件
- 结果不再只是回答，而是可验收交付物

## 什么叫真正的 delegation

`Delegation` 的核心不是把一句话丢给模型，而是把一个可执行任务正式交给系统：

- 目标足够清晰
- 边界可控
- 结果可验收
- 失败可恢复
- 责任可追溯

所以 task-oriented agent 通常要求：

- explicit task contract
- environment ownership
- intermediate progress
- acceptance criteria
- review / handoff path

## 协作式 agent 和委托式 agent 的差别

### 协作式 agent 更像 pair partner

适合：

- 高频互动
- 连续修改
- 共同思考
- 人类始终在回路中

### 委托式 agent 更像可管理的 worker

适合：

- 目标明确的子任务
- 可以独立推进的工程工作
- 中途不需要频繁人工确认的任务

这也是为什么 `subagents`、`background agents`、`worker-style runtimes` 最近越来越重要。

## 一个好任务契约至少要写清楚什么

1. 目标：到底要交付什么
2. 范围：哪些文件 / 系统 / 数据能碰，哪些不能碰
3. 环境：在哪执行，本地还是云端，是否有工具限制
4. 约束：预算、时间、权限、质量门槛
5. 验收：什么结果算完成
6. handoff：交给谁 review、合并、继续执行

## 委托式 agent 最常见的任务模式

### implementation task

- 实现一个明确功能
- 典型交付物：patch、tests、文档

### investigation task

- 定位 bug、阅读代码、产出根因分析
- 典型交付物：结论、证据链、候选修复方案

### review task

- 做代码审查、风险识别、测试建议
- 典型交付物：review comments、风险清单

### maintenance task

- 清理、重构、升级、批量修改
- 典型交付物：批量变更、检查清单、回归建议

## 系统设计里最难的几个问题

### 1. 什么适合委托，什么不适合

不适合委托的通常是：

- scope 极其模糊
- 需要持续创意碰撞
- 高风险且每一步都需人类判断

### 2. 任务描述写到什么粒度

太粗：agent 会扩 scope。

太细：agent 只是在执行脚本，没有发挥价值。

### 3. 失败后如何恢复，而不是从头来过

好的 delegation 系统应该能保留：

- 已完成的中间产物
- 当前上下文
- 失败点
- 下一步建议

### 4. 结果怎么自然接回主流程

委托结果不应该成为孤立答案，而应该回到：

- review flow
- CI flow
- merge flow
- release flow

## 真实失败模式

### 1. 任务边界不清

agent 很容易自己扩 scope，最后做成“看起来努力，实际上偏题”。

### 2. 验收标准缺失

没有 acceptance criteria 时，系统只能用“差不多完成”来判断，质量很不稳。

### 3. 结果没人接

委托结果没有接进 review 或交付链路，最后就留在对话里吃灰。

### 4. 并行委托互相污染

多个任务同时跑，但写集不隔离、假设不一致，最后冲突放大。

## 学这一页最该形成的判断力

### 判断 1：当前是在协作，还是在委托

如果你需要频繁来回讨论，那还不是委托式任务。

### 判断 2：这个任务是否已经“可验收”

不能验收的任务，就很难安全委托。

### 判断 3：系统是否支持真正的 handoff

没有 handoff，delegation 就只是一次更长的回答。

## 推荐怎么连着读

1. [[Background Agents]]
2. [[Multi-Agent Coding Workflow]]
3. [[Session and Memory Design]]
4. [[Agent Runtime Architecture]]
5. [[Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]

## 相关主题

- [[Background Agents]]
- [[Multi-Agent Coding Workflow]]
- [[Session and Memory Design]]
- [[Agent Runtime Architecture]]
- [[Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]

## 资料

- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [OpenAI Background mode](https://developers.openai.com/api/docs/guides/background)
- [ADK State](https://google.github.io/adk-docs/sessions/state/)
- [ADK Technical Overview](https://google.github.io/adk-docs/get-started/about/)
