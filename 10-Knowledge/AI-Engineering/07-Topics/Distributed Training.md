---
title: Distributed Training
type: topic
status: learning
tags:
  - ai/engineering
  - ai/distributed-training
created: 2026-03-13
updated: 2026-03-28
---

# Distributed Training

## 为什么它是训练工程的分水岭

一旦模型、batch、激活或优化器状态超出单卡边界，训练问题就不再只是“写对模型代码”，而变成：

- 怎么切任务
- 怎么同步状态
- 怎么让通信别拖死吞吐
- 怎么在失败后恢复

所以分布式训练是训练工程从“单机实验”走向“系统工程”的分界线。

## 它到底在解决什么

分布式训练通常同时解决三类问题：

1. **放得下**：单卡显存装不下模型或 batch
2. **跑得快**：单卡训练太慢，不能满足迭代速度
3. **跑得稳**：多机多卡协同时仍然可恢复、可调优、可复现

## 常见并行方式怎么区分

### `Data Parallel`

- 每个 worker 持有完整模型
- 不同 worker 处理不同数据切片
- 每步同步梯度

它最适合：

- 模型还能放进单卡
- 想先把训练吞吐扩起来

### `FSDP / ZeRO / Sharded Data Parallel`

- 不再让每张卡都保留完整模型状态
- 参数、梯度、优化器状态在不同 worker 间分片

它最适合：

- 模型已经接近或超过单卡显存上限
- 想在尽量保持数据并行心智的同时扩展规模

### `Tensor Parallel`

- 把单层里的张量计算切开，分散到多卡

它最适合：

- 单层计算太大
- 想突破单设备张量大小限制

### `Pipeline Parallel`

- 把模型分段，不同 stage 放在不同设备上
- microbatch 在 stage 间流动

它最适合：

- 模型层数多
- 设备可以按 stage 切分

### `Hybrid / 3D Parallel`

实际大模型训练常常不是三选一，而是组合：

- data parallel
- tensor parallel
- pipeline parallel
- sharding

## PyTorch 现在的主线怎么理解

从 `PyTorch Distributed` 的官方文档看，主干已经比较清楚：

- `DDP`：模型能放单卡时的默认扩展方式
- `FSDP2`：模型放不下单卡时的重要方案
- `Tensor Parallel` / `Pipeline Parallel`：继续扩规模时的更高阶方案
- `DTensor` / `DeviceMesh`：更底层的 sharding 和并行原语
- `torchrun`：最常见的 launcher

这套结构说明：分布式训练已经从“一个技巧”变成了完整栈。

## 真正难的地方在哪

### 1. 通信不是附属问题

扩卡后常见问题不是算得不够快，而是：

- all-reduce 太重
- stage 间等待太长
- 网络拓扑不友好
- overlap 做得不够

### 2. 显存问题不只来自参数

显存主要被几类东西吃掉：

- 参数
- 梯度
- optimizer states
- activations
- KV / temporary buffers

很多团队只盯参数大小，会低估 activations 和 optimizer 的压力。

### 3. checkpoint 是系统能力

模型越大，checkpoint 越不是“顺手保存一下”，而是：

- I/O 设计问题
- 恢复时间问题
- 容错问题
- 多并行策略一致性问题

## 一条更实用的调优顺序

1. 先看单卡 baseline 是否健康
2. 再看 dataloader 和 input pipeline 是否稳定
3. 再扩到 data parallel
4. 当显存不够时，再引入 sharding / FSDP / ZeRO
5. 当扩卡效率仍不够，再考虑 tensor / pipeline parallel
6. 最后再做更细的 overlap、kernel、microbatch 调参

## 你应该重点观察哪些指标

- step time
- samples / tokens per second
- GPU utilization
- communication time ratio
- memory peak
- checkpoint save / restore time
- 扩卡效率

## 典型失败模式

- 数据管道太慢，导致误以为并行策略有问题
- 扩卡后吞吐不上升，通信占比却飙升
- pipeline stage 不均衡，导致气泡严重
- checkpoint 太慢，训练恢复代价太大
- 混合了多种并行后，调试和复现成本暴涨

## 学习这页时最该记住什么

- 分布式训练不是“多加几张卡”
- 真正的工程能力在于：吞吐、容错、可恢复、可扩展和调优纪律

## 推荐怎么往下读

1. [[Infrastructure (GPU-TPU)]]
2. [[Training Stack Overview]]
3. [[Inference Optimization]]
4. [[../03-Training/DeepSpeed|DeepSpeed]]
5. [[../03-Training/FSDP|FSDP]]
6. [[../03-Training/Megatron-LM|Megatron-LM]]

## 相关主题

- [[Infrastructure (GPU-TPU)]]
- [[Training Stack Overview]]
- [[Inference Optimization]]
- [[Experiment Tracking]]

## 相关实体

- [[../03-Training/DeepSpeed|DeepSpeed]]
- [[../03-Training/Megatron-LM|Megatron-LM]]
- [[../03-Training/FSDP|FSDP]]

## 资料

- [PyTorch Distributed Overview](https://docs.pytorch.org/tutorials/beginner/dist_overview.html)
- [torch.distributed](https://docs.pytorch.org/docs/stable/distributed)
- [DeepSpeed Training Overview](https://www.deepspeed.ai/training/)
