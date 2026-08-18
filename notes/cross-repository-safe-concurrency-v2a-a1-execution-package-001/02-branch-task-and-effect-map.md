# V2-A A1 — Branch, Task and Effect Map

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-BRANCH-TASK-MAP-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-001
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
status: frozen_not_executed
```

## 1. Repository and branch topology

```yaml
repository: 08822407d/mnemosyne-target-lifecycle-validation-002
controller_base: e8e3296922185b4b70997c2351d6f39423f2cd4f
fixture_base: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
branches:
  controller:
    name: v2a-a1-001-controller
    initial_parent: e8e3296922185b4b70997c2351d6f39423f2cd4f
    writer: controller_only
  alpha:
    name: v2a-a1-001-alpha
    initial_parent: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
    writer: alpha_worker_only
  beta:
    name: v2a-a1-001-beta
    initial_parent: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
    writer: beta_worker_only
  alpha_then_beta:
    name: v2a-a1-001-order-alpha-beta
    initial_parent: verified_alpha_worker_final_head
    writer: controller_only
  beta_then_alpha:
    name: v2a-a1-001-order-beta-alpha
    initial_parent: verified_beta_worker_final_head
    writer: controller_only
pull_requests: []
```

The order branches are interleaving simulations, not merge targets. No order branch may be created before both worker branches have passed exact final-tree and write-set checks.

## 2. Alpha task contract

```yaml
task_id: MNE-V2A-A1-ALPHA-001
cell_id: A1
canonical_branch: v2a-a1-001-alpha
canonical_PR: null
primary_writer: one_fresh_alpha_worker
base_sha: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
authority_object: synthetic_agent_alpha_target_local_feature
read_and_version_set:
  - path: targets/agent-alpha/authority.yaml
    expected_blob: 73da56b34e8a078780a04ddc6db7a1b4ffc078ed
    must_still_match_before_publication: true
  - path: targets/agent-alpha/src/alpha_feature.py
    expected_blob: 27a2a0f2b679494c11d2885377e564a0b10ce896
    must_still_match_before_publication: true
  - path: targets/agent-alpha/tests/test_alpha_feature.py
    expected_blob: f3e0535c9f830115acdedc9c1c8b637896a79791
    must_still_match_before_publication: true
exact_write_set:
  - targets/agent-alpha/src/alpha_feature.py
  - targets/agent-alpha/tests/test_alpha_feature.py
generated_or_derived_effects: []
shared_or_repository_global_objects: []
semantic_contracts:
  - ALPHA-A1-STATIC-001
ordered_dependencies: []
tool_scope:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  allowed_branch: v2a-a1-001-alpha
  allowed_actions: [read_exact_fixture, create_exact_blobs, create_one_tree, create_one_commit, fast_forward_own_branch]
expected_final_blobs:
  targets/agent-alpha/src/alpha_feature.py: 18959a155b44d1d24a14407f23bb8731eb5aaf49
  targets/agent-alpha/tests/test_alpha_feature.py: 9303a7ce7968512c1036c5ad19bbfd61c8db544a
expected_final_subtrees:
  src: 36a77ea02517a7ab96a72562557e9b8d1d3f2960
  tests: 58fcc6280675dce8b717f66821eaf360e5bfcd9d
  agent_alpha: 9f30907c7174fb00f1f80b90dc118a9c2eef344e
  targets: fdb87ba25d93da5fa0a82410d592062a0cca118b
expected_final_root_tree: 5929e4caeac1f10681057f530286e3d3dc27b28d
expected_commit_count_from_fixture: 1
```

## 3. Beta task contract

```yaml
task_id: MNE-V2A-A1-BETA-001
cell_id: A1
canonical_branch: v2a-a1-001-beta
canonical_PR: null
primary_writer: one_fresh_beta_worker
base_sha: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
authority_object: synthetic_agent_beta_target_local_feature
read_and_version_set:
  - path: targets/agent-beta/authority.yaml
    expected_blob: 6310b0c931a4c0ee1ca35dd2ca107b586248e6f0
    must_still_match_before_publication: true
  - path: targets/agent-beta/src/beta_feature.py
    expected_blob: 8d4db9cae3d3f8dab7f99fca633ccbaa440dd3d9
    must_still_match_before_publication: true
  - path: targets/agent-beta/tests/test_beta_feature.py
    expected_blob: f878642cfd1adee37efeb1768b95a7e1306d88f5
    must_still_match_before_publication: true
exact_write_set:
  - targets/agent-beta/src/beta_feature.py
  - targets/agent-beta/tests/test_beta_feature.py
generated_or_derived_effects: []
shared_or_repository_global_objects: []
semantic_contracts:
  - BETA-A1-STATIC-001
ordered_dependencies: []
tool_scope:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  allowed_branch: v2a-a1-001-beta
  allowed_actions: [read_exact_fixture, create_exact_blobs, create_one_tree, create_one_commit, fast_forward_own_branch]
expected_final_blobs:
  targets/agent-beta/src/beta_feature.py: 5ddad8381514e9a203ac1b5e67e38463fe2b14a2
  targets/agent-beta/tests/test_beta_feature.py: a9eafff2c2e007f556dc789fecb4eb465e2955ca
expected_final_subtrees:
  src: 5fd10b293e5ede521870e4a9d277676a4de5b432
  tests: af6fa1eef776cb4548cb7dc251ff93cb798c8667
  agent_beta: e004404edde45225ea53d9ab84997bcf7921f618
  targets: 24fc0174e5d1c77a9bb2068302809e8aaf6a0c8b
expected_final_root_tree: 5dc4fa21362bb9e130de71779e2af0296eb11acc
expected_commit_count_from_fixture: 1
```

## 4. Intersection proof required before worker launch

```yaml
write_write_intersection: []
alpha_write_beta_read_intersection: []
beta_write_alpha_read_intersection: []
read_read_intersection: []
generated_or_derived_intersection: []
shared_or_global_intersection: []
authority_object_intersection: []
branch_intersection: []
uncommitted_result_dependency: false
merge_order_expectation: order_independent
```

The controller must compute these from the frozen task map; it may not accept worker self-classification as sufficient evidence.

## 5. Order-construction contracts

### Alpha then Beta

```yaml
branch: v2a-a1-001-order-alpha-beta
parent: verified_alpha_worker_final_head
controller_applies_exact_blobs:
  targets/agent-beta/src/beta_feature.py: 5ddad8381514e9a203ac1b5e67e38463fe2b14a2
  targets/agent-beta/tests/test_beta_feature.py: a9eafff2c2e007f556dc789fecb4eb465e2955ca
expected_commit_count_after_parent: 1
expected_final_root_tree: 2b919544aecfbd1634e5f136af22571f2e8d9fd0
```

### Beta then Alpha

```yaml
branch: v2a-a1-001-order-beta-alpha
parent: verified_beta_worker_final_head
controller_applies_exact_blobs:
  targets/agent-alpha/src/alpha_feature.py: 18959a155b44d1d24a14407f23bb8731eb5aaf49
  targets/agent-alpha/tests/test_alpha_feature.py: 9303a7ce7968512c1036c5ad19bbfd61c8db544a
expected_commit_count_after_parent: 1
expected_final_root_tree: 2b919544aecfbd1634e5f136af22571f2e8d9fd0
```

Both order commits must be created from the verified worker tree and peer blobs. They may not be hand-edited to force equality.

## 6. Static semantic oracle

```yaml
ALPHA-A1-STATIC-001:
  source_blob: 18959a155b44d1d24a14407f23bb8731eb5aaf49
  test_blob: 9303a7ce7968512c1036c5ad19bbfd61c8db544a
  expected_example: alpha_feature("  Example ") == "alpha-local:Example"
BETA-A1-STATIC-001:
  source_blob: 5ddad8381514e9a203ac1b5e67e38463fe2b14a2
  test_blob: a9eafff2c2e007f556dc789fecb4eb465e2955ca
  expected_example: beta_feature("  Example ") == "beta-local:Example"
COMBINED-A1-TREE-001:
  expected_root_tree: 2b919544aecfbd1634e5f136af22571f2e8d9fd0
  required_changed_paths: 4
  generated_shared_global_changes: 0
```

The required evidence level is static inspection plus mechanical Git identity verification. This package does not require or permit an executor to claim runtime test execution without a separately frozen product/tool contract.

## 7. Controller evidence write set

```text
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001/00-controller-receive.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001/01-product-model-and-permission-receipt.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001/02-branch-task-effect-map.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001/03-alpha-worker-result.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001/04-beta-worker-result.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001/05-order-alpha-beta-result.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001/06-order-beta-alpha-result.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001/07-semantic-and-mechanical-checks.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001/incidents/incident-ledger.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001/08-a1-result-bundle.yaml
```

Exact controller output count: 10. No worker writes these files. No eleventh output is authorized.
