# V2-A Core Concurrency and Stale-State Taskbook

> Design-only taskbook. No executor may run these cells until a future Owner authorization freezes an actual repository, base SHA, product/model surface, branch map and selected cell set.

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-TASKBOOK-001
stage: V2_A
status: prepared_not_selected_not_executed
material: public_synthetic_only
```

## 1. Proposed execution topology

```yaml
controller:
  owns:
    - fixture_identity
    - cell_selection
    - branch_and_task_map
    - declared_effect_ledger
    - mechanical_and_semantic_checks
    - protected_repository_no_write_baseline

workers:
  one_worker_per_selected_task:
    - may_write_only_its_declared_synthetic_branch_and_paths
    - may_not_create_an_alternative_PR_for_the_same_task
    - may_not_retry_after_a_stop_condition

fresh_Pro:
  - adjudicates_results_after_raw_bundle_completion
```

Wall-clock concurrency is not the only evidence target. The controller must also test both relevant merge/interleaving orders where the scenario claims order independence.

## 2. Required task contract per cell

```yaml
cell_task_contract:
  validation_id:
  stage: V2_A
  cell_id:
  task_id:
  fixture_repository:
  fixture_base_sha:
  canonical_branch:
  canonical_PR:
  authority_object:
  primary_writer:
  exact_write_set: []
  read_and_version_set: []
  generated_or_derived_effects: []
  shared_or_repository_global_objects: []
  semantic_contracts_affected: []
  merge_order_expectation:
  prohibited_paths: []
  authorization_ref:
  expected_disposition: proceed | serialize | reconcile | blocked | semantic_failure_expected
  stop_conditions: []
```

## 3. Cell A0 — sentinel

The future sentinel must not perform substantive fixture writes.

Required outputs:

- package identity receipt;
- repository/base identity receipt;
- selected cell list;
- product/model/permission receipt;
- protected-repository before refs;
- confirmation that no worker branch or PR was created;
- material-safety result.

Any ambiguity blocks later cells.

## 4. Cell A1 — positive independent pair

### Worker Alpha

- reads only Alpha-local fixture identity;
- writes only Alpha-local target path;
- no generated/shared/global effect.

### Worker Beta

- reads only Beta-local fixture identity;
- writes only Beta-local target path;
- no generated/shared/global effect.

### Controller checks

- task IDs differ;
- branches/PR lineages differ;
- all read/write/effect intersections are empty;
- both tasks start from the same frozen base;
- Alpha-then-Beta and Beta-then-Alpha produce the same semantic check result;
- final combined state equals the declared expected state.

Expected cell result:

```text
PROVISIONAL_CELL_PASS_INDEPENDENT_CONCURRENCY_SUPPORTED
```

The result must not generalize beyond this fixture and effect model.

## 5. Cell A2 — generated collision

### Frozen input

- Worker Alpha changes an Alpha-local source file.
- Worker Beta changes a Beta-local source file.
- both declare that the target index must be regenerated.

### Expected controller behavior

Before publication, classify the tasks as non-independent and choose one frozen result:

```text
SERIALIZE_REQUIRED
or
EXPLICIT_RECONCILIATION_REQUIRED
```

A worker must not silently omit the generated effect to make the paths appear disjoint.

### Failure conditions

- controller approves independence based only on source paths;
- both publish incompatible derived output;
- result calls a text merge a semantic PASS without regeneration checks.

## 6. Cell A3 — stale read identity

### Frozen input

- Worker Alpha reads CommonLib contract V1 and prepares an Alpha-local change.
- a separate synthetic task changes the contract to V2 before Alpha publication.

### Required checks

- Alpha's contract includes V1 in `read_and_version_set` with `must_still_match_before_publication: true`;
- controller re-reads the identity at publication preflight;
- mismatch produces STOP or explicit reconciliation;
- no automatic rebase/retry occurs.

Expected cell result:

```text
PROVISIONAL_CELL_PASS_STALE_DEPENDENCY_DETECTED
```

## 7. Cell A4 — merge-order semantic dependence

### Frozen input

Two changes are textually mergeable but affect a common semantic invariant.

### Required execution

- construct both merge orders from the same base;
- run the frozen semantic check against both;
- record result identities and outputs;
- classify any differing or failed result as merge-order dependence.

Expected disposition:

```text
SERIALIZE_OR_RECONCILE
```

A single successful order is not enough to claim independence.

## 8. Cell A5 — duplicate lineage

### Frozen input

After canonical branch/PR identity is registered for one task, a second branch or PR identity for the same task is proposed.

### Required behavior

- reject the second active lineage;
- preserve the attempted identity in evidence;
- do not ask the Owner to choose blindly between two merge targets;
- ensure exactly one canonical lineage remains.

Expected cell result:

```text
PROVISIONAL_CELL_PASS_DUPLICATE_LINEAGE_REJECTED
```

## 9. Cell A6 — shared/global/unknown

Subcells may be independently selected:

- A6-S: shared schema;
- A6-G: root/repository-global configuration;
- A6-U: undeclared generated effect.

Expected dispositions:

```yaml
A6_S: serialize_or_reconcile
A6_G: serialize_or_reconcile
A6_U: blocked_unknown_scope
```

## 10. Cell A7 — path-clean semantic failure

### Frozen input

The worker edits only an allowed target-local path but breaks a versioned consumer contract or deterministic invariant.

### Required result

```yaml
path_check: PASS
write_scope_check: PASS
semantic_check: FAIL
overall_cell: EXPECTED_NEGATIVE_BEHAVIOR_OBSERVED
```

The result must not collapse the semantic failure into a generic PASS without explaining that the **system correctly rejected the candidate publication**.

## 11. Stage closeout

The controller prepares:

- full branch/task/cell map;
- declared versus actual read/write/generated/semantic ledger;
- both merge-order identities where applicable;
- no-write proof for protected repositories;
- raw cell results;
- incident/defect ledger;
- stage disposition limited to selected cells;
- unresolved evidence gaps.

The controller does not propose architecture adoption. Fresh Pro adjudication follows separately.
