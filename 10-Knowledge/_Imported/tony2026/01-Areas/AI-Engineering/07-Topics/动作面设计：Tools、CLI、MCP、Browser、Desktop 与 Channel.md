---
title: 动作面设计：Tools、CLI、MCP、Browser、Desktop 与 Channel
type: topic
status: learning
tags:
  - ai/engineering
  - ai/tools
  - ai/cli
  - ai/mcp
  - ai/browser
created: 2026-04-03
updated: 2026-04-03
---

# 动作面设计：Tools、CLI、MCP、Browser、Desktop 与 Channel

## 为什么动作面要单独设计

agent 一旦开始真正行动，工程问题就不再只是“有没有 tool calling”。

更重要的是：

- 通过什么表面行动
- 这个表面稳定不稳定
- 权限和审批怎么卡
- 结果是否可观察、可回放

## 六类最常见动作面

### Tools

最小动作单位。

### CLI

最适合：

- repo-local
- shell-native
- 批量脚本

### MCP

最适合：

- shared integration
- team reuse
- protocolized capability

### Browser

最适合：

- UI-only SaaS
- 没有稳定 API 的路径

### Desktop

最适合：

- 本地 app
- 文件系统与 GUI 混合操作

### Channel

最适合：

- Slack / Feishu / email 这类 channel-first workflow
- 把 agent 能力嵌进沟通入口

## 设计动作面时最该问的 5 个问题

1. 这是不是最稳定的表面
2. 权限是不是过大
3. 输出是否可结构化
4. 失败后是否能恢复或回放
5. 是否值得从 browser 升级到 MCP/app

## 推荐继续读

- [[MCP 与 CLI 模式]]
- [[Computer Use Runtime and Safety]]
- [[Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
- [[Harness 真实工作流对照：Repo、Browser、Recurring Ops 与 Channel]]
- [[../../AI-Learning/06-Topics/Agent 动作面：Tools、CLI、MCP、Browser 与 Apps|Agent 动作面：Tools、CLI、MCP、Browser 与 Apps]]
