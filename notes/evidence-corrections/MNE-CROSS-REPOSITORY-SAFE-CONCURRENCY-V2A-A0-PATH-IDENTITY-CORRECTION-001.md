# MNE V2-A A0 Evidence Path-Identity Correction 001

```yaml
correction_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-PATH-IDENTITY-CORRECTION-001
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
source_output:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  branch: v2a-sentinel-001-controller
  final_head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
  path: runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/02-package-and-material-receipt.yaml
  final_blob: ad227d43d2eb0d74bf5938b50d220141ff6fdfdf
status: additive_durable_correction
historical_output_rewritten: false
controller_branch_modified_or_deleted: false
package_003_modified: false
A0_rerun_required: false
```

## Incorrect historical assertion

The preserved A0 output records this path/blob pair:

```yaml
path: notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/04-integrity-checklist.md
blob: 6741824758f6037443eb272da16c0847e6ea4d8d
```

The shortened path does **not** exist at the frozen Mnemosyne source commit:

```text
9b5a3a16d83f6cabc341445d70d350e3391d1daf
```

## Canonical identity

The package-003 manifest and repository tree identify the canonical tuple as:

```yaml
path: notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/04-package-integrity-and-non-execution-checklist.md
blob: 6741824758f6037443eb272da16c0847e6ea4d8d
frozen_commit: 9b5a3a16d83f6cabc341445d70d350e3391d1daf
exists: true
```

Controlling manifest:

```text
notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-003/01-package-and-source-manifest.md
blob 967c7a9ce38883ab897bf856fa4004b987e7d911
```

## Disposition

```yaml
classification: BOUNDED_EVIDENCE_ARTIFACT_PATH_IDENTITY_DEFECT
false_historical_path_assertion: true
matching_blob_makes_false_path_valid: false
underlying_package_corruption_found: false
canonical_path_blob_independently_reverified: true
substantive_source_integrity: PASS_AFTER_INDEPENDENT_CANONICAL_PATH_BLOB_REVERIFICATION
package_integrity: PASS
historical_output_02_retained_unchanged: true
package_repair_required: false
A0_rerun_required: false
later_V2_A_permanently_blocked: false
durable_correction_required_before_later_V2_A: satisfied_by_this_record_after_merge
```

Git blobs identify contents, not repository paths. Therefore the original row is not accepted as a valid path/blob verification even though its blob equals the canonical file's blob.

The correct treatment is additive correction rather than in-place rewriting. The original A0 artifact remains available as historical executor evidence; this file supplies the controlling correction for future review.

## Related adjudication

```text
notes/validation-adjudications/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A0-ADJUDICATION-001.md
```

That adjudication also records `A0-TOOL-001` as a separate non-blocking tool/product limitation. This path correction does not change the A0 overall disposition:

```text
PASS_WITH_BOUNDED_EVIDENCE_DEFECTS
```
