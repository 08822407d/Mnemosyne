# V2 Synthetic Fixture and Scenario Contracts

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-FIXTURE-SCENARIOS-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-PACKAGE-001
status: frozen_design_not_created_not_executed
material_class: public_synthetic_only_except_V2_C_design_only
```

## 1. Common fixture principles

Any future fixture must:

- contain only synthetic names, code, documents and history;
- have no credentials, private source, real user data or target truth;
- preserve one controller/evidence boundary separate from worker task roots;
- pin every repository and branch base by exact commit SHA;
- declare canonical task, branch and PR identities before worker execution;
- include deterministic semantic checks rather than relying only on textual mergeability;
- identify every generated/derived object and semantic interface used by a task;
- allow complete cleanup without deleting the preserved result bundle.

## 2. Proposed V2-A fixture

Recommended logical tree in one temporary public/synthetic fixture repository:

```text
fixture/
  targets/alpha/
    authority.yaml
    config.yaml
    consumer.md
  targets/beta/
    authority.yaml
    config.yaml
    consumer.md
  libraries/common-lib/
    contract.yaml
    implementation.txt
  generated/
    target-index.json
    dependency-index.json
  shared/
    schema.yaml
  repository/
    root-config.yaml
    task-lineage-registry.yaml
  checks/
    semantic-checks.yaml
  evidence/
```

The exact physical paths may change only before a future run package is frozen.

### Required deterministic relations

- Alpha and Beta have independent target-local files.
- Both appear in `generated/target-index.json`.
- Alpha reads one versioned field from `libraries/common-lib/contract.yaml`.
- `shared/schema.yaml` is explicitly common.
- `repository/task-lineage-registry.yaml` can detect a duplicate task lineage.
- `checks/semantic-checks.yaml` defines observable invariants that can fail even when path checks pass.

## 3. V2-A scenario set

### A0 — package, identity and no-write sentinel

Purpose:

- prove the selected package, fixture base, controller branch and protected-repository baseline are known before substantive execution.

PASS candidate:

- exact package and repository identities recorded;
- no private or real-target material;
- protected repository refs recorded before run;
- no worker branch created during sentinel-only scope;
- no ambiguity about selected cells.

### A1 — genuine independent positive case

Task Alpha changes only Alpha target-local content. Task Beta changes only Beta target-local content.

Both must declare:

- disjoint write sets;
- disjoint read/write dependencies;
- no generated/shared/global effect;
- no merge-order dependency.

PASS candidate:

- workers may proceed independently;
- both merge-order simulations produce the same expected semantic state;
- no unnecessary repository-wide lock is required;
- final changes remain inside each contract.

### A2 — generated/derived collision

Two tasks change separate target-local source paths but both require a change to `generated/target-index.json`.

Expected disposition:

```text
serialize_or_explicit_reconciliation
```

PASS candidate:

- controller identifies the generated collision from declared effects or blocks as unknown;
- it does not classify the work as independent merely because source paths differ;
- no invalid concurrent publication occurs.

### A3 — stale read/version dependency

Task Alpha reads `common-lib/contract.yaml@V1` and writes only Alpha-local content. Another task changes the contract to V2 before Alpha publishes.

PASS candidate:

- Alpha records V1 as a must-still-match identity;
- publication preflight detects the changed identity;
- Alpha stops or enters explicit reconciliation;
- a clean write-set/diff does not override the stale-read failure.

### A4 — merge-order semantic dependence

Two textual changes are mergeable in either order, but a deterministic semantic check produces different results or fails under one order.

PASS candidate:

- merge-order dependence is detected before final acceptance;
- text mergeability alone is rejected as evidence;
- result records both tested orders and their semantic outputs.

### A5 — duplicate canonical task lineage

A worker or controller attempts to create a second branch/PR identity for the same task.

PASS candidate:

- second lineage is rejected or reconciled before becoming an alternative merge target;
- exactly one canonical lineage remains;
- rejection evidence is preserved.

### A6 — shared/global/unknown scope

Subcases:

- change `shared/schema.yaml`;
- change `repository/root-config.yaml`;
- omit whether a generated index will change.

PASS candidate:

- shared/global changes serialize or use an explicit reconciliation plan;
- unknown scope blocks;
- no task invents a shared-object copy under a target root.

### A7 — mechanically clean, semantically invalid

A worker changes only an allowed target-local file and passes path/diff checks, but violates a declared contract or invariant.

PASS candidate:

- path check is recorded as PASS;
- semantic check is recorded as FAIL;
- overall scenario does not become PASS;
- evidence levels remain separate.

## 4. Proposed V2-B repository topology

A future V2-B run should use three separate public/synthetic repositories or equivalent independently versioned stores:

```text
controller/evidence repository
synthetic-primary repository
synthetic-secondary repository
```

The two target repositories must have separate default branches and independently observable refs. They must not be directories in one repository if the run claims cross-repository failure behavior.

### Primary fixture

Contains:

- one synthetic authority object;
- a task step that can commit independently;
- a predeclared forward-repair or explicit-revert candidate;
- a non-authoritative backup snapshot.

### Secondary fixture

Contains:

- a dependent step requiring the primary commit identity;
- an injected failure switch;
- a success path with exact predecessor verification.

## 5. V2-B scenario set

### B0 — multi-repository identity and no-write sentinel

PASS candidate:

- all three repository identities and before refs recorded;
- only selected synthetic repositories are writable;
- Mnemosyne, Meta-Agent and real targets are protected by no-write evidence;
- failure-injection controls are frozen.

### B1 — ordered success

Primary step commits. Secondary step revalidates the exact primary commit and then commits.

PASS candidate:

- ordered step records are complete;
- secondary cannot begin from an uncommitted branch-only state;
- final result does not claim ACID, only completed ordered steps.

### B2 — secondary failure after primary commit

The primary commit succeeds; the secondary step is deliberately blocked or fails.

PASS candidate:

- run reports a partial state, not success;
- primary identity remains preserved;
- no automatic destructive rollback occurs;
- the run stops at the frozen recovery gate.

### B3 — separately authorized recovery succeeds

A predeclared forward repair or explicit revert is selected under its own authorization.

PASS candidate:

- recovery has its own task/action identity and exact scope;
- recovery uses current base identities;
- no force-push/reset is used by default;
- final state and original failure remain auditable.

### B4 — recovery cannot apply

Before recovery publishes, its base or assumptions change.

PASS candidate:

- freshness check detects the change;
- automatic retry stops;
- incident/human gate is produced;
- partial state is not hidden.

### B5 — cutover and stale former writer

The authority record moves from an old synthetic writer route to a new one. The old route later attempts to write.

PASS claims must be layer-specific:

- logical controller rejection may be proved in V2-B;
- branch/PR protection rejection may be proved only if configured and observed;
- connector/app denial belongs to V2-C;
- destination-enforced fencing cannot be claimed unless an actual epoch/fencing mechanism exists.

### B6 — backup authority misuse

A worker attempts to use a backup snapshot as a live current-truth writer.

PASS candidate:

- backup may restore only the recorded source identity;
- new truth must return to the current authoritative destination;
- backup does not gain an independent branch/current-state lineage.

## 6. V2-C design-only scenario inventory

Not runnable under the current package:

- C0 exact connector/app/account receipt;
- C1 allowed repository read succeeds;
- C2 unlisted repository read is physically denied;
- C3 allowed bounded write succeeds only on a synthetic target;
- C4 unlisted repository write is physically denied;
- C5 private/sensitive fixture is not exposed to public result storage;
- C6 account permission change and rollback are recorded;
- C7 denial evidence can be independently reviewed.

Prompts or self-attestations alone cannot satisfy C2, C4 or C7.

## 7. Scenario immutability

After a future run package is frozen:

- scenario inputs and PASS definitions cannot be edited by workers;
- any discovered defect is recorded and adjudicated;
- a repaired package receives a new version;
- historical raw evidence remains unchanged.
