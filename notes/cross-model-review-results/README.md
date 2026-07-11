# Cross-Model Review Results

This directory stores non-execution-source heterogeneous model review artifacts, contrastive design tracks, maintainer triage records, evidence audits, and review packages for Mnemosyne.

These artifacts may include review prompts, access reports, project-understanding notes, formal review results, independent reference designs, finding indexes, maintainer triage records, and ingestion summaries.

They are not execution source. They do not approve repository edits, target workspace creation, target material ingestion, target repository write, regression formalization, operational build, or execution-source updates.

Findings and design proposals become actionable only after maintainer/user validation and, if needed, a separately approved task number.

## Current review rounds

- `FABLE5-REVIEW-001/` — post-079 to post-085 handoff authority and state-machine review.
- `FABLE5-REVIEW-002/` — regression-candidate and warning-closure traceability review.
- `FABLE5-REVIEW-003/` — post-repair snapshot refresh and portable continuation delta review after MNEMOSYNE-088/089/090/091.

## Independent contrastive design tracks

- `FABLE5-GREENFIELD-001/` — Fable 5 independent greenfield reconstruction track. The stored charter defines a source firewall, atomic multi-step plan, raw-preservation requirements, and a later comparison phase. It is a contrastive reference track, not a replacement for the current GPT design or execution source.
  - `steps/GF-STEP-1A/` — bounded core-user-need extraction pilot. Prompt, Fable chat summary, downloadable Markdown output, integrity metadata, structural validation, exposure ledger, and continuation status are stored. GF-STEP-1 remains incomplete; no substantive acceptance/rejection review has been performed.
  - `steps/GF-STEP-1B/` — bounded deferred-origin-need extraction and consolidated-question continuation. Prompt, Fable chat summary, downloadable Markdown output, integrity metadata, mechanism provenance register, question list, and continuation status are stored. GF-STEP-1 remains incomplete; no substantive acceptance/rejection review has been performed.
  - `steps/GF-STEP-1C/` — bounded research-prompt-index signal mapping and STEP-1 gap analysis. Prompt, Fable chat summary, downloadable Markdown output, integrity metadata, full index coverage, assembly map, completion determination, and proposed minimal original-prompt check are stored. GF-STEP-1 remains incomplete pending the required DR4 prompt check; no substantive acceptance/rejection review has been performed.
  - `steps/GF-STEP-1D/` — bounded DR4 original-prompt inspection and STEP-1 closure reassessment. Prompt, Fable chat summary, downloadable Markdown output, integrity metadata, N20 refinement, preservation/redaction tension map, question delta, and second-tier continuation status are stored. GF-STEP-1 remains incomplete pending the bounded MT/HO/FTDRE prompt check; no substantive acceptance/rejection review has been performed.
  - `steps/GF-STEP-1E/` — bounded MT/HO/FTDRE original-prompt inspection and final STEP-1 closure record. Prompt, Fable chat summary, downloadable Markdown output, integrity metadata, N19/N21 refinements, N12 handoff delta, final need assembly, and explicit-open-question closure are stored. GF-STEP-1 is complete with explicit open questions as a Fable advisory result; substantive maintainer acceptance remains deferred until GPT Pro quota is restored.
  - `steps/GF-STEP-2A/` — bounded research-evidence catalog and staged original-report reading plan. The revised Fable prompt, chat summary, downloadable source map, integrity metadata, report/domain inventory, date/PDF caveats, and STEP2B batch are stored. GF-STEP-2 remains incomplete; substantive acceptance remains deferred.
  - `steps/GF-STEP-2B1/` — bounded read of the foundational comprehensive research report. The exact prompt, chat summary, byte-faithful downloadable output, integrity metadata, 14 evidence records, S-01/S-02/S-03 dispositions, principle/product split, and STEP2B2 continuation are stored. GF-STEP-2 remains incomplete; substantive acceptance remains deferred.
  - `steps/GF-STEP-2B2A/` — bounded full-text-layer review of the plain-dialogue capability-boundary PDF. The exact prompt, chat summary, byte-faithful downloadable output, integrity metadata, six text-only evidence records, S-02/S-03 dispositions, visual/date limitations, and STEP2B3 continuation are stored. No OCR or visual inspection was performed; GF-STEP-2 remains incomplete and substantive acceptance remains deferred.
  - `steps/GF-STEP-2B3/` — bounded full-text-layer review of the local project-file workflow PDF. The exact prompt, chat summary, byte-faithful downloadable output, integrity metadata, five text-only evidence records, the S-04 refinement, four workflow-boundary rows, visual/date limitations, and STEP2B4 continuation are stored. No OCR or visual inspection was performed; GF-STEP-2 remains incomplete and substantive acceptance remains deferred.
  - `steps/GF-STEP-2B4A/` — strictly usage-bounded core-text probe of the hosted-repository workflow PDF. The exact prompt, chat summary, byte-faithful downloadable output, integrity metadata, three provisional text-only evidence items, provisional S-05 support, and exact unreviewed scope for STEP2B4B are stored. No final S-05 disposition, OCR, or visual inspection was performed; GF-STEP-2 remains incomplete and substantive acceptance remains deferred.
  - `incidents/INC-001-step2a-safety-routing.md` — operational record of the first STEP2A attempt being visibly routed from Fable 5 to Opus 4.8, the non-editable pasted-task UI, preserved partial output, explicit uncertainty about the proprietary trigger, and successful recovery through a revised fresh-conversation Fable run.

## Follow-up triage records

- `FABLE5-TRIAGE-001/` — Fable response after user answers to earlier review questions; closes several question items, raises Q2-2 warning-layer tracing to high priority, and leaves R3 hygiene cleanup unapproved pending re-check / user decision. MNEMOSYNE-096 added partial raw preservation; MNEMOSYNE-101 added the full uploaded Fable response text with documented CRLF-to-LF normalization. The original seven Chinese answers and full conservative interpretation package remain unavailable as exact originals.

## Follow-up evidence audits

- `FABLE5-TRIAGE-001/evidence-audits/MNEMOSYNE-097-q2-2-r3-readonly-audit.md` — read-only evidence table for Q2-2 warning-layer source/model/latest-version tracing and R3 hygiene fresh-snapshot recheck. It does not select a canonical warning layer or approve cleanup.

## Follow-up review packages

- `FABLE5-TRIAGE-001/review-packages/MNEMOSYNE-099-higher-model-q2-r3-decision-package.md` — package for future higher-model / restored-Pro review of Q2-2 and R3 options. It does not decide Q2-2 or approve cleanup.
- `FABLE5-TRIAGE-001/review-packages/MNEMOSYNE-100-higher-model-transfer-prompt.md` — copyable transfer prompt for executing the MNEMOSYNE-099 review package in a future higher-reasoning conversation. It does not itself decide or authorize repair.

## Ingestion status convention

```yaml
status_values:
  received_in_chat_not_canonical: file was received in a maintenance conversation but not yet copied into a canonical repository location
  canonical_copy_stored: file has been copied verbatim or with documented normalization
  canonical_summary_stored: non-verbatim summary has been stored with documented provenance
  raw_originals_partially_preserved: available originals and transfer metadata are stored, but some original materials remain unavailable
  charter_canonical_copy_stored: an independent design/review charter has been stored as non-execution-source evidence
  step_output_canonical_copy_stored: a bounded step prompt, response summary, and downloadable output have been stored with integrity and continuation metadata
  provider_routing_incident_stored: a provider model-routing or safety-routing observation is stored separately from the canonical task result, with trigger uncertainty preserved
  read_only_evidence_audit_stored: an evidence table or recheck record is stored without repair/writeback authority
  review_package_prepared: a non-execution-source prompt/package is prepared for later review but does not itself decide or authorize repair
  transfer_prompt_prepared: a copyable prompt is prepared for later execution in another conversation but does not itself decide or authorize repair
  triaged: maintainer triage record exists
  repair_candidates_routed: accepted repair candidates have been routed to user-approved tasks or explicitly deferred
```
