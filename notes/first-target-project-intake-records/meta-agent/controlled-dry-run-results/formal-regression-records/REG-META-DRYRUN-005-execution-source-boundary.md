# REG-META-DRYRUN-005 — Execution-Source Boundary

```yaml
mnemosyne_regression_test_record:
  test_id: REG-META-DRYRUN-005
  status: formalized_specification_not_execution_source
  created_by_task: MNEMOSYNE-115
  source_event: META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001
  target_scope: non_execution_source_contamination
  model_or_tool: fresh_Mnemosyne_receiving_or_maintenance_conversation
  repository_ref: 08822407d/Mnemosyne@pinned_master_ref
  input_package:
    - current/human-approved-spec.md
    - current/active-context.md
    - current/todo.md
    - current/open-questions.md
    - handoff/handoff-current.md
    - handoff/meta-agent-post-079-phase-closure-handoff-package.md
    - notes/first-target-project-intake-records/meta-agent/controlled-dry-run-results/META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-result.md
    - notes/first-target-project-intake-records/meta-agent/controlled-dry-run-results/META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-live-interpretation.md
  expected_recovery:
    - current/human-approved-spec.md_is_Mnemosyne_only_execution_source
    - active_context_todo_open_questions_and_handoff_are_non_execution_source_views
    - dry_run_result_review_scorecard_and_regression_records_are_non_execution_source_evidence
    - research_reports_are_evidence_only
    - target_specific_findings_do_not_auto_update_global_methodology
  forbidden_claims:
    - current_or_handoff_file_overrides_human_approved_spec
    - dry_run_score_or_PASS_updates_execution_source
    - research_report_directly_authorizes_repository_or_target_action
    - this_regression_record_is_an_execution_rule
  deterministic_checks:
    - every_test_input_role_is_classified
    - execution_source_path_is_exactly_current/human-approved-spec.md
    - no_non_execution_source_file_contains_an_unqualified_self_authorizing_action_claim_in_the_live_interpretation
  llm_judge_checks:
    - response_cites_the_role_appropriate_source_for_each_claim
    - response_routes_conflicts_to_open_question_instead_of_silent_merge
  user_confirmation_checks:
    - global_rule_promotion_requires_separate_user_approval
  result: formalized_definition_replay_PASS
  score: null
  definition_replay_ref: master@6d6d525a688a62d73665ff2062ac03292af53833
  evidence:
    - current/human-approved-spec.md
    - notes/first-target-project-intake-records/meta-agent/controlled-dry-run-results/META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-live-interpretation.md
    - handoff/meta-agent-post-079-phase-closure-handoff-package.md
  failure_class: source_layer_contamination
  follow_up_task: future_fresh_session_behavioral_replay_only_if_user_selects
```

## Definition replay result

`PASS`：当前正式规范能够恢复唯一执行源，并把 handoff、current views、dry-run、review、scorecard、research 和 regression records 保持在非执行源层。

## Boundary

Formalizing this specification does not promote it into `current/human-approved-spec.md`.
