---
title: AI 生产化 Readiness Playbook
type: playbook
status: active
domain: AI-Architect
created: 2026-05-09
updated: 2026-05-09
---

# AI 生产化 Readiness Playbook

> 目标：判断一个 AI 项目是否已经从 demo / PoC 进入 production-ready。核心不是“能跑”，而是“可评测、可追踪、可控权、可回滚、可治理、可承担业务后果”。

## 一句话标准

一个 AI 系统能上线，不是因为模型回答看起来不错，而是因为它已经具备：

`明确任务边界 -> 可验证 eval -> 可追踪 trace -> 可控安全策略 -> 可回滚发布 -> 可运营反馈闭环`

## Readiness 分级

| 等级 | 状态 | 特征 | 允许范围 |
|---|---|---|---|
| R0 | Demo | 单机或脚本可跑，无系统保障 | 个人演示 |
| R1 | PoC | 主链路可跑，有少量样例验证 | 小范围探索 |
| R2 | Pilot | 有 eval、trace、安全边界和灰度 | 受控试点 |
| R3 | Production | 有 SLO、发布门槛、回滚、监控和责任人 | 真实业务 |
| R4 | Platformized | 多团队复用，有治理、成本和平台能力 | 组织级推广 |

转型作品集至少要做到 **R2**；真实生产项目至少要做到 **R3**。

## 1. 业务与任务边界

### 必须回答

- 这个系统替谁完成什么任务？
- 用户输入是什么，输出是什么？
- AI 做什么、不做什么？
- 哪些场景必须拒答、转人工或降级？
- 出错后谁负责、怎么兜底？

### 上线门槛

| 检查项 | 必须达到 |
|---|---|
| 业务目标 | 有明确指标，如效率、成本、质量、转化、满意度 |
| 用户范围 | 首批用户、灰度范围、使用限制明确 |
| 任务边界 | 有正向用例、反向用例和拒答规则 |
| 人工介入 | 高风险场景有 human-in-the-loop |
| 兜底路径 | 模型失败、检索失败、工具失败时有降级 |

## 2. 数据、知识与权限

### 必须回答

- AI 依据什么数据和知识工作？
- 数据是否有 Owner、版本、更新频率和质量标准？
- 用户权限如何传递到检索、工具和输出？
- 日志是否会泄露敏感数据？

### 上线门槛

| 检查项 | 必须达到 |
|---|---|
| 数据来源 | 数据源、Owner、更新时间、可信等级清楚 |
| 权限控制 | RAG 检索、工具调用、输出展示均继承用户权限 |
| 敏感数据 | PII、密钥、财务、客户、合同等有识别和脱敏 |
| 数据质量 | 有过期、重复、冲突、缺失知识的治理机制 |
| 可追溯 | 回答、建议和动作能追溯到数据、知识或工具结果 |

## 3. 模型、Prompt 与工具边界

### 必须回答

- 为什么选择这个模型？
- Prompt 如何版本化、回滚和评审？
- 工具有哪些权限，是否会产生副作用？
- Agent 能否自由规划，还是受 workflow 约束？

### 上线门槛

| 检查项 | 必须达到 |
|---|---|
| 模型选择 | 有质量、成本、延迟、安全的选型理由 |
| Prompt 管理 | prompt 有版本、Owner、变更记录和回滚点 |
| 工具白名单 | tool schema、权限、参数校验、超时、重试明确 |
| 副作用控制 | 写操作、高风险动作必须人工确认或审批 |
| fallback | 模型不可用或工具失败时有降级策略 |

## 4. Eval 与质量门槛

### 必须回答

- eval set 覆盖哪些真实任务和失败模式？
- 用什么指标判断系统变好？
- 自动评测和人工复核怎么分工？
- 模型、prompt、知识、工具变更后如何回归？

### 上线门槛

| 检查项 | 必须达到 |
|---|---|
| Eval 集 | 覆盖 happy path、edge case、拒答、安全、权限、工具失败 |
| 指标 | correctness、faithfulness、safety、latency、cost 至少有定义 |
| 基线 | 有 baseline 和目标阈值 |
| 回归 | 关键变更必须跑 regression eval |
| Bad case | 线上 bad case 能回灌到 eval set |

## 5. Trace、观测与 SLO

### 必须回答

- 一次请求失败时，能否复盘完整链路？
- 线上是否能看到模型、prompt、retrieval、tool、cost、latency？
- AI 质量问题如何被发现和升级？

### 上线门槛

| 检查项 | 必须达到 |
|---|---|
| Trace ID | 每次请求有唯一 trace id |
| 关键字段 | app、user group、model、prompt、retrieval、tool、latency、token、cost |
| 质量信号 | 用户反馈、人工纠错、拒答率、fallback rate 可观测 |
| SLO | 定义可用性、p95 延迟、错误率、质量阈值、安全阈值 |
| 告警 | 成本异常、错误率异常、安全命中、质量下降可告警 |

## 6. 安全、隐私与治理

### 必须回答

- prompt injection、数据泄露、越权、tool abuse 如何防？
- 高风险动作是否有审批和审计？
- 第三方模型或工具的供应链风险如何管理？

### 上线门槛

| 检查项 | 必须达到 |
|---|---|
| Threat model | 完成 RAG / Agent / Tool / Data 分层威胁建模 |
| 权限边界 | 用户、模型、工具、数据之间的 trust boundary 清楚 |
| 安全测试 | 至少覆盖 prompt injection、越权、敏感数据、恶意文档 |
| 审计 | 高风险调用和策略命中可审计 |
| 风险接受 | 已知风险有 Owner、等级、缓解措施和接受记录 |

## 7. 发布、灰度与回滚

### 必须回答

- 生产发布前有哪些 gate？
- 灰度按照用户、场景、流量还是业务线推进？
- 触发什么条件必须回滚？

### 上线门槛

| 检查项 | 必须达到 |
|---|---|
| Release gate | eval、安全、成本、延迟和业务 Owner 均通过 |
| 灰度策略 | 内部试用 -> 小流量 -> 单业务线 -> 全量 |
| 回滚方案 | 可回滚模型、prompt、知识索引、工具开关和流量 |
| Kill switch | 高风险能力有一键关闭 |
| 变更记录 | 模型、prompt、数据、策略、工具变更可追溯 |

## 8. 成本、容量与 FinOps

### 必须回答

- 单次任务成本是多少？
- 峰值 QPS、并发、token 消耗如何估算？
- 模型路由、cache、限流和预算如何设计？

### 上线门槛

| 检查项 | 必须达到 |
|---|---|
| 成本模型 | 按 app、模型、token、工具、eval、缓存拆分 |
| 预算 | 有团队/应用预算和异常告警 |
| 容量 | 有峰值调用量、供应商限额、自部署容量估算 |
| 优化 | 有 cache、routing、context compression、batching 策略 |
| 限流 | 按用户、应用、租户、模型设置配额 |

## 9. 组织与责任

### 必须回答

- 谁负责业务指标？
- 谁负责知识质量？
- 谁负责模型、prompt、eval、工具、安全？
- incident 发生时谁决策回滚？

### 上线门槛

| 角色 | 职责 |
|---|---|
| Business Owner | 业务目标、用户范围、上线接受 |
| AI Architect | 架构边界、eval、治理和上线门槛 |
| Data Owner | 数据质量、权限、更新和敏感性 |
| Security Owner | 威胁建模、安全测试和风险接受 |
| SRE / Platform | 观测、SLO、容量、回滚和 incident |
| Product / Ops | 反馈运营、bad case 分类和改进闭环 |

## Readiness 评分表

每项 0-2 分：

- 0：缺失
- 1：有设计但未验证
- 2：已实现且有证据

| 类别 | 分数 |
|---|---:|
| 业务与任务边界 |  |
| 数据、知识与权限 |  |
| 模型、Prompt 与工具 |  |
| Eval 与质量门槛 |  |
| Trace、观测与 SLO |  |
| 安全、隐私与治理 |  |
| 发布、灰度与回滚 |  |
| 成本、容量与 FinOps |  |
| 组织与责任 |  |

判定：

- 0-8：Demo，不建议对外。
- 9-13：PoC，可以内部探索。
- 14-16：Pilot，可以受控灰度。
- 17-18：Production-ready，可以进入真实生产。

## 作品集怎么表达

面试里不要说“我做了一个 RAG / Agent”，要说：

> 我把它按 production readiness 做了分层评审：任务边界、数据权限、模型工具、eval、trace、安全、发布、成本和责任人。这个系统不是只跑通 demo，而是有上线门槛、回滚策略和持续治理机制。

## 外部参考

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework/generative-artificial-intelligence)
- [Azure Well-Architected Framework for AI workloads](https://learn.microsoft.com/en-us/azure/well-architected/ai/)
- [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework)

## 关联

- [[./AI 架构师快速落地转型作战台|AI 架构师快速落地转型作战台]]
- [[./AI 项目从 0 到 1 落地 Playbook|AI 项目从 0 到 1 落地 Playbook]]
- [[../07-Templates/AI Eval 与 Trace 工作簿|AI Eval 与 Trace 工作簿]]
- [[../07-Templates/AI 安全威胁建模模板|AI 安全威胁建模模板]]
- [[../06-Maps/AI 架构师转型缺口审查|AI 架构师转型缺口审查]]
