# Current Report Summaries / 当前研究报告摘要索引（派生视图）

## 文件定位

本文件是 current 派生视图，用于索引当前激活研究轮次的 summary 文件。

- active_cycles: RC-2026Q2-initial; RC-2026Q2-memory-testing (supplemental); RC-2026Q2-handoff-strategy (supplemental); RC-2026Q2-user-input-governance (supplemental); RC-2026Q2-first-target-dry-run-evaluation (supplemental); RC-2026Q3-platform-context-apps-delta (supplemental)
- 本文件不是执行源；
- 当前执行源仍是 `current/human-approved-spec.md`；
- 原始报告位于各 cycle 的 `originals/` 目录；
- PDF 图表 / 图片复核状态见 `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`；
- 如 summary 与原始报告冲突，应以原始报告为证据来源；如 summary 与 `current/human-approved-spec.md` 冲突，应以执行源为准。
- 对 DR6，先读 maintainer review；原始报告中的 Deep Research turn-citation markers 可能无法在 GitHub 中直接解析。

## 推荐读取顺序

- 先读相关 cycle 的 `research-cycle-origin-and-motivation.md`，理解研究为什么存在、服务什么设计问题，以及为什么研究报告是高权重证据层但不是执行源。
- 再读本文件和各 report summary，获得当前激活研究轮次的摘要入口。
- 再按需回查各 cycle `originals/` 中的原始报告。
- 若设计依赖 PDF 图表 / 图片 / 版式，应先查看 `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`，不要把未复核图表当作已验证证据。
- 对 2026Q3 平台事实，操作前仍需重新核验最新官方文档和实际账户 / surface 配置。

## 相关研究输入与读取顺序

- research motivation: `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
- current research prompts: `raw/research-reports/current/current-research-prompts.md`
- prompt index: `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
- report-topic map: `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`
- latest platform-delta motivation: `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/research-cycle-origin-and-motivation.md`

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
| RPT-2026Q2-MT-0001 | AI Agent external persistent memory system testing/debugging/evaluation/failure diagnosis | `raw/research-reports/cycles/2026Q2-memory-testing/report-summaries/DR1_memory_testing_debugging_evidence_review_summary.md` | `raw/research-reports/cycles/2026Q2-memory-testing/originals/DR1_memory_testing_debugging_evidence_review_report.md` | completed_from_markdown_report | not_applicable_markdown | yes | Supplemental current evidence; no unified mature memory-specific testing standard, but reusable evaluation/debugging practices exist. |

## RPT-2026Q2-HO-0001 — DR2 handoff strategy / 交接包策略量化研究

- report_id: RPT-2026Q2-HO-0001
- cycle_id: RC-2026Q2-handoff-strategy
- title/topic: Mnemosyne handoff package strategy, correct handoff definition, quantitative evaluation, and cross-conversation/cross-agent continuation
- source_prompt: `raw/research-reports/cycles/2026Q2-handoff-strategy/research-prompts/originals/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_prompt.md`
- source_report: `raw/research-reports/cycles/2026Q2-handoff-strategy/originals/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_report.md`
- summary_path: `raw/research-reports/cycles/2026Q2-handoff-strategy/report-summaries/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_summary.md`
- central_conclusions:
  - Mnemosyne's handoff direction is basically correct but insufficiently quantified.
  - Correct handoff should be measured by recovery of execution source, current gate/state, authorities, prohibitions, next safe action, stale-state resistance, unsupported-assumption handling, and evidence-path quality.
  - A repeatable scored replay test should precede the first real target-project dry-run; blocker failures should prevent proceeding.
  - Handoff packages should be tiered into minimum, standard, and extended packages; longer packages are not automatically safer.
  - Model/tool provenance and hidden-context risks must be recorded for handoff tests.
- Mnemosyne design implications:
  - DR2 can inform future bounded updates to replay scoring, handoff package templates, and provenance schemas.
  - DR2 reinforces that pre-050 replay PASS does not close the post-050 gate and that current repository state must be verified against files.
  - DR2 should be routed through candidate/open-question/template review before any execution-source promotion.
- execution_source_status: not_execution_source

## RPT-2026Q2-UIG-0001 — DR4 user-input governance

- report_id: RPT-2026Q2-UIG-0001
- cycle_id: RC-2026Q2-user-input-governance
- title/topic: user originals, raw requirements, restatements, user-approved decisions, redactions, synthetic substitutes, external pointers, Git history exposure, repository visibility
- source_prompt: `raw/research-reports/cycles/2026Q2-user-input-governance/research-prompts/originals/DR4_user_originals_requirements_redaction_governance_prompt.md`
- source_report: `raw/research-reports/cycles/2026Q2-user-input-governance/originals/DR4_user_originals_requirements_redaction_governance_report.md`
- summary_path: `raw/research-reports/cycles/2026Q2-user-input-governance/report-summaries/DR4_user_originals_requirements_redaction_governance_summary.md`
- central_conclusions:
  - `visibility_unverified = public_equivalent` / public-risk for storage decisions.
  - Originals, raw requirements, sensitive project/customer materials, secrets, credentials, private source, and unredacted personal/confidential data default outside Git.
  - User-approved decisions, reviewed redacted excerpts, synthetic substitutes, and safe external pointers/manifests are eligible in Git if approved and safe.
  - AI/human restatements are explanatory layer, not original requirements or approved baseline.
  - Git history exposure means delete/move/revert does not erase historical exposure; private repo does not automatically authorize originals.
- execution_source_status: not_execution_source

## Supplemental summary — DR5 first real target-project dry-run evaluation

| report_id | topic | summary_file | source_file | summary_status | figure_review_status | active_evidence | notes |
|---|---|---|---|---|---|---|---|
| RPT-2026Q2-FTDRE-0001 | First real target-project dry-run evaluation framework | `raw/research-reports/cycles/2026Q2-first-target-dry-run-evaluation/report-summaries/DR5_first_real_target_dry_run_evaluation_framework_summary.md` | `raw/research-reports/cycles/2026Q2-first-target-dry-run-evaluation/originals/DR5_first_real_target_dry_run_evaluation_framework_report.md` | completed_from_markdown_report | not_applicable_markdown | supplemental_current_evidence | Evidence only; not execution source. |

## Supplemental summary — DR6 2026Q3 platform/context/apps delta

| report_id | topic | summary_file | source_file | summary_status | figure_review_status | active_evidence | notes |
|---|---|---|---|---|---|---|---|
| RPT-2026Q3-PLATFORM-DELTA-0001 | Project memory / apps / GitHub / Deep Research / Work-Codex-Agent / provenance / no-write delta | `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/report-summaries/DR6_2026Q3_platform_memory_apps_capability_delta_summary.md` | `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/originals/DR6_2026Q3_platform_memory_apps_capability_delta_report.md` | accepted_with_corrections | not_applicable_markdown | supplemental_current_evidence | Read `review-records/MNEMOSYNE-123-DR6-maintainer-evidence-review.md` first; original citation markers have limited portability, so use `source-manifest.md` for load-bearing official URLs. |
