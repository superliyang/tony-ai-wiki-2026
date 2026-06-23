---
title: Agent Evaluation and Reliability
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent-runtime
  - ai/evaluation
created: 2026-03-22
updated: 2026-04-14
---

# Agent Evaluation and Reliability

## 为什么重要

- 对 agent 来说，“模型回答得像不像样”只是很小一部分
- 真正上线时，更关键的是：任务能不能完成、过程稳不稳、结果是否可重复
- 所以 agent 评测天然要比普通聊天模型评测更系统化

## 系统视角

`Agent Evaluation` 不是只测一个模型分数，而是评估一整条任务执行链：

- 目标理解是否正确
- 计划是否合理
- 工具调用是否成功
- 状态是否连续
- 失败后能否恢复
- 最终产物是否真的满足任务要求

也就是说，agent reliability 是“模型能力 + 系统能力 + 任务治理”的联合结果。

## 和普通 benchmark 的差别

普通 benchmark 更像问：

- 你会不会做题
- 你会不会推理
- 你会不会写代码

agent evaluation 更像问：

- 你能不能把任务真正做完
- 中间会不会乱跑
- 工具坏了你会怎么处理
- 换一个环境，你还能不能稳定复现

## 常见评测维度

- task success：任务最终是否完成
- step success：关键子步骤是否成功
- tool reliability：工具调用成功率、错误率、恢复率
- state continuity：上下文、会话、记忆是否断裂
- human burden：用户是否需要频繁纠正和接管
- repeatability：同类任务是否能稳定得到近似结果

## 真正难的地方

- 任务成功往往不是二元的，而是带主观判断
- 一个 agent 可能“最后完成了”，但过程极不可靠
- 离线评测和真实在线环境之间差距非常大
- 同一个系统在不同任务类型上的可靠性差异会很大

## 常见评测方式

- scenario tests：按真实任务脚本测端到端完成情况
- replay tests：重放典型任务，比较不同版本表现
- sandbox tasks：在受控环境里测工具调用与状态流转
- human review：人工判断产物是否真的可用
- online telemetry：线上统计成功率、重试率、人工接管率、耗时与成本
- trace grading：对完整执行轨迹做结构化评分，定位中间环节问题

## 推荐关注的 5 个核心指标

1. `task completion rate`
2. `tool success rate`
3. `handoff / escalation rate`
4. `mean time to completion`
5. `human correction load`

## 常见失败模式

- 成功率看起来不错，但只有在 demo 任务上成立
- 最终任务偶尔能做完，但过程成本极高
- 工具失败后系统不会降级和恢复
- 一换环境、一换 repo、一换数据，性能立刻塌掉

## 推荐治理方法

- 不要只测最终结果，也要测中间链路
- 把任务类型拆开评测，而不是只看一个总分
- 让离线评测和线上 telemetry 能互相印证
- 对 agent 版本迭代建立 regression suite，而不是靠主观体验判断
- 把 eval harness 视为持续系统，而不是一次性 benchmark

## 如果你要真正落地到工具和流程

继续读：

- [[Agent 效果评估：方法论、开源工具与判断框架]]

## 系统案例

- [[../../AI-Learning/09-Systems/Claude Code|Claude Code]]
- [[../../AI-Learning/09-Systems/Codex|Codex]]
- [[../../AI-Learning/09-Systems/Cursor|Cursor]]
- [[../../AI-Learning/09-Systems/OpenClaw|OpenClaw]]

## 相关

- [[Evaluation and Benchmarks]]
- [[Task Success and Failure Recovery]]
- [[Cost, Latency, and Safety Tradeoffs]]
- [[Human-in-the-Loop and Approval Gates]]
- [[Eval Harness 与 Regression Suites]]
- [[Agent 效果评估：方法论、开源工具与判断框架]]
- [[../../AI-Learning/06-Topics/Agent|Agent]]
