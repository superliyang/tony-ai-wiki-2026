---
title: 第 2 章实操：PyTorch MPS 最小训练实验
status: learning
created: 2026-03-27
updated: 2026-03-27
---

# 第 2 章实操：PyTorch MPS 最小训练实验

## 本章目标

把 `PyTorch MPS` 从“能检测到”推进到“真的做一次训练”。

## 为什么这一步关键

很多人会停在：

- `torch.backends.mps.is_available()` 返回 `True`

但真正的能力分界线在于：

- 你有没有真的跑一个训练循环
- 你能不能解释 `CPU` 和 `MPS` 的行为差异
- 你能不能识别 fallback、batch、数据尺寸对结果的影响

## 实验目标

完成一个最小可解释训练实验，推荐从最简单的文本分类或小型 MLP 开始。

## 最小脚本骨架

```python
import torch
import torch.nn as nn
import torch.optim as optim

DEVICE = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')

x = torch.randn(1024, 128, device=DEVICE)
y = torch.randint(0, 4, (1024,), device=DEVICE)

model = nn.Sequential(
    nn.Linear(128, 256),
    nn.ReLU(),
    nn.Linear(256, 4),
).to(DEVICE)

criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=1e-3)

for step in range(50):
    optimizer.zero_grad()
    logits = model(x)
    loss = criterion(logits, y)
    loss.backward()
    optimizer.step()
    if step % 10 == 0:
        print(step, loss.item())
```

## 你要记录的东西

- `torch` 版本
- `mps` 是否可用
- batch size
- step time
- loss 是否正常下降
- 是否遇到 fallback 或不支持的算子

## 对比实验

### 实验 A：`CPU` vs `MPS`

同一份脚本，分别在 `cpu` 和 `mps` 上跑。

记录：

- 单 step 时间
- 总训练时间
- 是否有明显兼容性差异

### 实验 B：batch size 对比

测试至少三个 batch size。

观察：

- 速度变化
- 内存压力
- 稳定性

### 实验 C：简单文本任务

如果你已经熟一点，可以把玩具张量替换成一个最小文本任务，重点是：

- tokenizer
- padding
- loss
- sequence length

## 你会学到什么

完成这一步后，你应该开始有这些直觉：

- `MPS` 很适合建立训练经验
- `MPS` 不是 `CUDA` 的一比一替代
- 你必须主动管理实验规模
- 模型“能跑”不代表实验“可解释”

## 本章输出物

- 一个 `scripts/train_mps_baseline.py`
- 一张 `CPU vs MPS` 对比表
- 一份 batch size 观察记录
- 一份 fallback / 限制清单

## 遇到问题时先查哪里

- [Apple: Accelerated PyTorch training on Mac](https://developer.apple.com/metal/pytorch/)
- [PyTorch: MPS backend](https://docs.pytorch.org/docs/stable/notes/mps.html)

## 下一步

- [[第 3 章：MLX 与 Apple Silicon 原生实验]]
- [[第 3 章实操：MLX-LM 原生推理与最小 LoRA 实验]]
