# MNEMOSYNE-189 Result — External Research Display Names and Target-Repository Migration Preparation

```yaml
task_id: MNEMOSYNE-189
record_id: MNEMOSYNE-189-RESULT-001
record_role: important_repository_writing_task_result
status: implementation_complete_pending_PR_creation_and_human_review
repository: 08822407d/Mnemosyne
base_branch: master
base_sha: ca0926a9d67f10e60d8e97373370daa792c6eacb
canonical_branch: mnemosyne-189-research-display-names-and-target-repo-migration
canonical_PR: pending_creation
source_issue: 250
execution_source_modified: false
Meta_Agent_target_truth_modified: false
migration_performed: false
new_repository_created: false
external_research_executed: false
```

## 1. User decisions and authorized scope

The user instructed this task to:

1. formally implement the short display-name behavior constraint recorded in Issue #250;
2. account for PR #251 and PR #252 already being assigned and merged rather than guessing the next PR number;
3. evaluate a future Meta-Agent move to a dedicated repository;
4. define what must be transferred and communicated so behavior remains equivalent;
5. design tests for moving target-specific content into target-owned repositories and creating PRs there.

Authorized repository actions:

```yaml
allowed:
  - create_one_MNEMOSYNE_189_branch
  - add_or_update_Mnemosyne_behavior_navigation_assessment_validation_and_template_files
  - update_A1_A2_display_alias_metadata_without_resuming_research
  - create_at_most_one_canonical_PR
prohibited:
  - modify_current_human_approved_spec
  - modify_Meta_Agent_target_truth_or_accepted_methodology
  - create_or_cut_over_a_Meta_Agent_repository
  - execute_migration_or_cross_repository_write_test
  - run_Fable_or_Deep_Research
  - execute_V0_V1_or_other_validation
  - merge_PR_or_enable_auto_merge
```

## 2. Lineage preflight

```yaml
github_write_lineage_preflight:
  task_id: MNEMOSYNE-189
  intended_scope_summary: adopt_external_research_display_names_and_prepare_target_repository_migration_assessment_validation_and_handoff
  default_branch: master
  pinned_default_branch_sha: ca0926a9d67f10e60d8e97373370daa792c6eacb
  intended_branch: mnemosyne-189-research-display-names-and-target-repo-migration
  accessible_open_PRs_before_branch: []
  exact_task_repository_matches_before_branch: []
  intended_branch_matches_before_branch: []
  Issue_250_exists: true
  PR_251_merged: true
  PR_252_merged: true
  decision: create_new_lineage
```

GitHub assigns issue and pull-request numbers from the same repository sequence. The task ID and branch are stable; the PR number is left unknown until the create-PR action returns it.

## 3. Implemented display-name constraint

Created:

```text
current/external-research-display-name-guard.md
notes/registries/project-research-display-name-registry-v0.1.md
notes/external-research-display-name-constraint-adoption-record.md
```

Adopted behavior:

```yaml
format: <PROJECT_ABBR>-DR-<SEQUENCE> <SHORT_TOPIC>
Mnemosyne_abbreviation: MNE
Meta_Agent_abbreviation: MA
new_project_default_sequence_width: 3
established_project_numbering_preserved: true
canonical_task_ID_remains_separate: true
```

Initial Mnemosyne aliases:

```yaml
MNE-DR-001_验证包审计:
  canonical_task: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
MNE-DR-002_表面威胁:
  canonical_task: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
```

Existing Meta-Agent canonical IDs such as `MA-DR-08` through `MA-DR-15` remain unchanged. Future allocation belongs to the Meta-Agent route.

The guidance loader and README wayfinding were updated. A1/A2 task, manifest and operator files now expose their short Project names without resuming either task.

## 4. Migration assessment and validation preparation

Created:

```text
notes/migration-designs/meta-agent-dedicated-repository-migration-assessment-v0.1.md
notes/validation-designs/target-project-dedicated-repository-migration-and-pr-validation-v0.1.md
notes/templates/target-project-dedicated-repository-migration-handoff-v0.1.md
```

Current migration disposition:

```yaml
disposition: PREPARE_AND_VALIDATE_BEFORE_CUTOVER
migration_selected: false
repository_created: false
copy_performed: false
cutover_performed: false
```

The design preserves these invariants:

- one active target truth;
- one active writer;
- copy is not cutover;
- old path becomes historical/tombstoned only after Owner cutover;
- destination behavior guidance must be Meta-Agent-owned and versioned;
- Mnemosyne maintenance state must not be imported;
- rollback and no-dual-writer behavior are tested before cutover;
- destination PR capability is surface- and permission-dependent.

## 5. Proposed test program

The validation design defines:

```yaml
T0: source_inventory_and_freeze
T1: mapping_and_shadow_package
T2: separately_authorized_shadow_copy_and_draft_PR
T3: two_fresh_destination_only_recovery_runs
T4: behavior_equivalence_cases
T5: synthetic_cross_repository_PR_capability
T6: rollback_and_no_dual_writer_rehearsal
T7: human_only_cutover_decision
```

Two campaigns are proposed:

- Meta-Agent dedicated-repository campaign after the Owner selects a destination;
- disposable generic target-repository campaign proving a Mnemosyne-to-target PR workflow.

No campaign is selected or executed by this task.

## 6. Product-surface facts and limitations

Current official OpenAI documentation states that the standard ChatGPT GitHub app is read-only for repository analysis/search. Codex is documented as able to work on repository tasks and propose pull requests. Therefore a cross-repository PR test must bind to the actual write-capable surface and observed actions rather than infer capability from a generic GitHub connection.

A full Git mirror duplicates the whole repository and is not by itself a subdirectory extraction. The assessment therefore recommends an exact snapshot plus immutable source manifest as the initial low-risk history strategy, with filtered history optional only if measured value justifies it.

No destination repository currently exists in the accessible repository search. Destination name, visibility, path mapping, history strategy, writer surface and cutover remain Owner decisions.

## 7. Protected boundaries

Unchanged:

```text
current/human-approved-spec.md
target-projects/meta-agent/current/approved-spec.md
target-projects/meta-agent/authority/source-and-owner-map.md
target-projects/meta-agent/methodology/core-methodology.md
target-projects/meta-agent/cases/case-and-feedback-ledger.md
target-projects/meta-agent/history/decision-version-and-migration-log.md
target-projects/meta-agent/handoff/handoff-current.md
```

The Meta-Agent route remains owned by its dedicated conversation. The migration assessment is Mnemosyne design/validation support, not a target-truth change or route takeover.

## 8. Run context

```yaml
run_context:
  schema_and_task:
    record_version: v0.2
    task_id: MNEMOSYNE-189
    record_id: MNEMOSYNE-189-RESULT-001

  date_or_window:
    started_at: 2026-08-05
    completed_or_recorded_at: 2026-08-05

  action:
    actor: ChatGPT
    actor_kind: model
    source: current_Mnemosyne_conversation_and_GitHub_connector
    switch_history:
      status: recorded
      evidence:
        - class: direct_user_instruction
          ref: current_conversation_user_report
          observed_or_accessed_at: 2026-08-05
          claim_scope: operator_switched_current_conversation_back_to_Pro_before_MNEMOSYNE_189
          detail: The user reported the conversation was switched back to Pro; exact served backend remains unattested.

  product_surface:
    value: standard_ChatGPT_conversation_with_write_capable_GitHub_connector_actions
    evidence:
      - class: operator_observed
        ref: GitHub_action_receipts_for_MNEMOSYNE_189
        observed_or_accessed_at: 2026-08-05
        claim_scope: product_surface_and_repository_actions
        detail: Branch, file and repository-read actions were returned by the installed GitHub connector.

  operator_selection:
    verbatim: "现在对话已经切换回pro模型"
    evidence:
      - class: direct_user_instruction
        ref: current_conversation_user_message
        observed_or_accessed_at: 2026-08-05
        claim_scope: operator_reported_selection_only
        detail: Does not attest the particular request backend.

  backend:
    status: unknown_or_not_attestable
    reason: Consumer-chat picker wording and model behavior do not attest the exact served backend.

  artifacts:
    status: recorded
    refs:
      - ref: current/external-research-display-name-guard.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: branch_bound
      - ref: notes/registries/project-research-display-name-registry-v0.1.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: branch_bound
      - ref: notes/migration-designs/meta-agent-dedicated-repository-migration-assessment-v0.1.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: branch_bound
      - ref: notes/validation-designs/target-project-dedicated-repository-migration-and-pr-validation-v0.1.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: branch_bound
      - ref: notes/templates/target-project-dedicated-repository-migration-handoff-v0.1.md
        relation: created
        immutable_identity:
          status: not_available_before_merge
          type: git_blob_sha
          value: branch_bound

  user_authorization:
    status: authorized
    actor: user
    decision_ref: current_conversation_instruction_to_formally_implement_constraint_and_evaluate_migration
    authorized_actions:
      - write_Mnemosyne_behavior_and_support_artifacts
      - create_one_branch_and_one_PR
      - assess_and_design_without_executing_migration
    excluded_actions:
      - modify_execution_source
      - modify_Meta_Agent_target_truth
      - create_destination_repository
      - execute_cutover_or_external_research
      - merge_PR
    evidence:
      - class: direct_user_instruction
        ref: current_conversation_user_message
        observed_or_accessed_at: 2026-08-05
        claim_scope: task_local_repository_write_and_assessment_authorization
        detail: Authorization expires with MNEMOSYNE-189.
    expires_with_task: true
    not_future_precedent: true

  limitations:
    - Destination repository identity and visibility are not selected.
    - Cross-repository write capability is not executed or certified.
    - Exact consumer-chat backend is not attestable.
    - No CI evidence is claimed unless later GitHub status or workflow receipts exist.

  omissions:
    - field: provider_normalization
      reason: not_available
      detail: No exact-request provider mapping or metadata is available.
    - field: human_adjudication
      reason: not_available
      detail: Human PR review and merge are pending.
```

## 9. Safe next gate

After the single canonical PR is created and reviewed, human merge adopts the behavior guard and preserves the migration preparation artifacts. It does not create the new repository or start validation. A later Meta-Agent-owned migration-preparation task must receive separate Owner decisions and exact write authority.
