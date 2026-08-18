# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
last_updated_by_task: MNEMOSYNE-229
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: A0_OWNER_ACCEPTED_PASS_WITH_BOUNDED_EVIDENCE_DEFECTS_A1_SEPARATELY_GATED
Fable_report_received: true
fresh_Pro_F2_adjudication_completed: true
Owner_F2_option_A_accepted: true
V2_staged_design_prepared: true
V2_A_A0_plan_prepared: true
package_003_merged: true
package_003_merge_PR: 294
package_003_merge_commit: 5ca091e1c52bb1e7483b2d54e9259d3ec85b7b93
package_003_post_merge_tree_identity_verified: true
G2A_execution_authorized: true
G2A_dynamic_fields_bound: true
execution_window_frozen: true
V2_A_A0_execution_authorized: true
V2_A_A0_executed: true
controller_branch_created: true
validation_repository_written: true
A0_final_head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
fresh_Pro_A0_adjudication_completed: true
Owner_A0_adjudication_accepted: true
A0_disposition: PASS_WITH_BOUNDED_EVIDENCE_DEFECTS
A0_rerun_required: false
package_003_repair_required: false
historical_A0_outputs_rewritten: false
controller_branch_modified_or_deleted_after_adjudication: false
A0_durable_evidence_correction_recorded: true
A1_to_A7_execution_authorized: false
V2_B_execution_authorized: false
V2_C_execution_authorized: false
external_quota_authorized: false
automatic_retry: false
real_target_adoption_authorized: false
```

## 1. Preserved Fable research and accepted F2 direction

The exact Fable report, input snapshot, fresh Pro F2 adjudication and Owner F2 Option A remain controlling historical evidence:

```text
raw/research-reports/cycles/2026Q3-cross-repository-safe-concurrency/
notes/research-adjudications/MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md
notes/cross-repository-safe-concurrency-and-ordered-work-amendment-candidate-v0.1.md
notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
```

The accepted F2 direction remains provisional and does not prove production readiness or authorize real-target adoption.

## 2. Package 003 and G2A

Package 003 remains the controlling A0 execution package:

```yaml
run_decision_candidate_003_blob: 9e46dd849c3c8604f5e2fa7fce9c02c5504ff202
package_003_source_manifest_blob: 967c7a9ce38883ab897bf856fa4004b987e7d911
```

The Owner G2A bound:

```yaml
protected_Mnemosyne_master: 9b5a3a16d83f6cabc341445d70d350e3391d1daf
protected_Meta_Agent_master: 1fdbd7af9437f72f7c8106714ad1e64908983fb7
authorized_visible_model_label: gpt-5.6 sol extra high
operator_selected_visible_model_label: gpt-5.6 sol extra high
```

Visible-label equality is accepted only at the operator-reported evidence level. Hidden backend identity remains unknown/not attestable.

## 3. A0 execution identity

```yaml
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
stage: V2_A
executed_cells: [A0]
A1_to_A7_executed: false
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
controller_branch: v2a-sentinel-001-controller
creation_base: e8e3296922185b4b70997c2351d6f39423f2cd4f
final_head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
commit_count_from_base: 10
final_diff_path_count: 7
unexpected_paths: []
eighth_output_created: false
controller_PRs: []
worker_or_fixture_branches_created: []
```

Final output blobs:

```yaml
00-controller-receive.yaml: 07c84ba87bf0b995ab52c9bdb39f3eec0f914910
01-product-and-permission-receipt.yaml: 0d31d6895b01a749ab715aa6dcf8e69ba2595037
02-package-and-material-receipt.yaml: ad227d43d2eb0d74bf5938b50d220141ff6fdfdf
03-repository-and-ref-baseline.yaml: 7b847bf19e767b432b081be67416b4092f142816
04-mechanical-checks.yaml: 2f8aee53805ea1e40138aa5ec9c9cf1854911ebf
incidents/incident-ledger.yaml: d5df2e14288e606e89985f8ee16b8de73de5889f
05-sentinel-result-bundle.yaml: aa655b4fb6a34684d6951a9321e6e3eee66d3123
```

## 4. Fresh Pro A0 adjudication and Owner acceptance

Durable records:

```text
notes/validation-adjudications/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-ADJUDICATION-001.md
notes/evidence-corrections/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-PATH-IDENTITY-CORRECTION-001.md
notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-OWNER-DECISION-001.md
```

Accepted disposition:

```yaml
overall_A0_adjudication: PASS_WITH_BOUNDED_EVIDENCE_DEFECTS
repository_safety_and_write_boundary: PASS
frozen_ref_and_inventory_integrity: PASS
package_and_source_content_integrity: PASS
evidence_record_integrity: PASS_WITH_ONE_BOUNDED_PATH_IDENTITY_DEFECT
A0_rerun_required: false
package_repair_required: false
```

This is not a clean unqualified pass and does not automatically unlock later cells.

## 5. Bounded defects

### A0-TOOL-001

```yaml
classification: NON_BLOCKING_BOUNDED_TOOL_PRODUCT_LIMITATION
failed_operation: GitHub.fetch_batch_branches_shortcut
repository_side_effect: none
failed_call_repeated: false
expected_values_refreshed: false
model_substituted: false
recovery_method:
  - supported_GitHub.search_branches
  - individual_supported_read_only_branch_reads
recovery_classification: ALLOWED_EVIDENCE_RECOVERY_NOT_PROHIBITED_RETRY
A0_rerun_required: false
```

### Package path identity

Historical output `02-package-and-material-receipt.yaml` falsely names:

```text
notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/04-integrity-checklist.md
```

The controlling canonical identity is:

```yaml
path: notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/04-package-integrity-and-non-execution-checklist.md
blob: 6741824758f6037443eb272da16c0847e6ea4d8d
```

The historical short path does not exist. The canonical path exists at the frozen source commit with the exact blob. The defect is an additive evidence-record correction, not package corruption.

```yaml
historical_output_02_rewritten: false
controller_branch_modified: false
package_003_modified: false
A0_rerun_required: false
later_V2_A_permanently_blocked: false
```

## 6. Evidence limits

Mechanically verified evidence includes source/package blobs, controller lineage, exact seven-path diff, final result blobs, validation master, fixture and frozen 16-ref inventory.

Operator/executor attestation remains the ceiling for visible model selection and non-GitHub product-surface usage. The no-write result is bounded to named refs and point-in-time observations; it is not a platform-global lock. No exhaustive secret scan of the public synthetic fixture is claimed.

## 7. Current gate

```yaml
current_gate: OWNER_DECIDES_WHETHER_TO_PREPARE_A1_EXACT_RUN_PLAN
A0_automatically_unlocks_A1: false
reuse_A0_G2A_for_A1: false
A1_execution_authorized: false
required_before_any_A1_execution:
  - separate_Owner_selection
  - exact_A1_run_design_and_package
  - then_current_source_and_ref_freeze
  - separate_model_product_surface_binding
  - exact_branch_PR_and_output_contract
  - explicit_execution_authorization
```

The controller branch and seven historical A0 outputs remain preserved unchanged. Any cleanup or evidence migration requires a separate Owner decision.

## 8. Explicit boundaries

No current record authorizes:

- modification or deletion of `v2a-sentinel-001-controller`;
- rewriting the seven A0 outputs;
- A0 rerun;
- package-003 repair;
- A1–A7 execution;
- V2-B or V2-C;
- Meta-Agent or real-target write/adoption;
- connector/account changes;
- Web, Deep Research, Fable or external quota;
- automatic retry, repair, compensation, reset or force-push.
