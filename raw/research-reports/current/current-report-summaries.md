# Current Report Summaries / 当前研究报告摘要索引（派生视图）

## 文件定位

本文件是 current 派生视图，用于索引当前激活研究轮次的 summary 文件。

- active_cycle: RC-2026Q2-initial
- 本文件不是执行源；
- 当前执行源仍是 `current/human-approved-spec.md`；
- 原始报告仍位于 `raw/research-reports/cycles/2026Q2-initial/originals/`；
- PDF 图表 / 图片复核状态见 `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`；
- 如 summary 与原始报告冲突，应以原始报告为证据来源；如 summary 与 `current/human-approved-spec.md` 冲突，应以执行源为准。


## 推荐读取顺序

- 先读 `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`，理解 7 份报告为什么存在、服务什么设计问题，以及为什么研究报告是高权重证据层但不是执行源。
- 再读本文件和各 report summary，获得当前激活研究轮次的摘要入口。
- 再按需回查 `raw/research-reports/cycles/2026Q2-initial/originals/` 中的原始报告。
- 若设计依赖 PDF 图表 / 图片 / 版式，应先查看 `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`，不要把未复核图表当作已验证证据。


## 相关研究输入与读取顺序

- research motivation: `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
- current research prompts: `raw/research-reports/current/current-research-prompts.md`
- prompt index: `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
- report-topic map: `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`

建议读取顺序：

1. 先读 research motivation，理解这轮研究为什么存在；
2. 按需读 current-research-prompts，理解研究输入 / prompt 可用性；
3. 再读 current-report-summaries，理解研究结果摘要；
4. 最后按需回查原始报告。

注意：summary 是研究结果摘要，prompt 是研究输入，两者不同。MNEMOSYNE-038 已恢复 6 个轻度研究 prompt 原文；prompts 不替代 report summaries 或研究结论。


## Summary Index

| report_id | topic | summary_file | source_file | summary_status | figure_review_status | active_evidence | notes |
|---|---|---|---|---|---|---|---|
| RPT-2026Q2-0001 | AI agent 长期记忆系统综合深度研究 | `raw/research-reports/cycles/2026Q2-initial/report-summaries/RPT-2026Q2-0001-summary.md` | `raw/research-reports/cycles/2026Q2-initial/originals/AI agent 长期记忆系统 pro深度研究.txt` | completed_from_readable_txt | not_applicable_txt | yes | 综合深度研究；建议用户抽样核对关键结论。 |
| RPT-2026Q2-0002 | 非开发长期对话记忆是否已有真实实践 | `raw/research-reports/cycles/2026Q2-initial/report-summaries/RPT-2026Q2-0002-summary.md` | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 1：非开发长期对话记忆是否已有真实实践.pdf` | completed_from_readable_pdf_text | pending_manual_review | yes | 摘要仅基于可读取文本；图表 / 图片 / 版式仍待人工复核。 |
| RPT-2026Q2-0003 | ChatGPT / Claude 纯对话场景的外部记忆能力边界 | `raw/research-reports/cycles/2026Q2-initial/report-summaries/RPT-2026Q2-0003-summary.md` | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 2：ChatGPT,Claude 纯对话场景的外部记忆能力边界.pdf` | completed_from_readable_pdf_text | pending_manual_review | yes | 摘要仅基于可读取文本；图表 / 图片 / 版式仍待人工复核。 |
| RPT-2026Q2-0004 | Codex / Claude Code / Cursor 等本地开发 Agent 的文件式记忆能力 | `raw/research-reports/cycles/2026Q2-initial/report-summaries/RPT-2026Q2-0004-summary.md` | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 3：Codex,Claude Code,Cursor 等本地开发 Agent 的文件式记忆能力.pdf` | completed_from_readable_pdf_text | pending_manual_review | yes | 摘要仅基于可读取文本；图表 / 图片 / 版式仍待人工复核。 |
| RPT-2026Q2-0005 | 云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计 | `raw/research-reports/cycles/2026Q2-initial/report-summaries/RPT-2026Q2-0005-summary.md` | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 4：云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计.pdf` | completed_from_readable_pdf_text | pending_manual_review | yes | 摘要仅基于可读取文本；图表 / 图片 / 版式仍待人工复核。 |
| RPT-2026Q2-0006 | 外部持久记忆的理论与工程依据 | `raw/research-reports/cycles/2026Q2-initial/report-summaries/RPT-2026Q2-0006-summary.md` | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 5：外部持久记忆的理论与工程依据.pdf` | completed_from_readable_pdf_text | pending_manual_review | yes | 摘要仅基于可读取文本；图表 / 图片 / 版式仍待人工复核。 |
| RPT-2026Q2-0007 | 开发场景的持久记忆经验能否迁移到普通长期对话和学习场景 | `raw/research-reports/cycles/2026Q2-initial/report-summaries/RPT-2026Q2-0007-summary.md` | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 6：开发场景的持久记忆经验能否迁移到普通长期对话和学习场景.pdf` | completed_from_readable_pdf_text | pending_manual_review | yes | 摘要仅基于可读取文本；图表 / 图片 / 版式仍待人工复核。 |
