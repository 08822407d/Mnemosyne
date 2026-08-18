# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
last_updated_by_task: MNEMOSYNE-231
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: A1_PACKAGE_002_DURABLE_EXECUTION_NOT_AUTHORIZED

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
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
  selected_cells: [A1]
  Owner_plan_preparation_selected: true
  package_001:
    id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-001
    preserved_immutable: true
    run_decision_candidate_001_blob: bb140196a38d8b14f6eba9e2175cd45744efb23b
    source_manifest_001_blob: 12a480449b1dac45cd265864a812f399d19ec15c
    execution_ready_as_written: false
  model_binding_order_defect:
    id: MNE-V2A-A1-MODEL-BINDING-ORDER-DEFECT-001
    status: confirmed_pre_execution_blocker
    classification: validation_protocol_and_package_profile_defect
    architecture_candidate_defect: false
    A1_runtime_failure: false
    A1_rerun_required: false
  package_002:
    id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-002
    role: additive_model_binding_and_operator_flow_repair
    run_decision_candidate_002_blob: a8b627b8aa74b5a1a5af19d3af485a17aa2cd0b7
    source_manifest_002_blob: 1f54f4711a44129c3dfee066aa2ab297f94718b7
    required_file_count: 6
    preserves_package_001_non_delta_semantics: true
  repaired_model_binding:
    controller_selected_label_bound_at: controller_G2A
    Alpha_authorized_label_bound_at: controller_G2A
    Beta_authorized_label_bound_at: controller_G2A
    Alpha_selected_label_bound_at: Alpha_worker_launch
    Beta_selected_label_bound_at: Beta_worker_launch
    worker_label_match_required_before_write: true
    hidden_backend_identity: unknown_or_not_attestable
  inherited_exact_profile_unchanged: true
  execution_authorized: false
  G2A_issued: false
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

The Fable report, exact input snapshot, fresh-Pro F2 adjudication and Owner Option A remain preserved under:

```text
raw/research-reports/cycles/2026Q3-cross-repository-safe-concurrency/
notes/research-adjudications/MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md
notes/cross-repository-safe-concurrency-and-ordered-work-amendment-candidate-v0.1.md
notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
```

The accepted direction remains provisional. It does not prove production readiness or authorize a real target.

## 2. Accepted A0 state

A0 remains Owner-accepted as:

```text
PASS_WITH_BOUNDED_EVIDENCE_DEFECTS
```

Its controller branch and seven historical outputs remain immutable. A0 neither requires rerun nor automatically authorizes A1.

## 3. A1 package 001 and discovered defect

Package 001 froze the fixture, branch map, worker/effect contracts, expected blobs/trees, order oracle, ten-file result set, no-PR, no-retry and retention rules.

A pre-execution review found one cross-file timing defect:

- package 001 required Alpha/Beta actual `operator_selected_visible_label` values in the controller G2A;
- the same package opened Alpha/Beta worker conversations only after controller G2A and preflight;
- those actual selected-label evidence objects therefore could not exist at G2A time.

The defect is recorded at:

```text
notes/validation-protocol-defects/
MNE-V2A-A1-MODEL-BINDING-ORDER-DEFECT-001.md
```

The prior execution-time review's mechanical source/ref/effect/order/tool findings remain useful. Its package-001 `ready_for_Owner_G2A` conclusion is superseded by this temporal blocker.

## 4. Additive package 002

Controlling repaired artifacts:

```text
notes/validation-run-decisions/
MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-002.md

notes/cross-repository-safe-concurrency-v2a-a1-execution-package-002/
```

Package 002 contains six files and supersedes package 001 only for:

- controller G2A model fields;
- worker selected-label timing;
- worker-opening/startup flow;
- staged model-receipt interpretation in the existing ten outputs.

All fixture, task, effect, branch, blob, tree, order, output, no-PR, no-retry and retention semantics remain inherited unchanged from package 001.

## 5. Repaired staged binding

```text
Owner G2A:
  controller authorized + actual selected label
  Alpha authorized label only
  Beta authorized label only

controller preflight and branch creation:
  freeze both immutable worker task payloads before first worker result

Alpha launch:
  bind Alpha actual selected label in its own fresh conversation
  compare before any write

Beta launch:
  bind Beta actual selected label in its own fresh conversation
  compare before any write
```

A missing, unknown or mismatched worker selected label blocks that worker before repository write. A planned or recommended label cannot substitute for actual worker-conversation evidence.

## 6. Current gate

```yaml
current_gate: PACKAGE_002_POST_MERGE_IDENTITY_REVIEW_THEN_SEPARATE_OWNER_G2A
package_002_publication_implies_G2A: false
A1_execution_authorized: false
required_before_A1_execution:
  - package_002_merged_and_exact_blobs_verified
  - fresh_Pro_execution_time_review_of_package_002_and_inherited_package_001
  - then_current_Mnemosyne_and_Meta_Agent_refs
  - controller_current_selected_label_and_exact_match
  - Alpha_and_Beta_Owner_authorized_labels
  - five_A1_branches_absent
  - no_competing_PR_or_lineage
  - explicit_Owner_G2A_for_A1_only
```

Worker selected labels are intentionally not G2A fields. They are required later at the respective worker pre-write gates.

## 7. Explicit boundaries

No current record authorizes:

- creation or movement of any A1 validation branch;
- modification of validation `master`, fixture, any `tlr-v1-*` ref or A0 controller;
- controller or worker launch;
- A1 execution or retry;
- modification of package 001;
- A2–A7, V2-B or V2-C;
- a validation PR or merge;
- Meta-Agent or real-target write/adoption;
- Web, Deep Research, Fable, another app, private material or external quota;
- package/fixture repair, reset, force-push or cleanup.
