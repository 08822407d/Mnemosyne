# Target-Project Dedicated Repository Migration Handoff Template v0.1

> Template for notifying a target Agent after a repository move. It is not an execution source, migration authorization, or completed handoff.

```yaml
template_id: MNEMOSYNE-TARGET-REPOSITORY-MIGRATION-HANDOFF-TEMPLATE-001
created_by_task: MNEMOSYNE-189
version: 0.1.0
status: template_not_instantiated
```

## 1. Migration handoff package

```yaml
migration_handoff:
  package_id:
  target_project_id:
  migration_id:
  prepared_at:

  source:
    repository:
    last_authoritative_commit:
    old_target_root:
    old_truth_path:
    old_path_disposition: active_until_cutover | historical_tombstone | rollback_only

  destination:
    repository:
    visibility:
    default_branch:
    verified_commit:
    new_target_root:
    new_truth_path:
    authority_status: shadow_non_authoritative | active_after_owner_cutover

  mapping:
    manifest_path:
    exact_source_inventory_count:
    exact_destination_inventory_count:
    preserved_objects: []
    transformed_objects: []
    recomputed_objects: []
    retired_objects: []
    unmapped_or_blocked: []

  behavior:
    destination_guidance_path:
    destination_load_command:
    source_Mnemosyne_snapshot:
      repository:
      commit:
      guard_paths: []
    adopted_semantics: []
    explicitly_excluded_Mnemosyne_semantics: []
    compatibility_guard_disposition:

  authority:
    owner:
    target_truth_effective_for_operational_use:
    operational_activation_authorized:
    private_material_authorized:
    repository_write_authority:
    no_dual_writer_status:

  validation:
    copy_identity_result:
    fresh_session_recovery_result:
    behavior_equivalence_result:
    destination_PR_capability_result:
    rollback_rehearsal_result:
    evidence_refs: []

  handoff:
    active_context_path:
    handoff_current_path:
    startup_prompt_path:
    safe_next_action:

  rollback:
    window:
    trigger_conditions: []
    exact_recovery_ref:
    old_path_reactivation_requires_owner_decision: true

  limitations_or_unknowns: []
```

## 2. Receive-only startup prompt template

```text
@GitHub Perform a receive-only target-repository migration handoff.

Target project: <TARGET_PROJECT_ID>
Destination repository: <OWNER/REPOSITORY>
Pinned destination ref: <COMMIT>
Migration handoff: <PATH>

Read the migration handoff, destination target truth, authority map, active
context, behavior guidance, migration mapping, current handoff and rollback
record in the exact order specified by the package.

Do not read the old Mnemosyne target path as current truth. Read it only if the
migration package explicitly requires a historical or rollback check.

First round only: return the structured migration_handoff_receive object below,
then stop. Do not modify either repository, create a branch or PR, start a
prototype/pilot/research run, ingest material, change target truth, or activate
the target.

migration_handoff_receive:
  target_project_id:
  migration_id:
  destination_repository:
  pinned_destination_ref:
  destination_paths_complete:
  designated_truth_path:
  truth_effective_status:
  owner:
  behavior_guidance_path:
  behavior_guidance_loaded:
  Mnemosyne_maintenance_route_imported: false
  old_repository_and_path_role:
  no_dual_writer_status:
  operational_activation_authorized:
  private_material_authorized:
  open_or_related_PRs:
  safe_next_action:
  conflicts_or_unknowns: []
  repository_write_performed: false
  status: RECEIVED | INPUT_OR_STATE_CONFLICT | BLOCKED
```

## 3. Required first-round checks

The receiver must verify:

1. destination repository and pinned commit;
2. exact designated truth path;
3. shadow versus active cutover state;
4. owner and authority precedence;
5. destination behavior guidance and loader;
6. old path disposition;
7. no dual writer;
8. current open PRs and stale branches when visible;
9. no implicit activation, private material, prototype, or pilot;
10. exactly one safe next action.

## 4. Meta-Agent specialization

A Meta-Agent migration instance must additionally state:

```yaml
Meta_Agent_required_fields:
  established_project_abbreviation: MA
  issued_MA_DR_range:
  sole_truth_object_ID: META-AGENT-V0.1-APPROVED-SPEC-001
  owner_acceptance_state: ACCEPT_WITH_LIMITATIONS
  operational_state: inactive_unless_separately_changed
  MA_MIG_record:
  post_research_handoff_state:
  Mnemosyne_guidance_compatibility_guard_disposition:
  target_owned_behavior_guidance_path:
```

The destination loader must not import Mnemosyne's current maintenance state, handoff, TODO, open questions, Fable A1/A2 route, or another target project.

## 5. Historical redirect in Mnemosyne

After successful cutover, the old target root should retain a compact tombstone rather than a live mirror:

```yaml
migration_tombstone:
  target_project_id:
  status: historical_migrated_not_current
  last_authoritative_source_commit:
  destination_repository:
  destination_cutover_commit:
  destination_truth_path:
  migration_record:
  rollback_record:
  active_writes_here: prohibited
```

The tombstone must not claim public Git history was erased.

## 6. Boundaries

- Instantiating this template requires a separate target-scoped task.
- A copied package remains non-authoritative until Owner cutover.
- A handoff does not authorize repository writes or operation.
- The receiver must stop on missing or conflicting authority state.
