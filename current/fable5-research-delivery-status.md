# Fable5 Research Delivery Status

> Non-execution-source live status for delivering repository-bound Fable5 tasks. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
status_id: MNEMOSYNE-FABLE5-RESEARCH-DELIVERY-STATUS-001
created_by_task: MNEMOSYNE-184
repository: 08822407d/Mnemosyne
verified_master_before_task: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
canonical_PR: 236
canonical_branch: mnemosyne-184-claude-fable5-delivery-redesign
rejected_predecessor_PR:
  PR: 235
  merged: false
  adopted: false
workflow: notes/research-operations/claude-project-github-and-fable5-delivery-v0.1.md
ready_queue: handoff/fable5-ready/
staged_plan: notes/research-plans/2026Q3-frontier-clarification-validation-fable5-staged-plan-v0.2.md
status: delivery_workflow_and_two_ready_packets_prepared_in_PR_236_pending_review_not_executed
execution_source_modified: false
research_executed: false
validation_executed: false
Meta_Agent_target_modified: false
non_FABLE_health_review_modified: false
```

## 1. Corrected product interpretation

```yaml
Claude_access:
  Project_Files:
    scope: persistent_shared_Project_knowledge
    official_GitHub_selection: files_or_folders
    whole_Mnemosyne_repository_recommended: false
    file_count_limit: officially_unlimited
    practical_limit: content_context_and_RAG_capacity
  chat_plus_GitHub:
    scope: current_chat
    official_description: selected_files_or_folders
    user_observed_2026_07_30_UI: repository_and_branch_linked_for_on_demand_reads
    exact_rollout_behavior: verify_in_each_chat
    visible_link_proves_file_read: false
  Project_membership_alone_grants_repository_access: false
```

The current workflow supports both documented file/folder selection and the user's observed on-demand repository-link UI. It never requires adding the whole repository to Project Files.

## 2. Independent-run boundary

```yaml
preferred_environment:
  - fresh_standalone_chat
  - new_one_run_Project_with_no_prior_chats_and_empty_Project_Files
existing_Mnemosyne_复合评审_Project:
  role: continuity_oriented_review_only_by_default
  independent_Stage_A_use: not_recommended
  reason:
    - Project_Memory_present
    - prior_chats_present
preferred_visible_model: Fable_5
preferred_effort: Max
exact_backend_identity: unknown_or_not_attestable
```

## 3. Current ready tasks

```yaml
ready_tasks:
  - task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
    operator: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/OPERATOR.md
    manifest: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
    executed: false
    report_received: false
  - task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
    operator: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/OPERATOR.md
    manifest: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
    executed: false
    report_received: false
```

A1 needs the complete validation-package folder plus three external source/adjudication files. A2 needs the manual-surface candidate, nine package files and `current/human-approved-spec.md`. Both exact sets are enumerated in their manifests.

## 4. Access sequence

```yaml
required_sequence:
  - create_clean_chat_or_one_run_Project
  - choose_visible_Fable_5_Max
  - keep_Research_off
  - add_or_link_GitHub_in_that_chat
  - run_exact_path_preflight
  - continue_only_on_complete_read_receipts
  - enable_Research
  - run_canonical_task
  - return_complete_report
```

Fallbacks are explicit file/folder selection, task-specific Project Files in a new one-run Project, then exact manual upload. Whole-repository Project Files are prohibited by default.

## 5. Queue lifecycle

```yaml
ready_queue_lifecycle:
  current_ready_queue: handoff/fable5-ready/
  completed_task_remains_in_ready_queue: prohibited
  accepted_completion_archive:
    tasks: raw/research-reports/cycles/<cycle>/tasks/
    reports_or_receipts: same_cycle
    manifest_update: required
  registry: notes/research-prompts/
  registry_is_operator_queue: false
```

## 6. Current route state

```yaml
frontier_clarification_validation:
  package_merged: true
  Stage_A_Fable5_tasks_ready: true
  Stage_A_Fable5_executed: false
  surface_selected: false
  V0_authorized: false
  V0_executed: false
  V1_authorized: false
  V1_executed: false
Stage_B_topics:
  count: 4
  ready_to_run: false
  generation_gate: Stage_A_report_adjudication
```

## 7. Safe next action

```yaml
safe_next_action:
  current:
    - review_and_merge_PR_236_or_request_changes
  after_merge:
    - user_may_run_zero_one_or_both_ready_tasks
    - use_each_task_OPERATOR_file_in_a_separate_clean_Fable5_Max_chat
    - return_complete_reports_for_adjudication
  automatic_research_execution: false
  automatic_surface_selection: false
  automatic_V0_or_V1: false
```
