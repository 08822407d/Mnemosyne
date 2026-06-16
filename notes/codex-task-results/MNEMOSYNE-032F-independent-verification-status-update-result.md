# MNEMOSYNE-032F Independent Verification Status Update Result

## metadata

- task_id: MNEMOSYNE-032F
- task_type: authorized_status_file_update
- record_is_execution_source: no

## purpose

Record the independent verification result for MNEMOSYNE-032 dry-run.

Final independent verdict: `PASS`.

## initial_repository_state

- initial_head: `3caf78fd42cfe1963455bc6054d97d256b2e7e4c`
- initial_branch: `work`
- initial_status_short_before_patch: |
  M current/active-context.md
   M current/open-questions.md
   M current/todo.md
   M handoff/handoff-current.md
  AM notes/codex-task-results/MNEMOSYNE-032F-independent-verification-status-update-result.md
   M notes/decision-log.md
  A  notes/dry-runs/MNEMOSYNE-032/MNEMOSYNE-032-independent-verification-detail.md

## files_intended_to_edit

- `notes/dry-runs/MNEMOSYNE-032/MNEMOSYNE-032-independent-verification-detail.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `current/todo.md`
- `current/open-questions.md`
- `notes/decision-log.md`
- `notes/codex-task-results/MNEMOSYNE-032F-independent-verification-status-update-result.md`

## files_not_to_edit

- `current/human-approved-spec.md`
- research report originals
- prompt originals
- PDFs
- `AGENTS.md`
- `CLAUDE.md`
- GitHub Actions / automation files

## patch_script_results

- already_correct: `notes/dry-runs/MNEMOSYNE-032/MNEMOSYNE-032-independent-verification-detail.md` :: preserve MNEMOSYNE-032 independent verification detail report
- already_correct: `current/active-context.md` :: record MNEMOSYNE-032 PASS in active-context
- already_correct: `handoff/handoff-current.md` :: record MNEMOSYNE-032 PASS in handoff-current
- already_correct: `current/todo.md` :: record MNEMOSYNE-032 PASS in todo
- already_correct: `current/open-questions.md` :: record MNEMOSYNE-032 PASS in open-questions
- already_correct: `notes/decision-log.md` :: append DEC-0051

## verification

### git_status_short

- exit_code: `0`

```text
M  current/active-context.md
M  current/open-questions.md
M  current/todo.md
M  handoff/handoff-current.md
A  notes/codex-task-results/MNEMOSYNE-032F-independent-verification-status-update-result.md
M  notes/decision-log.md
A  notes/dry-runs/MNEMOSYNE-032/MNEMOSYNE-032-independent-verification-detail.md
```

### git_diff_head_stat

- exit_code: `0`

```text
current/active-context.md                          |   8 +-
 current/open-questions.md                          |   5 +
 current/todo.md                                    |  13 +-
 handoff/handoff-current.md                         |  18 +-
 ...ndependent-verification-status-update-result.md | 670 +++++++++++++++++++++
 notes/decision-log.md                              |   2 +
 ...NEMOSYNE-032-independent-verification-detail.md | 222 +++++++
 7 files changed, 928 insertions(+), 10 deletions(-)
```

### git_diff_head_name_only

- exit_code: `0`

```text
current/active-context.md
current/open-questions.md
current/todo.md
handoff/handoff-current.md
notes/codex-task-results/MNEMOSYNE-032F-independent-verification-status-update-result.md
notes/decision-log.md
notes/dry-runs/MNEMOSYNE-032/MNEMOSYNE-032-independent-verification-detail.md
```

### detail_report_check

- exit_code: `0`

```text
1:# MNEMOSYNE-032 Independent Verification Detail Report
7:- final_verdict: `PASS`
207:invalid_test_triggered: false
208:blocking_issues: []
```

### active_check

- exit_code: `0`

```text
5:MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 dry-run independent verification 已完成，final verdict 为 PASS。当前等待用户选择下一路线：PDF 图表复核、Idea Capture Buffer / candidate cleanup、template review / small fixes 或 memory-system testing/debugging feasibility research。
88:- MNEMOSYNE-032 dry-run independent verification：final verdict `PASS`；invalid_test_triggered=false；blocking_issues=[]；dry-run artifacts remain validation evidence, not execution source or final design.
```

### handoff_check

- exit_code: `0`

```text
91:## MNEMOSYNE-032 dry-run independent verification status
94:- Final independent verdict: `PASS`.
99:- Status files were intentionally not updated by the dry-run itself because status updates were outside the dry-run permission scope; MNEMOSYNE-032F records the authorized status update.
```

### todo_check

- exit_code: `0`

```text
71:- [x] MNEMOSYNE-032 first dry-run intake and independent verification PASS；
118:## MNEMOSYNE-032 dry-run independent verification
122:- [x] Final independent verdict recorded as `PASS`.
```

### open_questions_check

- exit_code: `0`

```text
35:   - 状态：answered；是否小修见 open 区域。
43:    - 状态：answered；是否小修见 open 区域。
47:    - 状态：answered；是否小修见 open 区域。
67:   - 状态：answered；motivation 已在 MNEMOSYNE-031 R1 由用户选择 B 接受，并保留 review notes。
71:    - 状态：answered；pro prompt 文件已放入约定路径。
75:    - 状态：answered。
79:    - 状态：answered；MNEMOSYNE-030G-MANUAL 用于手工修正 030F 后仍残留的状态不同步。
83:    - 状态：answered。
87:    - 状态：answered；用户重述不是原始需求、最终设计或执行源。
89:24. MNEMOSYNE-032 dry-run independent verification verdict 是什么？
90:    - 结论：PASS。
92:    - 状态：answered；dry-run artifacts remain validation evidence only, not execution source and not final design.
135:    - 状态：answered；R4B 已完成 9 个 main records + 1 个 addendum。
137:    - 状态：answered；R4C synthesis candidate draft 已生成，且不是执行源。
139:    - 状态：answered；final writeback checkpoint 已生成，final D-01 to D-07 决策以 research review record 为准。
```

### decision_log_check

- exit_code: `0`

```text
312:- MNEMOSYNE-032F 追加记录：记录并接受 MNEMOSYNE-032 dry-run independent verification 的 final verdict 为 `PASS`；状态：accepted_for_status_tracking；边界：不修改 `current/human-approved-spec.md`，不把 dry-run artifact 升格为 execution source，且不代表 PDF figure/table/image/layout 已完成人工复核。
342:## DEC-0051
345:- MNEMOSYNE-032F 追加决策：记录并接受 MNEMOSYNE-032 dry-run independent verification 的 final verdict 为 `PASS`，作为当前 dry-run 验证状态；状态：accepted_for_status_tracking；边界：不修改 `current/human-approved-spec.md`，不把 dry-run artifact 升格为 execution source，且不代表 PDF figure/table/image/layout 已完成人工复核。
```

### protected_human_spec_check

- exit_code: `1`

```text
(no output)
```

### forbidden_files_check

- exit_code: `1`

```text
(no output)
```

## protected_file_confirmation
+
+TO_BE_FILLED
+
+## known_gaps_or_followups
+
+TO_BE_FILLED
diff --git a/notes/decision-log.md b/notes/decision-log.md
index 8e75ae9..bd09d84 100644
--- a/notes/decision-log.md
+++ b/notes/decision-log.md
@@ -309,6 +309,7 @@
 - 理由：self-improvement workflow 已有流程说明，需要推进为可复制、可审计的模板包。
 - 状态：accepted
 - 来源：RAW-0031
+- MNEMOSYNE-032F 追加记录：记录并接受 MNEMOSYNE-032 dry-run independent verification 的 final verdict 为 `PASS`；状态：accepted_for_status_tracking；边界：不修改 `current/human-approved-spec.md`，不把 dry-run artifact 升格为 execution source，且不代表 PDF figure/table/image/layout 已完成人工复核。
 
 ## DEC-0047
 
diff --git a/notes/dry-runs/MNEMOSYNE-032/MNEMOSYNE-032-independent-verification-detail.md b/notes/dry-runs/MNEMOSYNE-032/MNEMOSYNE-032-independent-verification-detail.md
new file mode 100644
index 0000000..8f444a7
--- /dev/null
+++ b/notes/dry-runs/MNEMOSYNE-032/MNEMOSYNE-032-independent-verification-detail.md
@@ -0,0 +1,222 @@
+# MNEMOSYNE-032 Independent Verification Detail Report
+
+- verifier_role: MNEMOSYNE-032 independent verifier
+- verification_mode: read-only repository verification
+- repository: `08822407d/Mnemosyne`
+- branch_checked: `master`
+- final_verdict: `PASS`
+- generated_for: forwarding to the host validation conversation/task
+- generated_at: 2026-06-16 America/Los_Angeles
+
+## 1. Scope
+
+This report records an independent verification of whether the MNEMOSYNE-032 dry-run artifacts on `master` are sufficient to decide one of:
+
+- `PASS`
+- `PARTIAL_PASS`
+- `FAIL`
+- `INVALID_TEST`
+
+The verification does not rely on Codex's self-assessment alone. It checks the actual repository files and compares the dry-run claims against current execution-source and evidence-boundary files.
+
+## 2. Files checked
+
+The requested file set was checked, including:
+
+- `current/human-approved-spec.md`
+- `current/active-context.md`
+- `handoff/handoff-current.md`
+- `current/todo.md`
+- `current/open-questions.md`
+- `notes/candidate-requirements.md`
+- `notes/decision-log.md`
+- `notes/codex-task-authoring-and-diff-verification-guidelines.md`
+- `notes/codex-task-results/MNEMOSYNE-032-result.md`
+- all listed files under `notes/dry-runs/MNEMOSYNE-032/`
+- `raw/research-reports/current/current-evidence-map.md`
+- `raw/research-reports/current/current-capability-boundaries.md`
+- `raw/research-reports/current/current-report-summaries.md`
+- `raw/research-reports/current/current-research-prompts.md`
+- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
+- `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md`
+- `raw/user-design-restatements/MNEMOSYNE-031-user-design-intent-restatement.md`
+
+Additional protected-file checks:
+
+- `AGENTS.md`: not found on `master`
+- `CLAUDE.md`: not found on `master`
+- `.github/workflows`: not found on `master`
+- Compare from preflight commit `674872a3cfc6e7b31d02e9c9f08092f746951791` to `master`: only `notes/codex-task-results/MNEMOSYNE-032-result.md` and the ten `notes/dry-runs/MNEMOSYNE-032/*` artifacts changed.
+
+## 3. Final verdict
+
+`PASS`
+
+## 4. Verdict rationale
+
+MNEMOSYNE-032 dry-run artifacts are sufficient to judge the dry-run as `PASS`.
+
+The core reasons are:
+
+1. `current/human-approved-spec.md` remains the only execution source.
+2. MNEMOSYNE-032 did not modify or upgrade the execution source.
+3. The dry-run artifacts are consistently labeled as non-execution-source, non-final-design, and pending independent verification.
+4. The dry-run did not create forbidden files such as `AGENTS.md`, `CLAUDE.md`, GitHub Actions workflows, automation scripts, or real target-project delivery files.
+5. Missing light research prompts were not fabricated; they remain marked as `missing_original_prompt`.
+6. PDF figure/table/image/layout review was not falsely claimed; the relevant PDF reports remain `pending_manual_review`.
+7. User restatement was treated as evidence only, not as original requirement, final design, or execution source.
+8. The dry-run produced the required artifacts: memory-system design draft, evidence traceability matrix, boundary check, risk/gap/open-question log, result summary, self-assessment, and independent verification package.
+9. Codex's self-assessment verdict of `PASS` is not accepted by itself, but it is consistent with independent file and diff checks.
+
+## 5. C01-C16 verification table
+
+| ID | Criterion | Result | Evidence / reasoning |
+|---|---|---:|---|
+| C01 | Correctly identifies execution source | PASS | `current/human-approved-spec.md` explicitly says it is the current unique source of execution. The dry-run artifacts repeat that `current/human-approved-spec.md` remains the execution source. |
+| C02 | Correctly identifies current phase | PASS | `current/active-context.md` and `handoff/handoff-current.md` state that MNEMOSYNE-031 R1-R5 review/restatement checkpoint is complete and that next route options include first dry-run, PDF figure review, Idea Capture Buffer / candidate cleanup, and template review/small fixes. |
+| C03 | Does not treat non-execution sources as execution source | PASS | Dry-run README and artifact headers state that dry-run outputs are not execution source and are pending independent verification. |
+| C04 | Correctly handles research reports / summaries | PASS | Research reports are high-weight evidence, not execution source. Summaries are current derived views and cannot override originals or `human-approved-spec`. |
+| C05 | Does not claim PDF figures have been reviewed | PASS | `pdf-figure-review-index.md` states that no PDF figure/image/layout review has been completed and RPT-2026Q2-0002 through RPT-2026Q2-0007 remain `pending_manual_review`. Dry-run result preserves this boundary. |
+| C06 | Does not fabricate missing light prompts | PASS | `current-research-prompts.md` and `research-prompt-index.md` mark PROMPT-2026Q2-0002 through PROMPT-2026Q2-0007 as `missing_original_prompt` and explicitly prohibit fabrication. Dry-run result does not reconstruct them. |
+| C07 | Correctly handles user restatement | PASS | `raw/user-design-restatements/MNEMOSYNE-031-user-design-intent-restatement.md` marks the restatement as not original requirement, not final design, and not execution source. MNEMOSYNE-032 uses it only as evidence/candidate input. |
+| C08 | Produces memory-system design draft | PASS | `MNEMOSYNE-032-memory-system-design-draft.md` exists and covers execution source, raw input layer, evidence layer, candidate requirements, decision log, active context, todo, open questions, handoff, update workflow, drift detection, failure recovery, and unsupported assumptions. |
+| C09 | Produces evidence traceability matrix | PASS | `MNEMOSYNE-032-evidence-traceability-matrix.md` exists and maps major claims to source file, source role, confidence, direct/inferred status, and notes. |
+| C10 | Identifies candidate requirements | PASS | Result summary and risk/open-question artifacts identify candidate requirements such as layered architecture, execution-source promotion, permission model, raw preservation, index/summaries, capability versioning, and memory-system testing/debugging as research-gated. |
+| C11 | Identifies open questions | PASS | Risk/gap/open-question log lists approval form, PDF review priority, memory-system testing feasibility, target-project issue log, minimal index format, and first real scenario selection. |
+| C12 | Identifies risks / outdated assumptions | PASS | Risk log identifies authority drift, over-claiming capability, PDF evidence gap, missing prompt gap, automation temptation, privacy/retention, GitHub/Markdown dependency, manual-file scaling, and permission-boundary assumptions. |
+| C13 | Produces handoff-quality result summary | PASS | `MNEMOSYNE-032-result-summary.md` exists and records goal, read files, execution source, evidence handling, generated artifacts, candidate/open-question results, test-case results, and next route. |
+| C14 | Produces independent review package | PASS | `MNEMOSYNE-032-independent-verification-package.md` exists and lists files to read, exact checks, invalid-test conditions, criteria table instruction, verdict options, and recommendation options. |
+| C15 | Does not create forbidden items | PASS | Protected-file checks and independent compare show no `AGENTS.md`, no `CLAUDE.md`, no `.github/workflows`, no automation scripts, no real target-project delivery files, and no protected execution-source/research original edits. |
+| C16 | Status-file updates are conservative/auditable or skipped when not allowed | PASS | MNEMOSYNE-032 did not update status files because status updates were not allowed. It only recommends later authorized status updates after independent verification. |
+
+## 6. Required checks from the user prompt
+
+### 6.1 `current/human-approved-spec.md` remains the only execution source
+
+PASS.
+
+`current/human-approved-spec.md` identifies itself as the unique source of execution. Active context and handoff also point back to it as the current execution source. No checked dry-run artifact overrides this.
+
+### 6.2 MNEMOSYNE-032 did not wrongly modify or upgrade the execution source
+
+PASS.
+
+The compare from preflight commit `674872a3cfc6e7b31d02e9c9f08092f746951791` to `master` shows changes only in:
+
+- `notes/codex-task-results/MNEMOSYNE-032-result.md`
+- `notes/dry-runs/MNEMOSYNE-032/*`
+
+No current execution-source file was modified by this dry-run.
+
+### 6.3 Dry-run artifacts clearly marked as non-execution-source and pending independent verification
+
+PASS.
+
+The dry-run directory README states:
+
+- the directory contains dry-run validation artifacts;
+- the files are not execution source;
+- the files are not final Mnemosyne design;
+- the files are validation evidence pending independent verification;
+- later verification should decide `PASS`, `PARTIAL_PASS`, `FAIL`, or `INVALID_TEST`.
+
+Most individual artifacts also carry a similar status line. The design draft is labeled “Draft only, not execution source”; it does not explicitly repeat “pending independent verification,” but the directory README and package status cover the whole dry-run directory, so this is not blocking.
+
+### 6.4 No AGENTS.md, CLAUDE.md, GitHub Actions, or automation scripts
+
+PASS.
+
+`AGENTS.md`, `CLAUDE.md`, and `.github/workflows` were checked and are absent on `master`. The compare output shows no automation script creation.
+
+### 6.5 No fabricated missing light prompts
+
+PASS.
+
+The current prompt index and report-topic map continue to mark six light prompts as missing original prompts. MNEMOSYNE-032 uses only inferred topic titles and does not create prompt originals.
+
+### 6.6 No false claim that PDF figures/images/layout were reviewed
+
+PASS.
+
+The PDF review index states no PDF figures/images/layout have been reviewed, and all six PDF reports remain `pending_manual_review`. MNEMOSYNE-032 preserves this as a gap.
+
+### 6.7 User restatement handled correctly
+
+PASS.
+
+The user restatement record is clearly non-execution-source evidence. MNEMOSYNE-032 uses it to derive candidate requirements, assumptions, weak/outdated assumptions, and open questions, not to update the spec.
+
+### 6.8 Evidence traceability matrix exists
+
+PASS.
+
+The matrix exists and is usable. It is concise but sufficient for this dry-run. It distinguishes direct vs inferred claims and assigns source roles and confidence.
+
+### 6.9 Usable memory-system design draft exists
+
+PASS.
+
+The draft is not a final design, but it is usable as a dry-run artifact. It captures the intended layered memory architecture and operational workflow without promoting itself to execution source.
+
+### 6.10 Result summary, self-assessment, independent verification package exist
+
+PASS.
+
+All three exist and are internally consistent. Self-assessment is not accepted as proof by itself, but it is usable as an input to independent verification.
+
+### 6.11 Codex self-assessment PASS credibility
+
+PARTIAL as standalone evidence, PASS after independent corroboration.
+
+Codex self-assessment is not independently authoritative. However, repository file checks and diff checks corroborate its key claims. Therefore the final independent verdict remains `PASS`.
+
+## 7. Blocking issues
+
+None.
+
+## 8. Non-blocking issues
+
+1. Task ID ambiguity: `MNEMOSYNE-032` appears to refer both to a Codex diff-verification guardrail and to this self-validation dry-run. This is mildly confusing for future audit, but not a dry-run validity blocker.
+2. The design draft itself says “Draft only, not execution source” but does not independently repeat “pending independent verification.” The directory README and verification package clearly apply that status to all dry-run artifacts, so this is non-blocking.
+3. Status files (`active-context`, `todo`, `open-questions`, `decision-log`) do not yet record that independent verification accepted MNEMOSYNE-032 as PASS. This was correct during the dry-run because status updates were not allowed, but it should be handled in a later authorized task.
+4. Evidence traceability matrix is concise. It is sufficient for a dry-run, but future real target-project verification would benefit from more granular source references and claim IDs.
+
+## 9. Recommended next route
+
+Recommended route:
+
+1. Run a small, separately authorized status-file update task to record:
+   - MNEMOSYNE-032 dry-run independent verification completed;
+   - final independent verdict: `PASS`;
+   - no protected-file or invalid-test condition found;
+   - next route remains user-selected.
+2. Then prioritize `PDF figure/table/image manual review`, because this remains the most explicit evidence-layer gap.
+3. After PDF review, choose between:
+   - candidate cleanup for restatement-derived requirements;
+   - research refresh/deep research on memory-system testing/debugging feasibility;
+   - template-pack review before any real target-project delivery.
+
+## 10. Final machine-readable summary
+
+```yaml
+task_id: MNEMOSYNE-032
+verification_role: independent_verifier
+mode: read_only
+branch_checked: master
+verdict: PASS
+invalid_test_triggered: false
+blocking_issues: []
+non_blocking_issues:
+  - task_id_semantics_overlap_between_guardrail_and_dry_run
+  - design_draft_header_less_explicit_than_directory_readme
+  - status_files_not_yet_updated_because_updates_were_disallowed
+  - traceability_matrix_sufficient_but_concise
+recommended_next_route:
+  - authorized_status_file_update
+  - pdf_figure_table_image_manual_review
+  - candidate_cleanup_or_research_refresh_or_template_review
+codex_self_assessment:
+  standalone_trust: insufficient
+  corroborated_by_independent_checks: true
+  accepted_final_status: PASS
+```
```

### detail_report_check

- exit_code: `0`

```text
1:# MNEMOSYNE-032 Independent Verification Detail Report
7:- final_verdict: `PASS`
207:invalid_test_triggered: false
208:blocking_issues: []
```

### active_check

- exit_code: `0`

```text
5:MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 dry-run independent verification 已完成，final verdict 为 PASS。当前等待用户选择下一路线：PDF 图表复核、Idea Capture Buffer / candidate cleanup、template review / small fixes 或 memory-system testing/debugging feasibility research。
88:- MNEMOSYNE-032 dry-run independent verification：final verdict `PASS`；invalid_test_triggered=false；blocking_issues=[]；dry-run artifacts remain validation evidence, not execution source or final design.
```

### handoff_check

- exit_code: `0`

```text
91:## MNEMOSYNE-032 dry-run independent verification status
94:- Final independent verdict: `PASS`.
99:- Status files were intentionally not updated by the dry-run itself because status updates were outside the dry-run permission scope; MNEMOSYNE-032F records the authorized status update.
```

### todo_check

- exit_code: `0`

```text
71:- [x] MNEMOSYNE-032 first dry-run intake and independent verification PASS；
118:## MNEMOSYNE-032 dry-run independent verification
122:- [x] Final independent verdict recorded as `PASS`.
```

### open_questions_check

- exit_code: `0`

```text
35:   - 状态：answered；是否小修见 open 区域。
43:    - 状态：answered；是否小修见 open 区域。
47:    - 状态：answered；是否小修见 open 区域。
67:   - 状态：answered；motivation 已在 MNEMOSYNE-031 R1 由用户选择 B 接受，并保留 review notes。
71:    - 状态：answered；pro prompt 文件已放入约定路径。
75:    - 状态：answered。
79:    - 状态：answered；MNEMOSYNE-030G-MANUAL 用于手工修正 030F 后仍残留的状态不同步。
83:    - 状态：answered。
87:    - 状态：answered；用户重述不是原始需求、最终设计或执行源。
89:24. MNEMOSYNE-032 dry-run independent verification verdict 是什么？
90:    - 结论：PASS。
92:    - 状态：answered；dry-run artifacts remain validation evidence only, not execution source and not final design.
135:    - 状态：answered；R4B 已完成 9 个 main records + 1 个 addendum。
137:    - 状态：answered；R4C synthesis candidate draft 已生成，且不是执行源。
139:    - 状态：answered；final writeback checkpoint 已生成，final D-01 to D-07 决策以 research review record 为准。
```

### decision_log_check

- exit_code: `0`

```text
312:- MNEMOSYNE-032F 追加记录：记录并接受 MNEMOSYNE-032 dry-run independent verification 的 final verdict 为 `PASS`；状态：accepted_for_status_tracking；边界：不修改 `current/human-approved-spec.md`，不把 dry-run artifact 升格为 execution source，且不代表 PDF figure/table/image/layout 已完成人工复核。
342:## DEC-0051
```

### protected_human_spec_check

- exit_code: `1`

```text
(no output)
```

### forbidden_files_check

- exit_code: `1`

```text
(no output)
```

## protected_file_confirmation

- `current/human-approved-spec.md` was not modified.
- Research report originals were not modified.
- Prompt originals were not modified.
- PDF files were not modified.
- `AGENTS.md` and `CLAUDE.md` were not created or modified.
- GitHub Actions / automation files were not created or modified.

## known_gaps_or_followups

- TASK_STATUS: verification_passed
- MNEMOSYNE-032 dry-run independent verification final verdict `PASS` has been recorded in status files.
- Dry-run artifacts remain validation evidence only, not execution source and not final design.
- Current execution source remains `current/human-approved-spec.md`.
- Recommended next route remains user-selected, with PDF figure/table/image manual review still a major evidence-layer gap.
