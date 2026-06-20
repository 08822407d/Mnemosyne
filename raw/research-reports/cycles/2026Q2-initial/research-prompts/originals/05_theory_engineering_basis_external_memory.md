# 轻度研究子课题 5：外部持久记忆的理论与工程依据

## 研究目标

请研究：RAG、checkpoint、handoff、memory store、long-context limitation、MemGPT、LangGraph、context engineering 等理论和工程实践，是否支持“模型像 CPU、外部文件像硬盘”的 AI 外部持久记忆架构。

本研究重点是理论和工程依据，不研究具体产品操作路径。

## 背景

我构想的外部持久记忆系统认为：

- 模型不应被当作唯一长期记忆；
- 当前对话上下文像 RAM，适合短期工作；
- 外部文件、数据库、Git 仓库像硬盘，保存长期状态；
- handoff、checkpoint、summary 是恢复点；
- RAG 和索引用于按需加载；
- 原文归档用于未来复核和重新评估；
- 滚动缓冲区用于短片段积累后阶段性评估。

我希望知道这些想法是否有理论和工程实践支持。

## 核心问题

1. 长上下文是否能替代外部持久记忆？如果不能，为什么？
2. lost-in-the-middle、上下文成本、延迟、注意力分散等问题是否支持外部记忆设计？
3. RAG 和 retrieval 是否支持“按需加载相关记忆，而不是加载全部历史”？
4. checkpoint、handoff、summary、compaction 是否是长任务 agent 的成熟做法？
5. MemGPT 是否支持“模型外部记忆 / 分层内存”的思想？
6. LangGraph persistence、memory、checkpoint 是否支持“可恢复状态”？
7. 滚动缓冲区加阶段性评估是否符合 event sourcing、compaction、learning records 或 agent memory 思路？
8. 完整原文归档作为 future re-evaluation evidence 是否有工程或研究依据？
9. 记忆系统自身规则外部化，是否对应 policy as code、instructions as code、rules as files 等成熟思想？

## 请优先查找的资料

- MemGPT 论文和项目；
- LangGraph memory、persistence、checkpoint 官方文档；
- RAG / retrieval 官方或经典资料；
- context engineering 资料；
- long-context limitations、lost-in-the-middle 相关研究；
- agent memory、conversation summary、compaction、checkpointing 相关论文；
- event sourcing、artifact registry、audit log 与 AI agent 结合的资料；
- OpenAI / Anthropic 关于 context management 和 agent memory 的官方工程建议。

## 输出要求

请输出：

1. 总体结论：该架构是否有理论和工程依据。
2. 长上下文为什么不能完全替代外部记忆。
3. RAG / retrieval 对该构想的支持点。
4. checkpoint / handoff / compaction 对该构想的支持点。
5. MemGPT / LangGraph 对该构想的支持点。
6. 滚动缓冲区和阶段性评估的合理性。
7. 原文归档的价值与风险。
8. 哪些部分是成熟实践，哪些仍偏实验性。
9. 对后续具体方案设计的参考要点。

## 注意事项

不要设计完整产品。重点是证明或反驳这些机制的理论与工程依据。不要使用未来预测作为可行性依据。
