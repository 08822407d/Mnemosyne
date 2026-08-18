# Cross-Repository Safe Concurrency V2-A A1 — Pro Exact Run-Decision Candidate 001

```yaml
run_decision_candidate_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-001
task_id: MNEMOSYNE-230
validation_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-STAGED-VALIDATION-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-001
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
stage: V2_A
selected_cells: [A1]
cell_name: positive_independent_pair
status: Pro_exact_plan_prepared_not_authorized_not_executed
source_master_at_preparation: 914cc1731fc8152610e215b064a81d057043bf0c
Owner_preparation_decision: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PREPARATION-OWNER-DECISION-001.md
A0_prerequisite:
  disposition: PASS_WITH_BOUNDED_EVIDENCE_DEFECTS
  Owner_accepted: true
  controller_final_head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
A1_execution_authorized: false
validation_repository_written_by_preparation: false
external_quota_authorized: false
real_target_adoption_authorized: false
```

## 1. Recommended exact profile

```yaml
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
material_class: public_synthetic_only
validation_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
fixture:
  branch: tlr-v1-fixture-base
  commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  tree: f1e221ce8aef404579b96adb3ab01319016889db

future_branches:
  controller: v2a-a1-001-controller
  alpha_worker: v2a-a1-001-alpha
  beta_worker: v2a-a1-001-beta
  alpha_then_beta: v2a-a1-001-order-alpha-beta
  beta_then_alpha: v2a-a1-001-order-beta-alpha

pull_requests: prohibited
validation_master_write: prohibited
fixture_or_tlr_v1_ref_write: prohibited
A0_controller_write: prohibited
```

The controller branch starts from validation `master`. Both worker branches start from the exact fixture commit. Each order branch starts from the corresponding first worker's final head and applies the peer's exact frozen blobs in one controller-owned integration commit.

## 2. Task and effect contracts

### Alpha

```yaml
task_id: MNE-V2A-A1-ALPHA-001
writer: one_fresh_next_tier_worker
base: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
read_and_version_set:
  - targets/agent-alpha/authority.yaml@73da56b34e8a078780a04ddc6db7a1b4ffc078ed
  - targets/agent-alpha/src/alpha_feature.py@27a2a0f2b679494c11d2885377e564a0b10ce896
  - targets/agent-alpha/tests/test_alpha_feature.py@f3e0535c9f830115acdedc9c1c8b637896a79791
exact_write_set:
  - targets/agent-alpha/src/alpha_feature.py
  - targets/agent-alpha/tests/test_alpha_feature.py
generated_or_derived_effects: []
shared_or_global_objects: []
semantic_contracts:
  - alpha_feature("  Example ") == "alpha-local:Example"
expected_final_blobs:
  targets/agent-alpha/src/alpha_feature.py: 18959a155b44d1d24a14407f23bb8731eb5aaf49
  targets/agent-alpha/tests/test_alpha_feature.py: 9303a7ce7968512c1036c5ad19bbfd61c8db544a
expected_final_root_tree: 5929e4caeac1f10681057f530286e3d3dc27b28d
```

### Beta

```yaml
task_id: MNE-V2A-A1-BETA-001
writer: one_fresh_next_tier_worker
base: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
read_and_version_set:
  - targets/agent-beta/authority.yaml@6310b0c931a4c0ee1ca35dd2ca107b586248e6f0
  - targets/agent-beta/src/beta_feature.py@8d4db9cae3d3f8dab7f99fca633ccbaa440dd3d9
  - targets/agent-beta/tests/test_beta_feature.py@f878642cfd1adee37efeb1768b95a7e1306d88f5
exact_write_set:
  - targets/agent-beta/src/beta_feature.py
  - targets/agent-beta/tests/test_beta_feature.py
generated_or_derived_effects: []
shared_or_global_objects: []
semantic_contracts:
  - beta_feature("  Example ") == "beta-local:Example"
expected_final_blobs:
  targets/agent-beta/src/beta_feature.py: 5ddad8381514e9a203ac1b5e67e38463fe2b14a2
  targets/agent-beta/tests/test_beta_feature.py: a9eafff2c2e007f556dc789fecb4eb465e2955ca
expected_final_root_tree: 5dc4fa21362bb9e130de71779e2af0296eb11acc
```

## 3. Independence and order oracle

```yaml
write_write_intersection: []
alpha_write_beta_read_intersection: []
beta_write_alpha_read_intersection: []
generated_or_derived_intersection: []
shared_or_global_intersection: []
uncommitted_peer_result_dependency: false

expected_combined_changed_paths:
  - targets/agent-alpha/src/alpha_feature.py
  - targets/agent-alpha/tests/test_alpha_feature.py
  - targets/agent-beta/src/beta_feature.py
  - targets/agent-beta/tests/test_beta_feature.py

expected_combined_root_tree: 2b919544aecfbd1634e5f136af22571f2e8d9fd0
required_order_results:
  alpha_then_beta_root_tree: 2b919544aecfbd1634e5f136af22571f2e8d9fd0
  beta_then_alpha_root_tree: 2b919544aecfbd1634e5f136af22571f2e8d9fd0
```

A1 tests branch/effect/order independence under this exact static semantic oracle. It does not claim wall-clock simultaneity, runtime test execution, provider-signed model identity, production readiness or general independence outside this fixture.

## 4. Product and conversation topology

```yaml
controller_conversations: 1
worker_conversations: 2
fresh_Pro_adjudication_conversations: 1
recommended_visible_label_for_all_execution_conversations: gpt-5.6 sol extra high
exact_backend_identity: unknown_or_not_attestable
model_labels_bound_by_future_G2A: true
Web_Deep_Research_Fable_other_apps: prohibited
external_quota: prohibited
```

The Alpha and Beta task messages must be frozen before either worker result is returned. They may be run sequentially by the operator, but neither worker may receive or read the peer's final branch head or output before completing its own branch.

## 5. Future G2A requirements

A future Owner execution authorization must bind in one exact controller startup message:

- this decision candidate's merged blob;
- the package source manifest's merged blob;
- then-current protected Mnemosyne and Meta-Agent master SHAs;
- the exact controller, Alpha and Beta authorized/selected visible labels;
- validation master, fixture, A0 head and pre-run branch inventory;
- the five exact A1 branch names;
- the exact controller output manifest and retention terms.

Any mismatch or unknown blocks before A1 branch creation. The controller may not refresh values, repair the package, substitute a model or retry.

## 6. Disposition

```yaml
Pro_recommendation: PREPARE_AND_PUBLISH_ONLY
G2A_execution_authorization: pending_future_Owner_decision
A1_execution: NOT_AUTHORIZED
A2_to_A7_execution: NOT_AUTHORIZED
V2_B_or_V2_C: NOT_AUTHORIZED
real_target_action: NOT_AUTHORIZED
```
