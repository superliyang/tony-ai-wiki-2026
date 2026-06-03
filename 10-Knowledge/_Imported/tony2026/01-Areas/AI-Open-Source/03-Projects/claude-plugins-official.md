---
title: claude-plugins-official
type: project
status: learning
domain: ai-open-source
category: Claude Code 生态扩展
organization: Anthropic
repo: https://github.com/anthropics/claude-plugins-official
local_fit: high
mac_fit: high
production_fit: medium
learning_fit: high
created: 2026-05-15
updated: 2026-05-15
---

# claude-plugins-official

## 它解决什么问题

`claude-plugins-official` 是 Anthropic 管理的 Claude Code plugins directory，用来发现、安装和学习 plugin 的标准结构。

## 为什么现在值得关注

Claude Code 的扩展生态正在从散落的 commands / agents / hooks 走向 marketplace 和 plugin bundle。这个 repo 是理解“插件应该怎么组织”的官方样本。

## 它在 stack 的哪一层

- 属于 `plugin marketplace / plugin distribution`
- 位于 skill、command、agent、hook、MCP 的上层打包层
- 更像 Claude Code 生态的“应用商店入口”

## 核心组件与架构

- `.claude-plugin/plugin.json`：插件元数据
- `commands/`：slash commands
- `agents/`：subagents
- `skills/`：skills
- `.mcp.json`：MCP 配置
- `plugins/` 与 `external_plugins/`：官方与第三方插件目录

## 最适合它的场景

- 学习 plugin 目录结构
- 选择可信 marketplace 起点
- 研究如何把团队能力打包分发

## 和相邻项目怎么区分

- 和 [[anthropics-skills]]：它管 plugin 打包和发现，skills repo 管单个 skill 的写法
- 和 [[awesome-claude-plugins]]：它更官方；后者更偏社区 curated list

## 推荐的学习动作

1. 看 `example-plugin`
2. 看一个 internal plugin 和一个 external plugin 的结构差异
3. 设计自己的团队 plugin：commands + agents + skills + hooks

## 风险与边界

- 官方目录仍提示第三方插件需要信任审查
- plugin 可能包含 MCP、hooks 或外部软件，安装前必须看源码和权限

## 官方入口

- [anthropics/claude-plugins-official GitHub](https://github.com/anthropics/claude-plugins-official)

## 关联

- [[项目索引|项目索引]]
- [[../01-Categories/Claude Code 生态扩展|Claude Code 生态扩展]]

