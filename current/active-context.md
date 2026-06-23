# Active Context

## Current compact view

### current phase

- Post-MNEMOSYNE-050 Batch B pre-real-dry-run protocol closure.
- Batch A small fixes are verified passed: post-047 ordinary Mnemosyne conversation verification result PASS, and MNEMOSYNE-048 ordinary Mnemosyne conversation verification result PASS.
- The pre-050 fresh ordinary replay was user-supplied and verified PASS for the pre-050 package.
- MNEMOSYNE-050 changes the onboarding/replay/check semantics, so the prior replay does not close the post-050 gate.
- Batch B preparation has produced onboarding/review instruments, a stable run-manifest template, and a stable fresh replay protocol, but real dry-run has not started.

### current execution source

- `current/human-approved-spec.md` is the current and only execution source.
- Active context, handoff, TODO, open questions, research reports, candidates, decision logs, dry-run/replay templates, and Codex result records are not execution source.

### latest completed checkpoints

- MNEMOSYNE-040: DR1 memory-system testing/debugging/evaluation evidence ingested as `RC-2026Q2-memory-testing`; DR1 is evidence only, not execution source.
- MNEMOSYNE-041: manual import inbox workflow established for current Codex Cloud non-image attachment limitations.
- MNEMOSYNE-042: user-action-first reply format added to the execution source.
- MNEMOSYNE-043: manual-import safety gate established; public or unverified visibility allows only public, synthetic, or explicitly redacted material.
- MNEMOSYNE-044: D-01–D-07 execution-source coverage map created; execution status comes from the coverage map plus `current/human-approved-spec.md`.
- MNEMOSYNE-045: current-state cleanup verified the compact current view as live state.
- MNEMOSYNE-046: first target-project dry-run minimal instruments created as non-execution-source design-only instruments; no real target-project dry-run has occurred.
- MNEMOSYNE-047: final Batch A residuals corrected and post-047 ordinary Mnemosyne conversation verification returned PASS.
- MNEMOSYNE-048: ordinary Mnemosyne conversation verification returned PASS; created the first-target-project dry-run onboarding package and review instruments.
- MNEMOSYNE-049: state synchronization after 048 records the fresh replay gate and current no-target/no-dry-run boundaries.
- MNEMOSYNE-050: added stable run-manifest and fresh replay protocol templates, unified check semantics, clarified actor/write and issue-layer semantics, and updated this state for a post-050 replay gate.

### current blockers/gates

- Next gate: post-MNEMOSYNE-050 fresh ordinary Thinking replay using `notes/first-target-project-fresh-replay-protocol.md`.
- Do not start real target-project dry-run until the post-050 fresh ordinary Thinking startup/handoff replay returns reviewed PASS.
- After post-050 replay PASS, user must still select a target, approve authority/safe input/no-target-write, and approve the run manifest.
- No real target-project dry-run has occurred.
- No target project has been selected.
- No target materials have been uploaded/ingested.
- No target repository has been written.
- Unpromoted checkpoint/candidate/research content is not executable.
- Manual imports must apply the MNEMOSYNE-043 safety gate and stop on unsafe or ambiguous material.

### current next route

- Run post-MNEMOSYNE-050 fresh ordinary Thinking startup/handoff replay using `notes/first-target-project-fresh-replay-protocol.md` and `handoff/first-target-project-dry-run-onboarding-package.md`.
- Do not start target dry-run, choose target, or upload target material before that replay and user approval.
- Do not treat the pre-050 replay PASS as validating the post-050 package.

### important non-execution-source references

- `notes/first-target-project-fresh-replay-protocol.md` for the next post-050 fresh ordinary Thinking startup/handoff replay.
- `notes/first-target-project-dry-run-manifest-template.md` for the run manifest required before a real dry-run.
- `handoff/first-target-project-dry-run-onboarding-package.md` for the first target-project dry-run onboarding package.
- `notes/first-target-project-dry-run-review-instruments.md` and related first-dry-run instruments for later authorized dry-run preparation.
- `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md` for D-01–D-07 reflection/promotion status.
- `notes/codex-task-results/MNEMOSYNE-047-result.md`, `notes/codex-task-results/MNEMOSYNE-048-result.md`, `notes/codex-task-results/MNEMOSYNE-049-result.md`, and `notes/codex-task-results/MNEMOSYNE-050-result.md` for recent task outcomes.
- `manual-import-inbox/README.md` and `notes/manual-import-inbox-workflow.md` for import tasks only.
- Research current views under `raw/research-reports/current/` for tool/capability/new mechanism/target-project design questions.

### visibility context

- Repository visibility is user-controlled and may alternate between public/private by stage.
- Current visibility must be reverified when material is imported.
- Visibility state alone is not a repair issue.
- MNEMOSYNE-043 safety rules remain applicable.

## Historical / superseded context below

The material below is retained for audit/history and may include superseded route wording. Do not use it as the current route when it conflicts with the compact current view above or with later task result records.

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
- `raw/research-reports/cycles/2026Q2-memory-testing/`
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
- MNEMOSYNE-038 已恢复并索引 RPT-2026Q2-0002 ~ RPT-2026Q2-0007 对应的轻度研究 prompt 原文，先前 `missing_original_prompt` 状态已被 supersede；
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
- MNEMOSYNE-038 已找回并更新 6 个轻度研究 prompt 原文及相关索引；

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
2. 后续任务应参考 `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md` 区分 final D-01 to D-07 checkpoint records 与当前可执行 spec 内容；不要把全部七项直接当作执行规则。
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

## MNEMOSYNE-044 D-01–D-07 coverage map

MNEMOSYNE-044 adds `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md` as a non-execution-source review/proposal artifact. The final MNEMOSYNE-031 D-01 to D-07 decisions remain authoritative checkpoint records, but they are not automatically standing execution rules. Only content already reflected in `current/human-approved-spec.md` is currently executable. The coverage map identifies D-01, D-03, D-04, and D-05 as needing separate user approval before any candidate wording can be promoted; D-06 remains research-gated/non-executable, and D-07 is checkpoint-only.

## MNEMOSYNE-051 / DR2 handoff-strategy research note

- MNEMOSYNE-051 ingests DR2 handoff-strategy research as `RC-2026Q2-handoff-strategy`.
- DR2 is research evidence only, not execution source.
- It provides evidence for correct handoff definition, scoring rubric, handoff tiers, replay testing, model/tool provenance, and pre-first-target-dry-run handoff readiness.
- It does not itself close the post-MNEMOSYNE-050 replay gate.
- It does not start a real target-project dry-run.
- It does not select a target project.
- It may inform a future bounded task to update replay/handoff templates or scoring instruments.
