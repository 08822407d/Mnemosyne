# Cross-Model Review Results

This directory stores non-execution-source heterogeneous model review artifacts, contrastive design tracks, maintainer triage records, evidence audits, and review packages for Mnemosyne.

These artifacts may include review prompts, access reports, project-understanding notes, formal review results, independent reference designs, finding indexes, maintainer triage records, and ingestion summaries.

They are not execution source. They do not approve repository edits, target workspace creation, target material ingestion, target repository write, regression formalization, operational build, or execution-source updates.

Findings and design proposals become actionable only after maintainer/user validation and, if needed, a separately approved task number.

## Current review rounds

- `FABLE5-REVIEW-001/` — post-079 to post-085 handoff authority and state-machine review. MNEMOSYNE-113 completed substantive Pro triage: F-001/F-003 were already repaired; F-004/F-005/F-006 are now closed with provenance, no-write-exception, and canonical-storage decisions.
- `FABLE5-REVIEW-002/` — regression-candidate and warning-closure traceability review. MNEMOSYNE-113 resolved Q2-1/Q2-2/Q2-3 through W4 clarification, layered warning canonicalization, and a future formalization-decision agenda; no regression test was formalized.
- `FABLE5-REVIEW-003/` — post-repair snapshot refresh and portable continuation delta review after MNEMOSYNE-088/089/090/091. MNEMOSYNE-113 closed the hygiene queue without rewriting historical evidence or frozen MNEMOSYNE-082/083 artifacts.

## First-wave substantive adjudication

- `FABLE5-TRIAGE-001/02-gpt-pro-substantive-adjudication-and-repair-decisions.md` — GPT Pro maintainer adjudication of FABLE5-REVIEW-001/002/003 and later human-answer triage. It accepts supported findings, rejects a flat-list canonicalization, selects layered warning roles, records provenance/no-write decisions, and applies minimal repairs.
- `../first-target-project-intake-records/meta-agent/controlled-dry-run-results/META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-live-interpretation.md` — current non-execution-source warning/status mapping. Original result, maintainer review, and frozen handoff layers remain preserved.
- `../../current/review-and-validation-status.md` — live wayfinding pointer for review and validation state. `current/human-approved-spec.md` remains the only execution source.

## Independent contrastive design tracks

- `FABLE5-GREENFIELD-001/` — Fable 5 independent greenfield reconstruction track. The stored charter defines a source firewall, atomic multi-step plan, raw-preservation requirements, and a later comparison phase. It is a contrastive reference track, not a replacement for the current GPT design or execution source.
  - `steps/GF-STEP-1A/` — bounded core-user-need extraction pilot. Prompt, Fable chat summary, downloadable Markdown output, integrity metadata, structural validation, exposure ledger, and continuation status are stored. GF-STEP-1 remained incomplete at this substep.
  - `steps/GF-STEP-1B/` — bounded deferred-origin-need extraction and consolidated-question continuation. Prompt, Fable chat summary, downloadable Markdown output, integrity metadata, mechanism provenance register, question list, and continuation status are stored.
  - `steps/GF-STEP-1C/` — bounded research-prompt-index signal mapping and STEP-1 gap analysis. Prompt, Fable chat summary, downloadable Markdown output, integrity metadata, full index coverage, assembly map, completion determination, and proposed minimal original-prompt check are stored.
  - `steps/GF-STEP-1D/` — bounded DR4 original-prompt inspection and STEP-1 closure reassessment. Prompt, Fable chat summary, downloadable Markdown output, integrity metadata, N20 refinement, preservation/redaction tension map, question delta, and second-tier continuation status are stored.
  - `steps/GF-STEP-1E/` — bounded MT/HO/FTDRE original-prompt inspection and final STEP-1 closure record. GF-STEP-1 is complete with explicit open questions as a Fable advisory result; no separate completed substantive maintainer acceptance of the greenfield need model has occurred.
  - `steps/GF-STEP-2A/` — bounded research-evidence catalog and staged original-report reading plan. The revised Fable prompt, chat summary, downloadable source map, integrity metadata, report/domain inventory, date/PDF caveats, and STEP2B batch are stored.
  - `steps/GF-STEP-2B1/` — bounded read of the foundational comprehensive research report. The exact prompt, chat summary, byte-faithful downloadable output, integrity metadata, 14 evidence records, S-01/S-02/S-03 dispositions, principle/product split, and STEP2B2 continuation are stored.
  - `steps/GF-STEP-2B2A/` — bounded full-text-layer review of the plain-dialogue capability-boundary PDF. Six text-only evidence records and S-02/S-03 dispositions are stored; no OCR or visual inspection was performed.
  - `steps/GF-STEP-2B3/` — bounded full-text-layer review of the local project-file workflow PDF. Five text-only evidence records and the S-04 refinement are stored; no OCR or visual inspection was performed.
  - `steps/GF-STEP-2B4A/` — strictly usage-bounded core-text probe of the hosted-repository workflow PDF. Three provisional records were created and later superseded by STEP2B4B.
  - `steps/GF-STEP-2B4B/` — completion of the hosted-repository workflow PDF text-layer review. Five final evidence records replace the provisional records and S-05 is refined. No OCR or visual inspection was performed.
  - `steps/GF-STEP-2B5/` — integrated full-text-layer review of the theory/engineering, non-development-practice, and development-to-non-development transfer reports. The exact prompt, user-pasted Fable summary, byte-faithful downloadable output, integrity metadata, 18 evidence records, S-01 refinement, theory–practice–transfer matrix, non-development boundaries, and GF-STEP-2B6 continuation are stored. No OCR or visual inspection was performed; no substantive maintainer acceptance was conducted by the Thinking-tier storage task.
  - `steps/GF-STEP-2B6/` — integrated complete read of the MT/HO/UIG/FTDRE supplemental Markdown reports. The prompt, user-pasted Fable summary, byte-faithful returned output, integrity metadata, 24 evidence records, four reassessed questions, two new questions, all-11-report coverage ledger, recorded output-schema deviations, and GF-STEP-2C continuation are stored. The reading phase is complete as a Fable advisory result; GF-STEP-2 remains incomplete and no substantive maintainer acceptance was performed.
  - `incidents/INC-001-step2a-safety-routing.md` — operational record of the first STEP2A attempt being visibly routed from Fable 5 to Opus 4.8, with trigger uncertainty preserved and a later successful revised run.
  - `incidents/INC-002-weekly-quota-exhaustion.md` — user-reported Fable weekly-quota exhaustion, now resolved after quota became available and GF-STEP-2B5 completed. The former pause was not a task failure or substantive finding.

## Follow-up triage records

- `FABLE5-TRIAGE-001/` — Fable response after human answers, preserved raw complements, later evidence audit, higher-model decision package, and the completed MNEMOSYNE-113 Pro adjudication. The original seven Chinese answers and conservative interpretation package remain unavailable as exact repository originals; the full later Fable response is preserved with documented CRLF-to-LF normalization.

## Follow-up evidence audits

- `FABLE5-TRIAGE-001/evidence-audits/MNEMOSYNE-097-q2-2-r3-readonly-audit.md` — read-only evidence table for Q2-2 warning-layer source/model/latest-version tracing and R3 hygiene fresh-snapshot recheck. Its deferred decisions are superseded by the later MNEMOSYNE-113 substantive adjudication; the evidence table remains historical support.

## Follow-up review packages

- `FABLE5-TRIAGE-001/review-packages/MNEMOSYNE-099-higher-model-q2-r3-decision-package.md` — package that prepared the restored-Pro review. Its decision task was executed by MNEMOSYNE-113.
- `FABLE5-TRIAGE-001/review-packages/MNEMOSYNE-100-higher-model-transfer-prompt.md` — transfer prompt prepared for the same review. Retained for provenance; no longer an unexecuted live decision gate.

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
  provider_quota_operational_pause_stored: a provider quota exhaustion observation is stored as an operational pause, not a substantive finding or task failure
  provider_quota_operational_pause_resolved: a former provider quota pause has ended and the previously blocked next step has completed
  read_only_evidence_audit_stored: an evidence table or recheck record is stored without repair/writeback authority
  review_package_prepared: a non-execution-source prompt/package is prepared for later review but does not itself decide or authorize repair
  substantive_adjudication_completed: a maintainer decision record has evaluated advisory findings and recorded scoped repair decisions
  transfer_prompt_prepared: a copyable prompt/package is prepared for later execution in another conversation
  triaged: maintainer triage record exists
  repair_candidates_routed: accepted repair candidates have been routed to user-approved tasks or explicitly deferred
```
