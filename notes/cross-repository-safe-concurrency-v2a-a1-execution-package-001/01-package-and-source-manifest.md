# V2-A A1 — Package and Source Manifest 001

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-SOURCE-MANIFEST-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-001
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
status: frozen_manifest_without_recursive_self_hash
source_repository: 08822407d/Mnemosyne
source_master_at_preparation: 914cc1731fc8152610e215b064a81d057043bf0c
```

## 1. Controlling preparation and run decisions

```yaml
Owner_preparation_decision:
  path: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PREPARATION-OWNER-DECISION-001.md
  blob: 3577b2f57440762c1bb8f9e344edfb7549e5aeb3
run_decision_candidate:
  path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-001.md
  blob: bb140196a38d8b14f6eba9e2175cd45744efb23b
```

Future G2A must name the merged run-decision blob above and this manifest's own merged blob separately. This file does not recursively list its own blob.

## 2. Exact package blobs

```yaml
package_files:
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/README.md: c34cdd093a51516cbeb079dd77977c9e183cb9f7
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/00-owner-gates-and-surface-contract.md: 543b4c7740a256b2cb54ef5a2d73f9b007e9d143
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/02-branch-task-and-effect-map.md: 6da0b44d982adb6431b54cd2ecc1af92c52d2b82
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/03-alpha-worker-task.md: 9cb67f6e8b007941779326509db0b2d07fd035dd
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/04-beta-worker-task.md: 9544963bc40face1eb3caca190de6fe5f96802f5
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/05-controller-task-and-order-construction.md: 886358e14a595bec7b20e032d97cb7d80b253773
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/06-mechanical-checks-and-result-template.md: 0ace207590f5219be23bd68bcee055f99ec13d25
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/07-operator-flow-and-startup-messages.md: 9b19d47014caaeeee13177e054a5724f161c0796
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/08-package-integrity-and-non-execution-checklist.md: 1493267a1a1488cb159a2ff4074057abeb065a47
required_package_file_count_including_this_manifest: 10
```

## 3. Load-bearing Mnemosyne sources

```yaml
execution_and_guards:
  current/human-approved-spec.md: 01f64a8223677829320c66dd46d3f172cc9155cc
  current/github-single-active-pr-lineage-guard.md: 042efe9e353097a17eea38d0bcb0ff1da7c4385e
  current/run-context-and-pr-provenance-guard.md: 0e588b3f6789d0d941221d33c3eaba1561f6e2a3
  current/user-operation-next-step-capability-and-intent-guard.md: 265d61aad34c9e55006647c9e12d77c4214310ea
F2_and_V2_design:
  notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md: 4d59e6edefb5f166261dca353f4552e9346d0f8a
  notes/research-adjudications/MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md: 27d607257bb1700d9ff9c73f0048a6a7b7847746
  notes/cross-repository-safe-concurrency-and-ordered-work-amendment-candidate-v0.1.md: 46fd66dc23d6615ea167e0950de970cc316c056b
  notes/validation-designs/cross-repository-safe-concurrency-v2-staged-validation-v0.1.md: f66678c0ebdc28a9407553b918838256e6e633a4
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
A0_accepted_evidence:
  notes/validation-adjudications/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-ADJUDICATION-001.md: 47f5067158f925bb042143f4d4d5b02a0cdb30d1
  notes/evidence-corrections/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-PATH-IDENTITY-CORRECTION-001.md: 7ed2fe5b0c155ee502aff2634b73dc5edd3517cb
  notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-OWNER-DECISION-001.md: cce3e10ac4e6b02d65d00edac2a6244823d67586
```

Any mismatch requires fresh Pro review before A1 G2A. Normal package/result publication may move Mnemosyne `master` while these exact blobs remain unchanged.

## 4. Validation repository hard pins

```yaml
validation_repository:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  default_branch: master
  default_branch_commit: e8e3296922185b4b70997c2351d6f39423f2cd4f
  fixture:
    ref: tlr-v1-fixture-base
    commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
    tree: f1e221ce8aef404579b96adb3ab01319016889db
    material_class: public_synthetic_only
  A0_controller:
    ref: v2a-sentinel-001-controller
    final_head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
    write_authorized_by_A1: false
```

### Frozen historical V1 ref inventory

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

All names and SHAs remain immutable evidence for A1.

## 5. Exact fixture identities used by A1

```yaml
base_top_level_trees:
  backups-fixture: 5ab44553054cf8d06acf791af44b664c2896fa56
  libraries: 9ef4ba0f9e132202d0ec45c2e51e5c9e5567c2b5
  repository-governance: 9f8d6294fe97dc2d537df18c4c7abcc6897d4cb7
  run-evidence: 4572ca8616d6c88413e9efbdeae4fc199c170df2
  runs: b55b1fe8a41cdd81f224637fec5797c35fb5ac01
  shared: a61736f9f5a894dea4dda559513b3e355362ad4b
  targets: b1701725c545ebe0a7f633fa00ea869574ad5217
base_targets:
  agent_alpha_tree: 05f9acdb82521a2d72a93b4271115c444477e853
  agent_beta_tree: dc3f5be7a8fde2b2cace9385353f1b0377af92ac
  alpha_authority_blob: 73da56b34e8a078780a04ddc6db7a1b4ffc078ed
  alpha_source_blob: 27a2a0f2b679494c11d2885377e564a0b10ce896
  alpha_test_blob: f3e0535c9f830115acdedc9c1c8b637896a79791
  beta_authority_blob: 6310b0c931a4c0ee1ca35dd2ca107b586248e6f0
  beta_source_blob: 8d4db9cae3d3f8dab7f99fca633ccbaa440dd3d9
  beta_test_blob: f878642cfd1adee37efeb1768b95a7e1306d88f5
generated_target_index:
  path: repository-governance/generated-target-index.json
  blob: 076ed542da7680901eb03cc4d00682550c5e4376
```

## 6. Exact A1 target blobs and expected trees

```yaml
Alpha:
  final_blobs:
    targets/agent-alpha/src/alpha_feature.py: 18959a155b44d1d24a14407f23bb8731eb5aaf49
    targets/agent-alpha/tests/test_alpha_feature.py: 9303a7ce7968512c1036c5ad19bbfd61c8db544a
  expected_subtrees:
    src: 36a77ea02517a7ab96a72562557e9b8d1d3f2960
    tests: 58fcc6280675dce8b717f66821eaf360e5bfcd9d
    agent_alpha: 9f30907c7174fb00f1f80b90dc118a9c2eef344e
    targets: fdb87ba25d93da5fa0a82410d592062a0cca118b
  expected_root_tree: 5929e4caeac1f10681057f530286e3d3dc27b28d
Beta:
  final_blobs:
    targets/agent-beta/src/beta_feature.py: 5ddad8381514e9a203ac1b5e67e38463fe2b14a2
    targets/agent-beta/tests/test_beta_feature.py: a9eafff2c2e007f556dc789fecb4eb465e2955ca
  expected_subtrees:
    src: 5fd10b293e5ede521870e4a9d277676a4de5b432
    tests: af6fa1eef776cb4548cb7dc251ff93cb798c8667
    agent_beta: e004404edde45225ea53d9ab84997bcf7921f618
    targets: 24fc0174e5d1c77a9bb2068302809e8aaf6a0c8b
  expected_root_tree: 5dc4fa21362bb9e130de71779e2af0296eb11acc
Combined:
  expected_targets_tree: bbdddd63f3c1ba9210a685c05bbef96ea13cc7ab
  expected_root_tree_for_both_orders: 2b919544aecfbd1634e5f136af22571f2e8d9fd0
```

These are mechanically derived Git identities, not runtime-test evidence. A future executor must reproduce them exactly from the fixture tree and frozen blobs.

## 7. Future branch and output manifest

```yaml
branch_map:
  controller: v2a-a1-001-controller
  alpha_worker: v2a-a1-001-alpha
  beta_worker: v2a-a1-001-beta
  alpha_then_beta: v2a-a1-001-order-alpha-beta
  beta_then_alpha: v2a-a1-001-order-beta-alpha
branch_count: 5
pull_requests_allowed: false
controller_output_root: runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001/
controller_output_files:
  - 00-controller-receive.yaml
  - 01-product-model-and-permission-receipt.yaml
  - 02-branch-task-effect-map.yaml
  - 03-alpha-worker-result.yaml
  - 04-beta-worker-result.yaml
  - 05-order-alpha-beta-result.yaml
  - 06-order-beta-alpha-result.yaml
  - 07-semantic-and-mechanical-checks.yaml
  - incidents/incident-ledger.yaml
  - 08-a1-result-bundle.yaml
controller_output_file_count: 10
other_writes_allowed: false
```

## 8. Dynamic G2A fields

Not frozen here:

```yaml
future_G2A_dynamic_fields:
  protected_Mnemosyne_master:
  protected_Meta_Agent_master:
  controller_Owner_authorized_visible_label:
  controller_operator_selected_visible_label:
  Alpha_Owner_authorized_visible_label:
  Alpha_operator_selected_visible_label:
  Beta_Owner_authorized_visible_label:
  Beta_operator_selected_visible_label:
  execution_window_start:
```

Future Pro must fill these from then-current repository state and direct Owner/operator evidence. No assistant may infer them.

## 9. Invalidation and stop rules

Fresh Pro must refresh or block before G2A if:

- any exact blob or tree in this manifest changes;
- validation master, fixture, A0 head or V1 inventory changes;
- any A1 branch, PR or equivalent lineage exists;
- model/product/tool capability changes;
- the exact branch, worker-message, write-set, output, retry, retention or cleanup contract changes;
- a known active route is expected to move a protected ref during A1.

After G2A, protected refs cannot be refreshed. A mismatch blocks. An executor cannot repair this package or retry a failed write.
