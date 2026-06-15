# Self-Improvement Template Pack / 自我改进模板包

## 文件定位

本文件为 Mnemosyne 自我改进流程提供可复制模板，用于规范 raw 输入、候选需求、冲突检查、用户决定、任务结果、阶段总结、研究 refresh、目标项目反馈、open question、TODO、应用检查和最小运行流程。

本文件不是执行源。

当前执行源仍是：

- `current/human-approved-spec.md`

模板填写结果需要经过用户确认后，才可能更新执行源。若本文件与 `current/human-approved-spec.md` 冲突，以 `current/human-approved-spec.md` 为准，并登记 open question。

## 使用原则

- 模板用于记录、整理和审计，不自动执行任何仓库更新。
- raw、candidate、conflict check、decision record、task result、stage summary、research intake、feedback、open question 和 TODO 条目本身都不是执行源。
- 是否更新 `current/human-approved-spec.md` 必须由用户确认。
- 涉及研究证据、工具能力边界或自动化可行性时，应按需回查 research current 视图。

## 1. Raw Input Entry Template

用于保存用户新构想、使用反馈、ChatGPT 阶段总结、Codex 任务结果、研究更新或目标项目反馈的原始输入。

```yaml
raw_id:
source_type:
source_ref:
created_at:
language:
author_or_origin:
input_type:
related_task_id:
related_project:
original_text: |
context_notes:
sensitivity:
should_extract_candidate:
needs_research_evidence:
needs_human_review:
status:
```

字段提示：

- `source_type` 可为 `user_idea`、`usage_feedback`、`chatgpt_summary`、`codex_task_result`、`research_update`、`target_project_feedback` 等。
- `sensitivity` 可先使用 `normal`、`private`、`confidential`、`unknown`。
- `status` 可为 `captured`、`needs_extract`、`extracted`、`archived`。

说明：Raw Input 不是执行源。

## 2. Candidate Requirement Template

用于从 raw / task result / feedback 中抽取候选需求。

```yaml
candidate_id:
title:
source_refs:
status:
requirement_type:
summary:
rationale:
affected_files:
affected_workflows:
proposed_change:
conflict_check_required:
research_evidence_required:
user_decision_required:
reflected_in:
notes:
```

状态可包括：

- `pending`
- `reflected`
- `rejected`
- `deferred`
- `merged`
- `superseded`

说明：Candidate Requirement 不是执行源。

## 3. Similarity / Conflict Check Template

用于检查新候选是否与已有需求、spec、decision、todo、open question 或 research evidence 冲突。

```yaml
check_id:
candidate_refs:
checked_against:
duplicate_of:
similar_to:
conflicts_with:
refines:
supersedes:
evidence_refs:
risk_level:
recommended_user_options:
unresolved_questions:
checker_notes:
```

字段提示：

- `checked_against` 应列出实际检查过的文件或记录。
- `risk_level` 可为 `low`、`medium`、`high`、`unknown`。
- `recommended_user_options` 应给出可选动作，而不是替用户决定。

说明：Similarity / Conflict Check 不是执行源。

## 4. User Decision Record Template

用于记录用户对候选需求的决定。

```yaml
decision_record_id:
candidate_refs:
user_decision:
decision_options_presented:
selected_option:
user_original_words: |
effective_change:
files_to_update:
should_update_human_approved_spec:
should_update_todo:
should_update_open_questions:
should_update_decision_log:
should_update_active_context:
should_update_handoff:
notes:
```

可选 `user_decision`：

- `accept`
- `refine`
- `merge`
- `replace`
- `keep_parallel`
- `keep_candidate`
- `defer`
- `reject`
- `needs_research`
- `needs_human_review`

说明：用户决定记录本身不是执行源；只有同步到 `current/human-approved-spec.md` 后才成为执行规则。

## 5. Codex Task Result Record Template

用于记录 Codex 任务结果。

默认路径占位符：

`notes/codex-task-results/TASK_ID-result.md`

实际任务应将 `TASK_ID` 替换为真实任务编号。

```yaml
task_id:
task_name:
codex_task_context:
files_created:
files_modified:
files_not_modified:
claimed_completion:
actual_git_status_short:
actual_git_diff_stat:
actual_git_diff_name_only:
targeted_diff_hunks_or_summary:
stale_phrase_or_presence_checks:
protected_file_check:
actual_diff_summary:
claim_vs_diff_consistency:
codex_summary:
known_gaps:
manual_review_required:
follow_up_tasks:
limits_or_uncertainties:
whether_task_claims_completion:
verification_notes:
reviewer_notes:
```

说明：

- Codex Task Result Record 不是执行源。
- 最终判断以 Git diff、仓库文件、用户 review 和必要验证为准。
- 如果 Codex 声称完成但文件未实际修改，应记录偏差。
- 文件修改类 Codex 任务应要求 `git status --short`、`git diff HEAD --stat`、`git diff HEAD --name-only` 和关键目标文件 diff。
- 多文件、高风险、清理 stale text 或入口状态修复任务，优先使用 exact replacement blocks 或 patch script。
- 任务结果必须比较 intended files 与 actual changed files，不能只保存 Codex prose summary。

## 6. ChatGPT Stage Summary Template

用于保存 ChatGPT 对话阶段性总结或 handoff。

```yaml
summary_id:
source_conversation:
created_at:
scope:
current_stage:
confirmed_decisions:
confirmed_requirements:
current_open_questions:
current_todo:
key_files:
risks_or_uncertainties:
next_recommended_step:
should_update_active_context:
should_update_handoff:
should_create_raw:
notes:
```

说明：Stage Summary 不是执行源。

## 7. Research Refresh Intake Template

用于处理新的研究报告、季度 refresh、ad-hoc research cycle 或工具能力更新。

```yaml
research_intake_id:
cycle_id:
report_refs:
trigger_reason:
affected_capability_boundaries:
affected_design_principles:
possible_superseded_evidence:
needs_delta_report:
needs_current_evidence_map_update:
needs_capability_boundaries_update:
needs_human_approved_spec_review:
notes:
```

说明：研究报告是证据层，不是执行源。

## 8. Target Project Feedback Template

用于目标项目使用 Mnemosyne 交付包后的反馈回流。

```yaml
feedback_id:
target_project:
delivery_package_ref:
feedback_source:
feedback_type:
original_feedback: |
affected_memory_schema:
affected_delivery_workflow:
should_update_mnemosyne:
should_update_target_project_package:
candidate_refs:
decision_required:
notes:
```

说明：Target Project Feedback 不是执行源；是否影响 Mnemosyne 或目标项目运行文件，需要用户确认和后续应用步骤。

## 9. Open Question Template

用于把未决问题登记到 `current/open-questions.md` 或后续专门文件。

```yaml
open_question_id:
question:
source_refs:
why_unresolved:
options:
evidence_needed:
decision_owner:
priority:
blocking_status:
next_review_trigger:
notes:
```

说明：Open Question 不是执行源；它用于标记需要后续决策、证据或人工 review 的事项。

## 10. TODO Item Template

用于把未来事项登记到 `current/todo.md` 或后续专门文件。

```yaml
todo_id:
title:
source_refs:
category:
priority:
blocking_status:
target_phase:
expected_output:
dependencies:
notes:
```

说明：TODO Item 不是执行源；它用于排期和追踪未来工作。

## 11. Apply Result Checklist

用于把用户确认后的结果应用到仓库。

检查项：

- [ ] 是否需要更新 `current/human-approved-spec.md`；
- [ ] 是否需要更新 `current/todo.md`；
- [ ] 是否需要更新 `current/open-questions.md`；
- [ ] 是否需要更新 `notes/decision-log.md`；
- [ ] 是否需要更新 `notes/candidate-requirements.md`；
- [ ] 是否需要更新 `current/active-context.md`；
- [ ] 是否需要更新 `handoff/handoff-current.md`；
- [ ] 是否需要更新 `handoff/startup-instructions.md`；
- [ ] 是否需要更新 research evidence current 视图；
- [ ] 是否需要创建 task result record；
- [ ] 如果是 Codex 文件修改任务，是否要求 `git status --short`、`git diff HEAD --stat`、`git diff HEAD --name-only`；
- [ ] 是否要求关键目标文件的 targeted diff；
- [ ] 是否要求 grep/rg 检查旧文字删除或新文字存在；
- [ ] 是否确认 protected files 未修改；
- [ ] 是否需要用户最终 review。

说明：Apply Result Checklist 是人工检查清单，不是自动执行系统。

## 12. Minimal Self-Improvement Runbook

最小操作流程：

1. Capture：保存原始输入。
2. Extract：抽取候选需求。
3. Compare：查重和冲突检查。
4. Present：向用户呈现决策选项。
5. Apply：根据用户确认更新对应文件。
6. Refresh：更新 active-context / handoff / todo。
7. Record：记录 Codex / ChatGPT 任务结果。
8. Review：用户 review。
9. Commit：提交并合并。
10. Verify：必要时核实实际文件状态。

说明：Runbook 描述人工/半自动工作顺序，不创建自动执行链路，也不替代 `current/human-approved-spec.md`。
