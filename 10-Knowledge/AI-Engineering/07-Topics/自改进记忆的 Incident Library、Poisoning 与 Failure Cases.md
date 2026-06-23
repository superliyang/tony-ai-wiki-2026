---
title: 自改进记忆的 Incident Library、Poisoning 与 Failure Cases
type: topic
status: learning
tags:
  - ai/engineering
  - ai/memory
  - ai/security
  - ai/runtime
created: 2026-03-29
updated: 2026-03-29
---

# 自改进记忆的 Incident Library、Poisoning 与 Failure Cases

## 为什么这页要单独存在

`self-improving memory` 最大的问题不是设计图，而是事故很容易“看起来像正常学习”。

所以这页不把重点放在抽象定义，而是把最常见的失败模式压成一个 `incident library`。

## 读这页时先记住一句话

**在自改进系统里，最危险的不是一次回答错，而是系统把错误学会了。**

## Incident 1：不可信内容诱导写入 learnings

### 触发方式

- 网页、邮件、工单、论坛、MCP resource、第三方知识库里包含恶意 instruction
- agent 在完成主任务时顺手把这段 instruction 当成“新经验”写入 `.learnings/*`

### 为什么会发生

- tool output 和 user instruction 在模型眼里容易混在一起
- write-memory 动作没有 provenance gate
- 第三方 MCP / plugin 输出被过度信任

### 典型症状

- 后续 session 出现“莫名其妙的新规则”
- skill extraction 开始围绕错误经验生长
- 同类任务越来越偏，而不是越来越稳

### 检测信号

- learning 条目没有明确来源或 related artifact
- 同一类 rule 只在单一外部来源出现
- 被写入的内容含有 instruction style 文本，而不是事实性总结

### 恢复动作

- 先冻结 promotion
- 将条目降级回 learning-only
- 回查 provenance
- 补 red-team case 到 eval suite

## Incident 2：compaction / consolidation 把 uncertainty 压没了

### 触发方式

- background consolidation 把“疑似问题”写成“稳定结论”
- compaction summary 遗漏否定词、条件限制、来源不确定性

### 为什么会发生

- 压缩逻辑天然追求简洁
- 简洁 often 牺牲 provenance 和 caveat
- system 没有要求保留 confidence / source

### 典型症状

- 新 session 里看到的 memory 语气越来越肯定
- 但原始证据其实并不充分

### 恢复动作

- long-term memory 写入必须带来源
- consolidation 输出必须保留 `confidence` 或 `status`
- 对 compaction 结果做 spot review

## Incident 3：shared memory 跨 scope 泄漏

### 触发方式

- user/project/team/tenant 没分清
- 多 agent 共用同一 namespace
- 项目 A 的 workaround 被项目 B 继承

### 为什么会发生

- scope 只是工程便利性，没有被当作安全边界
- store namespace 设计过粗
- 没有按 working tree / tenant / environment 分层

### 典型症状

- 不同项目出现相同但不合理的偏好
- 子 agent 继承了不该共享的上下文
- 纠错发生在一个 agent，漂移却扩散到多个 agent

### 恢复动作

- 收紧 namespace
- 加 shared-memory write review
- 区分 `session state / project memory / shared memory / policy files`

## Incident 4：一次性 workaround 被 promotion 成 durable rule

### 触发方式

- 某次调试靠临时手段绕过问题
- 由于看起来“有效”，被写入 `AGENTS.md` / `TOOLS.md` / `MEMORY.md`

### 为什么会发生

- recurrence 没验证
- success signal 只看“这次过了”，不看长期副作用
- promotion 缺少 human review

### 典型症状

- 后续新任务被这个 rule 锁死
- 系统变得越来越教条
- 旧 bug 消失，新 bug 增加

### 恢复动作

- 要求 promotion 附带 recurrence evidence
- 规则增加 `valid_for / invalid_if` 说明
- 允许 demotion 到 learning ledger

## Incident 5：第三方 MCP / plugin 把风险带进记忆层

### 触发方式

- 第三方 MCP server / plugin fetch 不可信内容
- 扩展本身的 prompt、tool schema、resource 文本带有误导性默认

### 为什么会发生

- 工具接入看起来像“基础设施”，但其实是 prompt surface
- 安装时只看功能，不看信任边界

### 典型症状

- 某类 tool 一启用，agent 的记忆写入风格就变化
- 记忆中出现扩展特定的偏置

### 恢复动作

- 对 MCP / plugin 增加 allowlist
- 对 memory write 保持 tighter permission
- 将第三方输出当作 untrusted content 处理

## Incident 6：background agent 静默写入，没人发现

### 触发方式

- cron / hook / background agent 在无人监督时写 memory
- 写入发生在 compaction flush 或 daily cleanup 阶段

### 为什么会发生

- “自动整理”被当成低风险操作
- silent path 没有 audit trail

### 典型症状

- 用户只发现行为变了，却找不到是谁改了什么
- 问题不是单次 reply，而是几轮之后才显现

### 恢复动作

- 背景写入必须有 ledger
- 关键 promotion 必须产生 review artifact
- 支持按时间窗口回滚

## 从 incident library 提炼出来的默认门槛

1. 所有 durable memory 写入都带 provenance
2. 所有 shared-memory 写入都带 scope
3. 所有 promotion 都要经过 eval gate
4. 所有 skill extraction 都支持 rollback / demotion
5. 第三方 tool / plugin / MCP 输出默认按 untrusted 处理

## 主要依据

- [OWASP Agentic Threats Navigator](https://genai.owasp.org/resource/owasp-gen-ai-security-project-agentic-threats-navigator/)
- [NIST Adversarial ML Taxonomy and Terminology](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=959735)
- [OpenClaw Memory](https://docs.openclaw.ai/concepts/memory)
- [OpenClaw Hooks](https://docs.openclaw.ai/automation/hooks)
- [Claude Code MCP](https://code.claude.com/docs/en/mcp)
- [Claude Code Memory](https://code.claude.com/docs/en/memory)
- [ChatGPT Agent System Card](https://cdn.openai.com/pdf/6bcccca6-3b64-43cb-a66e-4647073142d7/chatgpt_agent_system_card_launch.pdf)

## 关联

- [[记忆评测、污染、遗忘与纠偏]]
- [[Learnings、Promotion 与 Skill Extraction Pipeline]]
- [[共享记忆边界：用户、项目、多 Agent 与租户隔离]]
- [[自改进 Skill 的 Eval Gate、Release Gate 与 Rollback]]
- [[../06-Projects/Memory Lab/Memory Poisoning、Shared Memory Boundary 与 Release Gates 实验|Memory Poisoning、Shared Memory Boundary 与 Release Gates 实验]]
