---
title: 长期运行 Agent 的记忆系统
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/memory
  - ai/long-running
created: 2026-03-25
updated: 2026-03-29
---

# 长期运行 Agent 的记忆系统

## 为什么这层要单独拆出来

`Session and Memory Design` 解决的是记忆边界。

`Long-Running Agent Operations` 解决的是长期运行的节律和治理。

但当 agent 真开始跨天、跨任务、跨用户持续工作时，真正最容易出问题的是：

- 记忆写入策略
- 记忆压缩与纠偏
- thread state 和 long-term memory 的边界
- memory pollution 和权限泄漏

所以这一层值得单独拆出来。

## 你要先区分哪几类记忆

### `thread / working memory`

- 当前任务窗口内的状态
- 通常跟随线程、session、checkpoint
- 更像短期上下文和中间状态

### `semantic memory`

- 稳定事实、偏好、配置、知识
- 例如用户偏好、系统约束、组织规则

### `episodic memory`

- 过去发生过什么任务、用了什么策略、结果如何
- 更像经验记录和案例回放

### `procedural memory`

- 系统自己稳定化出来的做事方式
- 例如工具调用顺序、默认检查清单、偏好的执行模板

## 真正的工程难点

- 不是“能不能存”，而是“该不该存”
- 不是“检索出来”，而是“什么时候拉回、拉多少、会不会污染当前任务”
- 不是“长期保留”，而是“怎么纠错、过期、撤销、审计”

## 两种写入路径

### `hot-path writes`

- 在任务执行过程中立即写入
- 优点是更新及时
- 缺点是 latency 和污染风险高

### `background consolidation`

- 先记 trace / transcript，再后台抽取长期记忆
- 优点是更稳、更容易审计
- 缺点是时效性稍差

一个成熟系统通常不会只选一种，而是两者结合。

## 常见设计模式

- `checkpoint + replay`：把 thread state 当主要恢复来源
- `memory namespace`：按用户、项目、组织、agent 分层隔离
- `summary + raw trace`：压缩摘要用于热路径，原始轨迹用于审计
- `write policy`：不是每条信息都允许模型直接写入 durable memory
- `human correction`：高价值记忆要允许人工修正和撤销

## 为什么很多系统会记忆失控

- 把聊天历史误当长期记忆
- 没有 namespace，导致不同任务相互污染
- 没有 forgetting / invalidation 机制
- agent 自己写入太自由，慢慢积累错误事实
- 只管 recall，不管 provenance

## 长期运行系统里最重要的 5 个问题

1. 这条信息是 `thread state` 还是 `durable memory`？
2. 这条记忆谁有权限写入和读取？
3. 这条记忆如何纠错、撤回、过期？
4. 这条记忆为什么会被检索回来？
5. 这条记忆是否真的提升了任务质量，而不是增加噪声？

## 和 A2A / 多 Agent 的关系

一旦系统进入 multi-agent 或 A2A，记忆问题会更复杂：

- 共享哪些记忆
- 共享的是事实、任务状态还是 artifact
- 哪些只允许本地 agent 持有
- 哪些要通过协议显式传递，而不是靠隐式共享

## 推荐继续往下读

- [[Session and Memory Design]]
- [[记忆架构：State、Memory、Artifact 与 Context]]
- [[记忆写入、召回、压缩与 Consolidation]]
- [[记忆评测、污染、遗忘与纠偏]]
- [[Long-Running Agent Operations]]
- [[A2A 与 Multi-Agent Coordination]]
- [[Agent Security、Sandbox 与 Approval Architecture]]
- [[../../AI-Learning/06-Topics/Agent Memory|Agent Memory]]

## 相关

- [[Session and Memory Design]]
- [[Long-Running Agent Operations]]
- [[A2A 与 Multi-Agent Coordination]]
- [[../08-Maps/Agent 协作、记忆与信任边界图|Agent 协作、记忆与信任边界图]]
