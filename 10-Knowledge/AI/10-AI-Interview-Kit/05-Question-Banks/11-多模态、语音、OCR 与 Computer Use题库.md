# 多模态、语音、OCR 与 Computer Use题库

> 这组题解决的是：当面试不再停留在纯文本 LLM，而是进入 `voice / realtime / document AI / browser & computer use` 这些新表面时，你能不能依然讲得像做过系统的人。

## Q1. 做多模态系统时，你怎么判断该上单一 multimodal model，还是文本模型 + 专项组件拼装？
- 面试官在听什么：是否理解“模型能力强”不等于“系统就该一体化”。
- 资深回答关键词：task decomposition、成本、延迟、可解释性、可观测性、OCR/ASR 专项组件、fallback path。
- 典型追问：什么时候你宁愿牺牲端到端优雅，也要保留分层方案？

## Q2. 设计一个 Voice / Realtime assistant，你优先盯哪些链路？
- 面试官在听什么：是否理解实时语音系统不是普通 chat 套一层 TTS。
- 资深回答关键词：ASR / VAD、turn-taking、interruption handling、streaming、TTFT、barge-in、latency budget、fallback。
- 典型追问：用户打断时，状态和上下文怎么处理？

## Q3. OCR / Document AI 系统怎么做，才能不只是“看起来能抽取”？
- 面试官在听什么：是否理解 document AI 的核心是验证链，而不是单次抽取得像。
- 资深回答关键词：layout、field schema、evidence span、confidence、HITL、audit trail、post-extraction validation。
- 典型追问：模型抽错字段后，你怎么快速定位是 OCR、layout 还是抽取逻辑的问题？

## Q4. Computer Use / Browser Agent 最危险的风险边界是什么？
- 面试官在听什么：是否能把 computer use 从“模型会操作界面”提升到“动作与权限系统”来讲。
- 资深回答关键词：action risk、DOM / screenshot ambiguity、sandbox、approval gate、credential boundary、kill switch。
- 典型追问：为什么 computer use 的安全问题通常比普通 tool calling 更难？

## Q5. 多模态 RAG 和纯文本 RAG 的最大区别是什么？
- 面试官在听什么：是否理解文档、图片、表格、截图进入事实链路后，检索与引用会变复杂。
- 资深回答关键词：multimodal chunking、page / region grounding、evidence alignment、citation、layout-aware retrieval。
- 典型追问：如果一个答案同时依赖图表和正文，你怎么做可追溯引用？

## Q6. Voice / Realtime 体验不稳时，你先看什么指标？
- 面试官在听什么：是否能把“语音体验差”拆成系统指标，而不是泛泛说模型不够好。
- 资深回答关键词：ASR WER、TTFT、turn latency、interrupt success rate、handoff rate、session drop、tool latency。
- 典型追问：如果语音识别准确率不错，但用户仍觉得卡顿，你下一步查什么？

## Q7. 文档 AI / 合同抽取上线时，为什么往往必须保留人工复核？
- 面试官在听什么：是否理解高价值文档工作流里的责任边界。
- 资深回答关键词：field criticality、confidence threshold、exception queue、sampling、review surface、evidence span。
- 典型追问：哪些字段你会允许自动过，哪些字段必须 HITL？

## Q8. Computer Use Agent 怎么做评测，避免“demo 很酷，线上很脆”？
- 面试官在听什么：是否理解 UI 自动化 / browser agent 的评测难点。
- 资深回答关键词：task suite、environment drift、step success、end-to-end completion、replay、rollback、human takeover。
- 典型追问：页面结构经常变，eval 集怎么维护才有用？

## Q9. 什么时候你反而不建议上 multimodal / voice / computer use？
- 面试官在听什么：是否有克制力，而不是把新能力当成默认升级方向。
- 资深回答关键词：ROI、error cost、compliance、debuggability、workflow fit、simpler alternative。
- 典型追问：如果业务很兴奋，但你判断暂时不该上，你怎么说服对方？

## Q10. 多模态供应商 / 模型怎么选，才不只是看 demo 效果？
- 面试官在听什么：是否会从能力、成本、延迟、可控性和治理能力做综合判断。
- 资深回答关键词：capability fit、latency tier、cost envelope、grounding、compliance、deployment boundary、vendor lock-in。
- 典型追问：如果 voice 很强但文档差，你会统一供应商还是拆分能力栈？

## Q11. 如果让你设计一个“语音 + 文档 + 浏览器操作”的复合型 agent，你先做哪层？
- 面试官在听什么：是否能在新能力很多时保持分层，而不是一上来做巨无霸系统。
- 资深回答关键词：thin slice、workflow boundary、evidence layer、approval layer、progressive rollout、degrade plan。
- 典型追问：什么情况下你会刻意把 voice、document、computer use 拆成不同阶段上线？
