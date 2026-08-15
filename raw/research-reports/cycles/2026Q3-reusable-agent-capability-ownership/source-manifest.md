# RC-2026Q3 Reusable Agent Capability Ownership — Source Manifest

```yaml
cycle_id: RC-2026Q3-reusable-agent-capability-ownership
canonical_task_id: FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001
canonical_display_name_after_storage: MNE-DR-004 能力归属
run_display_name_as_used: MNE-DR-003 能力归属
source_master_at_storage_task_start: 1a61414bbe86a9a1b2a37c2ae1d22caf21c39dea

report:
  archive_member: FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-report.md
  bytes: 38468
  sha256: 80da22b0d4b35ecf1525b1e9a12a7357c8d32557af92cc7730e93fa780b6ae59
  preservation_level: EXACT_RECONSTRUCTABLE_ARCHIVE

final_task:
  path: raw/research-reports/cycles/2026Q3-reusable-agent-capability-ownership/originals/MNE-DR-003-final-task.md
  bytes: 11314
  sha256: 9fed83fc00aeecd528709409cd2bb0718e325371938a257bc294b27d3fba9fda
  preservation_level: EXACT_FILE_IN_REPOSITORY

input_manifest:
  path: raw/research-reports/cycles/2026Q3-reusable-agent-capability-ownership/originals/MNE-DR-003-input-manifest.yaml
  bytes: 3138
  sha256: ab6d1c06c36480cb2d653b21bc94f17f1b710725bce232e2d2465b91e5e5c1a5
  preservation_level: EXACT_FILE_IN_REPOSITORY

source_archive:
  directory: raw/research-reports/cycles/2026Q3-reusable-agent-capability-ownership/source-archive/
  reconstructed_zip_bytes: 23782
  reconstructed_zip_sha256: 29bee30189073df82b43741954aea3913ff34240c3e2f277d8c2540545adcb8d
  base64_part_count: 7
  preservation_level: EXACT_RECONSTRUCTABLE_ARCHIVE

visible_process_output:
  path: raw/research-reports/cycles/2026Q3-reusable-agent-capability-ownership/operator-records/FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001-process-output-normalized.md
  preservation_level: NORMALIZED_READABLE_COPY
  exact_provider_internal_log: unavailable

provider_reported_source_count: 218
portable_source_table_in_received_report: absent
repository_write_performed_by_research_run: false
validation_executed_by_research_run: false
```

## Reconstruction check

Follow `source-archive/README.md`; concatenate the seven ordered Base64 parts, decode them, verify the ZIP SHA-256, and then verify all three ZIP members against the identities above.

The archive is a repository artifact constructed and mechanically verified by MNEMOSYNE-213. It is not claimed to be an export of an unobserved Claude internal representation.
