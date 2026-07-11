# FABLE5-GREENFIELD-001 — GF-STEP-2B2A Prompt as Sent

```text
Run the next usage-bounded substep of FABLE5-GREENFIELD-001.

step_id: GF-STEP-2B2A
step_name: plain_dialogue_report_core_text_evidence_review
relationship_to_charter:
  bounded first part of the RPT-2026Q2-0003 review;
  continuation of GF-STEP-2B1;
  not completion of GF-STEP-2B2 or GF-STEP-2

Execution setting:
- Research mode must remain OFF.
- Run in this fresh Fable 5 conversation.
- Use the attached file:
  FABLE5-GREENFIELD-001-STEP2B1-foundational-report-evidence.md
- Do not retrieve STEP2A, the charter, or earlier step outputs.
- This prompt is self-contained.
- The remaining five-hour-session allowance is limited, so completion of a
  small valid artifact has priority over exhaustive analysis.

Purpose:
Review the text layer of one archived PDF report about external-memory
boundaries in plain ChatGPT and Claude conversation scenarios.

This substep is intentionally smaller than GF-STEP-2B1.

It must:
- establish the report's core text-derived evidence;
- reassess only STEP2A signals S-02 and S-03;
- preserve report date, interaction-surface scope, and uncertainty;
- clearly separate text-derived claims from unreviewed visual content;
- stop before the remaining usage window is exhausted.

It must not:
- evaluate or rank models or vendors;
- investigate model internals or training;
- build a general capability dataset;
- verify present-day product behavior through the web;
- design architecture;
- compare with the current GPT design;
- recommend repairs.

────────────────────────────────────
1. Allowed inputs
────────────────────────────────────

Allowed attachment:

- FABLE5-GREENFIELD-001-STEP2B1-foundational-report-evidence.md

Use it only for:
- S-02 and S-03 prior wording and disposition;
- evidence IDs F2B1-E02 through F2B1-E05 where relevant;
- research-domain and STEP-1 need identifiers;
- date/surface/overclaim discipline;
- continuation boundaries.

Allowed repository source — exactly one path:

- path:
  raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 2：ChatGPT,Claude 纯对话场景的外部记忆能力边界.pdf
- ref: master
- expected blob SHA:
  a1146ad6bfee5cbdc431f35fb0b7a442e162aab7

Read no other repository path.

Do not open:
- any other original report;
- any summary or summary index;
- any prompt;
- pdf-figure-review-index.md;
- current/**;
- handoff/**;
- notes/**;
- commands/**;
- task-result records;
- external websites.

References inside the PDF are report-internal metadata only. Do not open them.

────────────────────────────────────
2. Usage-preservation execution modes
────────────────────────────────────

First determine, without producing a separate response:

- whether a usable text layer is available;
- approximate page count, if exposed;
- approximate extracted-text word count, if exposed.

Then choose one mode.

Mode A — full_text_mode:

Use this mode only when:
- the usable text layer is no more than approximately 12,000 words; and
- the document is no more than approximately 30 pages, when page count is
  available.

In this mode:
- inspect the complete text layer;
- do not inspect images, charts, tables as visual objects, or layout meaning.

Mode B — core_text_mode:

Use this mode when:
- either threshold is exceeded;
- the size cannot be estimated confidently;
- PDF processing appears unusually costly;
- completing a full read may endanger delivery within the remaining allowance.

In this mode inspect only:
- document title and scope;
- introduction or executive summary;
- heading structure;
- sections directly addressing:
  - platform-provided conversation memory;
  - Projects or equivalent knowledge containers;
  - long-conversation continuity;
  - external-file or repository access;
  - export, migration, write-back, audit, or human-copy requirements;
  - unsupported assumptions and limitations;
- conclusion and explicit recommendations.

For core_text_mode:
- state exactly which portions were inspected;
- do not claim full-report inspection;
- propose a later GF-STEP-2B2B for uncovered text if necessary.

Choosing core_text_mode is valid completion, not failure.

────────────────────────────────────
3. Source integrity and PDF handling
────────────────────────────────────

Before analysis:

- obtain the observed Git blob SHA;
- compare it with the expected SHA;
- record whether the PDF text layer is usable;
- record page count and extracted-text size if available;
- record the selected execution mode.

If the SHA does not match:
- do not use the changed file;
- do not search for a replacement;
- produce a short integrity-failure artifact and stop.

PDF rules:

- text extraction only;
- no OCR;
- no screenshots;
- no image, chart, diagram, visual table, or layout interpretation;
- a table represented clearly in extracted text may be mentioned only as
  text-derived;
- every conclusion must be labeled text_only;
- visual-dependent meaning remains unverified.

Maximum retrieval/query batteries: 2.
Do not repeatedly retry PDF extraction.

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

1. The report is research evidence, not execution source.
2. The report's cited sources are not independently checked here.
3. Product statements retain their stated evidence date and interaction
   surface.
4. Do not generalize from one product mode to all product modes.
5. Absence of a documented feature is not proof of impossibility.
6. A recommendation is not an established capability fact.
7. Do not update the report using your own knowledge.
8. Do not discuss your own training cutoff or internal capabilities.
9. Do not inspect visual material.
10. Do not import existing Mnemosyne design details.

────────────────────────────────────
5. Core text evidence register
────────────────────────────────────

Extract at most 6 load-bearing evidence items.

Use IDs:

F2B2A-E01 through F2B2A-E06

Focus on:

- what ordinary conversation surfaces retain;
- what platform-provided memory or project knowledge can and cannot establish;
- what is or is not auditable, exportable, migratable, or rollbackable;
- whether repository/file write-back is native, conditional, manual, or
  unsupported in the studied surface;
- what human transfer or external tooling is required;
- which claims are dated and product-mode-specific.

For every item include:

- evidence_id
- source_anchor
- concise_statement
- evidence_category
- interaction_surface
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
- related_STEP2B1_evidence_ids
- related_research_domain_ids
- related_STEP1_need_ids
- prohibited_overclaim
- notes

Do not use the full allowance unless justified.

────────────────────────────────────
6. Reassess only S-02 and S-03
────────────────────────────────────

S-02 current STEP2B1 wording:

As of 2026-05-23, plain-dialogue surfaces have no default repository
write-back; conditional write paths may exist through apps, agents, or MCP
with surface-specific permissions and must not be assumed as defaults.

S-03 current wording:

Platform-provided memory is auxiliary rather than an auditable,
migratable, rollbackable project truth source.

For each choose:

- dedicated_report_confirms
- dedicated_report_refines
- dedicated_report_partially_supports
- dedicated_report_challenges
- dedicated_report_does_not_resolve

Record:

- signal_id
- disposition
- replacement_wording_if_refined
- supporting_F2B2A_evidence_ids
- interaction_surface_scope
- report_date_caveat
- remaining_visual_dependency
- remaining_current_fact_refresh_dependency
- prohibited_overclaim

Do not reassess S-01, S-04, or S-05.

────────────────────────────────────
7. Compact surface-and-date register
────────────────────────────────────

Create at most 5 rows.

For each record:

- item_id
- product_or_surface_as_named_in_report
- report_text_statement
- evidence_date_or_period
- volatility:
    high |
    medium |
    low
- may_enter_final_STEP2:
    text_evidence_with_date_caveat |
    needs_later_refresh |
    principle_only
- visual_dependency:
    none_identified |
    possible |
    unknown

Do not perform current fact checking.

────────────────────────────────────
8. Minimal STEP-1 linkage delta
────────────────────────────────────

Record evidence-coverage changes only for:

- GF1A-N01
- GF1A-N02
- GF1A-N09
- GF1A-N12

For each:

- need_id
- coverage_change
- supporting_evidence_ids
- remaining_report_dependency
- user_decision_not_resolved

Keep each entry to no more than three concise sentences.

────────────────────────────────────
9. Uncertainty and remaining-coverage note
────────────────────────────────────

Record at most 3 issues covering only:

- visual information not reviewed;
- dated or surface-specific product statements;
- report sections not inspected in core_text_mode;
- internal tension materially affecting S-02 or S-03.

Do not create a large contradiction register.

────────────────────────────────────
10. Status determination
────────────────────────────────────

Choose exactly one:

- GF_STEP_2B2A_complete_full_text_layer_reviewed
- GF_STEP_2B2A_complete_core_text_review_ready_for_STEP2B2B
- GF_STEP_2B2A_incomplete_source_integrity_failure
- GF_STEP_2B2A_incomplete_no_usable_text_layer
- GF_STEP_2B2A_incomplete_other_specific_gap

Do not declare GF-STEP-2B2 or GF-STEP-2 complete.

If full_text_mode completes:
- propose the next report-reading step;
- do not create STEP2B2B unnecessarily.

If core_text_mode completes:
- propose a narrowly bounded STEP2B2B only for the uncovered relevant text;
- do not execute it.

────────────────────────────────────
11. Hard workload limits
────────────────────────────────────

- repository paths: exactly 1
- retrieval/query batteries: maximum 2
- PDF reports opened: exactly 1
- evidence records: maximum 6
- signals reassessed: exactly S-02 and S-03
- surface/date rows: maximum 5
- uncertainty items: maximum 3
- no OCR
- no visual inspection
- no other report, summary, or prompt read
- no web search
- Research mode OFF
- no automatic continuation

Word-budget policy:

- soft target: 1,100–1,600 words
- hard cap: 2,000 words
- a complete file inside the hard cap is acceptable
- do not rewrite merely to enter the soft target
- at most one light compression pass, only if the hard cap is exceeded
- preserve evidence and limitations before optional explanation
- perform one approximate word-count check only
- do not repeat counting or compression

Usage-preservation stop rule:

- Prefer a structurally complete partial artifact over an unfinished exhaustive
  analysis.
- Do not add optional evidence records, narrative, or tables after all required
  sections are complete.
- Stop immediately after presenting the file and brief summary.

────────────────────────────────────
12. Required downloadable file
────────────────────────────────────

Create:

FABLE5-GREENFIELD-001-STEP2B2A-plain-dialogue-core-text-evidence.md

Required sections:

1. Metadata
2. Scope and selected execution mode
3. Allowed-source and anti-contamination policy
4. Source integrity and PDF text-access result
5. Evidence interpretation rules
6. Text-layer coverage record
7. Core text evidence register
8. S-02 and S-03 reassessment
9. Compact surface-and-date register
10. Minimal STEP-1 linkage delta
11. Visual, date, and remaining-coverage limitations
12. Status determination and bounded continuation
13. Boundary statement

Metadata:

charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2B2A
record_type: plain_dialogue_pdf_core_text_evidence_review
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-2B1
research_mode: false
source_file:
  path: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 2：ChatGPT,Claude 纯对话场景的外部记忆能力边界.pdf
  expected_blob_sha: a1146ad6bfee5cbdc431f35fb0b7a442e162aab7

The coverage section must state:

- expected and observed SHA;
- text-layer availability;
- selected mode;
- estimated page/text size when available;
- portions inspected;
- portions not inspected;
- retrieval batteries;
- evidence-record count;
- S-02 and S-03 dispositions;
- visual review not performed;
- completion status.

────────────────────────────────────
13. Chat response
────────────────────────────────────

After creating the file, state briefly:

- completion within limits;
- SHA result;
- selected mode;
- text-layer usability;
- full or partial text coverage;
- evidence-record count;
- S-02 disposition;
- S-03 disposition;
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
- inspect another report, summary, prompt, or PDF;
- use OCR or visual interpretation;
- perform external research;
- evaluate models or vendors;
- compare or modify the existing design;
- begin architecture work;
- create target-project artifacts;
- resume or close the paused route.

This output is non-execution-source advisory evidence only.
Stop after the downloadable file and brief summary.
```
