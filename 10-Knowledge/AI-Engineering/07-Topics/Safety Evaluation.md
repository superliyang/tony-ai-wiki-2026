---
title: Safety Evaluation
type: topic
status: learning
tags:
  - ai/engineering
  - ai/safety-eval
created: 2026-03-13
updated: 2026-03-28
---

# Safety Evaluation

## 为什么它是训练和上线之间的硬边界

模型质量高并不等于可安全上线。

`Safety evaluation` 的作用不是证明系统“绝对安全”，而是持续识别风险边界，并把高风险版本挡在生产门外。

因此它必须贯穿：

- 训练前的数据治理
- post-training 后的离线评测
- 发布前的红队与门禁
- 上线后的持续监控

## 安全评测到底在评什么

至少要看 5 类风险：

1. 有害内容生成
2. 越狱与 prompt injection 成功率
3. 隐私泄露与数据外流
4. 高风险场景下的误导、操纵或错误建议
5. 工具、检索、memory、agent action 引入的系统性风险

## 安全评测不是单一指标，而是分层系统

### 1. Dataset-level checks

- 训练数据是否带入明显高风险模式
- post-training 数据是否引入危险 instruction
- 是否存在训练 / eval contamination

### 2. Offline model evals

- 固定攻击集
- 已知 jailbreak 套件
- 风险类别 benchmark
- refusal / over-refusal 分析

### 3. Human review

- 高风险领域抽样
- 边界案例复核
- 自动化分类器误杀 / 漏杀校验

### 4. Release gates

- 关键风险指标是否低于阈值
- 关键能力回归是否在可接受范围内
- 新功能是否引入新攻击面

### 5. Post-deployment monitoring

- 线上告警
- 抽样复查
- escalation 和 rollback
- 红队与用户报告回流

## 常见安全评测方式

### 内容安全检测

- harm categories
- classifier / rules / policy models
- refusal accuracy

### 越狱与注入测试

- jailbreak prompts
- roleplay / obfuscation / multi-turn attacks
- tool escalation / indirect injection

### 任务型安全评测

- 代码生成安全
- tool calling 安全
- 浏览器 / desktop action 安全
- 高风险领域问答安全

### Agent / system evals

- 是否调用了不该调用的工具
- 是否越权访问数据
- 是否泄露 system prompt、memory、secret

## 为什么安全评测很难

### 1. 风险是动态对抗的

攻击者会变，攻击语料会变，系统集成方式也会变。

### 2. 产品形态决定风险形态

同一个模型做：

- chat
- coding
- browser agent
- workflow automation

其攻击面完全不同。

### 3. 自动化指标覆盖不完整

很多伤害形式并不容易被单一分数捕捉。

## 学这一页要形成的判断力

### 判断 1：这是模型安全问题，还是系统安全问题

如果风险来自工具权限、检索污染或 memory 泄露，仅靠模型重训往往不够。

### 判断 2：评测失败是否代表不能上线

要看：

- 场景风险级别
- 失败频率
- 可补救控制点
- 是否能通过 release gate 限制范围

### 判断 3：当前安全标准是否和产品形态匹配

聊天助手、coding agent、browser agent 的门槛应该不同。

## 典型失败模式

- 只做一次离线红队，没有持续监控
- 只看内容安全，不看 tool misuse
- 看 refusal 率，却不看 over-refusal
- 安全指标通过，但上线后没有 escalation 机制

## 推荐怎么连着读

1. [[Security and Privacy]]
2. [[AI Security Threat Modeling]]
3. [[Prompt Injection Defense 与 Tool Safety]]
4. [[AI Security Evaluation 与 Red Teaming]]
5. [[Agent 上线门槛与安全 Release Gates]]

## 相关主题

- [[Training Stack Overview]]
- [[Security and Privacy]]
- [[AI Security Threat Modeling]]
- [[AI Security Evaluation 与 Red Teaming]]
- [[Agent 上线门槛与安全 Release Gates]]
- [[Evaluation and Benchmarks]]
- [[Model Registry and Deployment]]

## 资料

- [NIST GenAI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [NIST Cyber AI Profile](https://csrc.nist.gov/pubs/ir/8596/iprd)
- [OpenAI Evaluation Best Practices](https://platform.openai.com/docs/guides/evaluation-best-practices)
- [OpenAI Working with Evals](https://platform.openai.com/docs/guides/evals/evaluating-model-performance-beta)
- [Anthropic Guardrails](https://docs.anthropic.com/en/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)
