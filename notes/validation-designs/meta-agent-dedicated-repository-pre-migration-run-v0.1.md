# Meta-Agent Dedicated-Repository Pre-Migration Run v0.1

> Run-specific validation package binding the generic migration design to `08822407d/Meta-Agent`. T0 read-only readiness is recorded; all destination writes remain unselected and unauthorized.

```yaml
run_id: META-AGENT-DEDICATED-REPOSITORY-PRE-MIGRATION-RUN-001
created_by_task: MNEMOSYNE-190
status: T0_PASS_WITH_INITIALIZATION_REQUIRED_T1_RECEIVE_PACKAGE_READY
source_repository: 08822407d/Mnemosyne
source_ref: fe09d0b76c9f94dc0c77fd0c2bb412e1d2cc0867
source_root: target-projects/meta-agent/
destination_repository: 08822407d/Meta-Agent
destination_visibility: public
material_class: public_or_synthetic_only
destination_write_authorized: false
cutover_authorized: false
```

## 1. Run scope

This run validates:

- repository and connector visibility;
- empty destination state;
- current route and truth boundaries;
- readiness for a dedicated Meta-Agent receive-only migration intake;
- the next exact decisions needed before an initial commit or shadow PR.

This run does not validate:

- complete source-tree export identity;
- destination initialization;
- target-repository PR creation;
- destination-only recovery;
- behavior equivalence;
- cutover or operational activation.

## 2. T0 — repository access and state receipt

```yaml
T0_repository_access_and_state:
  observed_at: 2026-08-06

  source:
    repository: 08822407d/Mnemosyne
    latest_master: fe09d0b76c9f94dc0c77fd0c2bb412e1d2cc0867
    PR_253_merged: true
    Issue_250_closed: true
    open_PRs: []

  destination:
    repository: 08822407d/Meta-Agent
    connector_installation_visible: true
    visibility: public
    archived: false
    configured_default_branch_name: master
    size_reported: 0
    commits: 0
    branches: []
    open_PRs: []
    permissions_reported:
      admin: true
      maintain: true
      pull: true
      push: true
      triage: true

  product_surface:
    standard_ChatGPT_GitHub_app_documented_write_role: read_only
    current_installed_action_surface_exposes_write_actions: true
    destination_write_used_in_this_run: false

  result: PASS_WITH_INITIALIZATION_REQUIRED
```

## 3. T0 limitations

```yaml
limitations:
  - connector_permission_metadata_is_platform_permission_not_task_authorization
  - empty_repository_has_no_actual_default_branch_ref
  - no_destination_file_search_can_be_tested_before_first_content_exists
  - no_commit_or_PR_identity_exists_yet
  - complete_source_tree_inventory_not_generated_in_this_run
  - exact_backend_identity_unknown_or_not_attestable
```

## 4. T1 — receive-only target-route intake

```yaml
T1_receive_only_intake:
  actor: dedicated_Meta_Agent_conversation
  input_package: handoff/meta-agent-dedicated-repository-pre-migration-test-package.md
  startup_prompt: handoff/meta-agent-dedicated-repository-pre-migration-next-conversation-startup-prompt.md
  repository_write: false
  expected_result: pre_migration_test_receive
  status: READY_AFTER_MNEMOSYNE_190_MERGE
```

T1 passes only if the receiver:

- preserves `META_AGENT_PRODUCT_BUILD` as its mainline;
- recovers the current source truth and inactive operational state;
- recognizes the destination as empty/non-authoritative;
- does not import Mnemosyne maintenance;
- distinguishes platform permission from task authority;
- returns exactly one safe next action;
- performs no write.

## 5. T1 owner-decision package fields

After T1 passes, prepare but do not default:

```yaml
owner_decisions:
  destination_repository:
    full_name: 08822407d/Meta-Agent
    visibility_confirmation: public | change_before_initialization

  initialization:
    selected: yes | no | defer
    actor_surface: dedicated_Meta_Agent_conversation_GitHub_actions | Codex | human_manual
    exact_paths: []
    exact_content_refs: []

  destination_layout:
    path_strategy: project_root | preserve_target_projects_meta_agent_prefix | other

  history:
    strategy: exact_snapshot_with_Mnemosyne_pointer | filtered_subdirectory_history

  behavior:
    adopted_Mnemosyne_semantics: []
    excluded_Mnemosyne_specific_semantics: []
    destination_guidance_path:

  validation:
    authorize_shadow_copy: yes | no | defer
    authorize_synthetic_PR_test: yes | no | defer
```

## 6. T2 candidate — initialization

T2 remains blocked until Owner authorization.

Recommended exact purpose:

```yaml
T2_initialization_candidate:
  create_default_branch: true
  authority_effect: none
  destination_status: initialized_empty_non_authoritative
  minimum_paths:
    - README.md
    - MIGRATION-STATUS.md
  prohibited:
    - copy_target_truth
    - claim_cutover
    - private_material
    - operational_activation
    - create_second_branch_or_PR
```

Initialization may be a direct first commit because the repository has no base branch. All later shadow content should use a separate branch and draft PR.

## 7. T3 candidate — source inventory and mapping

Before shadow copy, freeze:

```yaml
source_inventory:
  pinned_source_ref:
  complete_target_root_paths: []
  exact_bytes_or_blob_IDs: []
  artifact_roles: []
  preserve_transform_recompute_retire: []
  restricted_or_external_material: []

mapping:
  source_to_destination_paths: []
  truth_path_change:
  behavior_guidance_transformation:
  active_context_regeneration:
  handoff_regeneration:
  old_path_tombstone:
  rollback_ref:
```

A partial search result is not a complete inventory.

## 8. T4 candidate — shadow PR

Separately authorize one branch and one draft PR in `08822407d/Meta-Agent`.

```yaml
shadow_PR_invariants:
  destination_initialized: true
  source_ref_pinned: true
  destination_base_SHA_pinned: true
  exact_path_allowlist: true
  destination_truth_effective: false
  shadow_non_authoritative_marker: present
  source_Mnemosyne_write: false
  destination_open_PR_count_for_task: 1
  merge: prohibited
```

## 9. T5 candidate — destination-only recovery and behavior equivalence

Use two independent fresh conversations. Each sees only the destination repository and the migration startup prompt.

Blocking checks:

- sole truth path;
- inactive/limited state;
- Owner and authority precedence;
- no Mnemosyne maintenance import;
- no permission-as-authority;
- correct `MA-DR-*` naming behavior;
- one-PR lineage;
- private-material boundary;
- safe next action;
- no write unless specifically authorized.

## 10. T6 candidate — synthetic cross-repository PR test

Test a non-truth, synthetic change after the destination is initialized.

```yaml
synthetic_test:
  target_path_candidate: tests/migration-capability/README.md
  source_design_ref: pinned_Mnemosyne_validation_package
  destination_base_ref: pinned
  branch: one
  draft_PR: at_most_one
  merge: false
  source_repo_write: false
  target_truth_change: false
```

The test passes only with final PR reread, exact changed-path match, and no unrelated mutations.

## 11. T7 — human cutover

Not part of this run.

```yaml
cutover_requirements:
  - full_source_inventory_and_mapping_pass
  - shadow_copy_identity_pass
  - two_fresh_recovery_runs_pass
  - behavior_equivalence_pass
  - repository_PR_capability_pass
  - rollback_and_no_dual_writer_pass
  - explicit_user_cutover_decision
```

## 12. Current disposition

```yaml
disposition:
  T0: PASS_WITH_INITIALIZATION_REQUIRED
  T1: READY_AFTER_MNEMOSYNE_190_MERGE
  T2_through_T6: NOT_AUTHORIZED
  T7: HUMAN_ONLY_NOT_SELECTED
  next_actor: dedicated_Meta_Agent_conversation
```
