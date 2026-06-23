---
title: 欧盟合规官方来源：GDPR、NIS2、DORA
type: standard
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# 欧盟合规官方来源：GDPR、NIS2、DORA

## 定位

欧盟合规的主线可以粗略分成三层：

- `GDPR`：个人数据保护和隐私权利。
- `NIS2`：关键和重要实体的网络安全风险管理与事件报告。
- `DORA`：金融实体的 ICT 风险、韧性、第三方和事件管理。

## 官方来源

- European Commission GDPR：<https://commission.europa.eu/law/law-topic/data-protection/data-protection-eu_en>
- GDPR text：<https://eur-lex.europa.eu/eli/reg/2016/679/oj>
- EDPB guidance：<https://www.edpb.europa.eu/our-work-tools/general-guidance_en>
- European Commission NIS2：<https://digital-strategy.ec.europa.eu/en/policies/nis2-directive>
- NIS2 text：<https://eur-lex.europa.eu/eli/dir/2022/2555/oj>
- European Commission DORA：<https://finance.ec.europa.eu/digital-finance/digital-operational-resilience-act-dora_en>
- DORA text：<https://eur-lex.europa.eu/eli/reg/2022/2554/oj>

## GDPR：隐私与个人数据

### 关键问题

- 是否处理欧盟数据主体的个人数据？
- 组织角色是 controller 还是 processor？
- lawful basis 是什么？
- 是否涉及 special category data？
- 是否需要 DPIA？
- 是否跨境传输到 EEA 外？
- 是否能响应访问、更正、删除、限制处理、可携带、反对等权利？
- 是否有个人数据泄露通报流程？

### 技术与证据

- RoPA / 处理活动记录。
- DPIA。
- 数据流图和跨境传输记录。
- DPA / processor agreement。
- SCC、adequacy、TIA 等跨境材料。
- 访问控制、加密、日志、删除证明。
- breach record 和通报决策记录。

## NIS2：网络安全与关键实体

### 关键问题

- 是否属于 essential 或 important entity？
- 是否覆盖供应链和 ICT 服务商风险？
- 是否有网络安全风险管理措施？
- 事件是否达到重大影响阈值？
- 管理层是否承担监督责任？

### 技术与证据

- risk management policy。
- incident handling process。
- business continuity / crisis management。
- supply chain security review。
- vulnerability handling。
- encryption、access control、asset management。
- incident reporting evidence。

## DORA：金融数字运营韧性

### 关键问题

- 是否为金融实体或关键 ICT 第三方服务商？
- ICT 风险管理框架是否存在？
- 重大 ICT 事件如何报告？
- 数字运营韧性测试如何执行？
- 第三方 ICT 风险如何治理？

### 技术与证据

- ICT asset inventory。
- incident classification and reporting。
- resilience testing。
- third-party ICT register。
- exit plan and concentration risk analysis。
- logging、monitoring、backup、recovery evidence。

## 安全落地判断

欧盟合规不要只看隐私文案。安全团队至少要能提供：

- 数据处理和跨境传输证据。
- 身份、访问、加密、日志和删除控制。
- 安全事件和个人数据泄露的分级流程。
- 第三方和供应链安全证据。
- 管理层可读的风险和整改记录。

## 关联

- [[./地区合规官方来源索引|地区合规官方来源索引]]
- [[../05-Topics/数据安全与隐私保护|数据安全与隐私保护]]
- [[../05-Topics/安全治理、风险与合规|安全治理、风险与合规]]
- [[../08-Playbooks/数据安全与隐私评审 Playbook|数据安全与隐私评审 Playbook]]
