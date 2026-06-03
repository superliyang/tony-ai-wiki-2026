---
title: 第 0 章实操：把 Mac 变成 AI 实验室
status: learning
created: 2026-03-27
updated: 2026-03-27
---

# 第 0 章实操：把 Mac 变成 AI 实验室

## 本章目标

我们这一步不追求花哨，只追求把 `MacBook Pro Max M4` 变成一个稳定、可重复、适合长期实验的本地 AI 工作台。

## 你要达成的通过标准

完成后你应该能确认：

- `Xcode command line tools` 已就绪
- 一个干净的 Python 环境可以长期复用
- `PyTorch` 可以看到 `mps`
- `Ollama` 可以正常跑一个模型
- `MLX-LM` 可以完成一次最小生成
- 你已经建好自己的实验目录结构

## 推荐目录

建议你在本机固定一个主目录，比如：

```text
~/dev/mac-ai-lab/
├── notebooks/
├── scripts/
├── datasets/
├── artifacts/
├── apps/
└── docs/
```

这个目录以后会一直陪你走完整条学习路径。

## 步骤 1：准备系统基础

### 1. 安装或确认 Xcode command line tools

官方要求里，Apple 的 Metal + PyTorch 路线明确把 `xcode-select --install` 作为基础前置条件。

你可以执行：

```bash
xcode-select --install
```

### 2. 确认 macOS 与硬件前提

官方资料里对 Apple silicon 路线的要求大致是：

- Apple silicon Mac
- 足够新的 macOS
- 可用的命令行开发工具

你已经有 `MacBook Pro Max M4`，这一步重点不是“能不能跑”，而是确认系统工具链没有缺口。

## 步骤 2：建一个干净的 Python 环境

推荐先用最普通也最稳定的方式：

```bash
mkdir -p ~/dev/mac-ai-lab
cd ~/dev/mac-ai-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
```

如果你后面更喜欢 `uv`，可以再切；但入门阶段先别把环境管理搞复杂。

## 步骤 3：安装 PyTorch 并验证 MPS

这里我建议你遵循官方安装选择器，不死记某一条历史命令。

参考：

- [Apple: Accelerated PyTorch training on Mac](https://developer.apple.com/metal/pytorch/)
- [PyTorch: MPS backend](https://docs.pytorch.org/docs/stable/notes/mps.html)

验证代码：

```python
import torch
print(torch.__version__)
print(torch.backends.mps.is_available())
print(torch.backends.mps.is_built())
```

你理想上希望看到：

- `is_built() == True`
- `is_available() == True`

## 步骤 4：安装 Ollama 并跑通第一个模型

官方 macOS 文档当前强调：

- macOS Sonoma 或更新
- Apple M 系列支持 CPU + GPU
- 推荐安装方式是 `.dmg` 拖到 `Applications`

参考：

- [Ollama macOS](https://docs.ollama.com/macos)
- [Ollama Quickstart](https://docs.ollama.com/quickstart)

装完后，你的最小目标不是“调很多模型”，而是只跑通一个。

你可以做的验证：

```bash
ollama
```

或者直接跑一个你选定的小模型。

记录这些观察：

- 首次下载耗时
- CLI 是否可用
- 默认模型存储位置
- 交互体验是否顺畅

## 步骤 5：安装 MLX / MLX-LM

官方入口：

- [MLX](https://github.com/ml-explore/mlx)
- [MLX-LM](https://github.com/ml-explore/mlx-lm)

最小安装：

```bash
pip install mlx
pip install mlx-lm
```

这一步最重要的不是“性能神话”，而是开始进入 Apple silicon 原生实验路线。

## 步骤 6：建立最小验证脚本

至少准备三个文件：

- `scripts/check_mps.py`
- `scripts/check_ollama.md` 或你的命令记录
- `scripts/check_mlx_lm.py`

这样你以后切换环境或更新依赖时，可以快速回归验证。

## 你应该保存的实验记录

建议在 `docs/` 或 Obsidian 里记下：

- 安装日期
- Python 版本
- `torch` 版本
- `mlx` / `mlx-lm` 版本
- Ollama 版本
- 是否遇到路径、权限、模型缓存、内存问题

## 常见坑

- 只安装，不验证
- 工具都装在不同 Python 环境里
- 没有记录版本，后面复现不了
- 一开始就想跑太大的模型，把本地实验室搞得很不稳定

## 本章交付物

完成这一页后，你应该至少有：

- 一个长期可用的 `mac-ai-lab` 目录
- 一个可激活的 Python 环境
- 一次成功的 `mps` 验证
- 一次成功的 `Ollama` 运行
- 一次成功的 `MLX-LM` 最小生成

## 下一步

- [[第 1 章实操：本地推理对比实验]]
- [[第 1 章：本地推理与模型运行]]
