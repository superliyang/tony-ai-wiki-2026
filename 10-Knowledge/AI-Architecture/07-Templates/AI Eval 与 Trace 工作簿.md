---
title: AI Eval 与 Trace 工作簿
type: template
status: active
domain: AI-Architect
created: 2026-05-09
updated: 2026-05-09
---

# AI Eval 与 Trace 工作簿

> 目标：把“感觉效果不错”改造成“可回归、可比较、可上线、可复盘”的工程证据。

## 核心原则

AI 系统的测试不是只测代码正确性，而是同时测：

`任务完成质量 -> 证据可信度 -> 安全边界 -> 工具行为 -> 成本延迟 -> 线上漂移`

## 1. Eval 目标定义

| 项目 | 内容 |
|---|---|
| 应用名称 |  |
| 任务类型 | RAG / Agent / Copilot / Workflow / LLMOps |
| 目标用户 |  |
| 核心业务指标 |  |
| AI 质量指标 |  |
| 上线门槛 |  |
| 不可接受失败 |  |

示例：

- RAG：答案正确率、引用准确率、拒答质量、越权召回率。
- Agent：任务完成率、工具调用准确率、高风险拦截率、人工采纳率。
- LLMOps：回归通过率、成本下降、延迟稳定性、策略命中率。

## 2. Eval Set 设计

### Case 类型

| 类型 | 目的 | 占比建议 |
|---|---|---:|
| Happy path | 验证主流程能完成 | 30% |
| Edge case | 验证边界和异常输入 | 20% |
| Negative / refusal | 验证该拒答时拒答 | 15% |
| Permission | 验证不越权 | 10% |
| Safety | 验证安全策略 | 10% |
| Regression | 验证历史 bad case 不复发 | 15% |

### Case 模板

| 字段 | 内容 |
|---|---|
| case_id |  |
| task_type |  |
| user_role |  |
| input |  |
| context / docs |  |
| expected_behavior |  |
| expected_answer |  |
| must_cite |  |
| must_refuse | true / false |
| risk_tags | prompt_injection / pii / permission / tool_abuse / hallucination |
| severity | P0 / P1 / P2 / P3 |

## 3. 指标体系

### 通用指标

| 指标 | 含义 | 通过标准 |
|---|---|---|
| Correctness | 回答或动作是否正确 | 核心任务达到目标阈值 |
| Faithfulness | 是否基于给定证据 | 不编造证据 |
| Relevance | 是否回答用户问题 | 不跑题 |
| Refusal Quality | 该拒答时是否正确拒答 | 高风险拒答必须准确 |
| Safety | 是否触发安全风险 | P0 风险为 0 |
| Latency | p50 / p95 / p99 延迟 | 满足用户体验 |
| Cost | 单任务成本 | 在预算内 |

### RAG 指标

- retrieval recall
- context precision
- citation accuracy
- answer faithfulness
- permission leakage rate
- stale knowledge hit rate

### Agent 指标

- task completion rate
- plan correctness
- tool call accuracy
- tool argument validity
- side-effect safety
- human approval hit rate
- rollback success rate

### LLMOps 指标

- eval pass rate
- regression failure rate
- model fallback rate
- prompt version drift
- cost per successful task
- trace coverage

## 4. Grader 设计

| Grader 类型 | 适用场景 | 注意事项 |
|---|---|---|
| Exact match | 分类、格式、结构化输出 | 简单可靠，但覆盖有限 |
| Rule-based | 拒答、引用、字段、权限 | 适合上线 gate |
| LLM-as-judge | 语义正确性、解释质量 | 需要标注 rubric 和抽样复核 |
| Human review | 高风险、主观质量 | 成本高，但适合 gold set |
| Hybrid | 生产级 eval | 规则兜底 + LLM 判断 + 人工抽检 |

### Rubric 模板

| 评分项 | 0 分 | 1 分 | 2 分 |
|---|---|---|---|
| 正确性 | 错误或误导 | 部分正确 | 完全正确 |
| 证据性 | 无证据或编造 | 有证据但不完整 | 证据充分且引用准确 |
| 安全性 | 泄露或越权 | 有风险但被拦截 | 安全处理 |
| 可用性 | 用户无法使用 | 需要改写 | 可直接使用 |

## 5. Trace Schema

一次请求至少要能复盘：

| 字段 | 示例 | 用途 |
|---|---|---|
| trace_id | uuid | 串联全链路 |
| timestamp | 2026-05-09T10:00:00Z | 时间定位 |
| app_id | enterprise-rag | 应用归属 |
| user_group | support-agent | 权限和人群分析 |
| task_type | rag_qa | 任务分类 |
| input_hash | hash | 隐私保护下的问题聚合 |
| model | gpt-x / local-model | 模型版本 |
| prompt_version | prompt:v12 | prompt 回滚 |
| retrieval_query | query_hash / safe text | 检索复盘 |
| retrieved_doc_ids | doc ids | 知识来源 |
| tool_calls | name, args hash, status | 工具行为审计 |
| output_hash | hash | 输出追踪 |
| latency_ms | 1200 | 性能 |
| input_tokens |  | 成本 |
| output_tokens |  | 成本 |
| cost_usd |  | FinOps |
| safety_flags | pii, injection | 安全 |
| user_feedback | up/down/reason | 质量闭环 |

## 6. Release Gate

| Gate | 必须通过 |
|---|---|
| Quality gate | 核心 eval 指标达到阈值 |
| Safety gate | P0/P1 安全用例全部通过 |
| Permission gate | 越权访问和越权输出为 0 |
| Cost gate | 单任务成本和日预算可控 |
| Latency gate | p95 达标或有异步兜底 |
| Regression gate | 历史 bad case 不复发 |
| Human gate | 业务、安全、架构 Owner 签字 |

## 7. Bad Case 回灌

每个线上 bad case 都要记录：

| 字段 | 内容 |
|---|---|
| bad_case_id |  |
| 来源 | 用户反馈 / 监控 / 人工抽检 / incident |
| 问题类型 | hallucination / retrieval / permission / tool / safety / latency / cost |
| 严重级别 | P0 / P1 / P2 / P3 |
| 根因 |  |
| 修复动作 | prompt / data / retrieval / model / tool / policy |
| 是否进入 eval set | yes / no |
| 回归结果 | pass / fail |

## 8. 面试表达

用一句话讲：

> 我不是只靠人工感觉判断 AI 效果，而是把 eval set、grader、trace、release gate 和 bad case 回灌接成闭环，让模型、prompt、知识和工具变更都能被回归验证。

用三分钟讲：

> 我会先把业务指标拆成 AI 质量指标，例如 RAG 的 correctness、faithfulness、citation accuracy，Agent 的 task completion、tool accuracy 和 side-effect safety。然后按 happy path、edge case、拒答、权限、安全和历史 bad case 构造 eval set。上线前用规则、LLM-as-judge 和人工复核组合做评测；上线后用 trace 记录模型、prompt、检索、工具、token、延迟和用户反馈。任何线上 bad case 都会分类、修复并回灌到 regression eval。

## 外部参考

- [OpenAI Evals guide](https://platform.openai.com/docs/guides/evals)
- [OpenAI Agents SDK tracing](https://openai.github.io/openai-agents-python/tracing/)
- [RAGAS documentation](https://docs.ragas.io/)
- [promptfoo documentation](https://www.promptfoo.dev/docs/intro/)
- [DeepEval documentation](https://deepeval.com/docs/getting-started)
- [Langfuse documentation](https://langfuse.com/docs)
- [Phoenix documentation](https://arize.com/docs/phoenix)

## 关联

- [[../08-Playbooks/AI 生产化 Readiness Playbook|AI 生产化 Readiness Playbook]]
- [[../05-Topics/LLMOps 与 AgentOps 架构师视角|LLMOps 与 AgentOps 架构师视角]]
- [[../05-Topics/RAG 架构师视角|RAG 架构师视角]]
- [[../05-Topics/Agent 架构师视角|Agent 架构师视角]]
- [[./AI 架构设计模板|AI 架构设计模板]]
