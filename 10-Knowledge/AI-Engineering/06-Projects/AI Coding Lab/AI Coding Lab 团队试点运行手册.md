---
title: AI Coding Lab 团队试点运行手册
type: playbook
status: active
created: 2026-05-16
updated: 2026-05-16
---

# AI Coding Lab 团队试点运行手册

## 试点目标

团队试点不是为了证明“AI 很厉害”，而是为了回答：

- 哪些任务真的能提效
- 哪些任务风险太高
- 哪些规则需要写入项目记忆
- 哪些能力值得沉淀成 skill / subagent / hook / plugin
- 哪些质量指标和风险指标必须长期跟踪

## 试点范围

### 建议纳入

- 小型 bugfix
- 测试补全
- 文档同步
- PR summary
- review comment follow-up
- 低风险重构

### 暂不纳入

- 生产配置变更
- 鉴权、安全、支付、账号核心链路大改
- 数据库 schema 破坏性变更
- 大型架构迁移
- 无测试保护的核心模块重构

## 默认权限策略

| 能力 | 默认策略 |
|---|---|
| 读代码 | 允许 |
| 改代码 | 限定目录和任务范围 |
| 跑测试 | 允许 |
| 跑危险 shell | 人工审批 |
| Git destructive 命令 | 阻断或人工审批 |
| 读取 secret | 阻断 |
| 读取生产数据 | 阻断或只读脱敏 |
| 写外部系统 | 默认禁止 |
| PR comment | 可试点 |
| merge / release | 人工控制 |

## 试点流程

### Step 1：选择 repo

选择标准：

- 有测试或静态检查
- 任务边界清晰
- 业务风险低
- reviewer 有时间看 diff

### Step 2：写项目规则

最小内容：

- 项目结构
- 启动命令
- 测试命令
- 禁改目录
- 提交和 PR 格式
- 安全敏感模块

### Step 3：选择任务

每次任务必须有：

- task brief
- 可改范围
- 验证方式
- reviewer
- 完成标准

### Step 4：执行与记录

使用 [[AI Coding Lab 实战任务记录模板]]。

重点记录：

- 是否读对上下文
- 是否误改无关文件
- 是否跑了验证
- 是否尝试危险命令
- 是否需要人工救场

### Step 5：评估

使用 [[../../04-Evaluation/AI Coding 专家能力验收矩阵|AI Coding 专家能力验收矩阵]]。

试点至少看：

- 成功率
- 测试通过率
- review 返工率
- 无关改动率
- 危险命令尝试率
- 人工节省时间

### Step 6：沉淀与决策

每周复盘：

- 哪些任务继续开放
- 哪些任务暂停
- 哪些规则写入项目记忆
- 哪些流程做成 skill / subagent / hook
- 是否进入下一阶段试点

## 角色分工

- owner：决定试点范围和风险边界
- developer：执行任务并记录结果
- reviewer：审查 diff、测试和风险
- security owner：定义敏感路径和危险命令策略
- platform owner：维护共享 skills、hooks、MCP、plugins

## 退出条件

如果出现以下情况，试点应暂停：

- 多次误改核心模块
- 多次绕过测试
- 尝试读取 secret 或生产数据
- PR 噪音明显高于收益
- 团队无法稳定 review agent 输出

## 关联

- [[项目总览]]
- [[AI Coding Lab 30 天训练路线]]
- [[AI Coding Lab 专家验收清单]]
- [[../../08-Maps/AI Coding 团队落地路线图|AI Coding 团队落地路线图]]
- [[../../08-Maps/AI Coding 安全治理决策图|AI Coding 安全治理决策图]]

