---
title: Eval Harness 与 Regression Suites
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/evals
  - ai/harness
created: 2026-03-25
updated: 2026-04-14
---

# Eval Harness 与 Regression Suites

## 为什么这层值得单独拆出来

很多团队说自己在做 `Harness Engineering`，真正落到工程上，最容易被忽略的一块就是：

- 你有没有可重复的评测环境
- 你有没有版本迭代后的回归套件
- 你能不能在改 prompt、改 context、改 tool policy、改 protocol 之后，知道系统到底变好了还是变坏了

所以 `eval harness` 和 `regression suite` 可以看成 harness 的反馈回路核心。

## 这个主题是什么

`Eval Harness` 指的是：把 agent 的任务样本、执行环境、grader、trace、结果比较和版本对照，组织成一个可重复运行的评测系统。

`Regression Suite` 指的是：

- 一组代表性的任务集合
- 每次改动后重复跑
- 用来发现质量回退、脆弱点和新引入的失败模式

## 为什么 agent 特别需要它

普通单轮模型可以只测输出。

agent 系统不行，因为它的变化点太多：

- prompt 变了
- context 装配变了
- tool selection 变了
- MCP server 行为了变
- browser / computer use 行为了变
- app server / approval / retry 逻辑变了

没有 eval harness，你很容易陷入：

- demo 感觉更好了
- 但真实任务成功率下降了
- trace 更长了，成本更高了
- 审批变少了，但风险变大了

## 一个成熟 eval harness 往往包含什么

- `task set`：典型任务、边界任务、对抗任务
- `environment`：可重复运行的 sandbox / repo / tool setup
- `trace capture`：记录完整执行轨迹，而不只看最终答案
- `graders`：规则 grader、模型 grader、人工复核
- `comparison loop`：版本间对比，定位 regression
- `promotion rule`：只有通过阈值才允许上线或升配

## 为什么 trace grading 很关键

对 agent 来说，只看最终结果常常不够。

你还想知道：

- 它是不是走了错误路径才偶然成功
- 它是不是过度调用工具
- 它是不是绕过了应该触发的审批
- 它是不是在某个中间步骤已经表现出脆弱性

所以 `trace grading` 很适合成为 eval harness 的一部分。

## 你可以把评测分成三层

1. `task outcome`
   - 最终有没有完成任务
2. `trace quality`
   - 中间步骤是否合理、稳健、合规
3. `operational health`
   - latency、cost、handoff rate、retry rate 是否还能接受

## regression suite 该怎么长出来

一开始不需要很大。

更现实的做法是：

- 先从真实失败 case 收集样本
- 再补核心 happy path
- 然后增加高风险、长尾、对抗样本
- 每次 incident 后把新 case 反写回 suite

这样 suite 才会越来越像真实系统，而不是 demo 题库。

## 和 harness engineering 的关系

- harness 决定 agent 在什么环境里工作
- eval harness 决定你怎么判断这个环境和这个 agent 是否真的变好

所以它不是附属品，而是 harness 的质量闭环。

## 推荐继续往下读

- [[Harness Engineering]]
- [[Agent Evaluation and Reliability]]
- [[Agent 效果评估：方法论、开源工具与判断框架]]
- [[Task Success and Failure Recovery]]
- [[Cost, Latency, and Safety Tradeoffs]]
- [[Human-in-the-Loop and Approval Gates]]

## 相关

- [[Harness Engineering]]
- [[长期运行 Agent 的记忆系统]]
- [[Agent Security、Sandbox 与 Approval Architecture]]
- [[Agent Evaluation and Reliability]]
- [[Agent 效果评估：方法论、开源工具与判断框架]]
- [[../08-Maps/Harness Feedback Loop Map|Harness Feedback Loop Map]]
- [[../08-Maps/Agent Evaluation and Governance Map|Agent Evaluation and Governance Map]]
