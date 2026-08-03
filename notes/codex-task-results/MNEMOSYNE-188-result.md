# MNEMOSYNE-188 Result — Fable5 Project-Knowledge Research Surface

## 1. Positioning

```yaml
task_id: MNEMOSYNE-188
task_type: chronology_review_current_product_fact_review_and_Stage_A_execution_surface_repair
repository: 08822407d/Mnemosyne
base_branch: master
pinned_base_sha: 5cc758caa6baf86de0cf67cda2d852724f5edbbb
canonical_branch: mnemosyne-188-fable-research-project-knowledge-surface
canonical_PR: pending_creation
execution_source_modified: false
validation_package_modified: false
manual_surface_candidate_modified: false
Meta_Agent_target_modified: false
non_FABLE_health_review_modified: false
Fable5_or_Deep_Research_executed: false
validation_executed: false
```

## 2. Run context v0.2

```yaml
run_context:
  schema_and_task:
    record_version: v0.2
    task_id: MNEMOSYNE-188
    record_id: MNEMOSYNE-188-RUN-001

  date_or_window:
    started_at: 2026-08-03
    completed_or_recorded_at: 2026-08-03

  action:
    actor: ChatGPT
    actor_kind: model
    source: standard_ChatGPT_conversation_with_connected_GitHub_app_and_web_verification
    switch_history:
      status: recorded
      evidence:
        - class: operator_reported
          ref: current_conversation_user_message_starting_MNEMOSYNE_188
          observed_or_accessed_at: 2026-08-03
          claim_scope: user_reported_Pro_quota_restored_for_current_task
          detail: The user stated that Pro quota had recovered and requested review, advancement and latest Fable operating procedures.

  product_surface:
    value: standard_ChatGPT_conversation_with_GitHub_app_and_web_search
    evidence:
      - class: operator_observed
        ref: current_tool_environment
        observed_or_accessed_at: 2026-08-03
        claim_scope: repository_and_current_product_fact_review_surface

  operator_selection:
    verbatim: "pro额度已经恢复"
    evidence:
      - class: operator_reported
        ref: current_conversation_user_message_starting_MNEMOSYNE_188
        observed_or_accessed_at: 2026-08-03
        claim_scope: operator_reported_frontier_condition

  backend:
    status: unknown_or_not_attestable
    reason: Consumer-chat selection and user wording do not attest the exact served backend.

  artifacts:
    status: recorded
    refs:
      - ref: notes/research-operations/claude-fable5-project-knowledge-research-v0.3.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: null
      - ref: notes/research-plans/2026Q3-frontier-clarification-validation-fable5-staged-plan-v0.4.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: null
      - ref: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.3.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: null
      - ref: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.3.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: null

  user_authorization:
    status: authorized
    actor: user
    decision_ref: current_conversation_user_message_starting_MNEMOSYNE_188
    authorized_actions:
      - review_work_since_Pro_quota_pause
      - analyze_and_organize_current_route
      - advance_currently_safe_work
      - revise_latest_A1_A2_operating_procedures
      - create_one_bounded_repository_branch_and_PR
    excluded_actions:
      - execute_Fable5_or_Deep_Research
      - spend_external_research_quota
      - execute_V0_V1_V2_or_V3
      - modify_current_human_approved_spec
      - modify_validation_package_or_manual_surface_candidate
      - take_over_Meta_Agent_or_non_FABLE_health_review_routes
      - merge_or_enable_auto_merge
    evidence:
      - class: direct_user_instruction
        ref: current_conversation_user_message_starting_MNEMOSYNE_188
        observed_or_accessed_at: 2026-08-03
        claim_scope: current_task_analysis_and_repository_write_authorization
    expires_with_task: true
    not_future_precedent: true

  limitations:
    - The v0.3 Project-knowledge Research route has official product support but no empirical R0 result on the user's current Claude rollout.
    - R0 consumes some quota; exact cost cannot be predicted.
    - Exact served backend identity is unknown or not attestable.
    - Verification is connector-backed and author-reviewed; no local checkout/parser was available.

  omissions:
    - field: provider_attested_served_model_identifier
      reason: not_available
      detail: Consumer Chat did not provide exact-request provider metadata.
```

## 3. Work review since quota pause

Created:

```text
notes/frontier-clarification-validation-pro-quota-pause-review-2026-08-03.md
```

The review separates:

- PR #239 failure preservation and ordinary-chat fallback;
- PR #241 execution-intent repair;
- the separate Meta-Agent P0/P1 planning test and later Meta-Agent PRs #242/#243;
- reminder Issue #244;
- work not performed on A1/A2/V0/V1;
- the current Pro-restored surface redesign.

## 4. Current product-fact review

Official Claude Help Center sources reviewed on 2026-08-03 support:

- exact GitHub files/folders can be added to Project Files/Project knowledge and synced;
- Project RAG works with Research;
- Research uses web and internal context and can consume quota faster;
- connector tools can be invoked automatically during Research, so unneeded/write-capable tools should be disabled;
- Project files are subject to per-file and total-content limits.

This evidence does not prove current-account success. It supports a Research-direct Project-knowledge probe.

## 5. Surface repair

```yaml
v0_3_surface:
  Project: new_one_run_per_task
  Project_Files: exact_manifest_set_only
  whole_repository: prohibited
  Project_sync: required
  Research_R0:
    purpose: direct_Project_knowledge_visibility_probe
    external_web_sources: 0
    substantive_findings: prohibited
    operator_cancel_on_broad_external_collection: true
  Research_R1:
    allowed_only_after_R0_PASS: true
    purpose: complete_canonical_report
  chat_level_GitHub_during_Research: disabled
  other_connectors_during_Research: disabled
  repository_write: prohibited
```

The repair differs from run 001 because the primary inputs are persistent Project knowledge inside Research, not an ordinary-chat connector state.

## 6. Current task dispositions

```yaml
A1:
  state_after_merge: READY_NOT_SELECTED
  Project_file_count: 22
  next_possible_run: R0_then_conditional_R1

A2:
  state_after_merge: DEFERRED_PENDING_VALID_A1_ADJUDICATION
  Project_file_count: 15
  current_execution_selected: false
```

A2 remains deferred because A1 may require package changes that invalidate the A2 audit object.

## 7. Changed paths before result/finalization

Modified:

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
```

Created:

```text
notes/frontier-clarification-validation-pro-quota-pause-review-2026-08-03.md
notes/research-operations/claude-fable5-project-knowledge-research-v0.3.md
notes/research-plans/2026Q3-frontier-clarification-validation-fable5-staged-plan-v0.4.md
notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.3.md
notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.3.md
```

## 8. Protected boundaries

Unchanged:

```text
current/human-approved-spec.md
current/artifact-delivery-and-direct-generation-guard.md
current/cross-conversation-execution-intent-and-operator-flow-guard.md
notes/frontier-clarification-validation-package/
notes/validation-designs/frontier-clarification-validation-manual-surface-preparation-candidate-v0.1.md
target-projects/meta-agent/
handoff/handoff-current.md
current/active-context.md
current/todo.md
current/open-questions.md
```

No Fable run, Research run, validation cell, surface selection, merge or auto-merge was performed.

## 9. Pre-result verification

```yaml
compare:
  base: 5cc758caa6baf86de0cf67cda2d852724f5edbbb
  status: ahead
  ahead_by: 15
  behind_by: 0
  changed_files: 15
open_PRs_before_branch: []
open_PRs_before_result: []
```

Final PR identity, final counts, status checks and workflow runs belong in the companion finalization record.

## 10. Capability and research assessment

```yaml
model_capability_estimate:
  chronology_and_surface_repair: FRONTIER_RECOMMENDED
  Project_file_selection_and_R0_receipt_check: HUMAN_plus_MECHANICAL
  A1_A2_execution: Fable_5_Max_requested
  report_adjudication: FRONTIER_RECOMMENDED

research_assessment:
  additional_Pro_Deep_Research: NOT_NEEDED
  additional_foundational_Fable_research: NOT_NEEDED
  reason: remaining_need_is_direct_Stage_A_execution_and_adjudication
```

## 11. Safe next action

Human review of the MNEMOSYNE-188 PR is required. After merge, A1 may be explicitly selected for R0 and conditional R1. A2 remains deferred until valid A1 adjudication.