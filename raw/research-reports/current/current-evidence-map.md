# Current Evidence Map / 当前证据映射（派生视图）

> 说明：本文件是 current 派生视图，不是原始研究报告。  
> 当前来源轮次：`RC-2026Q2-initial`；补充当前证据轮次：`RC-2026Q2-memory-testing`。  
> 详细映射见：`raw/research-reports/cycles/2026Q2-initial/evidence-map.md`。

## 当前采用的研究证据视图

- active_cycles: RC-2026Q2-initial; RC-2026Q2-memory-testing (supplemental)
- report_count: 8
- use: 约束 Mnemosyne 的能力边界判断、机制设计与平台适配假设。

## 当前重点结论（摘要）

- 保持“模型负责计算，文件负责记忆”。
- 外部文件/Git 仓库作为长期真相源。
- 普通对话窗口默认半自动，不假设自动写回。
- 本地开发 Agent / 云端工作流能力需分层声明，不可混同。
- 研究报告属于高权重证据层，不是执行源。

## 需要人工复核

- RPT-2026Q2-0002 ~ RPT-2026Q2-0007（PDF）中的图表、图片与版式相关证据。
- 若未来设计决策依赖上述图表结论，必须先完成人工复核。

## 演化说明

- future_refresh: 本文件会随新 cycle 的 evidence map 更新 current 视图。
- history_policy: 旧 cycle 不覆盖、不删除，保留可追溯历史。


## Memory-system testing/debugging DR1 evidence

- report_id: RPT-2026Q2-MT-0001
- summary: `raw/research-reports/cycles/2026Q2-memory-testing/report-summaries/DR1_memory_testing_debugging_evidence_review_summary.md`
- conclusion: No unified mature industry-standard testing framework exists specifically for AI Agent external persistent memory systems. Mature reusable sub-practices exist and should be combined.
- candidate failure taxonomy: stale handoff; wrong source priority; memory drift; memory overwrite; missing critical context; over-retention; under-retention; hallucinated memory; retrieval failure; stale tool capability assumption; implicit automation assumption; privacy leakage; inconsistent handoff vs active context; user decision not recorded or not propagated; first target-project dry-run output looks complete but cannot actually land.
- current-stage implication: evaluate state correctness, source priority, temporal correctness, decision propagation, handoff executability, and delivery landability, not only final answer correctness.
- boundary: research evidence only; not execution source and not automatic writeback authority.
