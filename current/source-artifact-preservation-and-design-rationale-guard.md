# Source Artifact Preservation and Design-Rationale Guard

> User-approved Mnemosyne behavior guard for preserving irreplaceable source artifacts and recording compact, externally stated engineering rationale. This file is not a standalone execution source; `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
guard_id: MNEMOSYNE-SOURCE-ARTIFACT-PRESERVATION-RATIONALE-001
created_by_task: MNEMOSYNE-198
last_amended_by_task: MNEMOSYNE-203
status: active_after_MNEMOSYNE_203_merge
execution_source: current/human-approved-spec.md
execution_source_modified: false
amendment_source:
  - notes/proposed-active-guidance-amendments-from-or01-v0.1.md
  - notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001.md
scope_precedence:
  controls_specifically:
    - source_artifact_preservation_claims
    - exact_vs_normalized_copy_semantics
    - byte_change_vs_substantive_content_change_semantics
    - externally_stated_design_rationale_capture
    - default_on_demand_reading_of_cold_originals
  complements:
    - current/artifact-delivery-and-direct-generation-guard.md
    - current/deep-research-report-delivery-correction-guard.md
    - current/run-context-and-pr-provenance-guard.md
    - notes/object-templates-and-id-rules.md
```

## 1. Purpose

Mnemosyne cannot depend on the human user remembering every preservation or provenance step during long-running design work. Important conversations and tasks must themselves know when to preserve the source material that future redesign, migration, dispute review or stronger-model re-analysis may require.

This guard addresses five distinct problems:

1. an uploaded research report, task file, conversation export or other source artifact may be summarized or normalized without preserving the exact supplied file;
2. a repository record may call a readable copy an “original” even when byte identity was not proved;
3. a byte-level transformation such as line-ending or encoding normalization may be described imprecisely as a substantive content rewrite, or substantive equivalence may be assumed without review;
4. important design choices may survive only as final rules, scattered dialogue or model output, without a compact record of the problem, alternatives and selection reason;
5. preserving source material may be misread as requiring every ordinary task to load and analyze large historical files.

The intended result is **preserve first, read on demand**: irreplaceable source material remains recoverable, while normal runtime work uses the smallest relevant current working set.

## 2. Material source artifacts

A source artifact is material when losing its supplied form would materially weaken later recovery, review, redesign, migration or dispute resolution. Candidate classes include:

- complete user-exported conversation files used as project-origin or evaluation evidence;
- complete task or research prompts whose exact framing materially affected the result;
- operator-exported Deep Research reports;
- complete reports or conversation exports from Fable or another external model;
- externally supplied specifications, requirements, source documents or datasets that cannot be regenerated reliably;
- important model/task outputs whose complete wording is needed for later comparison;
- migration inputs, acceptance baselines and evidence-bearing manifests.

Not every temporary reply, generated summary, status note, duplicate export or replaceable derivative requires exact preservation. The task must apply proportionality and state why a source is material when that is not obvious.

## 3. Preservation-level vocabulary

Every material source artifact stored or referenced by a Mnemosyne task must use one honest preservation level:

```yaml
preservation_level:
  - EXACT_FILE_IN_REPOSITORY
  - EXACT_RECONSTRUCTABLE_ARCHIVE
  - EXACT_FILE_OUTSIDE_REPOSITORY_WITH_VERIFIED_POINTER
  - NORMALIZED_READABLE_COPY
  - IDENTITY_RECEIPT_ONLY
  - EXCERPT_OR_SUMMARY_ONLY
  - SOURCE_UNAVAILABLE
```

Meanings:

- `EXACT_FILE_IN_REPOSITORY`: the repository blob contains the exact bytes received by the task, verified by byte count and SHA-256.
- `EXACT_RECONSTRUCTABLE_ARCHIVE`: the repository contains all ordered parts plus a verified reconstruction procedure and hashes that reproduce the exact received bytes.
- `EXACT_FILE_OUTSIDE_REPOSITORY_WITH_VERIFIED_POINTER`: exact bytes remain in an approved external location; the repository stores a safe, tested pointer and identity receipt.
- `NORMALIZED_READABLE_COPY`: substantive content is available, but encoding, line endings, wrapping, container format or other bytes may differ.
- `IDENTITY_RECEIPT_ONLY`: filename, size, hash and review result are recorded, but the body cannot be reconstructed from the repository.
- `EXCERPT_OR_SUMMARY_ONLY`: only selected or derived content is preserved.
- `SOURCE_UNAVAILABLE`: the source could not be obtained or verified.

A lower level must never be described as a higher one. The unqualified words `original`, `exact copy`, `lossless`, `byte-identical` and `fully reconstructable` are prohibited unless mechanically proved for the stated artifact.

## 3A. Byte identity and substantive-content transformation assessment

When a stored or delivered derivative differs from the received source, assess byte identity and substantive content separately rather than collapsing both into the word “modified.”

Use this record when the distinction is material:

```yaml
source_transformation_assessment:
  byte_identity:
    status: unchanged | changed | unknown
    evidence_refs: []
  transformation_class:
    exact_move_or_rename |
    line_ending_normalization |
    encoding_normalization |
    wrapping_or_container_normalization |
    substantive_content_edit |
    mixed |
    unknown
  substantive_content:
    status: unchanged_as_reviewed | changed | not_fully_reviewed | unknown
    review_scope:
  preservation_level_before:
  preservation_level_after:
  exact_received_source_retained_separately: true | false | not_applicable
  limitations: []
```

Rules:

1. Do not use an unqualified statement such as “the content was modified” when the only established fact is a byte-level normalization.
2. Prefer precise wording such as: “Bytes changed because line endings or encoding were normalized; no substantive-content change was found within the stated review scope.”
3. `substantive_content.status: unchanged_as_reviewed` does not restore exact byte identity and does not permit an exact-preservation claim for the derivative.
4. If substantive equivalence was not reviewed, use `not_fully_reviewed`; do not infer equivalence merely from the stated transformation command or expected tool behavior.
5. Preserve the exact received source separately when it is material, safe, authorized, proportionate and feasible.
6. An exact move or rename may preserve bytes even though the repository path changes; record both identities and paths when needed.
7. Mixed transformations must disclose both normalization and substantive edits rather than choosing the less consequential label.
8. No new preservation level is created by this assessment. `NORMALIZED_READABLE_COPY` remains the appropriate level for a normalized derivative whose bytes differ from the received source.

## 4. Exact attachment-intake rule

When the user supplies a material file to a ChatGPT/Codex/Agent task and repository storage is safe and authorized, the task should preserve the exact bytes exposed to that task when an available write path supports it.

Minimum receipt:

```yaml
source_artifact_receipt:
  artifact_id:
  source_attachment_or_file_ref:
  operator_filename:
  media_type_or_extension:
  bytes:
  sha256:
  preservation_level:
  repository_or_external_path:
  repository_blob_or_archive_identity:
  byte_identity_verified: true | false
  source_device_identity_verified: true | false | unknown
  content_review_scope:
  sensitivity_and_storage_preflight_ref:
  limitations: []
```

Rules:

1. Hash the supplied file before normalization, parsing, rewrapping, newline conversion or renaming when raw bytes are available.
2. Prefer a direct exact file/blob over a custom Base64 multipart archive when the available surface supports direct byte-preserving storage.
3. For arbitrary binary content, use a byte-preserving/base64 blob path or a manual repository import; do not route it through a UTF-8-only text update and then claim exactness.
4. Renaming or `git mv` does not change file bytes; record the old and new paths when manual import is used.
5. A hash of the file exposed to the task proves identity only for that observed task input. Equality with the user's device copy requires a user-side pre-upload hash or an independent post-transfer comparison.
6. If the attachment preview, parsed text or OCR view conflicts with the directly accessible file, use the directly read file for artifact identity and record the preview conflict.
7. If raw attachment bytes are unavailable, do not infer them from extracted text. Use `NORMALIZED_READABLE_COPY`, `IDENTITY_RECEIPT_ONLY` or another accurate level.

## 5. Manual-import fallback

Use `manual-import-inbox/` or another user-approved direct repository/file-transfer path when:

- the conversation can read extracted text but cannot access the exact file bytes;
- the current GitHub write surface cannot preserve the file type or size safely;
- exact repository upload cannot be mechanically verified;
- the user already has the authoritative local export and prefers direct Git preservation;
- a binary or large file should not be reconstructed through long chat content.

The receiving task must inventory the staged file, perform the repository/material safety preflight, compute or verify identity, move or copy it to its canonical path without rewriting it, and record the preservation level. Manual import is a fallback, not a universal requirement when exact attachment-to-blob transfer is already available and verified.

## 6. Deep Research and external-model outputs

The Deep Research-specific single-report semantics remain controlled by `current/deep-research-report-delivery-correction-guard.md`.

Additional preservation rules:

- the product final-report surface contains one canonical substantive report;
- an operator-exported Markdown/Word/PDF file is a representation/export of that report, not a second conclusion;
- when the operator supplies the export file, Mnemosyne may preserve that exact exported file and must identify it as the exact export received;
- preserving the exact export does not prove byte identity with an unobserved internal product representation;
- a report body copied or normalized into another Markdown file is not automatically the exact operator export;
- prompt originals and report exports have separate identities and roles;
- wrong-topic or incomplete research is not repaired by exact preservation.

The same distinction applies to Fable and other external-model conversation/report exports: preserve the supplied file exactly when appropriate, but do not claim more about the provider's internal representation or hidden backend than the evidence supports.

## 7. Cold-source reading boundary

Preservation does not imply routine loading.

Material originals normally have:

```yaml
runtime_reading_profile:
  default: DO_NOT_READ
  access: ON_DEMAND
```

Ordinary target-Agent or business work should not load complete Mnemosyne construction conversations, old handoffs, completed task records, research prompts, full research reports or project-origin raw files merely because they exist.

Read a cold source only when a task-specific trigger applies, such as:

- reconstructing or disputing original intent;
- checking whether a summary or current rule distorted its source;
- designing or validating a migration;
- reviewing a high-impact design change;
- investigating an incident, contradiction or missing dependency;
- reproducing a research result or citation;
- performing a separately authorized full-history or cross-conversation evaluation.

Use current truth, compact manifests, summaries and source maps first. The task should state which cold originals were actually read; repository existence alone is not evidence that a source influenced the result.

## 8. Compact design-rationale record

Important engineering work must preserve an **externally stated rationale**, not private hidden chain-of-thought.

A rationale is required when a task materially:

- selects or changes architecture, schema, methodology or reusable behavior guidance;
- changes execution source, authority, privacy, trust, storage or migration boundaries;
- chooses among competing designs whose trade-offs matter later;
- rejects or defers a plausible high-impact alternative;
- creates a task/research framing likely to guide substantial later work;
- decides whether an upper-level Mnemosyne/Meta-Agent change affects existing target-system work.

It is normally unnecessary for exact-byte moves, formatting, typo repair, mechanical inventories or implementation of a fully frozen low-risk specification.

Minimum record:

```yaml
design_rationale:
  rationale_id:
  design_or_decision_ref:
  source_conversation_task_and_artifact_refs: []
  problem_and_user_goal:
  fixed_constraints: []
  assumptions_and_unknowns: []
  alternatives_considered:
    - option:
      material_advantages: []
      material_disadvantages: []
      evidence_refs: []
  selected_option:
  selection_reason:
  rejected_or_deferred_options:
    - option:
      reason:
  expected_effects: []
  known_risks: []
  validation_or_falsification_plan:
  affected_existing_artifacts_or_targets: []
  migration_rebuild_or_compatibility_implication:
  owner_decision_ref:
  reviewer_and_independence_limitations: []
```

The user-facing explanation should normally present this in concise natural language. Do not paste a large English-key YAML block into ordinary chat merely because the repository record uses a schema.

## 9. Rationale quality and limits

- Cite or point to the user wording, task, evidence and alternatives that actually influenced the choice.
- Separate verified facts, user values, model interpretation and engineering judgment.
- Record meaningful alternatives only; do not manufacture rejected options after the fact to make a decision appear more rigorous.
- `selection_reason` should explain the decisive trade-off, not merely restate the chosen option.
- State assumptions and unknowns that could invalidate the design.
- Record expected effects and falsification/validation conditions so later real-use evidence can challenge the choice.
- Do not require or claim private chain-of-thought, hidden scratchpad, token-by-token reasoning or unavailable internal model state.
- A rationale record is non-execution-source evidence unless and until an approved execution source incorporates the resulting rule.

## 10. Historical backfill

Do not backfill every historical task.

Backfill is appropriate only when:

- an active execution rule is being reviewed or changed;
- a historical design is about to be used in a real target;
- a conflict, migration or incident requires the original reasoning;
- a high-impact decision lacks enough explanation for reliable review;
- the user separately selects a bounded archival reconstruction task.

When backfilling, preserve uncertainty and point to the original conversation/task/report. Do not present a later model's reconstruction as the historical actor's exact reasoning.

## 11. Verification before preservation claims

Before claiming exact preservation, verify as applicable:

- exact received/staged byte count and SHA-256;
- repository blob or reconstructable archive identity;
- reconstruction output hash for multipart archives;
- original path is absent only after a verified move when relocation is intended;
- readable derivative and exact original are labelled separately;
- no unsafe material entered a public or unverified repository;
- byte identity and substantive-content status are stated separately when normalization or editing occurred;
- the result record names the preservation level and limitations.

A Git blob hash, SHA-256 or reconstruction test proves bytes only. It does not prove correctness, report quality, source authenticity, producer identity or hidden model identity.

## 12. Boundaries

This guard does not:

- authorize repository writes, manual upload, research execution, quota use or connector activation;
- require every chat reply, temporary file or derivative to be preserved;
- require all preserved originals to be loaded by future tasks;
- make raw material an execution source;
- move private material into public Git;
- promise that ChatGPT's internal storage representation is byte-identical to a user's local file without comparison evidence;
- treat byte-level normalization as a substantive edit or substantive equivalence as proof of exact preservation;
- require full historical rationale reconstruction;
- replace task-local privacy, authority, versioning, migration, review or rollback decisions.
