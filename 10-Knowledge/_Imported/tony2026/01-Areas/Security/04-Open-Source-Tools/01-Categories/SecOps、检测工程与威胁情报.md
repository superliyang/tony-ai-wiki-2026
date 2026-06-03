---
title: SecOps、检测工程与威胁情报
type: category
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# SecOps、检测工程与威胁情报

## 解决什么问题

- 把日志、检测规则、终端查询、网络检测、威胁情报和 case 管理连成 SOC 工作流。
- 支撑蓝队、紫队和事件响应。

## 代表项目

- [Wazuh](https://github.com/wazuh/wazuh)：开源 SIEM/XDR。
- [osquery](https://github.com/osquery/osquery)：用 SQL 查询终端状态。
- [Sigma](https://github.com/SigmaHQ/sigma)：通用检测规则格式。
- [YARA](https://github.com/VirusTotal/yara)：恶意样本和模式匹配规则。
- [Suricata](https://github.com/OISF/suricata)：IDS/IPS/NSM。
- [Zeek](https://github.com/zeek/zeek)：网络安全监控和协议分析。
- [MISP](https://github.com/MISP/MISP)：威胁情报共享平台。
- [TheHive](https://github.com/TheHive-Project/TheHive)：事件响应 case 管理。
- [Cortex](https://github.com/TheHive-Project/Cortex)：分析器和响应器。
- [sysmon-config](https://github.com/SwiftOnSecurity/sysmon-config)：Sysmon 配置模板。
- [LOLBAS](https://github.com/LOLBAS-Project/LOLBAS)：Living off the land 知识库。
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)：对抗技术测试库。

## 典型组合

`日志源 -> Sigma / YARA / Zeek / Suricata -> Wazuh / SIEM -> TheHive -> Cortex / 响应 -> MISP`

## 学习价值

- 理解检测工程不是写一条规则，而是从攻击技术到数据源、规则、分诊、响应和复盘的链路。

