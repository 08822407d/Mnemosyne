# V2-A A0 Sentinel — Mechanical Checks and Result Template v2

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-CHECKS-002
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-002
status: frozen_template_not_executed
```

## 1. Result vocabulary

Every mandatory check is one of:

```text
PASS
FAIL
BLOCKED
NOT_SELECTED
NOT_APPLICABLE
DISPUTED_REQUIRES_PRO_ADJUDICATION
```

No missing check is implicit PASS.

## 2. A0 checks S0–S19

### S0 — Owner authorization identity

Verify Owner G2A authorization selects only A0 and names exact candidate-002 and source-manifest-002 blobs.

### S1 — product/model surface

Verify visible product/model/reasoning labels equal the authorized values; record them verbatim. Backend remains unknown/not attestable.

### S2 — package publication/source-binding separation

Verify the controller did not require Mnemosyne `master` to equal a historical package-publication parent. Source integrity is proven by candidate/manifest and exact load-bearing blob checks.

### S3 — load-bearing Mnemosyne source blobs

Verify every required path/blob pair in source manifest 002.

### S4 — execution-window protected external refs before

Verify `Mnemosyne/master` and `Meta-Agent/master` equal the exact SHAs in the Owner G2A authorization immediately before any validation-repository write.

### S5 — validation repository identity

Verify public repository, default branch and `master@e8e3296922185b4b70997c2351d6f39423f2cd4f`.

### S6 — read-only fixture identity

Verify `tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6` and tree `f1e221ce8aef404579b96adb3ab01319016889db`.

### S7 — historical V1 ref inventory

Re-enumerate all `tlr-v1-*` refs and compare exact names/SHAs with source manifest 002.

### S8 — controller-lineage absence

Verify `v2a-sentinel-001-controller` and equivalent A0 PR/run lineage are absent before creation.

### S9 — controller branch parent

After authorized creation, verify controller branch starts from pinned validation master and no force/move occurred.

### S10 — exact output path set

Compare controller branch against base. Exactly seven allowed files may differ; no other path may differ.

### S11 — output completeness and identities

Verify seven outputs exist and record each blob and creation/update commit.

### S12 — protected validation refs unchanged

After A0, verify validation `master`, fixture and every historical V1 ref are unchanged.

### S13 — protected external refs unchanged

After A0, verify Mnemosyne and Meta-Agent master refs remain equal to the execution-window baselines from Owner authorization.

### S14 — no worker branch or PR

Verify no worker/fixture/scenario/alternative-controller branch or PR was created.

### S15 — material safety

Record exact inspected fixture paths and any mechanical scan. Verify no known private/real material was used without claiming exhaustive absence beyond evidence.

### S16 — no unselected tools/quota

Verify no web search, Deep Research, Fable, other app/connector, private file, or separate paid/external quota was used.

### S17 — no hidden continuation

Verify A1–A7, V2-B and V2-C were not started; no package repair, architecture modification, automatic retry or compensation occurred.

### S18 — bounded claim discipline

Verify source, no-write, model, material and evidence claims name exact scope/limitations; physical connector capability is not represented as task authority.

### S19 — final stop state

Verify controller stopped after final bundle, retained branch for fresh Pro, and created no PR/merge.

## 3. `02-package-and-material-receipt.yaml`

```yaml
package_and_material_receipt:
  run_id:
  decision_candidate:
    expected_blob:
    observed_blob:
    result:
  source_manifest:
    expected_blob:
    observed_blob:
    result:
  source_blob_checks:
    - path:
      expected_blob:
      observed_blob:
      role:
      result:
  package_files:
    - path:
      expected_blob:
      observed_blob:
      result:
  fixture:
    repository:
    ref:
    expected_commit:
    observed_commit:
    expected_tree:
    observed_tree:
  material_inspection:
    inspected_paths: []
    method:
    mechanical_scan:
      executed:
      scope:
      artifact_ref:
      result:
    limitations: []
  receipt_result: PASS | BLOCKED
```

## 4. `03-repository-and-ref-baseline.yaml`

```yaml
repository_and_ref_baseline:
  run_id:
  time_window:
    before_started_at:
    after_completed_at:
  Owner_authorized_execution_window_refs:
    Mnemosyne_master:
    Meta_Agent_master:
  observed_external_refs:
    Mnemosyne_before:
    Mnemosyne_after:
    Meta_Agent_before:
    Meta_Agent_after:
  validation_refs:
    - ref:
      expected_before:
      observed_before:
      observed_after:
      result:
  controller_branch:
    expected_absent_before: true
    observed_absent_before:
    creation_parent:
    observed_head_after_creation:
    final_head:
  open_PRs_before: []
  open_PRs_after: []
  claim_scope:
    named_repositories: []
    named_refs: []
    accessible_action_surfaces: []
    limitations: []
  baseline_result: PASS | FAIL | BLOCKED
```

## 5. `04-mechanical-checks.yaml`

```yaml
mechanical_checks:
  run_id:
  S0_Owner_authorization_identity:
  S1_product_model_surface:
  S2_publication_source_binding_separation:
  S3_load_bearing_source_blobs:
  S4_execution_window_external_refs_before:
  S5_validation_repository_identity:
  S6_fixture_identity:
  S7_V1_ref_inventory:
  S8_controller_lineage_absence:
  S9_controller_branch_parent:
  S10_exact_output_path_set:
  S11_output_completeness_and_identities:
  S12_validation_refs_unchanged:
  S13_external_refs_unchanged:
  S14_no_worker_branch_or_PR:
  S15_material_safety:
  S16_no_unselected_tools_or_quota:
  S17_no_hidden_continuation:
  S18_bounded_claim_discipline:
  S19_final_stop_state:
  all_mandatory_checks_accounted_for:
  disputed_checks: []
  overall_mechanical_disposition:
```

## 6. Incident ledger

`incidents/incident-ledger.yaml` exists even when empty:

```yaml
incident_ledger:
  run_id:
  incidents: []
  confirmed_none:
  known_detection_limitations: []
```

If an incident occurs, preserve exact state and classify at least one of:

```text
source_identity_mismatch
execution_window_ref_mismatch
model_or_surface_mismatch
branch_or_PR_lineage_conflict
material_classification_blocker
tool_or_product_limitation
prohibited_write_or_side_effect
package_or_profile_defect
insufficient_evidence
unresolved
```

No repair/retry is allowed.

## 7. Final bundle

```yaml
sentinel_result_bundle:
  validation_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-STAGED-VALIDATION-001
  package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-002
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
  selected_stage: V2_A
  selected_cells: [A0]
  sentinel_only: true
  Owner_authorization_ref:
  decision_candidate_blob:
  source_manifest_blob:
  execution_window_protected_refs: {}
  controller_branch:
  controller_final_head:
  source_identities: []
  output_files:
    - path:
      blob:
      creation_or_update_commit:
  mechanical_checks_ref:
  incident_ledger_ref:
  evidence_strength:
    declared:
    artifact_present:
    statically_inspected:
    mechanically_verified:
    runtime_executed:
    runtime_passed:
    independently_reproduced:
    platform_signed_or_independently_attested:
    known_limitations: []
  unresolved_gaps: []
  provisional_executor_disposition:
    value: SENTINEL_PASS_SELECTED_SCOPE | SENTINEL_PASS_WITH_BOUNDED_DEFECTS_FOR_PRO_REVIEW | SENTINEL_FAIL | SENTINEL_BLOCKED
    reason:
  fresh_Pro_adjudication: {status: pending, value: null}
  Owner_next_stage_decision: {status: pending, value: null}
  A1_to_A7_executed: false
  V2_B_or_V2_C_executed: false
  production_readiness_proven: false
  real_target_adoption_authorized: false
  prohibited_repository_write_performed: false
  automatic_retry_performed: false
  PR_created: false
```

## 8. Evidence ceiling

A0 may reach artifact-present, static inspection, mechanical verification and runtime execution/pass for actual GitHub operations. It does not automatically prove independent reproduction, provider-signed provenance, connector denial, semantic concurrency correctness or production readiness.

## 9. Fresh Pro review

Fresh Pro verifies candidate/manifest identity, branch parent/tree, seven-file diff, protected refs, provenance claims, material scope and absence of workers/PRs. Only fresh Pro and Owner may decide whether full V2-A preparation is justified.
