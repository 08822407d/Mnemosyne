# First Target-Project Dry-Run Review Instruments

## Positioning and boundaries

- Positioning: non-execution-source review instrument package.
- This file is not execution source.
- This file is not a target-project delivery package.
- Use only for design-only first target-project dry-run preparation/review.
- Current Mnemosyne execution source remains `current/human-approved-spec.md`.
- The target project must eventually have its own execution source; Mnemosyne execution source is not the target runtime truth source.

## A. Minimal drift review checklist

Use this unified row format for every drift check:

```yaml
check_id:
result: pass | fail | unknown | not_applicable
expected_ref:
actual_ref:
evidence_paths:
blocking:
issue_id:
```

Minimum checks:

```yaml
- check_id: DRIFT-01-target-execution-source-valid
  result: unknown
  expected_ref: "Target execution source path and authority are identified, current, and safe to use."
  actual_ref:
  evidence_paths:
  blocking: yes
  issue_id:

- check_id: DRIFT-02-active-state-matches-project
  result: unknown
  expected_ref: "Active state, TODO/open items, and run artifacts match actual project state."
  actual_ref:
  evidence_paths:
  blocking: yes
  issue_id:

- check_id: DRIFT-03-owner-decisions-propagated
  result: unknown
  expected_ref: "Latest user/owner decisions are propagated to every required current-state or run artifact location."
  actual_ref:
  evidence_paths:
  blocking: yes
  issue_id:

- check_id: DRIFT-04-stale-information-marked
  result: unknown
  expected_ref: "Stale or superseded information is explicitly marked and not used as current fact."
  actual_ref:
  evidence_paths:
  blocking: yes
  issue_id:

- check_id: DRIFT-05-file-roles-justified
  result: unknown
  expected_ref: "Selected file roles, owner, and update trigger remain justified by target schema tailoring."
  actual_ref:
  evidence_paths:
  blocking: yes
  issue_id:

- check_id: DRIFT-06-privacy-tools-automation-valid
  result: unknown
  expected_ref: "Privacy boundary, tool capability, and automation assumptions are verified or marked unverified."
  actual_ref:
  evidence_paths:
  blocking: yes
  issue_id:

- check_id: DRIFT-07-handoff-next-step-clear
  result: unknown
  expected_ref: "Handoff still produces one clear executable next step with actor, input, output, and completion criterion."
  actual_ref:
  evidence_paths:
  blocking: yes
  issue_id:
```

Failure conditions:

- execution source, privacy boundary, or latest owner decision is `fail` or `unknown`;
- handoff conflicts with actual state;
- stale content is used as current fact;
- file roles increase without schema-tailoring rationale.

## B. Handoff executability checklist

Required replay record fields:

```yaml
replay_id:
fresh_session_confirmed:
allowed_input_files:
prior_conversation_context_available: no
target_and_scope_recovered:
execution_source_recovered:
non_execution_sources_recovered:
current_stage_recovered:
completed_and_pending_work_recovered:
constraints_and_stop_conditions_recovered:
next_action_and_actor_recovered:
evidence_path_for_each_answer:
clarifications_requested:
already_answered_question_repeated:
simulated_next_action:
result:
```

Failure conditions:

- hidden old conversation context is required;
- target execution source cannot be identified or explicitly marked unknown;
- already answered questions are repeated unnecessarily;
- next action has no actor/input/output/completion criterion;
- target write or unverified automation is proposed;
- critical recovery answers lack evidence paths.

## C. Source-priority conflict checklist

Required conflict record fields:

```yaml
conflict_id:
claim_or_topic:
source_a_path:
source_a_authority:
source_a_date_or_version:
source_b_path:
source_b_authority:
source_b_date_or_version:
declared_priority_rule_ref:
selected_source:
selection_reason:
losing_source_disposition: stale | superseded | evidence_only | candidate | unresolved
user_clarification_required:
evidence_paths:
result:
issue_id:
```

Failure conditions:

- no priority rule but a decision is made anyway;
- newer date is treated as higher authority by default;
- low-authority evidence overrides target execution source or owner decision;
- conflict is silently merged;
- Mnemosyne execution source is treated as the target project runtime truth source.

## D. Post-dry-run failure triage rubric

Severity:

- P0: safety leak, execution-source promotion error, unauthorized target write, repository/state damage; stop and contain immediately.
- P1: wrong source priority, non-executable handoff, critical decision not propagated, artifact not landable; must fix before next run.
- P2: naming/readability/redundancy/minor friction; may defer.

Primary cause classes:

- template_or_instrument_defect
- ordinary_model_execution_error
- user_input_or_policy_gap
- tool_or_platform_boundary
- target_specific_design_defect
- repository_state_sync_defect
- unknown

Routing rules:

- repeated structural defect -> Codex small fix
- missing owner/privacy/authority/completion definition -> user clarification
- new policy or execution-source change -> open question / separate user approval
- unverified design idea -> candidate
- current external platform capability dependency -> capability check, and only later targeted Deep Research if necessary
- target-specific issue -> keep in target design, do not upgrade to global Mnemosyne rule

Failure conditions:

- root cause is confirmed without evidence;
- every failure is blamed on model behavior;
- target-specific defect is promoted globally;
- P0 continues without containment.
