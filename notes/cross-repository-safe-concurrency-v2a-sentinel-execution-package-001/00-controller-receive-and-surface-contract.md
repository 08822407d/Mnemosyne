# V2-A A0 Controller Receive and Surface Contract

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-CONTROLLER-RECEIVE-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-001
status: frozen_template_not_authorization
```

## 1. Controller identity

The future controller is one fresh ChatGPT conversation with the GitHub connector. It has no worker role and no authority to broaden the run.

```yaml
controller_contract:
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
  selected_stage: V2_A
  selected_cells:
    - A0
  controller_conversation_count: 1
  worker_conversations: 0
  product_surface: standard_ChatGPT_conversation_with_GitHub_connector
  required_visible_selection_if_available: gpt-5.6 sol extra high
  visible_selection_must_be_recorded_verbatim: true
  reasoning_setting_must_be_recorded_verbatim: true
  exact_backend_identity: unknown_or_not_attestable
  automatic_retry: false
  hidden_continuation: prohibited
```

A different visible model/product selection is not a harmless substitution. If the required option is unavailable, stop before any write and return to the Pro route.

## 2. Read-only receive gate

Before creating any branch, the controller must resolve all of the following:

```yaml
receive_inputs:
  Mnemosyne:
    repository: 08822407d/Mnemosyne
    expected_master: 2308c1e55fbbfb753ec527691809dd8f91f6f462
    exact_source_manifest_ref: notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-001/01-package-and-source-manifest.md

  Meta_Agent:
    repository: 08822407d/Meta-Agent
    expected_master: 1fdbd7af9437f72f7c8106714ad1e64908983fb7
    role: protected_read_only_ref

  validation_repository:
    repository: 08822407d/mnemosyne-target-lifecycle-validation-002
    visibility: public
    expected_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
    expected_fixture_ref: tlr-v1-fixture-base
    expected_fixture_commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
    expected_fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
    expected_controller_branch_absent: v2a-sentinel-001-controller
```

The controller must also confirm:

- the repository is public;
- all inspected fixture material is synthetic;
- no credential, secret, private conversation, real user record or real target truth is present;
- A0 is the only selected cell;
- no worker task, branch or PR is selected;
- no other app, connector, web research, Deep Research or Fable surface is enabled for the run;
- the future write paths are exactly the seven paths in the decision candidate.

## 3. Receive output template

The first future output file is:

```text
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/00-controller-receive.yaml
```

Required structure:

```yaml
controller_receive:
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
  package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-001
  validation_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-STAGED-VALIDATION-001
  selected_stage: V2_A
  selected_cells:
    - A0
  sentinel_only: true
  Mnemosyne_expected_master:
  Mnemosyne_observed_master:
  Meta_Agent_expected_master:
  Meta_Agent_observed_master:
  validation_repository_expected_master:
  validation_repository_observed_master:
  fixture_expected_ref:
  fixture_observed_ref:
  fixture_expected_commit:
  fixture_observed_commit:
  fixture_expected_tree:
  fixture_observed_tree:
  controller_branch_expected_absent:
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

## 4. Branch-creation gate

The controller may create the branch only when `receive_result: PASS` and the Owner's later G2A authorization is present and exact.

```yaml
branch_creation_contract:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  branch: v2a-sentinel-001-controller
  exact_parent: e8e3296922185b4b70997c2351d6f39423f2cd4f
  branch_must_be_absent_before_creation: true
  force_update: prohibited
  reuse_existing_branch: prohibited_without_Pro_reconciliation
  worker_or_fixture_branch_creation: prohibited
  PR_creation: prohibited
```

If branch creation returns an ambiguous result, do not retry blindly. Perform one read-only ref check and return the actual state.

## 5. Product and permission receipt

The second future output file is:

```text
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/01-product-and-permission-receipt.yaml
```

Required structure:

```yaml
product_and_permission_receipt:
  product_surface:
    value: standard_ChatGPT_conversation_with_GitHub_connector
    evidence_class: operator_observed
  operator_selection:
    verbatim:
    evidence_class: operator_reported_or_observed
  operator_reasoning_setting:
    verbatim:
    evidence_class: operator_reported_or_observed
  backend:
    status: unknown_or_not_attestable
    reason: consumer_chat_surface
  GitHub_authenticated_actor:
  repository_permissions_observed:
    validation_repository:
      read:
      write:
    Mnemosyne:
      read:
      write_capability_present_but_task_write_prohibited:
    Meta_Agent:
      read:
      write_capability_present_but_task_write_prohibited:
  task_authorized_actions:
    - create_exact_controller_branch
    - write_exact_seven_result_paths
    - perform_exact_read_only_ref_checks
  task_prohibited_actions:
    - write_Mnemosyne
    - write_Meta_Agent
    - write_existing_V1_refs
    - write_fixture
    - create_worker_branch
    - create_PR
    - run_A1_to_A7
    - retry
  physical_tool_capability_does_not_equal_task_authority: true
  receipt_result: PASS | BLOCKED
```

The receipt must distinguish physical connector capability from task authorization.

## 6. Receive stop conditions

Stop before any branch creation when:

- a source commit, blob, validation ref or fixture tree mismatches;
- the controller branch already exists;
- an open PR or conflicting task lineage exists;
- the visible model option is unavailable;
- the GitHub connector cannot read exact refs or create the exact branch;
- material classification is uncertain;
- any private or real-target content is found;
- any unlisted app/connector is required;
- an authorization field is missing or broader than the frozen package.

The controller returns `BLOCKED` and exact evidence. It does not repair the package, change the selected model, choose another repository, create a branch or retry.
