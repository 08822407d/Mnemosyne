# V2-A A1 Package 002 — Package and Source Manifest 001

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-002-SOURCE-MANIFEST-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-002
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
status: frozen_manifest_without_recursive_self_hash
source_repository: 08822407d/Mnemosyne
source_master_at_repair: 4ff2d021a568ae3bfdf98c7dee81d87545fcd3d1
```

Future G2A must name this manifest's merged blob separately. This file does not recursively list its own blob.

## 1. Controlling repair decisions

```yaml
Owner_repair_authorization:
  path: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-002-PREPARATION-OWNER-DECISION-001.md
  blob: f12b4526c30b099c2f8db982198ecf63c90d9718
model_binding_order_defect:
  path: notes/validation-protocol-defects/MNE-V2A-A1-MODEL-BINDING-ORDER-DEFECT-001.md
  blob: 7cd37e808540e50c57a7440e367fabaa99442826
run_decision_candidate_002:
  path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-002.md
  blob: a8b627b8aa74b5a1a5af19d3af485a17aa2cd0b7
```

## 2. Package 002 exact files

```yaml
package_files:
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-002/README.md: 9d8de59e633af40070c28df74d956a86bc839df4
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-002/00-delta-precedence-and-defect-contract.md: 85855f2e434902f5fbdc62b80b5d232d2646c3a4
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-002/02-staged-model-binding-contract.md: 935f19c92da2f47a8227ab7d4c172833ca1b5d58
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-002/03-revised-operator-flow-and-startup-messages.md: fd125ff3d434870a60014330c52b914d2ddd0a5b
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-002/04-package-integrity-and-non-execution-checklist.md: 935e2284866f92300fba602257d7c2d5312480a5
required_package_file_count_including_this_manifest: 6
```

## 3. Inherited candidate and package 001

```yaml
inherited_run_decision_candidate_001:
  path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-001.md
  blob: bb140196a38d8b14f6eba9e2175cd45744efb23b
inherited_package_001_manifest:
  path: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/01-package-and-source-manifest.md
  blob: 12a480449b1dac45cd265864a812f399d19ec15c
inherited_package_001_files:
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/README.md: c34cdd093a51516cbeb079dd77977c9e183cb9f7
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/00-owner-gates-and-surface-contract.md: 543b4c7740a256b2cb54ef5a2d73f9b007e9d143
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/02-branch-task-and-effect-map.md: 6da0b44d982adb6431b54cd2ecc1af92c52d2b82
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/03-alpha-worker-task.md: 9cb67f6e8b007941779326509db0b2d07fd035dd
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/04-beta-worker-task.md: 9544963bc40face1eb3caca190de6fe5f96802f5
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/05-controller-task-and-order-construction.md: 886358e14a595bec7b20e032d97cb7d80b253773
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/06-mechanical-checks-and-result-template.md: 0ace207590f5219be23bd68bcee055f99ec13d25
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/07-operator-flow-and-startup-messages.md: 9b19d47014caaeeee13177e054a5724f161c0796
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-001/08-package-integrity-and-non-execution-checklist.md: 1493267a1a1488cb159a2ff4074057abeb065a47
required_inherited_package_001_file_count_including_manifest: 10
```

Package 002 supersedes only the exact delta stated in `00-delta-precedence-and-defect-contract.md`. All inherited identities remain mandatory.

## 4. Load-bearing Mnemosyne sources

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
A0_accepted_evidence:
  notes/validation-adjudications/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-ADJUDICATION-001.md: 47f5067158f925bb042143f4d4d5b02a0cdb30d1
  notes/evidence-corrections/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-PATH-IDENTITY-CORRECTION-001.md: 7ed2fe5b0c155ee502aff2634b73dc5edd3517cb
  notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-OWNER-DECISION-001.md: cce3e10ac4e6b02d65d00edac2a6244823d67586
```

The parent V2 package identities remain inherited through package 001's exact manifest and must still match at execution-time review.

## 5. Validation repository hard pins

```yaml
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
visibility: public
material_class: public_synthetic_only
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

The frozen 16-ref `tlr-v1-*` inventory, fixture objects, expected worker blobs/trees and order oracle remain exactly those in package 001 manifest.

## 6. Repaired dynamic fields

A future controller G2A supplies:

```text
<RUN_DECISION_CANDIDATE_002_BLOB>
<PACKAGE_SOURCE_MANIFEST_002_BLOB>
<PROTECTED_MNEMOSYNE_MASTER>
<PROTECTED_META_AGENT_MASTER>
<CONTROLLER_OWNER_AUTHORIZED_VISIBLE_LABEL>
<CONTROLLER_OPERATOR_SELECTED_VISIBLE_LABEL>
<ALPHA_OWNER_AUTHORIZED_VISIBLE_LABEL>
<BETA_OWNER_AUTHORIZED_VISIBLE_LABEL>
```

Worker selected-label values are not controller-G2A fields. They are supplied separately at the actual Alpha/Beta worker launches.

## 7. Source-integrity rule

Normal publication may move Mnemosyne `master`. Source integrity is established through exact path/blob identities. Future G2A separately freezes then-current Mnemosyne and Meta-Agent refs for the execution window.

Any mismatch in package 002, inherited package 001 or load-bearing sources requires fresh Pro review. An executor may not refresh values or repair a package.
