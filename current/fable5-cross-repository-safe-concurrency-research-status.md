# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
last_updated_by_task: MNEMOSYNE-230
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: A1_EXACT_RUN_PLAN_PREPARED_EXECUTION_NOT_AUTHORIZED

Fable_report_received: true
fresh_Pro_F2_adjudication_completed: true
Owner_F2_option_A_accepted: true
V2_staged_design_prepared: true

V2_A_A0:
  plan_prepared: true
  executed: true
  controller_branch: v2a-sentinel-001-controller
  final_head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
  fresh_Pro_adjudication_completed: true
  Owner_adjudication_accepted: true
  disposition: PASS_WITH_BOUNDED_EVIDENCE_DEFECTS
  rerun_required: false
  package_003_repair_required: false
  historical_outputs_rewritten: false
  controller_branch_modified_or_deleted_after_adjudication: false
  durable_evidence_correction_recorded: true

V2_A_A1:
  Owner_plan_preparation_selected: true
  exact_run_plan_prepared: true
  package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-001
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
  selected_cells: [A1]
  execution_authorized: false
  controller_launched: false
  worker_launched: false
  validation_repository_written: false
  branches_created: false
  PRs_created: false
  external_quota_authorized: false

A2_to_A7_execution_authorized: false
V2_B_execution_authorized: false
V2_C_execution_authorized: false
Meta_Agent_write_authorized: false
real_target_write_or_adoption_authorized: false
automatic_retry_or_repair_authorized: false
```

## 1. Preserved Fable research and accepted F2 direction

The exact Fable report, input snapshot, fresh Pro F2 adjudication and Owner Option A remain preserved under:

```text
raw/research-reports/cycles/2026Q3-cross-repository-safe-concurrency/
notes/research-adjudications/MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md
notes/cross-repository-safe-concurrency-and-ordered-work-amendment-candidate-v0.1.md
notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
```

The accepted direction remains a provisional architecture baseline. It does not prove production readiness or authorize any real target.

## 2. Accepted A0 state

Durable A0 records:

```text
notes/validation-adjudications/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-ADJUDICATION-001.md
notes/evidence-corrections/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-PATH-IDENTITY-CORRECTION-001.md
notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-OWNER-DECISION-001.md
```

Accepted result:

```yaml
overall_A0_adjudication: PASS_WITH_BOUNDED_EVIDENCE_DEFECTS
repository_safety_and_write_boundary: PASS
frozen_ref_and_inventory_integrity: PASS
package_and_source_content_integrity: PASS
evidence_record_integrity: PASS_WITH_ONE_BOUNDED_PATH_IDENTITY_DEFECT
A0_rerun_required: false
package_repair_required: false
```

The bounded defects remain historical evidence:

- `A0-TOOL-001` — non-blocking unsupported read shortcut; required evidence was recovered using distinct supported read-only operations without repeating the failed call;
- one false shortened path in historical A0 output 02; the canonical package path/blob was independently verified and preserved through an additive correction.

A0 does not automatically authorize A1 or any later cell.

## 3. A1 preparation decision

The Owner selected preparation only:

```text
notes/owner-decision-results/
MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PREPARATION-OWNER-DECISION-001.md
```

This permits an exact Mnemosyne run plan/package and one Ready PR. It does not permit a validation-repository branch, file, commit, PR, worker launch or cell execution.

## 4. A1 exact run decision and package

```text
notes/validation-run-decisions/
MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-001.md

notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/
```

The package contains ten files and freezes:

- one controller, two worker and two order-simulation branch names;
- one public/synthetic fixture commit and tree;
- two exact two-path worker contracts;
- complete read/write/generated/shared/global/authority effect sets;
- four exact output blobs;
- exact Alpha-only, Beta-only and combined Git trees;
- both Alpha→Beta and Beta→Alpha order-construction contracts;
- a ten-file controller result manifest;
- model-label evidence, stop/no-retry rules and retention;
- fresh Pro adjudication after any future execution.

## 5. Exact future validation profile

```yaml
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
validation_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
fixture:
  ref: tlr-v1-fixture-base
  commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  tree: f1e221ce8aef404579b96adb3ab01319016889db
A0_controller:
  ref: v2a-sentinel-001-controller
  head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
future_A1_branches:
  - v2a-a1-001-controller
  - v2a-a1-001-alpha
  - v2a-a1-001-beta
  - v2a-a1-001-order-alpha-beta
  - v2a-a1-001-order-beta-alpha
future_validation_PRs: prohibited
```

### Frozen worker outputs

```yaml
Alpha:
  paths:
    - targets/agent-alpha/src/alpha_feature.py
    - targets/agent-alpha/tests/test_alpha_feature.py
  blobs:
    source: 18959a155b44d1d24a14407f23bb8731eb5aaf49
    test: 9303a7ce7968512c1036c5ad19bbfd61c8db544a
  expected_root_tree: 5929e4caeac1f10681057f530286e3d3dc27b28d
Beta:
  paths:
    - targets/agent-beta/src/beta_feature.py
    - targets/agent-beta/tests/test_beta_feature.py
  blobs:
    source: 5ddad8381514e9a203ac1b5e67e38463fe2b14a2
    test: a9eafff2c2e007f556dc789fecb4eb465e2955ca
  expected_root_tree: 5dc4fa21362bb9e130de71779e2af0296eb11acc
both_orders_expected_root_tree: 2b919544aecfbd1634e5f136af22571f2e8d9fd0
```

The oracle is static content inspection plus mechanical Git identity comparison. Runtime tests and wall-clock concurrency are not required and must not be claimed from this package.

## 6. Current gate

```yaml
current_gate: OWNER_SEPARATE_DECISION_AFTER_PACKAGE_MERGE_AND_EXECUTION_TIME_PRO_RECHECK
A1_automatically_authorized_by_package_merge: false
reuse_A0_G2A_for_A1: false
A1_execution_authorized: false
required_before_A1_execution:
  - package_merged_and_exact_blobs_verified
  - fresh_Pro_execution_time_source_ref_branch_and_product_review
  - then_current_Mnemosyne_and_Meta_Agent_refs
  - exact_controller_Alpha_Beta_visible_model_label_binding
  - five_A1_branches_absent
  - no_competing_PR_or_lineage
  - explicit_Owner_G2A_for_A1_only
```

## 7. Explicit boundaries

No current record authorizes:

- creation or movement of any A1 validation branch;
- modification of validation `master`, fixture, any `tlr-v1-*` ref or the A0 controller;
- controller or worker launch;
- A1 execution or retry;
- A2–A7, V2-B or V2-C;
- a validation PR or merge;
- Meta-Agent or real-target write/adoption;
- Web, Deep Research, Fable, another app, private material or external quota;
- package/fixture repair, reset, force-push or branch cleanup.
