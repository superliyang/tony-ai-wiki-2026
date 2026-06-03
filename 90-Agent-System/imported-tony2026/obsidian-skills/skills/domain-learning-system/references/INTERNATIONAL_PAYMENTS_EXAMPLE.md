# International Payments Example

This is a concrete example of how to reuse the same learning system for international payments.

## Domain Shape

```text
01-Areas/
└── International-Payments/
    ├── 00-Inbox/
    ├── 01-Foundations/
    ├── 02-Networks-and-Rails/
    ├── 03-Operations-and-Risk/
    ├── 04-Applications/
    ├── 05-Topics/
    ├── 06-Maps/
    ├── 07-Templates/
    ├── 学习进度.md
    └── 恢复笔记.md
```

## Suggested Sections

### 01-Foundations

- Money movement basics
- Correspondent banking
- Clearing vs settlement
- FX basics
- Nostro / vostro accounts

### 02-Networks-and-Rails

- SWIFT
- CHIPS
- ACH
- card networks
- RTP / instant payment rails
- CIPS
- stablecoins and onchain settlement

### 03-Operations-and-Risk

- message formats
- sanctions and AML
- fraud controls
- reconciliation
- chargebacks and disputes
- routing and fees

### 04-Applications

- cross-border ecommerce
- merchant acquiring
- remittance
- enterprise treasury
- B2B supplier payments

## Example Beginner Path

1. What is international payment infrastructure
2. Clearing vs settlement
3. SWIFT and correspondent banking
4. FX and liquidity
5. Compliance and operational risk

## Example Progress Snapshot

```markdown
current_topic: SWIFT and correspondent banking
last_completed: clearing vs settlement
next_up: nostro and vostro accounts
open_questions:
  - Why can payment messaging and settlement happen on different rails?
  - Where do compliance checks sit in the flow?
resume_note:
  Restart with the SWIFT note. Focus on the distinction between message transport,
  account relationships, and final settlement.
```
