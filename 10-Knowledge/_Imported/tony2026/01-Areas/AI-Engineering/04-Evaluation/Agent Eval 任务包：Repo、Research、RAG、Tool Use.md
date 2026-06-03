---
title: Agent Eval 任务包：Repo、Research、RAG、Tool Use
type: evaluation
status: learning
tags:
  - ai/evaluation
  - ai/agent
  - ai/task-pack
created: 2026-04-15
updated: 2026-04-15
---

# Agent Eval 任务包：Repo、Research、RAG、Tool Use

## 这页解决什么问题

很多团队知道“要做 agent eval”，但不知道第一批任务该怎么挑。

这页给的是一个最实用的起步包：不是追求全，而是先挑最能暴露系统问题的 4 类任务。

## 1. Repo Agent 任务包

适合：

- coding agent
- repo maintenance assistant
- issue triage / fix agent

### Happy Path

- 读一组相关文件，解释 bug 原因
- 修改单文件并通过已有测试

### Failure-Prone

- 需要跨 3 个以上文件找依赖
- 需要修改测试和实现一起保持一致

### Boundary

- repo 很大，检索结果容易跑偏
- 用户描述模糊，可能误改无关文件

### 重点指标

- `task completion rate`
- `unnecessary file touch rate`
- `test pass after patch`
- `cost per successful fix`

## 2. Research Agent 任务包

适合：

- deep research
- analyst copilot
- report drafting agent

### Happy Path

- 针对明确问题做资料整理
- 给出结构化对比结论

### Failure-Prone

- 来源冲突
- 时间敏感信息
- 长任务中间丢上下文

### Boundary

- 混入低质量来源
- 没区分事实、推断和建议

### 重点指标

- `source-grounded answer quality`
- `citation correctness`
- `time to completion`
- `hallucinated-claim rate`

## 3. RAG Agent 任务包

适合：

- 企业知识库
- document Q&A
- internal copilot

### Happy Path

- 命中高质量文档并回答
- 从多段文档拼出完整答案

### Failure-Prone

- 检索命中但 answer synthesis 错
- 多版本文档冲突
- 文档缺失但 agent 仍强答

### Boundary

- 脏 chunk
- 权限边界
- prompt injection in documents

### 重点指标

- `retrieval usefulness`
- `answer faithfulness`
- `unsupported-answer rate`
- `policy / permission violation rate`

## 4. Tool-Use Agent 任务包

适合：

- workflow agent
- browser / desktop / API executor
- operations assistant

### Happy Path

- 选择正确工具并完成单步动作
- 多工具串联后产出正确结果

### Failure-Prone

- 参数构造错
- tool timeout
- tool partial failure 后不会恢复

### Boundary

- 高风险动作需审批
- 异常输入诱发错误执行
- 外部系统返回脏数据

### 重点指标

- `tool selection correctness`
- `argument correctness`
- `retry recovery rate`
- `approval bypass rate`

## 任务包怎么落地

最小起步建议：

1. 每类先准备 `5-10` 个 case
2. 至少覆盖 `happy path + failure-prone + boundary`
3. 每个 case 都写清：
   - 目标
   - 环境
   - grader
   - 通过阈值
4. 每次线上 incident 都回写进来

## 如果你时间有限，先补哪类

- 如果你做 coding agent，先补 `Repo`
- 如果你做企业知识库，先补 `RAG`
- 如果你做调研助手，先补 `Research`
- 如果你做执行型 workflow，先补 `Tool Use`

## 关联

- [[Agent 效果评估指标清单]]
- [[评测索引]]
- [[Coding Agent Eval Pack：Repo 修复、测试与小型重构]]
- [[企业知识库 Agent Eval Pack：检索、归因与权限边界]]
- [[Research Agent Eval Pack：信息整合、引用与冲突处理]]
- [[../07-Topics/Agent 效果评估：方法论、开源工具与判断框架|Agent 效果评估：方法论、开源工具与判断框架]]
- [[../09-Templates/Agent Eval 任务包模板|Agent Eval 任务包模板]]
- [[../09-Templates/Agent 效果评测模板|Agent 效果评测模板]]
