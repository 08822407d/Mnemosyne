# V1 Mechanical Closeout and Return Contract

```yaml
execution_package_id: MNE-TARGET-LIFECYCLE-V1-EXECUTION-PACKAGE-001
cell_id: TLR-V1-CELL-CLOSEOUT-001
status: prepared_not_executed
semantic_final_adjudicator: fresh_Pro_conversation
```

## 1. Role

The closeout controller aggregates exact evidence after all selected V1 cells have stopped. It performs deterministic checks and produces the complete V1 bundle.

It must not:

- repair a failed scenario by changing its frozen input;
- hide failed attempts or incidents;
- decide that candidate v0.2 is globally accepted;
- authorize V2, S10, Mnemosyne ingestion or target adoption;
- replace the required fresh Pro semantic adjudication.

## 2. Preconditions

Closeout begins only when:

- an exact Owner V1 authorization exists;
- the controller and fixture receipts are complete;
- every selected cell has returned a result or a preserved blocked/failure state;
- no selected cell is still writing;
- all exact branch heads and result refs are available;
- the controller can re-read named real-repository refs.

Selected baseline cells:

```yaml
required_cells:
  - TLR-V1-CELL-CORE-001
  - TLR-V1-CELL-S7-001
  - TLR-V1-CELL-S8-001
  - TLR-V1-CELL-S11-001
```

## 3. Evidence inventory

Enumerate and pin:

- synthetic repository and visibility;
- V0 final head and V1 pinned base;
- controller branch/head;
- fixture branch/commit/tree;
- every task branch and head;
- every scenario input file and blob;
- every output file and blob;
- creation/update commit for every output blob;
- every failure, retry and incident ref;
- any scenario branch absent or unexpectedly duplicated;
- S8 conversation/input isolation receipt;
- source/snapshot/restore identities for S11.

Required normalized table:

| scenario/task | branch | base commit | head commit | result path | result blob | output commit | attempt/retry |
|---|---|---|---|---|---|---|---|

A missing exact identity blocks a clean pass disposition.

## 4. Declared-versus-actual write-set aggregation

For every task produce:

| task_id | declared roots/objects | actual changed paths | unexpected paths | authority/global/shared effect | verdict |
|---|---|---|---|---|---|

Compare each task branch against its recorded base rather than against an unrelated repository head.

Additional required checks:

- S3 Alpha/Beta path intersection;
- shared/global/dependency relation beyond path intersection;
- S4 serialization/reconciliation evidence;
- no target branch writes another target root;
- no scenario writes V0 evidence paths;
- no scenario result appears only as an uncommitted narrative.

## 5. Mechanical rubric M0–M11

Run the frozen package checks with exact applicability.

### M0 — Package identity

Verify candidate, validation, frozen package, V0 adjudication, V1 decision, V1 authorization and execution package exact identities.

### M1 — Repository and material identity

Verify public visibility, V1 pinned base, fixture commit/tree and public/synthetic-only inventory. Scan the V1 file inventory for credentials or real/private material indicators; record scope and limitation.

### M2 — Canonical task lineage

Verify each selected task has one canonical branch, no duplicate PR and no unapproved parallel variant. S3 has two distinct task IDs by design; it is not two branches for one task.

### M3 — Declared versus actual write set

Use the table in §4. Any unexpected shared/global/other-target path is a blocker until explicitly reconciled.

### M4 — Concurrency intersection

For S3 and S4, record exact intersections, shared/global relationships, dependencies and merge-order relationships. Empty path intersection alone is not sufficient.

### M5 — Authority preservation

Verify synthetic authority owners before/after each task; no task writer becomes standing authority; S11 restore preserves Alpha authority.

### M6 — Parent/meta content boundary

Verify S1 creates only a minimal blocking receipt and no operative/reconstructable Gamma content outside a target destination. Verify no parent/meta repository is used as backup.

### M7 — Documentation and migration

Verify S7 human/Agent docs/navigation/tests and required facts; verify S8's input lacks sufficient facts and Alpha remains unchanged.

### M8 — Source/requirement/API preservation

Verify exact source or immutable refs for S6, S7 and S9; material API changes explicit where authorized; no unapproved fine taxonomy invented.

### M9 — Backup and restore

Verify S11 exact source, both snapshots, simulated failure, surviving restore, authority and restored identity.

### M10 — Real-repository no-write proof

Re-read exact default-branch refs for:

- `08822407d/Mnemosyne`;
- `08822407d/Meta-Agent`.

Compare with controller before refs. Record the unnamed-target limitation exactly; do not claim per-repository proof for repositories not named and observed.

### M11 — Output and retry identity

Every attempt has exact input/output/branch/commit/blob identity, and no prior attempt was overwritten.

## 6. S8 contamination audit

The closeout must explicitly verify:

- S8 branch ancestry excludes S7 commits;
- sufficient S7 guide absent from S8 branch;
- S8 worker input inventory matches the isolation receipt;
- the worker conversation was reported fresh;
- no concrete hidden migration facts appear in the authorized S8 packet;
- S8 did not read forbidden branches/files through connector calls, to the extent preserved action evidence permits;
- Alpha content is unchanged on S8 branch except permitted evidence files.

If contamination is established or cannot be reasonably ruled out, classify S8 as invalid and do not treat a blocking response as successful evidence. Preserve the contaminated attempt and propose a clean rerun for Pro review.

## 7. Scenario summary

For each selected scenario record only a provisional execution disposition:

- `SCENARIO_PASS`
- `SCENARIO_PASS_WITH_NONCRITICAL_OBSERVATION`
- `SCENARIO_FAIL_CANDIDATE_OR_SEMANTIC`
- `SCENARIO_FAIL_EXECUTOR`
- `SCENARIO_BLOCKED_MISSING_AUTHORITY_OR_FACT`
- `SCENARIO_INVALID_PROTOCOL_OR_IDENTITY`

The mechanical controller may flag objective inconsistencies, but ambiguous candidate-versus-executor classification remains:

```text
DISPUTED_REQUIRES_PRO_FRONTIER_ADJUDICATION
```

## 8. Final no-write proof

Required table:

| repository | before ref | after ref | changed? | proof method | limitation |
|---|---|---|---|---|---|

If either named real repository changed during the V1 window, determine whether the change came from this V1 route. Do not automatically accuse or ignore unrelated concurrent work. A changed ref prevents the simple high-confidence no-write proof and requires Pro/Owner adjudication or a stronger task-action audit.

A narrative “the worker did not intend to write there” is insufficient.

## 9. Complete V1 bundle

Write the final controller bundle under:

```text
runs/MNE-TARGET-LIFECYCLE-V1-001/06-v1-result-bundle.yaml
```

It must contain:

```yaml
validation_result_bundle:
  result_id: MNE-TARGET-LIFECYCLE-V1-RESULT-001
  run_manifest_ref:
  V0_adjudication_ref:
  V1_authorization_ref:
  fixture_ref:
  controller_ref:
  selected_scenarios: []
  scenario_attempt_refs: []
  task_contract_refs: []
  branch_and_output_identity_refs: []
  declared_actual_write_set_ref:
  S8_isolation_and_contamination_ref:
  no_write_proof_ref:
  backup_restore_ref:
  incident_refs: []
  scenario_summary: {}
  critical_blockers: []
  candidate_defects: []
  validation_protocol_defects: []
  executor_defects: []
  disputed_items: []
  noncritical_observations: []
  proposed_amendments:
    - proposal:
      evidence_refs: []
      adoption_status: not_adopted_pending_fresh_Pro_and_Owner_review
  mechanical_controller_disposition:
  Pro_frontier_disposition:
    status: pending
    value: null
  Owner_architecture_decision:
    status: pending
    value: null
  S10_executed: false
  V2_authorized: false
  target_adoption_authorized: false
  execution_source_modified: false
  real_target_modified: false
```

## 10. Visible final response

The controller's visible final response must include the complete decision-relevant result, not only a repository pointer:

1. run/package/repository identities;
2. selected and unselected scenarios;
3. each scenario disposition and critical evidence;
4. every critical failure, incident and retry;
5. S8 isolation status;
6. exact no-write proof status;
7. S11 restore result;
8. candidate versus executor/protocol defects and disputes;
9. limitations;
10. required fresh Pro return route.

A repository file is the canonical supporting evidence, but it does not replace the visible summary needed for transfer.

## 11. Fresh Pro return package

The closeout response supplies:

- exact `Mnemosyne@master` used;
- exact synthetic repository and V1 controller/fixture/task branch refs;
- exact complete-bundle path/blob;
- no-write proof ref;
- all cell result refs;
- the frozen criteria version;
- a statement that the adjudicator must use a new Pro conversation that did not execute any cell.

The fresh Pro adjudicator reads only the exact required evidence set first. It may request specific additional branch files when a dispute requires them; it must not broad-read unrelated repositories.

## 12. Closeout dispositions

The mechanical controller chooses one routing result:

- `V1_BUNDLE_COMPLETE_READY_FOR_FRESH_PRO`
- `V1_BUNDLE_COMPLETE_WITH_BLOCKERS_READY_FOR_FRESH_PRO`
- `V1_INCOMPLETE_MISSING_CELL_OR_IDENTITY`
- `V1_INVALID_S8_CONTAMINATION`
- `V1_BLOCKED_NO_WRITE_PROOF`
- `V1_PROTOCOL_CONFLICT_RETURN_TO_PRO`

None is global architecture acceptance.

## 13. Stop boundary

After writing and returning the complete bundle, stop. Do not run S10, V2, reruns, candidate amendments, raw-result ingestion into Mnemosyne, architecture acceptance, target adoption or cleanup without the relevant later decisions.