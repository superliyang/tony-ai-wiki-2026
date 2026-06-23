---
title: Agent 效果评估：方法论、开源工具与判断框架
type: topic
status: learning
tags:
  - ai/engineering
  - ai/agent
  - ai/evaluation
  - ai/agentops
created: 2026-04-14
updated: 2026-04-15
---

# Agent 效果评估：方法论、开源工具与判断框架

## 这页解决什么问题

很多团队会说“这个 agent 看起来更聪明了”，但真正上线时，你更需要回答的是：

- 它在哪些任务上真的更好了
- 它是不是只是 demo 更好，而不是系统更稳
- 它的改进是不是靠更高成本、更高人工接管换来的
- 你应该用哪些开源工具，把这种判断变成可重复流程

## 先给结论

`Agent evaluation` 不是看一个总分，而是看 5 个面是否同时过关：

1. `task outcome`：任务有没有真的完成
2. `trajectory quality`：中间轨迹是不是合理、稳定、可解释
3. `tool reliability`：工具调用、参数构造、错误恢复是否可靠
4. `operational health`：延迟、成本、重试、人工接管是否可接受
5. `safety and governance`：有没有越权、绕审批、踩安全边界

所以判断 agent 好不好，不能只问“回答质量”，而要问：

- 在明确任务集上，它的 `success rate` 是否更高
- 在可接受成本内，它的 `cost per successful task` 是否更低
- 在真实工具和环境里，它的 `recovery / escalation behavior` 是否更成熟
- 在线样本是否支持离线结论，而不是互相打脸

## 一套最实用的方法论

### 1. 先定义任务族，而不是直接跑总分

对 agent 来说，最容易误判的一步，就是把完全不同的任务混成一个平均数。

更合理的拆法通常是：

- `happy path`：标准任务
- `business-critical path`：高价值、高频任务
- `failure-prone path`：最常出错的任务
- `adversarial / boundary path`：越权、注入、异常输入、脏数据
- `long-horizon path`：需要多步执行、恢复和上下文连续性的任务

没有任务分层，你最后得到的常常只是一个没有决策意义的总分。

### 2. 评估集要从真实失败里长出来

一开始最有价值的样本，不是精美 benchmark，而是：

- 真实线上失败 case
- 人工接管 case
- tool timeout / malformed args / empty retrieval case
- 审批被绕过或误触发 case

更现实的构建顺序通常是：

1. `historical incidents`
2. `happy paths`
3. `risky boundaries`
4. `synthetic long-tail`

### 3. 评分器要分层

agent 评估很少能只靠一种 grader。

更常见的是三层组合：

- `rule-based graders`
  - 适合检查 JSON schema、工具参数、状态转移、是否调用了必须工具
- `model-based graders`
  - 适合评估回答是否完整、计划是否合理、产物是否满足语义要求
- `human review`
  - 适合高风险任务、争议 case、judge 不稳定的边界样本

一个成熟系统通常不会只信任 judge model，也不会把所有 case 都交给人工。

### 4. 不只看最终结果，也要看轨迹

很多 agent 会“偶然成功”，但过程很差：

- 绕了远路
- 多调了很多工具
- 中间出现错误但被掩盖
- 没触发该有的审批

所以要把评估拆成至少两层：

- `outcome grading`
- `trace grading`

对 agent 来说，trace 经常比最终答案更能解释 regression。

### 5. 离线、在线、发布门禁必须形成闭环

一套成熟的 AgentOps eval loop 往往是：

1. `offline eval`
2. `sandbox replay`
3. `pre-release gate`
4. `online telemetry`
5. `sampled review`
6. `incident-fed regression`

如果只做其中一层，很容易出现：

- 离线分数很好，线上失败一堆
- trace 很丰富，但没有 release decision
- 样本很多，但没有回归套件

## 你到底该看哪些指标

### 一、任务结果层

- `task completion rate`
- `goal satisfaction rate`
- `artifact acceptance rate`
- `critical-step completion rate`

### 二、轨迹质量层

- `trajectory grade`
- `plan quality`
- `unnecessary step rate`
- `tool selection correctness`
- `argument correctness`

### 三、恢复与稳定性层

- `retry success rate`
- `error recovery rate`
- `fallback success rate`
- `handoff / escalation rate`
- `repeatability across reruns`

### 四、运营层

- `mean time to completion`
- `cost per successful task`
- `tool calls per successful task`
- `token cost per accepted artifact`

### 五、安全与治理层

- `approval bypass rate`
- `unsafe action attempt rate`
- `prompt injection susceptibility`
- `policy violation rate`

## 什么才叫“这个 Agent 真的变好了”

如果下面 6 条里，大部分都更好，才更接近真实改进：

1. 同一任务集上的 `success rate` 提升
2. `cost per successful task` 没有明显恶化
3. `tool failure / malformed action` 降低
4. `human takeover` 或 `manual correction load` 降低
5. 高风险任务没有引入新的安全回退
6. 在线抽样和离线回归结论一致

如果只是“demo 更惊艳”，但：

- 轨迹更长
- 成本更高
- 人工纠错更多
- 一换环境就塌

那它不算真正变好。

## 开源工具怎么选

### Promptfoo

最适合：

- 发布前 regression
- prompt / config / model 对比
- CI gate
- red-team quick checks

它更像 `pre-release evaluation layer`。

### Langfuse

最适合：

- trace + session + score
- dataset run 对比
- prompt / release comparison
- agent version regression diagnosis

它更像 `runtime evaluation workbench`。

### Arize Phoenix

最适合：

- trace-first 调试
- eval over traces
- retrieval / tool / workflow failure diagnosis
- 和 `OpenTelemetry / OpenInference` 风格的观测栈结合

它更像 `trace debugging and diagnosis layer`。

### Ragas

最适合：

- 指标库
- RAG 评估
- agent / tool-use testset generation
- multi-turn 与 judge-based evaluation

它更像 `metric + testset generation library`。

### Inspect AI

最适合：

- 可重复任务集
- sandbox 环境中的 agent eval
- solver / scorer 分离的实验设计
- 更研究化、更可编排的 benchmark

它更像 `task-and-scorer-oriented evaluation framework`。

### Giskard

最适合：

- 质量测试套件
- RAG evaluation toolkit
- LLM scan / security-style 测试
- 把测试接进 CI/CD

它更像 `quality + vulnerability testing toolkit`。

## 我会怎么组合

### 小团队的最低可用组合

- `Promptfoo + Langfuse`

适合：

- 先有发布前回归
- 再有线上 trace 和 dataset run 对比

### Trace 诊断优先的组合

- `Phoenix + Promptfoo`

适合：

- 线上经常退化
- 但你还看不清是 retrieval、tool 还是 prompt 出问题

### RAG / 知识型 Agent 的组合

- `Ragas + Langfuse`

适合：

- 需要同时做 testset generation、指标评估和线上 regression 对照

### 更研究化、更可控环境的组合

- `Inspect AI + Ragas`

适合：

- 想把任务、环境、scorer、agent 行为分开实验

### 安全和上线门禁更敏感的组合

- `Promptfoo + Giskard + Phoenix`

适合：

- 既要 pre-release gate
- 又要安全扫描
- 还要线上 trace 诊断

## 最常见的 8 个误判

1. 只看最终答案，不看轨迹
2. 只看平均分，不拆任务族
3. 只做离线 eval，不看线上样本
4. 只有 trace，没有 release gate
5. judge model 同时当裁判和被评对象，导致偏差
6. 忽略人工接管成本，只看“最终做完了没”
7. 没把 incident 反写回 regression suite
8. 把 open-source tool 当成银弹，而不是治理流程的一部分

## 如果你今天就要开始搭

最小顺序我建议是：

1. 明确 `task taxonomy`
2. 先收 `historical failures`
3. 建一个小的 `regression suite`
4. 用 `Promptfoo` 或 `Inspect AI` 跑 pre-release tasks
5. 用 `Langfuse` 或 `Phoenix` 接 trace
6. 每次线上 incident 都回流到 suite
7. 再逐步引入 `Ragas`、`Giskard` 这种更细工具

## 可直接套用的资产

- 模板：[[../09-Templates/Agent 效果评测模板|Agent 效果评测模板]]
- 任务包模板：[[../09-Templates/Agent Eval 任务包模板|Agent Eval 任务包模板]]
- 发布门禁：[[../09-Templates/Agent 上线门槛模板|Agent 上线门槛模板]]
- 指标清单：[[../04-Evaluation/Agent 效果评估指标清单|Agent 效果评估指标清单]]
- 起步任务包：[[../04-Evaluation/Agent Eval 任务包：Repo、Research、RAG、Tool Use|Agent Eval 任务包：Repo、Research、RAG、Tool Use]]
- 半成品案例包：[[../04-Evaluation/Coding Agent Eval Pack：Repo 修复、测试与小型重构|Coding Agent Eval Pack]]、[[../04-Evaluation/企业知识库 Agent Eval Pack：检索、归因与权限边界|企业知识库 Agent Eval Pack]]、[[../04-Evaluation/Research Agent Eval Pack：信息整合、引用与冲突处理|Research Agent Eval Pack]]

## 推荐继续往下读

1. [[Agent Evaluation and Reliability]]
2. [[Eval Harness 与 Regression Suites]]
3. [[Online Evals、Human Feedback 与 Annotation]]
4. [[LLMOps、AgentOps 与 Observability]]
5. [[Incident-Fed Evals、Shadow Rollout 与 Promotion Regression]]
6. [[Task Success and Failure Recovery]]
7. [[../../AI-Learning/09-Systems/Langfuse|Langfuse]]
8. [[../../AI-Learning/09-Systems/Arize Phoenix|Arize Phoenix]]
9. [[../../AI-Learning/09-Systems/Promptfoo|Promptfoo]]
10. [[../../AI-Learning/09-Systems/Ragas|Ragas]]
11. [[../../AI-Learning/09-Systems/Inspect AI|Inspect AI]]
12. [[../../AI-Learning/09-Systems/Giskard|Giskard]]

## 关联

- [[Agent Evaluation and Reliability]]
- [[Eval Harness 与 Regression Suites]]
- [[Online Evals、Human Feedback 与 Annotation]]
- [[LLMOps、AgentOps 与 Observability]]
- [[Agent 上线门槛与安全 Release Gates]]
- [[AI Security Evaluation 与 Red Teaming]]
- [[Task Success and Failure Recovery]]
- [[Incident-Fed Evals、Shadow Rollout 与 Promotion Regression]]
- [[../../AI-Learning/06-Topics/Agent|Agent]]
- [[../../AI-Learning/06-Topics/MLOps 与 LLMOps|MLOps 与 LLMOps]]

## 资料

- [Langfuse Docs](https://langfuse.com/docs)
- [Phoenix Docs](https://arize.com/docs/phoenix)
- [Promptfoo Docs](https://www.promptfoo.dev/docs/intro/)
- [Ragas Docs](https://docs.ragas.io/en/stable/)
- [Inspect Docs](https://inspect.aisi.org.uk/)
- [Giskard Docs](https://docs.giskard.ai/oss/sdk/index.html)
