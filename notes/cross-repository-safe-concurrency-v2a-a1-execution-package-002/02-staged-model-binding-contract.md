# V2-A A1 Package 002 — Staged Model-Binding Contract

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-STAGED-MODEL-BINDING-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-002
status: frozen_contract_not_authorization
```

## 1. Roles and evidence times

```yaml
roles:
  controller:
    conversation_exists_before_G2A: true
    selected_label_bound_at: controller_G2A
  Alpha_worker:
    conversation_exists_before_G2A: false
    authorized_label_bound_at: controller_G2A
    selected_label_bound_at: Alpha_worker_launch
  Beta_worker:
    conversation_exists_before_G2A: false
    authorized_label_bound_at: controller_G2A
    selected_label_bound_at: Beta_worker_launch
```

The contract does not create a claim before its evidence can exist.

## 2. Controller G2A model fields

The controller G2A/startup message must contain:

```yaml
controller_model_binding:
  Owner_authorized_visible_label:
  operator_selected_visible_label:
  authorized_evidence_class: direct_user_instruction
  selected_evidence_class: operator_observed_or_operator_reported
  exact_raw_string_match_required: true
Alpha_model_authorization:
  Owner_authorized_visible_label:
  operator_selected_visible_label: not_yet_observed
Beta_model_authorization:
  Owner_authorized_visible_label:
  operator_selected_visible_label: not_yet_observed
backend_identity:
  status: unknown_or_not_attestable
```

`not_yet_observed` is an explicit state, not an error, because worker conversations have not been opened.

The controller must block before branch creation if:

- controller authorized or selected label is missing;
- controller raw strings differ;
- either worker authorized label is missing;
- a worker selected label is falsely asserted as already observed;
- any other G2A identity or scope condition fails.

## 3. Immutable worker task payloads

Before the first worker conversation is launched, the controller must preserve in `02-branch-task-effect-map.yaml`:

```yaml
Alpha_immutable_task_payload:
  task_id: MNE-V2A-A1-ALPHA-001
  source_package_path: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/03-alpha-worker-task.md
  source_blob: 9cb67f6e8b007941779326509db0b2d07fd035dd
  Owner_authorized_visible_label:
  selected_label_field: runtime_pending
Beta_immutable_task_payload:
  task_id: MNE-V2A-A1-BETA-001
  source_package_path: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/04-beta-worker-task.md
  source_blob: 9544963bc40face1eb3caca190de6fe5f96802f5
  Owner_authorized_visible_label:
  selected_label_field: runtime_pending
payloads_frozen_before_first_worker_result: true
```

The exact task file/blob and inherited package contracts freeze all execution semantics. The controller must not rewrite a task payload after a worker result appears.

## 4. Runtime worker receipt wrapper

At the actual worker launch, the operator supplies only the role-specific runtime receipt fields:

```yaml
worker_runtime_model_receipt:
  role: Alpha | Beta
  task_id:
  Owner_authorized_visible_label:
  operator_selected_visible_label:
  selected_evidence_class: operator_observed_or_operator_reported
  exact_raw_string_match:
  specific_conversation_scope: true
  backend_identity: unknown_or_not_attestable
```

The wrapper also names the immutable task payload path/blob and the pre-created branch head. It cannot alter the task.

## 5. Worker pre-write gate

Each worker must perform this gate before any repository mutation:

```yaml
worker_pre_write_gate:
  immutable_task_path_blob_match:
  branch_name_match:
  branch_head_equals_fixture_base:
  Owner_authorized_label_present:
  operator_selected_label_present:
  exact_raw_string_match:
  peer_runtime_output_received: false
  result: PASS | WORKER_BLOCKED_BEFORE_WRITE
```

A worker returns `WORKER_BLOCKED_BEFORE_WRITE` and stops when any required field is missing, unknown or mismatched.

No branch movement, file write, retry, model substitution or package repair may occur after a blocked pre-write gate.

## 6. Sequential launch and partial-state rule

The operator launch order is:

```text
Alpha
→ only after Alpha completes exactly, Beta
```

This order is an operational safety choice and does not modify the A1 independence oracle. Both immutable worker tasks were already frozen before Alpha began.

If Alpha blocks or fails:

- do not launch Beta;
- preserve the three initial branches and controller pre-worker outputs;
- return to fresh Pro.

If Beta blocks or fails after Alpha writes:

- preserve Alpha's exact branch evidence;
- do not construct either order branch;
- controller records the partial state and stops;
- no retry or rollback is authorized.

## 7. Controller result receipt mapping

Package 001's ten output paths remain unchanged. Package 002 changes only field timing and interpretation:

### `00-controller-receive.yaml`

Records the controller G2A, controller label pair, worker authorized labels and explicit `worker_selected_labels: runtime_pending`.

### `01-product-model-and-permission-receipt.yaml`

Initial controller write records:

```yaml
controller:
  authorized_label:
  selected_label:
  exact_match:
alpha_worker:
  authorized_label:
  selected_label: pending_worker_launch
  exact_match: pending
beta_worker:
  authorized_label:
  selected_label: pending_worker_launch
  exact_match: pending
```

Before final bundle completion, the controller may update this same file with the independently preserved worker receipts. This does not create an eleventh output.

### `02-branch-task-effect-map.yaml`

Preserves immutable task payloads and authorized worker labels before the first worker result. It does not contain invented selected labels.

### `03-alpha-worker-result.yaml` and `04-beta-worker-result.yaml`

Each records the exact runtime wrapper and model receipt actually returned by that worker.

### `08-a1-result-bundle.yaml`

Summarizes all three role-specific bindings and evidence limits.

## 8. Evidence ceiling

Exact raw-string equality supports only the claim that the authorized and operator-reported/observed visible labels match for the named conversation.

It does not prove:

- hidden/backend identity;
- provider routing or weights identity;
- that another conversation used the same backend;
- correctness of the worker output;
- wall-clock concurrency.
