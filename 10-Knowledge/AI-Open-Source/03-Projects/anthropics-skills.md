---
title: anthropics-skills
type: project
status: learning
domain: ai-open-source
category: Claude Code 生态扩展
organization: Anthropic
repo: https://github.com/anthropics/skills
local_fit: high
mac_fit: high
production_fit: medium
learning_fit: high
created: 2026-05-15
updated: 2026-05-15
---

# anthropics-skills

## 它解决什么问题

`anthropics/skills` 是 Anthropic 公开的 Agent Skills 样例与规范参考，用来说明 skill 如何组织、安装、触发和复用。

## 为什么现在值得关注

这是理解 Claude Code `skill` 机制最直接的开源入口。它既有示例 skills，也有 template 和 spec，适合学习如何把高频任务方法沉淀成可复用能力。

## 它在 stack 的哪一层

- 属于 `skill specification / reference implementation`
- 是 Claude Code 自定义能力的底层样板
- 位于 `prompt pattern` 和 `plugin marketplace` 之间

## 核心组件与架构

- `skills/`：示例技能集合
- `spec/`：Agent Skills 规范
- `template/`：自定义 skill 模板
- plugin marketplace 安装方式：可作为 Claude Code marketplace 注册

## 核心对象模型 / 核心抽象

- `SKILL.md`
- `name`
- `description`
- instructions / examples / guidelines
- optional scripts / assets / references

## 最适合它的场景

- 学习 skill 结构
- 自定义团队 skills
- 做文档、表格、开发、企业沟通等可复用能力参考

## 和相邻项目怎么区分

- 和 [[claude-plugins-official]]：它更偏 skill 规范与样例；后者更偏 plugin marketplace 与打包分发
- 和 [[claude-code-templates]]：它更官方、更基础；后者更偏第三方组件集合与安装 CLI

## 推荐的学习动作

1. 先读 template skill
2. 再看 document / development 类 skill 如何写 description
3. 最后为自己的项目写一个 `repo-review` 或 `security-review` skill

## 风险与边界

- 不是所有示例都适合直接生产使用
- 官方也提示要在自己的环境充分测试后再用于关键任务

## 官方入口

- [anthropics/skills GitHub](https://github.com/anthropics/skills)

## 关联

- [[项目索引|项目索引]]
- [[../01-Categories/Claude Code 生态扩展|Claude Code 生态扩展]]

