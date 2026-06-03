---
title: Agent 上线门槛模板
type: reference
status: stable
tags:
  - template/release
  - template/agent
created: 2026-03-27
updated: 2026-04-15
---

# Agent 上线门槛模板

```yaml
---
title:
type: agent-release-gate
status: seed
tags: []
agent_name:
models: []
tools: []
high_risk_actions: []
approval_rules: []
kill_switches: []
red_team_packs: []
regression_suites: []
open_risks: []
ship_decision:
created: 2026-03-27
updated: 2026-03-27
---
```

## 发布对象

## 任务范围与不支持范围

- 支持的任务族：
- 不支持的任务族：
- 明确不承诺的能力：

## 风险边界

## Eval 必过检查项

- `task success rate`：
- `cost per successful task`：
- `handoff / escalation rate`：
- `policy violation rate`：
- `critical task regression`：

## 必过检查项

- regression suite 已跑：
- high-risk pack 已跑：
- prompt injection / tool misuse 已测：
- approval 触发链路已测：
- rollback 路径已验证：

## 回滚条件

## 上线观察项

- 需要盯的在线指标：
- 抽样 review 频率：
- 事故回写责任人：

## 发布结论

## 关联

- [[Agent 效果评测模板]]
- [[Agent Eval 任务包模板]]
- [[../04-Evaluation/Agent 效果评估指标清单|Agent 效果评估指标清单]]
- [[../04-Evaluation/Agent Eval 任务包：Repo、Research、RAG、Tool Use|Agent Eval 任务包：Repo、Research、RAG、Tool Use]]
