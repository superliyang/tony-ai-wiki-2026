---
title: AI 领域知识点总纲：点、线、面与层
type: topic
status: active
tags:
  - ai/topic
  - ai/knowledge-graph
  - ai/learning-system
created: 2026-04-12
updated: 2026-04-13
---

# AI 领域知识点总纲：点、线、面与层

> 如果 AI 知识只是一堆名词，很快就会碎。
> 更稳的组织方式是：先看 `点`，再看 `线`，再看 `面`，最后看 `层`。
> 这页的目的不是替代各个专题页，而是给整个 AI 领域一套可复用的认知骨架。

## 一、什么是点、线、面、层

### 1. 点：最小可学习单元

`点` 是一个具体知识点，可以是：

- 一个概念：[[Foundation Models]]、[[Reasoning Models]]、[[RAG]]、[[AI Security]]
- 一个机制：[[Pretraining]]、[[Transformer]]、[[Tool Use]]、[[上下文工程]]
- 一个系统：[[../09-Systems/OpenAI API|OpenAI API]]、[[../09-Systems/LangGraph|LangGraph]]、[[../09-Systems/OpenClaw|OpenClaw]]
- 一个指标：[[Evaluation]]、[[MLOps 与 LLMOps]]
- 一个失败模式：[[Prompt Injection 与 Jailbreaks]]、[[记忆污染、Memory Poisoning 与自改进风险]]
- 一个业务对象：[[AI Assistant]]、[[Coding Agents]]、[[OCR 与 Document AI]]

### 2. 线：一条能解释演化和决策的主线

`线` 不是知识点列表，而是一组能连续回答“为什么会这样、下一步怎么走”的主题链。

### 3. 面：一个能独立成立的领域面

`面` 是一组线的组合，比如：

- `模型能力面`
- `系统工程面`
- `安全治理面`
- `业务落地面`

### 4. 层：AI vault 里的结构层

在当前 vault 里，最重要的四层是：

- [[../../AI-Foundations/专题总览|AI-Foundations]]
- [[../专题总览|AI-Learning]]
- [[../../AI-Engineering/专题总览|AI-Engineering]]
- [[../../AI-Applications/专题总览|AI-Applications]]

> 这四层不是重复，而是同一个 AI 世界的四种观察高度。

## 二、AI 领域最重要的“点”有哪些

### A. 基础底座点

- [[Pretraining]]
- [[Transformer]]
- [[Foundation Models]]
- [[Multimodal Models]]
- [[Reasoning Models]]
- [[Long Context]]
- [[Alignment]]
- [[Synthetic Data]]

这些点回答的是：`模型为什么会有这些能力，能力边界从哪里来。`

### B. 系统能力点

- [[提示词工程]]
- [[上下文工程]]
- [[Tool Use]]
- [[RAG]]
- [[Agent]]
- [[Planning and Control]]
- [[Multi-Agent Systems]]
- [[Agent Memory]]
- [[MCP（Model Context Protocol）]]

这些点回答的是：`模型如何从“会回答”走到“会完成任务”。`

### C. 工程实现点

- [[AI 基础设施与 GPU Cloud]]
- [[Inference Serving]]
- [[Inference Efficiency]]
- [[MLOps 与 LLMOps]]
- [[Evaluation]]
- [[AI Security]]

这些点回答的是：`系统如何被训练、部署、评测、优化、治理。`

### D. 产品化与落地点

- [[AI Assistant]]
- [[Coding Agents]]
- [[AI Coding Workbench]]
- [[OCR 与 Document AI]]
- [[Voice、Realtime 与语音工作流]]
- [[AI Industry]]
- [[China AI Ecosystem]]
- [[Sovereign AI]]
- [[API Economy]]
- [[Developer Tools]]

这些点回答的是：`AI 最后是怎样进入产品、组织和产业的。`

## 三、AI 领域最重要的“线”有哪些

## 线 1：模型形成线

`历史/范式 -> Pretraining -> Transformer -> Foundation Models -> Post-training / Alignment -> Reasoning / Multimodal`

关键入口：

- [[模型形成线：Pretraining、Transformer、Foundation Models、Reasoning 与 Multimodal]]
- [[../../AI-Foundations/专题总览|AI-Foundations]]
- [[Pretraining]]
- [[Transformer]]
- [[Foundation Models]]
- [[Reasoning Models]]
- [[Multimodal Models]]

这条线回答的是：`为什么现代 AI 的底座能力会集中到少数 foundation models 上。`

## 线 2：能力升级线

`Prompt -> Context -> Retrieval -> Tool Use -> Agent -> Memory -> Planning -> Multi-Agent`

关键入口：

- [[能力升级线：Prompt、Context、RAG、Tool Use、Agent、Memory 与 Multi-Agent]]
- [[提示词工程]]
- [[上下文工程]]
- [[RAG]]
- [[Tool Use]]
- [[Agent]]
- [[Agent Memory]]
- [[Planning and Control]]
- [[Multi-Agent Systems]]

这条线回答的是：`模型怎样从静态回答升级成可执行系统。`

## 线 3：运行时工程线

`Inference Efficiency -> KV Cache / Serving -> Routing -> Observability -> Release Gate -> Rollback`

关键入口：

- [[运行时工程线：Inference、Serving、Evaluation、Release Gate 与 Security]]
- [[Inference Efficiency]]
- [[Inference Serving]]
- [[MLOps 与 LLMOps]]
- [[Evaluation]]
- [[../../AI-Engineering/07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]]
- [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]

这条线回答的是：`一个模型/agent 为什么能在线上稳定跑，而不只是 demo。`

## 线 4：安全与治理线

`AI Safety -> AI Security -> Prompt Injection -> Tool Safety -> Approval / Audit -> Release Gate`

关键入口：

- [[安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate]]
- [[AI Safety]]
- [[AI Safety 与 AI Security]]
- [[AI Security]]
- [[Prompt Injection 与 Jailbreaks]]
- [[../../AI-Engineering/07-Topics/Prompt Injection Defense 与 Tool Safety|Prompt Injection Defense 与 Tool Safety]]
- [[../../AI-Engineering/07-Topics/Agent 上线门槛与安全 Release Gates|Agent 上线门槛与安全 Release Gates]]

这条线回答的是：`为什么 AI 的风险不能只靠模型层修，而必须进入系统与组织。`

## 线 5：产品落地线

`Model/API -> Product Surface -> Workflow -> Case Study -> Rollout -> ROI / Governance`

关键入口：

- [[产品落地线：Model、Workflow、Case Study、Rollout、ROI 与 Governance]]
- [[AI Assistant]]
- [[Coding Agents]]
- [[OCR 与 Document AI]]
- [[Voice、Realtime 与语音工作流]]
- [[../../AI-Applications/03-Workflows/工作流索引|工作流索引]]
- [[../../AI-Applications/04-Case-Studies/案例索引|案例索引]]
- [[../../AI-Applications/05-Topics/Agent Rollout and Change Program|Agent Rollout and Change Program]]

这条线回答的是：`AI 怎样从一个 capability 变成一个真实组织能力。`

## 四、AI 领域最重要的“面”有哪些

## 面 1：能力面

这是“模型会什么”的面，核心是：

- [[Foundation Models]]
- [[Reasoning Models]]
- [[Multimodal Models]]
- [[Long Context]]
- [[Voice、Realtime 与语音工作流]]
- [[OCR 与 Document AI]]

## 面 2：系统面

这是“系统怎么完成任务”的面，核心是：

- [[RAG]]
- [[Tool Use]]
- [[Agent]]
- [[Planning and Control]]
- [[Multi-Agent Systems]]
- [[Agent Memory]]

## 面 3：工程面

这是“怎么把它做稳”的面，核心是：

- [[Inference Serving]]
- [[Inference Efficiency]]
- [[MLOps 与 LLMOps]]
- [[Evaluation]]
- [[AI Security]]

## 面 4：业务与组织面

这是“怎么进入组织和市场”的面，核心是：

- [[AI Assistant]]
- [[Coding Agents]]
- [[API Economy]]
- [[Developer Tools]]
- [[AI Industry]]
- [[China AI Ecosystem]]
- [[Sovereign AI]]

## 五、AI 领域最重要的“层”如何分工

## 1. Foundations 层

回答：`为什么现代 AI 会变成今天这样`

- 历史
- 范式
- 数学直觉
- 经典论文

入口：[[../../AI-Foundations/专题总览|AI-Foundations]]

## 2. Learning 层

回答：`现在 AI 世界里有哪些关键对象、主题和主线`

- 公司
- 人物
- 模型
- 系统
- 论文
- 主题
- 地图

入口：[[../专题总览|AI-Learning]]

## 3. Engineering 层

回答：`系统是怎么真正被构建、治理、放大的`

- 训练
- 评测
- 推理
- 部署
- runtime
- security
- ops

入口：[[../../AI-Engineering/专题总览|AI-Engineering]]

## 4. Applications 层

回答：`AI 怎样进入业务、流程和组织`

- 行业
- workflow
- 产品
- case study
- rollout
- ROI

入口：[[../../AI-Applications/专题总览|AI-Applications]]

## 六、怎样把点线面层串成一个真正可学的系统

### 方式 1：从点往上线

适合已经知道某个概念，但不知道它在全局哪里的人。

例如：

- 从 [[RAG]] 往上连到 `能力升级线`
- 再连到 `系统面`
- 再连到 `Learning/Engineering/Applications` 三层

### 方式 2：从线往下拆点

适合已经知道自己要学哪条主线的人。

例如：

- 先选 `Prompt -> Context -> Retrieval -> Tool Use -> Agent`
- 再把每一环拆成单独主题与系统案例

### 方式 3：从面切入

适合你在思考一个复杂问题，但不知道该读哪些主题。

例如：

- 想搞懂 `AI 为什么经常上线不稳`，优先看 `系统面 + 工程面 + 安全面`
- 想搞懂 `为什么某家公司更强`，优先看 `能力面 + 业务与组织面`

### 方式 4：从层切入

适合你现在的目标不是学一个点，而是换一个观察高度。

- Foundations：适合补原理和历史
- Learning：适合建立对象感和全景
- Engineering：适合建立可实现判断
- Applications：适合建立业务和组织判断

## 七、最值得重投入的主干知识点

按当前 vault 的优先级，我会把主干压在这些线上：

1. [[模型形成线：Pretraining、Transformer、Foundation Models、Reasoning 与 Multimodal]]
2. [[能力升级线：Prompt、Context、RAG、Tool Use、Agent、Memory 与 Multi-Agent]]
3. [[运行时工程线：Inference、Serving、Evaluation、Release Gate 与 Security]]
4. [[安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate]]
5. [[产品落地线：Model、Workflow、Case Study、Rollout、ROI 与 Governance]]

边缘但应保持可见的支线包括：

- [[Sovereign AI]]
- [[China AI Ecosystem]]
- [[API Economy]]
- [[Developer Tools]]
- [[Synthetic Data]]

> 它们不能看不见，但也不必抢走主干投入。

## 八、如果要继续细化，下一步该怎么补

- 新增一层 [[AI 五条主干专家工作台]]，把五条主干压成 `关键问题 / 核心指标 / 易混边界 / 面试表达要点`
- 给每个“面”补一页“关键问题与指标”
- 给每个“层”补一页“这一层最容易混淆的边界”
- 给五条主干各补一页“面试表达要点”
- 把重点主题从 `draft` 往 `usable study material` 推

## 关联

- [[AI 五条主干专家工作台]]
- [[AI 五条主干关键问题]]
- [[AI 五条主干核心指标]]
- [[AI 五条主干易混边界]]
- [[AI 五条主干面试表达要点]]
- [[AI 主题索引]]
- [[模型形成线：Pretraining、Transformer、Foundation Models、Reasoning 与 Multimodal]]
- [[能力升级线：Prompt、Context、RAG、Tool Use、Agent、Memory 与 Multi-Agent]]
- [[运行时工程线：Inference、Serving、Evaluation、Release Gate 与 Security]]
- [[安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate]]
- [[产品落地线：Model、Workflow、Case Study、Rollout、ROI 与 Governance]]
- [[../07-Maps/AI 知识点点线面图|AI 知识点点线面图]]
- [[../07-Maps/AI Ecosystem Map|AI Ecosystem Map]]
- [[../07-Maps/AI 五大专题审察与组织|AI 五大专题审察与组织]]
- [[../../AI-Foundations/专题总览|AI-Foundations]]
- [[../专题总览|AI-Learning]]
- [[../../AI-Engineering/专题总览|AI-Engineering]]
- [[../../AI-Applications/专题总览|AI-Applications]]
