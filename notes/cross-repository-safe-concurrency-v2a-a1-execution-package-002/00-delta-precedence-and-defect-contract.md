# V2-A A1 Package 002 — Delta Precedence and Defect Contract

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-002-DELTA-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-002
status: frozen_additive_delta_not_authorization
source_defect: MNE-V2A-A1-MODEL-BINDING-ORDER-DEFECT-001
```

## 1. Historical preservation

The following remain unchanged and must not be edited in place:

```text
notes/validation-run-decisions/
MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-001.md

notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/
```

Package 001 is the complete historical plan that exposed the temporal model-binding defect. Package 002 is an additive repair layer.

## 2. Exact supersession scope

Package 002 supersedes package 001 only where package 001 requires or implies:

1. Alpha/Beta `operator_selected_visible_label` values in the controller G2A before those conversations exist;
2. a controller preflight check that treats future worker selected labels as already observed facts;
3. a worker startup message that is frozen only as one inseparable text object containing a future runtime selection value;
4. a product/model receipt that cannot distinguish pre-worker authorization from worker-launch selection evidence;
5. an operator flow that has no explicit worker-launch binding gate before repository write.

When package 001 and package 002 differ on one of these points, package 002 controls.

## 3. Exact inherited scope

Package 001 remains controlling for all other fields. In particular:

```yaml
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
validation_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
fixture_commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
A0_controller_head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
branch_map:
  controller: v2a-a1-001-controller
  Alpha: v2a-a1-001-alpha
  Beta: v2a-a1-001-beta
  Alpha_then_Beta: v2a-a1-001-order-alpha-beta
  Beta_then_Alpha: v2a-a1-001-order-beta-alpha
controller_output_file_count: 10
validation_PR_allowed: false
retry_allowed: false
cleanup_during_run_allowed: false
```

Unchanged inherited content includes:

- both workers' exact task IDs and branch bases;
- complete read/version sets;
- exact two-path write sets;
- empty generated/shared/global/authority intersections;
- expected source/test blobs;
- expected Alpha-only, Beta-only and combined Git trees;
- controller order-construction procedure;
- static semantic oracle and evidence ceiling;
- protected-ref checks;
- no-hidden-continuation rule;
- retention through fresh-Pro adjudication and Owner disposition.

## 4. Defect classification

```yaml
defect_class: validation_protocol_and_package_profile_defect
pre_execution_blocker: true
underlying_A1_fixture_corruption: false
underlying_effect_contract_defect: false
underlying_order_oracle_defect: false
A1_runtime_failure: false
A1_rerun_required: false
```

The defect was found before any A1 branch existed. No A1 evidence needs to be deleted, repaired or rerun.

## 5. Evidence separation

The repaired protocol treats these as different evidence objects:

```yaml
Owner_authorized_visible_label:
  meaning: permission_constraint_for_one_role
  evidence: direct_user_instruction
operator_selected_visible_label:
  meaning: actual_visible_selection_for_one_specific_execution_conversation
  evidence: operator_observed_or_operator_reported_at_that_conversation_launch
backend_identity:
  status: unknown_or_not_attestable
```

A recommendation, planned selection or model self-report is not an operator-selected receipt.

## 6. No implicit execution

Package 002 publication, merge, post-merge verification or readiness review does not authorize:

- controller G2A;
- creation of the three initial A1 branches;
- worker startup;
- order-branch construction;
- A2–A7, V2-B or V2-C;
- any non-Mnemosyne write during package preparation.
