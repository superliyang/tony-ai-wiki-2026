---
title: 运行时工程线：Inference、Serving、Evaluation、Release Gate 与 Security
type: topic
status: active
tags:
  - ai/topic
  - ai/runtime-line
created: 2026-04-12
updated: 2026-04-13
---

# 运行时工程线：Inference、Serving、Evaluation、Release Gate 与 Security

> 这条线回答的是：
> `为什么一个 AI demo 看起来很强，但真正上线后却会暴露稳定性、成本、风险和治理问题。`

## 这条线为什么重要

很多 AI 讨论停在模型能力层，但企业真正吃亏的地方经常在 runtime：

- 延迟不稳
- 成本失控
- 流量高峰时退化
- 工具调用出错
- 回归问题难以及时发现
- 安全控制点不完整

所以这条线的核心不是“模型好不好”，而是：

`系统能不能长期、稳定、可控地跑。`

## 一条最简主线

`Inference Efficiency -> Serving -> Routing / Capacity -> Evaluation -> Release Gate -> Security / Audit -> Rollback / Incident Response`

## 一、Inference Efficiency：算得起，才跑得久

核心页：

- [[Inference Efficiency]]
- [[AI 基础设施与 GPU Cloud]]
- [[../../AI-Engineering/07-Topics/KV Cache、Prefill-Decode 与 Continuous Batching|KV Cache、Prefill-Decode 与 Continuous Batching]]

这一段解决的是：

- 每次请求到底要花多少算力
- latency 和 throughput 怎样平衡
- token 价格、显存占用、并发能力怎样互相影响

如果没有这层，产品很容易出现：

- 单次效果看起来不错
- 但一上量就成本爆炸或延迟无法接受

这也是为什么 senior 视角里，模型选择从来不是只看 benchmark。

## 二、Serving：为什么“能调用”不等于“能服务”

核心页：

- [[Inference Serving]]
- [[MLOps 与 LLMOps]]
- [[../07-Maps/AI Infra 与推理服务生态图|AI Infra 与推理服务生态图]]

Serving 关心的是：

- 请求如何接入
- 模型如何部署
- 流量如何分发
- 多模型、多区域、不同租户如何管理
- 故障如何隔离

从这一步开始，AI 系统更像在线服务，而不是实验 notebook。

常见设计议题：

- self-hosted vs managed API
- 专用模型 vs 通用模型 route
- warm pool / autoscaling / queueing
- streaming 与 realtime 的服务差异

## 三、Routing 与 Capacity：为什么正确请求要发给正确模型

相关页：

- [[Reasoning Models]]
- [[Coding Agents]]
- [[Voice、Realtime 与语音工作流]]

一旦产品进入多场景、多 SLA、多成本层级，系统就需要路由判断：

- 哪些请求上高能力模型
- 哪些请求走便宜模型
- 哪些请求先走 fast path，再升级
- 哪些任务应拆分到专门 tool 或 workflow

这一步把“模型评测”变成了“系统级调度问题”。

## 四、Evaluation：为什么没有 eval，系统迭代会越来越盲

核心页：

- [[Evaluation]]
- [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]

Eval 的价值不是做一张 leaderboard，而是给系统一个稳定判断面：

- 改了 prompt / context 后有没有退化
- 换模型后哪些任务更好、哪些更差
- 新 tool、新 memory、新 route 是否引入风险
- 哪些 release 可以放量，哪些要拦住

没有 eval，很多团队只能靠：

- 主观体验
- 零散用户反馈
- 上线后事故倒逼

这会让系统看似在迭代，实际在失控。

## 五、Release Gate：为什么 AI 上线不能像普通功能开关一样粗放

相关页：

- [[../../AI-Engineering/07-Topics/Agent 上线门槛与安全 Release Gates|Agent 上线门槛与安全 Release Gates]]
- [[AI Safety]]
- [[AI Security]]

Release gate 解决的是：

- 什么能力允许直接上线
- 什么能力必须先 shadow / canary / 人审
- 什么风险一旦出现必须回滚
- 线上异常由谁接管

它是把：

- 技术评测
- 风险判断
- 组织责任

接到一起的控制面。

## 六、Security：为什么安全控制点必须进入 runtime

核心页：

- [[AI Security]]
- [[AI Safety 与 AI Security]]
- [[Prompt Injection 与 Jailbreaks]]

AI 系统的安全不是一个“模型侧附属题”，而是 runtime 设计的一部分。

尤其在有 tool use、RAG、memory、browser action 的系统里，风险会进入：

- 输入层
- 检索层
- 工具层
- 输出层
- 审批层
- 日志与审计层

所以你需要的不只是 guardrail，而是控制链路。

## 七、Rollback 与 Incident Response：为什么出问题后还能站得住

相关页：

- [[../../AI-Engineering/07-Topics/AI 安全案例与失败模式|AI 安全案例与失败模式]]
- [[../../AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]

真正成熟的 runtime 不只是“尽量不出事”，还包括：

- 出问题时能快速识别
- 能定位是模型、route、tool 还是数据问题
- 能回滚到上一安全版本
- 能把事故重新喂回 eval 和 release 流程

这也是为什么 observability、incident library、regression suite 会越来越重要。

## 八、这条线最容易混淆的边界

### 1. 模型效果 vs 线上表现

- benchmark 更像静态信号
- runtime 表现是系统级结果

### 2. Serving vs Ops

- serving 是服务形态与请求承接
- ops 是长期运行、监控、反馈、修复和治理

### 3. Eval vs Release Gate

- eval 负责判断变化
- release gate 负责放量决策

### 4. Safety vs Security

- safety 更偏失误、伤害、行为边界
- security 更偏攻击、越权、供应链和控制链路

## 九、建议学习顺序

1. [[Inference Efficiency]]
2. [[AI 基础设施与 GPU Cloud]]
3. [[Inference Serving]]
4. [[MLOps 与 LLMOps]]
5. [[Evaluation]]
6. [[../../AI-Engineering/07-Topics/Eval Harness 与 Regression Suites|Eval Harness 与 Regression Suites]]
7. [[../../AI-Engineering/07-Topics/Agent 上线门槛与安全 Release Gates|Agent 上线门槛与安全 Release Gates]]
8. [[AI Security]]
9. [[AI Safety 与 AI Security]]
10. [[Prompt Injection 与 Jailbreaks]]
11. [[../../AI-Engineering/07-Topics/LLMOps、AgentOps 与 Observability|LLMOps、AgentOps 与 Observability]]

## 十、这条线在面试里能回答什么

- 为什么 AI 系统上线难点常常不在模型，而在 runtime
- 你会如何设计 eval、release gate 和 rollback 闭环
- 你如何平衡模型能力、成本、延迟和安全
- 为什么 AI 安全不能只做成一个输出过滤器

## 关联

- [[AI 五条主干专家工作台]]
- [[AI 领域知识点总纲：点、线、面与层]]
- [[AI 主题索引]]
- [[../07-Maps/AI 知识点点线面图|AI 知识点点线面图]]
- [[Inference Efficiency]]
- [[Inference Serving]]
- [[Evaluation]]
- [[AI Security]]
- [[AI Safety 与 AI Security]]
