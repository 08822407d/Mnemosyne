---
target_project_id: meta-agent
artifact_id: META-AGENT-V0.1-DECISION-VERSION-MIGRATION-LOG-001
artifact_role: reviewed_history_version_lineage_migration_and_rollback
status: initialized_pending_owner_acceptance
authority_level: reviewed_history_and_migration_record
target_runtime_truth_source: false
created_by_task: MNEMOSYNE-171
design_version: 0.1.0
schema_version: 0.1.0
policy_version: 0.1.0
delivery_version: 0.1.0
source_refs:
  - https://github.com/08822407d/Mnemosyne/pull/221
  - notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M0-requirements-and-authority-baseline.md
  - notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M1-workspace-safety-build-manifest.md
  - notes/first-target-minimum-upgrade-contract-v0.1.md
known_limits:
  - public_Git_history_cannot_be_promised_erased
  - no_prior_operational_Meta_Agent_state_existed
---

# Meta-Agent Decision, Version and Migration Log v0.1

## 1. Initial decision records

### MA-DEC-0001 — Select product-build launch route

```yaml
id: MA-DEC-0001
decision: select_META_AGENT_PRODUCT_BUILD_LAUNCH_PREPARATION
status: accepted
source_ref: current_conversation_user_instruction_after_PR_220_merge
effect:
  - product_build_route_selected
  - M0_and_M1_required_before_target_files
```

### MA-DEC-0002 — Accept M0 and M1 baseline

```yaml
id: MA-DEC-0002
decision: accept_Meta_Agent_v0_1_M0_and_M1
status: accepted_by_human_merge
source_ref: https://github.com/08822407d/Mnemosyne/pull/221
effect:
  - requirements_and_authority_baseline_accepted
  - workspace_safety_manifest_and_upgrade_profile_accepted
  - M2_requires_fresh_authorization
```

### MA-DEC-0003 — Select owner and designated runtime truth path

```yaml
id: MA-DEC-0003
decision:
  owner: user
  designated_runtime_truth_source: target-projects/meta-agent/current/approved-spec.md
  Mnemosyne_role: design_archive_control_plane_and_bootstrap_host
status: accepted_in_M0
source_ref: notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M0-requirements-and-authority-baseline.md
```

### MA-DEC-0004 — Select public-risk bootstrap workspace and safe-input default

```yaml
id: MA-DEC-0004
decision:
  workspace_root: target-projects/meta-agent/
  visibility_treatment: public_risk
  private_original_default: outside_git
  allowed_material: public_synthetic_redacted_safe_pointer_or_reviewed_non_sensitive_summary
status: accepted_in_M1
source_ref: notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M1-workspace-safety-build-manifest.md
```

### MA-DEC-0005 — Select standard upgrade profile

```yaml
id: MA-DEC-0005
decision:
  contract_id: META-AGENT-V0.1-UPGRADE-CONTRACT-001
  profile: standard
  unnecessary_service_architecture_required: false
status: accepted_in_M1
source_ref: current/first-target-minimum-upgrade-contract-status.md
```

### MA-DEC-0006 — Authorize exact seven-file M2 construction

```yaml
id: MA-DEC-0006
decision:
  task_id: MNEMOSYNE-171
  exact_target_file_count: 7
  operational_use_in_same_task: false
status: authorized
source_ref: current_conversation_user_instruction_after_PR_221_merge
```

## 2. Initial version set

```yaml
version_set:
  design_version: 0.1.0
  schema_version: 0.1.0
  policy_version: 0.1.0
  delivery_version: 0.1.0
  derived_transformation_context: none
  operational_status: pending_owner_acceptance
```

Version meanings:

- `design_version`: target memory/method architecture;
- `schema_version`: object fields and relations;
- `policy_version`: authority, update, privacy and promotion rules;
- `delivery_version`: concrete seven-file package;
- transformation context: how derived views were produced; none exist in v0.1.

## 3. Stable ID rules and issued ranges

```yaml
ID_rules:
  format: prefix_plus_zero_padded_sequence
  stable_after_creation: true
  ID_reuse_after_retirement: prohibited
  rename_split_merge_replace_retire_requires_mapping: true
  semantic_meaning_not_encoded_too_rigidly: true

issued:
  requirements: MA-REQ-0001_through_MA-REQ-0016
  pending_requirements: MA-PEND-0001_through_MA-PEND-0008
  decisions: MA-DEC-0001_through_MA-DEC-0006
  methods: MA-METHOD-0001_through_MA-METHOD-0006
  cases: []
  feedback: []
  evaluations: []
  migrations:
    - MA-MIG-0001
```

IDs shown as schema examples in the case ledger are not issued entries.

## 4. Bootstrap transition — MA-MIG-0001

```yaml
migration_record:
  migration_id: MA-MIG-0001
  type: bootstrap_initialization
  status: built_pending_owner_acceptance

  from_state:
    repository_ref: master@8ff567c6cd5020bd05e13034866825fdb6473f4a
    target_workspace: absent
    target_runtime_truth_source: absent
    design_version: none
    schema_version: none
    policy_version: none
    delivery_version: none

  to_state:
    target_workspace: target-projects/meta-agent/
    target_file_count: 7
    designated_runtime_truth_source: target-projects/meta-agent/current/approved-spec.md
    operational_effect: pending_owner_acceptance
    design_version: 0.1.0
    schema_version: 0.1.0
    policy_version: 0.1.0
    delivery_version: 0.1.0

  prior_object_mappings: not_applicable_no_prior_target_objects
  created_objects:
    - META-AGENT-V0.1-APPROVED-SPEC-001
    - META-AGENT-V0.1-ACTIVE-CONTEXT-001
    - META-AGENT-V0.1-SOURCE-OWNER-MAP-001
    - META-AGENT-V0.1-CORE-METHODOLOGY-001
    - META-AGENT-V0.1-CASE-FEEDBACK-LEDGER-001
    - META-AGENT-V0.1-DECISION-VERSION-MIGRATION-LOG-001
    - META-AGENT-V0.1-HANDOFF-001

  validation_required:
    - exact_seven_file_inventory
    - MA_REQ_0001_through_MA_REQ_0016_present
    - stable_ID_uniqueness
    - version_fields_present
    - source_and_authority_roles_separated
    - prohibited_material_absent
    - no_automatic_methodology_promotion
    - handoff_and_safe_next_action_present
    - rollback_record_present

  owner_disposition: pending
```

No previous target runtime was migrated. The ID exists so the bootstrap transition and its rollback boundary remain traceable.

## 5. Future object-mapping schema

```yaml
object_mapping:
  old_id:
  new_id_or_ids: []
  relation: unchanged | renamed | moved | reformatted | superseded | split_into | merged_from | replaced_by | retired | recomputed_from | unmappable_requires_human_review
  authority_changed: false
  source_refs_preserved: true
  rationale:
  validation_ref:
  owner_decision_ref:
```

A mapping records lineage; it does not by itself prove semantic equivalence.

## 6. Preserve, transform, recompute and retire defaults

| Artifact | Default |
|---|---|
| raw/source evidence | preserve or retain approved external pointer |
| confirmed requirements and owner decisions | preserve; supersede only explicitly |
| target execution source | controlled migration with owner review |
| current state | transform with freshness checks |
| summaries, indexes and derived profiles | recompute where practical |
| embeddings | recompute after model/chunking change |
| handoff | preserve relevant history; regenerate current handoff |
| rejected/retired candidates | preserve minimal status to prevent resurrection |
| ephemeral scratch | retire unless explicitly promoted |

## 7. Change classes

```yaml
change_classes:
  Class_0_presentation:
    minimum_gate: diff_review_and_identity_preservation
  Class_1_additive_compatible:
    minimum_gate: schema_or_delivery_version_and_backward_read_check
  Class_2_semantic_or_breaking:
    minimum_gate: MA_MIG_mapping_semantic_review_regression_owner_approval
  Class_3_authority_privacy_or_trust:
    minimum_gate: frontier_review_explicit_user_decision_mechanical_evidence_target_rollback
  Class_4_storage_or_runtime_platform:
    minimum_gate: data_and_authority_mapping_export_recovery_staged_validation_no_dual_truth
```

## 8. Rollback plan for MA-MIG-0001

```yaml
rollback_plan:
  rollback_id: META-AGENT-V0.1-ROLLBACK-001
  migration_ref: MA-MIG-0001
  previous_state_ref: master@8ff567c6cd5020bd05e13034866825fdb6473f4a

  before_M2_merge:
    action: close_or_replace_the_single_MNEMOSYNE_171_PR
    target_workspace_on_master: absent

  after_M2_merge_before_operational_acceptance:
    action: revert_the_M2_merge_or_supersede_with_reviewed_v0_1_1
    target_runtime_truth_effective_before_acceptance: false

  after_operational_acceptance:
    action: use_owner_approved_MA_MIG_change_record_and_versioned_revision

  derived_artifacts_to_discard_or_rebuild: []
  non_reversible_limitations:
    - public_Git_history_cannot_be_promised_erased
    - forks_caches_or_external_copies_may_persist
  authority_during_rollback:
    - user_remains_final_authority
    - no_target_spec_is_operational_until_an_accepted_state_is_declared
  verification_after_rollback:
    - target_paths_absent_or_marked_superseded
    - no_competing_truth_source
    - current_context_and_handoff_updated
    - owner_disposition_recorded
```

“Keep a backup” alone is not a rollback plan.

## 9. Current acceptance record

```yaml
M2_build_acceptance:
  repository_build: pending_canonical_PR_merge
  owner_operational_acceptance: pending
  accepted_for_operation: false
  next_required_decision:
    - ACCEPT_V0_1_FOR_BOUNDED_OPERATIONAL_PILOT
    - ACCEPT_WITH_LIMITATIONS
    - REQUEST_REVISION
    - REJECT_AND_ROLL_BACK
```
