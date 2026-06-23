---
title: DFIR、逆向与恶意样本分析
type: category
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# DFIR、逆向与恶意样本分析

## 解决什么问题

- 事件发生后做取证、时间线、内存分析、终端调查、移动应用分析和样本分析。
- 支撑事件响应、威胁狩猎和恶意软件分析。

## 代表项目

- [Velociraptor](https://github.com/velocidex/velociraptor)：终端可见性、DFIR 和威胁狩猎。
- [Volatility3](https://github.com/volatilityfoundation/volatility3)：内存取证。
- [Timesketch](https://github.com/google/timesketch)：时间线协作分析。
- [x64dbg](https://github.com/x64dbg/x64dbg)：Windows 逆向调试。
- [radare2](https://github.com/radareorg/radare2)：逆向工程框架。
- [Frida](https://github.com/frida/frida)：动态插桩。
- [MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF)：移动应用安全分析。
- [REMnux](https://github.com/REMnux/remnux-distro)：恶意软件分析发行版。

## 典型组合

`Velociraptor -> 证据采集 -> Timesketch -> Volatility/YARA -> 复盘报告`

## 风险与边界

- 取证必须注意证据链、时间同步和权限边界。
- 样本分析要隔离环境，避免污染主机。

