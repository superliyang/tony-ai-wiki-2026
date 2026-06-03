---
title: 授权攻防、AD 与对抗模拟
type: category
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# 授权攻防、AD 与对抗模拟

> 这一类工具只适合授权测试、靶场、红队/紫队演练和防御验证。

## 解决什么问题

- 验证攻击路径、AD 风险、协议滥用、凭据风险和蓝队检测能力。
- 把红队发现转成检测、响应和控制改进。

## 代表项目

- [Metasploit Framework](https://github.com/rapid7/metasploit-framework)：漏洞验证和渗透测试框架。
- [Impacket](https://github.com/fortra/impacket)：网络协议操作和安全测试库。
- [BloodHound](https://github.com/SpecterOps/BloodHound)：AD 攻击路径分析。
- [Sliver](https://github.com/BishopFox/sliver)：对抗模拟框架。
- [PowerUpSQL](https://github.com/NetSPI/PowerUpSQL)：SQL Server 攻击面和权限分析。
- [PowerSploit](https://github.com/PowerShellMafia/PowerSploit)：PowerShell 安全测试工具集。
- [Rubeus](https://github.com/GhostPack/Rubeus)：Kerberos 相关安全测试。
- [Seatbelt](https://github.com/GhostPack/Seatbelt)：Windows 安全态势枚举。

## 典型组合

`授权范围 -> 攻击路径假设 -> 工具验证 -> 蓝队检测 -> 响应复盘 -> 控制改进`

## 风险与边界

- 必须有书面授权、范围、停止条件和证据规则。
- 不在第三方、生产或不明确授权环境中运行。

