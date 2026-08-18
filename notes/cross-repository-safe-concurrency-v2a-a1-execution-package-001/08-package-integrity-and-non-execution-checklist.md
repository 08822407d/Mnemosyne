# V2-A A1 Package — Integrity and Non-Execution Checklist

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-INTEGRITY-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-001
status: preparation_checklist_not_run_authorization
```

## 1. Package completeness

```yaml
required_package_files:
  - README.md
  - 00-owner-gates-and-surface-contract.md
  - 01-package-and-source-manifest.md
  - 02-branch-task-and-effect-map.md
  - 03-alpha-worker-task.md
  - 04-beta-worker-task.md
  - 05-controller-task-and-order-construction.md
  - 06-mechanical-checks-and-result-template.md
  - 07-operator-flow-and-startup-messages.md
  - 08-package-integrity-and-non-execution-checklist.md
required_file_count: 10
source_manifest_self_hash_required: false
future_G2A_names_manifest_blob_separately: true
```

## 2. Frozen planning identities

Verify before merge and again after merge:

```yaml
source_master_at_preparation: 914cc1731fc8152610e215b064a81d057043bf0c
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
validation_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
fixture_commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
A0_controller_head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
frozen_tlr_v1_ref_count: 16
```

Normal Mnemosyne publication may move `master` after merge. Source integrity is established by exact path/blob identities; future G2A separately freezes the execution-window Mnemosyne/Meta-Agent refs.

## 3. A1 branch non-execution proof

During package preparation all of these must remain absent:

```text
v2a-a1-001-controller
v2a-a1-001-alpha
v2a-a1-001-beta
v2a-a1-001-order-alpha-beta
v2a-a1-001-order-beta-alpha
```

Preparation must not modify:

- validation `master`;
- `tlr-v1-fixture-base`;
- any `tlr-v1-*` ref;
- `v2a-sentinel-001-controller`;
- Meta-Agent;
- any real target.

## 4. Expected content and tree derivation

The exact four output blobs are:

```yaml
Alpha_source: 18959a155b44d1d24a14407f23bb8731eb5aaf49
Alpha_test: 9303a7ce7968512c1036c5ad19bbfd61c8db544a
Beta_source: 5ddad8381514e9a203ac1b5e67e38463fe2b14a2
Beta_test: a9eafff2c2e007f556dc789fecb4eb465e2955ca
```

Expected Git trees:

```yaml
Alpha_worker_root: 5929e4caeac1f10681057f530286e3d3dc27b28d
Beta_worker_root: 5dc4fa21362bb9e130de71779e2af0296eb11acc
Combined_both_orders_root: 2b919544aecfbd1634e5f136af22571f2e8d9fd0
```

The manifest must preserve the exact base tree entries and nested expected tree identities needed to reproduce these values. Workers may not replace exact content with a semantically similar variant.

## 5. Preparation-time non-effects

```yaml
A1_execution_authorized: false
controller_launched: false
worker_launched: false
validation_repository_written: false
A1_branches_created: false
A1_PR_created: false
A2_to_A7_executed: false
V2_B_or_V2_C_executed: false
Meta_Agent_modified: false
real_target_modified: false
Web_Deep_Research_Fable_used: false
external_quota_used: false
package_runtime_repair: false
automatic_retry: false
```

## 6. Future execution invalidation triggers

Fresh Pro must refresh or block before G2A if:

- any load-bearing source or package blob differs;
- validation master, fixture, A0 head or the 16-ref V1 inventory differs;
- any A1 branch/PR/equivalent lineage already exists;
- the validation repository visibility/material classification changes;
- the GitHub surface lacks create-blob/tree/commit/ref operations required by the frozen workflow;
- any model label, branch name, write set, output path, retry, quota, retention or cleanup term changes;
- another active route is expected to move the protected Mnemosyne or Meta-Agent ref during A1.

No executor may update this package in place. A substantive repair requires a new package version and preserves this version as evidence.

## 7. Post-run evidence boundary

If A1 later runs:

- all five A1 branches remain historical evidence;
- controller and workers cannot write adjudication into Mnemosyne;
- fresh Pro reviews the raw bundle read-only;
- the Owner separately accepts, revises, defers or rejects the result;
- durable writeback and branch cleanup each require separate authority;
- no result automatically authorizes A2–A7, V2-B, V2-C or a real target.
