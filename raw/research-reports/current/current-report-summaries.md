# Current Report Summaries / 当前研究报告摘要索引（派生视图）

## 文件定位

本文件是 current 派生视图，用于索引当前激活研究轮次的 summary 文件。

- active_cycles: RC-2026Q2-initial; RC-2026Q2-memory-testing; RC-2026Q2-handoff-strategy; RC-2026Q2-user-input-governance; RC-2026Q2-first-target-dry-run-evaluation; RC-2026Q3-platform-context-apps-delta
- 本文件不是执行源；
- 当前执行源仍是 `current/human-approved-spec.md`；
- 原始报告位于各 cycle 的 `originals/` 目录；
- PDF 图表 / 图片复核状态见 `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`；
- 如 summary 与原始报告冲突，应以原始报告为证据来源；如 summary 与 `current/human-approved-spec.md` 冲突，应以执行源为准。
- 对 DR6，先读 maintainer review；原始报告中的 Deep Research turn-citation markers 可能无法在 GitHub 中直接解析。

## 推荐读取顺序

- 先读相关 cycle 的 `research-cycle-origin-and-motivation.md`。
- 再读本文件和各 report summary。
- 再按需回查原始报告。
- 若设计依赖 PDF 图表 / 图片 / 版式，应先查看 figure review index。
- 对 2026Q3 平台事实，操作前仍需重新核验最新官方文档和实际账户/surface 配置。

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
| RPT-2026Q2-MT-0001 | AI Agent external persistent memory system testing/debugging/evaluation/failure diagnosis | `raw/research-reports/cycles/2026Q2-memory-testing/report-summaries/DR1_memory_testing_debugging_evidence_review_summary.md` | `raw/research-reports/cycles/2026Q2-memory-testing/originals/DR1_memory_testing_debugging_evidence_review_report.md` | completed_from_markdown_report | not_applicable_markdown | yes | Supplemental current evidence; no unified mature memory-specific testing standard, but reusable evaluation/debugging practices exist. |
| RPT-2026Q2-HO-0001 | Mnemosyne handoff package strategy and quantitative evaluation | `raw/research-reports/cycles/2026Q2-handoff-strategy/report-summaries/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_summary.md` | `raw/research-reports/cycles/2026Q2-handoff-strategy/originals/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_report.md` | completed_from_markdown_report | not_applicable_markdown | yes | Correct handoff, replay scoring, package tiering and provenance evidence. |
| RPT-2026Q2-UIG-0001 | User-input governance | `raw/research-reports/cycles/2026Q2-user-input-governance/report-summaries/DR4_user_originals_requirements_redaction_governance_summary.md` | `raw/research-reports/cycles/2026Q2-user-input-governance/originals/DR4_user_originals_requirements_redaction_governance_report.md` | completed_from_markdown_report | not_applicable_markdown | yes | Originals/redaction/pointers/Git history/repository-visibility evidence. |
| RPT-2026Q2-FTDRE-0001 | First real target-project dry-run evaluation framework | `raw/research-reports/cycles/2026Q2-first-target-dry-run-evaluation/report-summaries/DR5_first_real_target_dry_run_evaluation_framework_summary.md` | `raw/research-reports/cycles/2026Q2-first-target-dry-run-evaluation/originals/DR5_first_real_target_dry_run_evaluation_framework_report.md` | completed_from_markdown_report | not_applicable_markdown | supplemental_current_evidence | Evidence only; not execution source. |
| RPT-2026Q3-PLATFORM-DELTA-0001 | 2026Q3 Project memory / apps / GitHub / surface / provenance / no-write delta | `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/report-summaries/DR6_2026Q3_platform_memory_apps_capability_delta_summary.md` | `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/originals/DR6_2026Q3_platform_memory_apps_capability_delta_report.md` | accepted_with_corrections | not_applicable_markdown | supplemental_current_evidence | Read maintainer review first; original citation markers have limited portability. |
