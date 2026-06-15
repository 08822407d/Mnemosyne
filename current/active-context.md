# Active Context

## 当前阶段

MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。当前等待用户选择下一路线：PDF 图表复核、首次 dry-run 或 Idea Capture Buffer / candidate cleanup。

## MNEMOSYNE-031 current status

MNEMOSYNE-031 final writeback checkpoint status:

- R1/R2/R3 user review completed; no major issue reported by user.
- R4A prompt list completed.
- R4B user restatement completed: 9 main records + 1 addendum.
- R4B manifest/index completed.
- R4C synthesis completed as candidate draft, not execution source.
- R5 review completed through user confirmation of D-01 to D-07.
- Final writeback package prepared and checkpointed.
- Current execution source remains `current/human-approved-spec.md`.
- No PDF figure/table/image/layout review should be claimed.
- Original R5 draft is superseded by final user-confirmed decisions where they differ.

Next route should be selected by the user:

- PDF figure/table/image review;
- first dry-run using Mnemosyne itself or a small target scenario;
- Idea Capture Buffer / candidate requirements cleanup;
- template pack review / small fixes if needed.

## 当前执行源

`current/human-approved-spec.md` 是当前执行源。

以下内容不是执行源：

- `raw/`
- `raw/research-reports/`
- `raw/research-reports/current/current-research-prompts.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`
- `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
- `raw/research-reports/cycles/2026Q2-initial/report-summaries/`
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
- `raw/research-reports/current/current-report-summaries.md`
- `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md`
- `raw/user-design-restatements/MNEMOSYNE-031-user-design-intent-restatement.md`
- `notes/candidate-requirements.md`
- `notes/decision-log.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `handoff/startup-instructions.md`
- `notes/system-construction-baseline.md`
- `notes/overall-target-and-roadmap-snapshot.md`
- `notes/self-improvement-template-pack.md`
- `notes/target-project-memory-system-template-pack.md`
- `notes/delivery-manifest-template-pack.md`
- `notes/template-pack-review-and-first-scenario-selection.md`
- `notes/research-review-and-user-intent-restatement-workflow.md`

如发生冲突，以 `current/human-approved-spec.md` 为准，并登记 open question。

## 已完成内容

- v0.1 已被接受为可接手版本；
- v0.2 第一方向 self-improvement workflow 已完成流程说明和模板包；
- `notes/self-improvement-workflow.md` 已创建；
- `notes/self-improvement-template-pack.md` 已创建；
- `notes/target-project-memory-system-template-pack.md` 已创建；
- `notes/delivery-manifest-template-pack.md` 已创建；
- `notes/template-pack-review-and-first-scenario-selection.md` 已创建；
- 三类模板包 review 清单已创建；
- 首个场景候选矩阵已创建；
- trial run minimal input request 已创建；
- `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md` 已创建，研究动机入库；
- report-summaries README 已创建；
- 7 份研究报告 summary 文件已创建；
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md` 已创建；
- `raw/research-reports/current/current-report-summaries.md` 已创建；
- Codex Task Result Record 默认路径使用 `notes/codex-task-results/TASK_ID-result.md`；
- `notes/overall-target-and-roadmap-snapshot.md` 和 `notes/system-construction-baseline.md` 已作为规划 / 建设基线快照入库，且不是执行源。
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/README.md` 已创建；
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md` 已创建；
- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md` 已创建；
- `raw/research-reports/current/current-research-prompts.md` 已创建；
- pro 深度研究 prompt 原文路径约定已建立，且文件存在；
- RPT-2026Q2-0002 ~ RPT-2026Q2-0007 的轻度研究 prompt 原文缺失状态已记录为 `missing_original_prompt`；
- MNEMOSYNE-031 R1-R3 review、R4A prompt list、R4B restatement records、R4B manifest、R4C synthesis、R5 user decision review 与 final checkpoint records 已完成；
- MNEMOSYNE-032：Codex task authoring / diff verification guideline 已写入并落账，用于防止自然语言任务描述导致 Codex 未实际修改全部目标文件。

## 当前未完成内容


- 人工复核 PDF 图表 / 图片；
- 根据复核结果更新 figure review index；
- 用户 review `notes/delivery-manifest-template-pack.md`；
- 用户 review `notes/target-project-memory-system-template-pack.md`；
- 用户 review `notes/self-improvement-template-pack.md`；
- 用户 review `notes/template-pack-review-and-first-scenario-selection.md`；
- 根据 review 小修三类 template packs；
- 选择第一个目标项目场景；
- 第一轮 dry-run intake；
- Idea Capture Buffer；
- `AGENTS.md` / `CLAUDE.md`；
- 自动化增强（自动查重、自动写回、自动索引等）。
- 如果未来找回轻度研究 prompt，更新 `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`；

## 当前最重要文件

- `current/human-approved-spec.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `current/open-questions.md`
- `current/todo.md`
- `handoff/startup-instructions.md`
- `notes/self-improvement-workflow.md`
- `notes/self-improvement-template-pack.md`
- `notes/target-project-memory-system-template-pack.md`
- `notes/delivery-manifest-template-pack.md`
- `notes/template-pack-review-and-first-scenario-selection.md`
- `notes/research-review-and-user-intent-restatement-workflow.md`
- `notes/codex-task-authoring-and-diff-verification-guidelines.md`
- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`
- `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
- `raw/research-reports/current/current-report-summaries.md`
- `raw/research-reports/cycles/2026Q2-initial/report-summaries/README.md`
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
- `notes/system-construction-baseline.md`
- `notes/overall-target-and-roadmap-snapshot.md`
- `raw/research-reports/current/current-research-prompts.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`

## Next step / 下一步

1. MNEMOSYNE-031 R4B/R4C/R5 已完成并 checkpoint；不要重生成 R4B、R4C 或 R5。
2. 后续任务应使用 `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md` 中的 final D-01 to D-07 决策。
3. 当前下一路线由用户选择：PDF 图表复核 / first dry-run / Idea Capture Buffer / candidate cleanup。
4. 如果未来再次发现入口文件状态残留，可另开小型一致性修复；不要把这类修复写入 `current/human-approved-spec.md`。
