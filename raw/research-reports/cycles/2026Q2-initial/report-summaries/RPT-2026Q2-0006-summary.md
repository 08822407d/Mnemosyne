# Report Summary: RPT-2026Q2-0006

## 文件定位

- 本文件是研究报告摘要，不是原始报告；
- 本文件不是执行源；
- 当前执行源仍是 `current/human-approved-spec.md`；
- 如果本摘要与原始报告冲突，应以原始报告为证据来源，并登记 review note；
- 如果本摘要与 `human-approved-spec` 冲突，应以 `human-approved-spec` 为执行准则。

## 元数据

- report_id: RPT-2026Q2-0006
- source_file: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 5：外部持久记忆的理论与工程依据.pdf
- cycle_id: RC-2026Q2-initial
- report_type: light
- topic: 外部持久记忆的理论与工程依据
- readability: PDF 文本可抽取；摘要仅基于可读取文本，图表 / 图片 / 版式未复核。
- summary_status: completed_from_readable_pdf_text
- figure_review_status: pending_manual_review
- created_by_task: MNEMOSYNE-030

## 摘要

本报告为外部持久记忆提供理论和工程依据。它将 RAG、事件源、检查点、上下文压缩、MemGPT / LangGraph 式分层记忆、外部知识持久化、安全审计与 policy-as-code 等机制放在同一框架中理解：模型内部上下文适合短期计算，长期状态应存储在可检索、可审计、可恢复的外部介质中。报告同时指出完整原文归档有审计价值，也会带来隐私、合规和法律发现风险，因此应采用最小保留、加密、访问控制和明确用途。

## 关键结论

- 外部持久记忆有充分理论与工程依据，尤其是 RAG、事件日志、checkpoint、compaction 和分层存储。
- 长上下文不能替代结构化外部记忆；上下文过长会带来成本、漂移和信息利用不稳定。
- 完整原文归档可支持审计和复盘，但必须处理隐私、合规和最小化保留。
- 关键结论和决策理由应写入结构化外部存储，而不是只留在模型上下文。

## 对 Mnemosyne 设计的影响

强力支撑 Mnemosyne 的核心原则：模型负责计算，文件负责记忆；raw / summary / candidate / decision / handoff / task result 分层存储。

## 对能力边界的影响

RAG、MCP、自动索引和自动查重属于后续增强；当前可先用 Markdown/Git 建立可审计结构。

## 对目标项目模板 / delivery manifest 的影响

目标项目模板应包含外部记忆层、状态检查点、summary、handoff、隐私字段和审计记录；delivery manifest 应记录保存原文与否。

## 风险与限制

- PDF 图表 / 图片 / 版式未复核。
- 理论机制不等于当前仓库已实现自动化。
- 原文归档可能引入敏感数据和法律风险。

## 需要人工复核的内容

图表 / 图片 / 版式相关内容仍需人工复核；若后续设计依赖记忆层级图、RAG 流程图或法律风险案例，应先复核。

## 可引用锚点

- 总体结论
- 分层存储与检索
- 状态检查点与事件日志
- 上下文压缩
- 原文归档价值与风险
- 方案设计参考要点

## open questions / review notes

- 本摘要需要用户 review。
- 本摘要不得直接升级为执行源或最终规范。
- 如后续目标项目设计依赖本报告中的具体产品能力、表格、图示、图片或引用编号，应回查原始报告；PDF 报告还必须先完成人工图表 / 图片 / 版式复核。
