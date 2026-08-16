# V2-A A0 Sentinel — Mechanical Checks and Result Template

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-CHECKS-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-001
status: frozen_template_not_executed
```

## 1. Result vocabulary

Every check uses exactly one value:

```text
PASS
FAIL
BLOCKED
NOT_SELECTED
NOT_APPLICABLE
DISPUTED_REQUIRES_PRO_ADJUDICATION
```

No blank or omitted mandatory check is treated as PASS.

## 2. A0 checks S0–S18

### S0 — Owner authorization identity

Verify the future G2A authorization references the exact merged run-decision and package identities and selects only A0.

### S1 — product/model surface

Verify the operator-visible product, model and reasoning labels match the authorized values. Record them verbatim. Backend remains unknown/not attestable.

### S2 — Mnemosyne source commit

Verify `08822407d/Mnemosyne master` equals the pinned source commit.

### S3 — Mnemosyne source blobs

Verify every required path/blob pair in the source manifest.

### S4 — validation repository identity

Verify repository, public visibility, default branch and exact master commit.

### S5 — read-only fixture identity

Verify fixture ref, commit, tree and declared public/synthetic material class.

### S6 — V1 ref inventory

Re-enumerate all `tlr-v1-*` refs and compare names and SHAs to the frozen inventory.

### S7 — controller-lineage absence

Verify `v2a-sentinel-001-controller` and any equivalent open PR/run lineage are absent before branch creation.

### S8 — controller branch parent

After authorized branch creation, verify the branch's first parent/base is the pinned validation-repository master and no force update occurred.

### S9 — exact output path set

Compare actual controller-branch changes to the seven-file allowlist. No other path may differ from the controller base.

### S10 — output completeness and identities

Verify all seven outputs exist and record every output blob SHA and creation/update commit SHA.

### S11 — protected validation refs unchanged

Verify validation-repository master, fixture and every existing V1 ref are unchanged after A0.

### S12 — Mnemosyne and Meta-Agent refs unchanged

Verify the named protected master refs remain unchanged over the run window.

### S13 — no worker branch or PR

Verify no worker, fixture, scenario or alternative controller branch/PR was created.

### S14 — material safety

Record exact inspected fixture paths and any mechanical scan scope. Verify no known private/real material was used. Do not overclaim exhaustive absence.

### S15 — no unselected tools/quota

Verify no web search, Deep Research, Fable, other app/connector, private file or separately paid/external quota was used.

### S16 — no hidden continuation

Verify A1–A7, V2-B and V2-C were not started; package semantics were not edited; no retry, repair or architecture modification occurred.

### S17 — output claims bounded

Verify every no-write, model, material and evidence claim names its scope and limitations.

### S18 — final stop state

Verify the controller stopped after the result bundle and retained the branch for fresh Pro review without PR or merge.

## 3. File templates

### 3.1 `02-package-and-material-receipt.yaml`

```yaml
package_and_material_receipt:
  run_id:
  Mnemosyne_source_commit:
  source_blob_checks:
    - path:
      expected_blob:
      observed_blob:
      result:
  sentinel_package_files:
    - path:
      expected_blob:
      observed_blob:
      result:
  validation_fixture:
    repository:
    ref:
    expected_commit:
    observed_commit:
    expected_tree:
    observed_tree:
  material_inspection:
    inspected_paths: []
    inspection_method:
    mechanical_secret_or_material_scan:
      executed:
      exact_scope:
      artifact_ref:
      result:
    public_synthetic_evidence: []
    known_limitations: []
  selected_cells:
    - A0
  receipt_result: PASS | BLOCKED
```

### 3.2 `03-repository-and-ref-baseline.yaml`

```yaml
repository_and_ref_baseline:
  run_id:
  time_window:
    before_started_at:
    after_completed_at:
  repositories:
    - repository:
      role:
      refs:
        - ref:
          expected_before:
          observed_before:
          observed_after:
          result:
  controller_branch:
    expected_absent_before:
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

### 3.3 `04-mechanical-checks.yaml`

```yaml
mechanical_checks:
  run_id:
  S0_Owner_authorization_identity:
  S1_product_model_surface:
  S2_Mnemosyne_source_commit:
  S3_Mnemosyne_source_blobs:
  S4_validation_repository_identity:
  S5_read_only_fixture_identity:
  S6_V1_ref_inventory:
  S7_controller_lineage_absence:
  S8_controller_branch_parent:
  S9_exact_output_path_set:
  S10_output_completeness_and_identities:
  S11_protected_validation_refs_unchanged:
  S12_Mnemosyne_Meta_Agent_refs_unchanged:
  S13_no_worker_branch_or_PR:
  S14_material_safety:
  S15_no_unselected_tools_or_quota:
  S16_no_hidden_continuation:
  S17_output_claims_bounded:
  S18_final_stop_state:
  all_mandatory_checks_accounted_for:
  disputed_checks: []
  overall_mechanical_disposition:
```

### 3.4 `incidents/incident-ledger.yaml`

The file exists even when no incident occurs.

```yaml
incident_ledger:
  run_id:
  incidents: []
  confirmed_none:
  known_detection_limitations: []
```

If an incident occurs:

```yaml
incident:
  incident_id:
  detected_at:
  phase:
  category:
    - source_identity_mismatch
    - model_or_surface_mismatch
    - branch_or_PR_lineage_conflict
    - material_classification_blocker
    - tool_or_product_limitation
    - prohibited_write_or_side_effect
    - package_or_profile_defect
    - insufficient_evidence
    - unresolved
  exact_state_identities: []
  automatic_actions_stopped:
  evidence_preserved:
  repair_attempted: false
  retry_attempted: false
  Pro_gate_required: true
```

### 3.5 `05-sentinel-result-bundle.yaml`

```yaml
sentinel_result_bundle:
  validation_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-STAGED-VALIDATION-001
  package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-001
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
  selected_stage: V2_A
  selected_cells:
    - A0
  sentinel_only: true
  controller_branch:
  controller_final_head:
  source_identities: []
  product_surface_receipts: []
  output_files:
    - path:
      blob:
      creation_or_update_commit:
  mechanical_checks_ref:
  incident_ledger_ref:
  protected_repository_no_write_results: []
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
  fresh_Pro_adjudication:
    status: pending
    value: null
  Owner_next_stage_decision:
    status: pending
    value: null
  validation_execution_only: true
  A1_to_A7_executed: false
  V2_B_or_V2_C_executed: false
  production_readiness_proven: false
  real_target_adoption_authorized: false
  repository_write_performed: true
  prohibited_repository_write_performed: false
  automatic_retry_performed: false
  PR_created: false
```

## 4. Evidence-strength ceiling

A0 may normally reach:

- artifact present;
- statically inspected;
- mechanically verified;
- runtime executed/passed for the actual GitHub branch/file/ref actions.

It does not automatically reach:

- independently reproduced;
- platform-signed provenance;
- physical connector denial;
- semantic concurrency correctness;
- production readiness.

The result must set unsupported evidence fields to `false` and explain limitations.

## 5. Pro adjudication requirements

Fresh Pro should verify:

- exact run package identity;
- branch parent and output tree;
- seven-file path scope;
- protected-ref before/after comparisons;
- model/provenance claim discipline;
- material-safety evidence scope;
- absence of worker branches and PRs;
- whether any failure belongs to executor, package, tool surface or authorization.

Only fresh Pro and the Owner may decide whether to prepare a full V2-A fixture/run package.
