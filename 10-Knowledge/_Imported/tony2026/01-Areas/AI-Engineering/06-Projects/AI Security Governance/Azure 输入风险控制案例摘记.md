---
title: Azure 输入风险控制案例摘记
type: case-study
status: learning
created: 2026-03-27
updated: 2026-03-27
---

# Azure 输入风险控制案例摘记

## 这个案例为什么值得看

它不是完整企业案例，而是一个很有代表性的“控制点案例”：

- 把 jailbreak / prompt injection 检测前置到模型入口
- 把风险识别结果作为后续 guardrails 和 policy 的输入

## 适合学什么

- managed input detection 在体系里的位置
- 为什么输入检测不能替代 tool safety
- 企业为什么会先从 detection layer 开始，而不是一步到位做完整 agent governance

## 工程启发

- 适合做网关层的第一道风险筛查
- 适合和 release gate、人工复核、降级策略联动
- 适合多应用共享，而不是每个团队各自发明输入过滤逻辑

## 关联

- [[../../07-Topics/Prompt Injection Defense 与 Tool Safety|Prompt Injection Defense 与 Tool Safety]]
- [[../../07-Topics/Enterprise AI Security Operating Model|Enterprise AI Security Operating Model]]
- [[../../../AI-Learning/09-Systems/Azure AI Content Safety（Jailbreak Detection）|Azure AI Content Safety（Jailbreak Detection）]]

## 资料

- [Azure AI Content Safety jailbreak risk detection](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection)
