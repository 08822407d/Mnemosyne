# V2-A A1 Package 004 — Package and Source Manifest 001

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-004-SOURCE-MANIFEST-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-004
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
status: frozen_manifest_without_recursive_self_hash
source_repository: 08822407d/Mnemosyne
source_master_at_repair: b70acfc8ab190f18fdd987f034963039728ca887
```

Future review and G2A name this manifest's merged blob separately.

## Controlling repair identities

```yaml
Owner_preparation_authorization:
  path: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-004-PREPARATION-OWNER-DECISION-001.md
  blob: 7c545fd2bec50a4efd265a7daf958cc61562d800
source_identity_defect:
  path: notes/validation-protocol-defects/MNE-V2A-A1-PACKAGE003-SOURCE-ARCHIVE-MANIFEST-IDENTITY-DEFECT-001.md
  blob: d9a35c0a6691689a50be821e0783b00dc9904eb2
run_decision_candidate_004:
  path: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-RUN-DECISION-CANDIDATE-004.md
  blob: 87f110c5f99ba702a93cd38ca78bb6bfbff002db
```

## Correct source archive identity

```yaml
source_review_archive_manifest:
  path: raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/source-artifact-receipt-and-reconstruction-manifest.yaml
  controlling_actual_blob: 6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a
  superseded_incorrect_blob_for_scope: 7c2af723c395283aca23a5240847e46e6c97e93b
  original_bytes: 37074
  original_sha256: 6e639f7b49c8bfd6d47e950a7eb6cce54cf41c07903fb57fae3d0a29b7c2a4e0
source_review_archive_parts:
  raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/archive-part-001.b64: 89d4bbbae13745fd7ebea22fb16cb026b4e834e9
  raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/archive-part-002.b64: ccd208ca144c59251533c310fd7bd0a27317721a
  raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/archive-part-003.b64: cce7403d68c3ac9337620f2cf1b5a56aefaac968
  raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/archive-part-004.b64: 4b716ad17d9216bad885d4ec8da0bd2fb972e21e
  raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/archive-part-005.b64: 77a827e8532e0ffba920e80cda7a71ee1446d591
```

## Package 004 files

```yaml
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-004/README.md: b61b9fa5521d899e328f1beb20b0c2c2f984c655
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-004/00-delta-precedence-and-source-identity-correction-contract.md: a8c70040bc54109fa3aa92b31bf36c4205e78666
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-004/02-independent-archive-reconstruction-and-identity-receipt.md: 47a8a5508000135ea267814b9e0d0e564558e230
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-004/03-corrected-handoff-publication-and-receive-rehearsal-contract.md: 8dcc7cbaece35b8957849e7006ccfeeb931d0890
  notes/cross-repository-safe-concurrency-v2a-a1-execution-package-004/04-package-integrity-and-non-execution-checklist.md: 28f72b64ae1bbb632a89a7b9795b9cf83d9e5f92
required_package_file_count_including_this_manifest: 6
```

The manifest omits only its own recursive blob.

## Inherited candidates and packages

```yaml
candidate_003: 28da6ab6a3f3638292e83a7df511100d8d23b4b0
package_003_manifest: 7611773d861e065f539118853ec93026515f4065
candidate_002: a8b627b8aa74b5a1a5af19d3af485a17aa2cd0b7
package_002_manifest: 1f54f4711a44129c3dfee066aa2ab297f94718b7
candidate_001: bb140196a38d8b14f6eba9e2175cd45744efb23b
package_001_manifest: 12a480449b1dac45cd265864a812f399d19ec15c
```

Package 004 supersedes Package 003 only for the source archive manifest tuple and route-specific publication/handoff closure. All wrapper, model-binding, fixture, branch, task/effect, blob/tree, order, ten-output, no-PR, no-retry, retention and evidence-ceiling terms remain inherited.

## Validation pins

```yaml
validation_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
fixture_commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
A0_controller_head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
future_A1_branches:
  - v2a-a1-001-controller
  - v2a-a1-001-alpha
  - v2a-a1-001-beta
  - v2a-a1-001-order-alpha-beta
  - v2a-a1-001-order-beta-alpha
```

Any mismatch requires fresh Pro. An executor cannot refresh expected values, repair a package, issue G2A or execute A1.
