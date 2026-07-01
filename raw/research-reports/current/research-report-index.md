# Current Research Report Index / 当前研究报告索引（派生视图）

> 说明：本文件是 current 派生视图，不是原件存储位置。  
> 当前激活轮次来源：`RC-2026Q2-initial`；补充当前证据轮次：`RC-2026Q2-memory-testing`。  
> 原件保存在 `raw/research-reports/cycles/2026Q2-initial/originals/`。

## 当前激活轮次

- cycle_id: RC-2026Q2-initial
- status: active
- total_reports: 7

- cycle_id: RC-2026Q2-memory-testing
- status: supplemental_current_evidence_cycle
- total_reports: 1


## 研究动机入口

- motivation_file: `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
- status: created_by_MNEMOSYNE-030C
- 定位：该文件不是执行源，不是研究报告原件，也不是 summary；它用于解释 `RC-2026Q2-initial` 的 7 份报告为什么存在、分别服务什么设计问题，以及后续模型应如何使用这些报告。
- 建议读取顺序：先读 motivation，再读 `raw/research-reports/current/current-report-summaries.md`，再按需回查原始报告。
- current prompts: `raw/research-reports/current/current-research-prompts.md`
- prompt index: `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
- report-topic map: `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`

这些文件属于 research prompt / topic mapping 层，不是执行源，也不是研究报告结果。Prompt 是研究输入；report / summary / evidence map 是研究结果或派生证据。缺失的轻度研究 prompt 不得编造。

## 报告索引

| report_id | file_path | report_type | 主题 | 在 Mnemosyne 设计中的作用 | active_evidence | 可读性与复核说明 |
|---|---|---|---|---|---|---|
| RPT-2026Q2-0001 | raw/research-reports/cycles/2026Q2-initial/originals/AI agent 长期记忆系统 pro深度研究.txt | pro | Pro 版综合深度研究报告 | 作为跨平台能力边界、机制选型与 v0.1 承诺范围的综合高权重证据 | yes | TXT 通常可被 Codex 直接读取；仍建议对关键结论做人工抽样复核 |
| RPT-2026Q2-0002 | raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 1：非开发长期对话记忆是否已有真实实践.pdf | light | 非开发长期对话记忆实践 | 约束“普通对话场景长期记忆”的现实可行边界与可交付承诺 | yes | PDF：文本可能可读，图表/图片/版式信息需人工复核 |
| RPT-2026Q2-0003 | raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 2：ChatGPT,Claude 纯对话场景的外部记忆能力边界.pdf | light | ChatGPT / Claude 纯对话外部记忆能力边界 | 约束“无额外工具时的自动化假设”与对话窗口能力声明 | yes | PDF：文本可能可读，图表/图片/版式信息需人工复核 |
| RPT-2026Q2-0004 | raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 3：Codex,Claude Code,Cursor 等本地开发 Agent 的文件式记忆能力.pdf | light | 本地开发 Agent 文件式记忆能力 | 支撑“仓库文件写入、Git diff、可追溯记忆”相关机制设计 | yes | PDF：文本可能可读，图表/图片/版式信息需人工复核 |
| RPT-2026Q2-0005 | raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 4：云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计.pdf | light | 云端 Coding Agent + GitHub 工作流审计写回 | 支撑“PR/review/审计式写回”路径与权限边界判断 | yes | PDF：文本可能可读，图表/图片/版式信息需人工复核 |
| RPT-2026Q2-0006 | raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 5：外部持久记忆的理论与工程依据.pdf | light | 外部持久记忆理论与工程依据 | 支撑“外部文件/Git 作为长期真相源”的理论与工程正当性 | yes | PDF：文本可能可读，图表/图片/版式信息需人工复核 |
| RPT-2026Q2-0007 | raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 6：开发场景的持久记忆经验能否迁移到普通长期对话和学习场景.pdf | light | 开发场景经验向普通长期对话/学习迁移 | 约束“跨场景迁移”策略、可复用程度与必要改造项 | yes | PDF：文本可能可读，图表/图片/版式信息需人工复核 |


## Supplemental current evidence cycle: RC-2026Q2-memory-testing

| report_id | file_path | report_type | 主题 | 在 Mnemosyne 设计中的作用 | active_evidence | 可读性与复核说明 |
|---|---|---|---|---|---|---|
| RPT-2026Q2-MT-0001 | raw/research-reports/cycles/2026Q2-memory-testing/originals/DR1_memory_testing_debugging_evidence_review_report.md | deep_research | AI Agent external persistent memory system testing/debugging/evaluation/failure diagnosis | Evidence for memory-system evaluation maturity, failure taxonomy, OP-09/OP-10 partial answers, and first target-project dry-run checklist design | yes | Markdown report original; summary available at `raw/research-reports/cycles/2026Q2-memory-testing/report-summaries/DR1_memory_testing_debugging_evidence_review_summary.md`. Research evidence only, not execution source. |

## Supplemental current evidence cycle — RC-2026Q2-handoff-strategy

- cycle_id: RC-2026Q2-handoff-strategy
- status: supplemental_current_evidence_cycle
- total_reports: 1
- positioning: research evidence only; not execution source

| report_id | file_path | report_type | 主题 | 在 Mnemosyne 设计中的作用 | active_evidence | 可读性与复核说明 |
|---|---|---|---|---|---|---|
| RPT-2026Q2-HO-0001 | raw/research-reports/cycles/2026Q2-handoff-strategy/originals/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_report.md | deep_research | Mnemosyne handoff package strategy and quantitative evaluation | Evidence for correct handoff definition, quantitative handoff scoring, handoff package tiering, replay/test protocol, model/tool provenance, and pre-first-target-dry-run handoff readiness | yes | Markdown report original; summary available at raw/research-reports/cycles/2026Q2-handoff-strategy/report-summaries/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_summary.md. Research evidence only, not execution source. |

## Supplemental current evidence cycle: RC-2026Q2-user-input-governance

- cycle_id: RC-2026Q2-user-input-governance
- status: supplemental_current_evidence_cycle
- total_reports: 1
- positioning: research evidence only; not execution source

| report_id | file_path | report_type | 主题 | 在 Mnemosyne 设计中的作用 | active_evidence | 可读性与复核说明 |
|---|---|---|---|---|---|---|
| RPT-2026Q2-UIG-0001 | raw/research-reports/cycles/2026Q2-user-input-governance/originals/DR4_user_originals_requirements_redaction_governance_report.md | deep_research | User originals / raw requirements / restatements / approved decisions / redaction / external pointers / Git history exposure / repository visibility | Supplemental evidence for target user-input storage governance before first real target-project dry-run | yes | Markdown report original; summary available at `raw/research-reports/cycles/2026Q2-user-input-governance/report-summaries/DR4_user_originals_requirements_redaction_governance_summary.md`. Research evidence only, not execution source. |

## Supplemental current evidence — RC-2026Q2-first-target-dry-run-evaluation

- cycle_id: RC-2026Q2-first-target-dry-run-evaluation
- status: supplemental_current_evidence_cycle
- report_id: RPT-2026Q2-FTDRE-0001
- report_path: `raw/research-reports/cycles/2026Q2-first-target-dry-run-evaluation/originals/DR5_first_real_target_dry_run_evaluation_framework_report.md`
- summary_path: `raw/research-reports/cycles/2026Q2-first-target-dry-run-evaluation/report-summaries/DR5_first_real_target_dry_run_evaluation_framework_summary.md`
- execution_source_status: not_execution_source
- use: supplemental evidence for first real target-project dry-run evaluation, scorecard, postmortem, and regression test design.
