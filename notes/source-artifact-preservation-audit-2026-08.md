# Source-Artifact Preservation Audit — 2026-08

> Non-execution-source audit and repair basis for MNEMOSYNE-198. This record distinguishes exact stored bytes, reconstructable archives, normalized readable copies and identity-only receipts. It does not retroactively upgrade any artifact's preservation status.

```yaml
audit_id: MNEMOSYNE-SOURCE-ARTIFACT-PRESERVATION-AUDIT-001
task_id: MNEMOSYNE-198
repository: 08822407d/Mnemosyne
pinned_master: ae98f65bc98368f8c56feed76d60ca2b78e20782
audit_date: 2026-08
execution_source_modified: false
historical_files_modified: false
```

## 1. Question audited

The user asked whether later Deep Research files saved locally and supplied to a ChatGPT/Codex workflow could be preserved in the repository at original-file byte level, or whether file transfer through a conversation inherently prevented that.

The answer is **not one universal yes/no**:

- exact preservation is technically possible when the task can access raw file bytes and uses a byte-preserving Git path or a direct/manual repository import;
- several historical workflows did preserve exact staged/exported files;
- several other workflows intentionally stored only a normalized copy or an identity receipt;
- therefore the historical inconsistency came from the selected ingestion workflow and available task surface, not from an inherent rule that every conversation-supplied file must become lossy.

## 2. Current-surface mechanical capability check

### 2.1 Attachment-byte availability

A file attached to the current conversation was directly available to the task runtime as a file and could be read as bytes:

```yaml
observed_attachment:
  runtime_path: /mnt/data/7cb62d17-1aff-4ba0-95c5-934a85604e25.png
  bytes: 44257
  sha256: 21fdb1a59b28aea1bc2d1a6b7d11c6cfe2853d35bd1ea8255245c643716473f1
```

This proves the task could access and hash the exact bytes exposed to the current runtime. It does **not** independently prove those bytes are identical to the user's device copy because no pre-upload user-side hash was supplied.

### 2.2 Byte-preserving Git blob check

A synthetic binary containing NUL, CRLF and non-UTF-8 bytes was uploaded through the available GitHub base64-blob action without adding it to a branch tree:

```yaml
synthetic_blob_test:
  bytes: 33
  sha256: 6ea9544c818b7eddc6cd646e54ee8f9dbe880c89f935148d310b509527deb758
  locally_computed_git_blob_sha1: d5fa72ff52eb9e9fef22dec87699d1c8af4f4afd
  GitHub_returned_blob_sha1: d5fa72ff52eb9e9fef22dec87699d1c8af4f4afd
  result: PASS_EXACT_BYTES_TO_GIT_BLOB
  branch_or_tree_modified: false
```

The matching Git blob SHA proves that the currently available action can preserve arbitrary supplied bytes exactly when they are available to the task and encoded through the byte-preserving path.

The created blob is unreachable from repository branches and may be garbage-collected by GitHub. It is evidence of action capability, not a durable repository artifact.

## 3. Historical preservation findings

### 3.1 Initial seven-report cycle

```yaml
cycle: RC-2026Q2-initial
report_originals_present_in_repository: true
report_formats:
  - TXT
  - PDF
prompt_history:
  Pro_prompt: available
  six_light_research_prompts: initially_missing_later_recovered_by_user_and_ingested
```

The earliest preservation gap principally concerned six light-research **prompt originals**, not the seven report files themselves. `raw/research-reports/current/current-research-prompts.md` records that PROMPT-2026Q2-0002 through -0007 were later recovered and are now available.

The repository contains the original report files. Unless a contemporaneous source-device hash exists, repository presence alone proves the Git-stored bytes, not an independent device-to-repository equality comparison.

### 3.2 DR1 memory testing

```yaml
cycle: RC-2026Q2-memory-testing
prompt_and_report_ingestion: user_staged_files_then_git_mv
preservation_assessment: exact_relative_to_staged_repository_files
```

MNEMOSYNE-040 found the user-added prompt and report files and moved them to canonical paths with `git mv`; the task diff recorded the moves as zero-line-content changes. This preserved their staged bytes while changing paths.

### 3.3 DR2 handoff strategy

```yaml
cycle: RC-2026Q2-handoff-strategy
prompt_and_report_ingestion: manual_import_inbox_then_git_move
preservation_assessment: exact_relative_to_manual_import_files
```

MNEMOSYNE-051 moved the complete prompt and report from `manual-import-inbox/` to canonical cycle paths. The zero-line rename entries support byte-preserving relocation.

### 3.4 DR4 user-input governance

```yaml
cycle: RC-2026Q2-user-input-governance
report_ingestion: manual_import_inbox_then_move_by_MNEMOSYNE_058
prompt_ingestion: manual_import_inbox_then_move_by_MNEMOSYNE_059
preservation_assessment: exact_relative_to_manual_import_files
```

The report and corrected prompt were processed in two tasks but moved from the user-staged inbox rather than recreated from copied prose.

### 3.5 DR5 first-target dry-run evaluation

```yaml
cycle: RC-2026Q2-first-target-dry-run-evaluation
report_and_prompt_ingestion: manual_import_inbox_then_git_move
preservation_assessment: exact_relative_to_manual_import_files
```

MNEMOSYNE-066 moved the full report and prompt original to canonical cycle locations with zero-content-change rename entries.

### 3.6 DR6 platform/context/apps delta

```yaml
cycle: RC-2026Q3-platform-context-apps-delta
source_report_bytes: 46635
source_sha256: ea38e5db121d18af55533c8f8671c150ad401b5c9dfa3c3b81bc9b905dde8d06
storage_mode: ordered_lossless_UTF8_chunks
preservation_assessment: exact_reconstructable_report_content
```

The report's repository manifest identifies six ordered chunks and states reconstruction by concatenation without added separators. This is a reconstructable exact UTF-8-content representation rather than a single original file blob.

### 3.7 Four-topic Pro Deep Research batch

```yaml
cycle: RC-2026Q3-target-memory-governance-and-learning
reports: 4
prompt_originals: 4
archive_format: tar.bz2
archive_bytes: 56573
archive_sha256: f46cf54b923c00e86d8e539a290f76312ed287742ee9b713f9167db03e3cbd24
preservation_assessment: exact_reconstructable_archive
```

The repaired exact archive has an eight-logical-part/18-physical-file manifest and per-member byte counts and SHA-256 values. It is the strongest exact-preservation example in the current repository, though its multipart complexity also produced a repair burden.

### 3.8 Multi-model adjudication/provenance reports

```yaml
cycle: RC-2026Q3-multi-model-adjudication-provenance
reports_received: 2
raw_body_storage: false
stored_evidence:
  - filenames
  - byte_counts
  - sha256
  - review_and_comparison_records
preservation_assessment: identity_receipt_only
```

The cycle manifest explicitly says the raw bodies were not embedded because a reliable large-file upload channel was unavailable in that storage task. Exact report bytes cannot be reconstructed from the repository.

### 3.9 Adaptive Explanation Stage A

```yaml
cycle: RC-2026Q3-adaptive-explanation-stage-a
received_report_bytes: 64304
received_report_sha256: a4d38a426cf1ba5a371a7ad19ae7b8fee16ae33dc539f5bb329066bf4edeca6f
repository_copy: normalized_readable_copy
exact_received_file_reconstructable: false
preservation_assessment: normalized_readable_copy_plus_identity_receipt
```

The manifest deliberately avoids claiming byte-for-byte identity. A failed exact-archive attempt was removed rather than leaving an unverified archive.

### 3.10 Frontier planning and clarification handoff reports

```yaml
cycle: RC-2026Q3-frontier-planning-clarification-handoff
reports:
  - Pro
  - Fable
stored_evidence:
  - exact_supplied_filename
  - byte_count
  - sha256
  - report_receipt
  - review_and_adjudication
exact_report_bytes_reconstructable: false
preservation_assessment: identity_receipt_only
```

The cycle manifest explicitly states that the exact uploaded report bytes are not reconstructable from the repository.

## 4. Historical conclusion

```yaml
historical_conclusion:
  all_later_forwarded_files_were_lossy: false
  all_later_forwarded_files_were_exactly_preserved: false
  preservation_varied_by_ingestion_workflow: true
```

The user's manual repository-import method is reliable for preserving exact files when the task subsequently uses byte-preserving moves. It is **not required in every future case** if the conversation can access raw attachment bytes and a byte-preserving Git blob/file path is available and mechanically verified.

Use manual import when exact bytes are not exposed to the task, the file is too large or unsuitable for the current action, the write interface is text-only, or exact preservation cannot be proven.

## 5. Recommended future operating rule

For every material research/task/conversation-export artifact:

1. decide whether exact preservation is necessary;
2. perform repository/material safety preflight;
3. hash the file before transformation when raw bytes are accessible;
4. preserve it as a direct exact blob/file or verified reconstructable archive;
5. otherwise use manual import or an approved outside-Git exact store;
6. record one explicit preservation level;
7. keep readable normalization and exact source as separate roles;
8. treat originals as cold/on-demand evidence, not default runtime context.

## 6. Files and records used in this audit

```text
current/deep-research-report-delivery-correction-guard.md
current/run-context-and-pr-provenance-guard.md
raw/research-reports/current/research-report-index.md
raw/research-reports/current/current-research-prompts.md
raw/research-reports/cycles/2026Q3-target-memory-governance-and-learning/exact-archive/manifest.json
raw/research-reports/cycles/2026Q3-platform-context-apps-delta/originals/DR6_2026Q3_platform_memory_apps_capability_delta_report.md
raw/research-reports/cycles/2026Q3-multi-model-adjudication-provenance/manifest.yaml
raw/research-reports/cycles/2026Q3-adaptive-explanation-stage-a/manifest.md
raw/research-reports/cycles/2026Q3-frontier-planning-clarification-handoff/manifest.md
notes/codex-task-results/MNEMOSYNE-040-result.md
notes/codex-task-results/MNEMOSYNE-051-result.md
notes/codex-task-results/MNEMOSYNE-058-result.md
notes/codex-task-results/MNEMOSYNE-059-result.md
notes/codex-task-results/MNEMOSYNE-066-result.md
```

## 7. Boundaries

- This audit does not certify every file in every research cycle.
- It does not reconstruct missing report bodies.
- It does not prove a ChatGPT attachment is identical to a user's local source without an independent local hash/comparison.
- It does not require exact Git storage for sensitive material that belongs outside the public repository.
- It does not make research reports execution source or default runtime input.
