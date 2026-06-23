---
title: AI 架构师快速落地转型作战台
type: playbook
status: active
domain: AI-Architect
created: 2026-05-05
updated: 2026-05-05
---

# AI 架构师快速落地转型作战台

> 用法：不要把它当学习清单，而是当转型项目管理台。每天只问三件事：今天补哪个短板、产出什么证据、怎么进入作品集。

## 目标

用 30 天完成一次从传统互联网架构师到 AI 架构师的可验证迁移：

- 能设计一个 production-like AI 项目。
- 能解释 RAG / Agent / LLMOps 的边界和取舍。
- 能建立 eval、trace、安全、成本、上线门槛。
- 能把项目沉淀为作品集和面试表达。

## 第一步：确定目标岗位

| 目标 | 优先练什么 | 作品集组合 |
|---|---|---|
| AI 应用架构师 | RAG、Agent、Workflow、业务场景识别 | RAG + Agent |
| AI 平台架构师 | Model Gateway、LLMOps、Eval、Observability、Cost | RAG + LLMOps |
| AI 治理架构师 | AI Security、Risk、Compliance、Release Gate | RAG + 安全治理 |
| AI 架构负责人 | 架构评审、组织落地、平台推广、治理机制 | RAG + Agent + LLMOps |

默认建议：先按 **AI 应用架构师** 起步，因为它最快产生业务可见成果，再补平台和治理。

## 第二步：自我能力诊断

按 1-5 分自评：

| 能力 | 1 分 | 3 分 | 5 分 | 我的分数 |
|---|---|---|---|---|
| 场景识别 | 只会说“接 AI” | 能判断 RAG/Agent/Workflow | 能用 ROI、风险、数据质量排序场景 |  |
| RAG | 知道向量库 | 能设计检索、权限、引用 | 能做 eval、trace、知识治理和安全 |  |
| Agent | 知道 tool use | 能设计 workflow + tool gateway | 能处理高风险动作、幂等、审计、回滚 |  |
| LLMOps | 知道 prompt 管理 | 能设计模型网关和 trace | 能设计 eval gate、成本治理、灰度发布 |  |
| Eval | 知道要评测 | 能写 eval set | 能做自动/人工评测、回归和上线门槛 |  |
| 安全治理 | 知道 prompt injection | 能做基础防护 | 能做 AI threat model、risk register、red team |  |
| 成本延迟 | 知道 token 成本 | 能估算延迟成本 | 能做 routing、cache、限流、容量和 FinOps |  |
| 面试表达 | 能讲概念 | 能讲项目 | 能讲取舍、失败、复盘和证据 |  |

低于 3 分的能力，就是未来 30 天优先补的短板。

## 第三步：选择第一项目

不要从最酷项目开始，从最高胜率项目开始。

| 评分项 | 1 分 | 3 分 | 5 分 |
|---|---|---|---|
| 业务价值 | 价值模糊 | 能提高效率 | 有明确成本、效率或收入指标 |
| 数据可得性 | 数据难拿 | 有部分数据 | 数据可拿、可清洗、有 Owner |
| 风险可控 | 涉及高风险决策 | 可人工确认 | 只读或建议型，风险低 |
| 4 周可交付 | 依赖太多系统 | 可做 PoC | 可做 production-like demo |
| 作品集信号 | 像玩具 demo | 有业务背景 | 能体现 eval、安全、成本、上线 |

优先选择总分最高的项目。默认优先级：

1. 企业知识库 RAG。
2. 审批型 Agent Workflow。
3. 企业 LLMOps 最小平台。

## 第四步：7 天启动节奏

### Day 1：定位

- 选择目标岗位。
- 完成自我能力诊断。
- 明确第一项目。
- 输出：`转型目标 + 第一项目 one-liner`。

### Day 2：业务边界

- 写业务痛点。
- 明确 AI 做什么、不做什么。
- 定义人工介入点和失败兜底。
- 输出：`业务边界说明`。

### Day 3：架构图

- 选择 RAG / Agent / Workflow / LLMOps 模式。
- 画核心链路。
- 标出权限、数据、模型、工具、eval、trace。
- 输出：`架构图 v1`。

### Day 4：数据与知识

- 列数据源。
- 定义 metadata、权限、数据质量、更新策略。
- 输出：`数据和知识设计`。

### Day 5：Eval 与 Trace

- 构造 20-50 条 eval case。
- 定义 correctness、faithfulness、safety、latency、cost 指标。
- 设计 trace 字段。
- 输出：`eval set v1 + trace schema`。

### Day 6：安全与成本

- 做 threat model。
- 定义高风险动作和拦截规则。
- 估算 token、延迟、QPS、模型成本。
- 输出：`安全和成本评审`。

### Day 7：作品集草稿

- 按 [[../07-Templates/AI 架构师作品集模板|AI 架构师作品集模板]] 填一版。
- 写 1 分钟、3 分钟、10 分钟表达。
- 输出：`作品集草稿 v1`。

## 第五步：30 天交付节奏

### Week 1：完成设计闭环

- one-pager
- 架构图
- 数据/权限设计
- eval set v1
- threat model v1

### Week 2：完成最小原型

- 跑通主链路。
- 接入至少一个真实或仿真数据源。
- 记录 trace。
- 初步跑 eval。

### Week 3：补生产化能力

- 加入 fallback。
- 加入日志和观测。
- 加入成本估算。
- 加入安全拦截和人工确认。

### Week 4：形成作品集

- eval 报告。
- 成本/延迟报告。
- 上线 readiness checklist。
- 失败案例和复盘。
- 面试表达稿。

## 第六步：每周检查门槛

| 周期 | 通过标准 | 不通过说明 |
|---|---|---|
| Week 1 | 能讲清业务目标、边界、架构和风险 | 还停留在泛泛学概念 |
| Week 2 | 能跑通主链路并留下 trace | 还只是文档，没有工程证据 |
| Week 3 | 有 eval、安全、成本和 fallback | 还只是 demo，不能上线 |
| Week 4 | 能沉淀成作品集和面试表达 | 做了项目但讲不出架构能力 |

## 第七步：作品集证据清单

一个合格 AI 架构作品至少要有：

- 业务目标：解决什么问题，为什么适合 AI。
- 任务边界：AI 做什么，不做什么。
- 架构图：链路、组件、数据、模型、工具、eval、trace。
- 数据设计：数据源、权限、metadata、质量、新鲜度。
- Eval：case、指标、通过标准、bad case。
- 安全：threat model、权限、敏感数据、高风险动作。
- 成本延迟：token、模型、cache、routing、容量。
- 上线：灰度、回滚、监控、incident。
- 复盘：失败案例、改进动作、下一阶段。
- 表达：1 分钟、3 分钟、10 分钟版本。

## 第八步：转型判断标准

你不是读完这些文档就转型成功，而是达到下面标准：

- 面对一个 AI 需求，能判断是否适合 AI。
- 能在 RAG、Agent、Workflow、Fine-tuning、传统系统之间做取舍。
- 能画出生产化架构，而不是 demo 架构。
- 能定义 eval，而不是只说“效果不错”。
- 能解释安全风险，而不是只说“加权限”。
- 能估算成本和延迟，而不是只说“调用模型”。
- 能把传统系统经验迁移成 AI 架构能力。
- 能用一个项目讲出业务、技术、风险和复盘。

## 立即开始

如果现在就开始，建议顺序：

1. 用本文件完成自我诊断。
2. 从 [[../09-Portfolio/企业知识库 RAG 架构作品集样例|企业知识库 RAG 架构作品集样例]] 复制结构。
3. 选择一个真实或仿真的内部知识场景。
4. 7 天内完成 one-pager、架构图、eval set、threat model、作品集草稿。
5. 30 天内补齐 trace、readiness、成本延迟和面试表达。

## 关联

- [[../06-Maps/AI 架构师转型缺口审查|AI 架构师转型缺口审查]]
- [[./AI 架构师 90 天迁移 Playbook|AI 架构师 90 天迁移 Playbook]]
- [[./AI 项目从 0 到 1 落地 Playbook|AI 项目从 0 到 1 落地 Playbook]]
- [[../09-Portfolio/作品集样例索引|作品集样例索引]]
- [[../10-Interview-Kit/AI 架构师表达总纲|AI 架构师表达总纲]]
