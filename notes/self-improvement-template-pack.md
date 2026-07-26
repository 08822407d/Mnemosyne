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

用于保存用户新构想、使用反馈、ChatGPT 阶段总结、Codex 任务结果、研究更新或目标项目反馈的原始输入。任何 original bytes/text 进入 Git 前，必须先完成 `notes/object-templates-and-id-rules.md` 中的 `repository_capture_safety_preflight`。

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
repository_capture_safety_preflight_ref:
repository_capture_safety_preflight_result_summary: pass | blocked | incomplete
content_storage:
  mode: repository_original | repository_redacted_excerpt | repository_safe_pointer | outside_git
  original_text: |
  original_file_ref:
  redacted_excerpt_ref:
  safe_external_pointer_ref:
  outside_git_reference:
context_notes:
sensitivity:
should_extract_candidate:
needs_research_evidence:
needs_human_review:
status:
```

字段提示：

- `source_type` 可为 `user_idea`、`usage_feedback`、`chatgpt_summary`、`codex_task_result`、`research_update`、`target_project_feedback` 等。
- `sensitivity` 保留为描述性 metadata，可先使用 `normal`、`private`、`confidential`、`unknown`；它不是 storage authorization，不能替代安全预检。
- `content_storage.mode` 必须且只能选择一个 route；非选中 route 的内容字段必须为空或省略。
- `repository_original` 只允许在 canonical preflight 为 `pass` 时填写 `original_text` 或 `original_file_ref`；`repository_redacted_excerpt` 和 `repository_safe_pointer` 只允许填写各自经过筛查的内容。
- `outside_git` 不得在本 Raw Input 中包含 original repository content，只能保存安全的 outside-Git reference 与必要 local summary。
- `repository_capture_safety_preflight_result_summary` 必须与 `repository_capture_safety_preflight_ref` 一致；不一致、unknown 或安全关键证据不完整时必须 fail closed。
- public 或 unknown repository visibility 采用 public-risk treatment；credentials / secrets 绝对阻断；后续删除不能消除 Git 历史暴露。
- `status` 可为 `captured`、`needs_extract`、`extracted`、`archived`。

说明：Raw Input 不是执行源；本模板不新增隐私 taxonomy。

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

## 5A. Repository action context 与 no-write evidence linkage

任何执行 repository action 或提出 no-write claim 的 ChatGPT、Codex 或 future-Agent result record，都应引用 `notes/object-templates-and-id-rules.md` 中的 canonical instances，而不是在本模板重复维护 permission / authority / risk 字段。

```yaml
repository_action_result_linkage:
  repository_action_context_refs: []
  repository_write_performed: true | false
  no_write_claimed: true | false
  no_write_evidence_ref:
  no_write_evidence_exception_refs: []
  repository_write_result_record_ref:
```

规则：

- `repository_write_performed: false` 本身不能证明 no write；
- `no_write_claimed: true` 时，`no_write_evidence_ref` 必须指向完整、surface-specific、与 exact scope 匹配的证据对象；
- `pass_with_approved_exception` 必须同时引用字段完整、已批准且 exact run / exact scope 匹配的 exception；
- 发生 write 时，每项不同 surface/action 都应有独立 `repository_action_context_ref`，并在 result record 中记录实际文件与 external action；
- 本 linkage 只前瞻性适用，不重写历史 result records。

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
- [ ] 若任务涉及 GitHub / connected-repository / target-store action，是否为每个 action surface 记录独立 `repository_action_context_ref`；
- [ ] 是否通过 canonical action context 分离 `platform_permission`、当前 task-local `mnemosyne_task_authority` 和 `action_risk`，而不是在本 checklist 重复字段；
- [ ] 写入前是否明确 repository/target、branch/ref、paths、protected paths、target workspace/material/write boundary 与 action type；
- [ ] 是否确认 persistent permission、approval card 或 action availability 未被当作未来任务授权；
- [ ] 若任务声称 no-write，是否列出明确 claim surfaces，并绑定 checked_at、proof actor/process、pinned refs、机械 evidence refs/commands、changed paths、scope-match 与 limitations；
- [ ] 若使用 run-scoped exception，是否完整记录 approval、exact run/scope、substitute evidence 与 `not_future_precedent: true`；
- [ ] 若创建 branch / PR，是否完成 single-active-PR lineage preflight 与创建 PR 前复检；
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
