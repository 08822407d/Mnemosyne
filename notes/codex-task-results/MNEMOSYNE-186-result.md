# MNEMOSYNE-186 Result — Fable Repository-Bound Static-Audit Surface Repair

## 1. Positioning

```yaml
task_id: MNEMOSYNE-186
task_type: failed_run_adjudication_research_delivery_repair_and_branch_retention_assessment
repository: 08822407d/Mnemosyne
base_branch: master
pinned_base_sha: 7bcddd60e209afe6496fa3091332496e20c3e245
canonical_branch: mnemosyne-186-fable-repository-surface-repair
canonical_PR: pending_creation
execution_source_modified: false
validation_package_modified: false
Meta_Agent_target_modified: false
non_FABLE_health_review_modified: false
Fable_or_Deep_Research_executed_by_this_task: false
validation_executed: false
failed_branches_deleted: false
```

## 2. Run context v0.2

```yaml
run_context:
  schema_and_task:
    record_version: v0.2
    task_id: MNEMOSYNE-186
    record_id: MNEMOSYNE-186-RUN-001

  date_or_window:
    started_at: 2026-07-31
    completed_or_recorded_at: 2026-07-31

  action:
    actor: ChatGPT
    actor_kind: model
    source: standard_ChatGPT_conversation_with_connected_GitHub_app
    switch_history:
      status: recorded
      evidence:
        - class: direct_user_instruction
          ref: current_conversation_user_message_starting_MNEMOSYNE_186
          observed_or_accessed_at: 2026-07-31
          claim_scope: user_reported_switch_to_Pro_before_this_task
          detail: The user stated that the conversation had switched back to Pro before authorizing the repair.

  product_surface:
    value: standard_ChatGPT_conversation_with_GitHub_app
    evidence:
      - class: operator_observed
        ref: current_tool_environment
        observed_or_accessed_at: 2026-07-31
        claim_scope: product_surface_used_for_repository_actions
        detail: GitHub connector actions were invoked from the current ChatGPT conversation.

  operator_selection:
    verbatim: "pro模型"
    evidence:
      - class: operator_reported
        ref: current_conversation_user_message_starting_MNEMOSYNE_186
        observed_or_accessed_at: 2026-07-31
        claim_scope: operator_visible_or_reported_selection
        detail: This does not attest the exact served backend.

  backend:
    status: unknown_or_not_attestable
    reason: Consumer-chat picker wording and model behavior do not attest the exact served backend.

  artifacts:
    status: recorded
    refs:
      - ref: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.2.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: null
      - ref: notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.2.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: null
      - ref: notes/research-operations/claude-fable5-repository-bound-static-audit-v0.2.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: null
      - ref: notes/research-plans/2026Q3-frontier-clarification-validation-fable5-staged-plan-v0.3.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: null
      - ref: raw/research-reports/cycles/2026Q3-frontier-clarification-validation-stage-a/manifest.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: null
      - ref: notes/mnemosyne-maintenance-issues/META-AGENT-RESEARCH-EVIDENCE-INCIDENT-001-failed-branch-retention-assessment.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: null

  user_authorization:
    status: authorized
    actor: user
    decision_ref: current_conversation_user_message_starting_MNEMOSYNE_186
    authorized_actions:
      - repair_the_Fable5_A1_A2_delivery_and_execution_surface
      - preserve_and_adjudicate_the_returned_A1_failure_evidence
      - update_repository_guidance_and_status_files_needed_for_the_repair
      - create_one_branch_and_pull_request
      - load_latest_Mnemosyne_guidance_after_repair
      - assess_whether_failed_historical_branches_should_be_deleted
    excluded_actions:
      - delete_failed_branches_without_a_separate_explicit_decision
      - run_Fable5_or_Deep_Research
      - execute_V0_V1_V2_or_V3
      - modify_current_human_approved_spec
      - modify_Meta_Agent_target_truth_or_take_over_product_build
      - merge_or_enable_auto_merge
    evidence:
      - class: direct_user_instruction
        ref: current_conversation_user_message_starting_MNEMOSYNE_186
        observed_or_accessed_at: 2026-07-31
        claim_scope: current_task_repository_write_and_analysis_authorization
        detail: The user explicitly authorized repair and requested a branch-deletion assessment.
    expires_with_task: true
    not_future_precedent: true

  limitations:
    - The exact Fable billing record was not supplied; USD 8 is an approximate operator report.
    - No live revised Fable run was performed by MNEMOSYNE-186.
    - No local repository clone or independent parser was available; verification is connector-backed plus cross-document review.
    - Exact backend identity is unknown or not attestable.

  omissions:
    - field: provider_normalization
      reason: not_available
      detail: No current official mapping was needed for this task; the operator wording is preserved without backend inference.
```

```yaml
segments:
  - segment_id: MNEMOSYNE_186_S1
    order: 1
    time_window: current_task_after_user_reported_switch_to_Pro
    action_actor: ChatGPT
    product_surface:
      value: standard_ChatGPT_conversation_with_GitHub_app
      evidence:
        - class: operator_observed
          ref: current_tool_environment
          observed_or_accessed_at: 2026-07-31
          claim_scope: repository_action_surface
          detail: GitHub actions were performed through the connected app.
    operator_selection:
      verbatim: "pro模型"
      evidence:
        - class: operator_reported
          ref: current_conversation_user_message_starting_MNEMOSYNE_186
          observed_or_accessed_at: 2026-07-31
          claim_scope: operator_selection_for_this_task
          detail: Exact backend remains unknown.
    operator_reasoning_setting:
      verbatim: unknown_not_separately_reported
      evidence:
        - class: unknown_or_not_attestable
          ref: null
          observed_or_accessed_at: 2026-07-31
          claim_scope: reasoning_setting
          detail: No distinct reasoning-setting receipt was provided.
    provider_normalization_ref: null
    conversation_or_run_ref: current_Mnemosyne_maintenance_conversation
    artifact_or_commit_refs: []
    attribution_status: best_supported
    limitations:
      - Consumer-chat backend identity is not attested.
```

## 3. A1 failure adjudication

The operator supplied:

- a four-path ordinary-chat GitHub preflight marked `PASS`;
- a pre-launch claim that all 19 audit inputs were fully retrieved;
- a paid Advanced Research run that ended with `INPUT_OR_REPOSITORY_INTEGRITY_FAILURE`;
- an uploaded final-response Markdown file of 5,139 bytes with SHA-256 `f32daf913326e4feabbeb72f6239977d35332f3b889d01de1222de8f19a24450`;
- an approximate USD 8 quota-cost observation.

```yaml
A1_run_001:
  canonical_task_complete_read: best_supported_true
  canonical_task_final_heading: "## 17. Delivery and authority boundary"
  ordinary_chat_repository_access: reported_PASS
  Advanced_Research_repository_evidence_access: failed_18_of_18
  substantive_audit_started: false
  substantive_report_received: false
  fail_closed_behavior: PASS
  cost_control_behavior: FAIL
  accepted_role: execution_surface_failure_evidence_only
```

The final response explicitly stated that the canonical task's sections 1–17 were read in full. Therefore the repair does not duplicate or rewrite the long audit specification. It adds a versioned execution contract and preserves the old task as the canonical audit criteria/report contract.

## 4. Repair design

```yaml
revised_current_surface:
  visible_model: Fable_5
  visible_effort: Max
  Advanced_Research: false_for_entire_run
  chat_level_GitHub: required
  Project_Files: empty_by_default
  repository_gate_and_substantive_work_same_ordinary_chat: required
  ordinary_web_search:
    during_full_repository_gate: false
    after_gate_PASS: targeted_only
```

The four-path sample preflight is replaced by a full manifest gate:

```yaml
A1:
  support_paths: 3
  mandatory_audit_inputs: 19
  total_gate_paths: 22
A2:
  support_paths: 3
  mandatory_audit_inputs: 12
  total_gate_paths: 15
```

The canonical A1/A2 research questions and report sections are unchanged. The v0.2 execution contracts control only surface, context continuity, full input binding, cost protection, failure semantics, and delivery mechanics.

## 5. Failed-run evidence preservation

Created:

```text
raw/research-reports/cycles/2026Q3-frontier-clarification-validation-stage-a/manifest.md
raw/research-reports/cycles/2026Q3-frontier-clarification-validation-stage-a/failed-runs/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-run-001/operator-preflight-and-launch-receipt.md
raw/research-reports/cycles/2026Q3-frontier-clarification-validation-stage-a/failed-runs/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-run-001/research-final-response-readable-copy.md
raw/research-reports/cycles/2026Q3-frontier-clarification-validation-stage-a/failed-runs/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-run-001/maintainer-run-assessment.md
```

The uploaded file hash is preserved, while the repository copy is explicitly a normalized readable copy rather than an exact-byte archive.

## 6. Branch retention assessment

Current non-master failed branches:

```yaml
meta-agent-research-evidence-001:
  relation_to_master: diverged
  ahead_by: 2
  behind_by: 44
  evidence_value: real_README_manifest_overclaim_fixture
meta-agent-research-evidence-repair-001:
  relation_to_master: behind
  ahead_by: 0
  behind_by: 21
  evidence_value: empty_branch_no_PR_fixture
meta-agent-research-evidence-repair-002:
  relation_to_master: diverged
  ahead_by: 3
  behind_by: 21
  evidence_value: incomplete_multipart_fixture
```

Disposition:

```yaml
current_recommendation: RETAIN
reason:
  - process_repair_and_validation_are_deferred_not_closed
  - branch_001_and_repair_002_remain_useful_real_failure_fixtures
  - no_complete_branch_head_and_blob_snapshot_package_exists_on_master
  - branch_cleanup_requires_a_separate_explicit_user_decision
branch_deletion_performed: false
```

## 7. Files changed before result/finalization

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
notes/research-prompts/README.md
```

Created:

```text
notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.2.md
notes/research-prompts/FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001-execution-contract-v0.2.md
notes/research-operations/claude-fable5-repository-bound-static-audit-v0.2.md
notes/research-plans/2026Q3-frontier-clarification-validation-fable5-staged-plan-v0.3.md
notes/mnemosyne-maintenance-issues/META-AGENT-RESEARCH-EVIDENCE-INCIDENT-001-failed-branch-retention-assessment.md
raw/research-reports/cycles/2026Q3-frontier-clarification-validation-stage-a/manifest.md
raw/research-reports/cycles/2026Q3-frontier-clarification-validation-stage-a/failed-runs/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-run-001/operator-preflight-and-launch-receipt.md
raw/research-reports/cycles/2026Q3-frontier-clarification-validation-stage-a/failed-runs/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-run-001/research-final-response-readable-copy.md
raw/research-reports/cycles/2026Q3-frontier-clarification-validation-stage-a/failed-runs/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-run-001/maintainer-run-assessment.md
```

## 8. Protected boundaries

Unchanged:

```text
current/human-approved-spec.md
current/github-single-active-pr-lineage-guard.md
target-projects/meta-agent/
handoff/handoff-current.md
current/active-context.md
current/todo.md
current/open-questions.md
non-FABLE health-review route
validation package contents
manual-surface candidate contents
```

No Fable run, Deep Research run, validation cell, surface selection, branch deletion, merge, or auto-merge was performed.

## 9. Verification before result record

```yaml
compare:
  base: 7bcddd60e209afe6496fa3091332496e20c3e245
  status: ahead
  ahead_by: 20
  behind_by: 0
  changed_files: 20
open_PRs_before_branch: []
open_PRs_before_result_record: not_yet_rechecked
```

Final PR identity, final head, changed paths, status checks, workflow runs, and independent PR reread belong in the companion finalization record.

## 10. Capability and research assessment

```yaml
model_capability_estimate:
  failed_run_adjudication_and_surface_repair: FRONTIER_RECOMMENDED
  full_repository_input_gate: NEXT_TIER_SUFFICIENT_CANDIDATE_or_human
  deterministic_manifest_checks: MECHANICAL_ONLY
  revised_static_audit_execution: Fable_5_Max_ordinary_chat_requested
  report_adjudication: FRONTIER_RECOMMENDED

research_assessment:
  additional_Pro_Deep_Research: NOT_NEEDED
  additional_Fable_research_about_the_failure: NOT_NEEDED
  reason: direct_run_evidence_is_sufficient_for_the_bounded_surface_repair
```

## 11. Safe next action

Human review of the canonical MNEMOSYNE-186 PR is required. After merge, the user may rerun A1 using the complete same-ordinary-chat flow, keep Advanced Research off, and return the input-binding receipt plus complete report. A2 remains separately optional and should generally wait for A1 adjudication.
