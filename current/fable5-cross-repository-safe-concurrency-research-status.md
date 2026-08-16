# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
last_updated_by_task: MNEMOSYNE-221
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: FABLE_REPORT_RECEIVED_FRESH_PRO_ADJUDICATED_PENDING_OWNER_DISPOSITION
Fable_report_received: true
return_identity_verified: true
fresh_Pro_adjudication_completed: true
Owner_disposition_pending: true
external_execution_or_quota_authorized: false
automatic_retry: false
validation_design_authorized: false
validation_execution_authorized: false
repository_write_by_Fable: false
real_target_adoption_authorized: false
```

## Preserved result

```text
raw/research-reports/cycles/2026Q3-cross-repository-safe-concurrency/
```

Exact return identities:

```yaml
ZIP_sha256: d141fb3962c61617e2051c9b318516d63437e287f7b88b2f3e41df9d130c0559
formal_report_sha256: 83468668e64a7bf9b82292b0b672d6cb8b249e4cd069395df3a0888b9eda2ccd
visible_process_output_sha256: 4575975fa7af3dd2de3d8fbf4d06dd662257efc94f046d335c48a0731d964304
input_snapshot_file_count: 30
```

## Fresh Pro disposition

```yaml
return_identity: PASS_EXACT
run_validity: ACCEPT_WITH_LIMITATIONS
input_verification: PASS_WITH_BOUNDED_IDENTITY_DEFECT
task_contract_compliance: PASS_WITH_LIMITATIONS
citation_portability: FAIL
architecture_direction: ACCEPT_AS_CORROBORATED_MODIFIED_PROVISIONAL_DIRECTION
technical_details: ACCEPT_WITH_MATERIAL_CORRECTIONS
implementation_readiness: REJECT
```

The central hybrid direction is accepted as useful corroboration:

- task-local contracts and exact scope evidence by default;
- conservative serialization/reconciliation for shared/global/unknown work;
- no mandatory global orchestrator;
- ordered cross-repository identities and explicit partial-failure handling;
- stronger synthetic failure evidence before stronger acceptance.

Material corrections include:

- disjoint write sets alone are not a sufficient non-interference proof;
- final diff verification is not complete optimistic concurrency control;
- any future lease requires destination-enforced fencing;
- automatic compensation is not a default Git recovery mechanism;
- GitHub stale-ref primitives are tool-surface-specific;
- GitHub Actions concurrency and SLSA level claims in the report were overstated;
- many “missing” rules already exist in candidate v0.2;
- the report's external sources are not portable;
- one Owner-decision blob was truncated.

## Current Owner gate

```text
notes/owner-decision-candidates/
MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-DISPOSITION-CANDIDATE-001.md
```

Pro recommends:

```text
A — accept the modified provisional amendment and authorize V2 design only
```

This does not authorize V2 execution or any real-target action.

## Snapshot-branch release

After the result/adjudication PR is merged:

- the exact 30-file input snapshot will exist under the preserved research cycle;
- the exact Fable return will be reconstructable from `source-archive/`;
- no further Project re-sync is expected.

At that point the retention obligation for:

```text
mne-dr-005-project-knowledge-snapshot-001
```

may be released, provided the merge and preserved paths are mechanically verified.

The receive-only result-intake branch may also be released after its contents are confirmed present in the merged canonical result lineage.
