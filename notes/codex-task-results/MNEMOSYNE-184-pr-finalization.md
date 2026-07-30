# MNEMOSYNE-184 PR Finalization — Canonical PR #236

```yaml
task_id: MNEMOSYNE-184
record_type: PR_finalization_and_lineage_binding
status: FINALIZATION_IN_PROGRESS
repository: 08822407d/Mnemosyne
base_branch: master
base_sha: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
canonical_branch: mnemosyne-184-claude-fable5-delivery-redesign
canonical_PR: 236
rejected_predecessor_PR: 235
predecessor_merged: false
predecessor_adopted: false
PR_state: open
PR_draft: true
PR_merged: false
merge_performed: false
auto_merge_enabled: false
```

## 1. Lineage gates

```yaml
lineage_gates:
  latest_master_before_branch: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
  latest_master_immediately_before_PR_creation: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
  accessible_open_PRs_before_branch: []
  accessible_open_PRs_before_PR_creation: []
  rejected_PR_235_state: closed_unmerged
  branch: mnemosyne-184-claude-fable5-delivery-redesign
  decision: create_one_new_canonical_lineage_from_merged_master
```

PR #235 was not reopened or copied as authority. Its scope was independently re-evaluated against official current product documentation, the user's screenshots and merged repository state.

## 2. Canonical scope

```yaml
scope:
  product_fact_verification:
    - Claude_Project_Files_and_Project_Memory
    - chat_level_GitHub_selection_or_on_demand_link
    - Research_and_connector_preflight
    - file_and_Project_capacity
    - Fable_5_model_and_effort_receipt
  delivery_redesign:
    - dedicated_Fable5_ready_queue
    - two_exact_operator_guides
    - two_exact_input_manifests
    - completed_and_retired_task_lifecycle
    - greenfield_artifact_audit_and_broad_review_access_classes
  current_route_sync:
    - frontier_validation_handoff_status
    - frontier_research_status
    - dedicated_Fable5_delivery_status
```

## 3. Final changed paths

```text
current/fable5-research-delivery-status.md
current/frontier-clarification-validation-handoff-status.md
current/frontier-planning-clarification-handoff-research-status.md
handoff/fable5-ready/README.md
handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md
handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/OPERATOR.md
handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/task.md
handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/OPERATOR.md
handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
notes/research-operations/claude-project-github-and-fable5-delivery-v0.1.md
notes/research-plans/2026Q3-frontier-clarification-validation-fable5-staged-plan-v0.2.md
notes/research-prompts/README.md
notes/codex-task-results/MNEMOSYNE-184-result.md
notes/codex-task-results/MNEMOSYNE-184-pr-finalization.md
```

## 4. Protected boundaries

```yaml
protected_boundaries:
  current/human-approved-spec.md: unchanged
  handoff/handoff-current.md: unchanged
  current/active-context.md: unchanged
  current/todo.md: unchanged
  current/open-questions.md: unchanged
  target-projects/meta-agent/: unchanged
  all_other_target_projects: unchanged
  non_FABLE_health_review_route: not_imported_or_modified
  research_execution: false
  validation_execution: false
  Claude_Project_or_connector_mutation: false
```

## 5. Author and connector-backed checks

```yaml
checks:
  Project_Files_vs_chat_GitHub_distinction: present
  official_vs_observed_UI_difference_preserved: true
  whole_repository_Project_Files_required: false
  exact_path_preflight_required: true
  existing_memory_bearing_Project_not_preferred_for_independent_runs: true
  visible_Fable_5_Max_requested: true
  exact_backend_not_inferred: true
  ready_task_directories: 2
  files_per_ready_task: 3
  A1_manifest_input_count: 19
  A2_manifest_input_count: 12
  completed_task_removed_from_ready_queue_rule: present
  prior_report_contamination_prohibited: true
  Stage_B_ready_tasks_created: 0
  research_results_generated: 0
  validation_cells_started: 0
```

No live Claude connector test was performed. The operator preflight is the first run-specific evidence gate.

## 6. PR state before final recheck

```yaml
PR_snapshot:
  PR: 236
  draft: true
  merged: false
  compact_mergeable_snapshot: false
  interpretation: pending_GitHub_recalculation_and_full_fetch_recheck
  head_before_this_record: 3a67ae72d1842ddb4c04b9a2967346f309289f02
  commits_before_this_record: 19
  changed_files_before_this_record: 14
```

The initial `mergeable: false` snapshot is not treated as a conflict until GitHub recalculates the new head and a full PR fetch is performed.

## 7. Checks still required before ready transition

```yaml
pending_final_checks:
  - bind_result_record_to_PR_236
  - compare_final_head_to_base
  - confirm_behind_by_zero
  - enumerate_accessible_open_PRs
  - recheck_mergeability
  - check_commit_statuses
  - check_workflow_runs
  - update_PR_body_to_final_head_and_counts
  - mark_ready_for_review
```

## 8. Actions not performed

```yaml
not_performed:
  merge: true
  auto_merge: true
  Fable5_execution: true
  quota_spend: true
  validation_execution: true
  execution_source_change: true
  target_project_change: true
```

Here `true` means the named action was not performed.
