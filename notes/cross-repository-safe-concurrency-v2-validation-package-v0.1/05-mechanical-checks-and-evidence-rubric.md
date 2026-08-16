# V2 Mechanical Checks and Evidence Rubric

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-MECHANICAL-RUBRIC-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-PACKAGE-001
status: frozen_design_not_executed
```

## 1. Purpose

Mechanical checks establish identities, declared/actual effects and bounded negative evidence. They do not replace semantic adjudication.

Each check result must be one of:

```text
PASS
FAIL
BLOCKED
NOT_SELECTED
NOT_APPLICABLE
DISPUTED_REQUIRES_ADJUDICATION
```

No missing check may be silently treated as PASS.

## 2. Common checks M0–M17

### M0 — package identity

Verify exact validation/package files and selected package version.

### M1 — material safety

Verify only approved public/synthetic fixture material is present. Any ambiguous material blocks.

### M2 — repository and base identities

Record exact repository, default branch, fixture base SHA and controller base SHA for every selected repository.

### M3 — selected stage/cell scope

Verify that only Owner-authorized stages/cells are activated.

### M4 — task/branch/PR lineage

For every task, verify one canonical branch and at most one canonical open PR. Record rejected duplicate attempts.

### M5 — declared effect completeness

Require explicit fields for:

- write set;
- read/version set;
- generated/derived effects;
- shared/global objects;
- semantic contracts;
- ordered dependencies;
- tool/connector scope.

Unknowns must be declared, not omitted.

### M6 — actual write-set comparison

Verify actual changed paths are a subset of the declared allowed write set.

### M7 — read/version freshness

Immediately before publication/merge, compare every `must_still_match` identity to the current observed identity.

### M8 — generated/derived collision

Compare selected tasks' declared generated/derived effects. Unknown or overlapping effects cannot be classified independent.

### M9 — semantic contract check

Run or inspect the frozen deterministic semantic check and record its evidence level separately from M6.

### M10 — merge/interleaving order

Where order independence is claimed, construct all selected relevant orders from the same base and compare semantic results.

### M11 — shared/global/unknown disposition

Verify shared/global work serialized or followed an explicit reconciliation contract; unknown scope blocked.

### M12 — ordered predecessor identity

For each cross-repository step, verify its predecessor committed identity was re-read before the step began.

### M13 — recovery authorization and identity

Verify recovery has a distinct task/action, current base, exact scope and authorization. Record prohibited reset/force-push use.

### M14 — authority/cutover/backup

Verify current authority, old/new writer boundary, stale-writer outcome and backup non-authority at the evidence layer actually tested.

### M15 — protected-repository no-write

For every named protected repository, compare before and after refs over the selected time window. The claim is limited to those repositories, refs and accessible action surfaces.

### M16 — result completeness

Verify raw cell results, incidents, unresolved gaps, evidence levels and stage disposition are present.

### M17 — no hidden continuation

Verify no unselected cell, retry, package repair, architecture modification, result writeback or next-stage start occurred.

## 3. V2-A-specific checks A-M0–A-M8

```yaml
A_M0_positive_pair_effects_disjoint:
A_M1_both_merge_orders_built:
A_M2_both_merge_orders_semantically_equal:
A_M3_generated_collision_detected:
A_M4_stale_read_detected:
A_M5_duplicate_lineage_rejected:
A_M6_shared_global_unknown_fail_closed:
A_M7_path_clean_semantic_failure_preserved:
A_M8_no_unnecessary_global_serialization_in_positive_case:
```

## 4. V2-B-specific checks B-M0–B-M9

```yaml
B_M0_three_repository_topology_verified:
B_M1_ordered_success_predecessor_revalidated:
B_M2_partial_state_preserved_after_later_failure:
B_M3_false_atomic_completion_absent:
B_M4_recovery_separately_authorized:
B_M5_recovery_current_base_verified:
B_M6_failed_recovery_human_gate_present:
B_M7_stale_writer_evidence_layered:
B_M8_backup_remained_non_authoritative:
B_M9_destructive_default_rollback_absent:
```

## 5. V2-C-specific check placeholders

Not executable from this package:

```yaml
C_M0_connector_app_account_identity:
C_M1_repository_action_allowlist:
C_M2_unlisted_read_denial_evidence:
C_M3_unlisted_write_denial_evidence:
C_M4_private_public_isolation:
C_M5_permission_rollback:
C_M6_denial_evidence_reviewability:
```

## 6. Evidence rubric

### Declared

A task or actor states a fact, but no artifact or independent check is available.

### Artifact present

A file, branch, PR, log or test artifact exists with an exact identity.

### Statically inspected

An identified artifact has been read or mechanically parsed without executing its behavior.

### Mechanically verified

A deterministic identity/path/schema/tree/ref comparison was performed and preserved.

### Runtime executed

A named program, check or action actually ran on the selected surface.

### Runtime passed

The executed action satisfied its frozen acceptance criteria.

### Independently reproduced

A separate qualified actor/surface recreated the result from preserved inputs.

### Platform-signed or independently attested

A trusted platform or independent evidence source produced a verifiable record outside the worker's own assertion.

## 7. Claim discipline

Examples:

```yaml
bad_claim: no_dual_writer_proven_globally
correct_claim: no_named_default_branch_ref_change_observed_for_repositories_X_Y_between_T0_T1_on_accessible_surface_Z

bad_claim: connector_permission_enforced
correct_claim: worker_self_attested_no_connector_use

bad_claim: semantic_non_interference_proven
correct_claim: selected_fixture_orders_produced_equal_frozen_semantic_check_outputs
```

## 8. Overall rubric

A stage may receive:

```text
STAGE_PASS_SELECTED_SCOPE
STAGE_PASS_WITH_BOUNDED_DEFECTS_FOR_ADJUDICATION
STAGE_FAIL
STAGE_BLOCKED
```

Only fresh Pro/frontier adjudication may decide whether a defect belongs to the executor, fixture/profile, product surface or candidate.
