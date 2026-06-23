---
title: Agent 动作面：Tools、CLI、MCP、Browser 与 Apps
type: topic
status: learning
tags:
  - ai/topic
  - ai/agent
  - ai/tools
  - ai/cli
  - ai/mcp
created: 2026-04-03
updated: 2026-04-03
---

# Agent 动作面：Tools、CLI、MCP、Browser 与 Apps

## 这页解决什么混乱

很多 agent 讨论会把 `tool use`、`CLI`、`MCP`、`browser/computer use`、`apps/connectors` 混成同一个概念。

更稳的理解是：

- `tool` 是最小动作能力
- `CLI / MCP / browser / apps` 是不同动作面
- 成熟系统通常不是只选一个，而是组合使用

## 一条最实用的分层

### Tool

最基础的动作单元。

它回答的是：

- 模型可以调用什么能力
- 参数和返回值长什么样
- 调用失败后怎样重试或恢复

所以 `tool` 更像动作接口，而不是完整工作面。

### CLI

`CLI` 是最强的本地动作面。

适合：

- repo-local coding
- 脚本执行
- 文件批处理
- shell-native 运维动作

优点：

- 覆盖面广
- 对开发者任务表达力强
- 易于和现有脚本生态衔接

代价：

- 权限容易过大
- 输出不总是结构化
- 对非开发任务不够友好

### MCP

`MCP` 是协议化动作面。

适合：

- 团队共享集成
- 统一 tool contract
- 通过 server 暴露能力
- 跨 agent / 跨客户端复用

优点：

- 结构化
- 可复用
- 便于治理和发布

代价：

- 前期定义成本更高
- 并不天然替代 CLI

### Browser / Computer Use

这是 UI 动作面。

适合：

- SaaS 页面
- 没有 API 的后台
- 桌面或网页界面操作

优点：

- 能触达没有正式接口的系统
- 更接近最终用户路径

代价：

- 脆弱
- 页面变化会影响稳定性
- 安全与审批要求更高

### Apps / Connectors

这是业务接入面。

适合：

- GitHub、Notion、Google Drive 这类标准产品接入
- 提供更稳定的业务对象模型
- 降低浏览器自动化的脆弱性

优点：

- 更像产品级入口
- 语义更清晰
- 通常更可审计

代价：

- 覆盖范围受制于平台
- 不一定能做所有 UI 细节

## 真正成熟的系统怎么选

通常不是“选边站”，而是：

- `CLI` 负责 repo-local 和 shell-heavy 动作
- `MCP` 负责共享协议化集成
- `browser` 负责 UI-only 场景
- `apps/connectors` 负责成熟业务入口

所以问题不该是：

- `CLI` 好还是 `MCP` 好

而该是：

- 这类任务最适合暴露成哪种动作面
- 哪些动作面应该组合使用
- 哪些动作需要更强的 release gate

## 学这条子域时最该比较的维度

- 表达力
- 稳定性
- 权限边界
- 可观察性
- 团队复用性
- 与 harness 的耦合方式

## 推荐继续读

- [[Tool Use]]
- [[MCP（Model Context Protocol）]]
- [[Browser Agents 与 Computer Use]]
- [[../../AI-Engineering/07-Topics/MCP 与 CLI 模式|MCP 与 CLI 模式]]
- [[../../AI-Engineering/07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]]
- [[../../AI-Engineering/07-Topics/动作面设计：Tools、CLI、MCP、Browser、Desktop 与 Channel|动作面设计：Tools、CLI、MCP、Browser、Desktop 与 Channel]]
- [[从提示词到 Harness：Agent 能力的渐进式主线]]
