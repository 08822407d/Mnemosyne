# MNEMOSYNE-116 Result Record

```yaml
task_id: MNEMOSYNE-116
task_name: Require explicit Mnemosyne guidance refresh in handoffs and prepare fresh-session regression replay
task_type: execution_source_handoff_guidance_update_and_replay_preparation
action_actor: ChatGPT_GitHub_app
started_from:
  base_branch: master
  base_commit: bc4b4f098a0bcdd77cae731d59c51c79e5e8333f
  prerequisite_PR:
    number: 162
    merged: true
    merge_commit: bc4b4f098a0bcdd77cae731d59c51c79e5e8333f
branch: mnemosyne-116-handoff-guidance-and-fresh-replay-prep
user_decision_recorded: true
user_decision_provenance: current_maintenance_conversation_2026-07-13
approved_scope:
  - require_Mnemosyne_owned_handoff_packages_to_explicitly_instruct_receivers_to_execute_Load_Mnemosyne_guidance
  - require_target_project_business_handoffs_to_load_confirmed_project_specific_constraints_or_owner_rule
  - record_as_open_whether_target_project_business_conversations_should_also_load_Mnemosyne_guidance
  - load_Mnemosyne_guidance_in_the_current_conversation_without_replacing_the_current_task
  - continue_the_Meta_Agent_test_only_route_by_preparing_the_planned_fresh_session_behavioral_replay
not_approved_or_not_performed:
  - automatic_or_background_execution_of_a_fresh_conversation
  - claiming_the_current_non_fresh_conversation_completed_the_independent_replay
  - target_workspace_creation
  - target_material_ingestion
  - target_repository_write
  - operational_Meta_Agent_build
  - additional_regression_formalization
  - global_regression_rule_promotion
  - FABLE5_GREENFIELD_continuation
  - auto_merge
execution_source_modified: true
execution_source_section: current/human-approved-spec.md#15-交接与续接正确性原则
current_state_files_modified: true
handoff_behavior_guidance_modified: true
handoff_replay_files_created: true
formal_regression_definitions_modified: false
fresh_session_behavioral_replay_executed: false
target_workspace_created: false
target_materials_ingested: false
target_repository_written: false
operational_build_started: false
FABLE5_GREENFIELD_track_resumed_or_taken_over: false
auto_merge_authorized: false
```

## Summary

MNEMOSYNE-116 implements the user's explicit handoff-guidance decision and advances the Meta-Agent test-only route to the boundary that the current conversation can honestly complete.

The repository previously required a receiving conversation to read `README.md`, the execution source, the receive command, and the provided package. It did not explicitly require the handoff package to order a separate `Load Mnemosyne guidance` operation after receive. Therefore the new requirement is not a duplicate.

The task adds the settled rule to `current/human-approved-spec.md` §15 and aligns the operational prepare, receive, load, and startup guidance. It also records `HO-GUIDANCE-001`: target-project business conversations must load the target project's own confirmed constraints or owner rule, while the additional question of whether they should also load Mnemosyne guidance remains deliberately undecided.

The current maintenance conversation executed the Mnemosyne guidance refresh as behavior-constraint refresh only, preserved the Meta-Agent testing task, did not start another handoff, and did not import unrelated maintenance live state.

The next planned testing step requires a genuinely fresh conversation. This task therefore prepares a repository-backed replay package and startup prompt rather than falsely claiming fresh-session independence inside the current conversation.

## Execution-source update

`current/human-approved-spec.md` §15 now requires:

1. a Mnemosyne-owned handoff package to explicitly instruct the receiver to complete the handoff receive report, separately execute `Load Mnemosyne guidance` / `加载 MNEMOSYNE 约束指导`, and then continue the transferred task;
2. the guidance refresh to preserve the received task and not import unrelated maintenance live state;
3. target-project business handoffs to load the project's confirmed execution source, owner rule, or constraint guidance;
4. the additional Mnemosyne-guidance question for target-project business conversations to remain an open question rather than an assumed global answer.

The user decision is recorded by the current conversation instruction. No platform permission, historical authorization, or inferred preference is used as a substitute for that decision.

## Open question

Created:

- `current/handoff-guidance-open-question.md`

`HO-GUIDANCE-001` compares the risks and benefits of:

- loading only target-project constraints;
- loading target-project constraints plus a curated Mnemosyne common subset;
- loading full Mnemosyne guidance while prohibiting maintenance-route import.

No option is selected by this task.

## Guidance refresh performed in the current conversation

The current conversation reported:

```yaml
mnemosyne_guidance_refresh:
  operation: behavior_constraint_refresh
  current_conversation_task_preserved: true
  handoff_started: false
  maintenance_live_route_imported: false
  auto_handoff_detection_performed: false
  execution_source: current/human-approved-spec.md
```

This chat-level operation changed no repository state by itself. Repository changes in this task are the separately authorized branch and PR work documented here.

## Fresh-session replay preparation

Created:

- `handoff/meta-agent-regression-fresh-session-replay-package.md`
- `handoff/meta-agent-regression-fresh-session-replay-startup-prompt.md`

The package covers:

- `REG-META-DRYRUN-001` — approval-chain recovery;
- `REG-META-DRYRUN-002` — mechanical no-write proof and exception handling;
- `REG-META-DRYRUN-004` — target authority recovery without inventing a runtime truth source;
- `REG-META-DRYRUN-005` — execution-source boundary and non-execution-source contamination;
- `REG-META-DRYRUN-007` — PASS and PASS_WITH_WARNINGS semantics.

The package requires:

- an actually fresh ordinary ChatGPT conversation;
- explicit handoff receive followed by a separate Mnemosyne guidance refresh;
- a pinned `master` SHA after this PR is merged;
- independent recovery of each expected behavior from read-only repository evidence;
- mechanical before/after repository-state comparison;
- complete model/reviewer provenance;
- return of the result to the maintenance conversation;
- no final gate closure by the tested conversation.

No run-scoped exception is authorized if mechanical state comparison is unavailable. The tested run must then report `BLOCKED` or `INCOMPLETE`.

## Files created

- `current/handoff-guidance-open-question.md`
- `handoff/meta-agent-regression-fresh-session-replay-package.md`
- `handoff/meta-agent-regression-fresh-session-replay-startup-prompt.md`
- `notes/codex-task-results/MNEMOSYNE-116-result.md`

## Files modified

- `current/human-approved-spec.md`
- `commands/load-mnemosyne-guidance.md`
- `commands/prepare-mnemosyne-handoff.md`
- `commands/receive-mnemosyne-handoff.md`
- `handoff/startup-instructions.md`
- `current/meta-agent-test-route-status.md`
- `current/review-and-validation-status.md`
- `notes/first-target-project-intake-records/meta-agent/controlled-dry-run-results/formal-regression-records/README.md`

## Package preflight

The current maintenance conversation checked that the replay package:

- explicitly separates handoff receive from guidance refresh;
- uses all five formal regression paths from merged MNEMOSYNE-115;
- forbids repository and target-project writes;
- requires pinned before/after repository-state evidence;
- preserves unknown Meta-Agent runtime truth-source status;
- prevents PASS from becoming authority;
- prevents current/handoff/research/replay records from becoming execution source;
- assigns final gate ownership to the maintenance conversation.

Result:

```yaml
replay_package_definition_and_boundary_preflight:
  result: PASS
  evidence_class: same_conversation_package_review
  independence_limitation: not_the_fresh_session_behavioral_replay
```

## Verification

- Repository visibility was verified as public before writes.
- PR #162 was verified merged before this task began.
- A new branch was created from the merged `master` before the first write.
- Every repository write explicitly targeted `mnemosyne-116-handoff-guidance-and-fresh-replay-prep`.
- Pre-result compare reported `ahead_by: 13`, `behind_by: 0`, and 11 changed files in the intended execution-source, command, current-status, handoff-package, and regression-index scope.
- `current/human-approved-spec.md` changed only in §15 for the two user-approved handoff-guidance bullets, apart from the adjacent preserved formatting boundary.
- Official MNEMOSYNE-082/083 artifacts, target-workspace paths, target-material paths, target repositories, build paths, and FABLE5-GREENFIELD files are absent from the changed-file set.
- A final compare after this result record is created will be recorded in the PR body.

## Known limitations

- The independent behavioral replay has not yet been executed because the current conversation is not fresh.
- The package preflight was performed by the same maintenance conversation that created it.
- The new execution-source and operational guidance changes do not become `master` state until the MNEMOSYNE-116 PR is merged.
- The target-project-business-conversation question remains open by design.

## Boundary

MNEMOSYNE-116 updates only Mnemosyne handoff/continuation guidance and prepares a read-only regression replay. It does not build Meta-Agent, create a target workspace, ingest target materials, write a target repository, start an operational build, execute or auto-schedule the fresh replay, promote regressions globally, continue FABLE5-GREENFIELD, or authorize auto-merge.