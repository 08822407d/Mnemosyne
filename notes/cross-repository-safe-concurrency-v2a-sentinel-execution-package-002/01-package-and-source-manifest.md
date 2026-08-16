# V2-A A0 Package and Source Manifest — v2

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-SOURCE-MANIFEST-002
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-002
status: frozen_source_and_package_blob_manifest_without_recursive_self_hash
protocol_defect_repaired: V2A-SENTINEL-PROTOCOL-DEFECT-001
```

## 1. Source-binding rule

A0 source integrity is established by exact load-bearing **path/blob** identities, not by requiring current Mnemosyne `master` to equal a pre-publication commit.

The historical release that exposed the package-001 self-invalidation defect is:

```yaml
package_001_publication:
  PR: 291
  merge_commit: 9157c476e8bf785f6440af4aaefbc44532d47c14
  prior_pinned_master_inside_package_001: 2308c1e55fbbfb753ec527691809dd8f91f6f462
  defect: successful_publication_moved_master_and_invalidated_package_001_preflight
```

Package 002 instead requires exact source blobs plus Owner-supplied execution-window protected refs after package 002 is merged.

## 2. Load-bearing Mnemosyne source blobs

```yaml
source_repository: 08822407d/Mnemosyne
source_release_observation:
  master_at_repair_start: 9157c476e8bf785f6440af4aaefbc44532d47c14
  controlling_execution_window_master: supplied_by_future_G2A_not_this_field
source_files:
  - path: current/human-approved-spec.md
    blob: 01f64a8223677829320c66dd46d3f172cc9155cc
    role: execution_source
  - path: current/github-single-active-pr-lineage-guard.md
    blob: 042efe9e353097a17eea38d0bcb0ff1da7c4385e
    role: branch_PR_guard
  - path: current/run-context-and-pr-provenance-guard.md
    blob: 0e588b3f6789d0d941221d33c3eaba1561f6e2a3
    role: provenance_guard
  - path: current/user-operation-next-step-capability-and-intent-guard.md
    blob: 265d61aad34c9e55006647c9e12d77c4214310ea
    role: user_operation_and_capability_guard
  - path: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
    blob: 4d59e6edefb5f166261dca353f4552e9346d0f8a
    role: Owner_Option_A_decision
  - path: notes/research-adjudications/MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md
    blob: 27d607257bb1700d9ff9c73f0048a6a7b7847746
    role: fresh_Pro_F2_adjudication
  - path: notes/cross-repository-safe-concurrency-and-ordered-work-amendment-candidate-v0.1.md
    blob: 46fd66dc23d6615ea167e0950de970cc316c056b
    role: Owner_accepted_provisional_amendment
  - path: notes/validation-designs/cross-repository-safe-concurrency-v2-staged-validation-v0.1.md
    blob: f66678c0ebdc28a9407553b918838256e6e633a4
    role: staged_V2_design
```

Any load-bearing blob mismatch requires fresh Pro review before A0. Current master may differ because of package/result publication while these blobs remain unchanged.

## 3. Parent V2 package blobs

```yaml
parent_V2_package:
  notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/README.md: 3429f981f9b7dc0900dff4d356f9a001c280f1e6
  notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/00-owner-gates-and-stage-boundaries.md: fd56c6710ba4aa76e2e962693e3f97bb35ffb175
  notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/01-synthetic-fixture-and-scenario-contracts.md: 19235ec7110f6ad4f529a09400f00a7b00240934
  notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/02-v2-a-core-concurrency-taskbook.md: c36ac4604dea9ebe1bef00d30bea684db775f687
  notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/03-v2-b-ordered-cross-repository-taskbook.md: 836afd993d19d444a22d75704977c0de8f3383a4
  notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/04-v2-c-connector-security-design-only.md: f99c761245c4c3a5d2229d084fb0fb400b9e7360
  notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/05-mechanical-checks-and-evidence-rubric.md: 59082fb32c1e38d48878bc5f4b4f4faa561e44cb
  notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/06-run-manifest-and-result-template.md: 17494c9bf86a8782f5a3a91c6a33dd14aa27e5a8
  notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/07-package-integrity-and-non-execution-checklist.md: c7ee1083a9b84d7d070dfec7a9bd65655750b4a9
```

## 4. Repaired decision and package-002 blobs

```yaml
run_decision_candidate_002:
  path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-002.md
  blob: 78185751607cf4bd1930710bf1e5e84c9235bb33

package_002_files:
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/README.md: 3a4bb50cd8c2d89027690f0bc196eba7bf0bbebe
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/00-controller-receive-and-surface-contract.md: 3ee4276afcabfce3986b44a24ba0b2cdced239ba
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/02-next-tier-controller-task.md: 89382a949fbcfa0542679553b5a245137512e1ce
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/03-mechanical-checks-and-result-template.md: b615be7a3c05b3c5dd5d40e0e5cadc7a581cb0c6
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/04-startup-message.md: 5bb7053653d23a47ef113db36ef85d8bbc83884d
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/05-package-integrity-and-non-execution-checklist.md: c573d4c7b2e2558b482e0372b2d5310d79168814
```

This manifest does not recursively list its own blob. The future Owner G2A authorization names this manifest's exact merged blob separately, and the controller checks it before any write.

## 5. Validation repository hard-pinned identities

```yaml
validation_repository:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  default_branch: master
  default_branch_commit: e8e3296922185b4b70997c2351d6f39423f2cd4f
  future_write_branch: v2a-sentinel-001-controller
  future_write_branch_base: e8e3296922185b4b70997c2351d6f39423f2cd4f
  controller_branch_must_be_absent_before_G2A_execution: true
  fixture:
    ref: tlr-v1-fixture-base
    commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
    tree: f1e221ce8aef404579b96adb3ab01319016889db
    material_class: public_synthetic_only
    write_authorized: false
```

## 6. Historical V1 ref inventory

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

All names and SHAs must match before branch creation and remain unchanged after A0.

## 7. Execution-window protected refs

These are deliberately not frozen here:

```yaml
protected_external_refs:
  Mnemosyne_master: supplied_by_Owner_G2A_after_package_002_merge
  Meta_Agent_master: supplied_by_Owner_G2A_after_package_002_merge
```

Preparation observations only, not run authorization:

```yaml
observed_during_MNEMOSYNE_224_preparation:
  Mnemosyne_master: 9157c476e8bf785f6440af4aaefbc44532d47c14
  Meta_Agent_master: 1fdbd7af9437f72f7c8106714ad1e64908983fb7
```

The Owner G2A message supplies the authoritative run-window values after package merge. A mismatch at A0 launch blocks; controller cannot refresh them.

## 8. Exact future output manifest

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

## 9. Invalidation rules

Before G2A/A0, fresh Pro is required if:

- any load-bearing source or parent-package blob changes;
- any package-002 file/candidate blob differs from this manifest;
- validation master/fixture/V1 inventory changes;
- repository visibility or required GitHub physical capability changes;
- run scope, branch, output paths, retention, retry or quota boundary changes.

A move of Mnemosyne/Meta-Agent master caused only by normal publication **before** Owner G2A is not itself package invalidation; those current refs are freshly frozen by G2A. After G2A they may not move before or during A0.
