# V2-A A0 Package 003 — Package and Source Manifest

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-SOURCE-MANIFEST-003
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-003
status: frozen_manifest_without_recursive_self_hash
```

## 1. Controlling candidate and review evidence

```yaml
controlling_candidate:
  path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-003.md
  blob: 9e46dd849c3c8604f5e2fa7fce9c02c5504ff202

fresh_Pro_review:
  path: notes/adjudications/MNEMOSYNE-224-PACKAGE-002-FRESH-PRO-REVIEW-001.md
  blob: ba239150234dc161d0d605195e0efef1a9e5ef9f

operator_selection_incident:
  path: notes/run-context-incidents/MNEMOSYNE-224-OPERATOR-SELECTION-MISREPRESENTATION-001.md
  blob: 5b22b5e5e014922745088aa029b92238439d4037
```

The future Owner G2A binds the candidate-003 blob above and this manifest's exact merged blob. This manifest intentionally does not recursively include its own blob.

## 2. Package 003 exact blobs

```yaml
package_003_files:
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/README.md: 28280a2203fbb5d858954d095981602a4502b4e4
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/00-delta-precedence-and-provenance-contract.md: 96db07f2ab9b3239eb3c0b1ded58e15538765744
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/02-next-tier-controller-amendment.md: e3fa54205e1fa93116c52f515a4661b955e1d6bc
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/03-startup-message.md: dfb75bc9e2fda1ccba82f41eecd33459b71f495e
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/04-package-integrity-and-non-execution-checklist.md: 6741824758f6037443eb272da16c0847e6ea4d8d
```

Required package-003 file count is six including this manifest.

## 3. Exact inherited package 002 blobs

```yaml
parent_candidate_002:
  path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-002.md
  blob: 78185751607cf4bd1930710bf1e5e84c9235bb33

parent_package_002:
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/README.md: 3a4bb50cd8c2d89027690f0bc196eba7bf0bbebe
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/00-controller-receive-and-surface-contract.md: 3ee4276afcabfce3986b44a24ba0b2cdced239ba
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/01-package-and-source-manifest.md: f41a16d9da165a161ef9148994ef025f9cd3a806
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/02-next-tier-controller-task.md: 89382a949fbcfa0542679553b5a245137512e1ce
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/03-mechanical-checks-and-result-template.md: b615be7a3c05b3c5dd5d40e0e5cadc7a581cb0c6
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/04-startup-message.md: 5bb7053653d23a47ef113db36ef85d8bbc83884d
  notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/05-package-integrity-and-non-execution-checklist.md: c573d4c7b2e2558b482e0372b2d5310d79168814
```

Package 002 is inherited except where package 003 explicitly supersedes model-selection authorization/startup/provenance scope.

## 4. Load-bearing parent design and authority blobs

These remain governed by package-002 manifest 002 and must still match exactly. At minimum:

```yaml
load_bearing_sources:
  current/human-approved-spec.md: 01f64a8223677829320c66dd46d3f172cc9155cc
  current/github-single-active-pr-lineage-guard.md: 042efe9e353097a17eea38d0bcb0ff1da7c4385e
  current/run-context-and-pr-provenance-guard.md: 0e588b3f6789d0d941221d33c3eaba1561f6e2a3
  current/user-operation-next-step-capability-and-intent-guard.md: 265d61aad34c9e55006647c9e12d77c4214310ea
  notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md: 4d59e6edefb5f166261dca353f4552e9346d0f8a
  notes/research-adjudications/MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md: 27d607257bb1700d9ff9c73f0048a6a7b7847746
  notes/cross-repository-safe-concurrency-and-ordered-work-amendment-candidate-v0.1.md: 46fd66dc23d6615ea167e0950de970cc316c056b
  notes/validation-designs/cross-repository-safe-concurrency-v2-staged-validation-v0.1.md: f66678c0ebdc28a9407553b918838256e6e633a4
```

The complete parent V2 package blob list remains in manifest 002 and is transitively required.

## 5. Inherited validation repository identities

```yaml
validation_repository:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  master: e8e3296922185b4b70997c2351d6f39423f2cd4f
  fixture_ref: tlr-v1-fixture-base
  fixture_commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
  future_controller_branch: v2a-sentinel-001-controller
  controller_branch_must_be_absent: true
  output_file_count: 7
```

The complete 16-ref historical `tlr-v1-*` inventory in manifest 002 remains hard-pinned.

## 6. Dynamic execution-window fields

Not frozen in this file:

```yaml
future_G2A_dynamic_fields:
  protected_Mnemosyne_master:
  protected_Meta_Agent_master:
  authorized_visible_model_label:
  operator_selected_visible_model_label:
```

Future G2A additionally supplies this manifest's exact merged blob and the candidate-003 blob already listed above.

## 7. Invalidation and scheduling

Fresh Pro must refresh or block before G2A if:

- any exact blob in this or inherited manifest changes;
- validation master/fixture/V1 inventory changes;
- controller branch/competing lineage appears;
- model label or product/tool surface changes;
- run scope, seven paths, retry/quota/retention boundary changes;
- a known active route is expected to move Mnemosyne `master` during A0.

Ordinary publication before G2A may move Mnemosyne `master`; the current execution-window baseline is frozen only in the Owner G2A/startup message.
