# Cross-Model Review Results

This directory stores non-execution-source heterogeneous model review artifacts and maintainer triage records for Mnemosyne.

These artifacts may include review prompts, access reports, project-understanding notes, formal review results, finding indexes, maintainer triage records, and ingestion summaries.

They are not execution source. They do not approve repository edits, target workspace creation, target material ingestion, target repository write, regression formalization, operational build, or execution-source updates.

Findings become actionable only after maintainer/user validation and, if needed, a separately approved task number.

## Current review rounds

- `FABLE5-REVIEW-001/` — post-079 to post-085 handoff authority and state-machine review.
- `FABLE5-REVIEW-002/` — regression-candidate and warning-closure traceability review.
- `FABLE5-REVIEW-003/` — post-repair snapshot refresh and portable continuation delta review after MNEMOSYNE-088/089/090/091.

## Ingestion status convention

```yaml
status_values:
  received_in_chat_not_canonical: file was received in a maintenance conversation but not yet copied verbatim here
  canonical_copy_stored: file has been copied here verbatim or with documented normalization
  triaged: maintainer triage record exists
  repair_candidates_routed: accepted repair candidates have been routed to user-approved tasks or explicitly deferred
```
