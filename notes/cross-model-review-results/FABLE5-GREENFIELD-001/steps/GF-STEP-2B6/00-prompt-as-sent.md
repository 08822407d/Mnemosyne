Run the next integrated evidence-review substep of FABLE5-GREENFIELD-001.

step_id: GF-STEP-2B6
step_name: supplemental_testing_handoff_governance_and_dry_run_batch_review
relationship_to_charter:
  integrated review of the complete STEP2A supplemental-report batch;
  continuation of GF-STEP-2B5;
  final original-report reading batch of GF-STEP-2;
  not completion of GF-STEP-2 or the final capability-boundary baseline

Execution setting:
- Research mode must remain OFF.
- Run in a fresh Fable 5 conversation.
- Attach and use:
  FABLE5-GREENFIELD-001-STEP2B5-theory-nondev-transfer-evidence.md
- Do not retrieve STEP2A, STEP1 outputs, the charter, or earlier STEP2 outputs.
- This prompt is self-contained.
- Treat this as one integrated task. Do not split the four reports into
  separate substeps merely because they cover different operational domains.

Purpose:
Review the four supplemental Markdown research reports that complete the
repository's current GF-STEP-2 original-report evidence set:

1. memory-system testing, debugging, evaluation, and failure diagnosis;
2. handoff correctness, package strategy, and quantitative evaluation;
3. user-originals, requirements, redaction, visibility, and provenance
   governance;
4. first-real-target dry-run evaluation, evidence, and authority containment.

The task must identify what these reports actually support about:

- how external persistent-memory behavior should be evaluated;
- how failures should be classified and diagnosed;
- what constitutes a correct and recoverable handoff;
- what belongs in a handoff package and how package size should vary;
- how user originals, restatements, approved decisions, redacted material,
  and external pointers should remain distinct;
- how preservation, minimization, correction, withdrawal, deletion, and Git
  history interact;
- what distinguishes smoke tests, tabletop exercises, real-target dry runs,
  delivery, and target write;
- which gates and evidence are required before a real-target dry run;
- which findings are durable principles, candidate methods, policy proposals,
  dated repository-specific advice, or unresolved user decisions.

This is a repository-bounded evidence review.

It must not:
- perform external or web research;
- execute any research recommendation;
- treat the reports as execution source;
- evaluate or rank models, vendors, or frontier systems;
- inspect model internals or training;
- design the final Mnemosyne architecture;
- compare against the current GPT-produced design;
- recommend or perform repository repairs;
- begin GF-STEP-3.

────────────────────────────────────
1. Allowed inputs
────────────────────────────────────

Allowed attachment:

- FABLE5-GREENFIELD-001-STEP2B5-theory-nondev-transfer-evidence.md

Use the attachment only for:

- track continuity;
- the existing STEP-1 need identifiers;
- current question identifiers;
- S-01 and earlier STEP2 evidence-boundary conventions;
- the distinction among principles, practices, recommendations, dated product
  facts, and unresolved questions;
- confirmation that all seven initial-cycle reports have completed text-layer
  review.

Do not use conclusions in the attachment as substitutes for evidence in the
four reports reviewed here.

Allowed repository sources — exactly these four paths:

A. RPT-2026Q2-MT-0001

- path:
  raw/research-reports/cycles/2026Q2-memory-testing/originals/DR1_memory_testing_debugging_evidence_review_report.md
- ref: master
- expected blob SHA:
  3cd85dce404a1052e456ee0687c6c2e49b0b8fe8

B. RPT-2026Q2-HO-0001

- path:
  raw/research-reports/cycles/2026Q2-handoff-strategy/originals/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_report.md
- ref: master
- expected blob SHA:
  457163a791db6887c4695c69376754db98494c8c

C. RPT-2026Q2-UIG-0001

- path:
  raw/research-reports/cycles/2026Q2-user-input-governance/originals/DR4_user_originals_requirements_redaction_governance_report.md
- ref: master
- expected blob SHA:
  81ceb3d56f17e1a6136cd882df4dba0fb2ba83cb

D. RPT-2026Q2-FTDRE-0001

- path:
  raw/research-reports/cycles/2026Q2-first-target-dry-run-evaluation/originals/DR5_first_real_target_dry_run_evaluation_framework_report.md
- ref: master
- expected blob SHA:
  cbf188aa41ad9e688fbc93091f0bb23d9a2e5cf6

Read no other repository path.

Do not open:

- report summaries or summary indexes;
- research prompts;
- initial-cycle PDF or TXT reports;
- current/**;
- handoff/**;
- notes/** other than the attached prior-step artifact;
- task-result records;
- Fable review or triage records;
- existing GPT design artifacts;
- external URLs or websites.

The reports contain external citation markers and repository-specific references.
Treat all such references as report-internal metadata only. Do not follow them.

────────────────────────────────────
2. Source integrity and complete-read requirement
────────────────────────────────────

Create one source-access row for every report.

For each report record:

- report_id
- repository_path
- expected_blob_sha
- observed_blob_sha
- sha_match: true | false
- approximate_line_count
- complete_file_inspected: true | false
- truncation_or_access_gap
- retrieval_battery
- notes

Maximum retrieval/query batteries: 4 — one per source.

These Markdown files are expected to be manageable as one integrated batch.
Inspect each complete file.

If a source cannot be completely retrieved:

- do not search for a replacement;
- do not infer its missing content from another report or summary;
- continue with the verified accessible reports;
- mark the specific source as incomplete;
- reflect the missing source in the final status determination.

If any observed SHA differs:

- do not silently use the changed source;
- do not use another branch or cached version;
- record the integrity failure;
- continue only with reports whose SHAs match.

────────────────────────────────────
3. Evidence interpretation rules
────────────────────────────────────

Classify extracted material using only:

- report_direct_finding
- report_author_synthesis
- report_recommendation
- low_drift_engineering_principle
- cited_external_claim_not_independently_checked
- dated_product_or_workflow_statement
- dated_Mnemosyne_repository_state_statement
- method_candidate
- policy_candidate
- framing_assumption_to_verify
- mixed_or_uncertain

Apply all of these rules:

1. Every report is research evidence, not execution source.
2. A recommendation is not an approved Mnemosyne rule.
3. A requested metric, taxonomy, checklist, score, schema, or threshold is not
   validated merely because a report proposes it.
4. A cited external source is not independently verified in this step.
5. Repository-state statements in the reports describe their research-time
   snapshot and must not be treated as current repository truth.
6. Do not use current repository knowledge or your own knowledge to update or
   correct the reports.
7. Separate:
   - underlying need;
   - durable principle;
   - observed evidence;
   - method candidate;
   - policy candidate;
   - report-specific recommendation;
   - user decision.
8. A successful final answer is not proof that memory state, propagation,
   provenance, timing, or write behavior was correct.
9. A handoff score or LLM judge output is evidence only; it is not an execution
   source or automatic gate-closing authority.
10. Preservation of originals and minimization/redaction are not presumed
    compatible or incompatible; preserve the tension supported by the evidence.
11. A dry-run PASS applies only to the tested object and authority boundary.
12. Do not generalize a Mnemosyne-specific recommendation into a universal
    external-memory rule.
13. Do not import the current GPT-produced Mnemosyne architecture.
14. Continue the prior-exposure disclosure:
    independent by derivation and disclosure, not by claimed amnesia.

────────────────────────────────────
4. MT-0001 testing and failure evidence register
────────────────────────────────────

Create at most 6 load-bearing evidence records.

Use IDs:

F2B6-MT01 through F2B6-MT06

Focus on:

- operational definitions of correct memory-system behavior;
- why final-answer accuracy is insufficient;
- state, source, temporal, propagation, and artifact correctness;
- testing levels and maturity;
- observability, traces, trajectories, replay, issue logs, and postmortems;
- failure taxonomy and causal diagnosis;
- stale information, conflict, update, retrieval, handoff, and delivery
  failures;
- deterministic checks, LLM-assisted checks, and human-review boundaries;
- minimum viable evaluation before larger automation;
- methods that remain research prototypes rather than mature practice.

For every record include:

- evidence_id
- source_anchor
- concise_statement
- evidence_category
- evaluation_or_failure_scope
- maturity:
    mature_component |
    emerging_method |
    reasonable_engineering_derivation |
    not_recommended_as_primary_basis |
    mixed
- report_evidence_period
- confidence_as_report_evidence:
    high |
    medium |
    low
- method_selection_still_required: true | false
- related_STEP1_need_ids
- related_question_ids
- prohibited_overclaim
- notes

Do not create six records unless every record is load-bearing.

────────────────────────────────────
5. HO-0001 handoff evidence register
────────────────────────────────────

Create at most 6 load-bearing evidence records.

Use IDs:

F2B6-HO01 through F2B6-HO06

Focus on:

- the operational definition of a correct handoff;
- currentness recovery and stale-state resistance;
- execution-source, phase, gate, authority, task-intent, and next-action
  recovery;
- unsupported-assumption handling;
- evidence-path and provenance recovery;
- minimum, standard, and extended package concepts;
- package completeness versus compactness;
- quantitative scorecards and blocking criteria;
- fresh replay as evidence;
- handoff triggers;
- heterogeneous model/tool/surface migration;
- limits of LLM judges and single-score conclusions;
- avoiding repeated questions already answered in authorized sources.

For every record include:

- evidence_id
- source_anchor
- concise_statement
- evidence_category
- handoff_scope
- maturity:
    mature_principle |
    report_proposed_method |
    report_proposed_metric |
    repository_specific_recommendation |
    mixed
- report_evidence_period
- confidence_as_report_evidence:
    high |
    medium |
    low
- trigger_or_threshold_user_decision_required: true | false
- related_STEP1_need_ids
- related_question_ids
- prohibited_overclaim
- notes

Do not assume that longer packages are safer.

────────────────────────────────────
6. UIG-0001 user-input governance evidence register
────────────────────────────────────

Create at most 6 load-bearing evidence records.

Use IDs:

F2B6-UIG01 through F2B6-UIG06

Focus on:

- original user evidence versus restatement versus approved decision;
- evidentiary, interpretive, operative, disclosure, and provenance authority;
- repository versus external controlled storage;
- visibility pessimism;
- data minimization and selective retention;
- redaction, de-identification, synthetic substitution, and residual risk;
- external pointers and pointer-safety metadata;
- Git-history exposure and recontamination;
- correction, withdrawal, deletion, retention, and audit tensions;
- human approval and change control;
- what a private repository does not guarantee;
- differences between repository storage and execution authority.

For every record include:

- evidence_id
- source_anchor
- concise_statement
- evidence_category
- governance_scope
- authority_type:
    evidentiary |
    interpretive |
    operative |
    disclosure |
    provenance |
    mixed
- report_evidence_period
- confidence_as_report_evidence:
    high |
    medium |
    low
- policy_selection_still_required: true | false
- related_STEP1_need_ids
- related_question_ids
- preservation_redaction_tension
- prohibited_overclaim
- notes

Do not convert the report's proposed five-layer model directly into an approved
architecture.

────────────────────────────────────
7. FTDRE-0001 dry-run evidence register
────────────────────────────────────

Create at most 6 load-bearing evidence records.

Use IDs:

F2B6-DR01 through F2B6-DR06

Focus on:

- distinctions among:
  - synthetic smoke test;
  - tabletop exercise;
  - real target-project dry-run;
  - target delivery;
  - target repository write;
- minimum legal/evidence unit of a real-target dry run;
- authority/source map and truth-source prerequisites;
- safe input, user-originals policy, redaction, and external-pointer gates;
- run-manifest approval;
- no-target-write proof;
- synthetic-versus-real evidence separation;
- frozen rubric or predeclared acceptance criteria;
- memory usefulness rather than artifact polish;
- handoff usability, stale-state resistance, conflict handling, and abstention;
- scorecard, postmortem, and regression-candidate generation;
- PASS semantics and prohibition on authority escalation.

For every record include:

- evidence_id
- source_anchor
- concise_statement
- evidence_category
- tested_object_or_gate_scope
- report_evidence_period
- confidence_as_report_evidence:
    high |
    medium |
    low
- deterministic_or_human_gate:
    deterministic |
    human |
    mixed |
    method_candidate
- related_STEP1_need_ids
- related_question_ids
- prohibited_authority_inference
- prohibited_overclaim
- notes

Do not treat a proposed scorecard as a validated universal benchmark.

────────────────────────────────────
8. Reassess the open method and policy questions
────────────────────────────────────

Reassess exactly these four questions.

A. Q-07-updated — preservation versus redaction reconciliation

Previous scope:
- how to preserve evidentiary originals and provenance;
- how to minimize, redact, withdraw, delete, or keep sensitive material outside
  Git;
- which balance requires a user policy decision.

B. Q-08-updated — testing and evaluation method selection

Previous scope:
- the underlying need for testability and failure diagnosis is represented;
- exact metrics, benchmarks, failure classes, thresholds, and judge roles
  remain method-selection questions.

C. Q-09-updated — first real target and dry-run validation

Previous scope:
- the need for staged first-target validation is represented;
- the target identity and some authority/gate decisions remain user decisions.

D. Q-13 — handoff trigger criteria

Previous scope:
- what conditions require a handoff;
- how package tier, risk, context size, model/tool migration, and failure
  recovery affect the trigger.

For each question record:

- question_id
- previous_status
- report_evidence_found
- disposition:
    resolved_as_need |
    converted_to_policy_selection |
    converted_to_method_selection |
    partially_resolved |
    unresolved_user_decision
- updated_question_if_needed
- related_F2B6_evidence_ids
- what_the_reports_can_settle
- what_only_the_user_can_settle
- what_requires_later_current_fact_refresh
- can_GF_STEP_2_complete_with_question_open:
    yes |
    no

Do not create new question IDs unless a genuinely distinct, load-bearing
uncertainty is discovered.

Maximum new questions: 3.
Continue numbering from Q-14.

────────────────────────────────────
9. Integrated operational-boundary matrix
────────────────────────────────────

Create at most 12 rows.

Potential concerns include:

- final-answer correctness versus state/process correctness;
- state/source/time/propagation/artifact correctness;
- silent memory failure and causal diagnosis;
- testing maturity and evidence strength;
- deterministic checks versus model-assisted review;
- handoff correctness and stale-state resistance;
- package tiering and completeness-versus-compactness;
- provenance and reviewer identity;
- originals/restatements/approved decisions;
- redaction, minimization, deletion, and Git history;
- dry-run object classification;
- prerequisite and authority gates;
- no-write evidence;
- synthetic versus real evidence;
- scorecards, postmortems, and regression candidates;
- PASS semantics and non-escalation of authority.

For every row include:

- concern
- MT_evidence_ids
- HO_evidence_ids
- UIG_evidence_ids
- FTDRE_evidence_ids
- integrated_statement
- alignment:
    convergent |
    partially_convergent |
    tension |
    single_report_only |
    unresolved
- status:
    supported_principle |
    bounded_policy_candidate |
    bounded_method_candidate |
    user_decision |
    dated_repository_specific_advice |
    open_question
- what_must_not_be_claimed
- later_evidence_or_decision_needed

This is evidence synthesis, not architecture design.

────────────────────────────────────
10. Need-model linkage delta
────────────────────────────────────

Record material evidence-coverage changes for at most 9 of:

- GF1A-N06
- GF1A-N07
- GF1A-N11
- GF1A-N12
- GF1B-N13
- GF1B-N14
- GF1B-N15
- GF1C-N19
- GF1C-N20
- GF1C-N21

For each selected need:

- need_id
- coverage_before_this_batch
- coverage_after_this_batch
- supporting_F2B6_evidence_ids
- remaining_method_dependency
- remaining_policy_dependency
- remaining_user_decision
- later_current_fact_refresh_needed

Do not reproduce full need records.

────────────────────────────────────
11. Principle, method, policy, and dated-state separation
────────────────────────────────────

Create a compact classification table using:

- low_drift_engineering_principle
- evidence_supported_behavioral_boundary
- method_candidate
- metric_or_threshold_candidate
- policy_candidate
- dated_product_or_platform_statement
- dated_Mnemosyne_repository_state_statement
- report_recommendation
- unresolved_user_decision

For every row record:

- item_or_evidence_ids
- class
- concise_content
- may_enter_final_GF_STEP_2_baseline:
    yes |
    yes_with_qualification |
    no
- requires_current_fact_refresh:
    yes |
    no |
    uncertain
- requires_user_approval_before_design_use:
    yes |
    no |
    uncertain
- later_handling

Do not merge a policy proposal into a principle.

────────────────────────────────────
12. Contradiction, staleness, and uncertainty register
────────────────────────────────────

Create at most 10 items.

Include:

- report recommendations that rely on then-current Mnemosyne repository state;
- report statements overtaken by later repository work;
- metrics or thresholds without sufficient validation;
- LLM-judge limitations;
- unresolved preservation-versus-redaction tension;
- correction/deletion expectations versus immutable Git history;
- package compactness versus completeness;
- dry-run evaluation breadth versus workload;
- dependence on cited external sources not checked here;
- fast-moving benchmark or product claims;
- evidence gaps between recommended process and demonstrated outcomes.

For every item include:

- issue_id
- affected_report_ids
- source_anchor
- issue_type
- description
- affected_evidence_ids
- handling_for_final_GF_STEP_2

Do not resolve staleness using current repository knowledge. Mark it for the
later assembly/refresh gate.

────────────────────────────────────
13. All-report text-evidence completion ledger
────────────────────────────────────

Create a compact ledger confirming the status of all 11 reports planned in
STEP2A.

Initial reports:

- RPT-2026Q2-0001
- RPT-2026Q2-0002
- RPT-2026Q2-0003
- RPT-2026Q2-0004
- RPT-2026Q2-0005
- RPT-2026Q2-0006
- RPT-2026Q2-0007

Supplemental reports:

- RPT-2026Q2-MT-0001
- RPT-2026Q2-HO-0001
- RPT-2026Q2-UIG-0001
- RPT-2026Q2-FTDRE-0001

For each record only:

- report_id
- reviewed_in_step
- text_layer_status:
    complete |
    partial |
    inaccessible
- visual_review_status:
    not_applicable_markdown |
    not_performed_PDF
- substantive_acceptance_status:
    Fable_evidence_review_only
- remaining_dependency

Do not reproduce all earlier evidence records.

────────────────────────────────────
14. GF-STEP-2B6 and next-stage status determination
────────────────────────────────────

Choose exactly one:

- GF_STEP_2B6_complete_all_original_report_text_reviews_ready_for_STEP2C
- GF_STEP_2B6_complete_with_explicit_partial_source_coverage
- GF_STEP_2B6_incomplete_source_integrity_failure
- GF_STEP_2B6_incomplete_access_or_truncation
- GF_STEP_2B6_incomplete_other_specific_gap

Do not declare GF-STEP-2 complete.

If B6 completes, propose:

GF-STEP-2C:
  capability_boundary_baseline_assembly_and_refresh_gate

That next step should:

- assemble the complete STEP2 evidence set;
- determine the final evidence-supported boundary statements;
- separate low-drift principles from dated facts and candidate methods;
- identify exactly which product/platform facts require current refresh;
- decide whether any unreviewed PDF visual content is load-bearing;
- carry open user questions without answering them by inference;
- make the final GF-STEP-2 completion determination.

Do not execute GF-STEP-2C.

Do not propose GF-STEP-3 until GF-STEP-2C has completed.

────────────────────────────────────
15. Hard workload limits
────────────────────────────────────

- repository paths: exactly 4
- retrieval/query batteries: maximum 4
- Markdown reports opened: exactly 4
- evidence records per report: maximum 6
- total evidence records: maximum 24
- integrated matrix rows: maximum 12
- STEP-1 linkage entries: maximum 9
- uncertainty items: maximum 10
- new question IDs: maximum 3
- no report summaries, prompts, indexes, PDFs, or other repository files
- no external or web research
- Research mode OFF
- no architecture design
- no automatic continuation into GF-STEP-2C

Word-budget policy:

- soft target: 3,600–5,000 words
- hard cap: 6,000 words
- the soft target is advisory
- a complete first draft inside the hard cap is acceptable
- at most one light compression pass, only when the hard cap is exceeded
- remove repeated report narration before evidence, question dispositions,
  matrices, limitations, or status reasoning
- never silently omit one of the four reports
- never silently truncate a required evidence record
- use compact tables for matrices and ledgers
- perform no more than one approximate word-count check
- do not repeat counting or compression because reasonable methods differ

────────────────────────────────────
16. Required downloadable file
────────────────────────────────────

Create exactly:

FABLE5-GREENFIELD-001-STEP2B6-supplemental-operational-evidence.md

If downloadable artifact creation is unavailable, provide the exact complete
Markdown body in one fenced block.

Required sections:

1. Metadata
2. Scope and hard limits
3. Allowed sources and anti-contamination policy
4. Source integrity and access table
5. Evidence interpretation rules
6. MT-0001 testing and failure evidence register
7. HO-0001 handoff evidence register
8. UIG-0001 user-input governance evidence register
9. FTDRE-0001 dry-run evidence register
10. Updated Q-07/Q-08/Q-09/Q-13 register
11. Integrated operational-boundary matrix
12. Need-model linkage delta
13. Principle/method/policy/dated-state classification
14. Contradiction, staleness, and uncertainty register
15. All-report text-evidence completion ledger
16. Coverage and limitation ledger
17. GF-STEP-2B6 status determination
18. Proposed bounded GF-STEP-2C
19. Boundary statement

Metadata must include:

charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2B6
record_type: supplemental_testing_handoff_governance_dry_run_batch_review
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-2B5
research_mode: false
source_files:
  - report_id: RPT-2026Q2-MT-0001
    path: raw/research-reports/cycles/2026Q2-memory-testing/originals/DR1_memory_testing_debugging_evidence_review_report.md
    expected_blob_sha: 3cd85dce404a1052e456ee0687c6c2e49b0b8fe8
  - report_id: RPT-2026Q2-HO-0001
    path: raw/research-reports/cycles/2026Q2-handoff-strategy/originals/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_report.md
    expected_blob_sha: 457163a791db6887c4695c69376754db98494c8c
  - report_id: RPT-2026Q2-UIG-0001
    path: raw/research-reports/cycles/2026Q2-user-input-governance/originals/DR4_user_originals_requirements_redaction_governance_report.md
    expected_blob_sha: 81ceb3d56f17e1a6136cd882df4dba0fb2ba83cb
  - report_id: RPT-2026Q2-FTDRE-0001
    path: raw/research-reports/cycles/2026Q2-first-target-dry-run-evaluation/originals/DR5_first_real_target_dry_run_evaluation_framework_report.md
    expected_blob_sha: cbf188aa41ad9e688fbc93091f0bb23d9a2e5cf6

The coverage ledger must state:

- expected and observed SHA for every report;
- whether every report was read completely;
- approximate line count for every report;
- retrieval batteries used;
- evidence count by report and total;
- Q-07/Q-08/Q-09/Q-13 dispositions;
- matrix and linkage counts;
- all-11-report text-review completion status;
- PDF visual-review limitations carried from earlier steps;
- dated/current-fact dependencies;
- whether B6 completed;
- exact residual dependency before GF-STEP-2 can close.

────────────────────────────────────
17. File-content discipline
────────────────────────────────────

Preserve:

- source-qualified evidence;
- distinctions among principles, findings, recommendations, methods, policies,
  and user decisions;
- question dispositions;
- staleness and uncertainty;
- the all-report completion ledger;
- bounded STEP2C continuation.

Do not include:

- hidden chain-of-thought;
- long connector narration;
- raw tool logs;
- externally refreshed facts;
- architecture proposals;
- current-design comparison;
- repair recommendations;
- execution-source proposals;
- artifact-control messages;
- duplicated file-presentation text.

Before presenting the file:

- perform one structural check;
- perform no more than one approximate word-count check;
- confirm all four reports appear in the source table and evidence sections;
- confirm all 19 required sections exist;
- confirm the ending is clean;
- do not perform another compression cycle when within the hard cap.

────────────────────────────────────
18. Chat response
────────────────────────────────────

After presenting the file, provide only a brief summary stating:

- completion within limits;
- SHA and complete-read result for every report;
- evidence-record count per report and total;
- Q-07 disposition;
- Q-08 disposition;
- Q-09 disposition;
- Q-13 disposition;
- integrated matrix row count;
- STEP-1 linkage count;
- retrieval batteries used;
- all-11-report text-review completion status;
- approximate word count;
- B6 status determination;
- whether GF-STEP-2C was proposed;
- downloadable file creation result.

Do not repeat the file body in chat.

────────────────────────────────────
19. Boundary
────────────────────────────────────

Do not:

- write repository files;
- generate execution tasks;
- update execution source;
- inspect another report, summary, prompt, index, PDF, current file, handoff
  file, review record, or design artifact;
- perform web or external research;
- evaluate or rank models or vendors;
- compare against or modify the current GPT/Mnemosyne design;
- begin architecture design or GF-STEP-3;
- create target-project artifacts;
- formalize regression;
- resume or close the paused post-handoff route.

This output is non-execution-source advisory evidence only.
Stop after the downloadable file and brief summary.
