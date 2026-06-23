---
title: AI Coding Agent 场景题包
type: scenario-pack
status: active
updated: 2026-04-12
---

# AI Coding Agent 场景题包

## 一、场景定义

- 典型公司：做研发提效、代码助手、代码审查、自动修复、测试生成、repo agent 的团队。
- 典型目标：缩短开发反馈回路、提升修复效率、降低重复工作，同时控制错误改动、权限风险和回归风险。
- 面试官最想确认的是：你理解的不是“让模型会写代码”，而是“让代码改动可验证、可回滚、可审计”。

## 二、这类岗位最常见的问题树

### 开场与项目题

- 讲一个你做过的 coding agent / 开发提效项目。
- 这个系统和普通代码补全最大的区别是什么？
- 你在项目里真正负责的是模型、工具、评测，还是平台链路？

### 架构设计题

- 设计一个 AI Coding Agent，你会怎么分层？
- 如何给 agent 提供 repo context，而不把上下文堆爆？
- 怎么设计 sandbox、tool gateway 和 test gate？

### 质量与风险题

- 怎么评测 coding agent 的效果？
- 如果它稳定地产生“看起来合理但其实错”的改动怎么办？
- 如何控制越权、secret 泄露和 destructive action？

### 成本与体验题

- 长仓库、大上下文场景里怎么控成本和延迟？
- 什么时候用多 Agent，什么时候坚持单 Agent？

## 三、标准答法骨架

### 1. 设计一个 AI Coding Agent

- 先讲目标：不是“写更多代码”，而是提升通过验证的有效改动率。
- 再讲分层：planner / context builder / tool executor / verifier / reviewer。
- 再讲工具：读文件、搜代码、跑测试、改文件、看 diff，但高风险动作受限。
- 再讲验证：lint、unit test、repo policy、diff heuristics、人工 review。
- 最后讲治理：回放日志、失败样本、benchmark repo、release gate。

### 2. 这和代码补全有什么不同

- 补全是局部 token 预测，coding agent 是任务闭环。
- 它必须理解 repo、调用工具、验证结果、控制权限，还要能回滚。
- 所以核心难点不在模型会不会写，而在能不能稳定地产出可合并变更。

### 3. 怎么定义成功

- 不是看生成多少行代码，而是看 accepted diff rate、test pass rate、人工 review 成本、rollback rate。
- 还要看坏结果的上限能不能被门槛控制住。

## 四、面试官高频追问

### 追问 1：为什么不能让 agent 直接推到主分支？

- 因为 coding agent 的风险不只是代码错，而是它可能大范围改错、泄露信息、破坏生产分支。
- 高风险动作必须经 test gate 和 review gate，必要时保持 human-in-the-loop。

### 追问 2：repo 很大时，上下文怎么构建？

- 不能粗暴把整仓塞进去，要做 task-oriented context build。
- 先通过检索、调用图、符号级定位拿最相关片段，再按任务动态扩展。
- 旧上下文和无关文件要及时裁剪，否则成本和噪声都会上升。

### 追问 3：它偶尔很强、偶尔很差，你怎么收敛？

- 先做 failure taxonomy，把错分成上下文、检索、工具、验证、模型推理几类。
- 再做 benchmark repo 和 replay tasks，确保每次升级不是靠偶然成功。
- 最后把高频失败样本接进 release gate。

## 五、候选人反问模板

- “你们现在更看重 coding agent 的哪一类价值：提速、修 bug、测试生成，还是 code review？”
- “上线前你们要求通过哪些验证门槛？test gate 和人工 review 的边界在哪里？”
- “这个岗位更偏模型/agent 设计，还是偏平台治理和评测体系建设？”

## 六、复盘卡

- 我能否说清 coding agent 和代码补全的本质区别？
- 我能否讲出 `context -> tool -> verify -> review -> rollback` 的闭环？
- 我能否说出 3 个比“代码行数”更靠谱的 success metric？
- 我能否解释为什么高风险动作必须受控？
