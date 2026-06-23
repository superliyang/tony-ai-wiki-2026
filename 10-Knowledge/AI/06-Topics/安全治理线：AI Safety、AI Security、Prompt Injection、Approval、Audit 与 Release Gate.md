---
title: 安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate
type: topic
status: active
tags:
  - ai/topic
  - ai/safety-line
created: 2026-04-13
updated: 2026-04-13
---

# 安全治理线：AI Safety、AI Security、Prompt Injection、Approval、Audit 与 Release Gate

> 这条线回答的是：
> `为什么 AI 系统的风险不能只当成模型问题，而必须变成系统设计、审批流程和组织治理的一部分。`

## 这条线为什么重要

很多团队在做 AI 时，会先追求：

- 效果更强
- 成本更低
- 交互更顺

但真正决定能不能放心上线的，经常是另一套问题：

- 会不会胡说且造成真实损害
- 会不会被 prompt injection 或越权调用击穿
- 哪些步骤必须经过 approval
- 失败后有没有 audit trail
- 出事时能不能快速定位、降级、回滚

所以这条线的核心不是“把模型调得更乖”，而是：

`把风险边界做成一套可执行的控制链路。`

## 一条最简主线

`AI Safety -> AI Security -> Prompt Injection / Tool Safety -> Approval Gates -> Audit / Telemetry -> Release Gate -> Incident Response`

## 一、AI Safety：为什么准确率之外还要看伤害边界

核心页：

- [[AI Safety]]
- [[AI Safety 与 AI Security]]
- [[../../AI-Applications/04-Case-Studies/Air Canada Chatbot Liability Case|Air Canada Chatbot Liability Case]]

AI Safety 解决的是：

- 模型或系统行为是否会造成误导、伤害、违规或责任问题
- 输出是否越过业务或伦理边界
- 人类是否会过度信任一个看起来流畅但并不可靠的系统

它更偏：

- 行为边界
- 伤害后果
- 使用责任

而不是攻击者视角本身。

## 二、AI Security：为什么攻击面会随着 agent 化快速扩大

核心页：

- [[AI Security]]
- [[../../AI-Engineering/07-Topics/Enterprise AI Security Operating Model|Enterprise AI Security Operating Model]]
- [[../07-Maps/AI Security Threat Map|AI Security Threat Map]]

当系统进入：

- RAG
- tool use
- browser action
- memory
- multi-agent

攻击面就会从纯输出问题扩展到：

- 输入污染
- 检索污染
- 工具越权
- 凭证暴露
- 审批绕过
- 日志与供应链风险

这也是为什么 AI security 不是传统应用安全的简单平移，而是更像：

`LLM behavior risk + workflow risk + permission risk + runtime risk`

## 三、Prompt Injection 与 Tool Safety：为什么风险开始进入动作层

核心页：

- [[Prompt Injection 与 Jailbreaks]]
- [[../../AI-Engineering/07-Topics/Prompt Injection Defense 与 Tool Safety|Prompt Injection Defense 与 Tool Safety]]
- [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]

Prompt injection 的关键危险不只是让模型“说错话”，而是让它：

- 读错指令优先级
- 被外部内容接管行为
- 在不该调用工具时调用工具
- 在不该暴露数据时暴露数据

一旦系统有 action surface，安全问题就会从“回答风险”升级成“执行风险”。

这时真正重要的是：

- instruction hierarchy
- tool allowlist / denylist
- sandbox
- capability scoping
- side-effect isolation

## 四、Approval：为什么不是所有动作都该自动执行

核心页：

- [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
- [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]
- [[../../AI-Engineering/07-Topics/Agent 上线门槛与安全 Release Gates|Agent 上线门槛与安全 Release Gates]]

Approval 的真正作用不是拖慢系统，而是把高风险决策从“默认自动执行”改成“按风险分级执行”。

典型需要 approval 的环节：

- 对外发信
- 改动生产系统
- 删除/转移数据
- 提交财务或合同动作
- 跨租户、跨权限边界访问

更专业的判断方式不是“要不要人审”，而是：

`哪些动作可自动、哪些动作需确认、哪些动作永远不该由 agent 直接完成。`

## 五、Audit 与 Telemetry：为什么出问题后必须能追责和复盘

相关页：

- [[../../AI-Engineering/07-Topics/AI Security Telemetry、Escalation 与 Incident Response|AI Security Telemetry、Escalation 与 Incident Response]]
- [[../../AI-Engineering/08-Maps/AI Security 控制点图|AI Security 控制点图]]

如果一个 AI 系统没有 audit，你最后通常只能知道：

- 结果出错了

但不知道：

- 哪一轮输入触发的
- 检索了什么
- 为什么调了这个工具
- 当时的审批状态是什么
- 哪个版本的 prompt / route / policy 在生效

所以成熟系统需要的不只是日志，而是：

- decision trace
- tool trace
- approval trace
- policy trace
- version trace

## 六、Release Gate：为什么安全必须接到上线机制

核心页：

- [[../../AI-Engineering/07-Topics/Agent 上线门槛与安全 Release Gates|Agent 上线门槛与安全 Release Gates]]
- [[../../AI-Engineering/07-Topics/AI Security Evaluation 与 Red Teaming|AI Security Evaluation 与 Red Teaming]]
- [[../../AI-Engineering/06-Projects/AI Security Governance/企业 AI 安全治理与上线机制|企业 AI 安全治理与上线机制]]

Release gate 是把：

- 技术质量
- 风险控制
- 业务责任

接成一条线的地方。

你可以把它理解成：

`不是系统“能不能跑”，而是系统“能不能被允许跑”。`

常见 gate 形态：

- shadow
- canary
- limited rollout
- domain allowlist
- high-risk task block
- mandatory approval

## 七、Incident Response：为什么治理不是写完 policy 就结束

相关页：

- [[../../AI-Engineering/07-Topics/AI 安全案例与失败模式|AI 安全案例与失败模式]]
- [[../../AI-Engineering/07-Topics/AI Security Telemetry、Escalation 与 Incident Response|AI Security Telemetry、Escalation 与 Incident Response]]

真正的治理闭环包括：

- 事前 threat modeling
- 事中 detection / escalation
- 事后 incident review
- 再把经验喂回 eval、policy 和 release gate

没有 incident loop，安全治理就很容易停在 PPT。

## 八、这条线最容易混淆的边界

### 1. Safety vs Security

- safety 更偏伤害与行为边界
- security 更偏攻击、越权、供应链和控制面

### 2. Guardrail vs Governance

- guardrail 是单个控制点
- governance 是跨系统、跨流程、跨角色的控制体系

### 3. Approval vs Release Gate

- approval 管单次高风险动作
- release gate 管能力是否被允许放量上线

### 4. Audit vs Logging

- logging 记录事件
- audit 记录可追责的决策链和责任链

## 九、建议学习顺序

1. [[AI Safety]]
2. [[AI Safety 与 AI Security]]
3. [[AI Security]]
4. [[Prompt Injection 与 Jailbreaks]]
5. [[../../AI-Engineering/07-Topics/Prompt Injection Defense 与 Tool Safety|Prompt Injection Defense 与 Tool Safety]]
6. [[../../AI-Engineering/07-Topics/Agent Security、Sandbox 与 Approval Architecture|Agent Security、Sandbox 与 Approval Architecture]]
7. [[../../AI-Engineering/07-Topics/Human-in-the-Loop and Approval Gates|Human-in-the-Loop and Approval Gates]]
8. [[../../AI-Engineering/07-Topics/AI Security Evaluation 与 Red Teaming|AI Security Evaluation 与 Red Teaming]]
9. [[../../AI-Engineering/07-Topics/Enterprise AI Security Operating Model|Enterprise AI Security Operating Model]]
10. [[../../AI-Engineering/07-Topics/Agent 上线门槛与安全 Release Gates|Agent 上线门槛与安全 Release Gates]]
11. [[../../AI-Engineering/07-Topics/AI Security Telemetry、Escalation 与 Incident Response|AI Security Telemetry、Escalation 与 Incident Response]]

## 十、这条线在面试里能回答什么

- 为什么 AI 风险不能只靠模型对齐解决
- 你如何区分 safety、security、approval、release gate 的职责
- 你会如何给有 tool use 的 agent 设计控制链路
- 为什么 audit 和 incident response 是 AI 治理的一部分，而不是事后补丁

## 关联

- [[AI 五条主干专家工作台]]
- [[AI 领域知识点总纲：点、线、面与层]]
- [[AI 主题索引]]
- [[../07-Maps/AI 知识点点线面图|AI 知识点点线面图]]
- [[AI Safety]]
- [[AI Security]]
- [[Prompt Injection 与 Jailbreaks]]
- [[../../AI-Engineering/08-Maps/AI Security Engineering Map|AI Security Engineering Map]]
- [[../../AI-Engineering/08-Maps/AI Security 控制点图|AI Security 控制点图]]
