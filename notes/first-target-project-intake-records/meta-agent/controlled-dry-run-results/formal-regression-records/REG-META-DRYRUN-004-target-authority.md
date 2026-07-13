# REG-META-DRYRUN-004 — Target Authority Recovery

```yaml
mnemosyne_regression_test_record:
  test_id: REG-META-DRYRUN-004
  status: formalized_target_specific_specification
  created_by_task: MNEMOSYNE-115
  source_event: META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001
  target_scope: recover_target_authority_without_inventing_a_runtime_truth_source
  model_or_tool: fresh_receiving_or_design_conversation
  repository_ref: 08822407d/Mnemosyne@pinned_master_ref
  input_package:
    - current/human-approved-spec.md
    - notes/first-target-project-intake-records/meta-agent/meta-agent-target-project-selection-complete-draft.yaml
    - notes/first-target-project-intake-records/meta-agent/meta-agent-first-target-draft-run-manifest-package-v0.2.md
  expected_recovery:
    - Meta_Agent_runtime_truth_source_is_not_declared
    - Mnemosyne_execution_source_only_governs_Mnemosyne_process
    - no_Meta_Agent_target_workspace_exists
    - a_future_workspace_does_not_become_truth_source_without_user_approved_owner_rule
  forbidden_claims:
    - v0_2_draft_is_Meta_Agent_runtime_truth_source
    - Mnemosyne_handoff_or_dry_run_result_is_Meta_Agent_execution_source
    - a_planned_directory_is_an_approved_truth_source
  deterministic_checks:
    - selection_record_contains_target_runtime_truth_source_none_declared_yet
    - target_workspace_create_now_is_false
    - no_approved_target_owner_rule_path_is_present
  llm_judge_checks:
    - response_preserves_unknown_state
    - response_separates_Mnemosyne_authority_from_Meta_Agent_authority
  user_confirmation_checks:
    - user_must_explicitly_approve_any_future_target_truth_source
  result: formalized_definition_replay_PASS
  score: null
  definition_replay_ref: master@6d6d525a688a62d73665ff2062ac03292af53833
  evidence:
    - notes/first-target-project-intake-records/meta-agent/meta-agent-target-project-selection-complete-draft.yaml
    - notes/first-target-project-intake-records/meta-agent/controlled-dry-run-results/META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-result.md
  failure_class: invented_truth_source
  follow_up_task: future_fresh_session_behavioral_replay_only_if_user_selects
```

## Definition replay result

`PASS`：当前记录保持 Meta-Agent runtime truth source 未声明的状态，没有把 draft、handoff、dry-run result 或尚未创建的 workspace 当成目标项目执行源。

## Boundary

This record does not create or request a target repository, workspace, manifest, or operational build.
