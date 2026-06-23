---
title: PyTorch MPS 实战
type: topic
status: learning
created: 2026-03-26
updated: 2026-03-26
---

# PyTorch MPS 实战

## 为什么这页重要

如果你想用 `Mac M4 Max` 真正学训练和 fine-tuning，`PyTorch + MPS` 是最自然的一条通道。

## 你应该掌握的 4 件事

### 1. 如何确认 `mps` 可用

- `torch.backends.mps.is_available()`
- 明白环境要求：Apple silicon、对应 macOS、Xcode command line tools

### 2. fallback 是正常现象

在 Apple silicon 上做训练，不能假设所有 op 都完美支持。

所以你要理解：

- `PYTORCH_ENABLE_MPS_FALLBACK=1`
- 为什么 fallback 会影响性能和可预期性

### 3. Trainer 能跑，不等于全链路最优

`PyTorch` 路线非常适合：

- 学 transformer training
- 学 fine-tuning
- 学 datasets / dataloaders / optimizers

### 4. 它是专家路径的一部分，不是全部

- 本地先用 `PyTorch MPS` 学清训练逻辑
- 再学 `MLX` 理解 Apple 原生栈
- 最后学云上训练和 serving

## 资料

- [PyTorch MPS backend](https://docs.pytorch.org/docs/stable/notes/mps.html)
- [Apple Accelerated PyTorch on Mac](https://developer.apple.com/metal/pytorch/)
- [Transformers: Apple Silicon training](https://huggingface.co/docs/transformers/perf_train_special)
