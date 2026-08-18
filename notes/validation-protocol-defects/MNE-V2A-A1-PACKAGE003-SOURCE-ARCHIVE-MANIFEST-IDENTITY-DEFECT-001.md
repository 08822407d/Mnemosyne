# V2-A A1 Package 003 Source-Archive Manifest Identity Defect 001

```yaml
defect_id: MNE-V2A-A1-PACKAGE003-SOURCE-ARCHIVE-MANIFEST-IDENTITY-DEFECT-001
task_id: MNEMOSYNE-233
run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-001
classification: package_publication_identity_closure_failure
severity: material_pre_execution_blocker
architecture_candidate_defect: false
A1_runtime_failure: false
validation_repository_affected: false
```

## Observed defect

Package 003 and three publication/transfer artifacts froze this path/blob tuple:

```yaml
path: raw/validation-reviews/MNE-DR-005-A1-package002-readiness-review/exact-source/source-artifact-receipt-and-reconstruction-manifest.yaml
recorded_blob: 7c2af723c395283aca23a5240847e46e6c97e93b
```

The path's actual blob on PR #300's merged tree and current `master@b70acfc8ab190f18fdd987f034963039728ca887` is:

```yaml
actual_blob: 6e90c8f1384657939d5dcd9e7e30177e3c2e7b2a
```

Direct lookup of `7c2af723c395283aca23a5240847e46e6c97e93b` did not resolve to a repository blob during the receive investigation.

Affected committed artifacts:

```yaml
package_003_manifest:
  path: notes/cross-repository-safe-concurrency-v2a-a1-execution-package-003/01-package-and-source-manifest.md
  blob: 7611773d861e065f539118853ec93026515f4065
handoff_package_001:
  path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-handoff-package.md
  blob: d2dc7f9dbb1c023cb377a78934eee91469e0485e
startup_prompt_001:
  path: handoff/mnemosyne-f2-v2a-a1-wrapper-verification-repair-startup-prompt.md
  blob: d5926454ab4718953b0fab976e4a82cf7f31e4cb
MNEMOSYNE_232_verification:
  path: notes/codex-task-results/MNEMOSYNE-232-verification.md
  blob: 3fbd45e724a25565a3b747e848a6b09bf47c9801
```

The first handoff attempt also failed because the old conversation's visible startup text used a wrong package path, package ID and receive key even though the repository's canonical startup artifact used the correct values. That is a separate user-visible operator-flow/canonical-artifact drift. Both failures point to missing final publication closure.

## Evidence and root-cause limit

Independent reconstruction performed by MNEMOSYNE-233 reproduced:

```yaml
original_bytes: 37074
original_sha256: 6e639f7b49c8bfd6d47e950a7eb6cce54cf41c07903fb57fae3d0a29b7c2a4e0
gzip_bytes: 13234
gzip_sha256: e138a3ab4f28f38b5c17935992d3db6c2e0688f5dc5a46ca37bb346b62e7032c
archive_parts: 5
all_archive_part_git_blob_identities_match_repository_manifest: true
reconstructed_bytes: 37074
reconstructed_sha256: 6e639f7b49c8bfd6d47e950a7eb6cce54cf41c07903fb57fae3d0a29b7c2a4e0
```

No source-review content corruption was observed.

The exact origin of `7c2af723c395283aca23a5240847e46e6c97e93b` is not proven by committed history. The strongest evidence-bound explanation is that a provisional, stale or incorrectly calculated identity was propagated without final-head path/blob readback. Do not represent this inference as mechanically proven producer state.

## Disposition

```yaml
underlying_archive_corruption_observed: false
source_identity_metadata_defect_observed: true
packages_001_002_003_preserved_immutable: true
package_003_ready_for_G2A_as_written: false
A1_rerun_required: false
additive_candidate_and_package_004_required: true
corrected_handoff_and_receive_rehearsal_required: true
```

Package 004 may supersede only this source-identity tuple and identities derived from it. It must not modify the wrapper transport/comparison repair, fixture, branch map, tasks/effects, expected blobs/trees, order oracle, ten-output contract, no-PR, no-retry, retention or execution authorization.

A separate general handoff-protocol hardening audit remains a TODO. It is not implemented by this repair.
