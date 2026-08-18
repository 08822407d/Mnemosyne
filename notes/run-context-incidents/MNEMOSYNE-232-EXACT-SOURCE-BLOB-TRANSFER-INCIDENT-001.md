# MNEMOSYNE-232 Exact-Source Blob Transfer Incident 001

```yaml
incident_id: MNEMOSYNE-232-EXACT-SOURCE-BLOB-TRANSFER-INCIDENT-001
task_id: MNEMOSYNE-232
phase: exact_source_preservation
category: bounded_blob_transfer_attempts_created_unreferenced_Git_objects
observed_unreferenced_blob_shas:
  - ed7a03ff392ee722893f48dcb1181e14c86d3a29
  - d35917aeb3addf3c93bcf7038113ebb001b0565a
  - b64212605f423736417666d99dd01662d421086e
all_blobs_used_by_any_tree_commit_or_ref: false
branch_ref_moved_by_failed_attempts: false
identical_failed_payload_retried: false
```

## Event

Three bounded GitHub `create_blob` attempts produced non-matching objects: one incomplete/truncated source payload, one archive part missing its required final LF, and one altered/truncated archive-part transfer. Each returned SHA differed from the mechanically predicted blob identity. All were rejected and never referenced by a tree, commit or branch.

## Recovery

The task switched to an `EXACT_RECONSTRUCTABLE_ARCHIVE`: deterministic gzip, base64, five bounded parts, a reconstruction manifest and original/gzip hashes. This is a distinct, verified recovery method, not reuse of the bad blob.

## Evidence limit

The rejected blobs may remain as unreachable repository objects. Branch/ref inventory cannot prove their absence. This incident is recorded as an actual example of why `ref_not_moved` must not be generalized to `zero_repository_side_effect`.

```yaml
expected_values_refreshed: false
package_or_fixture_repaired_in_place: false
validation_repository_affected: false
A1_execution_affected: false
not_future_precedent: true
```
