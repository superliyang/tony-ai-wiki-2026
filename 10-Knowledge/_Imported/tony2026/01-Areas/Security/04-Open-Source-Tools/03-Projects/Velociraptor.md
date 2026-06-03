---
title: Velociraptor
type: project
status: learning
domain: Security
category: DFIR、逆向与恶意样本分析
organization: Velocidex
repo: https://github.com/velocidex/velociraptor
local_fit: medium
mac_fit: medium
production_fit: medium
learning_fit: high
updated: 2026-05-05
---

# Velociraptor

## 它是什么

Velociraptor 是面向终端可见性、DFIR、威胁狩猎和事件响应的开源平台。

## 为什么现在值得关注

- 能把“事件响应”从手工登录主机变成集中查询、采集和分析。
- 对理解 EDR/MDR 背后的响应工作流很有帮助。

## 它在 stack 的哪一层

- 更像 `平台`：DFIR 和终端狩猎平台。

## 核心抽象

- artifact：查询和采集逻辑。
- client：终端 agent。
- hunt：批量狩猎任务。
- notebook / collection：分析和证据组织。

## 最适合它的场景

- DFIR 实验室。
- 勒索、凭据窃取、异常进程和持久化调查。

## 风险与边界

- 取证需要权限、证据链和操作审计。
- 生产部署要考虑隐私和终端性能影响。

## 关联

- [[../01-Categories/DFIR、逆向与恶意样本分析|DFIR、逆向与恶意样本分析]]
- [[../../08-Playbooks/安全事件响应 Playbook|安全事件响应 Playbook]]

