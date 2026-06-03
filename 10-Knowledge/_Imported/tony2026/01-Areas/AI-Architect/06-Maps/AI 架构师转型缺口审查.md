---
title: AI 架构师转型缺口审查
type: gap-review
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# AI 架构师转型缺口审查

> 目标：从“我知道 AI 架构师应该懂什么”，推进到“我能准确、快速地落地一个 AI 项目，并把它转化为岗位能力、项目成果和面试证据”。

## 一句话结论

当前 `AI-Architect` 领域已经具备完整的认知骨架：能力全景、迁移路线、RAG/Agent/LLMOps 专题、设计模板、面试表达和作品集样例。

但如果目标是“准确、快速落地转型”，还欠缺四类硬东西：

1. **转型诊断**：我现在在哪、差多少、先补哪块。
2. **落地作战台**：第一批项目怎么选、怎么排、每天做什么。
3. **生产化证据**：eval、trace、SLO、release gate、incident、成本、安全这些可验证交付物。
4. **真实化转换**：如何把现有经历改写成 AI 架构作品集和面试 STAR。

## 当前覆盖评分

| 能力层 | 当前状态 | 评分 | 判断 |
|---|---:|---:|---|
| 世界观与能力模型 | 已成体系 | 85 | 能解释 AI 架构师和传统架构师的差异 |
| 专题覆盖 | 覆盖主干 | 80 | RAG、Agent、LLMOps、安全、成本、数据都有入口 |
| 面试表达 | 有骨架 | 70 | 还缺模拟答案和追问训练 |
| 作品集结构 | 有模板和样例 | 75 | 还缺把本人真实经历映射进去的转换工具 |
| 生产化落地 | 偏框架化 | 55 | 缺 readiness checklist、eval workbook、runbook |
| 工具链选型 | 偏缺 | 45 | 还没把主流框架、平台、观测、评测、安全工具接到决策表里 |
| 组织转型 | 有方向 | 55 | 缺 stakeholder map、治理机制、平台推广策略 |
| 快速转型执行 | 偏缺 | 50 | 90 天路线有了，但缺 7/30/60 天作战节奏和评分门槛 |

## 对照外部框架后的缺口

### 1. NIST AI RMF：治理闭环还不够硬

NIST AI Risk Management Framework 的主线是 `Govern -> Map -> Measure -> Manage`。这说明 AI 架构不是只画系统图，还要能定义风险治理、场景上下文、度量方式和持续管理机制。

当前已有安全治理专题，但还缺：

- AI risk register
- risk acceptance 记录
- 模型、数据、prompt、工具的变更审批
- 第三方模型供应商风险管理
- 高风险场景的责任人和升级路径

已补：[[../08-Playbooks/AI 生产化 Readiness Playbook|AI 生产化 Readiness Playbook]]。

### 2. OWASP LLM / Agentic AI：威胁模型还不够细

OWASP 的 LLM Top 10 和 Agentic AI Threats 说明：AI 安全不是传统应用安全的简单延伸，核心风险包括 prompt injection、sensitive information disclosure、supply chain、excessive agency、tool abuse、memory poisoning、goal manipulation 等。

当前已有安全治理，但还缺：

- RAG threat model checklist
- Agent threat model checklist
- tool gateway 安全基线
- prompt / memory / tool / retrieval 的分层攻击面
- 红队用例库和上线阻断条件

已补：[[../07-Templates/AI 安全威胁建模模板|AI 安全威胁建模模板]]。

### 3. OpenAI Agents / Evals：评测与追踪还不够可操作

现代 AI 应用落地越来越依赖 eval、trace、guardrails 和任务级观测。仅有“要评测”的意识还不够，必须知道 eval set 怎么建、grader 怎么设计、trace 看什么、线上 bad case 怎么回灌。

当前已有 eval 概念，但还缺：

- eval dataset 设计模板
- 自动 grader / 人工复核规则
- trace 字段规范
- prompt/model/dataset 版本联动
- 上线 gate 和回归门槛

已补：[[../07-Templates/AI Eval 与 Trace 工作簿|AI Eval 与 Trace 工作簿]]。

### 4. Cloud Well-Architected：生产化五大支柱还不够完整

Azure、Google Cloud 等架构框架通常强调 reliability、security、cost optimization、operational excellence、performance efficiency。AI workload 也逃不开这些，只是指标形态变了。

当前已有成本延迟、安全，但还缺：

- AI SLO / SLA 定义
- 模型调用失败降级策略
- release gate 与 rollback runbook
- incident 分类和演练
- 成本预算、配额、限流和 FinOps 报表

已补：[[../08-Playbooks/AI 生产运行 Runbook|AI 生产运行 Runbook]]。

## 最高优先级缺口

### P0：没有“我现在该怎么转”的作战台

现在文档能学习，但还不能每天驱动行动。

必须补：

- 自我能力诊断表
- 第一项目选择评分卡
- 7 天启动计划
- 30 天交付计划
- 每周产物检查
- 项目作品集转换规则

入口：[[../08-Playbooks/AI 架构师快速落地转型作战台|AI 架构师快速落地转型作战台]]

### P0：没有“生产化证据包”

面试和真实落地最怕只停留在 demo。必须能展示：

- 架构图
- eval 报告
- trace 样例
- 安全威胁模型
- 成本和延迟测算
- 灰度上线记录
- incident / postmortem

这批证据比“我会 LangChain / RAG / Agent”更有信号。

### P1：缺工具链决策表

需要把工具按架构职能分层，而不是收藏项目：

- 应用开发：OpenAI Agents SDK、LangGraph、LlamaIndex、Semantic Kernel
- RAG：向量库、全文检索、reranker、document parser、chunking pipeline
- Eval：OpenAI Evals、RAGAS、promptfoo、DeepEval
- Observability：Langfuse、Phoenix、OpenTelemetry
- Guardrails：policy engine、PII 检测、prompt injection 检测、tool gateway
- Platform：model gateway、prompt registry、dataset registry、cost dashboard

已补：[[./AI 架构师工具链决策地图|AI 架构师工具链决策地图]]。

### P1：缺“场景选择与 ROI”方法

快速转型不能从最炫的 Agent 开始，要从最高胜率场景开始。

需要补：

- 场景评分卡：价值、可行性、风险、数据质量、上线阻力
- RAG / Agent / Workflow / Fine-tuning / BI Copilot 的选型规则
- 业务指标到 eval 指标的映射
- PoC、Pilot、Production 三阶段门槛

### P1：缺真实经历迁移器

传统互联网架构师通常已有很多能力，但不会翻译成 AI 语言。

需要补：

- 高并发系统 -> model gateway / capacity / rate limit
- 权限系统 -> RAG ACL / tool permission / trust boundary
- 数据平台 -> knowledge pipeline / eval dataset / feature-quality mindset
- 稳定性体系 -> AI SLO / trace / fallback / incident
- 平台工程 -> LLMOps / AgentOps / developer platform

## 应该补的 12 个交付物

| 优先级 | 交付物 | 解决的问题 |
|---|---|---|
| P0 | [[../08-Playbooks/AI 架构师快速落地转型作战台|AI 架构师快速落地转型作战台]] | 每天怎么推进转型 |
| P0 | AI 自我能力诊断表 | 我当前最短板是什么 |
| P0 | 第一 AI 项目选择评分卡 | 先做哪个项目最稳 |
| P0 | [[../08-Playbooks/AI 生产化 Readiness Playbook|AI 生产化 Readiness Playbook]] | 怎么判断能不能上线 |
| P0 | [[../07-Templates/AI Eval 与 Trace 工作簿|AI Eval 与 Trace 工作簿]] | 怎么证明效果变好 |
| P1 | [[../07-Templates/AI 安全威胁建模模板|AI 安全威胁建模模板]] | 怎么识别和拦截 AI 风险 |
| P1 | [[./AI 架构师工具链决策地图|AI 架构师工具链决策地图]] | 工具怎么选，为什么选 |
| P1 | [[../08-Playbooks/AI 生产运行 Runbook|AI 生产运行 Runbook]] | 上线后怎么值守和响应 |
| P1 | 真实经历迁移工作表 | 怎么把旧经验转成 AI 架构能力 |
| P1 | STAR 项目表达样例 | 怎么讲得像做过、懂取舍 |
| P2 | 行业作品集样例 | 怎么贴近目标岗位 |
| P2 | AI 架构评审案例库 | 怎么练复杂场景判断 |

## 最快转型路线

### 7 天：从学习者切到执行者

- Day 1：做自我能力诊断，确定目标岗位：AI 应用架构师 / AI 平台架构师 / AI 治理架构师。
- Day 2：选一个第一项目，不超过 4 周能出结果。
- Day 3：写项目 one-pager：业务目标、用户、AI 边界、失败兜底。
- Day 4：画架构图，明确 RAG / Agent / Workflow / LLMOps 模式。
- Day 5：定义 eval set 和上线门槛。
- Day 6：补安全威胁模型和成本延迟估算。
- Day 7：形成作品集草稿。

### 30 天：做出一个可讲的 production-like 项目

- 完成最小可用 AI 应用。
- 有 eval set、trace、bad case、成本估算。
- 有一版安全评审和上线 readiness。
- 有 1 分钟、3 分钟、10 分钟项目表达。

### 60 天：把单点项目升级为架构能力

- 把一个项目抽象成模板。
- 补 model gateway、prompt registry、eval regression、release gate。
- 形成第二个作品集：Agent 或 LLMOps。
- 开始模拟 AI 架构系统设计面试。

### 90 天：形成转型闭环

- 至少 2 个作品集，一个应用型，一个平台/治理型。
- 能独立评审 AI 项目方案。
- 能解释成本、安全、评测、上线、组织落地。
- 能把传统架构经验自然迁移到 AI 语境。

## 不要再优先做什么

- 不要继续无限补“AI 名词解释”。
- 不要先追最复杂的 autonomous agent。
- 不要只收集开源项目而不形成选型表。
- 不要只写作品集样例而不做 eval 和 trace。
- 不要把转型路线做成泛泛学习计划。

## 下一批最该做

1. 已补 [[../08-Playbooks/AI 架构师快速落地转型作战台|AI 架构师快速落地转型作战台]]。
2. 已补 [[../08-Playbooks/AI 生产化 Readiness Playbook|AI 生产化 Readiness Playbook]]。
3. 已补 [[../07-Templates/AI Eval 与 Trace 工作簿|AI Eval 与 Trace 工作簿]]。
4. 已补 [[../07-Templates/AI 安全威胁建模模板|AI 安全威胁建模模板]]。
5. 已补 [[./AI 架构师工具链决策地图|AI 架构师工具链决策地图]]。
6. 下一步：补真实经历迁移工作表、STAR 项目表达样例和 AI 架构评审案例库。

## 外部参考

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST AI RMF Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework/generative-artificial-intelligence)
- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP Agentic AI Threats and Mitigations](https://owasp.org/www-project-agentic-ai-threats-and-mitigations/)
- [OpenAI Evals guide](https://platform.openai.com/docs/guides/evals)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [Azure Well-Architected Framework for AI workloads](https://learn.microsoft.com/en-us/azure/well-architected/ai/)
- [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework)

## 关联

- [[../专题总览|AI Architect 专题总览]]
- [[./AI 架构师迁移地图|AI 架构师迁移地图]]
- [[./AI 架构师专题分解图|AI 架构师专题分解图]]
- [[../08-Playbooks/AI 架构师 90 天迁移 Playbook|AI 架构师 90 天迁移 Playbook]]
- [[../08-Playbooks/AI 生产化 Readiness Playbook|AI 生产化 Readiness Playbook]]
- [[../08-Playbooks/AI 生产运行 Runbook|AI 生产运行 Runbook]]
- [[../07-Templates/AI Eval 与 Trace 工作簿|AI Eval 与 Trace 工作簿]]
- [[../07-Templates/AI 安全威胁建模模板|AI 安全威胁建模模板]]
- [[./AI 架构师工具链决策地图|AI 架构师工具链决策地图]]
- [[../09-Portfolio/作品集样例索引|作品集样例索引]]
