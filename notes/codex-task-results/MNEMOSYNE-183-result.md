# MNEMOSYNE-183 Result — Claude GitHub Access and Fable5 Research Delivery

```yaml
task_id: MNEMOSYNE-183
task_type: current_product_fact_verification_and_research_delivery_workflow_revision
repository: 08822407d/Mnemosyne
base: master@5e556c2a6dacb41d68bf6209dbf8156b92b79e72
canonical_branch: mnemosyne-183-fable5-claude-delivery-workflow
execution_source_modified: false
Fable5_research_executed: false
validation_executed: false
real_or_private_material_used: false
Meta_Agent_target_modified: false
non_FABLE_health_review_modified: false
```

## 1. User-observed problem

The user supplied 2026-07-30 Claude.ai screenshots showing:

- an existing `Mnemosyne 复合评审` Project with visible Project Memory and prior chats;
- a Project `Files` area that can upload files or add GitHub content;
- a chat-level `+` menu with `Add from GitHub`;
- a current repository-link modal stating that Claude reads the selected repository/branch through the GitHub connector when needed and does not download it immediately.

The user identified four operational risks:

1. adding the full Mnemosyne repository to Project Files can exceed or inefficiently consume project knowledge capacity;
2. the two ready Fable5 tasks require many repository files but prior delivery instructions did not surface their exact paths and UI steps;
3. it was unclear whether Project Files, chat-level GitHub linking, or mere Project membership provides repository reads;
4. completed prompt redirects mixed with runnable prompt texts make manual task discovery error-prone.

## 2. Current product-fact review

Official Anthropic sources checked on 2026-07-30:

- https://support.anthropic.com/en/articles/10167454-using-the-github-integration
- https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects
- https://support.anthropic.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects
- https://support.anthropic.com/en/articles/11088861-using-research-on-claude-ai
- https://support.anthropic.com/en/articles/8241126-what-kinds-of-documents-can-i-upload-to-claude-ai

Findings:

```yaml
Project_Files:
  official_role: persistent_project_knowledge_used_across_project_chats
  GitHub_selection: selected_files_and_folders
  synchronization_and_reconfiguration: supported
  RAG: automatically_enabled_near_context_limit_up_to_documented_10x_capacity
  entire_Mnemosyne_repo_recommended: false

chat_plus_GitHub:
  official_documentation: chat_specific_file_or_folder_access
  user_observed_current_UI: repository_and_branch_link_read_on_demand
  exact_rollout_behavior: surface_dependent_beta_or_transition_state
  repository_link_alone_proves_file_read: false

Project_membership_without_files_or_chat_link:
  repository_access_established: false

Research:
  can_use_internal_connected_context_and_web: supported_in_principle
  exact_GitHub_read_success_for_one_run: must_be_verified_in_that_chat
```

The help documentation and current UI wording are not identical. The workflow therefore supports both a repository-linked on-demand route and an explicit file/folder-selection route, with an input-integrity stop on read failure.

## 3. Operational decision

```yaml
preferred_independent_Fable5_environment:
  - fresh_standalone_chat_or_new_one_run_Project
  - Project_Files_empty_by_default
  - no_prior_reports_or_hidden_keys
  - GitHub_selected_through_chat_plus_menu
  - exact_ready_task_path_supplied
  - connector_preflight_before_Research

existing_Mnemosyne_复合评审_Project:
  continuity_work: suitable
  strict_independent_Stage_A_audit: not_preferred
  reason:
    - visible_Project_Memory
    - prior_chats
    - avoidable_framing_dependency
```

A plain pasted GitHub URL is not treated as equivalent to the `+` connector flow. A repository hyperlink created by the UI proves only that the repository was linked, not that mandatory files were read.

## 4. Ready queue and lifecycle

Created the sole human-facing runnable queue:

```text
handoff/fable5-ready/
```

Each active task contains:

```text
task.md
OPERATOR.md
input-manifest.yaml
```

Lifecycle:

```yaml
completed_and_accepted:
  archive_task: raw/research-reports/cycles/<cycle>/tasks/
  archive_report_or_receipt: raw/research-reports/cycles/<cycle>/reports/
  remove_from_handoff_fable5_ready: required
  completed_redirect_inside_ready_queue: prohibited

legacy_notes_research_prompts:
  role: registry_and_stable_reference
  may_contain_completed_redirects: true
  use_for_operator_task_discovery: false
```

## 5. Reworked Stage-A task delivery

### A1

```yaml
task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
ready_directory: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/
source_package_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830
explicit_selection_total: 20
research_question_changed: false
delivery_and_source_binding_changed: true
```

The selection set consists of the ready entrypoint, canonical task, the 15-file validation package folder and three external design/adjudication files.

A mechanical compare from package commit `67eb96d...` through master `5e556c...` found no A1 mandatory audit-source path changed. MNEMOSYNE-183 also changes none of those paths. Later master changes require recheck.

### A2

```yaml
task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
ready_directory: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/
source_audit_commit: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
explicit_selection_total: 19
research_question_changed: false
delivery_and_source_binding_changed: true
```

The selection set consists of the ready entrypoint, canonical task, manual-surface candidate, the complete 15-file validation package folder and `current/human-approved-spec.md`.

MNEMOSYNE-183 changes none of the A2 mandatory audit-source paths. Later master changes require recheck.

## 6. Connector preflight

Both operator guides now require a same-chat, Research-off preflight that reads only the ready entrypoint and canonical task and returns file receipts. After success, the user may switch to Fable5 Research in the same chat and submit the substantive startup instruction.

The preflight:

- reduces the risk of consuming a research run on an unavailable connector;
- does not prove all mandatory evidence reads;
- does not test the research question;
- does not establish context isolation or no-write evidence;
- cannot replace the canonical task's full input gate.

## 7. Files created

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
notes/codex-task-results/MNEMOSYNE-183-result.md
```

## 8. Actions not performed

```yaml
not_performed:
  Fable5_A1_execution: true
  Fable5_A2_execution: true
  Stage_B_task_generation: true
  Project_Files_modification: true
  Claude_connector_live_test: true
  V0_or_V1_execution: true
  execution_source_update: true
  target_project_update: true
  repository_merge_or_auto_merge: true
```

Here `true` means the named action was deliberately not performed.

## 9. Capability and research assessment

```yaml
product_fact_and_workflow_design: FRONTIER_RECOMMENDED
operator_file_selection_and_connector_preflight: NEXT_TIER_SUFFICIENT
file_count_path_and_diff_checks: MECHANICAL
Fable5_reports: still_recommended_but_not_executed
additional_Pro_Deep_Research: NOT_NEEDED
```

## 10. Safe next action

Human review and merge of the single MNEMOSYNE-183 PR. After merge, the user may run A1 and A2 separately by opening each ready directory's `OPERATOR.md`. No research or validation starts automatically.
