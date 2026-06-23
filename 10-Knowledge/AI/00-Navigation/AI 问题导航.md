---
title: AI 问题导航
type: dashboard
status: active
updated: 2026-05-15
canvas:
  - "[[知识导航门户.canvas]]"
知识导航门户: []
---

# AI 问题导航

> 这页给“按问题回顾 AI”用，不给“按目录巡检”用。

如果你脑子里出现的是：

- 我想搭一个能工作的 Agent
- 我想把 LLMOps / AgentOps 理顺
- 我想做 AI Security
- 我想选一组值得长期跟的开源栈
- 我想把 Mac 变成 AI 实验室
- 我想理解 AI 记忆与自改进
- 我想通过人物、组织与案例建立判断
- 我想通过作者、论文与时间线理解 AI
- 我想知道最近半年哪些 AI 知识最值得重投入
- 我想接上 2026-04-29 之后的新 AI 拓扑
- 我想接上 2026-04-07 之后的新 AI 拓扑
- 我想快速刷新 2026 新模型格局
- 我想理解 Foundations 争论今天怎么活在 LLM / agent 里

那就先来这页，而不是先猜自己该进哪个 area。

## 总入口

- [[AI 总控制塔|AI 总控制塔]]
- [[AI 决策导航|AI 决策导航]]
- [[../当前工作台|当前工作台]]
- [[AI-Learning/07-Maps/AI 五大专题审察与组织|AI 五大专题审察与组织]]
- [[AI-Learning/07-Maps/AI Ecosystem Map|AI Ecosystem Map]]
- [[AI-Learning/11-Recent-Supplements/补线索引|补线索引]]

## 高杠杆问题页

- [[我想搭 Agent]]
  - 看对象、动作面、runtime、productization 和 rollout
- [[我想做 LLMOps 与 AgentOps]]
  - 看 traces、evals、release、registry、observability 和 vendor tradeoff
- [[我想做 AI Security]]
  - 看 attack surface、tool safety、guardrails、release gate 和 operating model
- [[我想选 AI 开源栈]]
  - 看核心样本、模式、源码切入点和 adoptability
- [[我想把 Mac 变成 AI 实验室]]
  - 看 Apple Silicon、本地推理、MLX、Ollama 和可执行路径
- [[我想理解 AI 记忆与自改进]]
  - 看 memory design、consolidation、evaluation、promotion 和实验线
- [[我想通过人物、组织与案例理解 AI]]
  - 看人物线、组织能力、系统表面和真实 rollout 样本
  - 方法页：[[怎么读 AI 人物：路线、分歧与信号]]、[[怎么读 AI 组织：能力画像、生态位与 Adoptability]]、[[AI Rollout Operating Packet：试点、门禁、复盘与规模化]]、[[AI Failure Packet：任务边界、事实源、审批、回滚与责任]]
- [[我想通过作者、论文与时间线理解 AI]]
  - 看时间线、经典论文、作者主线和术语映射
  - 方法页：[[怎么读 AI 论文：问题、转折点与长期影响]]、[[AI 历史主时间线：从符号主义到大模型]]、[[怎么用 AI 基础双语术语表：从术语到现代 AI]]
  - 近五年主线：[[近五年关键 AI 论文与路线映射（2021-2025）]]
  - 最近两年补线：[[AI-Learning/11-Recent-Supplements/2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use|2024-2026 AI 新路线补线：Long Context、Multimodal 与 Computer Use]]
  - 新补的语音线：[[AI-Learning/11-Recent-Supplements/2024-2026 AI 新路线补线：Voice、Realtime 与语音工作流|2024-2026 AI 新路线补线：Voice、Realtime 与语音工作流]]
  - 新补的文档线：[[AI-Learning/11-Recent-Supplements/2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流|2024-2026 AI 新路线补线：OCR、Document AI 与文档工作流]]
- [[AI-Learning/11-Recent-Supplements/最近半年最值得重投入学习的 AI 主线（截至 2026-04-07）|最近半年最值得重投入学习的 AI 主线（截至 2026-04-07）]]
  - 看最近半年最值得你花大精力和大时间的 6 条主线，以及为什么它们比零散热点更值得学
  - 继续进入：[[AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]、[[AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]、[[AI-Learning/06-Topics/Reasoning Models|Reasoning Models]]、[[AI-Learning/06-Topics/Coding Agents|Coding Agents]]
- [[AI-Learning/11-Recent-Supplements/2026-04-07 至 2026-04-29 AI 拓扑补线：Frontier Work Models、Sandbox Agents 与 Enterprise Model Lifecycle|2026-04-07 至 2026-04-29 AI 拓扑补线]]
  - 看上次同步之后，AI 拓扑如何从模型刷新继续推进到 `frontier work model`、`sandbox agent runtime` 和 `enterprise model lifecycle`
  - 继续进入：[[AI-Learning/03-Models/GPT-5-5|GPT-5.5]]、[[AI-Learning/03-Models/Claude Opus 4-7|Claude Opus 4.7]]、[[AI-Learning/03-Models/Mistral Large 3|Mistral Large 3]]、[[AI-Learning/09-Systems/OpenAI Sandbox Agents|OpenAI Sandbox Agents]]、[[AI-Learning/09-Systems/Mistral Forge|Mistral Forge]]
- [[AI-Learning/11-Recent-Supplements/2026-04-29 至 2026-05-15 AI 拓扑补线：Governed Agents、Device Intelligence 与 Evaluation Institutionalization|2026-04-29 至 2026-05-15 AI 拓扑补线]]
  - 看最新变化如何从模型名继续推进到 `governed agents`、`mobile steering`、`vertical workflow packaging`、`device intelligence` 和 `institutionalized evaluation`
  - 继续进入：[[AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]、[[AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]、[[AI-Applications/05-Topics/Enterprise Agent Workflows|Enterprise Agent Workflows]]、[[AI-Engineering/07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]]
- [[AI-Learning/11-Recent-Supplements/截至 2026-04-07 的 2026 新模型刷新|截至 2026-04-07 的 2026 新模型刷新]]
  - 看截至 `2026-04-07` 的 frontier model refresh、reasoning 分层、coding lane、voice lane 和 open model 新信号
  - 继续进入：[[AI-Learning/03-Models/模型索引|模型索引]]、[[AI-Learning/06-Topics/Reasoning Models|Reasoning Models]]、[[AI-Learning/06-Topics/Coding Agents|Coding Agents]]、[[AI-Learning/06-Topics/Open-Weight Models|Open-Weight Models]]
- [[AI-Learning/11-Recent-Supplements/2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime|2025-2026 AI 新路线补线：Deep Research、Memory 与 Agent Runtime]]
  - 看 `2025-2026` 里最容易漏掉的 `research agent / product memory / runtime memory / context management / MCP / A2A`
  - 继续进入：[[AI-Learning/06-Topics/Deep Research 与 Research Agents|Deep Research 与 Research Agents]]、[[AI-Learning/06-Topics/Agent Memory|Agent Memory]]、[[AI-Learning/06-Topics/MCP（Model Context Protocol）|MCP（Model Context Protocol）]]、[[AI-Learning/06-Topics/A2A（Agent-to-Agent）与协作协议|A2A（Agent-to-Agent）与协作协议]]
- [[AI-Learning/11-Recent-Supplements/2025-2026 AI 治理补线：Model Spec、Preparedness、Transparency 与 AI Act|2025-2026 AI 治理补线：Model Spec、Preparedness、Transparency 与 AI Act]]
  - 看最近一波 `model behavior governance`、preparedness reporting、transparency 和 GPAI obligations 怎么变成正式主线
  - 继续进入：[[AI-Learning/06-Topics/模型行为治理：Model Spec、Preparedness、Transparency 与 AI Act|模型行为治理：Model Spec、Preparedness、Transparency 与 AI Act]]、[[AI-Learning/06-Topics/AI Safety 与 AI Security|AI Safety 与 AI Security]]、[[AI-Learning/06-Topics/安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate|安全治理线]]
- [[哪些 AI Foundations 争论今天还活着]]
  - 看旧争论如何变成今天的 workflow、agent、RAG、eval 与 control 问题
  - 对照页：[[从 Symbolic AI 到 LLM Agent：旧问题的新形式]]

## 怎么用这组问题页

1. 先打开最接近你当前问题的那一页
2. 按它给的最短路径读，不要一次性开太多地图
3. 如果读到中途发现自己问错了问题，再回到这页切换路线
4. 如果你已经开始在几种方案里做选择，切去 [[AI 决策导航|AI 决策导航]]
5. 如果你已经明确知道自己要进哪个专题，再回到 [[AI 总控制塔|AI 总控制塔]]

## 这组入口想解决什么

- 不是把知识库再拆得更碎
- 而是把已有内容编排成“问题 -> 判断 -> 路径 -> 回答”的回顾方式

## 关联

- [[AI 总控制塔|AI 总控制塔]]
- [[AI-Learning/专题总览|AI-Learning]]
- [[AI-Engineering/专题总览|AI-Engineering]]
- [[AI-Open-Source/专题总览|AI-Open-Source]]
- [[AI-Applications/专题总览|AI-Applications]]
