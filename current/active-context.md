# Active Context

## 当前阶段

MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 dry-run independent verification 已完成，final verdict 为 PASS。当前等待用户选择下一路线：PDF 图表复核、Idea Capture Buffer / candidate cleanup、template review / small fixes 或 memory-system testing/debugging feasibility research。

## MNEMOSYNE-035 status

- Operation/conclusion separation guidance has been added to the execution source.
- The load command has been updated to apply the guidance.
- No `AGENTS.md`, `CLAUDE.md`, GitHub Actions, or automation was added.
- Current execution source remains `current/human-approved-spec.md`.

## MNEMOSYNE-034 status

- Objective neutral engineering stance has been added to the execution source.
- `commands/` registry has been added for lightweight user-facing guidance shortcuts.
- No `AGENTS.md`, `CLAUDE.md`, GitHub Actions, or automation was added.
- Current execution source remains `current/human-approved-spec.md`.

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
- MNEMOSYNE-032 first dry-run has completed independent verification with verdict `PASS`;
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
- MNEMOSYNE-032 dry-run independent verification：final verdict `PASS`；invalid_test_triggered=false；blocking_issues=[]；dry-run artifacts remain validation evidence, not execution source or final design.

## 当前未完成内容


- 人工复核 PDF 图表 / 图片；
- 根据复核结果更新 figure review index；
- 用户 review `notes/delivery-manifest-template-pack.md`；
- 用户 review `notes/target-project-memory-system-template-pack.md`；
- 用户 review `notes/self-improvement-template-pack.md`；
- 用户 review `notes/template-pack-review-and-first-scenario-selection.md`；
- 根据 review 小修三类 template packs；
- 选择第一个目标项目场景；
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
3. 当前下一路线由用户选择：PDF 图表复核 / Idea Capture Buffer / candidate cleanup / template review / memory-system testing-debugging feasibility research。
4. 如果未来再次发现入口文件状态残留，可另开小型一致性修复；不要把这类修复写入 `current/human-approved-spec.md`。

## MNEMOSYNE-033 Idea Capture Buffer update

- MNEMOSYNE-033 已建立 Idea Capture Buffer / candidate cleanup 机制。
- 已创建 `notes/idea-capture-triage-rules.md`。
- 已创建 `notes/idea-capture-buffer.md`。
- 新想法进入 buffer，不直接进入 execution source。
- 下一步：使用 idea buffer 捕获新想法，生成 / 执行 Pro Deep Research prompt，后续选择 PDF review / template review / first real target dry-run。

## MNEMOSYNE-033A exported conversation insight backfill

- MNEMOSYNE-033A 已将导出对话洞察补录到 idea buffer / open questions / candidate cleanup。
- 补录内容来源类型为 `historical_conversation_derived_insight`，不是执行源、不是最终设计、不是用户批准 spec。
- 完整对话导出默认不入库；本次只创建 `RAW-0055` 摘要定位和 buffer / candidate / open question 条目。
- 当前执行源仍是 `current/human-approved-spec.md`。

Pending after MNEMOSYNE-033A:

- triage IDEA-2026-0009 之后的新增 exported-conversation-derived entries；
- 决定完整导出记录是否需要清洗版摘要 / selected excerpts；
- 处理模型能力差异 / Codex 模型选择等 open questions；
- 明确 AI 回复在 raw/context evidence 中保存粒度；
- 继续 Pro Deep Research / PDF review / template review / first target selection。
