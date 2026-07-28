# Four-Topic Pro Deep Research — Post-Merge Storage Integrity Repair

> Non-execution-source repair record. It repairs storage and live-wayfinding defects after PR #216; it does not change report interpretations, execution source, user decisions or target-project state.

```yaml
repair_id: MNEMOSYNE-165-POST-MERGE-STORAGE-REPAIR-001
repair_task: MNEMOSYNE-166
source_task: MNEMOSYNE-165
source_PR: 216
source_merge_commit: a66d92c572f178de52e3b3b238324decf279b7fb
status: repaired_on_follow_up_revision
execution_source_modified: false
```

## Defects found

PR #216 merged a manifest and README that declared an eight-part exact archive, but the changed-path set contained only logical part files 1 through 6. Logical parts 7 and 8 were absent.

Independent deterministic regeneration also showed that the merged logical part 5 did not match the manifest-governed Base64 stream. Its Git blob SHA was not the expected identity for regenerated logical part 5. Therefore the repository could not reconstruct the declared archive after merge even if only the missing final files had been added.

```yaml
archive_defects:
  logical_part_005:
    state: content_mismatch
    expected_unwrapped_chars: 10000
    expected_unwrapped_sha256: 6ae53fdae639053fa5893b885da4c76f8cf11e3c66074478fb8ef59043297468
  logical_part_007:
    state: missing
    expected_unwrapped_chars: 10000
    expected_unwrapped_sha256: cf9f696f14cd8fea48f19c8a74e5baa55f7f14b80657187ab33c6baf04cda295
  logical_part_008:
    state: missing
    expected_unwrapped_chars: 5432
    expected_unwrapped_sha256: b5ec7860ddf620b1d91ec47c5924dad1475713cd7ce27761d9e8027709b30b24
```

The cycle README also pointed to the following cycle-local files that were not created:

```text
review-records/MNEMOSYNE-165-four-topic-maintainer-review.md
review-records/MNEMOSYNE-165-deep-research-execution-incident-ledger.md
source-manifest.md
evidence-ledger.md
decision-preparation-v0.1.md
```

The actual canonical derived records were created under:

```text
notes/research-batch-reviews/2026-07-27-four-topic-pro-deep-research/
```

The live batch status also still described PR #216 as pending merge.

## Exact archive regeneration

The archive was independently regenerated from the eight exact local inputs recorded in `manifest.json` using deterministic tar metadata:

```yaml
format: PAX_tar_then_bzip2_level_9_then_base64
file_order: manifest_member_order
file_mode: 0644
uid: 0
gid: 0
uname: empty
gname: empty
mtime: 0
directory_entries: none
```

Mechanical receipt:

```yaml
regenerated_tar:
  bytes: 235520
  sha256: b63b62b2a397c31bff6a57aeefec6b0cccdd1a477e93550435bb34b75f2a8168
regenerated_tar_bz2:
  bytes: 56573
  sha256: f46cf54b923c00e86d8e539a290f76312ed287742ee9b713f9167db03e3cbd24
regenerated_base64:
  chars_after_removing_CR_LF: 75432
  sha256: bdb9292b9626afd3e76aa3a6f79086f92c0296309e4231f623d515fa92000138
manifest_identity_match: pass
```

Logical parts 1–4 and 6 matched their regenerated Git-blob identities. Logical part 5 was replaced by small physical segments, each independently checked against its expected Git blob SHA. Logical parts 7 and 8 were restored and their wrapped Git blob SHAs checked.

```yaml
logical_part_005_storage:
  physical_segment_count: 11
  verified_segment_blob_SHAs:
    segment_001: fa4358b70e4cb9bd82eb1a448bc014e948c6f7ea
    segment_002: 2c375f16c312256ff313e54b82e907b29b6c4aff
    segment_003: 3f49b48ed784f9205d6868b602c518b3cc082c4b
    segment_004: b8471f336bc6905d3b0e22067afce25ff5f5a675
    segment_005: a5c408e6d51c945f9f21f544c21843e2b188cd61
    segment_006: 921331ee844405c3bd880b935f4ee6e5d80df8e7
    segment_007a: f38194a3005bb859cda13ecce9ca5b88a2200375
    segment_007b: 2f04cb2d11f217d1142720566b964ff33f169bba
    segment_008: 89291a58403ceb772d94cbed3b9105408c472346
    segment_009: 02a5ced4bf0cf7515d784eacee80049b866f8739
    segment_010: 428e0b8103adbf4ecd77bb9a870b6cdaeafce423
logical_part_007_wrapped_blob_SHA: 0bbad5e3b569e81cfa0a47654130be7b70dda544
logical_part_008_wrapped_blob_SHA: a7ca34ee2d38ede17883e208f8f8e5b7ca544c5f
```

Line wrapping and the physical segmentation of logical part 5 are non-semantic because reconstruction concatenates files in lexical order and removes CR/LF before Base64 decoding.

## Repairs applied

```yaml
removed:
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-005-of-008.txt
added:
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-005-of-008-segment-001-of-010.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-005-of-008-segment-002-of-010.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-005-of-008-segment-003-of-010.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-005-of-008-segment-004-of-010.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-005-of-008-segment-005-of-010.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-005-of-008-segment-006-of-010.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-005-of-008-segment-007a-of-010.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-005-of-008-segment-007b-of-010.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-005-of-008-segment-008-of-010.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-005-of-008-segment-009-of-010.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-005-of-008-segment-010-of-010.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-007-of-008.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-008-of-008.txt
updated:
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/manifest.json
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/README.md
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/README.md
  - current/pro-deep-research-four-topic-batch-status.md
```

The README repair points to the actual canonical derived records instead of inventing duplicate cycle-local paths.

## Conversation-retention boundary

The exact accepted prompt/report bytes and maintainer interpretations are recoverable after this repair. The original four Deep Research conversations are no longer required as active working contexts for the selected minimum-upgrade-contract route.

They can still contain product-native evidence that is not fully portable in exported Markdown:

- source-panel ordering and conversation-local citation resolution;
- Activity/plan history;
- operator-visible mode and timing observations;
- original product error state.

Therefore the safe disposition is:

```yaml
original_research_conversations:
  may_archive_in_product_UI: true
  may_delete_permanently_now: false_recommended
  routine_next_route_dependency: none
  exceptional_future_use:
    - citation_portability_repair
    - source_panel_audit
    - product_incident_review
```

## Boundary

- Historical MNEMOSYNE-165 result and report bytes are not rewritten.
- The repair does not alter evidence dispositions.
- No research report becomes execution source.
- No target project is selected or modified.
- No implementation, automatic migration, cross-Agent sharing or learner profiling is authorized.
