# Frontier Clarification Validation — Staged Fable5 Research Plan v0.2

> Non-execution-source research planning record. It supersedes v0.1 for task delivery and lifecycle only. It does not run Fable5, spend quota, accept a report, modify the validation package or authorize V0/V1.

```yaml
plan_id: FABLE5-FRONTIER-CLARIFICATION-VALIDATION-STAGED-PLAN-001
version: 0.2.0
created_by_task: MNEMOSYNE-184
supersedes_delivery_and_operator_sections_of: notes/research-plans/2026Q3-frontier-clarification-validation-fable5-staged-plan-v0.1.md
status: stage_A_ready_queue_prepared_not_executed_stage_B_topics_deferred
source_package: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
source_package_merge_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830
manual_candidate_merge_commit: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
foundational_Pro_research: complete_adjudicated
foundational_Fable_research: complete_adjudicated_no_rerun
additional_foundational_same_topic_research: not_needed
post_package_independent_review: recommended
quota_execution_authority: user_only
```

## 1. Unchanged research rationale

The original broad architecture question has already been independently researched and adjudicated. The two current tasks review concrete artifacts created afterward:

1. the complete validation package;
2. the manual multi-conversation surface candidate.

The research questions and allowed dispositions remain unchanged from v0.1. This revision fixes how the tasks are delivered to Claude/Fable5 and how completed tasks leave the operator queue.

## 2. Product-access correction

```yaml
Claude_access_model:
  Project_Files:
    scope: persistent_across_Project_chats
    use_for_current_independent_tasks: not_preferred
    whole_Mnemosyne_repository: do_not_add
  chat_plus_GitHub:
    scope: current_chat
    preferred_for_current_tasks: true
    exact_path_read_receipts: required
  Project_membership_alone_grants_repository_access: false
  visible_repository_link_proves_file_reads: false
```

Official documentation currently describes file/folder selection for both chat and Project GitHub integration. The user's current chat UI instead describes linking a repository and branch for on-demand connector reads. The workflow supports both and requires an empirical same-chat preflight before Research starts.

## 3. Independent-run environment

```yaml
Stage_A_environment:
  preferred:
    - fresh_standalone_Claude_chat
    - new_one_run_Project_with_no_prior_chats_and_empty_Project_Files
  existing_Mnemosyne_复合评审_Project:
    use_for_independent_Stage_A: not_recommended
    reason:
      - Project_Memory_present
      - prior_chats_present
      - avoidable_framing_dependency
  visible_model: Fable_5
  visible_effort: Max
  exact_backend_identity: unknown_or_not_attestable
  Research_during_connector_preflight: false
  Research_after_preflight: enabled_by_user
  repository_write: prohibited
```

A1 and A2 must use separate clean chats or one-run Projects. Neither sees the other task or report before completion.

## 4. Stage A ready tasks

### A1 — Validation-package adversarial audit

```yaml
task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
canonical_task: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
operator_entrypoint: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/OPERATOR.md
input_manifest: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
decision_it_can_change:
  - proceed_to_surface_selection_without_package_revision
  - revise_condition_contracts_scenarios_keys_rubric_or_result_semantics
  - major_redesign_before_V0
  - stop_and_retain_historical_design_only
mandatory_repository_set:
  - complete_15_file_validation_package_folder
  - source_validation_design
  - cross_report_adjudication
  - interim_architecture_and_validation_decision
preferred_selection_actions:
  - select_or_link_repository_at_chat_level
  - if_file_browser_is_used_select_the_complete_package_folder_plus_three_external_files
whole_repository_Project_Files_required: false
```

### A2 — Manual-surface isolation and provenance threat model

```yaml
task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
canonical_task: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
operator_entrypoint: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/OPERATOR.md
input_manifest: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
decision_it_can_change:
  - prepare_and_verify_manual_V0_preflight
  - revise_manual_candidate
  - prefer_API_or_runtime_preparation
  - defer_or_stop_surface_route
mandatory_repository_set:
  - manual_surface_candidate
  - exact_9_file_validation_package_subset
  - current_human_approved_spec
preferred_selection_actions:
  - select_or_link_repository_at_chat_level
  - if_file_browser_is_used_select_only_manifest_paths
whole_repository_Project_Files_required: false
```

## 5. Access gate for both tasks

The operator must run a preflight in the same chat with Research off:

```yaml
required_preflight:
  reads:
    - ready_task_entrypoint
    - input_manifest
    - canonical_task
    - first_primary_audit_object
  return:
    - exact_paths
    - complete_read_true_or_false
    - visible_artifact_ID_or_heading
    - branch_or_ref_observed
    - access_limitations
  pass_requires:
    - all_minimum_paths_complete
    - expected_task_and_artifact_IDs_visible
    - no_write_action
  visible_repository_link_alone: insufficient
```

The complete research task then performs its own mandatory-file gate. If any required file is missing, truncated, mismatched or not reliably bound, the run stops before analysis.

## 6. Access fallbacks

```yaml
fallback_order:
  - chat_level_on_demand_connector
  - explicit_file_or_folder_selection
  - new_one_run_Project_with_only_manifest_listed_content
  - exact_manual_upload_set
```

Do not add the whole repository. For A1, select the entire package folder plus three external files rather than manually browsing every package file. For A2, select only the manifest-listed subset.

Manual upload is last resort. A1's minimum upload set is 19 files and is close to the current per-chat upload count; use connector or folder selection whenever possible. A2's minimum set is 12 files.

## 7. Independence and contamination controls

```yaml
prohibited_inputs:
  - foundational_Pro_report
  - foundational_Fable_report
  - the_other_Stage_A_task_or_report
  - unrelated_Project_Memory
  - old_Mnemosyne_chats
  - maintainer_preferred_disposition_not_named_by_the_task
  - unrelated_repository_files
```

The existing package's hidden-author-key file is an intentional audit object for A1/A2 where listed. It must not be confused with hidden material from another validation campaign.

## 8. Stage A return and adjudication

Each final response must contain the complete report body and record:

- exact task ID and topic;
- exact visible model and effort text;
- access mode and repository-read receipts;
- any branch/commit attestation limitation;
- any fallback or quota warning;
- complete source table and report sections required by the canonical task;
- no GitHub write.

Reports return independently to the current Mnemosyne frontier-clarification validation route. They do not become authority automatically. The maintainer must perform input-integrity, source-role, evidence-calibration, cross-report and package-impact review before any amendment or surface decision.

## 9. Stage B remains conditional

The four v0.1 Stage B topics remain unchanged and non-runnable:

```yaml
Stage_B:
  FABLE5_FCV_REVIEWER_INDEPENDENCE_001:
    ready_to_run: false
    trigger: Stage_A_or_selected_reviewer_arrangement_creates_a_decision_relevant_question
  FABLE5_FCV_V1_INFERENCE_AND_THRESHOLDS_001:
    ready_to_run: false
    trigger: package_audit_resolved_and_surface_verified_before_V1
  FABLE5_FCV_EVIDENCE_EQUIVALENCE_001:
    ready_to_run: false
    trigger: selected_surface_lacks_default_proof_and_exception_is_actually_considered
  FABLE5_FCV_PORTABILITY_AND_PROPAGATION_001:
    ready_to_run: false
    trigger: valid_V1_evidence_and_specific_target_owner_request
```

No Stage B ready directory is created until its trigger occurs and the task is re-authored against the then-current artifacts.

## 10. Ready queue and completed-task lifecycle

```yaml
operator_queue: handoff/fable5-ready/
ready_task_required_files:
  - task.md
  - OPERATOR.md
  - input-manifest.yaml
completed_task_handling:
  - archive_original_task_under_raw/research-reports/cycles/<cycle>/tasks/
  - archive_report_or_receipt_under_same_cycle
  - update_cycle_manifest_and_current_status
  - remove_ready_task_directory
  - leave_only_non_runnable_registry_redirect_if_needed
retired_unexecuted_handling:
  - remove_ready_task_directory
  - record_retirement_reason_in_non_runnable_plan_or_record
```

`notes/research-prompts/` is not the operator discovery surface. A detailed old prompt may remain for history or redirection but is not runnable without a matching ready-queue entry.

## 11. Quota discipline

```yaml
quota_recommendation:
  high_value_tasks_ready_now: 2
  execute_now_if_user_chooses: 0_to_2
  conditional_reserve: 4
  automatically_spend_all_available_runs: false
  next_task_generation_gate: Stage_A_reports_received_and_adjudicated
```

## 12. Capability and research assessment

```yaml
capability_assessment:
  task_and_delivery_redesign: FRONTIER_RECOMMENDED
  operator_connector_preflight: NEXT_TIER_SUFFICIENT_CANDIDATE_or_human
  static_Fable5_audit: FRONTIER_RECOMMENDED_INDEPENDENT_ROLE
  exact_path_and_manifest_checks: MECHANICAL_ONLY
  report_adjudication_and_package_amendment: FRONTIER_RECOMMENDED

additional_Pro_Deep_Research:
  status: NOT_NEEDED
additional_foundational_Fable_research:
  status: NOT_NEEDED
Fable5_Stage_A:
  status: RECOMMENDED_AFTER_READY_QUEUE_MERGE
```

## 13. Safe next action

```yaml
safe_next_action:
  - review_and_merge_the_MNEMOSYNE_184_delivery_redesign_PR_or_request_changes
  - after_merge_user_may_run_A1_and_A2_in_separate_clean_Fable5_Max_runs
  - return_complete_reports_for_repository_bound_adjudication
  - freeze_no_Stage_B_task_until_Stage_A_disposition
  - keep_surface_V0_and_V1_unselected
```

No research result or validation evidence has been generated by this plan.
