# V2-A A0 Sentinel — Frozen Next-Tier Controller Task v2

> Not runnable until the Owner issues G2A authorization bound to candidate 002, source manifest 002, exact execution-window protected refs, and one visible model selection. Without that authorization, return `NOT_AUTHORIZED` and stop.

```yaml
task_artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-CONTROLLER-TASK-002
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-002
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
stage: V2_A
selected_cells: [A0]
sentinel_only: true
worker_tasks: []
status: frozen_not_authorized_not_executed
```

## 1. Mission

Run only the A0 package/identity/material/surface/permission/no-write sentinel. Do not test concurrency semantics, run A1–A7, create workers/PRs, modify the fixture, or reinterpret the package.

## 2. Instruction hierarchy

1. exact Owner G2A authorization;
2. package 002 at the exact merged candidate/source-manifest identities named by that authorization;
3. load-bearing source blobs listed by manifest 002;
4. exact public synthetic validation refs.

Historical package 001 is evidence of the repaired defect, not the runnable contract.

## 3. P0 — execution context

Record before repository writes:

- visible ChatGPT product/model/reasoning labels verbatim;
- GitHub authenticated actor and connector availability;
- other enabled apps/connectors;
- Owner G2A authorization reference;
- candidate-002 and manifest-002 expected blobs;
- execution-window Mnemosyne/Meta-Agent expected master SHAs;
- backend status `unknown_or_not_attestable`.

If visible selection differs from the Owner-authorized label, stop.

## 4. P1 — completely read-only preflight

### 4.1 Owner and package identity

Verify:

- Owner authorization selects only `A0`;
- exact merged `RUN-DECISION-CANDIDATE-002` blob equals the authorization value;
- exact merged `01-package-and-source-manifest.md` blob equals the authorization value;
- every path/blob pair in manifest 002 matches.

Do **not** require Mnemosyne `master` to equal the historical package-publication parent. Package publication is allowed to move `master`; load-bearing blob equality is the source-integrity test.

### 4.2 Execution-window protected refs

Verify current:

```yaml
Mnemosyne_master: exact_value_from_Owner_authorization
Meta_Agent_master: exact_value_from_Owner_authorization
```

These refs are no-write baselines, not source-document identities. Any mismatch blocks before validation-branch creation.

### 4.3 Validation repository

Verify:

```yaml
repository: 08822407d/mnemosyne-target-lifecycle-validation-002
visibility: public
master: e8e3296922185b4b70997c2351d6f39423f2cd4f
fixture_ref: tlr-v1-fixture-base
fixture_commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
controller_branch_absent: v2a-sentinel-001-controller
```

Re-enumerate every `tlr-v1-*` ref and compare exact names/SHAs to manifest 002. Verify no open validation PR uses the proposed controller branch or equivalent A0 run lineage.

### 4.4 Material safety

Inspect only identified public/synthetic fixture artifacts needed to support the material classification. Record exact scope and limitations. Do not claim exhaustive secret scanning unless a specific mechanical scan is actually run and preserved.

### 4.5 Preflight result

Any false or unknown required condition returns `BLOCKED` in conversation and stops with **zero validation-repository writes**. Do not create a branch merely to store a failed preflight.

## 5. P2 — create controller branch

Only after P1 PASS:

```yaml
repository: 08822407d/mnemosyne-target-lifecycle-validation-002
branch: v2a-sentinel-001-controller
parent: e8e3296922185b4b70997c2351d6f39423f2cd4f
force: false
```

Read the branch back immediately. If creation is ambiguous, perform one read-only ref lookup and stop; do not retry or move it.

## 6. P3 — exact seven-file write set

Write only:

```text
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/00-controller-receive.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/01-product-and-permission-receipt.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/02-package-and-material-receipt.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/03-repository-and-ref-baseline.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/04-mechanical-checks.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/incidents/incident-ledger.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/05-sentinel-result-bundle.yaml
```

For each output record exact path, blob SHA and creation/update commit SHA. `05-sentinel-result-bundle.yaml` is last because it references prior output identities.

## 7. P4 — mechanical checks

Use `03-mechanical-checks-and-result-template.md` from package 002.

Mandatory checks include:

- Owner/candidate/manifest authorization identity;
- all load-bearing source blobs;
- execution-window protected refs before/after;
- validation master, fixture and V1 inventory;
- controller branch parent;
- exact seven-file diff;
- no worker branch/PR;
- no unselected tools/quota/material;
- no hidden continuation/retry/package repair;
- output claim scope and limitations.

A missing check is never implicit PASS.

## 8. P5 — final result and stop

Allowed executor dispositions:

```text
SENTINEL_PASS_SELECTED_SCOPE
SENTINEL_PASS_WITH_BOUNDED_DEFECTS_FOR_PRO_REVIEW
SENTINEL_FAIL
SENTINEL_BLOCKED
```

After committing the final bundle:

- do not create/merge a PR;
- do not run A1–A7/V2-B/V2-C;
- do not write Mnemosyne/Meta-Agent;
- do not delete controller branch;
- do not retry;
- return seven outputs, final head, blob/commit identities, protected-ref comparisons, visible labels, incidents and limitations to a fresh Pro conversation.

## 9. Exact prohibited actions

```yaml
prohibited:
  - write_Mnemosyne
  - write_Meta_Agent
  - access_or_write_unnamed_real_target
  - modify_validation_master
  - modify_any_tlr_v1_ref
  - modify_fixture
  - create_worker_or_fixture_branch
  - create_PR
  - run_A1_to_A7
  - run_V2_B_or_V2_C
  - use_web_Deep_Research_Fable_or_other_app
  - use_private_material
  - repair_or_rebase_package
  - change_architecture
  - automatic_retry
  - automatic_compensation
  - reset_or_force_push
```

## 10. Escalation

Return to Pro without writes on source/blob/ref/model/lineage/material/permission ambiguity. Return to fresh Pro after writes if any check fails/disputes or evidence is weaker than frozen criteria.
