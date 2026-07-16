Run the next integrated evidence-review substep of FABLE5-GREENFIELD-001.

step_id: GF-STEP-2B5
step_name: theory_nondevelopment_practice_and_transfer_batch_review
relationship_to_charter:
  integrated review of the complete STEP2A batch-2 source set;
  continuation of GF-STEP-2B4B;
  not completion of GF-STEP-2

Execution setting:
- Research mode must remain OFF.
- Run in a fresh Fable 5 conversation.
- Attach and use:
  FABLE5-GREENFIELD-001-STEP2B4B-hosted-workflow-final-text-evidence.md
- Do not retrieve STEP2A, STEP2B1, earlier step outputs, or the charter.
- This prompt is self-contained.
- This is one integrated task. Do not split it into one task per report merely
  because three reports are involved.

Purpose:
Review the complete text layers of three related archived reports as one
coherent evidence batch:

1. theoretical and engineering justification for external persistent memory;
2. real practices and limits in non-development long-term dialogue;
3. transferability of development-oriented persistent-memory practices to
   ordinary dialogue, learning, and research scenarios.

The task must determine:

- which underlying principles are supported independently of any product;
- which non-development practices have real evidence versus being proposals;
- which development practices transfer directly;
- which practices require adaptation;
- which practices should not be transferred;
- which conclusions remain dated, source-limited, or report-dependent.

This is a repository-bounded document-evidence review.

It must not:
- perform new external research;
- verify current product behavior through the web;
- rank models, vendors, or services;
- investigate model internals or training;
- design the Mnemosyne architecture;
- compare against the existing GPT-produced design;
- recommend or perform repairs;
- begin GF-STEP-3.

────────────────────────────────────
1. Allowed inputs
────────────────────────────────────

Allowed attachment:

- FABLE5-GREENFIELD-001-STEP2B4B-hosted-workflow-final-text-evidence.md

Use the attachment only for:

- track and step continuity;
- current research-domain and STEP-1 need identifiers;
- the distinction between report evidence and execution source;
- text-only, date, visual, authority, and prohibited-overclaim rules;
- confirmation that the first STEP2A source batch has been completed.

Do not use its hosted-workflow conclusions as substitutes for evidence in the
three reports being reviewed here.

Allowed repository sources — exactly these three paths:

A. RPT-2026Q2-0006 — theory and engineering basis

- path:
  raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 5：外部持久记忆的理论与工程依据.pdf
- ref: master
- expected blob SHA:
  406246cd4b172d490849830b4e8f1d674c513c4f

B. RPT-2026Q2-0002 — non-development long-term dialogue practices

- path:
  raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 1：非开发长期对话记忆是否已有真实实践.pdf
- ref: master
- expected blob SHA:
  a5c38087536d49459ee4d7d36a93a04c4bdc3c94

C. RPT-2026Q2-0007 — transfer from development to dialogue and learning

- path:
  raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 6：开发场景的持久记忆经验能否迁移到普通长期对话和学习场景.pdf
- ref: master
- expected blob SHA:
  c4e0b43647da84411a52cc3a70ee046217a0b7e3

Read no other repository path.

Do not open:

- any other original report;
- any report summary, summary index, or research prompt;
- pdf-figure-review-index.md;
- current/**;
- handoff/**;
- notes/**;
- commands/**;
- task-result records;
- Fable review records;
- existing design documents;
- external websites.

References and URLs inside the reports are report-internal metadata only. Do not
open them.

────────────────────────────────────
2. Source integrity and access table
────────────────────────────────────

Before substantive analysis, create one source-access row per report.

For each report record:

- report_id
- repository_path
- expected_blob_sha
- observed_blob_sha
- sha_match: true | false
- page_count_if_available
- extracted_text_size_if_available
- text_layer_usable: true | false
- extraction_complete_and_untruncated: true | false | uncertain
- execution_mode:
    full_text_mode |
    core_text_mode |
    inaccessible
- retrieval_battery
- notes

Maximum retrieval/query batteries: 3 — one per source.

If a SHA does not match:

- do not use that changed report;
- do not search for a replacement;
- continue with the reports whose SHAs match;
- make the final status reflect the missing verified source.

Do not repeatedly retry extraction.

────────────────────────────────────
3. PDF text handling
────────────────────────────────────

For each report independently, prefer full_text_mode.

Use full_text_mode when:

- a usable embedded text layer exists;
- the report is no more than approximately 15 pages;
- extracted text is no more than approximately 45,000 characters or
  approximately 8,000 words;
- complete reading appears feasible within this task.

Use core_text_mode only when:

- a report clearly exceeds either threshold;
- text size cannot be determined reliably;
- extraction is unusually costly;
- reading the whole text would endanger completion of the integrated artifact.

In core_text_mode inspect:

- title and stated scope;
- executive summary or introduction;
- heading structure;
- sections directly relevant to this task;
- limitations;
- conclusion and recommendations.

If core_text_mode is used:

- state exactly what was and was not inspected;
- do not claim full-report coverage;
- do not automatically create a separate micro-step;
- list a residual source dependency only when the unread text could conceal a
  load-bearing contradiction or missing principle.

PDF rules:

- embedded text extraction only;
- no OCR;
- no screenshots;
- no interpretation of images, visual tables, diagrams, charts, or layout;
- textually extracted tables may be used only when unambiguous;
- every report-derived evidence item must be marked text_only;
- visual-dependent meaning remains unverified.

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
- empirical_or_practice_example
- framing_assumption_to_verify
- mixed_or_uncertain

Apply all of these rules:

1. Each report is research evidence, not execution source.
2. A cited external source is not independently verified here.
3. A theoretical argument is not automatically empirical validation.
4. A real-world example does not establish broad prevalence.
5. A report recommendation is not an accepted Mnemosyne requirement.
6. Product or workflow observations retain their named surface and evidence
   period.
7. Development workflows must not be assumed transferable without adaptation.
8. Similar terminology across reports does not prove identical semantics.
9. Separate:
   - underlying user need;
   - low-drift principle;
   - observed practice;
   - candidate mechanism;
   - adaptation requirement;
   - user decision.
10. Do not update the reports using your own current knowledge.
11. Do not discuss your own training cutoff, internal capabilities, or hidden
    context.
12. Do not import current Mnemosyne design details.

────────────────────────────────────
5. RPT-2026Q2-0006 evidence register
────────────────────────────────────

Create at most 7 evidence records.

Use IDs:

F2B5-T01 through F2B5-T07

Focus on theoretical or engineering claims concerning:

- external versus internal state;
- durable state across process or session boundaries;
- separation of computation and persistent storage;
- versioning, provenance, reproducibility, rollback, and auditability;
- retrieval rather than loading all material into active context;
- consistency, reconciliation, stale state, and conflict;
- limits of context windows or platform-owned memory as truth sources;
- why file/Git/database/RAG mechanisms may or may not be justified;
- trade-offs and failure modes of externalization.

For every record include:

- evidence_id
- source_anchor
- concise_statement
- evidence_category
- principle_scope
- source_evidence_date_or_period
- text_only: true
- visual_review_status: not_performed
- confidence_as_report_evidence:
    high |
    medium |
    low
- low_drift_status:
    low_drift |
    partly_date_sensitive |
    date_sensitive
- empirical_support_in_this_report:
    present |
    limited |
    absent |
    uncertain
- related_research_domain_ids
- related_STEP1_need_ids
- supports_or_challenges_S01
- prohibited_overclaim
- notes

Do not fill the allowance unless justified.

────────────────────────────────────
6. RPT-2026Q2-0002 evidence register
────────────────────────────────────

Create at most 6 evidence records.

Use IDs:

F2B5-ND01 through F2B5-ND06

Focus on non-development long-term dialogue, learning, and research practices:

- actual documented practices;
- manual or semi-manual continuity methods;
- project notebooks, journals, knowledge bases, summaries, handoff packages,
  retrieval systems, or other external state;
- platform-provided containers versus user-controlled records;
- evidence of repeated use, maturity, or failure;
- human maintenance burden;
- privacy, visibility, and correction concerns;
- limits on calling a practice “persistent memory.”

For every record include:

- evidence_id
- source_anchor
- concise_statement
- evidence_category
- practice_or_scenario_scope
- practice_evidence_strength:
    documented_practice |
    limited_example |
    proposal_only |
    unclear
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
- related_research_domain_ids
- related_STEP1_need_ids
- prohibited_overclaim
- notes

Do not infer broad adoption from isolated examples.

────────────────────────────────────
7. RPT-2026Q2-0007 transfer evidence register
────────────────────────────────────

Create at most 7 evidence records.

Use IDs:

F2B5-TR01 through F2B5-TR07

For each candidate transferred practice, determine whether it is:

- directly_transferable
- transferable_with_adaptation
- weakly_transferable
- not_transferable
- evidence_insufficient

Relevant practices may include:

- external source-of-truth files;
- version history and provenance;
- structured state and handoff records;
- diff/review workflows;
- tests and validation;
- instruction files;
- issue/task tracking;
- retrieval and indexing;
- approval gates;
- branching and rollback;
- automated write-back.

For every record include:

- evidence_id
- source_anchor
- practice_or_principle
- transfer_status
- development_context_role
- nondevelopment_target_context
- required_adaptation
- transfer_failure_risk
- evidence_category
- source_evidence_date_or_period
- text_only: true
- visual_review_status: not_performed
- confidence_as_report_evidence:
    high |
    medium |
    low
- related_research_domain_ids
- related_STEP1_need_ids
- prohibited_overclaim
- notes

Do not convert a possible analogy into a validated transfer rule.

────────────────────────────────────
8. Reassess S-01
────────────────────────────────────

Current working wording from GF-STEP-2B1:

Externalized, versioned files can carry durable project state across sessions
and tool surfaces; active model context or platform-provided memory must not be
treated as the sole auditable project truth source. Externalization alone does
not guarantee memory quality and still requires retrieval, governance,
reconciliation, and review.

Use primarily RPT-2026Q2-0006, with 0002 and 0007 as corroborating or
challenging evidence.

Choose exactly one:

- batch_reports_confirm
- batch_reports_refine
- batch_reports_partially_support
- batch_reports_challenge
- batch_reports_do_not_resolve

Record:

- signal_id: S-01
- previous_wording
- disposition
- replacement_wording_if_refined
- supporting_F2B5_evidence_ids
- theoretical_basis
- observed_practice_basis
- cross_scenario_transfer_basis
- low_drift_scope
- date_sensitive_scope
- remaining_visual_dependency
- remaining_original_report_dependency
- remaining_external_refresh_dependency
- prohibited_overclaim

Do not reassess S-02 through S-05.

────────────────────────────────────
9. Integrated theory–practice–transfer matrix
────────────────────────────────────

Create at most 10 rows.

For each row include:

- concern
- theory_report_evidence_ids
- nondevelopment_practice_evidence_ids
- transfer_report_evidence_ids
- integrated_statement
- evidence_alignment:
    convergent |
    partially_convergent |
    tension |
    single_report_only |
    unresolved
- status:
    supported_principle |
    bounded_practice |
    adaptation_required |
    candidate_only |
    open_question
- what_must_not_be_claimed
- later_evidence_needed

Include only concerns materially supported by at least one report.

Potential concerns include:

- external state as durable continuity;
- auditability and provenance;
- user-controlled versus platform-owned state;
- retrieval and context-budget management;
- version history and rollback;
- human confirmation and correction;
- handoff;
- testing and validation;
- non-development usability burden;
- privacy and visibility;
- portability;
- stale or conflicting memory.

This matrix is evidence synthesis, not architecture design.

────────────────────────────────────
10. Non-development boundary statements
────────────────────────────────────

Create a compact register of at most 6 boundary statements.

Use IDs:

B5-ND-B01 and upward

For every statement include:

- boundary_id
- concise_statement
- supporting_evidence_ids
- applies_to
- does_not_apply_to
- evidence_strength:
    strong |
    moderate |
    weak
- user_decision_still_required
- report_or_refresh_dependency
- prohibited_overclaim

Examples of acceptable boundary types:

- manual continuity is feasible but not automatic;
- user-controlled records improve auditability but increase maintenance burden;
- platform containers are useful but do not automatically become portable
  project truth;
- practices documented in learning or research settings may not generalize to
  every long-term dialogue.

Do not state product facts beyond the reports.

────────────────────────────────────
11. STEP-1 linkage delta
────────────────────────────────────

Record material evidence-coverage changes for at most 8 of:

- GF1A-N01
- GF1A-N03
- GF1A-N04
- GF1A-N09
- GF1A-N10
- GF1A-N11
- GF1A-N12
- GF1B-N13
- GF1B-N15
- GF1C-N19

For each selected item:

- need_id
- coverage_before_this_batch
- coverage_after_this_batch
- supporting_F2B5_evidence_ids
- remaining_report_dependency
- method_selection_or_user_decision_not_resolved

Do not reproduce the complete need text.

────────────────────────────────────
12. Contradiction, weakness, and uncertainty register
────────────────────────────────────

Create at most 8 items covering:

- theoretical claims lacking empirical support;
- examples whose prevalence is unclear;
- conflicting recommendations;
- development assumptions that fail in non-development settings;
- product-dependent or dated observations;
- high human-maintenance burdens;
- missing failure or longitudinal evidence;
- visual material not reviewed;
- report reliance on unverified cited sources.

For each item:

- issue_id
- affected_report_ids
- source_anchor
- issue_type
- description
- affected_evidence_ids
- handling_for_later_GF_STEP_2

Do not resolve uncertainty by inference.

────────────────────────────────────
13. Principle, practice, and recommendation separation
────────────────────────────────────

Create a compact classification table with these classes:

- low_drift_engineering_principle
- observed_or_documented_practice
- dated_product_or_workflow_observation
- report_recommendation
- analogy_or_transfer_hypothesis
- unresolved_question

For each row state:

- item_or_evidence_ids
- class
- concise_content
- may_enter_final_STEP2_without_external_refresh:
    yes |
    yes_with_date_caveat |
    no
- further_original_report_needed
- later_delta_research_needed

Do not merge recommendations into findings.

────────────────────────────────────
14. Status determination
────────────────────────────────────

Choose exactly one:

- GF_STEP_2B5_complete_batch2_text_review_ready_for_supplemental_batch
- GF_STEP_2B5_complete_with_explicit_partial_report_coverage
- GF_STEP_2B5_incomplete_source_integrity_failure
- GF_STEP_2B5_incomplete_unusable_text_layer
- GF_STEP_2B5_incomplete_other_specific_gap

Do not declare GF-STEP-2 complete.

Completion requires:

- all three SHAs match;
- all three usable text layers are reviewed under the declared mode;
- S-01 receives a batch-level disposition;
- theory, practice, and transfer claims remain separately classified;
- any partial coverage is explicit;
- visual and freshness dependencies are preserved.

If complete, propose one integrated next step for the supplemental report batch.
Do not execute it and do not split it into micro-steps unless one supplemental
report is inaccessible or anomalously large.

────────────────────────────────────
15. Hard workload limits
────────────────────────────────────

- repository paths: exactly 3
- retrieval/query batteries: maximum 3
- PDF reports opened: exactly 3
- RPT-0006 evidence records: maximum 7
- RPT-0002 evidence records: maximum 6
- RPT-0007 evidence records: maximum 7
- total evidence records: maximum 18
- integrated matrix rows: maximum 10
- non-development boundary statements: maximum 6
- STEP-1 linkage entries: maximum 8
- uncertainty items: maximum 8
- final signal dispositions: exactly S-01
- no OCR
- no visual inspection
- no other report, summary, prompt, or index read
- no web or external research
- Research mode OFF
- no automatic continuation

Word-budget policy:

- soft target: 2,800–4,000 words
- hard cap: 4,800 words
- the soft target is advisory
- a complete first draft within the hard cap is acceptable
- at most one light compression pass, only if the hard cap is exceeded
- remove repeated report narration before evidence records, matrices,
  uncertainty, or disposition
- do not silently omit one of the three reports
- perform one approximate word-count check only
- do not repeat counting or compression because methods differ

────────────────────────────────────
16. Required downloadable file
────────────────────────────────────

Create exactly:

FABLE5-GREENFIELD-001-STEP2B5-theory-nondev-transfer-evidence.md

Required sections:

1. Metadata
2. Scope and hard limits
3. Allowed sources and anti-contamination policy
4. Source integrity and access table
5. PDF text-handling and coverage record
6. RPT-2026Q2-0006 theory evidence register
7. RPT-2026Q2-0002 non-development practice evidence register
8. RPT-2026Q2-0007 transfer evidence register
9. S-01 batch reassessment
10. Integrated theory–practice–transfer matrix
11. Non-development boundary statements
12. STEP-1 linkage delta
13. Contradiction, weakness, and uncertainty register
14. Principle/practice/recommendation classification
15. Visual, date, scope, and evidence limitations
16. Status determination and bounded continuation
17. Boundary statement

Metadata:

charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2B5
record_type: theory_nondevelopment_practice_and_transfer_batch_review
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-2B4B
research_mode: false
source_files:
  - report_id: RPT-2026Q2-0006
    path: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 5：外部持久记忆的理论与工程依据.pdf
    expected_blob_sha: 406246cd4b172d490849830b4e8f1d674c513c4f
  - report_id: RPT-2026Q2-0002
    path: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 1：非开发长期对话记忆是否已有真实实践.pdf
    expected_blob_sha: a5c38087536d49459ee4d7d36a93a04c4bdc3c94
  - report_id: RPT-2026Q2-0007
    path: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 6：开发场景的持久记忆经验能否迁移到普通长期对话和学习场景.pdf
    expected_blob_sha: c4e0b43647da84411a52cc3a70ee046217a0b7e3

The coverage section must state:

- expected and observed SHA for every report;
- text-layer usability for every report;
- execution mode for every report;
- page/text size when available;
- complete or partial text coverage for every report;
- retrieval batteries used;
- evidence-record count by report;
- S-01 disposition;
- visual review not performed;
- remaining freshness or source dependencies;
- completion status.

────────────────────────────────────
17. Chat response
────────────────────────────────────

After presenting the file, state briefly:

- completion within limits;
- SHA result for all three reports;
- execution mode and text coverage for each report;
- evidence-record count for each report and total;
- S-01 disposition;
- integrated matrix row count;
- non-development boundary count;
- retrieval batteries used;
- visual inspection performed: no;
- approximate word count;
- status determination;
- proposed next integrated batch;
- downloadable file result.

Do not repeat the file body.

────────────────────────────────────
18. Boundary
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
- begin architecture work or GF-STEP-3;
- create target-project artifacts;
- resume or close the paused route.

This output is non-execution-source advisory evidence only.
Stop after the downloadable file and brief summary.
