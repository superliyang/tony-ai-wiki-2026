---
title: 应用安全与 API 安全
type: topic
status: seed
domain: Security
created: 2026-04-29
updated: 2026-04-29
---

# 应用安全与 API 安全

## 定位

应用安全关注业务系统本身如何避免被攻击、滥用和越权。

API 安全是现代应用安全的核心，因为移动端、前端、微服务、第三方集成和 AI agent 都越来越依赖 API。

## 关键问题

- 认证是否可靠
- 授权是否正确
- 输入是否可信
- 业务逻辑是否可被绕过
- API 是否可被批量滥用
- 错误信息、日志、接口响应是否泄露敏感信息

## 主要控制

- secure coding
- threat modeling
- input validation
- output encoding
- authentication / authorization
- rate limiting
- API gateway
- WAF / RASP
- SAST / DAST / IAST
- security code review

## 高频风险

- SQL injection
- XSS
- SSRF
- broken access control
- IDOR
- insecure deserialization
- mass assignment
- business logic abuse
- API token leakage

## 和其他分支的关系

- 和 [[身份与访问安全]] 共同处理 authn / authz
- 和 [[数据安全与隐私保护]] 共同处理敏感数据读写
- 和 [[供应链安全]] 共同处理依赖漏洞和构建安全
- 和 [[安全治理、风险与合规]] 共同形成 SDLC 和安全评审机制
