---
title: 能力升级线：Prompt、Context、RAG、Tool Use、Agent、Memory 与 Multi-Agent
type: topic
status: active
tags:
  - ai/topic
  - ai/capability-line
created: 2026-04-12
updated: 2026-04-13
---

# 能力升级线：Prompt、Context、RAG、Tool Use、Agent、Memory 与 Multi-Agent

> 这条线回答的是：
> `模型怎样从“会输出文字”一步步升级成“能完成任务的系统”。`

## 这条线为什么重要

很多人会把 [[提示词工程]]、[[RAG]]、[[Tool Use]]、[[Agent]]、[[Agent Memory]] 当成平行名词。

更好的理解方式是把它们放进一条能力升级链：

`Prompt -> Context -> Retrieval -> Tool Use -> Agent -> Memory -> Planning -> Multi-Agent`

只有放进这条链里，你才容易判断：

- 当前问题到底缺的是 prompt，还是缺 context
- 是该补 retrieval，还是该引入 tool
- 是该做单 agent，还是引入 workflow / planner
- memory 应该放在哪里，边界怎么管
- multi-agent 是真正有必要，还是只是把复杂度提前放大

## 一、Prompt：最早、最轻的控制面

核心页：

- [[提示词工程]]
- [[AI Assistant]]

Prompt 的作用是：

- 明确任务意图
- 规定输出结构
- 注入角色和约束
- 用少量自然语言控制模型行为

但 prompt 的边界也很明显：

- 它不能凭空创造缺失知识
- 它不能替代系统状态
- 它不能稳定解决复杂多步任务

所以 senior 视角里，prompt 是起点，不是终点。

## 二、Context：为什么系统开始比 prompt 更重要

核心页：

- [[上下文工程]]
- [[Long Context]]

当任务复杂度上升时，真正决定表现的往往不是 prompt 本身，而是：

- 给了什么上下文
- 上下文怎么组织
- 什么该进入上下文，什么不该
- 上下文污染、冲突和长度如何控制

这就是为什么很多团队后来会从“prompt engineering”转向“context engineering”。

更专业的说法是：

`我们不只是写提示词，而是在设计模型的工作内存。`

## 三、RAG：把事实源从参数里部分外置

核心页：

- [[RAG]]
- [[Evaluation]]

RAG 解决的不是所有问题，而是一个很明确的问题：

`当事实变化快、语料私有、上下文必须可追溯时，不能只依赖模型参数。`

RAG 的价值在于：

- 提供更可控的事实来源
- 降低 hallucination 风险
- 提升企业知识、文档问答、客服、运营等场景的可用性

但它的代价也很现实：

- retrieval 质量决定上限
- chunking / indexing / ranking 影响大
- 引入额外延迟、成本和调试复杂度

所以 RAG 不是“模型不够强的补丁”，而是“事实治理层”的一种设计。

## 四、Tool Use：从回答问题变成操作世界

核心页：

- [[Tool Use]]
- [[MCP（Model Context Protocol）]]
- [[Agent 动作面：Tools、CLI、MCP、Browser 与 Apps]]

当模型开始调工具，系统发生质变：

- 从生成答案，变成执行动作
- 从封闭推断，变成调用外部能力
- 从“知道”走向“做到”

这一步之后，判断重点变成：

- 什么时候该调工具
- 调哪个工具
- 参数是否安全
- 权限和审批如何控制
- 失败后是否能恢复

所以 tool use 的关键不只是 schema，而是 action policy。

## 五、Agent：让模型承担多步任务编排

核心页：

- [[Agent]]
- [[Planning and Control]]
- [[从提示词到 Harness：Agent 能力的渐进式主线]]

Agent 的本质不是“一个更酷的 chatbot”，而是：

- 能理解目标
- 能做多步决策
- 能在步骤之间维护状态
- 能根据反馈继续推进

你可以把它理解成：

`Tool Use 是单步动作能力，Agent 是把动作串成任务闭环的能力。`

真正的 agent 系统通常还会涉及：

- planner / executor 分层
- approval / guardrails
- retry / fallback / rollback
- eval / release gate

## 六、Memory：为什么很多任务不能只靠当前会话

核心页：

- [[Agent Memory]]
- [[AI 记忆设计]]
- [[大模型记忆、项目记忆与 Chat Memory]]

Memory 的价值在于跨回合、跨任务、跨项目保存有用状态。

但这里非常容易混淆：

- `context` 是当前任务工作内存
- `RAG` 是外部事实检索
- `memory` 是长期状态与经验沉淀

如果这三个边界不清楚，系统很容易变成：

- 所有东西都塞进 prompt
- 所有东西都做成检索
- 所有东西都试图长期记住

结果就是复杂度高、可控性差、污染风险大。

## 七、Planning：为什么强 agent 不等于强规划

核心页：

- [[Planning and Control]]
- [[Coding Agents]]

很多系统表面像 agent，但其实只有：

- prompt
- tool call
- 少量循环

真正进入 `planning` 层后，才会开始出现：

- 任务拆解
- 子目标管理
- 中间状态审查
- 失败路径切换
- 长任务推进

这也是为什么 coding agent、computer use、复杂 enterprise workflow 往往会把 planning 放到更高优先级。

## 八、Multi-Agent：什么时候真的值得上多 Agent

核心页：

- [[Multi-Agent Systems]]
- [[A2A（Agent-to-Agent）与协作协议]]

Multi-agent 真正有价值的场景通常是：

- 角色天然分工明显
- 单 agent 上下文负担太大
- 不同步骤的工具、权限、评测标准不同
- 需要并行探索或互相审查

它不该被当成默认升级路径，因为它也会带来：

- 协调复杂度
- 状态一致性问题
- 成本放大
- 调试困难

所以更稳的判断往往是：

`先把单 agent 做稳，再看是否值得引入多 agent。`

## 九、这条线最容易混淆的边界

### 1. Prompt vs Context

- prompt 是控制指令
- context 是任务材料与状态

### 2. RAG vs Memory

- RAG 更像事实源与外部知识访问
- memory 更像长期状态与经验沉淀

### 3. Tool Use vs Agent

- tool use 是单步动作
- agent 是多步任务闭环

### 4. Agent vs Workflow

- 有些问题更适合显式 workflow，而不是把全部控制交给 agent

### 5. Single Agent vs Multi-Agent

- 不是层级越多越高级，而是边界越清楚越可靠

## 十、建议学习顺序

1. [[提示词工程]]
2. [[上下文工程]]
3. [[RAG]]
4. [[Tool Use]]
5. [[MCP（Model Context Protocol）]]
6. [[Agent]]
7. [[Planning and Control]]
8. [[Agent Memory]]
9. [[AI 记忆设计]]
10. [[Multi-Agent Systems]]
11. [[A2A（Agent-to-Agent）与协作协议]]
12. [[Coding Agents]]
13. [[Browser Agents 与 Computer Use]]

## 十一、这条线在面试里能回答什么

- 为什么仅靠 prompt engineering 不足以做复杂 AI 系统
- 你如何区分 context、RAG、memory 的职责边界
- 什么情况下应该上 tool use、agent、multi-agent
- 你如何判断一个 agent 系统是“看起来聪明”还是“真的可交付”

## 关联

- [[AI 五条主干专家工作台]]
- [[AI 领域知识点总纲：点、线、面与层]]
- [[AI 主题索引]]
- [[../07-Maps/AI 知识点点线面图|AI 知识点点线面图]]
- [[提示词工程]]
- [[上下文工程]]
- [[RAG]]
- [[Tool Use]]
- [[Agent]]
- [[Agent Memory]]
- [[Multi-Agent Systems]]
