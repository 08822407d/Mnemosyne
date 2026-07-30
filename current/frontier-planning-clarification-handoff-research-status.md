# Frontier Planning, Clarification Handoff, and Research-Trigger Status

> Non-execution-source live status. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
status_id: FRONTIER-PLANNING-CLARIFICATION-HANDOFF-RESEARCH-STATUS-006
created_by_task: MNEMOSYNE-178
last_status_task: MNEMOSYNE-184
source_guard: current/user-operation-next-step-capability-and-intent-guard.md
adjudication_guard: current/frontier-planning-clarification-handoff-adjudication-guard.md
delivery_correction_guard: current/deep-research-report-delivery-correction-guard.md
source_cycle: RC-2026Q3-frontier-planning-clarification-handoff
validation_design: notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md
complete_validation_package: notes/frontier-clarification-validation-package/README.md
validation_package_merge_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830
post_package_Fable5_plan: notes/research-plans/2026Q3-frontier-clarification-validation-fable5-staged-plan-v0.2.md
Fable5_delivery_workflow: notes/research-operations/claude-project-github-and-fable5-delivery-v0.1.md
Fable5_ready_queue: handoff/fable5-ready/
canonical_delivery_PR: pending_creation_by_MNEMOSYNE_184
rejected_predecessor_PR:
  PR: 235
  merged: false
  adopted: false
status: foundational_research_complete_package_merged_and_Fable5_delivery_redesign_prepared_not_executed
execution_source: current/human-approved-spec.md
execution_source_modified: false
foundational_Pro_research_executed: true
foundational_Fable_research_executed: true
foundational_reports_adjudicated: true
additional_foundational_same_topic_research_recommended: false
post_package_independent_Fable5_review_recommended: true
post_package_Fable5_executed: false
controlled_validation_selected: false
controlled_validation_completed: false
target_project_propagation_authorized: false
```

## 1. Closed foundational research cycle

```yaml
foundational_research:
  Pro:
    task: PRO-DR-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001
    disposition: ACCEPT_WITH_CORRECTIONS_AS_PRIMARY_NON_EXECUTION_SOURCE_EVIDENCE
  Fable:
    task: FABLE5-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001
    disposition: ACCEPT_WITH_CORRECTIONS_AS_INDEPENDENT_ADVERSARIAL_NON_EXECUTION_SOURCE_EVIDENCE
    rerun_required: false
  cross_report_adjudication: complete
  additional_broad_architecture_research: not_needed
```

Do not rerun or lightly rephrase the completed foundational questions. Completed redirects under `notes/research-prompts/` are not runnable tasks.

## 2. Adjudicated architecture state

```yaml
adjudication:
  universal_clarification_default: rejected
  direct_frontier: required_for_high_impact_low_clarity
  structured_owner_package: available_route
  next_tier_interviewer: validation_gated_candidate
  gated_mixed_escalation: preferred_validation_candidate_for_mixed_impact
  research_first: decision_relevant_external_fact_gaps_only
  human_retains_surface_quota_and_execution_authority: true
```

No research report is target truth or execution source.

## 3. Post-research artifacts under audit

```yaml
merged_validation_package:
  package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-PACKAGE-001
  version: 0.1.0
  merge_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830
  public_synthetic_scenarios: 14
  V1_smoke_scenarios: 8
  conditions: 5
  V1_primary_cells: 40
manual_surface_candidate:
  candidate_id: FRONTIER-CLARIFICATION-VALIDATION-MANUAL-SURFACE-CANDIDATE-001
  version: 0.1.0
  merge_commit: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
  selected: false
  verified: false
```

The remaining foundational evidence gap remains direct controlled validation. Static audits can identify package or surface defects but cannot replace that evidence.

## 4. Why two Stage-A Fable5 tasks remain recommended

```yaml
Stage_A_tasks:
  - task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
    canonical_task: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
    operator: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/OPERATOR.md
    manifest: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
    role: independent_construct_validity_protocol_failure_and_falsification_audit
  - task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
    canonical_task: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
    operator: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/OPERATOR.md
    manifest: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
    role: independent_manual_surface_isolation_provenance_no_write_and_burden_audit
```

The substantive research questions are unchanged. MNEMOSYNE-184 corrects their delivery, access verification and lifecycle.

## 5. Corrected Claude access contract

```yaml
Claude_access_contract:
  Project_Files:
    persistent_across_Project_chats: true
    whole_Mnemosyne_repository: do_not_add
    current_official_file_count: unlimited
    practical_limit: content_context_and_RAG_capacity
  chat_plus_GitHub:
    current_chat_scope: true
    official_file_or_folder_selection: true
    user_observed_on_demand_repository_link: true
    exact_behavior_must_be_preflighted: true
  Project_membership_alone_grants_repo_access: false
  repository_hyperlink_proves_exact_read: false
```

Preferred sequence:

1. fresh standalone chat or new one-run Project;
2. visible `Fable 5` with `Max` effort;
3. Research off;
4. chat-level `+` -> `Add from GitHub`;
5. exact-path preflight;
6. Research on only after preflight passes;
7. full mandatory input gate;
8. complete report return.

The existing `Mnemosyne 复合评审` Project is continuity-oriented and not preferred for independent Stage-A runs because it has Project Memory and prior chats.

## 6. Exact repository inputs

```yaml
A1:
  complete_validation_package_folder_files: 15
  external_design_and_adjudication_files: 3
  canonical_task_files: 1
  minimum_manual_upload_set: 19
A2:
  manual_surface_candidate_files: 1
  package_subset_files: 9
  Mnemosyne_authority_files: 1
  canonical_task_files: 1
  minimum_manual_upload_set: 12
whole_repository_required: false
```

Exact paths and selection groups are in the task manifests. For A1, folder selection is preferred over manually choosing every package file.

## 7. Ready-queue and archive rule

```yaml
operator_discovery:
  only_ready_queue: handoff/fable5-ready/
  notes_research_prompts_is_operator_queue: false
completed_and_accepted:
  - archive_original_task_and_report_or_receipt_under_research_cycle
  - update_cycle_manifest
  - remove_ready_directory
retired_without_execution:
  - remove_ready_directory
  - preserve_non_runnable_reason_record
```

This prevents completed and future tasks from being mixed in the user's manual selection surface.

## 8. Staged quota discipline

```yaml
Fable5_quota_plan:
  high_value_tasks_ready_now: 2
  user_may_run_now: 0_to_2
  conditional_topics_reserved: 4
  simultaneous_generation_of_all_six_tasks: not_recommended
  automatic_execution: prohibited
  automatic_quota_spend: prohibited
```

Conditional Stage B topics remain:

1. reviewer independence and next-tier judge reliability;
2. V1 inference limits and progression thresholds;
3. no-write/context-isolation evidence equivalence;
4. portability and target-project propagation after valid V1 evidence.

They are not ready-to-run until Stage A or a later surface decision supplies their exact inputs.

## 9. Current evidence and execution state

```yaml
current_state:
  conceptual_design: complete
  complete_execution_and_review_package: merged
  Stage_A_delivery_packets: prepared_pending_PR_review
  Stage_A_reports: not_run
  manual_surface_candidate: prepared_not_selected_not_verified
  selected_execution_surface: none
  V0_authorized: false
  V0_executed: false
  V1_authorized: false
  V1_executed: false
  V2_executed: false
  V3_executed: false
```

No synthetic validation result, pass rate or model ranking exists.

## 10. Capability and research assessment

```yaml
model_capability_estimate:
  delivery_workflow_and_task_packet_design: FRONTIER_RECOMMENDED
  independent_Fable5_review: FRONTIER_RECOMMENDED_INDEPENDENT_ROLE
  visible_requested_condition: Fable_5_Max
  exact_path_preflight: NEXT_TIER_SUFFICIENT_CANDIDATE_or_human
  deterministic_manifest_checks: MECHANICAL_ONLY
  report_adjudication_and_package_amendment: FRONTIER_RECOMMENDED

research_assessment:
  additional_Pro_Deep_Research: NOT_NEEDED
  additional_foundational_Fable_research: NOT_NEEDED
  Fable5_post_package_Stage_A: RECOMMENDED_AFTER_DELIVERY_PR_MERGE
  Stage_B: DEFER_UNTIL_STAGE_A_ADJUDICATION
```

Visible model and effort text do not attest an exact backend.

## 11. Current safe next action

```yaml
safe_next_action:
  current:
    - review_and_merge_the_MNEMOSYNE_184_delivery_redesign_PR_or_request_changes
  after_merge:
    - user_may_run_zero_one_or_both_ready_Stage_A_tasks
    - use_separate_clean_Fable5_Max_chats
    - return_complete_reports_for_repository_bound_adjudication
  automatic_package_amendment: false
  automatic_surface_selection: false
  automatic_V0_execution: false
  automatic_V1_execution: false
```
