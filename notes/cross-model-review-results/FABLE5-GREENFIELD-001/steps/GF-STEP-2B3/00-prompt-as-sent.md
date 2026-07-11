# FABLE5-GREENFIELD-001 — GF-STEP-2B3 Prompt as Sent

```text
Run the next usage-bounded substep of FABLE5-GREENFIELD-001.

step_id: GF-STEP-2B3
step_name: local_project_file_workflow_report_text_evidence_review
relationship_to_charter:
  continuation of GF-STEP-2B2A;
  dedicated review of RPT-2026Q2-0004;
  not completion of GF-STEP-2

Execution setting:
- Research mode must remain OFF.
- Run in a fresh Fable 5 conversation.
- Use the attached file:
  FABLE5-GREENFIELD-001-STEP2B2A-plain-dialogue-core-text-evidence.md
- Do not retrieve STEP2A, STEP2B1, the charter, or earlier outputs.
- This prompt is self-contained.
- The remaining five-hour-session allowance is limited.
- Producing one complete, structurally valid artifact has priority over
  exhaustive analysis.

Purpose:
Review the text layer of one archived PDF report about file-based continuity in
local development-agent workflows.

This is a bounded document-evidence review.

The step must:
- identify what the report text supports about project-file continuity;
- distinguish file access from reliable persistent memory;
- identify the role and limitations of repository instruction/state files;
- reassess only STEP2A signal S-04;
- retain evidence dates, product-surface scope, and uncertainty;
- separate text-derived evidence from unreviewed visual material.

The step must not:
- evaluate or rank models, vendors, or frontier systems;
- investigate model internals or training;
- build a generalized capability dataset;
- verify current product behavior through the web;
- design the Mnemosyne architecture;
- compare with the existing GPT-produced design;
- recommend repairs.

────────────────────────────────────
1. Allowed inputs
────────────────────────────────────

Allowed attachment:

- FABLE5-GREENFIELD-001-STEP2B2A-plain-dialogue-core-text-evidence.md

Use the attachment only for:
- the existing research-domain and STEP-1 need identifiers;
- S-04’s prior wording as restated below;
- source-strength, date, surface, and overclaim discipline;
- continuity and boundary information.

Do not treat the attachment’s S-02 or S-03 product findings as input to the
present report analysis except where a short contrast between plain dialogue
and local project workflows is necessary.

Allowed repository source — exactly one path:

- path:
  raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 3：Codex,Claude Code,Cursor 等本地开发 Agent 的文件式记忆能力.pdf
- ref: master
- expected blob SHA:
  5fe68eb33fabcecd3bc23b8a38451f03bd0bbc2e

Read no other repository path.

Do not open:
- any other original report;
- any summary or summary index;
- any research prompt;
- pdf-figure-review-index.md;
- current/**;
- handoff/**;
- notes/**;
- commands/**;
- task-result records;
- existing design documents;
- external websites.

Any file names, URLs, products, rule files, or mechanisms named inside the PDF
are report-internal metadata only. Do not open them.

────────────────────────────────────
2. Usage-preservation execution modes
────────────────────────────────────

First determine, without producing a separate response:

- whether a usable text layer exists;
- approximate page count, if available;
- approximate extracted-text character or word count, if available.

Then choose one mode.

Mode A — full_text_mode:

Use only when:
- the PDF is no more than approximately 10 pages; and
- extracted text is no more than approximately 25,000 characters or
  approximately 5,000 words; and
- complete reading appears safe within the remaining session allowance.

In this mode:
- inspect the complete text layer;
- do not inspect visual objects or layout meaning.

Mode B — core_text_mode:

Use when:
- either threshold is exceeded;
- size cannot be estimated confidently;
- PDF extraction is unusually costly;
- complete reading may jeopardize delivery before the session allowance ends.

In this mode inspect only:
- title, scope, introduction, or executive summary;
- heading structure;
- sections directly addressing:
  - repository instruction or rule files;
  - persistent project state;
  - session startup and context recovery;
  - file read/write behavior;
  - local repository access;
  - source-of-truth and authority limitations;
  - staleness, drift, conflicts, or unreliable compliance;
  - migration or portability between tools;
- conclusion and explicit recommendations.

For core_text_mode:
- list exactly which sections were inspected;
- do not claim full-report inspection;
- propose a later bounded STEP2B3B only when relevant text remains unread.

Choosing core_text_mode counts as valid completion.

────────────────────────────────────
3. Source integrity and PDF handling
────────────────────────────────────

Before analysis:

- obtain the observed Git blob SHA;
- compare it with the expected SHA;
- record PDF page count if available;
- record extracted-text size if available;
- state whether the text layer is usable;
- record the selected mode.

If the SHA does not match:
- do not use the changed source;
- do not search for another copy;
- create a short integrity-failure artifact and stop.

PDF handling rules:

- text extraction only;
- no OCR;
- no screenshots;
- no image, chart, diagram, visual table, or layout interpretation;
- textual table content may be used only when extraction is unambiguous;
- every evidence conclusion must be marked text_only;
- visual-dependent meaning remains unverified.

Maximum repository retrieval/query batteries: 2.
Do not repeatedly retry extraction.

────────────────────────────────────
4. Evidence interpretation rules
────────────────────────────────────

Use only these evidence categories:

- report_direct_finding
- report_author_synthesis
- report_recommendation
- cited_external_claim_not_independently_checked
- dated_product_or_workflow_statement
- low_drift_engineering_principle
- mixed_or_uncertain

Apply these rules:

1. The report is research evidence, not execution source.
2. Referenced product documentation is not independently checked here.
3. A recommendation is not a verified product capability.
4. Product behavior retains the report’s evidence period and named surface.
5. Do not generalize one tool’s workflow to all development agents.
6. File read/write access is not, by itself, reliable long-term memory.
7. A rule file or instruction file is context, not guaranteed enforcement.
8. Separate:
   - access capability;
   - persistence mechanism;
   - semantic correctness;
   - authority and write approval;
   - auditability;
   - portability.
9. Do not update the report from your own current knowledge.
10. Do not discuss your own training cutoff or internal abilities.
11. Do not inspect visual content.
12. Do not import the current Mnemosyne design.

────────────────────────────────────
5. Local project-file evidence register
────────────────────────────────────

Extract at most 5 load-bearing evidence items.

Use IDs:

F2B3-E01 through F2B3-E05

Prefer evidence concerning:

- how local development agents discover and read project instruction files;
- whether those files persist across sessions;
- how project state or memory files are created or updated;
- which actions are automatic, manual, or confirmation-gated;
- whether file access guarantees correct or consistent use;
- how stale, conflicting, oversized, or misplaced instructions behave;
- audit, versioning, migration, and portability limits.

For every item record:

- evidence_id
- source_anchor
- concise_statement
- evidence_category
- named_product_or_workflow_scope
- source_evidence_date_or_period
- text_only: true
- visual_review_status: not_performed
- confidence_as_report_evidence:
    high |
    medium |
    low
- date_sensitivity:
    high |
    medium |
    low
- access_persistence_correctness_distinction
- related_research_domain_ids
- related_STEP1_need_ids
- supports_or_challenges_S04
- prohibited_overclaim
- notes

Do not fill the allowance unless each record is load-bearing.

────────────────────────────────────
6. Reassess only S-04
────────────────────────────────────

S-04 prior wording:

Local coding-agent file access is a prerequisite, not automatic reliable
memory. Reliable continuity additionally requires an explicit source of truth,
write-back rules, review or audit, conflict handling, user confirmation where
authority is involved, and a handoff or state-recovery mechanism.

Choose exactly one disposition:

- dedicated_report_confirms
- dedicated_report_refines
- dedicated_report_partially_supports
- dedicated_report_challenges
- dedicated_report_does_not_resolve

Record:

- signal_id: S-04
- previous_wording
- disposition
- replacement_wording_if_refined
- supporting_F2B3_evidence_ids
- named_tool_and_surface_scope
- access_vs_memory_distinction
- report_date_caveat
- remaining_visual_dependency
- remaining_current_fact_refresh_dependency
- remaining_original_report_dependency
- prohibited_overclaim

Do not directly reassess S-01, S-02, S-03, or S-05.

Material relevant to S-05 may be recorded only as preliminary corroboration;
RPT-2026Q2-0005 remains its dedicated source.

────────────────────────────────────
7. Compact workflow-boundary table
────────────────────────────────────

Create at most 4 rows.

For each row:

- boundary_id
- workflow_or_file_type_as_named_in_report
- report_text_supported_role
- what_it_does_not_guarantee
- automation_level:
    automatic |
    conditional |
    manual |
    mixed |
    unclear
- evidence_date_or_period
- date_sensitivity:
    high |
    medium |
    low
- visual_dependency:
    none_identified |
    possible |
    unknown

Do not turn the table into a product comparison.

────────────────────────────────────
8. Minimal STEP-1 linkage delta
────────────────────────────────────

Record evidence-coverage changes only for:

- GF1A-N02
- GF1A-N09
- GF1A-N10
- GF1A-N11
- GF1B-N15

Include at most four of these need IDs. Select only those materially changed by
the report.

For each selected item:

- need_id
- coverage_change
- supporting_evidence_ids
- remaining_report_dependency
- user_decision_not_resolved

Keep each entry concise.

────────────────────────────────────
9. Limitations and remaining uncertainty
────────────────────────────────────

Record at most 3 items, limited to:

- visual content not reviewed;
- product/version/date sensitivity;
- text not inspected in core_text_mode;
- unclear difference between native feature and recommended practice;
- report reliance on cited documentation not independently checked.

Do not create a broad contradiction register.

────────────────────────────────────
10. Status determination
────────────────────────────────────

Choose exactly one:

- GF_STEP_2B3_complete_full_text_layer_reviewed
- GF_STEP_2B3_complete_core_text_review_ready_for_STEP2B3B
- GF_STEP_2B3_incomplete_source_integrity_failure
- GF_STEP_2B3_incomplete_no_usable_text_layer
- GF_STEP_2B3_incomplete_other_specific_gap

Do not declare GF-STEP-2 complete.

If full_text_mode completes:
- state that STEP2B3B is unnecessary;
- propose a bounded next report step for RPT-2026Q2-0005 only.

If core_text_mode completes:
- propose a narrowly bounded STEP2B3B for uncovered relevant text;
- do not start RPT-2026Q2-0005 yet.

────────────────────────────────────
11. Hard workload limits
────────────────────────────────────

- repository paths: exactly 1
- retrieval/query batteries: maximum 2
- PDF reports opened: exactly 1
- evidence records: maximum 5
- signals reassessed: exactly S-04
- workflow-boundary rows: maximum 4
- STEP-1 linkage entries: maximum 4
- limitations: maximum 3
- no OCR
- no visual inspection
- no other report, summary, prompt, or index read
- no external or web research
- Research mode OFF
- no automatic continuation

Word-budget policy:

- soft target: 1,050–1,500 words
- hard cap: 1,850 words
- a complete first draft inside the hard cap is acceptable
- do not rewrite merely to enter the soft target
- at most one light compression pass, only if the hard cap is exceeded
- preserve evidence and limitations before optional explanation
- perform one approximate word-count check only
- do not repeat counting or compression

Usage-preservation stop rule:

- Prefer a complete core-text artifact over an unfinished exhaustive review.
- Once all required sections are complete, add no optional narrative.
- Stop immediately after presenting the file and the brief summary.

────────────────────────────────────
12. Required downloadable file
────────────────────────────────────

Create a downloadable Markdown file named exactly:

FABLE5-GREENFIELD-001-STEP2B3-local-project-file-text-evidence.md

Required sections:

1. Metadata
2. Scope and selected execution mode
3. Allowed-source and anti-contamination policy
4. Source integrity and PDF text-access result
5. Evidence interpretation rules
6. Text-layer coverage record
7. Local project-file evidence register
8. S-04 reassessment
9. Compact workflow-boundary table
10. Minimal STEP-1 linkage delta
11. Visual, date, and remaining-coverage limitations
12. Status determination and bounded continuation
13. Boundary statement

Metadata:

charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2B3
record_type: local_project_file_pdf_text_evidence_review
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-2B2A
research_mode: false
source_file:
  path: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 3：Codex,Claude Code,Cursor 等本地开发 Agent 的文件式记忆能力.pdf
  expected_blob_sha: 5fe68eb33fabcecd3bc23b8a38451f03bd0bbc2e

The coverage section must state:

- expected and observed SHA;
- text-layer availability;
- selected execution mode;
- page and extracted-text size if available;
- portions inspected;
- portions not inspected;
- retrieval batteries used;
- evidence records created;
- S-04 disposition;
- visual inspection not performed;
- completion status.

────────────────────────────────────
13. Chat response
────────────────────────────────────

After presenting the file, state briefly:

- completion within limits;
- SHA result;
- selected execution mode;
- text-layer usability;
- full or partial text coverage;
- evidence-record count;
- S-04 disposition;
- workflow-boundary row count;
- retrieval batteries used;
- visual inspection performed: no;
- approximate word count;
- status determination;
- downloadable file result.

Do not repeat the file body.

────────────────────────────────────
14. Boundary
────────────────────────────────────

Do not:

- write repository files;
- generate execution tasks;
- update execution source;
- inspect another report, summary, prompt, index, or PDF;
- use OCR or visual interpretation;
- perform external research;
- evaluate or rank models or vendors;
- compare or modify the existing design;
- begin architecture work;
- create target-project artifacts;
- resume or close the paused route.

This output is non-execution-source advisory evidence only.
Stop after the downloadable file and brief summary.
```
