# Cross-Repository Safe Concurrency V2-A A1 — Pro Repaired Run-Decision Candidate 002

```yaml
run_decision_candidate_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-002
task_id: MNEMOSYNE-231
validation_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-STAGED-VALIDATION-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-002
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
stage: V2_A
selected_cells: [A1]
cell_name: positive_independent_pair
status: Pro_repaired_exact_plan_not_authorized_not_executed
source_master_at_repair: 4ff2d021a568ae3bfdf98c7dee81d87545fcd3d1
Owner_repair_authorization: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-002-PREPARATION-OWNER-DECISION-001.md
source_defect: notes/validation-protocol-defects/MNE-V2A-A1-MODEL-BINDING-ORDER-DEFECT-001.md
supersedes_candidate_001_scope:
  - controller_G2A_model_label_fields
  - Alpha_Beta_operator_selected_label_timing
  - worker_opening_and_startup_flow
candidate_001_other_semantics_preserved: true
A1_execution_authorized: false
validation_repository_written_by_repair: false
```

## 1. Inherited exact run profile

Candidate 002 preserves candidate 001 and package 001 for every field not explicitly superseded by additive package 002.

```yaml
inherited_candidate_001:
  path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-001.md
  blob: bb140196a38d8b14f6eba9e2175cd45744efb23b
inherited_package_001_manifest:
  path: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/01-package-and-source-manifest.md
  blob: 12a480449b1dac45cd265864a812f399d19ec15c
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
material_class: public_synthetic_only
validation_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
fixture:
  branch: tlr-v1-fixture-base
  commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  tree: f1e221ce8aef404579b96adb3ab01319016889db
A0_controller:
  branch: v2a-sentinel-001-controller
  final_head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
future_branches:
  controller: v2a-a1-001-controller
  alpha_worker: v2a-a1-001-alpha
  beta_worker: v2a-a1-001-beta
  alpha_then_beta: v2a-a1-001-order-alpha-beta
  beta_then_alpha: v2a-a1-001-order-beta-alpha
pull_requests: prohibited
```

The Alpha/Beta contracts, expected blobs and trees, combined order tree, controller ten-file result paths, no-retry rule and retention rule remain exactly those frozen by candidate/package 001.

## 2. Repaired staged model binding

### Phase C — Controller G2A/startup

A future Owner G2A binds:

```yaml
controller:
  Owner_authorized_visible_label:
  operator_selected_visible_label:
  exact_raw_string_equality_required: true
alpha_worker:
  Owner_authorized_visible_label:
  operator_selected_visible_label: pending_until_worker_launch
beta_worker:
  Owner_authorized_visible_label:
  operator_selected_visible_label: pending_until_worker_launch
backend_identity:
  status: unknown_or_not_attestable
```

The controller selected label must be current operator-observed or operator-reported evidence for the actual controller conversation.

The Alpha and Beta authorized labels are authorization constraints only. The G2A must not claim that either worker has already selected a model.

### Phase W-A — Alpha launch

After controller preflight passes, the three initial branches exist and both worker task payloads are preserved before any worker result:

- the operator opens the fresh Alpha conversation;
- selects or observes the current visible label;
- supplies that exact raw string in the Alpha runtime wrapper;
- Alpha verifies `selected == Owner-authorized` before any write.

### Phase W-B — Beta launch

Beta independently performs the same binding in its own fresh conversation after the task payload was already frozen.

A worker's missing, unknown or mismatched selected-label evidence produces:

```text
WORKER_BLOCKED_BEFORE_WRITE
```

No model substitution or retry is authorized.

## 3. Immutable task payload versus dynamic runtime wrapper

Each worker startup consists of two distinct evidence objects:

```yaml
immutable_worker_task_payload:
  source: exact_package_001_worker_task_path_and_blob
  frozen_before_first_worker_result: true
  runtime_mutation_allowed: false
runtime_model_receipt_wrapper:
  Owner_authorized_visible_label:
  operator_selected_visible_label:
  exact_raw_string_match:
  evidence_classes:
    - direct_user_instruction
    - operator_observed_or_operator_reported
  may_change_task_semantics: false
```

Only the operator-selected receipt is supplied at worker launch. It cannot alter branch, task ID, read/write/effect contract, expected content, oracle, output scope or prohibitions.

## 4. Repaired operator order

```text
package 002 publication and post-merge verification
→ fresh Pro execution-time review
→ Owner controller G2A with controller selected label and worker authorized labels
→ controller read-only preflight
→ controller creates controller / Alpha / Beta branches
→ controller writes 00/01/02 and preserves both immutable worker task payloads
→ controller stops and returns the two frozen worker launch payloads
→ Owner opens Alpha conversation and binds Alpha selected label at launch
→ if Alpha PASS, Owner opens Beta conversation and binds Beta selected label at launch
→ Owner returns both raw outputs to controller
→ controller verifies, constructs both order branches and completes ten-file bundle
→ fresh Pro adjudication
→ Owner disposition
```

If Alpha blocks or fails, Beta is not launched. If Beta blocks or fails after Alpha has written, Alpha evidence is preserved and the run stops without order-branch construction.

No wall-clock simultaneity claim follows from sequential operator launch.

## 5. Future controller G2A dynamic fields

A future G2A must bind:

- candidate 002 merged blob;
- package 002 source-manifest merged blob;
- then-current protected Mnemosyne and Meta-Agent master SHAs;
- controller Owner-authorized and current operator-selected labels;
- Alpha Owner-authorized label;
- Beta Owner-authorized label;
- validation master, fixture and A0 head;
- complete pre-run branch/PR inventory;
- exact five-branch map;
- exact ten-file controller output manifest;
- no-PR, no-retry and retention terms;
- confirmation that no known competing route will move protected refs during the bounded execution window.

The controller G2A must not contain asserted Alpha/Beta selected-label values.

## 6. Unchanged execution and evidence boundaries

```yaml
A1_execution: NOT_AUTHORIZED
A2_to_A7_execution: NOT_AUTHORIZED
V2_B_or_V2_C: NOT_AUTHORIZED
real_target_action: NOT_AUTHORIZED
Web_Deep_Research_Fable_other_apps: PROHIBITED
external_quota: PROHIBITED
package_001_modification: PROHIBITED
validation_branch_creation_by_this_candidate_publication: PROHIBITED
```

Package 002 repairs temporal satisfiability and provenance only. It does not strengthen the evidence ceiling, change the test oracle or authorize execution.
