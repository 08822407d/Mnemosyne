# Four-Topic Pro Deep Research — Post-Merge Storage Integrity Repair

> Non-execution-source repair record. It repairs storage and live-wayfinding defects after PR #216; it does not change report interpretations, execution source, user decisions or target-project state.

```yaml
repair_id: MNEMOSYNE-165-POST-MERGE-STORAGE-REPAIR-001
repair_task: MNEMOSYNE-166
source_task: MNEMOSYNE-165
source_PR: 216
source_merge_commit: a66d92c572f178de52e3b3b238324decf279b7fb
status: repaired_on_follow_up_branch_pending_human_merge
execution_source_modified: false
```

## Defects found

PR #216 merged a manifest and README that declared an eight-part exact archive, but the changed-path set contained only:

```text
part-001-of-008.txt
...
part-006-of-008.txt
```

`part-007-of-008.txt` and `part-008-of-008.txt` were absent. Therefore the repository could not reconstruct the declared archive after merge.

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

The regenerated first six 10,000-character parts matched the existing archive payload. The missing final payload was added as parts 7 and 8. Line wrapping inside part files is non-semantic because reconstruction removes CR/LF before Base64 decoding.

## Repairs applied

```yaml
added:
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-007-of-008.txt
  - raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/parts/part-008-of-008.txt
updated:
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
