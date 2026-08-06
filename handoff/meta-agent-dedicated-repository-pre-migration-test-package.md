# Meta-Agent Dedicated-Repository Pre-Migration Test Package

> Receive-only handoff from the Mnemosyne migration-design route to the dedicated Meta-Agent product-build conversation. It does not change Meta-Agent target truth, initialize the destination repository, authorize a shadow copy, or select cutover.

```yaml
handoff_id: META-AGENT-DEDICATED-REPOSITORY-PRE-MIGRATION-HANDOFF-001
created_by_task: MNEMOSYNE-190
status: ready_after_MNEMOSYNE_190_merge
target_project_id: meta-agent
route: META_AGENT_PRODUCT_BUILD
source_repository: 08822407d/Mnemosyne
source_ref: fe09d0b76c9f94dc0c77fd0c2bb412e1d2cc0867
destination_repository: 08822407d/Meta-Agent
destination_state: empty_public_repository_no_commits_or_branches
migration_selected: false
first_round_write_authorized: false
```

## 1. Purpose

Transfer the verified repository-access facts, migration boundaries, and run-specific pre-migration test design to the Meta-Agent conversation that owns target-specific construction and migration.

The receiving conversation must not treat the existence of the new repository as a target-truth cutover. The current designated Meta-Agent truth remains:

```text
target-projects/meta-agent/current/approved-spec.md
```

at the pinned Mnemosyne source until a later explicit Owner cutover.

## 2. Runtime readiness checks

Before reading substantive files, verify:

```yaml
runtime_checks:
  Mnemosyne_PR_253:
    merged: true
    expected_merge_commit: fe09d0b76c9f94dc0c77fd0c2bb412e1d2cc0867
  Mnemosyne_pre_migration_package_visible_on_latest_master: true
  overlapping_open_Mnemosyne_or_Meta_Agent_migration_PRs: []
  destination_repository_accessible: true
  destination_repository: 08822407d/Meta-Agent
  destination_visibility: public
  destination_commits: 0
  destination_branches: 0
  destination_open_PRs: []
```

If the destination is no longer empty, do not assume the change is valid. Enumerate the new state and return `INPUT_OR_STATE_CONFLICT`.

## 3. Required reading order

Read from `08822407d/Mnemosyne` at the execution-time latest `master`, while binding the migration baseline to `fe09d0b76c9f94dc0c77fd0c2bb412e1d2cc0867` unless a later approved migration record supersedes it:

1. `current/human-approved-spec.md` for Mnemosyne process/safety authority only;
2. `notes/migration-designs/meta-agent-dedicated-repository-migration-assessment-v0.1.md`;
3. `notes/validation-designs/target-project-dedicated-repository-migration-and-pr-validation-v0.1.md`;
4. `notes/migration-designs/meta-agent-pre-migration-readiness-assessment-2026-08-06.md`;
5. `current/meta-agent-dedicated-repository-pre-migration-status.md`;
6. this handoff package;
7. `target-projects/meta-agent/current/approved-spec.md`;
8. `target-projects/meta-agent/authority/source-and-owner-map.md`;
9. `target-projects/meta-agent/current/active-context.md`;
10. `target-projects/meta-agent/current/meta-agent-mnemosyne-guidance-compatibility-guard.md`;
11. `target-projects/meta-agent/history/decision-version-and-migration-log.md`;
12. `target-projects/meta-agent/handoff/handoff-current.md`;
13. `target-projects/meta-agent/handoff/meta-agent-post-ma-dr-09-handoff-package.md`.

Read destination repository metadata independently. Do not use the empty destination as a substitute for the source target package.

## 4. First-round receive-only output

Return only:

```yaml
pre_migration_test_receive:
  handoff_id: META-AGENT-DEDICATED-REPOSITORY-PRE-MIGRATION-HANDOFF-001
  current_conversation_mainline: META_AGENT_PRODUCT_BUILD

  source:
    repository: 08822407d/Mnemosyne
    latest_master:
    migration_baseline_ref: fe09d0b76c9f94dc0c77fd0c2bb412e1d2cc0867
    required_paths_complete:
    target_truth_path: target-projects/meta-agent/current/approved-spec.md
    target_truth_effective_for_operational_use:

  destination:
    repository: 08822407d/Meta-Agent
    accessible:
    visibility:
    default_branch_configuration:
    commits:
    branches:
    open_PRs:
    connector_or_surface_observed:
    reported_platform_permissions:

  authority:
    user_owner: true
    migration_selected: false
    destination_initialization_authorized: false
    destination_shadow_copy_authorized: false
    cutover_authorized: false
    Meta_Agent_target_truth_modified: false
    no_dual_writer_status:

  behavior:
    temporary_Mnemosyne_compatibility_guard_read:
    destination_Meta_Agent_owned_guidance_exists: false
    behavior_migration_required: true
    Mnemosyne_maintenance_route_imported: false

  T0_readiness:
    result: PASS_WITH_INITIALIZATION_REQUIRED | BLOCKED | INVALID
    completed_checks: []
    missing_or_conflicting_checks: []

  proposed_T1_owner_decisions:
    - destination_repository_visibility_confirmation
    - initialization_actor_and_surface
    - initialization_exact_paths
    - destination_root_path_mapping
    - exact_snapshot_or_filtered_history
    - behavior_guidance_adoption_scope

  safe_next_action:
  repository_write_performed: false
  external_task_started: false
  status: RECEIVED | INPUT_OR_STATE_CONFLICT | BLOCKED
```

Then stop.

## 5. Prohibited first-round actions

Do not:

- create an initial commit in `08822407d/Meta-Agent`;
- create a branch, file, issue, comment, label, PR, or repository setting change;
- copy any Meta-Agent target file;
- modify Mnemosyne;
- change the target truth path or effectiveness state;
- adopt behavior guidance;
- start T2/T3/T4/T5/T6 validation;
- design or implement a prototype, pilot, private-data route, RAG, MCP, automation, or activation;
- infer that connector platform permissions equal task authorization.

## 6. After the receive report

The user may separately select one of:

```yaml
A_PREPARE_INITIALIZATION_DECISION_PACKAGE:
  write: false
  output:
    - exact_initial_commit_paths_and_content
    - initialization_surface
    - visibility_and_material_safety_receipt
    - rollback_and_cleanup

B_PREPARE_T0_T1_FULL_SOURCE_INVENTORY_AND_MAPPING:
  write: false
  output:
    - exact_source_tree_inventory
    - preserve_transform_recompute_retire_map
    - destination_path_map
    - behavior_compatibility_snapshot

C_AUTHORIZE_DESTINATION_INITIALIZATION:
  write: separately_authorized
  prerequisites:
    - A_and_B_reviewed
    - exact_task_local_action_context
    - one_active_writer

D_DEFER_OR_RETAIN_IN_MNEMOSYNE:
  write: false
```

No option is selected by this package.

## 7. Behavioral continuity requirement

Before any target copy is treated as usable, prepare Meta-Agent-owned behavior guidance covering the adopted subset of Mnemosyne process/safety controls and explicitly excluding Mnemosyne maintenance state. A later behavior-equivalence campaign must test at least:

- user-operation and next-step layout;
- capability/research assessment;
- cross-conversation execution intent;
- `MA-DR-*` display names;
- platform permission versus task authority;
- single-PR lineage;
- private-material boundary;
- wrong truth-source and route-import traps.

## 8. Boundary

This handoff is navigation and test preparation. It is not Meta-Agent target truth, migration authority, destination initialization authority, or operational activation.
