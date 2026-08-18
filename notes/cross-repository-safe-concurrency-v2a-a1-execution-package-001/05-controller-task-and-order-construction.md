# V2-A A1 — Frozen Controller and Order-Construction Task

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-CONTROLLER-TASK-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-001
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
controller_task_id: MNE-V2A-A1-CONTROLLER-001
status: frozen_not_authorized_not_executed
```

## 1. Mission

Coordinate only A1. Establish the frozen source/ref/model/branch baseline; create three initial branches; preserve a complete task/effect map; independently verify two isolated workers; construct Alpha→Beta and Beta→Alpha order branches; compare exact final trees and static semantic oracles; write the exact ten-file controller bundle; stop for fresh Pro adjudication.

Do not perform either worker's target change on their behalf. Do not run A2–A7.

## 2. Phase C0 — read-only receive and preflight

Before any validation write, verify:

### Source and authority

- Owner G2A selects exactly A1 and names the exact run-decision and source-manifest blobs;
- every path/blob in the source manifest matches;
- A0 adjudication and Owner decision remain exact and do not require rerun/package repair;
- the A1 package is the published controlling package.

### Dynamic execution window

- current `Mnemosyne/master` equals the G2A value;
- current `Meta-Agent/master` equals the G2A value;
- no known open Mnemosyne PR or branch is expected to publish during the run window;
- controller, Alpha and Beta authorized/selected labels are present and exactly equal as separate raw strings;
- only GitHub connector use is authorized.

### Validation repository

Verify exactly:

```yaml
repository: 08822407d/mnemosyne-target-lifecycle-validation-002
master: e8e3296922185b4b70997c2351d6f39423f2cd4f
fixture_ref: tlr-v1-fixture-base
fixture_commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
A0_controller:
  branch: v2a-sentinel-001-controller
  head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
frozen_tlr_v1_ref_count: 16
open_validation_PRs: []
```

Re-enumerate the full branch inventory. The five A1 branch names must all be absent. Unexplained additional branches or any competing A1 lineage block.

### Fixture and semantic oracle

Verify base blobs and exact worker target blobs from the branch/task map. Read the exact four frozen target contents. Verify the precomputed worker and combined tree identities are derived from the exact fixture tree and path/blob replacements; do not refresh them from historical V1 S3 branches.

Any false or unknown required condition returns `CONTROLLER_BLOCKED` and stops with zero validation writes. A blocked preflight is returned in conversation; do not create a branch merely to record it.

## 3. Phase C1 — create initial branches

Only after C0 PASS, create exactly:

```yaml
v2a-a1-001-controller:
  parent: e8e3296922185b4b70997c2351d6f39423f2cd4f
v2a-a1-001-alpha:
  parent: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
v2a-a1-001-beta:
  parent: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
```

Use non-force branch creation. Read all three refs back immediately. If creation is ambiguous, perform one read-only ref lookup and stop; do not recreate or move a conflicting branch.

Do not create either order branch yet.

## 4. Phase C2 — write frozen pre-worker evidence

On `v2a-a1-001-controller`, write only the first three controller outputs:

```text
00-controller-receive.yaml
01-product-model-and-permission-receipt.yaml
02-branch-task-effect-map.yaml
```

The task/effect map must record both worker contracts and confirm all frozen intersections are empty. It must also preserve both complete worker startup messages before either worker result is returned.

After these files are committed, stop active work and return the two exact worker messages to the Owner. Do not monitor the worker branches in the background.

## 5. Phase C3 — worker execution separation

The Owner launches two fresh worker conversations using the frozen messages.

Requirements:

- both messages are fixed before the first worker result;
- each worker sees only its own task plus the peer's frozen non-sensitive task/effect summary, not peer runtime output;
- each worker writes only its own precreated branch;
- the controller does not write either worker branch;
- wall-clock overlap is not required and must not be claimed unless independently evidenced.

The controller resumes only after the Owner returns both worker completion messages or a stop/block report.

## 6. Phase C4 — independently verify workers

Do not trust worker summaries as sufficient evidence. Re-read GitHub.

### Alpha PASS candidate

```yaml
branch: v2a-a1-001-alpha
merge_base: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
commit_count_from_base: 1
changed_paths:
  - targets/agent-alpha/src/alpha_feature.py
  - targets/agent-alpha/tests/test_alpha_feature.py
final_tree: 5929e4caeac1f10681057f530286e3d3dc27b28d
final_blobs:
  source: 18959a155b44d1d24a14407f23bb8731eb5aaf49
  test: 9303a7ce7968512c1036c5ad19bbfd61c8db544a
```

### Beta PASS candidate

```yaml
branch: v2a-a1-001-beta
merge_base: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
commit_count_from_base: 1
changed_paths:
  - targets/agent-beta/src/beta_feature.py
  - targets/agent-beta/tests/test_beta_feature.py
final_tree: 5dc4fa21362bb9e130de71779e2af0296eb11acc
final_blobs:
  source: 5ddad8381514e9a203ac1b5e67e38463fe2b14a2
  test: a9eafff2c2e007f556dc789fecb4eb465e2955ca
```

Record `03-alpha-worker-result.yaml` and `04-beta-worker-result.yaml` on the controller branch only after each corresponding verification is complete.

If either worker is blocked, fails, writes an unexpected path, has more than one commit, produces an unexpected tree, reads peer runtime output, or has ambiguous lineage:

- do not create order branches;
- record the evidence and incident;
- write the final controller bundle with failure/blocked disposition;
- stop without retry.

## 7. Phase C5 — construct Alpha then Beta

Only after both workers pass:

1. Create `v2a-a1-001-order-alpha-beta` from the exact Alpha worker final head.
2. Build one tree from the Alpha final tree, replacing only:
   - `targets/agent-beta/src/beta_feature.py` with blob `5ddad8...`;
   - `targets/agent-beta/tests/test_beta_feature.py` with blob `a9eaff...`.
3. Require the new tree to equal:

```text
2b919544aecfbd1634e5f136af22571f2e8d9fd0
```

4. Create one commit with the Alpha head as parent and message:

```text
V2-A A1 order Alpha-Beta: apply verified Beta blobs
```

5. Re-read the order branch before ref movement; it must still equal the Alpha head.
6. Move the ref once, non-force.
7. Verify:
   - one integration commit after Alpha;
   - fixture→final diff exactly four frozen target paths;
   - final tree `2b9195...`;
   - no evidence/generated/shared/global path changed.
8. Record `05-order-alpha-beta-result.yaml`.

## 8. Phase C6 — construct Beta then Alpha

Symmetrically:

1. Create `v2a-a1-001-order-beta-alpha` from the exact Beta worker final head.
2. Apply only the two exact Alpha blobs.
3. Require tree `2b919544aecfbd1634e5f136af22571f2e8d9fd0`.
4. Create one commit with message:

```text
V2-A A1 order Beta-Alpha: apply verified Alpha blobs
```

5. Move the ref once, non-force, after confirming it still equals the Beta head.
6. Verify one integration commit, exact four-path fixture diff and no other effects.
7. Record `06-order-beta-alpha-result.yaml`.

The controller may not edit either order tree after a mismatch. A mismatch is preserved as a cell failure/dispute.

## 9. Phase C7 — semantic and mechanical evaluation

Record in `07-semantic-and-mechanical-checks.yaml`:

- exact worker task IDs, bases, heads, trees, blobs and diffs;
- complete declared effect sets and all intersections;
- both order branch identities and commit chains;
- both final root trees;
- static inspection of the four exact source/test blobs;
- expected example results encoded by the test files;
- unchanged generated, shared, governance and library trees;
- no worker/fixture/controller PR;
- protected refs before/after;
- evidence levels and limitations.

Required positive oracle:

```yaml
alpha_worker_tree: 5929e4caeac1f10681057f530286e3d3dc27b28d
beta_worker_tree: 5dc4fa21362bb9e130de71779e2af0296eb11acc
alpha_then_beta_tree: 2b919544aecfbd1634e5f136af22571f2e8d9fd0
beta_then_alpha_tree: 2b919544aecfbd1634e5f136af22571f2e8d9fd0
order_trees_equal: true
combined_expected_tree_match: true
unexpected_changed_paths: []
```

Runtime execution fields must remain `false`/`not_performed` unless a separately frozen execution surface actually ran a preserved command. Static content/tree equality must not be mislabeled runtime PASS.

## 10. Phase C8 — final bundle and stop

Maintain `incidents/incident-ledger.yaml` even when empty.

Write `08-a1-result-bundle.yaml` last. Allowed executor dispositions:

```text
PROVISIONAL_CELL_PASS_INDEPENDENT_CONCURRENCY_SUPPORTED
CELL_PASS_WITH_BOUNDED_DEFECTS_FOR_PRO_REVIEW
CELL_FAIL
CELL_BLOCKED
CELL_DISPUTED
```

After the final bundle:

- perform only the frozen read-only final branch/ref/PR checks;
- do not update any result again;
- do not create a PR;
- do not merge or delete branches;
- do not run A2–A7, V2-B or V2-C;
- return all branch heads, commit/tree/blob identities, model receipts, incidents, protected-ref checks and limitations to a fresh Pro adjudicator;
- stop.

## 11. Historical A0 and V1 boundaries

The A0 branch and sixteen `tlr-v1-*` branches are immutable evidence. Historical V1 S3 Alpha/Beta blobs may be used only as corroborating existing-object identities; the A1 workers must create new A1 branches and satisfy this package's stronger test blobs, tree oracle and controller evidence contract.
