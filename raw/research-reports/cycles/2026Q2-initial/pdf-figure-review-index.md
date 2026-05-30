# PDF Figure Review Index / PDF 图表人工复核索引

## 文件定位

本文件用于登记 `RC-2026Q2-initial` 中 PDF 图表 / 图片 / 版式证据的人工复核状态。

- 本文件不是执行源；
- 本文件不是 OCR 输出；
- 当前尚未完成人工图表复核；
- 当前执行源仍是 `current/human-approved-spec.md`；
- 未复核 PDF 图表 / 图片不得作为已验证设计证据；
- 本文件不声称任何 PDF 图表 / 图片 / 版式内容已经被复核；
- 如本文件与 `current/human-approved-spec.md` 冲突，应以执行源为准，并登记 open question。

## Review Policy

- RPT-2026Q2-0002 ~ RPT-2026Q2-0007 均为 PDF。
- 当前 report summaries 仅基于可读取文本。
- PDF 图表 / 图片 / 版式 / 页码定位仍需人工复核。
- RPT-2026Q2-0001 是 TXT，不需要 PDF 图表复核。
- 6 份 PDF 当前均处于 `pending_manual_review`。
- 当前没有任何 PDF 图表 / 图片被声明为已复核。
- 后续目标项目设计、capability boundaries、Evidence Item 或 delta report 若依赖 PDF 图表 / 图片 / 版式证据，应先在本索引登记人工复核结果。

## Figure Review Table

| report_id | source_file | figure_or_page_ref | suspected_content_type | design_dependency | review_status | reviewer | review_date | extracted_claim | confidence | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| RPT-2026Q2-0002 | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 1：非开发长期对话记忆是否已有真实实践.pdf` | unknown_pending_manual_inspection | PDF figures / images / layout / tables | unknown_pending_review | pending_manual_review | not_assigned | not_reviewed | not_extracted | not_applicable_until_review | 摘要仅基于可读取文本；图表 / 图片 / 版式仍待人工复核。 |
| RPT-2026Q2-0003 | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 2：ChatGPT,Claude 纯对话场景的外部记忆能力边界.pdf` | unknown_pending_manual_inspection | PDF figures / images / layout / tables | unknown_pending_review | pending_manual_review | not_assigned | not_reviewed | not_extracted | not_applicable_until_review | 摘要仅基于可读取文本；图表 / 图片 / 版式仍待人工复核。 |
| RPT-2026Q2-0004 | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 3：Codex,Claude Code,Cursor 等本地开发 Agent 的文件式记忆能力.pdf` | unknown_pending_manual_inspection | PDF figures / images / layout / tables | unknown_pending_review | pending_manual_review | not_assigned | not_reviewed | not_extracted | not_applicable_until_review | 摘要仅基于可读取文本；图表 / 图片 / 版式仍待人工复核。 |
| RPT-2026Q2-0005 | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 4：云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计.pdf` | unknown_pending_manual_inspection | PDF figures / images / layout / tables | unknown_pending_review | pending_manual_review | not_assigned | not_reviewed | not_extracted | not_applicable_until_review | 摘要仅基于可读取文本；图表 / 图片 / 版式仍待人工复核。 |
| RPT-2026Q2-0006 | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 5：外部持久记忆的理论与工程依据.pdf` | unknown_pending_manual_inspection | PDF figures / images / layout / tables | unknown_pending_review | pending_manual_review | not_assigned | not_reviewed | not_extracted | not_applicable_until_review | 摘要仅基于可读取文本；图表 / 图片 / 版式仍待人工复核。 |
| RPT-2026Q2-0007 | `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 6：开发场景的持久记忆经验能否迁移到普通长期对话和学习场景.pdf` | unknown_pending_manual_inspection | PDF figures / images / layout / tables | unknown_pending_review | pending_manual_review | not_assigned | not_reviewed | not_extracted | not_applicable_until_review | 摘要仅基于可读取文本；图表 / 图片 / 版式仍待人工复核。 |

## 当前汇总

- RPT-2026Q2-0001 是 TXT，不需要 PDF 图表复核。
- RPT-2026Q2-0002 ~ RPT-2026Q2-0007 这 6 份 PDF 均处于 `pending_manual_review`。
- 当前没有任何 PDF 图表 / 图片被声明为已复核。

## 使用规则

- 若目标项目设计、capability boundaries、Evidence Item 或 delta report 需要依赖 PDF 图表 / 图片 / 版式证据，应先补充具体 `figure_or_page_ref`、复核人、复核日期、提取结论和置信度。
- 未完成 `pending_manual_review` 的图表 / 图片 / 版式内容不得写成已验证设计证据。
- 如果人工复核发现 summary 与 PDF 原件不一致，应更新对应 summary 的 open questions / review notes，并登记后续修正任务。
