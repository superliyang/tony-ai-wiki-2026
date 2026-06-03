---
title: AI 架构师 STAR 项目表达样例
type: interview-template
status: active
domain: AI-Architect
created: 2026-05-09
updated: 2026-05-09
---

# AI 架构师 STAR 项目表达样例

> 目标：把项目讲成“业务问题 + 架构判断 + 生产化证据 + 复盘能力”，而不是讲成“我用了某个框架”。

## STAR+E 结构

传统 STAR：

`Situation -> Task -> Action -> Result`

AI 架构师建议升级为 STAR+E：

`Situation -> Task -> Architecture -> Result -> Evidence`

其中 Evidence 是关键：eval、trace、安全、成本、上线、复盘。

## 通用模板

### 1 分钟版本

> 背景是 `业务问题`。我负责 `角色和范围`。我没有直接做一个 demo，而是先定义 `任务边界和风险`，然后设计了 `核心架构模式`。落地时重点补了 `eval/trace/security/cost/release`。结果是 `业务或技术结果`。这个项目证明我能把 AI 系统从想法推进到可验证、可治理、可上线的架构。

### 3 分钟版本

> 当时的 Situation 是……  
> 我的 Task 是……  
> Architecture 上我做了几个判断：第一……第二……第三……  
> 落地过程中我补了 eval、trace、安全和上线门槛……  
> Result 是……  
> 最重要的 Evidence 是……  
> 复盘来看，最大教训是……

### 追问回答骨架

| 追问 | 回答重点 |
|---|---|
| 为什么不用传统系统？ | 自然语言、非结构化知识、多源上下文、解释成本 |
| 为什么不用 autonomous agent？ | 风险、状态、权限、审计、责任边界 |
| 怎么证明效果？ | eval set、指标、baseline、bad case 回归 |
| 怎么防幻觉？ | RAG、引用、faithfulness eval、拒答、人工确认 |
| 怎么防越权？ | ACL、tool permission、trust boundary、trace |
| 怎么上线？ | pilot、release gate、灰度、rollback、SLO |
| 怎么控成本？ | routing、cache、token、quota、budget、cost per task |

## 样例 1：企业知识库 RAG

### 1 分钟

> 我做过一个企业知识库 RAG 方案，背景是客服和运营的知识分散在 Wiki、FAQ、工单和文档里，传统搜索只能找资料，不能给可信答案。我负责架构设计和生产化评审。我的重点不是简单接向量库，而是把知识治理、权限过滤、hybrid search、rerank、引用校验、eval 和 trace 接成闭环。上线前我们用高频问题、过期知识、权限隔离和 prompt injection 做 eval，线上通过 bad case 回灌持续优化。这个项目证明我能把 RAG 从 demo 做成可信知识系统。

### 3 分钟

> Situation 是企业知识分散，客服和运营重复问专家，回答口径不一致。Task 是做一个可信问答助手，但不能泄露无权限知识，也不能编造答案。Architecture 上我做了三个关键判断：第一，使用 hybrid search + rerank，而不是只用向量库；第二，权限过滤前置，避免无权限内容进入上下文；第三，答案必须引用证据，引用不足就拒答或转人工。落地时我设计了 metadata、knowledge owner、eval set、trace schema 和 bad case 运营。Result 是系统从 PoC 进入受控灰度，专家重复答疑下降，知识治理责任更清楚。Evidence 是 eval 报告、trace、权限测试、引用准确率和失败案例复盘。

### 高信号追问

问：RAG 最大坑是什么？

答：

> 最大坑不是向量库，而是知识质量、权限、引用和评测。很多 RAG demo 能回答，但生产里会遇到旧文档、相似制度、越权内容和无证据编造。所以我会先设计 metadata 和 ACL，再设计 retrieval eval、citation accuracy 和 bad case 回灌。

## 样例 2：审批型 Agent

### 1 分钟

> 我做过审批型 Agent 的架构设计，目标是让 AI 帮审批人检查材料、查规则、查预算和生成风险建议。我的核心判断是不能一开始做完全 autonomous agent，而要做 bounded agent：workflow 控状态，Agent 做理解和建议，tool gateway 控工具权限，高风险动作必须人工确认。上线前重点做了 tool eval、风险召回、安全威胁建模、trace 和回滚策略。这个项目证明我理解 Agent 落地的边界：可控、可审计、可回滚。

### 3 分钟

> Situation 是审批流程材料不完整、规则分散、审批人需要跨系统查询。Task 是提升审批效率，但不能让 AI 越权决策。Architecture 上我把系统拆成确定性工作流、bounded agent、规则知识库、tool gateway、risk policy 和 human-in-the-loop。工具按风险分级：只读工具可以自动调用，低风险写操作需要幂等，高风险批准必须人工确认。Eval 覆盖材料缺失、金额超阈、规则冲突、工具失败、prompt injection。Result 是先从只读建议进入低风险辅助，而不是直接自动审批。Evidence 是工具调用 trace、审批确认记录、安全测试和 bad case 复盘。

### 高信号追问

问：为什么不用完全自主 Agent？

答：

> 审批系统有明确状态、权限和责任边界。完全自主 Agent 会让状态推进、工具调用和责任归属变得不可控。我会让 Agent 负责理解和建议，而不是负责最终决策；让 workflow 控制状态，让工具网关控制权限，让人审节点控制高风险动作。

## 样例 3：企业 LLMOps 平台

### 1 分钟

> 我设计过企业 LLMOps 平台方案，背景是多个团队各自接模型、各自写 prompt、各自看日志，导致成本不可控、效果不可比较、安全策略不一致。我设计的 MVP 包括 model gateway、prompt registry、eval gate、trace、cost dashboard 和 release gate。重点不是建大平台，而是先把模型调用、版本、评测、观测、成本和发布门槛接成最小治理闭环。

### 3 分钟

> Situation 是 AI 应用开始扩散，但每个团队独立接模型，缺少统一治理。Task 是做一个平台底座，降低接入成本并提高上线质量。Architecture 上我先选 anchor tenant，不做大而全平台，而是做 model gateway、prompt registry、dataset/eval registry、trace store、policy engine 和 cost dashboard。每次 prompt 或模型变更都要经过 regression eval 和灰度发布。Result 是平台从代理层升级为治理层。Evidence 是接入规范、eval gate、trace schema、成本归因和发布回滚记录。

### 高信号追问

问：模型网关和 LLMOps 平台的区别是什么？

答：

> 模型网关只是统一调用、鉴权、限流和路由；LLMOps 平台要进一步管理 prompt、dataset、eval、trace、release gate、成本和 incident。没有 eval 和发布门槛的网关只是代理层，不是治理平台。

## 低信号表达 vs 高信号表达

| 低信号 | 高信号 |
|---|---|
| 我用了 LangChain 做 RAG | 我设计了权限感知 RAG，并用 eval 和 trace 验证召回、引用和安全 |
| 我做了一个 Agent | 我把 Agent 限定在 workflow 内，工具分级，人审高风险动作 |
| 我接了多个模型 | 我设计了 model gateway、prompt registry、eval gate 和成本归因 |
| 效果还不错 | 我有 eval set、baseline、bad case 回归和线上反馈闭环 |
| 加了权限 | 我设计了 trust boundary、ACL 前置过滤、tool permission 和审计 |

## 关联

- [[./AI 架构师面试专题总览|AI 架构师面试专题总览]]
- [[./AI 架构师表达总纲|AI 架构师表达总纲]]
- [[../07-Templates/传统架构经验迁移到 AI 架构工作表|传统架构经验迁移到 AI 架构工作表]]
- [[../11-Case-Library/案例库索引|案例库索引]]
- [[../09-Portfolio/作品集样例索引|作品集样例索引]]
