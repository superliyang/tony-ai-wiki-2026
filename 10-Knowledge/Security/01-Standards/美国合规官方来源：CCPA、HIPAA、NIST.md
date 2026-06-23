---
title: 美国合规官方来源：CCPA、HIPAA、NIST
type: standard
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# 美国合规官方来源：CCPA、HIPAA、NIST

## 定位

美国不是一个单一隐私法体系，常见是：

- 州隐私法：例如 California CCPA / CPRA。
- 行业法：例如 HIPAA。
- 安全框架：例如 NIST CSF、NIST SP 800 系列。
- 执法和消费者保护：FTC、州 AG、行业监管。

## 官方来源

- California Privacy Protection Agency：<https://cppa.ca.gov/>
- California CCPA resources：<https://oag.ca.gov/privacy/ccpa>
- HHS HIPAA：<https://www.hhs.gov/hipaa/index.html>
- HHS HIPAA Security Rule：<https://www.hhs.gov/hipaa/for-professionals/security/index.html>
- NIST Cybersecurity Framework：<https://www.nist.gov/cyberframework>
- NIST Privacy Framework：<https://www.nist.gov/privacy-framework>
- FTC data security guidance：<https://www.ftc.gov/business-guidance/privacy-security/data-security>

## CCPA / CPRA：加州消费者隐私

### 关键问题

- 是否适用 CCPA / CPRA 范围？
- 是否收集 California consumer personal information？
- 是否涉及 sale / share？
- 是否处理 sensitive personal information？
- privacy notice 是否清晰？
- 消费者请求如何响应？
- 第三方、service provider、contractor 的合同条款是否齐全？

### 技术与证据

- 数据类别和收集目的。
- privacy notice 和 request workflow。
- opt-out / limit use of sensitive personal information。
- request verification and fulfillment record。
- vendor contract record。
- data retention schedule。

## HIPAA：健康信息安全与隐私

### 关键问题

- 是否是 covered entity 或 business associate？
- 是否处理 electronic protected health information？
- Security Rule 的 administrative、physical、technical safeguards 如何覆盖？
- 是否有 risk analysis 和 risk management？
- 是否有 breach notification 流程？

### 技术与证据

- risk analysis。
- access control。
- audit controls。
- integrity controls。
- transmission security。
- workforce training。
- business associate agreement。
- incident and breach record。

## NIST：安全风险管理语言

### 关键问题

- 是否需要统一安全能力语言？
- 是否要建立 Identify、Protect、Detect、Respond、Recover 的控制体系？
- 是否要将安全指标和管理层汇报标准化？
- 是否用于客户审计或内部成熟度评估？

### 技术与证据

- asset inventory。
- risk assessment。
- access control。
- data security。
- logging and monitoring。
- incident response。
- recovery planning。
- governance and metrics。

## 安全落地判断

美国合规最大的难点是“州 + 行业 + 合同 + 客户审计”叠加。安全团队应该先把：

- 数据主体和地区。
- 行业数据类型。
- 第三方共享。
- 安全控制证据。
- breach notification obligations。

整理成一张矩阵，再和法务、隐私、合规团队确认。

## 关联

- [[./地区合规官方来源索引|地区合规官方来源索引]]
- [[./安全标准与法规索引|安全标准与法规索引]]
- [[../05-Topics/数据安全与隐私保护|数据安全与隐私保护]]
- [[../08-Playbooks/数据安全与隐私评审 Playbook|数据安全与隐私评审 Playbook]]
