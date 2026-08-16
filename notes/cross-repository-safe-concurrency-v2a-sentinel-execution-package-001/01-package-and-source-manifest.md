# V2-A A0 Package and Source Manifest

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-SOURCE-MANIFEST-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-001
status: frozen_source_manifest_with_final_non_self_package_blobs
```

## 1. Mnemosyne source receipt

```yaml
source_repository: 08822407d/Mnemosyne
source_branch: master
source_commit: 2308c1e55fbbfb753ec527691809dd8f91f6f462
source_files:
  - path: current/human-approved-spec.md
    blob: 01f64a8223677829320c66dd46d3f172cc9155cc
    role: execution_source
  - path: current/github-single-active-pr-lineage-guard.md
    blob: 042efe9e353097a17eea38d0bcb0ff1da7c4385e
    role: active_branch_PR_guard
  - path: current/run-context-and-pr-provenance-guard.md
    blob: 0e588b3f6789d0d941221d33c3eaba1561f6e2a3
    role: active_run_provenance_guard
  - path: current/user-operation-next-step-capability-and-intent-guard.md
    blob: 265d61aad34c9e55006647c9e12d77c4214310ea
    role: active_user_operation_and_capability_guard
  - path: current/fable5-cross-repository-safe-concurrency-research-status.md
    blob: 4c83d65e054f1be9022d6c1cf08da014a567b5fe
    role: current_F2_status_before_MNEMOSYNE_223
  - path: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
    blob: 4d59e6edefb5f166261dca353f4552e9346d0f8a
    role: Owner_Option_A_authority
  - path: notes/research-adjudications/MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md
    blob: 27d607257bb1700d9ff9c73f0048a6a7b7847746
    role: fresh_Pro_F2_adjudication
  - path: notes/cross-repository-safe-concurrency-and-ordered-work-amendment-candidate-v0.1.md
    blob: 46fd66dc23d6615ea167e0950de970cc316c056b
    role: Owner_accepted_modified_provisional_amendment
  - path: notes/validation-designs/cross-repository-safe-concurrency-v2-staged-validation-v0.1.md
    blob: f66678c0ebdc28a9407553b918838256e6e633a4
    role: V2_staged_validation_design
  - path: notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/README.md
    blob: 3429f981f9b7dc0900dff4d356f9a001c280f1e6
    role: V2_package_entrypoint
  - path: notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/00-owner-gates-and-stage-boundaries.md
    blob: fd56c6710ba4aa76e2e962693e3f97bb35ffb175
    role: Owner_gate_contract
  - path: notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/01-synthetic-fixture-and-scenario-contracts.md
    blob: 19235ec7110f6ad4f529a09400f00a7b00240934
    role: fixture_and_A0_contract
  - path: notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/02-v2-a-core-concurrency-taskbook.md
    blob: c36ac4604dea9ebe1bef00d30bea684db775f687
    role: V2_A_taskbook
  - path: notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/03-v2-b-ordered-cross-repository-taskbook.md
    blob: 836afd993d19d444a22d75704977c0de8f3383a4
    role: unselected_stage_boundary_reference
  - path: notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/04-v2-c-connector-security-design-only.md
    blob: f99c761245c4c3a5d2229d084fb0fb400b9e7360
    role: unselected_design_only_stage_boundary_reference
  - path: notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/05-mechanical-checks-and-evidence-rubric.md
    blob: 59082fb32c1e38d48878bc5f4b4f4faa561e44cb
    role: mechanical_and_evidence_contract
  - path: notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/06-run-manifest-and-result-template.md
    blob: 17494c9bf86a8782f5a3a91c6a33dd14aa27e5a8
    role: result_template_source
  - path: notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/07-package-integrity-and-non-execution-checklist.md
    blob: c7ee1083a9b84d7d070dfec7a9bd65655750b4a9
    role: design_package_integrity_contract
```

The controller must compare every listed blob. Path or semantic-role matching alone is insufficient.

## 2. Validation repository receipt

```yaml
validation_repository:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  default_branch: master
  default_branch_commit: e8e3296922185b4b70997c2351d6f39423f2cd4f
  write_scope_after_future_G2A:
    branch: v2a-sentinel-001-controller
    base_commit: e8e3296922185b4b70997c2351d6f39423f2cd4f
    paths: exact_seven_A0_result_paths
  fixture:
    ref: tlr-v1-fixture-base
    commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
    tree: f1e221ce8aef404579b96adb3ab01319016889db
    material_class: public_synthetic_only
    write_authorized: false
```

## 3. Existing V1 ref inventory to protect

```yaml
protected_V1_refs:
  tlr-v1-controller: e892749fc9e242b24908f89b6a78f1c0f0bed75e
  tlr-v1-fixture-base: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  tlr-v1-s1-destination-block: d20f1239784f88072399a3c874800f6c94c0ad2c
  tlr-v1-s2-bounded-writer: b0923aedf551262f0b24409611824c526252982f
  tlr-v1-s3-alpha: 1a8496893260f35b0b06d32d6b2128a192489ae7
  tlr-v1-s3-beta: 9a77045e77856a25336a664840aeaa984cdb8886
  tlr-v1-s4-alpha-dependent: 4861cc27e8960353f29af9ca5cfa0927430b89ad
  tlr-v1-s4-shared-schema: 2aa6c0a8a7ac39ab1d3e06a64006e83aff20b5aa
  tlr-v1-s4-unknown-global: c77f20f0320313d1ccb2b4d1272dfa0daba8ef77
  tlr-v1-s5-upstream-proposal: 8bfd56e5800566b048702d8b8a89e3bd05f9e6e9
  tlr-v1-s6-beta-requirement: e90fcc6633bae50236aa96f9c499ba6c7379f53f
  tlr-v1-s7-alpha-migration: be627df6a1e633e8c93f25c056b643b603f1aea8
  tlr-v1-s7-commonlib-v2: 9cfae2953fa8d7b2ff4ab2e14abab263891932de
  tlr-v1-s8-insufficient-docs: d9c4c88aa17d6edf73955054833bd2738709aec9
  tlr-v1-s9-imperfect-route: b16a458339497425387d71c843388ef30aa2eb46
  tlr-v1-s11-backup-restore: 47262b6bf8f89c9ac13d7f488595f8adff250299
```

The controller re-enumerates all `tlr-v1-*` refs at launch. Any extra, missing or changed ref blocks A0 unless a new Pro package refresh explains it.

## 4. Protected external refs

```yaml
protected_external_refs:
  08822407d/Mnemosyne:
    master: 2308c1e55fbbfb753ec527691809dd8f91f6f462
  08822407d/Meta-Agent:
    master: 1fdbd7af9437f72f7c8106714ad1e64908983fb7
```

No real target repository is named or accessed. The correct claim is limited to these named refs plus the validation-repository refs above.

## 5. Exact future A0 output manifest

```yaml
output_manifest:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  branch: v2a-sentinel-001-controller
  root: runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/
  files:
    - 00-controller-receive.yaml
    - 01-product-and-permission-receipt.yaml
    - 02-package-and-material-receipt.yaml
    - 03-repository-and-ref-baseline.yaml
    - 04-mechanical-checks.yaml
    - 05-sentinel-result-bundle.yaml
    - incidents/incident-ledger.yaml
  exact_file_count: 7
  other_writes_allowed: false
```

Each output must record its Git blob SHA and creation/update commit SHA in the final result bundle.

## 6. MNEMOSYNE-223 package-file identities

```yaml
MNEMOSYNE_223_package_files:
  notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-001.md: 0a50ad12435354e50a80970a458d7c6af94785e4
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-001/README.md: 21b0b7d3723a5e8654089b7bba31046b806e354c
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-001/00-controller-receive-and-surface-contract.md: 0b8a18b9743726391513887a03da78074c10313d
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-001/01-package-and-source-manifest.md: SELF_IDENTITY_RECORDED_IN_MNEMOSYNE_223_VERIFICATION
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-001/02-next-tier-controller-task.md: fd689c9aeb4d9a22ea9e3e518d4e992f31a3dc73
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-001/03-mechanical-checks-and-result-template.md: 0004903f8e36a3a482303f9371ce3c9428ca67e5
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-001/04-startup-message.md: 9d69ccdccb4ed87e215dccbc816e9b4f80c91d82
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-001/05-package-integrity-and-non-execution-checklist.md: 314441d97dff977bf901c5b6c52ea5a9a3f27aee
```

The manifest does not attempt a recursive self-hash. Its own final blob is recorded in MNEMOSYNE-223 verification/finalization records.

## 7. Invalidation rules

This package is invalidated before G2A if any of the following changes:

- Mnemosyne source commit or any required blob;
- validation repository master, fixture commit/tree or V1 ref inventory;
- Meta-Agent protected master ref;
- repository visibility or write permission surface;
- selected model/product availability;
- exact run scope, output paths or branch name;
- Owner retry, quota, retention or prohibited-action decision.

The controller cannot repair an invalid package. A Pro refresh produces a new package version or decision candidate.
