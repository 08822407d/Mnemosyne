# PDF Figure Review Index / PDF 图表与图片人工复核索引

## 文件定位

本文件用于登记 `RC-2026Q2-initial` 中 PDF 图表 / 图片 / 版式证据的人工复核状态。

- 本文件不是执行源；
- 本文件不是 OCR 输出；
- 当前尚未完成人工图表复核；
- 本文件不声称任何 PDF 图表 / 图片 / 版式内容已经被复核；
- 对 PDF 图表 / 图片的任何设计依赖，都必须先通过本索引登记复核结果；
- 当前执行源仍是 `current/human-approved-spec.md`。

## 复核状态表

| report_id | source_file | figure_or_page_ref | suspected_content_type | design_dependency | review_status | reviewer | review_date | extracted_claim | confidence | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| RPT-2026Q2-0002 | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 1：非开发长期对话记忆是否已有真实实践.pdf` | unknown_pending_manual_inspection | PDF 图表 / 图片 / 版式 / 引用编号 | 非开发长期对话记忆实践、产品案例与场景成熟度判断 | pending_manual_review | TBD | TBD | TBD | TBD | 摘要仅基于可读取文本；图表 / 图片 / 版式未复核。 |
| RPT-2026Q2-0003 | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 2：ChatGPT,Claude 纯对话场景的外部记忆能力边界.pdf` | unknown_pending_manual_inspection | PDF 图表 / 图片 / 版式 / 引用编号 | 纯对话入口能力边界、读写外部记忆限制、工具授权判断 | pending_manual_review | TBD | TBD | TBD | TBD | 摘要仅基于可读取文本；图表 / 图片 / 版式未复核。 |
| RPT-2026Q2-0004 | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 3：Codex,Claude Code,Cursor 等本地开发 Agent 的文件式记忆能力.pdf` | unknown_pending_manual_inspection | PDF 图表 / 图片 / 版式 / 引用编号 | 本地开发 Agent 文件式记忆能力、工具差异与治理建议 | pending_manual_review | TBD | TBD | TBD | TBD | 摘要仅基于可读取文本；图表 / 图片 / 版式未复核。 |
| RPT-2026Q2-0005 | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 4：云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计.pdf` | unknown_pending_manual_inspection | PDF 图表 / 图片 / 版式 / 引用编号 | 云端 Coding Agent、GitHub workflow、PR / review / 权限审计判断 | pending_manual_review | TBD | TBD | TBD | TBD | 摘要仅基于可读取文本；图表 / 图片 / 版式未复核。 |
| RPT-2026Q2-0006 | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 5：外部持久记忆的理论与工程依据.pdf` | unknown_pending_manual_inspection | PDF 图表 / 图片 / 版式 / 引用编号 | 外部持久记忆理论、RAG、事件源、checkpoint、隐私与合规风险判断 | pending_manual_review | TBD | TBD | TBD | TBD | 摘要仅基于可读取文本；图表 / 图片 / 版式未复核。 |
| RPT-2026Q2-0007 | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 6：开发场景的持久记忆经验能否迁移到普通长期对话和学习场景.pdf` | unknown_pending_manual_inspection | PDF 图表 / 图片 / 版式 / 引用编号 | 开发经验向普通对话、学习、源码学习和研究场景迁移判断 | pending_manual_review | TBD | TBD | TBD | TBD | 摘要仅基于可读取文本；图表 / 图片 / 版式未复核。 |

## 使用规则

- 若目标项目设计、capability boundaries、Evidence Item 或 delta report 需要依赖 PDF 图表 / 图片 / 版式证据，应先在本表补充具体 `figure_or_page_ref`、复核人、复核日期、提取结论和置信度。
- 未完成 `pending_manual_review` 的图表 / 图片 / 版式内容不得写成已验证设计证据。
- 如果人工复核发现摘要与 PDF 原件不一致，应更新对应 summary 的 `open questions / review notes`，并登记后续修正任务。
