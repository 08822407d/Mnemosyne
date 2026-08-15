# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
last_updated_by_task: MNEMOSYNE-219
source_master: 94072794cb67eb90034a19569d4716fc18aa635d
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: OWNER_RUN_SELECTED_SNAPSHOT_FOLDER_PREFLIGHT_PASS_RESEARCH_NOT_STARTED
external_execution_or_quota_authorized: one_Fable5_Research_run_selected_by_Owner
automatic_retry: false
repository_write_by_Fable: prohibited
validation_execution_by_Fable: prohibited
Fable_started: false
Research_started: false
```

## Current source state

The roadmap timing gate remains met. Target Lifecycle V1 has a completed controller bundle on:

```text
08822407d/mnemosyne-target-lifecycle-validation-002
tlr-v1-controller@e892749fc9e242b24908f89b6a78f1c0f0bed75e
```

The exact result-bundle blob remains:

```text
8a5f3644707ae518182ed352174e58d1ca419067
```

Later repository state now also contains the fresh Pro adjudication and Owner architecture decision. MNE-DR-005 must preserve the historical controller `pending_fresh_Pro` fields as historical evidence while treating the later accepted adjudication/decision as the current status. The accepted global architecture remains provisional for target-specific consideration and does not prove production readiness or authorize target adoption.

## Project-knowledge snapshot

```yaml
snapshot_repository: 08822407d/Mnemosyne
snapshot_branch: mne-dr-005-project-knowledge-snapshot-001
snapshot_branch_head_after_preflight_receipt: 074720c9b1f63e0785d49666482447a017b23ef0
snapshot_folder: project-knowledge/MNE-DR-005/
snapshot_folder_tree: 3f6b627782ebb0c72070e8b1ae1be40a5ce6fc5a
snapshot_folder_file_count: 30
canonical_originals_moved_or_modified: false
snapshot_branch_merge_allowed: false
snapshot_branch_retention_required: true
```

The branch is a temporary read-only Project-knowledge input surface. It must not be merged into `master` and remains retained until the Fable report is returned or the run is abandoned, the exact input/report identities are preserved, and Pro intake no longer needs Project re-sync.

## Folder-selection preflight

The Owner completed the preflight on the current Claude web UI:

```yaml
preflight_result: PASS
selection_action: one_folder_selected
Claude_Project_knowledge_count: 30
extra_files_observed: false
Research_started_during_preflight: false
ordinary_repository_picker_exposed_branch_list: false
successful_branch_route:
  - click_hyperlink_icon
  - paste_full_branch_URL
  - select_project-knowledge/MNE-DR-005_folder
UI_evidence_class: operator_observed_current_account_rollout
```

This proves the single-folder packaging route works for the current account and task. It does not yet establish a universal Mnemosyne rule for every future Claude run.

## Current product-surface assessment gate

The Owner paused before Research to ask whether Claude can support ongoing GitHub-backed Agent construction with comparable convenience to the current ChatGPT workflow.

Current answer recorded by MNEMOSYNE-219:

- Claude Project GitHub context is appropriate for bounded read-only research packets, not as the primary long-term repository-writing surface;
- Claude Code web or terminal is the closer candidate for branch/commit/test/PR work;
- a bounded documentation-centric Claude Code pilot is required before adopting it as a default Mnemosyne/Meta-Agent maintenance surface;
- durable truth remains in repository files rather than Claude Project memory.

Current detailed records:

```text
current/claude-github-work-surface-facts.md
notes/research-operations/claude-web-github-context-and-code-work-surfaces-2026-08-15.md
```

## Current gate

```yaml
current_gate: OWNER_DECIDES_WHETHER_TO_RESUME_THE_ALREADY_SELECTED_FABLE_RUN
new_quota_authorization_required_if_resumed_now: false
new_resume_instruction_required_after_explicit_pause: true
Research_may_start_before_MNEMOSYNE_219_PR_merge: technically_yes_but_not_recommended_for_record_consistency
recommended_order:
  - merge_MNEMOSYNE_219_record_PR
  - explicitly_resume_MNE_DR_005
  - select_visible_Fable5_and_Research
  - send_the_single_startup_message
```

The existing one-run authorization is preserved, but the explicit pause means the route must not infer automatic resumption.
