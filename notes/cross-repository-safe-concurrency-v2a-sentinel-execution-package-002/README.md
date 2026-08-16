# Cross-Repository Safe Concurrency V2-A A0 Sentinel — Execution Package 002

> Repaired preparation-only package for `MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001`. It supersedes package 001 **only for pre-run source binding and protected-Mnemosyne freshness semantics**. It does not authorize or execute A0.

```yaml
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-002
version: 0.2.0
task_id: MNEMOSYNE-224
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
selected_stage: V2_A
selected_cells: [A0]
sentinel_only: true
status: repaired_prepared_not_owner_authorized_not_executed
supersedes_for_scope:
  package: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-001
  exact_scope:
    - pre_run_Mnemosyne_source_binding
    - protected_Mnemosyne_and_Meta_Agent_execution_window_baseline
preserves_from_package_001:
  - validation_repository
  - validation_master_base
  - read_only_fixture_identity
  - complete_V1_ref_inventory
  - controller_branch_name
  - seven_file_write_set
  - no_worker_no_PR_boundary
  - model_surface_policy
  - no_retry_no_hidden_continuation
  - fresh_Pro_return_gate
validation_execution_authorized: false
controller_branch_created: false
validation_repository_written: false
```

## 1. Protocol defect repaired

Package 001 froze:

```text
Mnemosyne master@2308c1e55fbbfb753ec527691809dd8f91f6f462
```

as both a source identity and the required execution-window protected ref. Publishing package 001 through PR #291 necessarily moved `master` to:

```text
9157c476e8bf785f6440af4aaefbc44532d47c14
```

Therefore package 001 would fail its own freshness gate after successful publication. Re-publishing a new exact master SHA in another package would repeat the problem indefinitely.

`V2A-SENTINEL-PROTOCOL-DEFECT-001` fixes this by separating:

1. **immutable source/blob binding** — exact load-bearing path/blob identities are frozen in `01-package-and-source-manifest.md`;
2. **execution-window no-write baselines** — exact current `Mnemosyne/master` and `Meta-Agent/master` SHAs are supplied by the later Owner G2A authorization after this package is merged, then verified before and after A0.

The validation repository base and V1 fixture/ref identities remain hard-pinned because they are actual run/fixture dependencies rather than publication-window no-write baselines.

## 2. Files

```text
README.md
00-controller-receive-and-surface-contract.md
01-package-and-source-manifest.md
02-next-tier-controller-task.md
03-mechanical-checks-and-result-template.md
04-startup-message.md
05-package-integrity-and-non-execution-checklist.md
```

## 3. Frozen run topology

```yaml
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
visibility: public
controller_base: master@e8e3296922185b4b70997c2351d6f39423f2cd4f
read_only_fixture: tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
future_controller_branch: v2a-sentinel-001-controller
worker_branches: []
controller_PR: null
```

## 4. Frozen write boundary

Only after a later explicit G2A authorization, A0 may create `v2a-sentinel-001-controller` from the pinned validation master and write exactly seven result files under:

```text
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/
```

No fixture, `master`, historical `tlr-v1-*` ref, worker branch or PR may be modified or created.

## 5. Owner authorization contract

The later Owner G2A authorization must bind to:

- the exact merged blob of `MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-002.md`;
- the exact merged blob of `01-package-and-source-manifest.md`;
- an exact execution-window `Mnemosyne/master` SHA observed after this package is merged;
- an exact execution-window `Meta-Agent/master` SHA observed at the same Pro freshness gate;
- the exact visible model option selected for the fresh controller conversation.

No additional Mnemosyne write may occur between that Owner authorization/final freshness check and A0 launch. If either protected external ref moves, A0 blocks before creating the controller branch.

## 6. Current gate

```yaml
G1A_repaired_package_prepared: true
G2A_execution_authorized: false
A0_executed: false
A1_to_A7_authorized: false
V2_B_authorized: false
V2_C_authorized: false
```

Merge of this package is not run authorization.
