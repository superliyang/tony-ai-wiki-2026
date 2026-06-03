---
title: Agent 效果评测模板
type: reference
status: stable
tags:
  - template/evaluation
  - template/agent
created: 2026-04-15
updated: 2026-04-15
---

# Agent 效果评测模板

```yaml
---
title:
type: agent-evaluation
status: seed
tags: []
agent_name:
owner:
version_under_test:
baseline_version:
task_families: []
environments: []
models: []
tools: []
graders:
  rule_based: []
  model_based: []
  human_review: []
primary_metrics: []
secondary_metrics: []
gates:
  min_task_success:
  max_cost_per_success:
  max_handoff_rate:
  max_policy_violations:
known_risks: []
open_questions: []
created: 2026-04-15
updated: 2026-04-15
---
```

## 评测对象

- agent 名称：
- 版本：
- baseline：
- 目标改动：

## 任务分层

- `happy path`：
- `business-critical path`：
- `failure-prone path`：
- `adversarial / boundary path`：
- `long-horizon path`：

## 环境设置

- sandbox / staging / replay 环境：
- 数据与依赖：
- tool mock / real tool 边界：
- 是否允许外网：

## Grader 设计

### Rule-based

- schema / action validity：
- 必须步骤检查：

### Model-based

- 语义完成度：
- 计划质量：
- 产物可用性：

### Human Review

- 抽样比例：
- 审核角色：
- 争议回收规则：

## 指标

### Primary

- `task success rate`
- `cost per successful task`
- `handoff / escalation rate`
- `policy violation rate`

### Secondary

- `trajectory grade`
- `tool success rate`
- `retry recovery rate`
- `mean time to completion`

## 结果摘要

- 最终判断：
- 相比 baseline：
- 最大改进点：
- 最大退化点：

## 是否可进入下一阶段

- 是否通过 release gate：
- 需要补哪些 regression case：
- 需要补哪些在线观察：

## 关联

- [[../04-Evaluation/Agent 效果评估指标清单|Agent 效果评估指标清单]]
- [[../07-Topics/Agent 效果评估：方法论、开源工具与判断框架|Agent 效果评估：方法论、开源工具与判断框架]]
- [[Agent Eval 任务包模板]]
- [[Agent 上线门槛模板]]
