---
title: 2026-04-07 至 2026-04-29 AI 拓扑补线：Frontier Work Models、Sandbox Agents 与 Enterprise Model Lifecycle
type: recent-supplement
status: active
domain: AI
created: 2026-04-29
updated: 2026-04-29
---

# 2026-04-07 至 2026-04-29 AI 拓扑补线：Frontier Work Models、Sandbox Agents 与 Enterprise Model Lifecycle

> 上次明确同步点是 [[截至 2026-04-07 的 2026 新模型刷新]] 和 [[最近半年最值得重投入学习的 AI 主线（截至 2026-04-07）]]。
> 本页只补 `2026-04-07` 之后到 `2026-04-29` 这段时间里，对知识拓扑有影响的变化。

## 一句话结论

这半个月的 AI 变化，不应该按“又出了几个模型”来记，而应该按三条拓扑变化来记：

1. `frontier work model`：模型发布越来越明确面向 `coding / computer use / knowledge work / science / long-horizon tasks`
2. `sandbox agent runtime`：agent 的关键竞争点从 tool calling 继续下沉到 `shell / sandbox / filesystem / approval / artifact` 的运行时边界
3. `enterprise model lifecycle`：开源权重和企业定制模型不只是“能下载”，而是进入 `pre-training -> post-training -> RL -> eval -> governance -> deployment` 的生命周期服务

## 这次新增的拓扑节点

### 1. [[../03-Models/GPT-5-5|GPT-5.5]]

`GPT-5.5` 更适合被记成 OpenAI 的 `frontier work model` 节点，而不是单纯的通用聊天模型。

它对拓扑的意义是：

- 把 `coding`、`computer use`、`knowledge work`、`science`、`long-horizon tasks` 放到同一条“高强度工作模型”主线上
- 继续强化 [[../06-Topics/Reasoning Models|Reasoning Models]] 与 [[../06-Topics/Coding Agents|Coding Agents]] 的交叉地带
- 让 [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]] 变得更重要，因为越强的 work model 越需要任务级回归测试，而不是只看聊天 benchmark

推荐沉淀位置：

- 模型层：[[../03-Models/GPT-5-5|GPT-5.5]]
- 系统层：[[../09-Systems/Codex|Codex]]、[[../09-Systems/OpenAI API|OpenAI API]]
- 工程层：[[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]

### 2. [[../03-Models/Claude Opus 4-7|Claude Opus 4.7]]

`Claude Opus 4.7` 继续巩固 Anthropic 的高强度工作模型路线。

它对拓扑的意义是：

- 把 Claude 的 `long-running coding`、`instruction following`、`vision` 和 `cyber safeguard` 继续推向一个更明确的 enterprise workhorse / flagship 对照
- 让 [[../09-Systems/Claude Code|Claude Code]] 不只是一个 coding tool，而是 Claude 模型路线在软件工程 runtime 里的产品化证明
- 继续强化 `model capability -> agent product -> security boundary` 这条判断线

推荐沉淀位置：

- 模型层：[[../03-Models/Claude Opus 4-7|Claude Opus 4.7]]
- 系统层：[[../09-Systems/Claude Code|Claude Code]]
- 工程层：[[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]

### 3. [[../09-Systems/OpenAI Sandbox Agents|OpenAI Sandbox Agents]]

OpenAI 的 Agents SDK sandbox / shell 工具线，说明 `agent runtime` 正在从“能调用工具”升级成“能安全运行工作负载”。

它对拓扑的意义是：

- `harness control plane` 和 `sandbox execution plane` 必须分开理解
- shell、filesystem、network、secret、artifact、approval 都是 agent 的真实边界，而不是实现细节
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]] 不再只是 coding agent 的产品体验问题，而是 agent 系统架构的核心层

推荐沉淀位置：

- 系统层：[[../09-Systems/OpenAI Sandbox Agents|OpenAI Sandbox Agents]]
- 主题层：[[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]]
- 工程层：[[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]

### 4. [[../03-Models/Mistral Large 3|Mistral Large 3]] 与 [[../09-Systems/Mistral Forge|Mistral Forge]]

Mistral 这条线这次最值得记录的不是单个模型名，而是企业模型生命周期路线。

它对拓扑的意义是：

- open-weight 模型正在和企业私有数据、定制训练、评测、治理、部署绑定
- `Mistral Forge` 代表的是 `model customization lifecycle`，不是普通 SaaS 产品
- 这条线应该和 [[../../AI-Engineering/07-Topics/Model Registry and Deployment|Model Registry and Deployment]]、[[../../AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]] 连起来

推荐沉淀位置：

- 模型层：[[../03-Models/Mistral Large 3|Mistral Large 3]]
- 系统层：[[../09-Systems/Mistral Forge|Mistral Forge]]
- 主题层：[[../06-Topics/Open-Weight Models|Open-Weight Models]]
- 工程层：[[../../AI-Engineering/07-Topics/Model Registry and Deployment|Model Registry and Deployment]]

## 对五条主干的影响

### 1. 模型形成线

这次变化加强了一个判断：

> frontier model 不再只按“参数、上下文、benchmark”分层，而越来越按“能否承担真实工作负载”分层。

应该补到：

- [[../06-Topics/模型形成线：Pretraining、Transformer、Foundation Models、Reasoning 与 Multimodal|模型形成线]]
- [[../06-Topics/Reasoning Models|Reasoning Models]]
- [[../06-Topics/Multimodal Models|Multimodal Models]]
- [[../06-Topics/Open-Weight Models|Open-Weight Models]]

### 2. 能力升级线

最重要的能力升级不是“会回答更多问题”，而是：

- 能写更复杂代码
- 能操作 shell / browser / files
- 能在长任务里保持目标、约束和上下文
- 能接受企业的私有知识和 domain tuning

应该补到：

- [[../06-Topics/能力升级线：Prompt、Context、RAG、Tool Use、Agent、Memory 与 Multi-Agent|能力升级线]]
- [[../06-Topics/Tool Use|Tool Use]]
- [[../06-Topics/Agent|Agent]]
- [[../06-Topics/Coding Agents|Coding Agents]]
- [[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]]

### 3. 运行时工程线

这次变化最强的工程信号在 runtime：

- model selection 之外，必须设计 sandbox、approval、artifact、filesystem、network、secret boundary
- agent 不只是 prompt + tools，而是一个可以失败、回滚、审计、复现的执行系统
- eval 需要覆盖端到端任务，而不是只覆盖单轮输出质量

应该补到：

- [[../06-Topics/运行时工程线：Inference、Serving、Evaluation、Release Gate 与 Security|运行时工程线]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]
- [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]

### 4. 安全治理线

越接近真实工作负载，安全治理越从内容安全转向执行安全：

- shell 能做什么
- sandbox 能不能联网
- credential 如何隔离
- approval gate 放在哪里
- 产物和日志能不能审计
- 模型升级能不能回归验证

应该补到：

- [[../06-Topics/安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate|安全治理线]]
- [[../06-Topics/AI Security|AI Security]]
- [[../../AI-Engineering/07-Topics/AI Security Threat Modeling|AI Security Threat Modeling]]
- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]

### 5. 产品落地线

产品落地判断也变了：

- 问题不只是“用哪个模型”
- 而是“选择哪种工作模型、哪种 runtime、哪种企业生命周期”

更具体地说：

- 如果是软件工程：重点看 `GPT-5.5 / Claude Opus 4.7 + Codex / Claude Code + sandbox / eval`
- 如果是企业知识系统：重点看 `Mistral Forge + proprietary data + eval + deployment governance`
- 如果是可操作 agent：重点看 `sandbox / shell / approvals / audit / rollback`

应该补到：

- [[../06-Topics/产品落地线：Model、Workflow、Case Study、Rollout、ROI 与 Governance|产品落地线]]
- [[../09-Systems/系统索引|系统索引]]
- [[../../AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]

## 当前优先级判断

如果我们接下来继续深学 AI，我会把重投入顺序调整成：

1. [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]：因为 sandbox / shell / app server / approval 已经成为 agent 系统的真实底座
2. [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]：因为执行型 agent 的风险不在“说错话”那么简单
3. [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]：因为 frontier work model 的价值必须用任务级回归来判断
4. [[../../AI-Engineering/07-Topics/Prompt Registry、Datasets 与 Evals|Prompt Registry、Datasets 与 Evals]]：因为企业定制模型生命周期需要可追踪数据和评测资产
5. [[../06-Topics/Coding Agents|Coding Agents]]：因为 coding 仍然是最容易验证 agent 能力边界的高价值场景

## 官方资料入口

- [OpenAI: Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
- [OpenAI Platform: GPT-5.5](https://platform.openai.com/docs/models/gpt-5.5)
- [OpenAI Platform: Agents sandboxes](https://developers.openai.com/api/docs/guides/agents/sandboxes)
- [OpenAI Platform: Shell tool](https://developers.openai.com/api/docs/guides/tools-shell)
- [Anthropic: Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7)
- [Mistral Docs: Models overview](https://docs.mistral.ai/models/overview)
- [Mistral: Forge](https://mistral.ai/news/forge)

## 下一步沉淀

- 把 `sandbox / shell / approval` 做成一条更具体的 agent security playbook
- 把 `frontier work model` 做成一个跨 OpenAI / Anthropic / Google / Mistral 的模型选型判断表
- 把 `enterprise model lifecycle` 做成 `数据 -> 训练 -> 评测 -> 部署 -> 审计` 的工程地图
