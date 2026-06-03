---
title: 红队蓝队紫队演练路径 Playbook
type: playbook
status: active
domain: Security
created: 2026-05-05
updated: 2026-05-05
---

# 红队蓝队紫队演练路径 Playbook

> 用途：在授权范围内组织红队、蓝队、紫队演练，把攻击链、检测工程、事件响应和治理改进连成闭环。

## 安全边界

本 playbook 只用于授权演练、内部安全验证、桌面推演、检测工程和防御改进。

不要把它用于未授权扫描、入侵、绕过、持久化、横向移动或真实攻击活动。

## 一句话

红蓝紫演练的目标不是“红队赢”或“蓝队赢”，而是让组织知道：

`哪些攻击路径真实可行 -> 哪些信号看得见 -> 哪些响应能执行 -> 哪些控制要改进`

## 三种演练模式

### Tabletop Exercise

适合：

- 事件响应流程训练。
- 管理层、法务、隐私、公关、业务 owner 协同。
- 还没有成熟靶场或生产授权时。

输出：

- 决策时间线。
- 角色分工。
- 通报路径。
- 改进任务。

### Purple Team Exercise

适合：

- 验证检测规则。
- 调优日志源和分诊流程。
- 映射 ATT&CK TTP 到检测覆盖。

输出：

- TTP 覆盖矩阵。
- 检测规则改进。
- 告警分诊卡。
- 响应 playbook 更新。

### Red Team Assessment

适合：

- 验证真实业务风险。
- 测试端到端攻击路径。
- 检验组织检测和响应成熟度。

前提：

- 明确授权。
- 明确范围。
- 明确停止条件。
- 明确沟通和升级机制。

输出：

- 攻击路径复盘。
- 风险证明。
- 控制缺口。
- 管理层摘要。

## 演练流程

### 1. 定义目标和范围

必须写清：

- 演练目标。
- 授权系统。
- 禁止动作。
- 演练窗口。
- 联系人。
- 停止条件。
- 数据保护要求。
- 证据留存要求。

典型目标：

- 验证云密钥泄露响应。
- 验证账号接管检测。
- 验证数据导出异常检测。
- 验证 CI/CD secret 暴露风险。
- 验证 Kubernetes 高权限滥用检测。

### 2. 选择场景

优先选择业务相关场景：

- 高权限账号异常。
- 云 access key 泄露。
- 数据批量导出。
- CI/CD 供应链篡改。
- 公开漏洞应急。
- 终端恶意行为。
- 第三方系统数据泄露。

### 3. 映射 ATT&CK 和防御控制

做两张映射：

- ATT&CK：攻击者行为和 TTP。
- D3FEND / 内部控制：检测、隔离、阻断、取证、恢复。

注意：映射是语言，不是目的。真正要回答的是“这些行为我们看得见吗，能响应吗？”

### 4. 准备日志和检测

每个场景至少定义：

- 需要哪些日志。
- 哪些字段必须存在。
- 触发逻辑是什么。
- 排除逻辑是什么。
- 严重级别是什么。
- 分诊上下文是什么。
- 响应动作是什么。

关联：[[./SOC 检测工程 Playbook|SOC 检测工程 Playbook]]

### 5. 执行演练

执行时记录：

- 时间线。
- 操作事件。
- 触发的告警。
- 未触发的预期检测。
- 分诊动作。
- 响应动作。
- 沟通和升级。

要求：

- 不泄露真实敏感数据。
- 不破坏业务系统。
- 不扩大授权范围。
- 不把演练凭据留在环境里。

### 6. 复盘

复盘不只看技术结果：

- 哪些路径可行？
- 哪些日志缺失？
- 哪些检测没触发？
- 哪些告警无法分诊？
- 哪些响应动作不可执行？
- 哪些沟通和审批卡住？
- 哪些控制需要平台化？

### 7. 改进

改进项必须有：

- owner。
- 优先级。
- 截止时间。
- 验证方式。
- 复测计划。

## 场景库

### 场景 1：账号接管

训练目标：

- 身份日志。
- MFA 异常。
- 设备态势。
- 会话吊销。
- 高权限操作审计。

产物：

- 登录异常检测。
- 高风险账号响应流程。
- 用户通知和强制重置流程。

### 场景 2：云密钥泄露

训练目标：

- 云审计日志。
- access key 使用历史。
- 异常资源创建。
- 权限变更。
- 凭据轮换。

产物：

- 云 key 泄露 playbook。
- 高权限 API 检测。
- key 生命周期治理任务。

### 场景 3：数据批量导出

训练目标：

- 数据访问日志。
- 导出审批。
- 异常行为检测。
- 隐私和法务通报判断。

产物：

- 数据导出检测。
- 数据泄露影响评估模板。
- 通报决策记录。

### 场景 4：CI/CD 供应链异常

训练目标：

- CI/CD secret 访问。
- workflow 变更。
- artifact 替换。
- 发布审批。

产物：

- CI/CD 检测规则。
- secret 轮换流程。
- 供应链评审改进。

### 场景 5：Kubernetes 高权限滥用

训练目标：

- Kubernetes audit log。
- RBAC 变更。
- privileged workload。
- secret 访问。
- network policy。

产物：

- K8s 高风险操作检测。
- RBAC 复核。
- admission policy 改进。

## 指标

- detection coverage。
- expected alerts triggered。
- missed detection count。
- time to detect。
- time to triage。
- time to contain。
- playbook executable rate。
- evidence completeness。
- repeated gap count。

## 常见误区

- 没有授权范围就开始演练。
- 只追求红队突破，不沉淀蓝队检测。
- 只写报告，不验证修复。
- 只演练技术团队，不拉上法务、隐私、业务和管理层。
- 只看 ATT&CK 映射数量，不看真实可响应能力。

## 官方框架入口

- MITRE ATT&CK：<https://attack.mitre.org/>
- MITRE D3FEND：<https://d3fend.mitre.org/>
- CISA Incident and Vulnerability Response Playbooks：<https://www.cisa.gov/news-events/news/incident-and-vulnerability-response-playbooks>
- NIST SP 800-61：<https://www.nist.gov/publications/computer-security-incident-handling-guide>

## 关联

- [[../06-Maps/红队蓝队紫队演练闭环图|红队蓝队紫队演练闭环图]]
- [[./安全实战实验室路线 Playbook|安全实战实验室路线 Playbook]]
- [[./SOC 检测工程 Playbook|SOC 检测工程 Playbook]]
- [[./安全事件响应 Playbook|安全事件响应 Playbook]]
- [[../07-Templates/安全演练计划模板|安全演练计划模板]]
- [[../07-Templates/检测覆盖矩阵模板|检测覆盖矩阵模板]]
