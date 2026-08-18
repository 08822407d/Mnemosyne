# V2-A A1 — Mechanical Checks and Result Template

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-MECHANICAL-RUBRIC-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-001
status: frozen_not_executed
```

Every check must be one of:

```text
PASS
FAIL
BLOCKED
NOT_APPLICABLE
DISPUTED_REQUIRES_FRESH_PRO
```

A missing check is not an implicit PASS.

## 1. Checks A1-M0 through A1-M24

```yaml
A1_M0_Owner_G2A_and_selected_scope:
A1_M1_run_decision_and_manifest_blobs:
A1_M2_load_bearing_source_blobs:
A1_M3_material_public_synthetic_boundary:
A1_M4_product_model_and_permission_receipts:
A1_M5_protected_Mnemosyne_Meta_Agent_refs_before:
A1_M6_validation_master_fixture_A0_and_V1_refs:
A1_M7_pre_run_branch_and_PR_inventory:
A1_M8_exact_five_branch_map:
A1_M9_task_effect_fields_complete:
A1_M10_effect_intersections_empty:
A1_M11_worker_messages_frozen_before_first_result:
A1_M12_Alpha_exact_base_one_commit_two_paths:
A1_M13_Alpha_exact_blobs_and_tree:
A1_M14_Beta_exact_base_one_commit_two_paths:
A1_M15_Beta_exact_blobs_and_tree:
A1_M16_peer_runtime_output_isolation:
A1_M17_Alpha_then_Beta_order_constructed:
A1_M18_Beta_then_Alpha_order_constructed:
A1_M19_order_trees_equal_expected_combined_tree:
A1_M20_static_semantic_oracles_match:
A1_M21_generated_shared_global_and_unrelated_trees_unchanged:
A1_M22_no_worker_or_controller_PR_no_extra_branch_no_extra_output:
A1_M23_protected_refs_after_and_retention:
A1_M24_no_hidden_continuation_retry_repair_or_later_cell:
```

## 2. Evidence requirements by check

### A1-M10 — effect intersections

Record complete normalized sets and their pairwise intersections. Empty write-set intersection alone is insufficient. Required empty sets include:

- write/write;
- Alpha write/Beta read;
- Beta write/Alpha read;
- generated/derived;
- shared/global;
- authority-object;
- branch identity.

### A1-M11 and A1-M16 — worker independence

Required evidence:

- both worker task messages have exact blob/text identities or are preserved verbatim in `02-branch-task-effect-map.yaml` before either worker completes;
- worker results record distinct conversation/model receipts;
- worker summaries and GitHub histories contain no peer final-head dependency;
- the operator may execute workers sequentially, but the messages may not be revised after observing the first result.

This check does not claim wall-clock simultaneous execution.

### A1-M12 through A1-M15 — worker branches

For each worker:

- merge base equals fixture commit;
- exactly one commit from base;
- exactly two changed paths;
- exact expected blobs;
- exact expected root tree;
- no evidence or peer path;
- ref moved non-force once after a still-current-base check.

### A1-M17 through A1-M19 — order construction

For each order:

- branch starts from the verified first worker head;
- exactly one controller integration commit is added;
- only the peer's two exact blobs are applied;
- fixture→final diff is exactly four paths;
- final tree is `2b919544aecfbd1634e5f136af22571f2e8d9fd0`;
- both order trees are equal.

### A1-M20 — semantic evidence

Required static oracle:

```yaml
Alpha:
  source_blob: 18959a155b44d1d24a14407f23bb8731eb5aaf49
  test_blob: 9303a7ce7968512c1036c5ad19bbfd61c8db544a
  expected_example: alpha-local:Example
Beta:
  source_blob: 5ddad8381514e9a203ac1b5e67e38463fe2b14a2
  test_blob: a9eafff2c2e007f556dc789fecb4eb465e2955ca
  expected_example: beta-local:Example
Combined:
  expected_root_tree: 2b919544aecfbd1634e5f136af22571f2e8d9fd0
```

Evidence strength must be recorded as `statically_inspected` and `mechanically_verified`. Runtime fields remain false unless a future package amendment freezes and authorizes a runtime surface.

### A1-M21 — unchanged effects

At minimum verify fixture and both order branches preserve unchanged identities for:

```yaml
repository_governance_tree: 9f8d6294fe97dc2d537df18c4c7abcc6897d4cb7
run_evidence_tree: 4572ca8616d6c88413e9efbdeae4fc199c170df2
runs_tree: b55b1fe8a41cdd81f224637fec5797c35fb5ac01
shared_tree: a61736f9f5a894dea4dda559513b3e355362ad4b
libraries_tree: 9ef4ba0f9e132202d0ec45c2e51e5c9e5567c2b5
generated_target_index_blob: 076ed542da7680901eb03cc4d00682550c5e4376
```

## 3. Exact controller output schemas

### `00-controller-receive.yaml`

```yaml
controller_receive:
  run_id:
  package_id:
  selected_stage: V2_A
  selected_cells: [A1]
  Owner_authorization_ref:
  decision_candidate_expected_observed:
  source_manifest_expected_observed:
  source_blob_results: []
  protected_refs_before: []
  validation_and_fixture_receipt:
  A0_and_V1_receipt:
  pre_run_branch_inventory:
  branch_absence_results:
  unresolved_inputs: []
  receive_result: PASS | BLOCKED
```

### `01-product-model-and-permission-receipt.yaml`

```yaml
product_model_permission_receipt:
  controller:
    authorized_label:
    selected_label:
    evidence_classes: []
    exact_match:
  alpha_worker:
    authorized_label:
    selected_label:
    evidence_classes: []
    exact_match:
  beta_worker:
    authorized_label:
    selected_label:
    evidence_classes: []
    exact_match:
  backend_identity: unknown_or_not_attestable
  GitHub_actor:
  observed_read_actions: []
  observed_write_actions: []
  other_apps_or_quota_used: []
  task_authority_does_not_equal_physical_capability: true
```

### `02-branch-task-effect-map.yaml`

```yaml
branch_task_effect_map:
  branch_map: {}
  alpha_contract: {}
  beta_contract: {}
  intersections: {}
  Alpha_worker_message_verbatim:
  Beta_worker_message_verbatim:
  messages_frozen_before_worker_completion:
```

### Worker result files

```yaml
worker_result:
  worker: Alpha | Beta
  task_id:
  operator_return_ref:
  independently_observed_branch_head:
  merge_base:
  commit_count:
  changed_paths: []
  final_blobs: {}
  final_tree:
  model_receipt:
  peer_runtime_output_read:
  incidents: []
  disposition:
```

### Order result files

```yaml
order_result:
  order: Alpha_then_Beta | Beta_then_Alpha
  branch:
  first_worker_head:
  integration_commit:
  integration_parent:
  applied_peer_blobs: {}
  commit_count_after_parent:
  fixture_to_final_changed_paths: []
  final_tree:
  expected_tree_match:
  unexpected_effects: []
  disposition:
```

### `07-semantic-and-mechanical-checks.yaml`

```yaml
semantic_and_mechanical_checks:
  checks_A1_M0_to_A1_M24: {}
  worker_tree_results: {}
  order_tree_results: {}
  static_semantic_oracles: {}
  evidence_strength:
    declared:
    artifact_present:
    statically_inspected:
    mechanically_verified:
    runtime_executed: false
    runtime_passed: false
    independently_reproduced:
    platform_signed_or_independently_attested:
    known_limitations: []
  disputed_checks: []
```

### Incident ledger

```yaml
incident_ledger:
  run_id:
  incidents:
    - incident_id:
      phase:
      category:
      exact_state_identities: []
      repository_side_effect:
      retry_performed: false
      repair_performed: false
      evidence_preserved:
      fresh_Pro_gate:
  confirmed_none:
```

### `08-a1-result-bundle.yaml`

```yaml
A1_result_bundle:
  run_id:
  selected_scope: [A1]
  controller_identity:
  worker_identities: []
  order_identities: []
  exact_output_blobs: {}
  protected_ref_before_after: []
  branch_and_PR_inventory_after:
  checks_ref:
  incident_ledger_ref:
  limitations: []
  executor_disposition:
    value: PROVISIONAL_CELL_PASS_INDEPENDENT_CONCURRENCY_SUPPORTED | CELL_PASS_WITH_BOUNDED_DEFECTS_FOR_PRO_REVIEW | CELL_FAIL | CELL_BLOCKED | CELL_DISPUTED
    reason:
  fresh_Pro_adjudication:
    status: pending
  A1_execution_only: true
  production_readiness_proven: false
  real_target_adoption_authorized: false
```

## 4. Positive acceptance candidate

All of the following are required for the executor to emit the provisional positive disposition:

- every A1-M check is PASS or explicitly NOT_APPLICABLE;
- both workers exactly match their frozen trees and contracts;
- all effect intersections are empty;
- both worker messages were frozen before first result;
- both order branches exactly match the combined tree;
- no generated/shared/global/unrelated change exists;
- protected refs remain unchanged at the bounded observation points;
- no PR, extra branch, extra output, retry, repair or later cell occurs;
- all evidence ceilings are honestly stated.

Fresh Pro may still classify a fixture, tool, protocol or executor defect and may reject or limit the provisional disposition.
