---
title: Tool Calling and Action Execution
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent-runtime
  - ai/tool-use
created: 2026-03-22
updated: 2026-03-22
---

# Tool Calling and Action Execution

## 为什么重要

- agent 真正产生业务价值，往往不在回答文本，而在执行动作
- 只要进入 action layer，系统就必须处理 schema、权限、回执、失败恢复和审计

## 系统视角

`Tool Calling` 关注的是模型如何选择工具、生成参数并触发动作；`Action Execution` 关注的是执行环境如何真正跑起来、如何把结果带回控制循环。

所以这不是一个 prompt 小技巧，而是 agent runtime 里的正式子系统。

## 一条典型链路

1. 模型决定需要调用哪个工具
2. 系统把参数映射到可执行 schema
3. 执行层运行动作
4. 系统把结果结构化回传给模型
5. 模型根据结果继续规划、确认或停止

## 工程难点

- schema 设计是否稳定
- 工具返回值是否足够结构化
- 执行层是否有 timeout、retry、cancel
- 高风险动作是否要求 approval
- 失败结果如何被模型正确理解，而不是继续误操作

## 常见设计模式

- typed tools：正式 schema + 参数校验
- tool adapter：把异构外部系统包成统一工具接口
- execution sandbox：把高风险动作放在受控环境中执行
- browser/computer-use loop：把截图、动作与状态回读收进闭环
- observation envelope：统一记录输入、输出、错误与元数据

## 失败模式

- 模型工具选对了，但参数错了
- 执行成功了，但结果无法被下一轮消费
- 工具调用成功率很低，模型却持续重试
- 系统没有动作级审计，问题难追

## 推荐治理方法

- 工具 schema 尽量小而稳定
- 结果返回要结构化，不要让模型硬解析长文本
- 动作层一定要有权限、预算、超时和日志
- 高风险动作默认走 approval gate

## 系统案例

- [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]
- [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/ChatGPT Agent|ChatGPT Agent]]

## 相关

- [[Agent Runtime Architecture]]
- [[Session and Memory Design]]
- [[Planning Loops and State Machines]]
- [[MCP 与 CLI 模式]]
- [[Computer Use Runtime and Safety]]
- [[Human-in-the-Loop and Approval Gates]]
- [[../../AI-Learning/06-Topics/Tool Use|Tool Use]]
