---
title: Agent Security、Sandbox 与 Approval Architecture
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/security
  - ai/sandbox
created: 2026-03-25
updated: 2026-03-25
---

# Agent Security、Sandbox 与 Approval Architecture

## 为什么这层是 Agent 工程的硬边界

agent 一旦不只是回答问题，而是真的：

- 跑 shell
- 调远端工具
- 控浏览器
- 调另一个 agent
- 长期保存记忆

安全问题就不再是“上线前补一下”，而是系统设计的第一层边界。

## 你可以把这层拆成四块

### `sandbox`

让 agent 的动作发生在受控环境中。

### `permission model`

定义默认允许什么、禁止什么、什么必须审批。

### `approval architecture`

定义哪些动作需要用户接管、哪些需要 watch mode、哪些需要显式确认。

### `audit / recovery`

定义怎么记录、回放、追责、止损和恢复。

## 不同动作面的风险并不一样

### `CLI / shell`

风险点：

- 文件破坏
- 网络外联
- 环境变量 / secrets 泄漏
- 对本地系统产生不可逆影响

### `MCP`

风险点：

- 远端 server 的真实性和权限边界
- tool metadata 不完整
- 一个看似只读的 server 实际能触发高风险动作

### `browser / computer use`

风险点：

- prompt injection 来自页面本身
- 敏感域名、登录态、支付动作
- watch mode 缺失导致系统自动误操作

### `A2A`

风险点：

- 远端 agent 语义不透明
- capability 声明与真实行为不一致
- 跨组织协作导致责任链不清晰

## 最常见的防线

- 最小权限 sandbox
- allowlist / denylist
- 只读默认、升级授权
- 高风险动作审批
- secrets 隔离，不把真实生产凭据直接交给 agent
- 完整日志、trace、artifact 和回放能力

## approval architecture 应该怎么想

不是所有动作都需要人审。

更现实的设计是分层：

1. `auto-allow`
   - 低风险、可回滚、低价值动作
2. `soft approval / watch mode`
   - 中风险动作，允许继续但必须有人盯着
3. `explicit approval`
   - 高风险动作，必须确认后才执行
4. `hard deny`
   - 默认禁止的动作面

## 为什么安全和可用性总在拉扯

- 管得太严，agent 没法用
- 放得太开，agent 迟早出事

所以好的 agent security 不是“什么都不让干”，而是：

- 让低风险动作顺滑
- 让高风险动作显式可见
- 让错误动作可止损、可追踪、可回放

## 推荐继续往下读

- [[Computer Use Runtime and Safety]]
- [[MCP 与 CLI 模式]]
- [[Harness Engineering]]
- [[Human-in-the-Loop and Approval Gates]]
- [[Eval Harness 与 Regression Suites]]
- [[A2A 与 Multi-Agent Coordination]]

## 相关

- [[Human-in-the-Loop and Approval Gates]]
- [[Computer Use Runtime and Safety]]
- [[Harness Engineering]]
- [[A2A 与 Multi-Agent Coordination]]
- [[../08-Maps/Agent 协作、记忆与信任边界图|Agent 协作、记忆与信任边界图]]
