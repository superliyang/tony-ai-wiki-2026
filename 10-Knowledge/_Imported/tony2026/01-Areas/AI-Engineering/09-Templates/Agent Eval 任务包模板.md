---
title: Agent Eval 任务包模板
type: reference
status: stable
tags:
  - template/evaluation
  - template/agent
  - template/task-pack
created: 2026-04-15
updated: 2026-04-15
---

# Agent Eval 任务包模板

```yaml
---
title:
type: agent-eval-pack
status: seed
tags: []
agent_scope:
task_family:
environment:
risk_level:
datasets: []
tools: []
graders: []
metrics: []
release_usage:
created: 2026-04-15
updated: 2026-04-15
---
```

## 这个任务包服务什么判断

- 想判断：
- 影响哪个发布决定：
- 最容易暴露哪类 failure mode：

## 任务集合

### Happy Path

- case 1：
- case 2：

### High-Value / Critical

- case 1：
- case 2：

### Failure-Prone

- case 1：
- case 2：

### Adversarial / Boundary

- case 1：
- case 2：

### Long-Horizon

- case 1：
- case 2：

## Grader 设计

- rule-based：
- model-based：
- human-review：

## 通过阈值

- 最低 `task success rate`：
- 最高 `cost per success`：
- 最高 `handoff rate`：
- 最高 `policy violation rate`：

## 发布用途

- 用于 pre-release gate：
- 用于 incident replay：
- 用于 shadow rollout compare：

## 关联

- [[Agent 效果评测模板]]
- [[../04-Evaluation/Agent Eval 任务包：Repo、Research、RAG、Tool Use|Agent Eval 任务包：Repo、Research、RAG、Tool Use]]
- [[../07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]
