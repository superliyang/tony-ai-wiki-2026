---
title: Incident-Fed Eval 与 Shadow Rollout 实验
type: project
status: learning
project: Memory Lab
created: 2026-03-29
updated: 2026-03-29
---

# Incident-Fed Eval 与 Shadow Rollout 实验

## 实验目标

把 `self-improving-learning-ledger` 从“会记、会提议”推进到“会经过真实事故驱动的评测与灰度”。

## 这个实验要回答什么

1. 我们能不能把过去的 incident 变成 regression pack
2. promotion candidate 在 shadow rollout 下会不会暴露新的偏差
3. 一旦 candidate 失败，rollback 能不能真的执行

## 实验材料

- `Memory Poisoning` 相关 case
- shared-memory boundary leakage case
- bad promotion case
- plugin / MCP contamination case
- 至少一个正向稳定 pattern

## 推荐实验步骤

### 1. 建立最小 incident pack

把 3 到 5 个真实 failure pattern 写成固定回放集：

- poisoning replay
- boundary replay
- false promotion replay
- rollback replay

### 2. 给每个 promotion candidate 过一遍 replay

不要只看它是不是“会建议 promotion”，还要看：

- 会不会误提 durable rule
- 会不会把 scope 提得太高
- 会不会忽略 rollback

### 3. 做 shadow rollout

让 candidate：

- 参与判断
- 但暂时不拥有最终 durable write 权限
- 记录“它本来会怎么做”

### 4. 收集偏差

至少记这几类：

- over-promotion
- under-promotion
- wrong-scope promotion
- missing rollback
- silent write preference

### 5. 决定 scoped release 或 demotion

只有在 replay + shadow 都稳定时，才进入更小范围 release。

## 最小验收标准

- 每个 candidate 都有 replay 记录
- 至少 1 个 poisoning / boundary 负例通过
- shadow 结果有日志
- rollout owner 明确
- rollback 操作明确

## 产出物

- incident-fed regression list
- shadow rollout observation log
- release / no-release decision
- rollback checklist

## 关联

- [[Self-Improving-Agent 与 AutoSkill 实验]]
- [[Memory Poisoning、Shared Memory Boundary 与 Release Gates 实验]]
- [[最小 Self-Improving Skill 设计]]
- [[最小 Self-Improving Plugin 设计]]
- [[../../07-Topics/Incident-Fed Evals、Shadow Rollout 与 Promotion Regression|Incident-Fed Evals、Shadow Rollout 与 Promotion Regression]]
