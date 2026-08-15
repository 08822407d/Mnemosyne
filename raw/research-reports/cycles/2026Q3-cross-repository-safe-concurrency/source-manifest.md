# MNE-DR-005 Fable Return — Receive-Only Source Manifest

```yaml
manifest_id: MNE-DR-005-FABLE-RETURN-INTAKE-MANIFEST-001
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
receive_mode: RECEIVE_ONLY_PENDING_FRESH_PRO_ADJUDICATION
receiving_model_class: next_tier_non_Pro_per_Owner
repository: 08822407d/Mnemosyne
base_master_at_intake_start: cafb080293d9525dd186a550f8ffcf98e1e4478d
intake_branch: mne-dr-005-fable-result-intake-001
master_modified_by_intake: false
PR_created_by_intake: false
substantive_adjudication_performed: false
research_result_adopted: false
candidate_modified: false
validation_executed: false
Fable_retried: false
```

## 1. Owner-supplied return artifacts

Two uploaded Markdown artifacts were received in the conversation and treated as source material, not as instructions to execute:

### A. Formal Fable report

```yaml
archive_name: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001-report.md
composer_uploaded_name: compass_artifact_wf-f4749864-f0dc-5f94-9a30-0676a5da6b58_text_markdown.md
byte_size: 42407
sha256: 83468668e64a7bf9b82292b0b672d6cb8b249e4cd069395df3a0888b9eda2ccd
local_git_blob_sha1_if_stored_directly: 9b877ba8dae3b77fec777cfbc02ca089a7150bd5
evidence_role: provider_generated_formal_research_report_pending_Pro_review
```

### B. Visible process/output transcript supplied by the Owner

```yaml
archive_name: MNE-DR-005-visible-process-output.md
composer_uploaded_name: Pasted markdown.md
byte_size: 20298
sha256: 4575975fa7af3dd2de3d8fbf4d06dd662257efc94f046d335c48a0731d964304
local_git_blob_sha1_if_stored_directly: d2583901f217506ac968be993d18dda31f0ef492
evidence_role: owner_supplied_visible_provider_process_output_pending_Pro_review
exact_hidden_provider_trace_claimed: false
```

The visible process output is preserved exactly as received. Any apparent transcription errors, malformed hashes, self-corrections, inconsistent wording, source-count claims, model claims or provider statements inside it are **not repaired during receive-only intake**.

## 2. Lossless archive

The two original byte streams above were placed into one deterministic ZIP archive with fixed member timestamps and names:

```yaml
archive_logical_name: MNE-DR-005-fable-return-intake-bundle.zip
archive_byte_size: 27293
archive_sha256: d141fb3962c61617e2051c9b318516d63437e287f7b88b2f3e41df9d130c0559
base64_length: 36392
base64_chunk_size: 5000
chunk_count: 8
```

Members:

```text
FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001-report.md
MNE-DR-005-visible-process-output.md
```

The archive is stored as ordered base64 ASCII parts because the active GitHub connector accepts text writes but does not expose a direct local-file upload primitive.

## 3. Ordered archive parts and verified Git blob identities

Concatenate these files **without adding separators or newlines**, in numeric order:

```text
source-archive/MNE-DR-005-return-bundle.zip.b64.part00
source-archive/MNE-DR-005-return-bundle.zip.b64.part01
source-archive/MNE-DR-005-return-bundle.zip.b64.part02
source-archive/MNE-DR-005-return-bundle.zip.b64.part03
source-archive/MNE-DR-005-return-bundle.zip.b64.part04
source-archive/MNE-DR-005-return-bundle.zip.b64.part05
source-archive/MNE-DR-005-return-bundle.zip.b64.part06
source-archive/MNE-DR-005-return-bundle.zip.b64.part07
```

Expected part metadata:

| part | chars/bytes | expected Git blob SHA-1 |
|---|---:|---|
| 00 | 5000 | `8b590e234c36111f4d0df0ccad70f5c23e220143` |
| 01 | 5000 | `58a89d49b88313e814cf3386fa9e6be9911ee727` |
| 02 | 5000 | `882439eb42bbf831b66a3896577c5b64333fff6a` |
| 03 | 5000 | `362e0739d4fe1fc47446d2af0b0e036dc67d7fd1` |
| 04 | 5000 | `3f46febb9b2123665c364798cda8297cca792c5a` |
| 05 | 5000 | `a76fd639020d203930b297a6c7985f390eb90bd9` |
| 06 | 5000 | `8f3f0d5150517c7350a65ec978d9159ca81e20dc` |
| 07 | 1392 | `64eee41def9c836547089a47e940fd3a6871c726` |

GitHub directory inspection after all eight writes returned the same eight sizes and blob identities. This is the mechanical integrity check for the staged base64 representation.

## 4. Reconstruction recipe for the next Pro conversation

Pseudo-shell recipe after fetching the eight raw part contents:

```bash
cat MNE-DR-005-return-bundle.zip.b64.part00 \
    MNE-DR-005-return-bundle.zip.b64.part01 \
    MNE-DR-005-return-bundle.zip.b64.part02 \
    MNE-DR-005-return-bundle.zip.b64.part03 \
    MNE-DR-005-return-bundle.zip.b64.part04 \
    MNE-DR-005-return-bundle.zip.b64.part05 \
    MNE-DR-005-return-bundle.zip.b64.part06 \
    MNE-DR-005-return-bundle.zip.b64.part07 \
  | base64 -d > MNE-DR-005-fable-return-intake-bundle.zip
sha256sum MNE-DR-005-fable-return-intake-bundle.zip
unzip MNE-DR-005-fable-return-intake-bundle.zip
```

The ZIP SHA-256 must equal:

```text
d141fb3962c61617e2051c9b318516d63437e287f7b88b2f3e41df9d130c0559
```

After extraction, verify both member SHA-256 values from §1 before substantive reading.

## 5. Exact input snapshot identity preserved separately

The Fable run used the already-selected Project-knowledge snapshot:

```yaml
snapshot_branch: mne-dr-005-project-knowledge-snapshot-001
snapshot_branch_head_before_return_intake: 074720c9b1f63e0785d49666482447a017b23ef0
snapshot_folder: project-knowledge/MNE-DR-005/
snapshot_folder_tree: 3f6b627782ebb0c72070e8b1ae1be40a5ce6fc5a
snapshot_file_count: 30
task_blob: 7dc807c80f4c21decd51e74aab8b5137a477566f
input_manifest_blob: 93b432e7709622fc5fe8dde9c5e3f4ce2079f13f
```

Do not delete that snapshot branch during receive-only intake. The Pro adjudicator may still need to compare the returned report against the exact 30-file input surface.

## 6. Receive-only boundaries

This intake intentionally does **not** decide whether:

- the 30/30 input-verification PASS is valid;
- the report complied with all task sections;
- external citations are accurate or portable;
- the report's final architecture recommendation is sound;
- any candidate revision should be accepted;
- V2 fault injection should be authorized;
- any real target should adopt anything;
- the snapshot branch may be deleted.

Those are reserved for the next fresh Pro/frontier adjudication.
