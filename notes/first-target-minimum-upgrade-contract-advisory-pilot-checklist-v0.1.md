# First-Target Minimum Upgrade Contract — Advisory Pilot Checklist v0.1

> Non-execution-source first-target review instrument. It does not select a target project, authorize a target workspace or target write, modify `current/human-approved-spec.md`, or make `FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-001` a mandatory global rule.

```yaml
checklist_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-ADVISORY-PILOT-CHECKLIST-001
created_by_task: MNEMOSYNE-167
candidate_ref: notes/first-target-minimum-upgrade-contract-v0.1.md
candidate_disposition: ACCEPT_AS_ADVISORY_PILOT_ONLY
execution_source: current/human-approved-spec.md
execution_source_modified: false
activation: only_after_explicit_first_target_selection_and_approved_run_manifest
```

## 1. Purpose

Use this checklist during the first real target-project memory-system design to test whether a small, target-tailorable upgrade contract reduces lock-in without creating disproportionate process burden.

The checklist evaluates the candidate. It does not presume the candidate is correct, and it does not make failure of the advisory pilot an automatic failure of the target-project design.

```yaml
pilot_role:
  required_global_template_rule: false
  target_specific_review_input: true
  target_write_authorization: false
  automatic_migration_authorization: false
  promotion_to_global_rule_requires:
    - completed_target_specific_pilot
    - evidence_and_burden_review
    - explicit_user_disposition
    - fresh_bounded_repository_task
```

## 2. Activation gate

Do not instantiate this checklist until all of the following are true:

```yaml
activation_gate:
  target_project_selected: true
  target_owner_or_user_identified: true
  target_runtime_truth_source: identified_or_explicitly_unknown
  repository_and_storage_safety_boundary: reviewed
  target_lifespan_and_change_expectation: recorded
  approved_first_target_run_manifest: present
  design_only_or_target_write_scope: explicit
```

If the target is temporary, low-risk or intentionally disposable, the reviewer may select a simplified profile or `not_applicable_with_rationale`; the checklist must not force long-lived infrastructure onto a short-lived Agent.

## 3. Pilot profile selection

```yaml
upgrade_pilot_profile:
  selected: minimal | standard | enhanced | not_applicable_with_rationale
  target_lifespan:
  authority_or_privacy_risk:
  expected_change_types:
  expected_model_or_tool_changes:
  migration_downtime_tolerance:
  audit_or_rollback_need:
  rationale:
```

Profile guidance:

- `minimal`: temporary or small Agent; files/Git as appropriate; compact versioning and rollback references.
- `standard`: long-lived target with plausible schema, model, tool or storage evolution.
- `enhanced`: multiple writers, high audit need, significant privacy/authority risk or planned storage/runtime migration.
- `not_applicable_with_rationale`: deliberately disposable system or another target-specific reason accepted by the owner.

The profile names are review conveniences, not universal architecture classes.

## 4. Review-row schema

Use this row for every check:

```yaml
check_id:
result: pass | fail | unknown | not_tested | not_applicable
profile:
expected:
actual:
evidence_refs: []
burden_observed:
simplification_or_exception:
owner_decision_ref:
blocking_for_pilot_verdict: yes | no
blocking_for_target_design: no_by_default | yes_by_explicit_run_manifest
result_rationale:
```

Rules:

- `blocking_for_target_design` is `no_by_default`; this is an advisory pilot.
- A run manifest may make a row blocking for that target only, with explicit owner approval and rationale.
- `unknown` and `not_tested` prevent a full pilot PASS when `blocking_for_pilot_verdict: yes`, but do not silently block the target project.
- A simplification or exception must preserve authority, source and rollback clarity appropriate to the target.

## 5. Core advisory checks

### UPGRADE-PILOT-01 — Stable identity is proportionate

```yaml
check_id: UPGRADE-PILOT-01-stable-identity
expected: Authority-bearing requirements, decisions and canonical memory objects have stable IDs or an explicitly justified simpler identity rule; IDs are not silently reused after retirement.
blocking_for_pilot_verdict: yes
```

### UPGRADE-PILOT-02 — Source and authority are preserved

```yaml
check_id: UPGRADE-PILOT-02-source-authority
expected: Raw/source evidence, approved requirements and decisions, target execution source, current state and derived views have distinct roles and conflict precedence.
blocking_for_pilot_verdict: yes
```

### UPGRADE-PILOT-03 — Version set is sufficient but compact

```yaml
check_id: UPGRADE-PILOT-03-version-set
expected: Design, schema, policy and delivery versions are recorded where relevant; model/tool/transformation identity is recorded only to the level supportable by evidence.
blocking_for_pilot_verdict: yes
```

### UPGRADE-PILOT-04 — One realistic change can be mapped

```yaml
check_id: UPGRADE-PILOT-04-change-mapping
expected: The design can express at least one realistic future change with an old-to-new object or field mapping and a compatibility statement.
blocking_for_pilot_verdict: yes
```

The change may be synthetic during a design-only pilot. It must not modify the target runtime without separate authorization.

### UPGRADE-PILOT-05 — Preserve, transform, recompute and retire are distinguished

```yaml
check_id: UPGRADE-PILOT-05-artifact-treatment
expected: The pilot distinguishes what must be preserved, what may be transformed, what should be recomputed and what may be retired; raw and confirmed authority are not silently regenerated from summaries.
blocking_for_pilot_verdict: yes
```

### UPGRADE-PILOT-06 — Validation checks meaning, not only bytes

```yaml
check_id: UPGRADE-PILOT-06-validation
expected: Acceptance criteria cover identity, authority, scope, unresolved conflicts and behavior/retrieval where relevant; a successful file conversion alone is insufficient.
blocking_for_pilot_verdict: yes
```

### UPGRADE-PILOT-07 — Previous state and rollback are explicit

```yaml
check_id: UPGRADE-PILOT-07-rollback
expected: A previous-state reference, rollback trigger, restoration method, non-reversible writes and authoritative state during rollback are stated proportionately.
blocking_for_pilot_verdict: yes
```

For a design-only pilot, a dry-run rollback description or reconstruction demonstration is sufficient unless the run manifest requires more.

### UPGRADE-PILOT-08 — Derived views are rebuildable where practical

```yaml
check_id: UPGRADE-PILOT-08-derived-views
expected: Summaries, indexes, embeddings or model-generated projections identify their source and transformation context and can be rebuilt where practical; exceptions are recorded.
blocking_for_pilot_verdict: no
```

### UPGRADE-PILOT-09 — Mnemosyne does not become a second runtime truth source

```yaml
check_id: UPGRADE-PILOT-09-truth-source-separation
expected: Mnemosyne remains the design archive/control plane; the target project has one explicit runtime truth source or an explicit unresolved owner decision.
blocking_for_pilot_verdict: yes
```

### UPGRADE-PILOT-10 — Next-tier executor usability is tested

```yaml
check_id: UPGRADE-PILOT-10-next-tier-executor
expected: Bounded implementation or maintenance instructions can be followed by the intended non-frontier execution model, or the task identifies a clear escalation point for frontier reasoning.
blocking_for_pilot_verdict: yes
```

This check evaluates instruction and task design, not hidden backend identity. Consumer UI labels, speed and model self-report do not attest the served backend.

### UPGRADE-PILOT-11 — Complexity remains proportionate

```yaml
check_id: UPGRADE-PILOT-11-proportionality
expected: The candidate adds less expected burden than the lock-in, migration and recovery risk it addresses; unnecessary event sourcing, dual-write, shadow cutover, bitemporal storage or services are omitted.
blocking_for_pilot_verdict: yes
```

## 6. Optional enhanced checks

Apply only when target-specific risk justifies them:

```yaml
optional_enhanced_checks:
  - multi_writer_conflict_and_idempotency
  - dual_write_reconciliation
  - shadow_read_or_shadow_execution
  - valid_time_and_transaction_time
  - storage_export_and_recovery
  - privacy_consent_and_revocation_during_migration
  - heterogeneous_review_for_authority_or_trust_boundary_change
```

Mark omitted enhanced checks `not_applicable` with rationale; they are not part of the small-project default.

## 7. Pilot burden and value record

```yaml
pilot_burden_and_value:
  additional_files_or_fields:
  human_review_time:
  next_tier_model_rework:
  frontier_escalations:
  confusion_or_duplicate_truth_created:
  upgrade_or_rollback_risk_reduced:
  useful_fields:
  unnecessary_fields:
  target_specific_changes_needed:
  recommendation:
```

No exact time or cost estimate should be invented when it was not measured.

## 8. Pilot verdict

```yaml
pilot_verdict:
  result: PASS_FOR_TARGET_SPECIFIC_USE | PASS_WITH_SIMPLIFICATION | REVISE_CONTRACT | DEFER_UNTIL_REAL_MIGRATION_EVIDENCE | REJECT_AS_TOO_BURDENSOME
  passed_checks: []
  failed_or_unknown_checks: []
  simplifications: []
  residual_risks: []
  owner_or_user_disposition_ref:
  global_promotion_recommended: no_by_default
  follow_up_candidate_or_task:
```

Meanings:

- `PASS_FOR_TARGET_SPECIFIC_USE`: useful and proportionate for this target only.
- `PASS_WITH_SIMPLIFICATION`: useful after reducing fields or gates for this target.
- `REVISE_CONTRACT`: structural defects require candidate revision before broader use.
- `DEFER_UNTIL_REAL_MIGRATION_EVIDENCE`: design-only evidence is insufficient.
- `REJECT_AS_TOO_BURDENSOME`: expected process cost exceeds demonstrated benefit for this target.

No verdict automatically updates the target execution source, Mnemosyne execution source or global templates.

## 9. Boundaries

- This checklist is not an execution source.
- It does not create or modify a target workspace, target material, target repository or runtime.
- It does not authorize migration, automatic writeback, cross-Agent sharing or learner profiling.
- It does not require event sourcing, dual-write, shadow cutover, bitemporal storage, databases or services.
- It does not select Meta-Agent or another target.
- It does not close the migration research question or promote the candidate globally.
- Any target-specific use requires the target owner's explicit run manifest and final disposition.
