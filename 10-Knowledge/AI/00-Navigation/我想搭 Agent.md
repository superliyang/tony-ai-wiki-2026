---
title: 我想搭 Agent
type: guide
status: active
updated: 2026-04-03
---

# 我想搭 Agent

## 先别急着写代码，先判断这 5 件事

- 你要的是 `assistant`、`workflow`、`runtime` 还是 `coding agent`
- 它的动作面主要是 `CLI`、`browser`、`MCP`、`SDK tools` 还是多种混合
- 它是一次性任务，还是要长期运行、后台继续、支持人工接管
- 你需要 `memory`、`approval`、`multi-agent` 到什么程度
- 最终交付的是答案、artifact、patch、PR，还是业务动作

## 最短阅读路径

1. [[AI 总控制塔|AI 总控制塔]]
2. [[AI-Learning/07-Maps/AI Agent Systems Map|AI Agent Systems Map]]
3. [[AI-Learning/06-Topics/从提示词到 Harness：Agent 能力的渐进式主线|从提示词到 Harness：Agent 能力的渐进式主线]]
4. [[AI-Engineering/07-Topics/Agent、Workflow、Runtime 与 Harness：边界与组合关系|Agent、Workflow、Runtime 与 Harness：边界与组合关系]]
5. [[AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
6. [[AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
7. [[AI-Engineering/07-Topics/Tool Gateway、MCP Servers 与 SDK Tools|Tool Gateway、MCP Servers 与 SDK Tools]]
8. [[AI-Engineering/07-Topics/A2A 与 Multi-Agent Coordination|A2A 与 Multi-Agent Coordination]]
9. [[AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]
10. [[AI-Applications/05-Topics/Agent Productization|Agent Productization]]
11. [[AI-Applications/05-Topics/Agent ROI and Value Capture|Agent ROI and Value Capture]]

## 代表系统样本

- [[AI-Learning/09-Systems/Codex|Codex]]
- [[AI-Learning/09-Systems/Claude Code|Claude Code]]
- [[AI-Learning/09-Systems/OpenClaw|OpenClaw]]
- [[AI-Learning/09-Systems/ChatGPT Agent|ChatGPT Agent]]
- [[AI-Learning/09-Systems/Google Agent Development Kit（ADK）|Google Agent Development Kit（ADK）]]

## 代表开源样本

- [[AI-Open-Source/05-Case-Studies/Agent 核心开源样本对比：LangGraph、AutoGen、OpenHands、browser-use、MCP Servers、A2A|Agent 核心开源样本对比]]
- [[AI-Open-Source/03-Projects/LangGraph|LangGraph]]
- [[AI-Open-Source/03-Projects/AutoGen|AutoGen]]
- [[AI-Open-Source/03-Projects/OpenHands|OpenHands]]
- [[AI-Open-Source/03-Projects/browser-use|browser-use]]
- [[AI-Open-Source/03-Projects/MCP Servers|MCP Servers]]
- [[AI-Open-Source/03-Projects/A2A|A2A]]
- [[AI-Open-Source/06-Maps/Agent 系统核心 8 关系图|Agent 系统核心 8 关系图]]

## 读完这页路径后，你应该能自己回答

- 你到底是在做 `agent product`、`agent runtime` 还是 `agent workbench`
- 你的动作面和扩展面该开到哪一层
- 哪些能力必须一开始就设计：approval、memory、trace、rollback
- 哪些开源样本适合作为参考，不该混成一锅

## 关联

- [[AI 决策导航|AI 决策导航]]
- [[什么时候该用 Workflow，什么时候该上 Agent]]
- [[什么时候该用 LangGraph、AutoGen、OpenHands、browser-use、MCP 与 A2A]]
- [[AI 问题导航|AI 问题导航]]
- [[AI-Learning/07-Maps/Agent 平台生态图|Agent 平台生态图]]
- [[AI-Applications/06-Maps/Assistant-to-Runtime Migration Map|Assistant-to-Runtime Migration Map]]
