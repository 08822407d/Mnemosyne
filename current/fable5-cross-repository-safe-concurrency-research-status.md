# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
last_updated_by_task: MNEMOSYNE-224
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: V2A_A0_SENTINEL_PROTOCOL_REPAIR_PACKAGE_002_PREPARED_EXECUTION_NOT_AUTHORIZED
Fable_report_received: true
return_identity_verified: true
fresh_Pro_adjudication_completed: true
Owner_F2_disposition:
  selected: A
  decision_ref: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
modified_provisional_amendment_accepted: true
V2_staged_validation_design_prepared: true
Owner_stage_selection: A_prepare_minimal_V2_A_sentinel
V2_A_A0_plan_prepared: true
V2_A_A0_execution_authorized: false
V2_A_A1_to_A7_execution_authorized: false
V2_B_execution_authorized: false
V2_C_execution_authorized: false
controller_branch_created: false
validation_repository_written_by_MNEMOSYNE_224: false
connector_permission_change_authorized: false
external_execution_or_quota_authorized: false
automatic_retry: false
real_target_adoption_authorized: false
```

## 1. Preserved research and adjudication

```text
raw/research-reports/cycles/2026Q3-cross-repository-safe-concurrency/
notes/research-adjudications/MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md
notes/cross-repository-safe-concurrency-and-ordered-work-amendment-candidate-v0.1.md
notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
```

Controlling F2 disposition remains:

```yaml
return_identity: PASS_EXACT
run_validity: ACCEPT_WITH_LIMITATIONS
input_verification: PASS_WITH_BOUNDED_IDENTITY_DEFECT
task_contract_compliance: PASS_WITH_LIMITATIONS
citation_portability: FAIL
architecture_direction: ACCEPT_AS_CORROBORATED_MODIFIED_PROVISIONAL_DIRECTION
technical_details: ACCEPT_WITH_MATERIAL_CORRECTIONS
implementation_readiness: REJECT
```

## 2. Staged V2 design

```text
notes/validation-designs/cross-repository-safe-concurrency-v2-staged-validation-v0.1.md
notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/
```

- V2-A: public/synthetic core concurrency and stale-state design;
- V2-B: public/synthetic ordered multi-repository failure/recovery design;
- V2-C: connector/app permission/privacy design only.

No V2 stage is currently authorized to execute.

## 3. A0 sentinel topology

```yaml
sentinel:
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
  selected_stage: V2_A
  selected_cells: [A0]
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  controller_base: master@e8e3296922185b4b70997c2351d6f39423f2cd4f
  read_only_fixture: tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
  future_controller_branch: v2a-sentinel-001-controller
  worker_branches: []
  PR_creation: prohibited
  output_file_count: 7
  recommended_visible_selection_if_available: gpt-5.6 sol extra high
  post_run_review: fresh_ChatGPT_Pro
```

A0 tests only package/source identity, material class, product/tool surface, branch/path scope and bounded no-write evidence. It does not test A1–A7 concurrency semantics.

## 4. Protocol defect discovered after PR #291

Package 001/candidate 001 hard-pinned the pre-publication Mnemosyne `master` as an execution precondition:

```text
2308c1e55fbbfb753ec527691809dd8f91f6f462
```

PR #291 successfully published that package and therefore moved `master` to:

```text
9157c476e8bf785f6440af4aaefbc44532d47c14
```

This created a publication-induced self-invalidation loop: every new publication of an exact protected master would itself change the master again.

```yaml
protocol_defect_id: V2A-SENTINEL-PROTOCOL-DEFECT-001
classification: package_profile_defect
A0_executed_before_detection: false
validation_repository_write_before_detection: false
candidate_or_F2_architecture_defect: not_established
```

## 5. Repair package 002

Controlling future A0 package candidate after MNEMOSYNE-224 merge:

```text
notes/validation-run-decisions/
MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-002.md

notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/
```

Repair semantics:

```yaml
immutable_source_integrity:
  mechanism: exact_load_bearing_path_blob_pairs
  candidate_blob: bound_by_future_G2A
  source_manifest_blob: bound_by_future_G2A

execution_window_no_write_baseline:
  Mnemosyne_master: supplied_by_future_G2A_after_package_merge
  Meta_Agent_master: supplied_by_future_G2A_after_package_merge
  may_controller_refresh_expected_value: false
  must_match_before_first_validation_write: true
  must_match_after_A0: true

hard_pinned_run_dependencies:
  validation_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
  fixture_commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
  historical_V1_ref_inventory: exact_manifest_002
```

Package 001 and MNEMOSYNE-223 records remain historical evidence; package 002 supersedes only the defective pre-run binding scope.

## 6. Current gate

```yaml
current_gate: MERGE_MNEMOSYNE_224_REPAIR_THEN_FRESH_PRO_FREEZE_G2A_DYNAMIC_FIELDS
G1A_repaired_package_prepared: true
G2A_execution_authorized: false
required_future_G2A_dynamic_fields:
  - decision_candidate_002_blob
  - source_manifest_002_blob
  - protected_Mnemosyne_master
  - protected_Meta_Agent_master
  - authorized_visible_model_label
```

After these values are frozen by Owner authorization, no additional Mnemosyne publication occurs before A0. The Owner authorization text is preserved verbatim in validation output.

## 7. Explicit boundaries

No current artifact authorizes:

- creation of `v2a-sentinel-001-controller`;
- any validation-repository write;
- A0 or A1–A7 execution;
- V2-B/V2-C;
- connector/app/account permission changes;
- web, Deep Research, Fable or external quota;
- private/real-target material;
- modification of Target Lifecycle candidate v0.2, execution source, Meta-Agent or real target;
- lock/lease/orchestrator service;
- automatic retry/compensation/reset/force-push;
- target adoption or production-readiness claims.
