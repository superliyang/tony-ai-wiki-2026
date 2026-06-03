---
title: Agent 效果评估指标清单
type: evaluation
status: learning
tags:
  - ai/evaluation
  - ai/agent
  - ai/metrics
created: 2026-04-15
updated: 2026-04-15
---

# Agent 效果评估指标清单

## 这页怎么用

这页不是要你把所有指标都采齐，而是帮你先分清：

- 哪些指标决定“它有没有真的更好”
- 哪些指标决定“它是不是只是更贵、更慢”
- 哪些指标决定“它能不能上线”

## 一、任务结果层

这些指标回答的是：任务有没有真正完成。

- `task completion rate`
- `goal satisfaction rate`
- `artifact acceptance rate`
- `critical-step completion rate`

### 判断要点

- 优先按任务族拆开看，不看一个平均数
- `business-critical path` 的权重通常高于普通 happy path

## 二、轨迹质量层

这些指标回答的是：它是不是靠合理路径完成。

- `trajectory grade`
- `plan quality`
- `unnecessary step rate`
- `tool selection correctness`
- `argument correctness`

### 判断要点

- 最终成功不代表过程健康
- 轨迹越来越长、越来越绕，通常意味着系统正在变脆

## 三、工具与恢复层

这些指标回答的是：agent 在真实工具环境里稳不稳。

- `tool success rate`
- `tool timeout rate`
- `retry success rate`
- `fallback success rate`
- `error recovery rate`

### 判断要点

- 如果 tool success 提升，但重试次数飙升，可能只是把失败成本藏起来了
- 真正成熟的系统要看 `失败后恢复`，不是只看“第一次成不成”

## 四、人工负担层

这些指标回答的是：它是否真的在减负，而不是转移负担。

- `handoff / escalation rate`
- `manual correction load`
- `approval request quality`
- `time spent by reviewer`

### 判断要点

- 如果任务成功率上升，但人工纠错更重，未必是净改进
- `approval` 变少不一定是好事，可能是绕过了该有人看的节点

## 五、运营层

这些指标回答的是：它的代价是否可接受。

- `mean time to completion`
- `p95 time to completion`
- `cost per successful task`
- `tool calls per successful task`
- `token cost per accepted artifact`

### 判断要点

- agent 系统比单轮模型更应该看 `cost per success`
- 只看平均 latency 容易掩盖长尾问题，最好带 `p95`

## 六、安全与治理层

这些指标回答的是：它有没有破坏边界。

- `approval bypass rate`
- `unsafe action attempt rate`
- `policy violation rate`
- `prompt injection susceptibility`
- `high-risk action false-positive / false-negative`

### 判断要点

- 这层通常决定“能不能上线”，而不是“效果好不好”
- 一旦进入真实工具执行，这层往往比质量分更重要

## 七、发布判断最常用的核心组合

如果只能先抓一小组，我会先抓：

1. `task success rate`
2. `cost per successful task`
3. `handoff / escalation rate`
4. `tool success rate`
5. `trajectory grade`
6. `policy violation rate`

## 八、最容易误读的 6 件事

1. 成功率升了，但 `cost per success` 恶化很多
2. 人工接管降了，但安全违规升了
3. 轨迹更长，但最终分数变化不大
4. 平均指标好看，但 `p95` 明显恶化
5. 只看离线 judge，不看线上样本
6. 不拆任务族，只看加权总分

## 什么时候可以说“这个版本值得推进”

更靠谱的判断通常是：

- `task success` 提升
- `cost per success` 没有明显恶化
- `handoff` 没上升
- `policy violation` 不上升
- 高风险任务没有新增 regression

## 关联

- [[评测索引]]
- [[Agent Eval 任务包：Repo、Research、RAG、Tool Use]]
- [[../07-Topics/Agent 效果评估：方法论、开源工具与判断框架|Agent 效果评估：方法论、开源工具与判断框架]]
- [[../09-Templates/Agent 效果评测模板|Agent 效果评测模板]]
- [[../09-Templates/Agent 上线门槛模板|Agent 上线门槛模板]]
