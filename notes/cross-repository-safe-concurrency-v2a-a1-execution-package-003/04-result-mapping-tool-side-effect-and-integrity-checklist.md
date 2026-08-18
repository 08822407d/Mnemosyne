# V2-A A1 Package 003 — Result Mapping, Tool Side-Effect and Integrity Checklist

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-003-INTEGRITY-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-003
status: preparation_checklist_not_run_authorization
```

No eleventh output is added.

- `02` stores both templates before Alpha.
- `03` and `04` each store expected, Owner-sent and worker-received wrapper blocks plus exact comparison fields.
- `08` summarizes both comparisons and any partial-state disposition.

Required comparison schema:

```yaml
runtime_wrapper_comparison:
  expected_wrapper_verbatim:
  Owner_sent_wrapper_verbatim:
  worker_received_wrapper_verbatim:
  expected_wrapper_sha256:
  Owner_sent_wrapper_sha256:
  worker_received_wrapper_sha256:
  all_wrapper_sha256_values_equal:
  expected_equals_Owner_sent:
  Owner_sent_equals_worker_received:
  expected_equals_worker_received:
  only_role_selected_label_placeholder_changed:
  G2A_authorized_label_match:
  task_path_blob_repository_branch_base_profile_match:
  comparison_result: PASS | FAIL | DISPUTED_REQUIRES_FRESH_PRO
```

Positive A1 requires both Git worker contracts, both wrapper comparisons and both order trees PASS, with no prohibited branch/PR/output/retry/repair/later cell.

Object calls may succeed before `update_ref`. Incident evidence must record returned object SHAs when available, unknown unenumerable object risk when ambiguous, and ref state separately. `ref_not_moved` cannot support `zero_repository_side_effect`; no retry or cleanup is authorized.

Package 003 requires exactly six files: README, 00, 01, 02, 03, 04. The manifest omits its own recursive blob.

```yaml
A1_G2A_issued: false
A1_execution_authorized: false
validation_repository_written: false
A1_branches_created: false
package_001_or_002_modified: false
later_cells_or_targets: false
external_research_or_quota: false
automatic_retry_or_repair: false
```

Fresh Pro blocks before G2A on any source/package/ref/lineage mismatch or if the current surface cannot preserve, return and compare the canonical blocks.
