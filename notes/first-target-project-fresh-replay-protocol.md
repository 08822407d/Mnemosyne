# First Target-Project Fresh Replay Protocol

## Positioning

- Positioning: non-execution-source verification protocol.
- Used to test startup/handoff executability.
- This protocol is not a dry-run result.
- This protocol is not execution source.

## Protocol metadata

- protocol_version: 2026-06-23-post-MNEMOSYNE-053
- replay_verdict_enum: `PASS | FAIL | BLOCKED`
- handoff_package_strategy: `notes/handoff-package-strategy-v0.1.md`
- reviewer_scorecard: `notes/handoff-replay-scorecard-v0.1.md`
- scoring_status: required_for_reviewed_gate_decision

## When to run

Run after:

- onboarding/read-order/protocol changes;
- current/handoff/startup changes that could affect onboarding;
- a prior replay failure;
- before the first real target-project dry-run;
- handoff package tier-definition changes;
- scorecard critical-check changes;
- provenance requirement changes;
- reviewed-verdict semantic changes.

Any change to the onboarding package, replay protocol, minimum read path, or critical result semantics invalidates the previous replay for that gate.

Completion of MNEMOSYNE-053 invalidates earlier replay evidence for the first-target dry-run gate. The next valid replay must use this protocol version and the maintainer scorecard review.

## Isolation requirements

- use a new ordinary Thinking-model conversation or another explicitly approved test environment;
- record the visible model/tool label and interface/session type;
- record memory/history setting when visible;
- record whether hidden prior context is expected as `yes | no | unknown`;
- the repository must be explicitly associated or the required files must be explicitly supplied;
- paste no prior Mnemosyne conversation content except the fixed replay prompt;
- known use of prior Mnemosyne conversation context invalidates isolation;
- `hidden_prior_context_expected: unknown` must be recorded as a limitation but does not automatically invalidate the test;
- read-only;
- no target selection;
- no target materials;
- no repository or target writes.

## Fixed replay prompt

Copy this prompt into a new ordinary Thinking-model conversation:

```text
加载 Mnemosyne 指导约束。

请执行当前版本的 first-target-project fresh startup/handoff replay。

严格边界：
1. 只读仓库；不要选择目标，不要请求或上传目标材料，不要启动真实 target-project dry-run，不要写仓库或目标项目。
2. 不要依赖旧对话记忆、平台隐式记忆或未提供的历史上下文作为事实依据。
3. 只根据当前可访问的授权仓库文件和 onboarding package 作答。
4. `current/human-approved-spec.md` 必须作为 Mnemosyne 唯一 execution source；若该文件不可访问，报告 `BLOCKED`。
5. 不要把 handoff、startup、active-context、research report、task result record、old conversation export 或 hidden platform memory 当 execution source。
6. 如果遇到缺失文件、冲突状态、过期指令、权限不明或工具能力不明，明确标记 `unknown` / `unsupported_assumption` / `stale`；不要自行补全。
7. 不得声称 real dry-run、target selection、target material ingestion、target repository write 或其他无当前证据的执行已经发生。
8. 下一动作只能是模拟、只读、验证或草拟，不得写入 target project。

输出：

replay_output:
  actual_files_read:
  execution_source:
  major_non_execution_boundaries:
  current_phase:
  current_gate:
  live_truths:
    real_target_project_dry_run_status:
    target_selection_status:
    target_material_status:
    target_repository_write_status:
  current_task_intent:
  completed_vs_pending:
  authorities_and_required_user_decisions:
  forbidden_actions:
  conflicts_or_missing_files:
  stale_or_historical_interference:
  unsupported_assumptions:
  one_simulated_safe_next_action:
  evidence_map:
    - claim:
      path:
      authority_level:
      freshness_note:
  limitations:
  claimed_replay_verdict: PASS | FAIL | BLOCKED

每项关键结论必须给出 repository evidence path。
受测会话的 claimed verdict 不是最终 reviewed verdict；维护对话将按 scorecard 独立复核。
```

## Replay result schema

```yaml
replay_record:
  replay_id:
  protocol_version:
  repository:
  tested_ref_or_commit:
  provenance:
    tested_at:
    source_conversation_or_task:
    target_conversation_or_task:
    tool_or_interface:
    visible_model_label:
    reasoning_effort_if_visible:
    repository_access_mode:
    memory_or_history_setting: off | on | unknown
    hidden_prior_context_expected: yes | no | unknown
    files_available:
    files_read:
    user_supplied_context:
    automation_level:
    limitations:

  executor_output:
    actual_files_read:
    execution_source_recovered:
    non_execution_sources_recovered:
    current_stage_recovered:
    current_gate_recovered:
    real_dry_run_status_recovered:
    target_selection_status_recovered:
    target_material_status_recovered:
    target_write_status_recovered:
    current_task_intent_recovered:
    completed_vs_pending_recovered:
    required_user_decisions_recovered:
    forbidden_actions_recovered:
    conflicts_or_missing_files:
    historical_state_interference:
    unsupported_assumptions:
    already_answered_question_repeated:
    simulated_next_action:
    evidence_map:
    limitations:
    claimed_replay_verdict: PASS | FAIL | BLOCKED

  maintainer_review:
    reviewer:
    reviewed_at:
    reviewed_against_ref:
    scorecard_version: v0.1
    critical_checks:
    dimension_scores:
    applicable_points:
    earned_points:
    normalized_score:
    quality_band: strong | usable_with_warnings | insufficient | not_scored
    stale_item_count:
    selected_historical_excerpt_count:
    token_tier_used: minimum | standard | extended | none
    authority_level_per_claim:
    executor_reviewer_discrepancies:
    warning_findings:
    critical_failures:
    reviewed_replay_verdict: PASS | FAIL | BLOCKED
    gate_recommendation:
```

## Verdict and scoring rules

The executor's claimed verdict is not the final reviewed verdict.

`BLOCKED` means the replay cannot be reliably evaluated because required access/files are unavailable, required canonical files are missing, or fresh-session isolation is invalid.

`FAIL` means the replay is evaluable but recovered incorrect or unsafe state, any critical check does not pass, or the normalized score is below 70.

`PASS` requires:

- a valid fresh-session test;
- required files discovered/read;
- correct execution source and non-execution boundaries;
- correct current phase/gate and live state;
- correct task intent, authority, approvals, and forbidden actions;
- unknown/stale/conflicting items labeled rather than invented;
- evidence paths supporting all critical answers;
- every critical scorecard check is `pass`;
- normalized score is at least 70;
- no actual write or target action.

Quality is recorded separately:

- `strong`: 85–100;
- `usable_with_warnings`: 70–84;
- `insufficient`: below 70;
- `not_scored`: blocked or not reliably scoreable.

For the first real target-project dry-run gate:

- `PASS + strong` may satisfy the replay quality requirement.
- `PASS + usable_with_warnings` requires explicit user acceptance of documented non-blocking warnings or repair before gate closure.
- `FAIL` and `BLOCKED` cannot close the gate.

Replay verdict remains separate from individual dry-run/check results, which use `pass | fail | unknown | not_tested | not_applicable`.

## Closeout and provenance

Required sequence:

```text
fresh replay output
→ user returns it to the ordinary Mnemosyne maintainer conversation
→ maintainer verifies verdict and evidence against latest master
→ if verified PASS, only a new reviewed Codex task may synchronize current state
→ if FAIL/BLOCKED, create issue entries and a bounded repair task
```

- The fresh replay session must not score or persist its own final reviewed PASS.
- The ordinary Mnemosyne maintainer conversation must compare executor output with latest master and complete `notes/handoff-replay-scorecard-v0.1.md`.
- Only a later reviewed Codex task may persist a verified replay record and synchronize current state.

Do not let a replay conversation write its own PASS into the repository.

Minimum provenance for a reviewed replay includes source type, tested ref/commit, verification scope, reviewer, date/time if available, and evidence paths checked against latest master.
