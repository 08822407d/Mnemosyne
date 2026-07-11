# FABLE5-GREENFIELD-001 — GF-STEP-2B1 Prompt as Sent

```text
Run the next bounded substep of FABLE5-GREENFIELD-001.

step_id: GF-STEP-2B1
step_name: foundational_external_memory_report_evidence_review
relationship_to_charter:
  first original-report reading substep of GF-STEP-2;
  continuation of GF-STEP-2A;
  not completion of GF-STEP-2

Execution setting:
- Research mode must remain OFF.
- Continue in the same successful Fable 5 conversation that produced STEP2A.
- Use the STEP2A deliverable already present in that conversation:
  FABLE5-GREENFIELD-001-STEP2A-research-source-map.md
- If this is instead executed in a fresh conversation, the user will attach
  that STEP2A file.
- Do not retrieve the charter from repository notes or conversation history.
- This prompt is self-contained.

Purpose:
Read one archived original research report and record what that report actually
supports about external persistent project memory and related workflow
assumptions.

This is a bounded document-evidence review.

It does not:
- evaluate or rank AI models or vendors;
- investigate model internals or training processes;
- build a general model-capability dataset;
- verify current product behavior through the web;
- design the Mnemosyne architecture;
- compare against the current GPT-produced design;
- recommend repairs.

The goal is to establish the foundational report-evidence layer before the more
specific conversation, local-file, and hosted-repository reports are read in
later substeps.

────────────────────────────────────
1. Allowed inputs
────────────────────────────────────

Allowed prior-step input:

- FABLE5-GREENFIELD-001-STEP2A-research-source-map.md
  already present in this conversation, or attached if this is a fresh
  conversation.

Use STEP2A only for:
- report and research-domain identifiers;
- preliminary signal IDs;
- STEP-1 need IDs;
- source-strength, PDF, and freshness rules;
- continuation boundaries.

Allowed repository source — exactly one path:

- path:
  raw/research-reports/cycles/2026Q2-initial/originals/AI agent 长期记忆系统 pro深度研究.txt
- ref: master
- expected blob SHA:
  1c4a48c53d7ac126eb29a0ea7ab1e0e8a0f5c82a

Read no other repository path.

Do not open:
- any PDF;
- any other original research report;
- any report summary or summary index;
- any research prompt;
- any report-topic map or motivation file;
- current/**;
- handoff/**;
- notes/**;
- commands/**;
- manual-import-inbox/**;
- task-result records;
- FABLE5 review or triage records;
- existing design documents;
- external websites.

If the allowed report names another file, source, product, task, design element,
or repository path, record the reference as report-internal metadata only.
Do not open it.

────────────────────────────────────
2. Source integrity and access
────────────────────────────────────

Before using the report:

- obtain the observed Git blob SHA;
- compare it with the expected SHA;
- state whether the complete text file was inspected;
- record the report's own stated evidence date or cutoff;
- record any access truncation or unreadable section.

If the SHA does not match:
- do not silently use the changed file;
- do not search for a replacement;
- create a short integrity-failure deliverable and stop.

Maximum repository retrieval/query batteries: 2.

────────────────────────────────────
3. Evidence interpretation rules
────────────────────────────────────

Classify extracted material using only:

- report_direct_finding
- report_author_synthesis
- report_recommendation
- cited_external_claim_not_independently_checked
- dated_product_or_workflow_statement
- low_drift_engineering_principle
- mixed_or_uncertain

Apply these rules:

1. The report is research evidence, not execution source.
2. A cited vendor statement is not independently verified merely because the
   report cites it.
3. A recommendation is not a confirmed capability fact.
4. A product or workflow statement must retain its evidence date and scope.
5. Do not turn a statement about one interface, product mode, or evidence date
   into a universal claim.
6. Separate:
   - low-drift engineering principles;
   - current-product observations;
   - report recommendations;
   - unresolved uncertainty.
7. Do not use your own training knowledge or current product knowledge to
   update, correct, or supplement the report.
8. Do not discuss your own training cutoff, hidden context, internal
   capabilities, or model comparisons.
9. Do not treat the report as proving that every project should use GitHub.
10. Do not import implementation details from the existing Mnemosyne design.

────────────────────────────────────
4. Report coverage map
────────────────────────────────────

Create a compact coverage map of the report.

For each major report section or thematic group record:

- section_or_anchor
- topic
- inspected:
    yes |
    partial |
    no
- reason_if_partial_or_no
- relevant_research_domain_ids
- relevant_STEP1_need_ids
- candidate_evidence_item_ids

Do not reproduce the report's table of contents verbatim.

The coverage map must be sufficient to show whether the complete report was
actually inspected.

────────────────────────────────────
5. Foundational evidence register
────────────────────────────────────

Extract at most 14 load-bearing evidence items.

Prefer items relevant to:

- RD-01 ordinary conversation continuity;
- RD-03 local project-file workflows;
- RD-04 hosted repository and review workflows;
- RD-05 external file and version-history engineering basis;
- RD-11 overall external-memory/meta-agent feasibility.

For each item record:

- evidence_id:
    F2B1-E01 and upward
- source_anchor
- concise_statement
- evidence_category
- scope:
    engineering_principle |
    conversation_surface |
    local_project_workflow |
    hosted_repository_workflow |
    cross_surface |
    governance
- report_evidence_date_or_cutoff
- confidence_as_report_evidence:
    high |
    medium |
    low
- underlying_source_independently_checked_in_this_step: false
- date_sensitivity:
    high |
    medium |
    low
- related_research_domain_ids
- related_STEP1_need_ids
- supports_or_challenges_preliminary_signal_ids
- prohibited_overclaim
- notes

Do not add entries merely to reach the allowance.

Short source excerpts are allowed, but do not reproduce long passages.

────────────────────────────────────
6. STEP2A signal reassessment
────────────────────────────────────

Reassess these STEP2A preliminary signals:

- S-01:
  model context/internal memory is not a long-term project truth source;
  external versioned files carry persistent state.

- S-02:
  plain conversation surfaces must not be assumed to write repository state
  automatically.

- S-03:
  platform-provided memory is auxiliary rather than the project truth source.

For each select one:

- report_confirmed
- report_refined
- report_partially_supported
- report_challenged
- report_does_not_resolve

Record:

- signal_id
- previous_wording
- disposition
- replacement_wording_if_refined
- supporting_evidence_ids
- evidence_scope
- date_caveat
- remaining_original_report_dependency
- remaining_refresh_dependency
- prohibited_overclaim

The report may also contain broad material relevant to S-04 or S-05.

If so:
- record it only as preliminary corroboration;
- do not mark S-04 or S-05 confirmed;
- their dedicated reports remain unread.

────────────────────────────────────
7. Principle-versus-product separation
────────────────────────────────────

Create a table with three classes:

A. low_drift_principles
B. dated_product_or_workflow_observations
C. report_recommendations_or_design_options

For each entry state:

- evidence_id
- class
- concise_content
- why_it_belongs_in_this_class
- may_be_used_in_final_STEP2_without_external_refresh:
    yes |
    yes_with_date_caveat |
    no
- later_source_needed

Do not perform the external refresh now.

────────────────────────────────────
8. Contradiction and uncertainty register
────────────────────────────────────

Record:

- contradictions within the report;
- tensions between findings and recommendations;
- claims based mainly on vendor documentation;
- claims whose applicability depends on the interaction surface;
- claims whose freshness is load-bearing;
- areas the report explicitly leaves uncertain.

For each item:

- issue_id
- source_anchor
- issue_type
- description
- affected_evidence_ids
- handling_for_later_STEP2

If none are found, state that explicitly.

────────────────────────────────────
9. STEP-1 linkage delta
────────────────────────────────────

Using STEP2A's linkage table, record only changes in evidence coverage for:

- GF1A-N01
- GF1A-N02
- GF1A-N04
- GF1A-N09
- GF1A-N10
- GF1B-N15

For each:

- need_id
- previous_coverage
- coverage_after_this_report
- supporting_evidence_ids
- remaining_report_dependencies
- user_decision_not_resolved_by_evidence

Do not reproduce unchanged STEP-1 need descriptions.

────────────────────────────────────
10. Deferred sources
────────────────────────────────────

Explicitly keep these reports unread:

- RPT-2026Q2-0003
- RPT-2026Q2-0004
- RPT-2026Q2-0005
- every STEP2A batch-2 and batch-3 report

State what the present report cannot settle without them.

Do not automatically continue into another report.

────────────────────────────────────
11. Status determination
────────────────────────────────────

Choose one:

- GF_STEP_2B1_complete_foundational_report_review_ready_for_STEP2B2
- GF_STEP_2B1_incomplete_source_integrity_failure
- GF_STEP_2B1_incomplete_access_or_truncation
- GF_STEP_2B1_incomplete_other_specific_gap

Do not declare GF-STEP-2 complete.

If complete, propose a bounded STEP2B2 for RPT-2026Q2-0003 only.
Do not execute STEP2B2.

────────────────────────────────────
12. Workload limits
────────────────────────────────────

- repository source paths: exactly 1
- retrieval/query batteries: maximum 2
- original reports read: exactly 1
- maximum evidence records: 14
- preliminary signals directly reassessed: exactly S-01, S-02, S-03
- no PDF reads
- no report-summary reads
- no research-prompt reads
- no external or web research
- Research mode OFF
- no automatic continuation
- stop after the downloadable file and brief chat summary

Word-budget policy:

- soft target: 1,700–2,700 words
- hard cap: 3,300 words
- the soft target is advisory
- a complete first draft within the hard cap is acceptable
- at most one light compression pass
- preserve evidence anchors, distinctions, limitations, and signal decisions
  before optional narrative
- never silently omit a major report section
- perform no more than one approximate word-count check
- do not repeat compression because counting methods differ

────────────────────────────────────
13. Required downloadable file
────────────────────────────────────

Create a downloadable Markdown file named exactly:

FABLE5-GREENFIELD-001-STEP2B1-foundational-report-evidence.md

Required sections:

1. Metadata
2. Scope and hard limits
3. Allowed sources and anti-contamination policy
4. Source integrity and access result
5. Evidence interpretation rules
6. Report coverage map
7. Foundational evidence register
8. STEP2A signal reassessment
9. Principle-versus-product separation
10. Contradiction and uncertainty register
11. STEP-1 linkage delta
12. Deferred-source register
13. Incidental-exposure ledger
14. Coverage and limitation ledger
15. STEP2B1 status determination
16. Proposed bounded STEP2B2
17. Boundary statement

Metadata must include:

charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2B1
record_type: foundational_original_report_evidence_review
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-2A
research_mode: false
source_file:
  path: raw/research-reports/cycles/2026Q2-initial/originals/AI agent 长期记忆系统 pro深度研究.txt
  expected_blob_sha: 1c4a48c53d7ac126eb29a0ea7ab1e0e8a0f5c82a

The coverage ledger must state:

- expected and observed SHA;
- whether the full text was inspected;
- retrieval batteries used;
- report sections covered;
- evidence records created;
- S-01/S-02/S-03 dispositions;
- low-drift versus dated items recorded;
- unresolved freshness dependencies;
- deferred reports;
- STEP2B1 completion status.

────────────────────────────────────
14. Chat response
────────────────────────────────────

After creating the file, briefly state:

- completion within limits;
- SHA match result;
- whether the full report was inspected;
- report evidence date or cutoff;
- evidence-record count;
- S-01 disposition;
- S-02 disposition;
- S-03 disposition;
- number of low-drift items;
- number of dated items;
- retrieval batteries used;
- incidental exposure, if any;
- approximate word count;
- STEP2B1 status;
- downloadable file creation result.

Do not repeat the full file in chat.

────────────────────────────────────
15. Boundary
────────────────────────────────────

Do not:

- write repository files;
- generate execution tasks;
- update execution source;
- inspect another report, summary, prompt, or PDF;
- perform external research;
- evaluate models or vendors;
- compare or modify the existing design;
- begin architecture work;
- create target-project artifacts;
- resume or close the paused route.

This output is non-execution-source advisory evidence only.
Stop after the downloadable file and brief chat summary.
```
