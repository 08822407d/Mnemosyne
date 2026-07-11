# FABLE5-GREENFIELD-001 — GF-STEP-2B4A Prompt as Sent

```text
Run the next strictly usage-bounded substep of FABLE5-GREENFIELD-001.

step_id: GF-STEP-2B4A
step_name: hosted_repository_workflow_report_core_text_probe
relationship_to_charter:
  bounded preliminary probe of RPT-2026Q2-0005;
  continuation of GF-STEP-2B3;
  not completion of the RPT-2026Q2-0005 review or GF-STEP-2

Execution setting:
- Research mode must remain OFF.
- Run in a fresh Fable 5 conversation.
- Use only the attached file:
  FABLE5-GREENFIELD-001-STEP2B3-local-project-file-text-evidence.md
- Do not retrieve STEP2A, earlier steps, or the charter.
- This prompt is self-contained.
- The remaining five-hour-session allowance is very limited.
- Delivering one small valid artifact has priority over complete report
  coverage.

Purpose:
Perform a small text-layer probe of one archived report about hosted
repository-based work, review trails, and controlled write-back.

This substep must only:
- verify source integrity and text-layer usability;
- inspect a small set of core report portions;
- extract no more than three provisional evidence items;
- determine whether the report is suitable for a later full text-layer review;
- preserve exact uncovered scope for continuation.

This substep must not:
- complete the full RPT-2026Q2-0005 evidence review;
- make a final decision on S-05;
- evaluate or rank models, services, or vendors;
- investigate model internals or training;
- perform security testing;
- verify present-day product behavior through the web;
- design architecture;
- compare with or repair the current Mnemosyne design.

────────────────────────────────────
1. Allowed inputs
────────────────────────────────────

Allowed attachment:

- FABLE5-GREENFIELD-001-STEP2B3-local-project-file-text-evidence.md

Use it only for:
- the preliminary S-05 references;
- research-domain and STEP-1 need identifiers;
- the distinction between write capability, reviewed acceptance, auditability,
  and semantic correctness;
- date, source-strength, visual, and authority caveats.

Allowed repository source — exactly one path:

- path:
  raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 4：云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计.pdf
- ref: master
- expected blob SHA:
  ee4bb0ab829cb59819263858c3c4a3a0178c22da

Read no other repository path.

Do not open:
- another original report;
- any summary, index, or prompt;
- pdf-figure-review-index.md;
- current/**;
- handoff/**;
- notes/**;
- commands/**;
- task-result records;
- external websites.

References inside the PDF are report-internal metadata only. Do not follow them.

────────────────────────────────────
2. Mandatory small-scope mode
────────────────────────────────────

Use core_text_probe_mode only.

Do not switch to full_text_mode even if the PDF is short.

Inspect only:

1. title and stated scope;
2. executive summary, overview, or introduction;
3. heading structure;
4. sections directly discussing:
   - branch, commit, pull-request, or review trails;
   - human approval or permission boundaries;
   - differences between claimed completion and observable repository changes;
   - whether write actions are native, conditional, or externally mediated;
5. conclusion or explicit limitations.

Do not inspect every section merely because sufficient usage appears available.

Record:
- exact portions inspected;
- exact portions not inspected;
- whether a later full review is justified.

────────────────────────────────────
3. Source integrity and PDF handling
────────────────────────────────────

Before analysis:

- obtain the observed Git blob SHA;
- compare it with the expected SHA;
- record page count if available;
- record extracted-text size if available;
- determine whether the text layer is usable.

If the SHA does not match:
- do not use the source;
- do not search for another copy;
- create a short integrity-failure artifact and stop.

PDF rules:

- text extraction only;
- no OCR;
- no screenshots;
- no visual interpretation of images, charts, tables, or layout;
- no repeated extraction attempts;
- every evidence item must be marked text_only;
- visual-dependent meaning remains unverified.

Maximum retrieval/query batteries: 1.

────────────────────────────────────
4. Evidence interpretation rules
────────────────────────────────────

Use only:

- report_direct_finding
- report_author_synthesis
- report_recommendation
- cited_external_claim_not_independently_checked
- dated_product_or_workflow_statement
- low_drift_engineering_principle
- mixed_or_uncertain

Apply:

1. The report is evidence, not execution source.
2. Referenced documentation is not independently verified.
3. Write access does not prove semantic correctness.
4. A commit or PR proves a repository change, not that the change is correct.
5. Claimed task completion and observed repository state must remain distinct.
6. Recommendations are not validated platform capabilities.
7. Product statements retain their named surface and 2026Q2 evidence period.
8. Do not use current knowledge to update the report.
9. Do not generalize one hosted workflow to all services.
10. Do not inspect visual material or current Mnemosyne design files.

────────────────────────────────────
5. Provisional evidence register
────────────────────────────────────

Extract at most 3 load-bearing provisional items.

Use IDs:

F2B4A-P01 through F2B4A-P03

Each item must contain:

- evidence_id
- source_anchor
- concise_statement
- evidence_category
- named_workflow_scope
- source_evidence_date_or_period
- text_only: true
- visual_review_status: not_performed
- provisional_status: requires_full_report_review
- confidence_as_report_evidence:
    high |
    medium |
    low
- write_audit_correctness_distinction
- related_research_domain_ids
- related_STEP1_need_ids
- possible_relation_to_S05
- prohibited_overclaim

Do not use all three slots unless justified.

────────────────────────────────────
6. S-05 handling
────────────────────────────────────

Do not select a final S-05 disposition.

Record only:

- signal_id: S-05
- prior_signal_theme:
    hosted repository write-back claims may differ from observable diffs;
    reliable audit requires repository evidence plus review
- provisional_support:
    present |
    absent |
    mixed |
    insufficient_scope
- supporting_provisional_evidence_ids
- what_full_review_must_still_check
- date_and_surface_caveat
- prohibited_overclaim

The final S-05 disposition is reserved for GF-STEP-2B4B.

────────────────────────────────────
7. Coverage and continuation ledger
────────────────────────────────────

Record:

- source SHA result;
- page count and text size if available;
- text-layer usability;
- portions inspected;
- portions deliberately not inspected;
- retrieval batteries used;
- provisional evidence count;
- whether visual material remains unreviewed;
- whether full text-layer review is justified;
- exact topics GF-STEP-2B4B must cover.

Do not create a broad STEP-1 linkage table in this probe.

────────────────────────────────────
8. Status determination
────────────────────────────────────

Choose exactly one:

- GF_STEP_2B4A_complete_probe_ready_for_STEP2B4B
- GF_STEP_2B4A_complete_probe_full_review_not_required
- GF_STEP_2B4A_incomplete_source_integrity_failure
- GF_STEP_2B4A_incomplete_no_usable_text_layer
- GF_STEP_2B4A_incomplete_other_specific_gap

Do not declare S-05, GF-STEP-2B4, or GF-STEP-2 complete.

Do not execute STEP2B4B.

────────────────────────────────────
9. Hard workload limits
────────────────────────────────────

- repository paths: exactly 1
- retrieval/query batteries: exactly 1 maximum
- PDF reports opened: exactly 1
- execution mode: core_text_probe_mode only
- provisional evidence items: maximum 3
- final signal dispositions: 0
- no STEP-1 linkage table
- no contradiction register
- no OCR or visual inspection
- no other report, summary, prompt, or index read
- no external research
- Research mode OFF
- no automatic continuation

Word-budget policy:

- soft target: 650–900 words
- hard cap: 1,100 words
- a complete first draft within the hard cap is acceptable
- no compression pass unless the hard cap is exceeded
- preserve source integrity, evidence, uncovered scope, and continuation
  information before optional prose
- perform one approximate word-count check only
- stop immediately after the file and brief summary

────────────────────────────────────
10. Required downloadable file
────────────────────────────────────

Create exactly:

FABLE5-GREENFIELD-001-STEP2B4A-hosted-workflow-core-text-probe.md

Required sections:

1. Metadata
2. Scope and hard limits
3. Allowed-source and anti-contamination policy
4. Source integrity and text-access result
5. Core-text portions inspected
6. Provisional evidence register
7. Provisional S-05 note
8. Unreviewed scope and STEP2B4B requirements
9. Status determination
10. Boundary statement

Metadata:

charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2B4A
record_type: hosted_repository_workflow_core_text_probe
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-2B3
research_mode: false
source_file:
  path: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 4：云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计.pdf
  expected_blob_sha: ee4bb0ab829cb59819263858c3c4a3a0178c22da

────────────────────────────────────
11. Chat response
────────────────────────────────────

After presenting the file, state only:

- completion within limits;
- SHA result;
- text-layer usability;
- page/text size when available;
- portions inspected;
- provisional evidence count;
- provisional S-05 support status;
- retrieval batteries used;
- visual inspection performed: no;
- approximate word count;
- status determination;
- downloadable file result.

Do not repeat the file body.

────────────────────────────────────
12. Boundary
────────────────────────────────────

Do not:

- write repository files;
- generate execution tasks;
- update execution source;
- inspect another report, summary, prompt, index, or PDF;
- use OCR or visual interpretation;
- perform external research;
- perform security testing;
- evaluate or rank models or vendors;
- compare or modify the existing design;
- begin architecture work;
- create target-project artifacts;
- resume or close the paused route.

This output is non-execution-source advisory evidence only.
Stop after the downloadable file and brief summary.
```
