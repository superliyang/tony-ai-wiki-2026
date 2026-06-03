---
title: Computer Use Runtime and Safety
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/computer-use
  - ai/safety
created: 2026-03-25
updated: 2026-03-25
---

# Computer Use Runtime and Safety

## 为什么这个主题重要

一旦 agent 从 API / CLI 进入 `computer use`，系统面对的就不只是工具调用，而是真实 UI 环境中的 perception-action loop。

这会把风险和复杂度一起拉高。

## 这个 runtime 通常包含什么

- 一个受控浏览器或桌面环境
- 屏幕截图能力
- 鼠标和键盘动作能力
- 页面 / 界面状态回读
- agent loop，把观察结果再送回模型
- 审计日志、回放、暂停与人工接管能力

## 为什么它和普通 tool call 不一样

普通 tool call 往往是：

- 结构化输入
- 明确动作
- 结构化输出

computer use 更像：

- 部分感知
- 动作序列
- 不稳定界面
- 需要反复观察和修正

所以它天然更脆弱，也更依赖 harness。

## 最常见的工程风险

- 坐标或目标识别错误
- 页面变化导致动作漂移
- 提示注入来自网页内容本身
- 登录态、敏感信息、支付和提交动作风险极高
- latency 高，循环慢
- niche UI、多窗口、模态弹窗会显著降低可靠性

## 安全治理要点

- 放在最小权限的 VM / container 中运行
- 不默认给高敏账号、支付、生产控制台权限
- 允许 `take over` / human handoff
- 域名 allowlist / denylist
- 对高风险动作设置 approval gate
- 保留完整日志、截图与事件流

## 为什么“trusted environment”非常关键

computer use 很容易受 prompt injection 影响，因为网页、图片、屏幕上的内容本身都可能在“指挥”模型。

所以这类系统比普通工具调用更需要：

- 可信环境
- 最小权限
- 明确边界
- 人类监督

## 什么时候它适合上线

- trusted environment
- 可接受较高 latency
- 高风险动作有人审
- 目标是 background assistance，而不是完美自动驾驶

## 什么时候它更适合做实验而不是主链路

- 对稳定性要求极高
- 需要精确、可审计、低风险动作
- 已经存在更好的 API / CLI / MCP 路径

## 推荐继续往下读

- [[Tool Calling and Action Execution]]
- [[Human-in-the-Loop and Approval Gates]]
- [[Harness Engineering]]
- [[../../AI-Learning/06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]]
- [[../../AI-Learning/09-Systems/ChatGPT Agent|ChatGPT Agent]]

## 相关

- [[Harness Engineering]]
- [[MCP 与 CLI 模式]]
- [[Human-in-the-Loop and Approval Gates]]
- [[../08-Maps/Agent Action Surfaces and Protocols Map|Agent Action Surfaces and Protocols Map]]
