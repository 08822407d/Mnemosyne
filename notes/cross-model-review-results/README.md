# Cross-Model Review Results

This directory stores non-execution-source heterogeneous model review artifacts and maintainer triage records for Mnemosyne.

These artifacts may include review prompts, access reports, project-understanding notes, formal review results, finding indexes, maintainer triage records, and ingestion summaries.

They are not execution source. They do not approve repository edits, target workspace creation, target material ingestion, target repository write, regression formalization, operational build, or execution-source updates.

Findings become actionable only after maintainer/user validation and, if needed, a separately approved task number.

## Current review rounds

- `FABLE5-REVIEW-001/` — post-079 to post-085 handoff authority and state-machine review.
- `FABLE5-REVIEW-002/` — regression-candidate and warning-closure traceability review.
- `FABLE5-REVIEW-003/` — post-repair snapshot refresh and portable continuation delta review after MNEMOSYNE-088/089/090/091.

## Follow-up triage records

- `FABLE5-TRIAGE-001/` — Fable response after user answers to earlier review questions; closes several question items, raises Q2-2 warning-layer tracing to high priority, and leaves R3 hygiene cleanup unapproved pending re-check / user decision. MNEMOSYNE-096 adds partial raw preservation under `FABLE5-TRIAGE-001/raw/`; see its manifest for unavailable or not-fully-embedded source materials.

## Follow-up evidence audits

- `FABLE5-TRIAGE-001/evidence-audits/MNEMOSYNE-097-q2-2-r3-readonly-audit.md` — read-only evidence table for Q2-2 warning-layer source/model/latest-version tracing and R3 hygiene fresh-snapshot recheck. It does not select a canonical warning layer or approve cleanup.

## Ingestion status convention

```yaml
status_values:
  received_in_chat_not_canonical: file was received in a maintenance conversation but not yet copied verbatim here
  canonical_copy_stored: file has been copied here verbatim or with documented normalization
  canonical_summary_stored: non-verbatim summary has been stored with documented provenance
  raw_originals_partially_preserved: available originals and transfer metadata are stored, but some original materials are unavailable or not fully embedded
  read_only_evidence_audit_stored: an evidence table or recheck record is stored without repair/writeback authority
  triaged: maintainer triage record exists
  repair_candidates_routed: accepted repair candidates have been routed to user-approved tasks or explicitly deferred
```
