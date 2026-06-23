---
title: AI 架构评审 Playbook
type: playbook
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# AI 架构评审 Playbook

> 用于评审一个 AI 应用、RAG、Agent、AI 平台或 AI 功能是否具备上线和规模化条件。

## 适用场景

- 一个 AI POC 准备进入生产。
- 一个传统系统准备接入 LLM / RAG / Agent。
- 一个团队要上线 AI Copilot、自动化 Agent、知识库问答、智能客服、代码助手、数据分析助手。
- 一个企业要建设统一 AI 平台、模型网关、LLMOps 或 AgentOps。

## 评审核心问题

一句话：

`这个 AI 系统要替谁完成什么任务，在什么边界内，依据什么知识，能调用哪些工具，如何评测，如何上线，失败了如何兜底？`

## Step 1：业务与任务边界

必须问清楚：

- 目标用户是谁？
- 任务是什么？是问答、生成、抽取、分析、推荐、规划，还是执行？
- 哪些任务明确不支持？
- 成功标准是什么？
- AI 是 Copilot、Autopilot 还是 Agent？
- 哪些环节需要人工确认？

评审输出：

- 任务范围清单
- 不支持范围清单
- 人工介入点
- 业务成功指标

## Step 2：模型与能力选型

必须问清楚：

- 选用哪些模型？为什么？
- 是否需要多模型路由、fallback、降级？
- prompt、RAG、fine-tuning、tool calling 如何分工？
- 是否需要结构化输出？
- 是否有模型版本管理和回归策略？

典型判断：

| 问题 | 优先方案 |
|---|---|
| 知识不在模型里 | RAG |
| 输出格式稳定 | structured output |
| 需要执行动作 | tool calling / agent workflow |
| 领域语言强、任务稳定 | fine-tuning 候选 |
| 风险高、动作不可逆 | human-in-the-loop |

## Step 3：数据、知识与上下文

必须问清楚：

- 数据来源是什么？
- 知识是否新鲜、可信、可追溯？
- RAG 是否有 metadata、权限过滤、引用和版本？
- 用户输入、上传文件、日志、反馈是否含敏感数据？
- 是否有数据保留、删除和训练使用边界？

评审输出：

- 数据流图
- 知识库结构
- 权限过滤方案
- 敏感数据清单

## Step 4：RAG / Agent / Workflow 架构

如果是 RAG：

- chunking 策略是什么？
- embedding 和检索策略是什么？
- 是否 hybrid search / rerank？
- 如何做引用、grounding 和 hallucination 控制？
- 如何评测 retrieval 和 answer quality？

如果是 Agent：

- Agent 状态如何管理？
- 可以调用哪些工具？
- 工具权限如何限制？
- 高风险动作如何审批？
- 失败如何重试、回滚、终止？
- 是否有 audit trail？

如果是 Workflow：

- 哪些步骤确定性执行？
- 哪些步骤交给模型判断？
- 哪些步骤需要人工确认？

## Step 5：评测与上线门槛

必须问清楚：

- 是否有 eval dataset / golden set？
- 是否覆盖正常任务、边界任务、恶意输入和高风险任务？
- 是否有回归测试？
- 是否有人类评审和线上反馈闭环？
- 上线门槛是什么？

评测维度：

- task success
- answer faithfulness
- retrieval quality
- tool-call correctness
- policy violation
- latency
- cost per successful task
- escalation / handoff rate

## Step 6：安全、隐私与治理

必须问清楚：

- 是否做过 prompt injection / jailbreak / data leakage 测试？
- 工具调用是否最小权限？
- 高风险动作是否审批？
- 是否记录 prompt、retrieval、tool call 和输出审计？
- 是否有数据脱敏、保留和删除策略？
- 是否有 kill switch 和 incident response？

重点风险：

- prompt injection
- RAG 泄露
- tool abuse
- memory poisoning
- sensitive data in logs
- cross-tenant leakage
- over-automation

## Step 7：工程运行与成本

必须问清楚：

- 延迟预算是多少？
- 并发和容量如何估算？
- token 成本如何监控？
- 是否有缓存、batching、fallback？
- 模型供应商故障如何降级？
- 是否有 trace、metrics、logs、dashboard？

运行指标：

- p50 / p95 latency
- cost per request
- cost per successful task
- model error rate
- retrieval latency
- tool failure rate
- escalation rate

## Step 8：组织与责任

必须问清楚：

- business owner 是谁？
- model / prompt / data / tool / security owner 分别是谁？
- 谁负责 eval 更新？
- 谁处理事故？
- 谁批准上线和例外？

评审输出：

- RACI
- risk register
- rollout plan
- operation runbook

## 评审结论模板

| 结论 | 条件 |
|---|---|
| 可以上线 | 关键 eval 通过，安全控制到位，owner 明确，有回滚 |
| 有条件上线 | 存在中风险，但有补偿控制、期限和 owner |
| 暂缓上线 | 任务边界、数据权限、eval 或高风险工具控制不清 |
| 不建议上线 | 存在不可接受的数据、安全、合规或业务风险 |

## 关联

- [[../05-Topics/AI 时代架构师能力全景|AI 时代架构师能力全景]]
- [[./AI 项目从 0 到 1 落地 Playbook|AI 项目从 0 到 1 落地 Playbook]]
- [[../07-Templates/AI 架构设计模板|AI 架构设计模板]]
- [[../../AI-Engineering/09-Templates/AI 安全评审模板|AI 安全评审模板]]
- [[../../AI-Engineering/09-Templates/Agent 上线门槛模板|Agent 上线门槛模板]]

