---
title: Infrastructure (GPU-TPU)
type: topic
status: learning
tags:
  - ai/engineering
  - ai/infrastructure
created: 2026-03-13
updated: 2026-03-28
---

# Infrastructure (GPU-TPU)

## 为什么它是训练工程的物理边界

大模型工程首先受限于：

- accelerator 性能与显存
- 网络带宽与拓扑
- 存储吞吐
- checkpoint 恢复速度
- 调度稳定性与资源可得性

所以基础设施不是背景条件，而是训练系统的物理边界。

## 用系统眼光看基础设施，至少要拆成 4 层

### 1. Accelerator layer

- GPU / TPU / CPU 协同
- 单卡算力
- 显存容量
- 卡间互联
- mixed precision 支持

### 2. Node and host layer

- host CPU、NUMA、PCIe
- 本地 NVMe / scratch
- dataloader 与 host-to-device 传输
- failure detection 与 local recovery

### 3. Cluster substrate

- RDMA / InfiniBand / ICI / NVLink / NVSwitch
- 对象存储 / 文件系统
- scheduler / quota / gang scheduling
- checkpoint / restore path

### 4. AI-native cloud layer

- reservation / capacity planning
- 多 tenant 与 cost control
- 训练 / 推理一体化 lifecycle
- 托管平台与可观测性

## GPU 与 TPU 不要只看芯片名字

真正的工程判断通常是：

- 软件栈成熟度
- 运维经验
- 生态兼容性
- 性能可预测性
- 调度与恢复能力
- 团队是否已经掌握对应编译与运行时

### GPU 路线通常更适合

- 需要最大化生态兼容性
- 训练框架与开源工具链主要围绕 CUDA
- 既做训练又做推理，希望工具复用

### TPU 路线通常更适合

- 团队已经接受 XLA / JAX / PyTorch/XLA 心智
- 更强调大规模矩阵计算与 pod 级系统效率
- 可以围绕 slice / multislice 做系统级调优

## 真正会把训练拖垮的 infra 问题

### 1. GPU 利用率低，但不是模型问题

常见成因：

- dataloader 太慢
- host 预处理阻塞
- 小 batch / packing 不合理
- checkpoint 频率过高

### 2. 扩卡后吞吐不升反降

常见成因：

- all-reduce / all-gather 占比过高
- topology 不匹配并行策略
- microbatch 太小，通信摊销不了
- 网络或存储抖动导致 straggler

### 3. 集群可得性不足

这往往不是“纯成本问题”，而会反过来影响：

- 实验节奏
- 迭代速度
- 训练计划可信度
- post-training 排期

## 训练团队真正要形成的基础设施判断力

### 判断 1：问题是 accelerator 不够，还是系统 feeding 不够

如果 GPU utilization 低，先问：

- 数据有没有及时喂上来
- host 是否成为 bottleneck
- 通信和 checkpoint 是否占用了太多 wall time

### 判断 2：选型是在买芯片，还是在买系统

比如 `Cloud TPU` 不只是买 TPU 芯片，而是在买：

- pod / slice 拓扑
- host 模式
- XLA / PyTorch-XLA 路线
- 训练与调试方式

同理，GPU cloud 也不只是买卡，而是在买：

- 网络
- 存储
- 调度
- driver / runtime 稳定性

### 判断 3：infra 是否和训练阶段匹配

- pretraining：更强调大规模吞吐与稳定恢复
- post-training：更强调周转速度和多实验并行
- eval / red-team：更强调弹性资源和隔离

## 和其他页面怎么连起来看

- [[Distributed Training]]：解释计算与通信如何切
- [[Frameworks (PyTorch-JAX-TensorFlow)]]：解释 infra 怎样被框架暴露出来
- [[Experiment Tracking]]：解释 infra 故障如何映射到实验可解释性
- [[Serving and Scaling]]：解释训练 infra 与推理 infra 的分工与复用

## 相关主题

- [[Training Stack Overview]]
- [[Distributed Training]]
- [[Frameworks (PyTorch-JAX-TensorFlow)]]
- [[Experiment Tracking]]
- [[Serving and Scaling]]
- [[Cost, Latency, and Safety Tradeoffs]]

## 相关实体

- [[../02-Frameworks/PyTorch|PyTorch]]
- [[../02-Frameworks/JAX|JAX]]
- [[../03-Training/DeepSpeed|DeepSpeed]]
- [[../03-Training/FSDP|FSDP]]

## 资料

- [Cloud TPU System Architecture](https://docs.cloud.google.com/tpu/docs/system-architecture)
- [Train a Model Using TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e-intro)
- [TensorFlow Distributed Training](https://www.tensorflow.org/guide/distributed_training)
- [PyTorch Distributed Overview](https://docs.pytorch.org/tutorials/distributed.html)
