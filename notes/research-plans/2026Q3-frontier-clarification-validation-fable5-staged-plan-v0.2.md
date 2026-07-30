# Frontier Clarification Validation — Staged Fable5 Research Plan v0.2

> Supersedes v0.1 for task discovery and delivery only. The two Stage-A research questions remain unchanged. This revision adds Claude Project/GitHub access rules, exact ready-task paths, operator manifests and completion lifecycle. It does not run research, spend quota, modify the validation package or authorize V0/V1.

```yaml
plan_id: FABLE5-FRONTIER-CLARIFICATION-VALIDATION-STAGED-PLAN-001
version: 0.2.0
created_by_task: MNEMOSYNE-182
revised_by_task: MNEMOSYNE-183
status: stage_A_ready_queue_prepared_not_executed
supersedes_for_delivery: notes/research-plans/2026Q3-frontier-clarification-validation-fable5-staged-plan-v0.1.md
source_package_merge_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830
manual_candidate_merge_commit: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
research_execution_authority: user_only
```

## 1. Current research judgment

The foundational Pro and Fable research cycle is complete and is not reopened. Two post-package audits remain recommended because they examine artifacts that did not exist during the foundational cycle:

1. static construct-validity and failure-mode audit of the merged validation package;
2. static threat model of the manual multi-conversation V0 surface candidate.

Four dependent Stage-B topics remain deferred until Stage A is returned and adjudicated.

## 2. Ready-task discovery

The only operator-facing ready queue is:

```text
handoff/fable5-ready/
```

Ready tasks:

```yaml
A1:
  task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  ready_directory: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/
  entrypoint: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md
  operator_guide: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/OPERATOR.md
  input_manifest: handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/input-manifest.yaml
  canonical_task: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
  pinned_commit: 67eb96d5317a2bb589236a4a8b2e75be2508d830

A2:
  task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
  ready_directory: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/
  entrypoint: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/task.md
  operator_guide: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/OPERATOR.md
  input_manifest: handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/input-manifest.yaml
  canonical_task: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
  pinned_commit: 5e556c2a6dacb41d68bf6209dbf8156b92b79e72
```

`notes/research-prompts/` is a legacy registry, not a runnable-task queue.

## 3. Claude delivery route

Preferred route for each Stage-A task:

```yaml
environment:
  - fresh_standalone_chat_or_new_one_run_Project
  - no_prior_Mnemosyne_or_Fable_reports
  - no_reuse_between_A1_and_A2_before_both_complete
  - Project_Files_empty_by_default
  - GitHub_added_through_chat_plus_menu
  - exact_ready_entrypoint_named_in_startup_message
```

Do not add the whole Mnemosyne repository to Project Files. Project knowledge is persistent across project chats and may activate RAG; it is not necessary for the preferred chat-level connector route.

The visible repository link is not a file-read receipt. Each canonical task must verify every mandatory path and exact commit before substantive analysis.

## 4. Fallback selection sets

### A1

Select:

```text
handoff/fable5-ready/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001/task.md
notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001.md
notes/frontier-clarification-validation-package/                  [15 files]
notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md
notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/03-cross-report-consensus-conflict-and-adjudication.md
notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/04-interim-architecture-and-validation-decision.md
```

Total selected files: 20.

### A2

Select:

```text
handoff/fable5-ready/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001/task.md
notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001.md
notes/validation-designs/frontier-clarification-validation-manual-surface-preparation-candidate-v0.1.md
notes/frontier-clarification-validation-package/                  [15 files]
current/human-approved-spec.md
```

Total selected files: 19. The canonical task requires a subset of the package folder; selecting the complete folder reduces operator omission risk and remains below the documented 20-file chat limit.

## 5. Independence protocol

```yaml
Stage_A:
  A1_chat_or_Project: fresh_and_isolated
  A2_chat_or_Project: separate_fresh_and_isolated
  cross_report_visibility_before_completion: prohibited
  foundational_Pro_report_supplied: false
  foundational_Fable_report_supplied: false
  existing_Mnemosyne_复合评审_Project_preferred: false
  reason: visible_project_Memory_and_prior_chats_create_avoidable_framing_dependency
```

The reports may use current official platform documentation and external research as required by their tasks. They must not use previous Mnemosyne research conclusions as authority.

## 6. Stage-A decisions

A1 may change:

```yaml
- proceed_to_surface_decision_without_package_revision
- amend_package_before_surface_selection
- major_redesign_before_V0_preparation
- stop_validation_route
```

A2 may change:

```yaml
- prepare_and_verify_manual_V0_preflight
- amend_manual_candidate
- prefer_API_or_runtime_preparation
- defer_or_stop_surface_route
```

Neither report selects a surface or authorizes validation.

## 7. Stage-B reserve

The following remain conditional and non-runnable:

```yaml
- FABLE5-FCV-REVIEWER-INDEPENDENCE-001
- FABLE5-FCV-V1-INFERENCE-AND-THRESHOLDS-001
- FABLE5-FCV-EVIDENCE-EQUIVALENCE-001
- FABLE5-FCV-PORTABILITY-AND-PROPAGATION-001
```

Do not freeze or execute them before Stage-A adjudication and the relevant surface/phase trigger.

## 8. Completion lifecycle

After a Stage-A report is received and accepted:

```yaml
required:
  - archive_original_task_under_raw_research_cycle
  - archive_report_or_report_receipt
  - update_cycle_manifest
  - remove_task_directory_from_handoff/fable5-ready/
  - update_current_delivery_status
prohibited:
  - leave_completed_task_in_ready_queue
  - add_report_to_the_other_pending_task_Project_or_chat
  - treat_report_as_execution_source
```

A completed redirect may remain in `notes/research-prompts/` for stable references, but completed tasks never remain under `handoff/fable5-ready/`.

## 9. Current safe next action

```yaml
safe_next_action:
  - review_and_merge_MNEMOSYNE_183_delivery_workflow_PR
  - after_merge_user_may_run_A1_and_A2_separately_using_their_OPERATOR_files
  - return_complete_reports_for_repository_backed_adjudication
  - do_not_run_Stage_B_or_V0_automatically
```
