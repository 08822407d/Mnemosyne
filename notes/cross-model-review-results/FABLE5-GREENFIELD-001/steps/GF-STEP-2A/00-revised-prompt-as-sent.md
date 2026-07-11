# FABLE5-GREENFIELD-001 — GF-STEP-2A Revised Prompt as Sent

```text
Run the next bounded substep of FABLE5-GREENFIELD-001.

step_id: GF-STEP-2A
step_name: research_evidence_catalog_and_staged_reading_plan
relationship_to_charter: planning substep for GF-STEP-2; not completion of
GF-STEP-2

Execution setting:
- Research mode must remain OFF.
- Continue in the same conversation.
- Attach:
  FABLE5-GREENFIELD-001-STEP1E-second-tier-prompts-and-final-closure.md
- Do not retrieve the charter from repository notes or conversation history.
- This prompt is self-contained.

Purpose:
Organize the repository's existing research evidence before later design work.

This step only catalogs reports, maps them to the needs recorded in STEP-1,
records evidence limitations, and chooses a small group of original reports for
the next reading step.

It does not evaluate any model or service, produce a final technical baseline,
perform external research, design an architecture, or recommend changes to the
existing project.

────────────────────────────────────
1. Allowed inputs
────────────────────────────────────

Allowed attachment:

- FABLE5-GREENFIELD-001-STEP1E-second-tier-prompts-and-final-closure.md

Use it only to:
- reference the final STEP-1 need IDs;
- identify which research topics relate to those needs;
- preserve the open-question references;
- avoid introducing unrelated topics.

Allowed repository files — exactly these three paths:

A. Research-cycle motivation

- path:
  raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md
- ref: master
- expected blob SHA:
  f90f4854f8cdac903d919d6918d49e667e812f3f

B. Current research-report index

- path:
  raw/research-reports/current/research-report-index.md
- ref: master
- expected blob SHA:
  0efc2af50cd4ef37abb93aa67b33fdd4c812c9be

C. Current report-summary index

- path:
  raw/research-reports/current/current-report-summaries.md
- ref: master
- expected blob SHA:
  f22906d36613c70b686f5121f9b1d8e5091dab0b

Read no other repository file.

Do not open:
- any original research report;
- any individual report-summary file;
- any research-prompt file;
- any PDF;
- any visual-review index;
- current/**;
- handoff/**;
- notes/**;
- commands/**;
- manual-import-inbox/**;
- task-result records;
- existing design documents;
- external websites.

If an allowed file mentions another path, record its name as metadata only.
Do not open it.

────────────────────────────────────
2. Source-status rules
────────────────────────────────────

Keep these source classes separate:

- motivation_context:
  explains why a research topic exists;
  not a research result.

- report_index_metadata:
  report ID, cycle, path, format, topic, active status and review notes;
  not a substantive result.

- summary_index_signal:
  a conclusion or implication explicitly stated in the summary index;
  useful for planning but weaker than the original report.

- original_report_needed:
  the present sources are insufficient for a load-bearing statement.

- visual_check_needed:
  a PDF may contain relevant tables, figures or layout that have not been
  reviewed.

- date_refresh_candidate:
  a product or workflow statement may have changed since the evidence cycle.

Never:
- treat motivation text as a report conclusion;
- claim that an original report was read;
- treat a summary as stronger than its original;
- treat an unreviewed PDF figure as verified evidence;
- treat any report as execution source;
- turn a report topic into a detailed technical claim.

────────────────────────────────────
3. Report inventory
────────────────────────────────────

Inventory all active reports found in the allowed sources.

The expected IDs are:

Initial cycle:
- RPT-2026Q2-0001
- RPT-2026Q2-0002
- RPT-2026Q2-0003
- RPT-2026Q2-0004
- RPT-2026Q2-0005
- RPT-2026Q2-0006
- RPT-2026Q2-0007

Supplemental cycles:
- RPT-2026Q2-MT-0001
- RPT-2026Q2-HO-0001
- RPT-2026Q2-UIG-0001
- RPT-2026Q2-FTDRE-0001

Include another report only if one of the allowed indexes marks it as active.

For every report record:

- report_id
- cycle_id
- topic_as_listed
- report_type
- original_report_path
- summary_path_or_none
- active_evidence
- source_format:
    txt |
    markdown |
    pdf |
    other
- summary_status
- visual_review_status
- related_research_domains
- related_STEP1_need_ids
- planning_value:
    foundational |
    high |
    medium |
    low
- proposed_reading_batch:
    batch_1 |
    batch_2 |
    batch_3 |
    defer_unless_needed
- reason_for_priority
- date_sensitivity:
    high |
    medium |
    low
- notes

Do not put every report in batch 1.

────────────────────────────────────
4. Research-domain map
────────────────────────────────────

Use these neutral research domains:

- RD-01:
  ordinary conversation continuity and platform-provided memory

- RD-02:
  non-development long-term dialogue, learning and research

- RD-03:
  local project-file workflows

- RD-04:
  hosted repository and review workflows

- RD-05:
  external file and version-history engineering basis

- RD-06:
  transfer between development and non-development scenarios

- RD-07:
  quality assurance, issue detection and evaluation evidence

- RD-08:
  handoff and continuation between sessions and tools

- RD-09:
  user-input handling, visibility, redaction and external references

- RD-10:
  first-target trial evaluation and decision boundaries

- RD-11:
  overall feasibility and scope of an external-memory meta-agent

For each domain record:

- domain_id
- domain_title
- related_STEP1_need_ids
- relevant_report_ids
- evidence_level_currently_available
- original_reports_needed
- visual_check_dependency
- date_sensitivity
- why_the_domain_matters

Do not write a final rule or design recommendation for the domain.

────────────────────────────────────
5. Preliminary evidence-signal register
────────────────────────────────────

Create at most 16 preliminary evidence signals.

Each signal must contain:

- signal_id
- concise_signal
- domain_id
- source_report_ids
- current_source_level:
    motivation_only |
    index_only |
    summary_index |
    mixed
- current_confidence:
    high |
    medium |
    low
- original_report_needed:
    yes |
    no |
    uncertain
- visual_check_possible:
    yes |
    no |
    uncertain
- date_refresh_possible:
    yes |
    no |
    uncertain
- claim_boundary_note
- related_STEP1_need_ids

A signal is only a planning item. It must not be phrased as a final factual rule.

Do not add signals merely to reach the maximum.

────────────────────────────────────
6. STEP-1 linkage
────────────────────────────────────

Create a compact linkage table for:

- GF1A-N01 through GF1A-N12;
- GF1B-N13 through GF1B-N18;
- GF1C-N19 through GF1C-N21.

For every need record:

- need_id
- related_research_domains
- present_evidence_coverage:
    apparently_covered |
    partially_covered |
    not_yet_covered |
    user_decision_not_research_fact
- report_ids_to_read
- related_open_questions
- handling_note_for_later_STEP2_work

Do not reproduce the full need descriptions.

Keep user choices separate from research evidence. Examples of user choices
include approval granularity, language preference, first-target identity,
storage-product preference and handoff-trigger preference.

────────────────────────────────────
7. Visual-review limitation register
────────────────────────────────────

For every PDF report record:

- report_id
- visual_review_status
- possible_unreviewed_material:
    table |
    figure |
    image |
    layout |
    unknown
- may_text_only_reading_be_used:
    yes_with_caveat |
    no |
    uncertain
- required_handling_before_visual_dependent_claim
- related_domain_ids

Do not inspect the PDFs in this step.

────────────────────────────────────
8. Date-sensitivity register
────────────────────────────────────

Identify statements that might require a later date refresh.

For each item:

- item_id
- affected_report_ids
- affected_domain_ids
- category:
    product_behavior |
    workflow_behavior |
    service_limit |
    stable_engineering_principle
- why_it_may_change_or_remain_stable
- evidence_cycle
- refresh_before_final_STEP2_output:
    yes |
    no |
    uncertain
- proposed_handling:
    use_with_date_note |
    read_original_first |
    later_separate_refresh |
    stable_enough
- external_check_performed_now: false

Do not perform any external check in this step.

Maximum items: 10.

────────────────────────────────────
9. Staged original-report reading plan
────────────────────────────────────

Choose a first original-report batch for GF-STEP-2B.

Rules:

- select at most 4 reports;
- choose one coherent group;
- explain why each report is required now;
- state which research domains it covers;
- state which preliminary signals it may confirm, refine or reject;
- copy the exact original-report path from the index;
- mark that its current blob SHA must be obtained before STEP2B;
- state whether a PDF needs a separate visual check;
- explicitly list reports deferred to later batches.

A coherent first group may focus on one of these:

- ordinary conversation and project-file workflows;
- engineering basis and cross-scenario transfer;
- quality assurance, handoff, input handling and first-target trial evidence.

Choose the smallest group that materially advances STEP-2.

Do not read the selected reports now.

────────────────────────────────────
10. Status determination
────────────────────────────────────

Choose one:

- GF_STEP_2A_complete_source_map_ready_for_STEP2B
- GF_STEP_2A_incomplete_source_index_gap
- GF_STEP_2A_incomplete_integrity_failure
- GF_STEP_2A_incomplete_other_specific_gap

Do not declare GF-STEP-2 complete.

STEP2A is complete only if:

- all three source SHAs match;
- every active report is inventoried;
- every research domain has a source plan;
- source-strength distinctions are explicit;
- PDF and date limitations are recorded;
- no more than four reports are selected for STEP2B.

If incomplete, identify the exact missing item. Do not search elsewhere.

────────────────────────────────────
11. Workload limits
────────────────────────────────────

- repository paths: exactly 3
- retrieval batteries: maximum 3
- expected active reports: 11
- research domains: 11
- preliminary signals: maximum 16
- date-sensitivity items: maximum 10
- STEP2B reports selected: maximum 4
- no original-report reads
- no individual-summary reads
- no prompt reads
- no PDF reads
- no external search
- Research mode OFF
- no automatic continuation into STEP2B
- stop after the downloadable file and brief chat summary

Word-budget policy:

- soft target: 1,800–2,800 words
- hard cap: 3,400 words
- the soft target is advisory
- a complete first draft within the hard cap is acceptable
- at most one light compression pass
- preserve the full report inventory and reading rationale
- use compact tables
- never omit an active report
- perform no more than one approximate word-count check
- do not repeat compression solely because counting methods differ

────────────────────────────────────
12. Required file
────────────────────────────────────

Create a downloadable Markdown file named exactly:

FABLE5-GREENFIELD-001-STEP2A-research-source-map.md

Required sections:

1. Metadata
2. Scope and limits
3. Allowed sources and anti-contamination policy
4. Source-status rules
5. Source-access and SHA table
6. Active-report inventory
7. Research-domain map
8. Preliminary evidence-signal register
9. STEP-1 linkage table
10. Visual-review limitation register
11. Date-sensitivity register
12. Recommended STEP2B source set
13. Deferred-report batches
14. Incidental-exposure ledger
15. Coverage and limitations
16. STEP2A status determination
17. Proposed bounded STEP2B
18. Boundary statement

Metadata:

charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2A
record_type: research_evidence_catalog_and_read_plan
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-1E
GF_STEP_1_status: complete_with_explicit_open_questions
research_mode: false
source_files:
  - path: raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md
    expected_blob_sha: f90f4854f8cdac903d919d6918d49e667e812f3f
  - path: raw/research-reports/current/research-report-index.md
    expected_blob_sha: 0efc2af50cd4ef37abb93aa67b33fdd4c812c9be
  - path: raw/research-reports/current/current-report-summaries.md
    expected_blob_sha: f22906d36613c70b686f5121f9b1d8e5091dab0b

The coverage section must state:

- SHA result for each source;
- whether each source was completely read;
- retrieval batteries used;
- active reports inventoried;
- domains mapped;
- preliminary signals recorded;
- PDF limitations recorded;
- date-sensitive items recorded;
- reports selected for STEP2B;
- reports deferred;
- whether STEP2A completed.

────────────────────────────────────
13. File discipline
────────────────────────────────────

Include only:

- source metadata;
- evidence-strength distinctions;
- report and domain mappings;
- qualified preliminary signals;
- limitations;
- staged reading plan.

Do not include:

- hidden reasoning;
- connector logs;
- conclusions absent from the allowed sources;
- external-search material;
- architecture proposals;
- changes to the existing project;
- artifact-control text;
- duplicated file-presentation messages.

Before presenting the file:

- perform one structural check;
- perform one approximate word-count check;
- confirm all active reports are inventoried;
- confirm no more than four STEP2B reports were selected;
- confirm the ending is clean.

────────────────────────────────────
14. Chat response
────────────────────────────────────

After creating the file, briefly state:

- whether the task completed within limits;
- SHA result for all three sources;
- active reports inventoried;
- research domains mapped;
- preliminary signals recorded;
- PDF limitations recorded;
- date-sensitive items recorded;
- report IDs selected for STEP2B;
- reports deferred;
- retrieval batteries used;
- incidental exposure, if any;
- approximate word count;
- STEP2A status;
- downloadable file creation result.

Do not repeat the file body in chat.

────────────────────────────────────
15. Boundary
────────────────────────────────────

Do not:

- write repository files;
- generate other execution tasks;
- update execution source;
- inspect an original research report;
- inspect an individual report summary;
- inspect a PDF;
- perform external research;
- compare or change the existing design;
- begin architecture work;
- create target-project artifacts;
- resume or close the paused route.

This output is non-execution-source advisory evidence only.
Stop after the downloadable file and brief chat summary.
```
