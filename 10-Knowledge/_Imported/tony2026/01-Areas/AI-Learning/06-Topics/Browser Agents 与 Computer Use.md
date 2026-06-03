---
title: Browser Agents 与 Computer Use
type: topic
status: learning
tags:
  - ai/topic
  - ai/agent
  - ai/browser
  - ai/computer-use
created: 2026-03-25
updated: 2026-04-03
---

# Browser Agents 与 Computer Use

## 这个主题是什么

`Browser Agents` 和 `Computer Use` 关注的是：agent 不只是调用 API 或命令行，而是直接通过浏览器、屏幕截图、鼠标、键盘和页面状态去完成任务。

它代表了一种很特别的 action surface：

- 不是结构化 API
- 不是本地 shell
- 而是面向真实 UI 的操作循环

## 为什么它在最近很热

因为它解决了 agent 落地里一个很现实的问题：

- 很多系统没有好用 API
- 很多长尾流程其实都发生在网页和桌面界面里
- 如果 agent 能直接看见页面并采取动作，它就能覆盖更大的任务空间

所以大家会把它看成“让 agent 进入真实软件世界”的关键一步。

## 你先要抓住什么

- browser / computer use 很强，但它不是万能入口
- 它更像 last-mile automation surface
- 当没有结构化接口时，它很有价值
- 当已经有稳定 API / MCP / CLI 时，它未必是最优选择

## 一条典型工作循环

1. agent 先观察页面或屏幕
2. 从截图、DOM、页面状态中理解当前界面
3. 选择动作：点击、输入、滚动、快捷键、等待
4. 执行动作
5. 再次观察，进入下一轮决策

本质上，它是一种 `observe -> act -> observe` 的闭环。

## 它和 CLI、MCP 的关键差异

### 和 CLI 比

- `CLI` 更适合本地 repo、脚本、系统命令
- `Computer Use` 更适合网页、SaaS、桌面界面

### 和 MCP 比

- `MCP` 更适合结构化、稳定、可复用的系统接入
- `Computer Use` 更适合没有稳定接口、但界面可操作的长尾任务

### 和 harness 的关系

- computer use 往往不会单独存在
- 它通常是 harness 里的一个动作面
- 真正难的是它如何被约束、记录、回放、审批和恢复

## 为什么它很容易让人误判

很多演示会让人觉得：

- 只要给 agent 一个浏览器，它就几乎什么都能做

但真实工程里，常见问题是：

- 截图理解不稳定
- 页面变化导致动作漂移
- 登录态和敏感数据风险高
- CAPTCHA、权限弹窗、多窗口切换都很脆弱
- latency 通常比 API / CLI 更高

## 什么时候它特别有价值

- 跨多个 SaaS 界面做串联
- 没有标准 API 的内部后台系统
- 人类平时本来就是“点网页完成”的流程
- 需要 agent 辅助，但短期又不值得深度平台化接入

## 什么时候不要优先用它

- 已经有稳定 API
- 已经有 CLI / script workflow
- 高风险、高精度、强审计场景
- 速度和稳定性要求很高的生产链路

## 最近两年最值得记住的论文锚点

- [[ScreenAI：A Vision-Language Model for UI and Infographics Understanding]]
- [[WebVoyager：Building an End-to-End Web Agent with Large Multimodal Models]]
- [[../11-Recent-Supplements/2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use|2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use]]

## 推荐继续往下读

- [[提示词工程]]
- [[上下文工程]]
- [[Tool Use]]
- [[MCP（Model Context Protocol）]]
- [[../../AI-Engineering/07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]]
- [[../../AI-Engineering/07-Topics/App Server 与 Rich Agent Protocols|App Server 与 Rich Agent Protocols]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]

## 系统案例

- [[../09-Systems/ChatGPT Agent|ChatGPT Agent]]
- [[../09-Systems/OpenClaw|OpenClaw]]

## 相关

- [[Tool Use]]
- [[MCP（Model Context Protocol）]]
- [[上下文工程]]
- [[../07-Maps/Agent Prompt-Context-Harness Map|Agent Prompt-Context-Harness Map]]
- [[../11-Recent-Supplements/2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use|2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use]]
