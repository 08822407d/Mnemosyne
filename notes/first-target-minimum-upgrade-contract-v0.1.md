# First-Target Minimum Upgrade Contract v0.1 — Candidate

> Non-execution-source candidate design. This file does not modify `current/human-approved-spec.md`, select a target project, authorize a target workspace or target write, or become a target project's runtime contract without a later explicit user and target-owner decision.

```yaml
candidate_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-001
created_by_task: MNEMOSYNE-166
status: candidate_ready_for_user_review
source_decision_route: FIRST_TARGET_MINIMUM_UPGRADE_CONTRACT
execution_source: current/human-approved-spec.md
execution_source_modified: false
target_project_selected: false
implementation_authorized: false
```

## 1. Purpose

Mnemosyne should be usable before it is perfect, but its first real target-project memory system should not be locked to:

- the current Mnemosyne template version;
- the model that designed it;
- one storage layout or retrieval implementation;
- one set of derived summaries, indexes or embeddings;
- an undocumented authority hierarchy;
- an irreversible delivery state.

This candidate defines the smallest upgrade, migration, validation and rollback contract that should be considered during first-target intake, design, delivery and later drift review.

It is deliberately smaller than a universal event-sourcing architecture. Small or temporary Agents should not be forced to adopt dual-write, shadow cutover, bitemporal storage or a runtime event store merely because those mechanisms can help in larger migrations.

## 2. Evidence and existing-design basis

```yaml
repository_basis:
  execution_source:
    - current/human-approved-spec.md#8-模型迁移原则
    - current/human-approved-spec.md#9-交付包原则
    - current/human-approved-spec.md#16-目标项目工作区原则
  existing_template_fields:
    - notes/target-project-memory-system-template-pack.md::migration_requirement
    - notes/target-project-memory-system-template-pack.md::design_version
    - notes/target-project-memory-system-template-pack.md::model_migration_policy
    - notes/target-project-memory-system-template-pack.md::drift_review_policy
    - notes/target-project-memory-system-template-pack.md::versioning_rule
    - notes/target-project-memory-system-template-pack.md::rollback_or_revision_plan
  research_evidence:
    - notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/01-maintainer-reliability-review.md
    - notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/02-unified-evidence-ledger.md#E-10
    - notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/02-unified-evidence-ledger.md#E-11
    - notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/02-unified-evidence-ledger.md#E-12
  evidence_role: candidate_design_input_not_execution_source
```

## 3. Candidate minimum contract

Every first real target-project design should explicitly answer the following. A field can be `not_applicable`, but it must not disappear silently when its purpose is relevant.

```yaml
minimum_upgrade_contract:
  contract_id:
  target_project_ref:
  contract_status: draft | needs_user_review | confirmed_for_target | superseded
  contract_version:

  stable_identity:
    object_id_rule:
    ID_reuse_prohibited: true
    rename_split_merge_retire_mapping_required: true

  authority_and_source:
    target_execution_source_ref:
    raw_evidence_role:
    approved_requirement_and_decision_role:
    current_state_role:
    derived_artifact_role:
    conflict_precedence:

  version_set:
    design_version:
    schema_version:
    policy_version:
    delivery_version:
    transformation_or_model_version_rule:

  migration:
    migration_manifest_required: true
    old_to_new_mapping_required: true
    preserve_recompute_retire_decisions_required: true
    compatibility_statement_required: true

  validation:
    acceptance_criteria_ref:
    identity_and_authority_checks_required: true
    behavior_or_retrieval_regression_check_required_when_relevant: true
    unresolved_conflict_policy:

  rollback:
    previous_state_ref_required: true
    rollback_plan_ref_required: true
    rollback_limitations_required: true

  derived_views:
    rebuildable_where_practical: true
    non_rebuildable_exception_record_required: true

  review:
    owner_or_user_decision_required: true
    high_impact_escalation_rule:
    drift_review_trigger:
```

## 4. Stable identity and object lineage

### 4.1 Objects that normally need stable IDs

At minimum, stable identity should be considered for:

- approved requirements and constraints;
- user or owner decisions;
- canonical memory objects;
- authority/source records;
- unresolved questions whose continuity matters;
- handoff/checkpoint objects;
- migration manifests;
- consent, permission or privacy decisions when the project uses them;
- evaluation cases and acceptance criteria.

Raw bytes can retain content hashes and source refs rather than a complex semantic ID when that is sufficient. Ephemeral scratch state does not require durable identity unless it becomes evidence or current truth.

### 4.2 ID rules

```yaml
candidate_ID_rules:
  stable_after_creation: true
  semantic_meaning_not_encoded_too_rigidly: true
  ID_reuse_after_retirement: prohibited
  content_change_does_not_silently_create_a_new_identity: true
  split_merge_or_replacement_requires_mapping: true
  source_refs_preserved: true
```

### 4.3 Mapping relations

```text
unchanged
renamed
moved
reformatted
superseded
split_into
merged_from
replaced_by
retired
recomputed_from
unmappable_requires_human_review
```

A mapping records lineage; it does not automatically assert semantic equivalence.

## 5. Authority and source preservation

Migration must not collapse these roles:

```text
raw/source evidence
approved requirements and decisions
target-project execution source
current operational state
handoff/navigation
research evidence
model-generated or derived projections
```

Candidate invariants:

1. Raw evidence does not automatically override approved current truth.
2. A derived summary, embedding, index, profile or model inference does not become authoritative merely because it is newer.
3. Authority changes require an explicit decision record and cannot be hidden inside a schema or storage migration.
4. Mnemosyne remains design factory and design archive; the target project's confirmed execution source remains its runtime truth source.
5. A stronger future model may recompute candidates and derived views, but cannot silently rewrite confirmed requirements or decisions.

## 6. Version set

The contract uses several small version dimensions rather than one ambiguous global version.

| Version | What it identifies | Change examples |
|---|---|---|
| `design_version` | target memory-system design | new object roles, workflow or authority architecture |
| `schema_version` | structural representation | added/removed fields, changed object relations |
| `policy_version` | update, sharing, privacy, review or authority rules | new approval or conflict rules |
| `delivery_version` | concrete package delivered to the target | changed files or setup instructions |
| transformation/model context | how derived views were produced | summarizer prompt/model, embedding model, indexer version |

The target may combine versions when the system is very small, provided the mapping remains unambiguous.

## 7. Migration manifest candidate

```yaml
migration_manifest:
  migration_id:
  target_project_ref:
  status: proposed | approved | in_progress | validated | rolled_back | abandoned
  created_at:
  owner:

  from_state:
    design_version:
    schema_version:
    policy_version:
    delivery_version:
    baseline_ref:

  to_state:
    design_version:
    schema_version:
    policy_version:
    delivery_version:

  trigger_and_objective:
  scope_included: []
  scope_excluded: []

  object_mappings:
    - old_id:
      new_id_or_ids: []
      relation: unchanged | renamed | moved | split_into | merged_from | replaced_by | retired | recomputed_from | unmappable_requires_human_review
      authority_changed: false
      source_refs_preserved: true
      rationale:

  artifact_decisions:
    preserve: []
    transform: []
    recompute: []
    retire: []
    unresolved: []

  compatibility:
    readers_supported:
    writers_supported:
    known_breaks: []
    transition_mode: offline_copy_transform | in_place | read_old_write_new | dual_read | dual_write | shadow | rebuild_from_raw | other

  validation_plan_ref:
  acceptance_criteria_ref:
  rollback_plan_ref:
  residual_risks: []
  human_decision_ref:
```

## 8. Preserve, transform, recompute or retire

| Artifact class | Default candidate treatment | Reason |
|---|---|---|
| raw/source evidence | preserve | historical evidence and reinterpretation baseline |
| confirmed requirements/decisions | preserve; explicitly supersede only by decision | authority-bearing truth |
| target execution source | controlled migration with owner review | runtime authority |
| current state | transform with freshness checks | may contain stale or transient facts |
| summaries and indexes | recompute where practical | derived and model/tool dependent |
| embeddings | normally recompute after embedding-model or chunking change | vector values are implementation-specific |
| handoff/checkpoint | preserve relevant history; regenerate current handoff | navigation must reflect current state |
| rejected/retired candidates | preserve minimally with status | prevents accidental resurrection |
| ephemeral scratch | retire unless explicitly promoted | avoid unnecessary migration burden |

These are defaults, not universal mandates.

## 9. Change classes and gates

### Class 0 — Presentation-only

Examples: formatting, links, explanatory prose with no authority or meaning change.

Minimum gate: diff review and identity preservation.

### Class 1 — Additive compatible change

Examples: optional field, new derived index, additional non-authoritative view.

Minimum gate: schema version, backward-read check and rollback/ref removal plan.

### Class 2 — Semantic or breaking schema change

Examples: splitting a memory object, changing field meaning, changing conflict behavior.

Minimum gate: migration manifest, object mappings, semantic-diff review, regression tests and owner approval.

### Class 3 — Authority, privacy or trust-boundary change

Examples: changing execution source, sharing scope, write authority, consent, retention or target/Mnemosyne ownership.

Minimum gate: high-impact review, explicit human decision, mechanical evidence where applicable, target-specific rollback and heterogeneous review when required by approved Mnemosyne rules.

### Class 4 — Storage/runtime platform migration

Examples: file/Git to database, vector store or knowledge graph; local to hosted runtime.

Minimum gate: data and authority mapping, export/recovery path, staged validation and proof that the old and new systems do not both silently claim authority.

## 10. Validation candidate

```yaml
migration_validation:
  exact_or_counted_object_inventory:
  stable_ID_coverage:
  source_ref_preservation:
  authority_precedence_unchanged_or_explicitly_approved:
  raw_and_confirmed_records_preserved:
  object_mapping_complete:
  unresolved_conflicts: []
  derived_view_rebuild_check:
  retrieval_or_behavior_regression_results:
  stale_state_check:
  privacy_and_access_check:
  handoff_and_current_state_check:
  rollback_rehearsal_or_reason_not_run:
  residual_risks: []
  final_owner_disposition: accept | accept_with_limitations | revise | rollback | reject
```

A successful file conversion is not sufficient validation. The migration must preserve meaning, authority, scope and expected behavior.

## 11. Rollback candidate

```yaml
rollback_plan:
  rollback_id:
  migration_ref:
  previous_state_ref:
  trigger_conditions: []
  restoration_steps: []
  derived_artifacts_to_discard_or_rebuild: []
  writes_that_cannot_be_automatically_reversed: []
  data_loss_or_divergence_risk: []
  authority_during_rollback:
  verification_after_rollback: []
  owner_decision_ref:
```

Rollback must say which state is authoritative during the transition. “Keep a backup” is not a complete rollback plan.

## 12. Small-project minimum profile

A temporary or small Agent can satisfy this candidate without a service architecture.

```yaml
small_project_profile:
  storage: files_or_Git_as_appropriate
  required:
    - stable_IDs_for_authority_bearing_objects
    - source_refs
    - compact_version_fields
    - append_only_or_reviewed_history_for_raw_and_decisions
    - migration_log_with_old_to_new_mapping
    - explicit_acceptance_checks
    - previous_state_and_rollback_ref
  not_required_by_default:
    - full_event_sourced_runtime
    - dual_write
    - shadow_cutover
    - bitemporal_database
    - automated_migration_service
```

This profile is intended to preserve upgradeability without making a small Agent disproportionately expensive.

## 13. Conditional mechanisms

The following mechanisms require target-specific justification:

| Mechanism | Consider when | Avoid by default when |
|---|---|---|
| full event-sourced runtime | multiple writers, strong audit/replay, frequent projection rebuilds | small low-risk system, MVP, low migration complexity |
| dual-write | zero/low downtime and two stores must remain synchronized temporarily | no reliable reconciliation or write idempotency |
| shadow cutover | new system can be evaluated without taking authority | cost, privacy or duplicated processing is unacceptable |
| bitemporal storage | both valid-time and transaction-time queries are necessary | simple chronological history is sufficient |
| rebuild from raw | raw evidence is complete and transformations are reproducible | raw is incomplete, sensitive or too expensive to replay |

## 14. Integration map for a later approved template update

This candidate does not modify the template pack now. A later approved patch could map it as follows:

| Existing target-project instrument | Candidate addition |
|---|---|
| Intake `migration_requirement` | lifespan, expected upgrade types, downtime, audit and rollback needs |
| Memory System Design Spec | `upgrade_contract_ref`, schema/policy/delivery versions, derived-view rebuild policy |
| Execution Source Rule | versioning and authority-change procedure |
| Delivery Package | delivered-version set, previous-state ref and rollback plan |
| Handoff | current versions, active migration state and authoritative surface |
| Drift Review | schema/policy/tool/model drift and revalidation triggers |
| Completion Criteria | upgrade contract reviewed or explicitly marked not applicable with rationale |

## 15. First-target pilot acceptance rubric

Before this candidate is promoted beyond design evidence, the first real target-project design should test whether it can:

1. assign stable identity without excessive administrative burden;
2. preserve raw and approved authority boundaries;
3. express one realistic design/schema update through a migration manifest;
4. map changed objects without ambiguity;
5. rebuild at least one derived view or document why it cannot be rebuilt;
6. validate behavior or retrieval before acceptance;
7. restore or reconstruct the previous state;
8. keep Mnemosyne archive and target runtime truth distinct;
9. remain usable by the intended non-frontier execution model where the task is classified as suitable;
10. avoid unnecessary event-sourcing or service complexity.

Candidate result states:

```text
PASS_FOR_TARGET_SPECIFIC_USE
PASS_WITH_SIMPLIFICATION
REVISE_CONTRACT
DEFER_UNTIL_REAL_MIGRATION_EVIDENCE
REJECT_AS_TOO_BURDENSOME
```

## 16. User decisions still required

A later decision package should ask:

- whether this minimum contract should become a required part of the first target-project design process;
- whether it should remain advisory until a real pilot demonstrates value;
- which fields are mandatory for all targets versus only long-lived/high-risk targets;
- whether template-pack changes should occur before or during the first target project;
- what level of migration rehearsal is proportionate for a small Meta-Agent or temporary Agent.

## 17. Boundaries

- This candidate does not modify the execution source.
- It does not select Meta-Agent or another target project.
- It does not create a target workspace or ingest target materials.
- It does not approve an actual target execution source, schema, migration or write.
- It does not require event sourcing, dual-write, shadow cutover or a database.
- It does not authorize automatic migration or automatic writeback.
- It does not treat research reports as implementation authority.
- It does not close the migration, shared-memory, learner-state, adaptive-explanation, GPT Live or HO-GUIDANCE questions.
