# WORK-ULTRA-FABLE-GF5-STAGE-A-001 Storage Anomaly Record

> Non-execution-source integrity record. This file records Work-reported reconstruction behavior preserved in the source/exposure ledger. It does not rewrite the historical archive parts.

```yaml
record_id: WORK-ULTRA-FABLE-GF5-STAGE-A-001-STORAGE-ANOMALY-001
storage_task: MNEMOSYNE-152
anomaly_count: 2
stage_A_invalidated: false
semantic_content_inferred_or_rewritten: false
historical_archive_parts_modified: false
```

## RA-001 — GF-STEP-2D binary-part overlap

```yaml
source_id: SRC-011
recoverable: true
storage_boundary_only: true
direct_concatenation_bytes: 22883
expected_archive_bytes: 22882
repair:
  remove_exactly_one_overlapping_boundary_byte: true
result:
  recovered_source_bytes: 68834
  recovered_source_sha256: ebb994bd3d8f4998cbdc7aead17dcc609958a53798f6c8e9d6dd03d8de5893ac
semantic_rewrite: false
```

The first binary part ended with a byte equal to the first byte of part 2. Direct concatenation failed gzip integrity. Removing only the duplicated boundary byte restored the archive and exact predeclared source identity.

## RA-002 — GF-STEP-3B text-part boundary LFs

```yaml
source_id: SRC-026
recoverable: true
storage_boundary_only: true
direct_part_total_bytes: 68037
expected_source_bytes: 68033
repair:
  remove_leading_LF_from_parts:
    - 2
    - 3
    - 4
  remove_trailing_LF_from_part:
    - 5
result:
  recovered_source_bytes: 68033
  recovered_source_sha256: af4dd4c2d9658319462a28cc13c469f24823be06cc003f33858b348a68fb6685
semantic_rewrite: false
```

The indexed UTF-8 parts contained four storage-only line feeds at split boundaries. Removing only those boundary bytes restored the exact predeclared source identity.

## Disposition

- Preserve the original archive parts and historical manifests.
- Do not silently change old indexes in this storage task.
- Future reconstruction guidance must cite this anomaly record or use a verified exact whole-source artifact.
- These anomalies do not authorize broader normalization or semantic repair.
