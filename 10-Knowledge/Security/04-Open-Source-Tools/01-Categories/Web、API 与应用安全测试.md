---
title: Web、API 与应用安全测试
type: category
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# Web、API 与应用安全测试

## 解决什么问题

- 验证 Web、API、认证授权、输入输出、业务逻辑和客户端交互安全。
- 把应用安全从“上线前人工测试”推进到可重复的工具链。

## 代表项目

- [OWASP ZAP](https://github.com/zaproxy/zaproxy)：Web 应用安全测试代理与扫描。
- [mitmproxy](https://github.com/mitmproxy/mitmproxy)：HTTP/TLS 交互式代理。
- [sqlmap](https://github.com/sqlmapproject/sqlmap)：SQL 注入自动化验证。
- [ffuf](https://github.com/ffuf/ffuf)：Web fuzzing。
- [gobuster](https://github.com/OJ/gobuster)：目录、DNS、vhost 枚举。
- [dirsearch](https://github.com/maurosoria/dirsearch)：Web 路径扫描。
- [kiterunner](https://github.com/assetnote/kiterunner)：API 内容发现。
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)：漏洞 payload 和绕过知识库。
- [OWASP WSTG](https://github.com/OWASP/wstg)：Web Security Testing Guide。
- [OWASP Juice Shop](https://github.com/juice-shop/juice-shop)：可练习的不安全 Web 应用。

## 典型组合

`代理抓包 -> API/路径发现 -> 认证授权测试 -> fuzz -> 漏洞验证 -> 复测 -> 评审报告`

## 风险与边界

- 自动化测试不能替代威胁建模和业务逻辑评审。
- SQL 注入、fuzz 和扫描必须限定在授权测试环境。

