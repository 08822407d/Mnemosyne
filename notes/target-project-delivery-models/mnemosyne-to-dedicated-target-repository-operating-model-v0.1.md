# Mnemosyne-to-Dedicated-Target-Repository Operating Model v0.1

> General target-project delivery model prepared from the Meta-Agent migration case. It defines how Mnemosyne conversations may continue designing and delivering memory systems after a target moves to its own repository. It does not authorize any particular target write or migration.

```yaml
model_id: MNEMOSYNE-TO-DEDICATED-TARGET-REPOSITORY-OPERATING-MODEL-001
created_by_task: MNEMOSYNE-190
version: 0.1.0
status: prepared_not_adopted_as_universal_automation
execution_source: false
primary_case: Meta_Agent
```

## 1. Core rule

```text
Mnemosyne designs and validates memory systems.
The target repository stores the target's live truth, state, handoff, and accepted target-owned memory artifacts.
```

A separate repository does not end Mnemosyne's role. It clarifies it.

## 2. Three-route model

### Route A — Mnemosyne design and memory-system route

Responsibilities:

- reconstruct target needs and constraints;
- design memory roles, schema, authority, retention, migration, validation, handoff, and rollback;
- preserve supporting research and architecture evidence;
- prepare exact target delivery manifests;
- create a candidate target-repository branch/PR when explicitly authorized and the write surface is validated;
- review drift and future upgrades.

It does not become target runtime truth.

### Route B — target construction and governance route

For Meta-Agent, this is the dedicated Meta-Agent construction conversation.

Responsibilities:

- own target-specific current work and decisions;
- read the target repository as the primary live source;
- review Mnemosyne delivery packages against target truth and Owner decisions;
- implement or supervise target-specific changes;
- maintain target active context and handoff;
- propose cutover, activation, and target-policy changes;
- prevent Mnemosyne-specific maintenance state from being imported.

### Route C — human Owner and merge/cutover route

Responsibilities:

- select repository visibility and destination;
- authorize target writes, private-material stores, and external side effects;
- merge or reject target PRs;
- approve target truth-location changes;
- approve operational activation and rollback.

## 3. Target-repository source-of-truth rule

After a successful cutover:

```yaml
target_repository:
  contains:
    - designated_target_truth
    - accepted_target_owned_behavior_guidance
    - current_state
    - authority_map
    - handoff
    - target_cases_feedback_and_research_evidence
  active_writer: exactly_one

Mnemosyne_repository:
  contains:
    - design_and_research_evidence
    - delivery_and_migration_manifests
    - validation_results
    - immutable_target_refs
    - historical_bootstrap_and_tombstone
  live_target_truth_copy: prohibited
```

A Mnemosyne summary of target state is a dated evidence view or pointer, never a second truth source.

## 4. Can Mnemosyne directly create PRs in target repositories?

Yes, when all conditions below pass:

```yaml
target_PR_gate:
  current_product_surface_has_observed_write_actions: true
  destination_repository_access_verified: true
  task_local_user_authorization: true
  target_owner_and_authority_read: true
  destination_base_SHA_pinned: true
  Mnemosyne_design_ref_pinned: true
  exact_target_paths_allowlisted: true
  one_task_one_branch_at_most_one_PR: true
  source_Mnemosyne_write_prohibited_unless_separately_authorized: true
  target_truth_or_authority_change_explicitly_classified: true
  rollback_or_revision_plan_present: true
  human_merge_required: true
```

The ordinary read-only ChatGPT GitHub app does not satisfy the write-surface condition. Codex or another explicitly write-capable action surface may.

## 5. Two delivery modes

### Bootstrap-host mode

Use when the target repository does not exist or the target design is too immature for cutover.

```yaml
location: Mnemosyne/target-projects/<target-id>/
role: temporary_bootstrap_workspace
truth_status: target_specific_declared_path_only
cutover_required_later: conditional
```

### Direct target-repository mode

Use when the target repository exists, access is validated, and target ownership is stable.

```yaml
location: target_owned_repository
role: target_truth_state_and_operation
Mnemosyne_role: design_delivery_validation_and_history
```

A target may remain in bootstrap-host mode indefinitely if measurable migration benefits do not justify a split.

## 6. Initial memory system before the target is mature

An incomplete target can still receive a useful memory system. The first version should be deliberately modest:

```yaml
initial_memory_profile:
  storage: versioned_text_files
  review: human_required
  material: public_synthetic_redacted_or_safe_pointer
  derived_indexes: optional_and_rebuildable
  private_material: not_authorized_by_default
  automatic_writeback: false
  automatic_method_promotion: false
  hidden_user_profile: prohibited
  operational_activation: separate_gate
```

The design should capture:

- what is known;
- what is unknown;
- what is only a candidate;
- which evidence supports each change;
- which real-use traces should be collected;
- when frontier-model post-hoc review should occur.

## 7. Meta-Agent application

Meta-Agent's existing repository-backed package already forms a preliminary external memory system. After migration, Mnemosyne can refine it through target PRs.

Likely next improvements include:

1. Meta-Agent-owned behavior guidance and loader;
2. exact memory-role and artifact-role registry;
3. capability-claim and validation ledger;
4. case/feedback intake with no automatic generalization;
5. research and source-revision registry;
6. deterministic current-state and handoff checks;
7. target-repository migration/tombstone records;
8. later retrieval/index design only after measured need.

These are candidates, not automatic target changes.

## 8. Change workflow after migration

```text
new need or observed failure
  -> target evidence/raw record
  -> Mnemosyne design/research if needed
  -> candidate target change + exact delivery manifest
  -> target-route review
  -> target repository PR
  -> human merge or rejection
  -> target active context/handoff update
  -> later drift and outcome review
```

If the design changes authority, privacy, target truth, or operational activation, frontier reasoning and explicit Owner decision are required.

## 9. Cross-repository references

Use immutable references:

```yaml
Mnemosyne_to_target_reference:
  repository:
  commit_or_tag:
  target_truth_path:
  delivery_manifest:

Target_to_Mnemosyne_reference:
  repository: 08822407d/Mnemosyne
  design_commit:
  design_or_validation_path:
```

Do not use ambiguous `latest` references in migration or target-truth records.

## 10. No-dual-writer rule

During shadow validation:

- source remains authoritative;
- destination is explicitly non-authoritative;
- only one side receives live target changes.

After cutover:

- destination becomes the only active target writer/truth location;
- the old Mnemosyne target root becomes historical/tombstoned;
- emergency rollback requires an Owner decision and exact ref;
- no bidirectional live sync is allowed.

## 11. Minimum validation before direct target PR delivery

```yaml
minimum_validation:
  - fresh_session_can_recover_target_from_destination_only
  - target_truth_and_authority_roles_are_correct
  - Meta_Agent_owned_behavior_guidance_passes_blocking_cases
  - target_repository_branch_and_PR_actions_are_observable
  - no_source_repository_mutation_occurs
  - path_allowlist_and_single_PR_lineage_pass
  - rollback_is_rehearsed
```

## 12. Boundaries

This operating model does not:

- authorize a target repository write;
- designate a permanent product surface;
- require every target to migrate;
- make Mnemosyne the target Owner;
- approve private data, runtime activation, RAG, MCP, or automation;
- allow a target repository to import Mnemosyne maintenance state as live guidance.
