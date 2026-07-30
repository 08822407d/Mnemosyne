# MNEMOSYNE-184 Result — Claude Project/GitHub and Fable5 Delivery Redesign

## 1. Positioning

```yaml
task_id: MNEMOSYNE-184
task_type: product_fact_verification_research_delivery_redesign_and_route_status_sync
repository: 08822407d/Mnemosyne
base_branch: master
pinned_base_sha: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
canonical_branch: mnemosyne-184-claude-fable5-delivery-redesign
canonical_PR: pending_creation
user_visible_selection_verbatim: Pro
exact_served_backend: unknown_or_not_attestable
execution_source_modified: false
research_executed: false
validation_executed: false
Meta_Agent_target_modified: false
non_FABLE_health_review_modified: false
```

This task redoes the rejected PR #235 scope from merged `master` after the user switched the current ChatGPT conversation to Pro. PR #235 was closed without merge and is not treated as adopted work.

## 2. User questions resolved

The task addresses:

1. the difference between Claude Project Files/project knowledge and chat-level `+ -> Add from GitHub`;
2. whether Project membership alone grants repository access;
3. whether the whole Mnemosyne repository must be added;
4. exactly which files the two current Fable5 tasks require;
5. how to handle future independent design, artifact-audit and broad repository-review tasks;
6. how completed research tasks leave the operator's active selection surface.

## 3. Current product-fact review

Official Claude documentation reviewed on 2026-07-30:

```text
https://support.claude.com/en/articles/10167454-use-the-github-integration
https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects
https://support.claude.com/en/articles/8241126-upload-files-to-claude
https://support.claude.com/en/articles/11088861-use-research-on-claude
https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings
https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
```

The user's screenshots were separately treated as current operator-observed UI evidence. No screenshot was committed to the public repository.

## 4. Product-access conclusion

```yaml
Project_Files:
  scope: persistent_shared_knowledge_across_Project_chats
  official_GitHub_behavior: select_files_or_folders_then_sync_or_reconfigure
  official_file_count: unlimited
  practical_capacity: context_extracted_content_and_RAG_limited
  whole_Mnemosyne_repository_recommended: false

chat_plus_GitHub:
  scope: current_chat
  official_behavior: selected_files_or_folders_are_accessed_and_processed
  user_observed_UI: repository_and_branch_linked_for_on_demand_connector_reads
  exact_rollout_behavior: must_be_verified_in_each_chat
  visible_link_proves_exact_file_read: false

Project_membership_alone_grants_repository_access: false
```

A Project chat can read repository material only when the relevant content is in Project knowledge, explicitly selected/attached to that chat, or available through a chat-level GitHub link that succeeds on exact-path reads.

## 5. Independent Fable5 environment

```yaml
preferred_environment:
  - fresh_standalone_chat
  - new_one_run_Project_with_no_prior_chats_and_empty_Project_Files
existing_Mnemosyne_复合评审_Project:
  recommended_for_independent_Stage_A: false
  suitable_for: continuity_oriented_review
preferred_visible_condition:
  model: Fable_5
  effort: Max
exact_backend_identity: unknown_or_not_attestable
```

The existing Project visibly contains Memory and prior chats. It is therefore not the preferred environment for framing-independent audits.

## 6. Ready queue and exact input manifests

Created the sole human-facing queue:

```text
handoff/fable5-ready/
```

Current task directories:

```text
handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/
handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/
```

Each contains:

```text
task.md
OPERATOR.md
input-manifest.yaml
```

A1 exact audit set:

```yaml
canonical_task: 1
complete_validation_package_files: 15
external_design_and_adjudication_files: 3
minimum_manual_upload_set: 19
preferred_selection: complete_package_folder_plus_three_external_files
```

A2 exact audit set:

```yaml
canonical_task: 1
manual_surface_candidate: 1
required_package_subset: 9
Mnemosyne_authority_file: 1
minimum_manual_upload_set: 12
```

Neither task requires the whole repository in Project Files.

## 7. Connector preflight

Every current repository-bound run now requires this sequence:

```yaml
sequence:
  - clean_chat_or_one_run_Project
  - select_visible_Fable_5_Max
  - keep_Research_off
  - add_or_link_GitHub_in_the_same_chat
  - read_ready_entrypoint_manifest_canonical_task_and_primary_object
  - return_exact_path_receipts
  - continue_only_on_PASS
  - enable_Research
  - execute_canonical_task
```

The preflight is not a research run and does not prove every mandatory file; the canonical task performs the complete input gate. A repository hyperlink without file receipts is insufficient.

## 8. Task-class guidance

The operating workflow distinguishes:

- independent greenfield design: task plus minimal constraints, no broad repository framing;
- repository-bound artifact audit: ready packet and exact manifest;
- broad repository health review: dedicated clean context, staged on-demand discovery and file-access ledger rather than whole-repository Project Files.

## 9. Completed-task lifecycle

```yaml
ready_queue: handoff/fable5-ready/
completed_task_allowed_to_remain_ready: false
on_acceptance:
  - archive_original_task_under_raw/research-reports/cycles/<cycle>/tasks/
  - archive_report_or_receipt_under_same_cycle
  - update_manifest_and_status
  - remove_ready_task_directory
registry: notes/research-prompts/
registry_is_operator_queue: false
```

This preserves audit history without forcing the user to distinguish completed and active tasks in one directory.

## 10. Files created

```text
current/fable5-research-delivery-status.md
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
```

## 11. Files modified

```text
current/frontier-clarification-validation-handoff-status.md
current/frontier-planning-clarification-handoff-research-status.md
```

## 12. Explicitly unchanged

```text
current/human-approved-spec.md
handoff/handoff-current.md
current/active-context.md
current/todo.md
current/open-questions.md
target-projects/meta-agent/
all_other_target_projects
non-FABLE health-review files
```

The canonical A1/A2 research questions and long report contracts remain unchanged. The ready packets supersede only the older high/xhigh operator-label wording with the current visible `Fable 5` + `Max` request and add access/delivery controls.

## 13. Verification performed

```yaml
checks:
  latest_master_and_open_PR_preflight: passed_before_branch_creation
  rejected_PR_235_merged: false
  ready_task_directories: 2
  files_per_ready_task: 3
  exact_input_manifests_present: true
  Project_Files_whole_repository_required: false
  A1_input_count_reconciled: 19
  A2_input_count_reconciled: 12
  completed_task_ready_queue_prohibition_present: true
  prior_report_contamination_prohibited: true
  Research_off_connector_preflight_present: true
  visible_Fable_5_Max_receipt_present: true
  repository_write_by_Fable5: prohibited
  synthetic_research_result_generated: false
```

No live Claude connector test was performed. Current product capability remains subject to the operator preflight in the actual Fable5 chat.

## 14. Capability and research assessment

```yaml
model_capability_estimate:
  product_fact_and_delivery_redesign: FRONTIER_RECOMMENDED
  operator_connector_preflight: NEXT_TIER_SUFFICIENT_CANDIDATE_or_human
  exact_manifest_checks: MECHANICAL_ONLY
  independent_report_execution: Fable_5_Max_requested
  report_adjudication: FRONTIER_RECOMMENDED

research_assessment:
  additional_Pro_Deep_Research: NOT_NEEDED
  additional_foundational_Fable_research: NOT_NEEDED
  two_post_package_Stage_A_tasks: RECOMMENDED_AFTER_PR_MERGE
  four_Stage_B_topics: DEFER_UNTIL_STAGE_A_ADJUDICATION
```

## 15. Actions not performed

```yaml
not_performed:
  Fable5_run: true
  quota_spend: true
  validation_execution: true
  V0_or_V1_authorization: true
  Claude_Project_Files_change: true
  live_connector_test: true
  GitHub_merge_or_auto_merge: true
  execution_source_change: true
  Meta_Agent_target_change: true
  non_FABLE_route_takeover: true
```

In the block above, `true` means the named action was not performed.

## 16. Safe next action

Human review of the canonical MNEMOSYNE-184 PR is required. After merge, the user may run zero, one or both ready tasks in separate clean Fable5 Max chats and return complete reports for repository-bound adjudication. No surface, V0, V1 or Stage B action follows automatically.
