---
title: 2026-04-29 至 2026-05-15 AI 拓扑补线：Governed Agents、Device Intelligence 与 Evaluation Institutionalization
type: recent-supplement
status: active
domain: AI
created: 2026-05-15
updated: 2026-05-15
---

# 2026-04-29 至 2026-05-15 AI 拓扑补线：Governed Agents、Device Intelligence 与 Evaluation Institutionalization

> 上次主线补线停在 [[2026-04-07 至 2026-04-29 AI 拓扑补线：Frontier Work Models、Sandbox Agents 与 Enterprise Model Lifecycle]]。
> 本页只补 `2026-04-29` 之后到 `2026-05-15` 这段时间里，对 AI 知识拓扑有影响的变化。

## 一句话结论

这半个月的 AI 变化，不应该按“又出了几个模型”来记，而应该按五条更稳定的结构变化来记：

1. `governed agents`：agent 开始从单点工具进入 `inventory / identity / permission / telemetry / lifecycle / policy` 的企业治理平面。
2. `mobile steering for long-running agents`：长任务 agent 不再只在桌面运行，用户需要随时 review、approve、redirect 和接管。
3. `vertical workflow packaging`：agent 不只是通用聊天框，而是被打包进小企业、金融、办公、采购、销售等具体业务流程。
4. `device intelligence`：AI 从应用层继续下沉到 Android、汽车、车载系统和上下文感知设备层。
5. `institutionalized evaluation`：frontier model 的评测不再只是公司自测，开始进入政府、标准机构和安全研究机构的协作评测体系。

## 这次新增的拓扑信号

### 1. Codex Mobile 与长任务 agent 的“随时接管面”

OpenAI 在 `2026-05-14` 宣布 Codex 进入 ChatGPT 移动端预览，重点不是“手机也能写代码”，而是说明长任务 agent 需要一个随时可接管的操作面：

- agent 在远程机器、devbox 或受管环境里运行。
- 用户在手机上查看 diff、终端输出、测试结果、截图和 approval。
- 文件、凭据、权限和本地环境仍留在执行机器上。
- 手机端承担的是 `review / approval / redirect / context injection`，不是把所有执行搬到手机。

应该沉淀到：

- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel|Harness 工作流模式：Terminal、Desktop、Cloud 与 Channel]]
- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
- [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]

### 2. Running Codex Safely 与 agent 安全控制平面

OpenAI 在 `2026-05-08` 公开了内部运行 Codex 的安全控制方式。它把 agent 安全从抽象原则落到了几类可配置边界：

- `sandbox`：写入范围、网络边界、保护路径。
- `approval policy`：哪些动作低风险可自动通过，哪些动作必须人工确认。
- `network policy`：允许常见可信域，阻断不可信域，对陌生域触发审批。
- `identity / credential`：CLI 和 MCP OAuth 凭据进入系统 keyring，登录绑定到企业 workspace。
- `rules`：按命令模式设置 allow / block / require approval。
- `agent-native telemetry`：记录 prompt、工具审批、工具执行、MCP 使用、网络 allow/deny 等事件，并接入 SIEM / compliance logging。

这说明 agent 安全已经从“prompt injection 防护”进入 `runtime control + policy-as-code + audit trail` 阶段。

应该沉淀到：

- [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]
- [[../../AI-Engineering/07-Topics/AI Security Telemetry、Escalation 与 Incident Response|AI Security Telemetry、Escalation 与 Incident Response]]
- [[../../AI-Engineering/07-Topics/Guardrails、Policy Enforcement 与 Security Gateways|Guardrails、Policy Enforcement 与 Security Gateways]]
- [[../../AI-Engineering/07-Topics/Enterprise AI Security Operating Model|Enterprise AI Security Operating Model]]

### 3. Microsoft Agent 365 与企业 agent 控制平面

Microsoft 在 `2026-05-01` 附近把 Agent 365 推到 GA，并在 `2026-05-05` 的 Frontier Firms 叙事里继续强调 agent 的组织级部署与治理。

它的拓扑意义不是“Microsoft 又多一个 Copilot 产品”，而是：

- agent 正在变成企业 IT 资产，需要 inventory。
- agent 需要身份、权限、生命周期、数据保护、威胁防护和行为审计。
- agent 可能来自 Microsoft 365、Copilot Studio、Azure AI Foundry、第三方平台或本地工具。
- 企业真正缺的不是“能不能建 agent”，而是“能不能知道哪些 agent 在运行、谁能用、访问什么、做了什么、成本多少、风险多大”。

应该沉淀到：

- [[../../AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]
- [[../../AI-Engineering/07-Topics/Enterprise AI Security Operating Model|Enterprise AI Security Operating Model]]
- [[../../AI-Applications/05-Topics/Agent Operating Model and Governance|Agent Operating Model and Governance]]
- [[../../AI-Applications/05-Topics/Agent Portfolio and Use Case Prioritization|Agent Portfolio and Use Case Prioritization]]

### 4. Claude for Small Business 与 vertical workflow packaging

Anthropic 在 `2026-05-13` 推出 Claude for Small Business，信号不在“小企业版本”本身，而在 agent 落地方式：

- 不是先卖模型能力，而是把 Claude 放进 QuickBooks、PayPal、HubSpot、Canva、Docusign、Google Workspace、Microsoft 365 等现有工具。
- 不是让用户自己 prompt，而是给出 payroll、month-end close、invoice chasing、campaign、contract review 等 ready-to-run workflows。
- 不是默认自动执行，而是保留 approval：发送、发布、付款等动作前需要用户确认。
- 不是只给工具，还补 AI fluency training，说明 adoption 和 enablement 已经成为产品的一部分。

这说明 enterprise / SMB agent 产品正在从 `general assistant` 进入 `workflow bundle + connector + skill + approval` 组合。

应该沉淀到：

- [[../../AI-Applications/05-Topics/Enterprise Agent Workflows|Enterprise Agent Workflows]]
- [[../../AI-Applications/05-Topics/Agent Productization|Agent Productization]]
- [[../../AI-Applications/05-Topics/Agent Adoption and Change Management|Agent Adoption and Change Management]]
- [[../../AI-Applications/03-Workflows/Finance Operations Agent Workflow|Finance Operations Agent Workflow]]
- [[../../AI-Applications/03-Workflows/Revenue Operations Agent Workflow|Revenue Operations Agent Workflow]]

### 5. Gemini Intelligence 上车与 device / ambient AI

Google 在 `2026-04-30` 到 `2026-05-12` 这一轮 Android / car updates 里，把 Gemini 推进车载和 Android Auto 场景。

这条线的关键不是“车里有聊天机器人”，而是 device intelligence 正在变成：

- 利用设备上下文理解当前任务。
- 结合短信、邮件、日历、地图、车载硬件、车主手册和车辆状态。
- 在驾驶、停车、充电、导航、消息、订单等场景里给出 proactive assistance。
- 通过车辆 OTA 和手机系统更新进入真实物理环境。

它让 AI 安全和产品设计的边界变硬：

- 车载场景有更高安全风险，不能照搬聊天产品的交互假设。
- device agent 需要处理实时上下文、权限、隐私、误触发、分心、安全降级。
- “AI 应用”会越来越多地变成“OS / device / vehicle capability”。

应该沉淀到：

- [[../06-Topics/Multimodal Models|Multimodal Models]]
- [[../06-Topics/Browser Agents 与 Computer Use|Browser Agents 与 Computer Use]]
- [[../../AI-Applications/05-Topics/Personal Assistant Agents|Personal Assistant Agents]]
- [[../../AI-Engineering/07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]]

### 6. CAISI / AISI 与 frontier model 预发布评测制度化

`2026-05-05` 前后，NIST / CAISI 与 Google DeepMind、Microsoft、xAI 签署 frontier AI national security testing 相关协议，Microsoft 也宣布与美国 CAISI、英国 AISI 合作做 frontier model 测试与评估。

这条线的拓扑意义是：

- frontier model 的评测从公司内部 benchmark 走向 `pre-deployment evaluation + government collaboration + national security risk assessment`。
- 风险类别从泛泛的“安全”具体到 cybersecurity、biosecurity、chemical weapons、large-scale public safety、misuse pathways。
- evaluation science 本身开始变成一条长期主线：benchmark、dataset、workflow、red team、post-deployment monitoring、safeguard assessment。

应该沉淀到：

- [[../06-Topics/模型行为治理：Model Spec、Preparedness、Transparency 与 AI Act|模型行为治理：Model Spec、Preparedness、Transparency 与 AI Act]]
- [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]
- [[../../AI-Engineering/07-Topics/AI Security Evaluation 与 Red Teaming|AI Security Evaluation 与 Red Teaming]]
- [[../../AI-Engineering/07-Topics/Incident-Fed Evals、Shadow Rollout 与 Promotion Regression|Incident-Fed Evals、Shadow Rollout 与 Promotion Regression]]

### 7. Claude + SpaceX compute 与容量变成产品能力

Anthropic 在 `2026-05-06` 宣布与 SpaceX 的 compute partnership，并同步提升 Claude Code 与 API 使用限制。

这条线的拓扑意义是：

- compute 不只是训练模型的后台资源，也直接影响 agent 产品能否支持长任务、高频 API、更多用户和更少限流。
- coding agent、research agent、workflow agent 的使用体验高度依赖可用容量、限流策略、延迟和价格。
- “模型选型”必须加入 capacity / rate limit / compute reliability 维度，而不只是 benchmark。

应该沉淀到：

- [[../../AI-Engineering/07-Topics/Cost, Latency, and Safety Tradeoffs|Cost, Latency, and Safety Tradeoffs]]
- [[../../AI-Engineering/07-Topics/Cost Optimization|Cost Optimization]]
- [[../06-Topics/AI 基础设施与 GPU Cloud|AI 基础设施与 GPU Cloud]]
- [[../06-Topics/Coding Agents|Coding Agents]]

## 对五条主干的影响

### 1. 模型形成线

这次不是模型结构突破，而是 model capability 的外部条件变得更重要：

- 容量、限流、延迟、成本正在影响实际可用性。
- 预发布评测和政府协作正在影响 frontier model release path。
- system card / eval report / deployment boundary 会比单纯模型名更重要。

应该补到：

- [[../06-Topics/模型形成线：Pretraining、Transformer、Foundation Models、Reasoning 与 Multimodal|模型形成线]]
- [[../06-Topics/Reasoning Models|Reasoning Models]]
- [[../06-Topics/Foundation Models|Foundation Models]]

### 2. 能力升级线

能力升级正在从“模型会不会”变成“系统能不能稳妥完成”：

- mobile steering 让长任务 agent 多了一个协作面。
- device intelligence 让模型能力进入物理世界上下文。
- vertical workflow packaging 让能力以 workflow 和 connector 方式交付。

应该补到：

- [[../06-Topics/能力升级线：Prompt、Context、RAG、Tool Use、Agent、Memory 与 Multi-Agent|能力升级线]]
- [[../06-Topics/Agent|Agent]]
- [[../06-Topics/Tool Use|Tool Use]]
- [[../06-Topics/Agent Memory|Agent Memory]]

### 3. 运行时工程线

运行时工程线现在必须显式加入 `control plane`：

- agent inventory。
- identity / permission。
- sandbox / network / filesystem boundary。
- approval / policy-as-code。
- telemetry / audit / SIEM。
- cost / rate limits / capacity planning。

应该补到：

- [[../06-Topics/运行时工程线：Inference、Serving、Evaluation、Release Gate 与 Security|运行时工程线]]
- [[../../AI-Engineering/07-Topics/Agent Runtime Architecture|Agent Runtime Architecture]]
- [[../../AI-Engineering/07-Topics/Harness Engineering|Harness Engineering]]
- [[../../AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]

### 4. 安全治理线

安全治理的重心继续从内容安全扩展到执行安全、组织安全和评测制度：

- agent 访问哪些系统。
- agent 继承谁的权限。
- agent 何时需要审批。
- agent 行为如何审计。
- frontier model 上线前如何做独立评测。
- device / vehicle agent 失败时如何降级。

应该补到：

- [[../06-Topics/安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate|安全治理线]]
- [[../06-Topics/AI Security|AI Security]]
- [[../../AI-Engineering/07-Topics/AI Security Threat Modeling|AI Security Threat Modeling]]
- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]

### 5. 产品落地线

产品落地线越来越清楚：

- 横向平台：Codex、Copilot、Claude、Gemini。
- 垂直工作流：finance、SMB、procurement、sales、service、legal、healthcare。
- 控制平面：Agent 365、enterprise workspace controls、MCP connector boundaries。
- 设备入口：mobile、desktop、car、OS。
- 评测与信任：pre-deployment testing、agent telemetry、approval gates。

应该补到：

- [[../06-Topics/产品落地线：Model、Workflow、Case Study、Rollout、ROI 与 Governance|产品落地线]]
- [[../../AI-Applications/05-Topics/Agent Rollout and Change Program|Agent Rollout and Change Program]]
- [[../../AI-Applications/05-Topics/Agent ROI and Value Capture|Agent ROI and Value Capture]]

## 当前优先级判断

如果接下来继续深学 AI，我会把重投入顺序调整成：

1. [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]：因为执行型 agent 的边界已经变成生产系统问题。
2. [[../../AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]：因为 agent control plane 正在成为企业 AI 的核心控制点。
3. [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]：因为 frontier model 和 agent system 都需要可复现评测。
4. [[../../AI-Applications/05-Topics/Enterprise Agent Workflows|Enterprise Agent Workflows]]：因为 AI 落地正在从“会话”走向“业务 workflow bundle”。
5. [[../../AI-Engineering/07-Topics/Computer Use Runtime and Safety|Computer Use Runtime and Safety]]：因为 device / vehicle intelligence 让 agent 进入更高风险的物理上下文。
6. [[../../AI-Engineering/07-Topics/Cost, Latency, and Safety Tradeoffs|Cost, Latency, and Safety Tradeoffs]]：因为 compute capacity 正在直接影响产品可用性和商业模型。

## 不是每周都该补什么

这类 recent supplement 不应该每周硬写一篇。建议节奏是：

- 每周只记录 `signal`：新产品、新论文、新监管、新事故、新 benchmark。
- 每半月到每月写一次 `topology supplement`：只有当信号足以改变知识图谱时才补。
- 每季度做一次 `priority refresh`：重新排序最值得深学的主干。
- 每次补线后，都要决定哪些内容应该沉到稳定的 `Topics / Systems / Models / Applications / Engineering`。

## 官方资料入口

- [OpenAI: Work with Codex from anywhere](https://openai.com/index/work-with-codex-from-anywhere/)
- [OpenAI: Running Codex safely at OpenAI](https://openai.com/index/running-codex-safely/)
- [Anthropic: Introducing Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business)
- [Anthropic: Higher usage limits for Claude and a compute deal with SpaceX](https://www.anthropic.com/news/higher-limits-spacex?fp=1)
- [Google: Android in cars updates](https://blog.google/products-and-platforms/platforms/android/android-in-cars-updates/)
- [Google: Gemini is coming to cars with Google built-in](https://blog.google/products-and-platforms/platforms/android/cars-with-google-built-in-gemini-tips-2026/)
- [NIST: Center for AI Standards and Innovation](https://www.nist.gov/caisi)
- [Microsoft: Agent 365](https://www.microsoft.com/microsoft-agent-365)
- [Microsoft: Frontier Firms operating model](https://blogs.microsoft.com/blog/2026/05/05/how-frontier-firms-are-rebuilding-the-operating-model-for-the-age-of-ai/)
- [Microsoft: Advancing AI evaluation with CAISI and AISI](https://blogs.microsoft.com/on-the-issues/2026/05/05/advancing-ai-evaluation-with-the-center-for-ai-standards-us-and-innovation-and-the-ai-security-institute-uk/)

## 下一步沉淀

- 做一张 `Agent Control Plane` 决策地图：OpenAI Codex controls、Microsoft Agent 365、Anthropic MCP connectors、enterprise SIEM / compliance logging 怎么分层。
- 把 `sandbox / shell / approval / telemetry` 做成可执行的 agent security playbook。
- 给 `SMB / finance / procurement / support / coding / research` 建一组 vertical workflow case packets。
- 补一页 `Device / Vehicle AI Safety`：手机、车机、浏览器、桌面、可穿戴设备的 agent 边界。
- 补一条 `Evaluation Institutionalization` 阅读路径：CAISI / AISI / system card / red team / incident-fed eval / post-deployment monitoring。
