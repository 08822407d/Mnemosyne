# V2-A A0 Controller Receive and Surface Contract — v2

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-CONTROLLER-RECEIVE-002
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-002
status: frozen_template_not_authorization
```

## 1. Controller identity

```yaml
controller_contract:
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
  selected_stage: V2_A
  selected_cells: [A0]
  controller_conversation_count: 1
  worker_conversations: 0
  product_surface: standard_ChatGPT_conversation_with_GitHub_connector
  authorized_visible_selection: supplied_by_G2A_owner_authorization
  visible_selection_must_be_recorded_verbatim: true
  reasoning_setting_must_be_recorded_verbatim: true
  exact_backend_identity: unknown_or_not_attestable
  automatic_retry: false
  hidden_continuation: prohibited
```

The recommended visible option remains `gpt-5.6 sol extra high` if available, but the controlling value is the exact label in the later Owner G2A authorization. No silent substitution is permitted.

## 2. Two-layer freshness model

### Layer A — immutable source/package identities

Before any write, verify:

- exact candidate-002 blob named by the Owner authorization;
- exact source-manifest-002 blob named by the Owner authorization;
- every path/blob pair listed in the source manifest;
- package id/version and selected cell `[A0]`.

These checks are independent of whether Mnemosyne `master` advanced solely to publish this package.

### Layer B — execution-window protected refs

The Owner G2A authorization supplies exact:

```yaml
execution_window_baseline:
  Mnemosyne_master:
  Meta_Agent_master:
```

The controller must observe those exact SHAs before creating the validation branch and again after A0. A mismatch is `BLOCKED`; the controller cannot refresh, repair or retry.

This separates source identity from no-write evidence and prevents package publication from invalidating itself.

## 3. Hard-pinned run dependencies

```yaml
validation_repository:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  expected_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
  expected_fixture_ref: tlr-v1-fixture-base
  expected_fixture_commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  expected_fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
  expected_controller_branch_absent: v2a-sentinel-001-controller
```

The full historical `tlr-v1-*` inventory is frozen in the source manifest. Any extra, missing or changed historical ref blocks A0.

## 4. Read-only receive gate

Before creating any branch, the controller must confirm:

- Owner G2A authorization is present and selects only A0;
- authorization candidate blob and source-manifest blob match exactly;
- all listed load-bearing source blobs match;
- execution-window protected external refs match the Owner authorization;
- validation repository is public and exact hard-pinned refs match;
- `v2a-sentinel-001-controller` is absent;
- no open PR uses that branch or equivalent A0 run lineage;
- fixture material remains public/synthetic within the inspected scope;
- no worker task/branch/PR is selected;
- only the exact seven output paths are authorized;
- required GitHub branch/ref/file operations are available;
- no unselected app, web research, Deep Research, Fable or private-file access is required.

Any false or unknown condition yields a read-only `BLOCKED` response and no validation-repository write.

## 5. Receive output

After receive PASS and authorized branch creation, create:

```text
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/00-controller-receive.yaml
```

Required structure:

```yaml
controller_receive:
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
  package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-002
  validation_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-STAGED-VALIDATION-001
  selected_stage: V2_A
  selected_cells: [A0]
  sentinel_only: true
  Owner_authorization_ref:
  expected_decision_candidate_blob:
  observed_decision_candidate_blob:
  expected_source_manifest_blob:
  observed_source_manifest_blob:
  immutable_source_blob_checks: []
  execution_window_baseline:
    Mnemosyne_expected_master:
    Mnemosyne_observed_master_before:
    Meta_Agent_expected_master:
    Meta_Agent_observed_master_before:
  validation_repository_expected_master:
  validation_repository_observed_master:
  fixture_expected_commit:
  fixture_observed_commit:
  fixture_expected_tree:
  fixture_observed_tree:
  V1_ref_inventory_result:
  controller_branch_expected_absent: true
  controller_branch_observed_absent:
  visible_product_surface:
  operator_selection_verbatim:
  operator_reasoning_setting_verbatim:
  GitHub_connector_available:
  other_apps_or_connectors_enabled: []
  material_class: public_synthetic_only
  material_safety_unknowns: []
  unresolved_inputs: []
  receive_result: PASS | BLOCKED
  block_reason:
```

## 6. Branch creation gate

Only after receive PASS:

```yaml
branch_creation_contract:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  branch: v2a-sentinel-001-controller
  exact_parent: e8e3296922185b4b70997c2351d6f39423f2cd4f
  branch_must_be_absent_before_creation: true
  force_update: prohibited
  reuse_existing_branch: prohibited_without_fresh_Pro_reconciliation
  worker_or_fixture_branch_creation: prohibited
  PR_creation: prohibited
```

If branch creation is ambiguous, perform one read-only ref lookup and stop. Do not retry or move a ref.

## 7. Product/permission receipt

Create only after branch creation:

```text
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/01-product-and-permission-receipt.yaml
```

It must separate:

- operator-visible product/model/reasoning selection;
- authenticated GitHub actor and observed physical capability;
- Owner-authorized task actions;
- prohibited task actions;
- `backend.status: unknown_or_not_attestable`.

Physical connector capability never expands task authority.

## 8. Receive stop conditions

Stop before branch creation when:

- decision-candidate or source-manifest blob differs from Owner authorization;
- any load-bearing source blob differs from the manifest;
- either execution-window protected ref differs from the Owner authorization;
- any hard-pinned validation/V1 identity differs;
- controller branch or competing lineage already exists;
- visible model selection differs from the authorized label;
- required GitHub operations are unavailable;
- material classification is uncertain;
- private/real-target content appears;
- scope, authorization or write paths are ambiguous.

The controller does not change this package, pick a substitute model, update expected refs or retry.
