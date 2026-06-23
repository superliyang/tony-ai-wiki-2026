# Memory、Planning 与 Multi-Agent题库

> 这组题解决的是：当面试从“会不会调工具”继续深入到 `长期状态、任务规划、多 Agent 协作` 时，你能不能讲清楚边界和取舍，而不是只会堆 buzzword。

## Q1. Context、RAG、Memory 三者的职责边界怎么分？
- 面试官在听什么：是否理解这三层不是同义词。
- 资深回答关键词：working memory、fact retrieval、long-term state、pollution risk、control boundary。
- 典型追问：什么时候你反而不该把东西长期记住？

## Q2. 什么时候系统真的需要长期 Memory？
- 面试官在听什么：是否有克制力，不把 memory 当作默认升级方向。
- 资深回答关键词：cross-session continuity、user preference、project state、task carryover、high-value recall。
- 典型追问：如果 memory 带来的收益很弱，你会怎么做？

## Q3. Memory 污染和错误记忆怎么治理？
- 面试官在听什么：是否理解 memory 的风险不只是“记不住”，而是“记错了还长期生效”。
- 资深回答关键词：write policy、verification、expiration、scoping、user review、rollback、memory eval。
- 典型追问：共享 memory 场景下最危险的边界是什么？

## Q4. 你如何判断一个 Agent 已经需要显式 Planning，而不是简单循环？
- 面试官在听什么：是否理解 planning 的门槛和收益。
- 资深回答关键词：task decomposition、subgoal state、branching factor、recovery path、long-horizon task。
- 典型追问：什么时候 planning 会让系统更差？

## Q5. Planner、Executor、Verifier 三层怎么拆？
- 面试官在听什么：是否能把复杂 agent 结构讲成清晰分层。
- 资深回答关键词：goal decomposition、action execution、evidence check、termination rule、handoff。
- 典型追问：如果结果冲突，谁负责裁决？

## Q6. 单 Agent、Workflow、Multi-Agent 之间怎么选？
- 面试官在听什么：是否具备结构选择能力，而不是把 multi-agent 当高级默认答案。
- 资深回答关键词：coordination cost、task modularity、parallel gain、debuggability、control boundary。
- 典型追问：什么时候普通 workflow 明显优于多 Agent？

## Q7. Multi-Agent 最常见的失败模式是什么？
- 面试官在听什么：是否做过或至少想清过多 Agent 的真实代价。
- 资深回答关键词：looping、conflict、state divergence、overhead、tool contention、blame ambiguity。
- 典型追问：你怎么限制协作层数和调用深度？

## Q8. 你如何做 Memory / Planning / Multi-Agent 的评测？
- 面试官在听什么：是否知道这些能力不能只看单轮 demo。
- 资深回答关键词：long-horizon task suite、state consistency、memory precision / recall、plan completion、handoff success。
- 典型追问：如果一次任务要跑 20 分钟，eval 怎么做得可维护？

## Q9. 共享项目记忆怎么避免跨用户、跨租户污染？
- 面试官在听什么：是否理解 memory 一旦进共享层，安全和治理难度立刻上升。
- 资深回答关键词：scope boundary、tenant isolation、project namespace、approval、retention policy、audit。
- 典型追问：哪些信息你永远不会写入共享 memory？

## Q10. 如果 Multi-Agent 看起来很酷，但成本和复杂度明显上升，你怎么说服团队收缩？
- 面试官在听什么：是否有能力做减法，而不是只会扩系统。
- 资深回答关键词：measured gain、coordination overhead、failure cost、simplification、single-agent fallback、workflow substitution。
- 典型追问：如果团队已经投入很多，你怎么避免“沉没成本”绑架决策？
