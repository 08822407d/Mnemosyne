# FABLE5-GREENFIELD-001 — GF-STEP-1E Prompt as Sent

```text
Run the next bounded substep of FABLE5-GREENFIELD-001.

step_id: GF-STEP-1E
step_name: second_tier_prompt_check_and_step1_final_closure
relationship_to_charter: continuation of GF-STEP-1A through GF-STEP-1D;
inspect exactly the three supplemental prompt originals identified by STEP1D
as the remaining closure dependency

Execution setting:
- Research mode must remain OFF.
- Continue in the same Fable 5 conversation.
- Attach and use:
  - FABLE5-GREENFIELD-001-STEP1A-core-needs-pilot.md
  - FABLE5-GREENFIELD-001-STEP1B-deferred-needs-and-questions.md
  - FABLE5-GREENFIELD-001-STEP1C-research-prompt-index-gap-map.md
  - FABLE5-GREENFIELD-001-STEP1D-DR4-prompt-check-and-closure.md
- Do not retrieve the charter from the repository or conversation history.
- This prompt is self-contained and governs this bounded substep.

Purpose:
Inspect the three remaining supplemental-cycle original research prompts
identified by GF-STEP-1D:

1. memory-system testing/debugging/evaluation/failure diagnosis;
2. handoff strategy and quantitative evaluation;
3. first real target-project dry-run evaluation.

Extract only the requirement, constraint, priority, and unresolved-question
signals explicitly supported by those prompt texts.

Use the evidence to confirm, refine, split, downgrade, or withdraw the
provisional GF1C-N19 and GF1C-N21 records; reassess Q-08, Q-09, and the
second-tier part of Q-10; then make the final GF-STEP-1 completion
determination.

This step does not execute any research prompt, does not inspect any research
report, and does not perform architecture design, comparison, or repair work.

────────────────────────────────────
1. Allowed inputs
────────────────────────────────────

Allowed attachments:

- FABLE5-GREENFIELD-001-STEP1A-core-needs-pilot.md
- FABLE5-GREENFIELD-001-STEP1B-deferred-needs-and-questions.md
- FABLE5-GREENFIELD-001-STEP1C-research-prompt-index-gap-map.md
- FABLE5-GREENFIELD-001-STEP1D-DR4-prompt-check-and-closure.md

Allowed repository sources — exactly these three paths:

A. Memory testing / MT-0001

- path:
  raw/research-reports/cycles/2026Q2-memory-testing/research-prompts/originals/DR1_memory_testing_debugging_evidence_review_prompt.md
- ref: master
- expected blob SHA:
  e6fc63b1548a442e238da4e5740c77eaf9f794fd

B. Handoff strategy / HO-0001

- path:
  raw/research-reports/cycles/2026Q2-handoff-strategy/research-prompts/originals/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_prompt.md
- ref: master
- expected blob SHA:
  51f3927800b69d25d47e5a5dd86029cbf473c776

C. First-target dry-run evaluation / FTDRE-0001

- path:
  raw/research-reports/cycles/2026Q2-first-target-dry-run-evaluation/research-prompts/originals/DR5_v2_first_real_target_dry_run_evaluation_framework_prompt.md
- ref: master
- expected blob SHA:
  716166c5ae54e341f94909594d99de645a19054c

Read no other repository path.

Explicitly excluded:

- PROMPT-2026Q2-0001 through PROMPT-2026Q2-0007 originals;
- PROMPT-2026Q2-UIG-0001 / DR4, which was already inspected in STEP1D;
- all research reports, summaries, indexes, and motivation files;
- current/**;
- handoff/**;
- notes/**;
- commands/**;
- manual-import-inbox/**;
- MNEMOSYNE task records;
- FABLE5 review or triage records;
- existing GPT-produced design artifacts;
- external websites and web-search results.

Do not use the raw endpoint, contents API, search, or conversation recovery to
open any additional path.

If a permitted prompt internally mentions existing design files, task IDs,
candidate paths, current implementation state, or report conclusions, classify
that content as prompt-internal framing. Do not open the referenced material and
do not import it into the greenfield need model unless the prompt wording itself
states a broader user requirement independently of that implementation context.

────────────────────────────────────
2. Evidence interpretation rules
────────────────────────────────────

Each allowed source is an original research prompt.

A research prompt is:

- research input;
- evidence of what questions, constraints, comparisons, and deliverables were
  considered important;
- not a research conclusion;
- not proof that any requested fact is true;
- not execution source;
- not automatic approval of any requested schema or mechanism.

Classify prompt passages using only:

- explicit_user_requirement_or_constraint
- research_question_or_requested_evidence
- research_delivery_or_process_instruction
- framing_assumption_to_verify
- mixed_or_uncertain

Apply all of these rules:

1. Do not convert research questions into settled requirements.
2. Do not treat requested metrics, benchmarks, taxonomies, failure classes, or
   schemas as validated merely because a prompt asks for them.
3. Do not infer anything from the unread research reports.
4. Do not universalize a task-specific report-delivery instruction into a
   permanent memory-system requirement unless the wording clearly establishes
   broader scope.
5. Distinguish:
   - a need for testability from a proposed test method;
   - a need for reliable handoff from a proposed package strategy;
   - a need for first-target validation from a proposed evaluation framework.
6. Treat embedded current-design context as framing only.
7. Preserve source-specific uncertainty.
8. Continue the known prior-exposure disclosure:
   independent by derivation and disclosure, not by claimed amnesia.
9. Do not create a new need record merely because a prompt contains a detailed
   research deliverable list.
10. Prefer refining an existing record over creating a near-duplicate.

────────────────────────────────────
3. Source-access and integrity work
────────────────────────────────────

Create a source-access table containing one row for each of the three prompts.

For each source record:

- prompt_id
- repository_path
- expected_blob_sha
- observed_blob_sha
- sha_match: true | false
- complete_file_inspected: true | false
- approximate_line_count
- retrieval_battery
- prohibited_reference_names_seen
- referenced_material_opened: false
- access_notes

If any expected SHA does not match:

- do not silently continue using the changed file;
- record the mismatch;
- inspect no replacement source;
- continue only with sources whose SHA matches;
- make the final completion determination reflect the missing verified source.

────────────────────────────────────
4. Per-prompt decomposition
────────────────────────────────────

Produce three separate decomposition tables:

- MT-0001 decomposition
- HO-0001 decomposition
- FTDRE-0001 decomposition

Each table should group load-bearing passages rather than listing every
paragraph.

Across all three prompts:

- target 15–24 total decomposition entries;
- hard maximum 27 entries.

For every entry record:

- prompt_id
- source_anchor
- evidence_category
- concise_content
- directness:
    explicit |
    implied |
    question_only
- related_existing_need_ids
- effect_on_need_model:
    confirms |
    refines |
    creates_candidate |
    raises_question |
    process_only |
    framing_only
- report_evidence_would_still_be_required: true | false
- rationale

Do not reproduce long prompt passages.

────────────────────────────────────
5. Reassess GF1C-N19
────────────────────────────────────

Current provisional record:

GF1C-N19 — memory_system_testability_and_failure_diagnosis

Primary sources for reassessment:

- MT-0001
- HO-0001 where its quantitative-evaluation content directly affects N19

Choose exactly one action:

- retain_as_is
- refine
- split
- downgrade_to_priority_signal
- withdraw_as_unsupported

If retained, refined, or split, provide complete replacement record text for
GF1C-N19 containing:

- need_id
- need_title
- source_anchors
- source_class
- interpreted_need
- scope
- relationship_to GF1A-N11 and GF1A-N12
- distinction_between_need_and_candidate_metrics
- confidence
- unresolved_ambiguity
- related_question_ids
- possible_prior_exposure_echo
- derivation_note

Do not create a duplicate of GF1C-N19 under a new identifier.

────────────────────────────────────
6. Reassess GF1C-N21
────────────────────────────────────

Current provisional record:

GF1C-N21 — first_real_target_dry_run_validation

Primary source:

- FTDRE-0001

Also account for the DR4 requirement recorded in STEP1D that a practical v0.1
user-input governance policy must exist before the first real target dry run.

Choose exactly one action:

- retain_as_is
- refine
- split
- downgrade_to_priority_signal
- withdraw_as_unsupported

If retained, refined, or split, provide complete replacement record text for
GF1C-N21 containing:

- need_id
- need_title
- source_anchors
- source_class
- interpreted_need
- scope
- prerequisites
- relationship_to GF1A-N05, GF1A-N11, GF1C-N19, and GF1C-N20
- distinction_between_validation_need_and_candidate_framework
- confidence
- unresolved_ambiguity
- related_question_ids
- possible_prior_exposure_echo
- derivation_note

Do not create a duplicate of GF1C-N21 under a new identifier.

────────────────────────────────────
7. Handoff-related requirement delta
────────────────────────────────────

Use HO-0001 to assess whether GF1A-N12
(self_bootstrap_and_handoff_continuity) is sufficient.

Choose one status:

- GF1A_N12_sufficient_unchanged
- GF1A_N12_requires_refinement
- distinct_new_need_justified
- only_candidate_methods_found

If refinement is required, provide only a delta for GF1A-N12 rather than
rewriting unrelated fields.

A distinct new record is permitted only if HO-0001 explicitly supports a
load-bearing requirement not represented by:

- GF1A-N12;
- GF1C-N19;
- another existing need.

New records, if genuinely required, begin at:

GF1E-N22

Maximum new records in this entire step, excluding replacement text for N19 and
N21: 4.

────────────────────────────────────
8. Cross-prompt constraint map
────────────────────────────────────

Create a compact map covering:

- testability and observability;
- debugging and failure diagnosis;
- evaluation criteria and metrics;
- handoff triggers;
- handoff package completeness versus compactness;
- quantitative comparison of handoff strategies;
- first-target dry-run prerequisites;
- first-target success/failure criteria;
- dry-run evidence preservation;
- relationship between the dry run and user-input governance;
- human approval and authority;
- report-derived recommendations versus prompt-level requirements.

For every row state:

- concern
- source_prompt_ids
- related_need_ids
- prompt_supported_requirement_or_question
- candidate_method_or_metric
- status:
    confirmed_need |
    refined_need |
    candidate_only |
    open_question |
    framing_only
- research_report_needed_for_method_selection: true | false

This is a need-model map, not an evaluation-framework design.

────────────────────────────────────
9. Reassess the unresolved questions
────────────────────────────────────

Carry forward without silently answering:

- Q-01 through Q-06;
- Q-07-updated;
- Q-11;
- Q-12.

Reassess Q-08:

- which metrics, failure classes, and evaluation methods the MT and HO prompts
  specify;
- whether the need is now sufficiently represented even though method choice
  still requires report evidence.

Reassess Q-09:

- what the FTDRE prompt defines as the first real target;
- what the prompt requires the dry run to demonstrate;
- which details remain evidence questions or user decisions.

Reassess the second-tier portion of Q-10:

- whether these three original prompts contained load-bearing constraints not
  visible in the index;
- whether any further original-prompt inspection is still required merely to
  identify a missing need.

For Q-08, Q-09, and Q-10 provide:

- previous_question_or_status
- prompt_evidence_found
- status:
    resolved |
    partially_resolved |
    unresolved |
    converted_to_method_selection_question
- updated_question_if_needed
- related_need_record_effect
- can_GF_STEP_1_close_without_further_prompt_reading:
    yes |
    no

Maximum newly created question IDs: 3.

Continue numbering at:

Q-13

Do not create a new question when an existing question can be refined.

────────────────────────────────────
10. Need-record changes and assembly register
────────────────────────────────────

First provide a change ledger:

- records retained unchanged;
- records refined;
- records split;
- records downgraded;
- records withdrawn;
- genuinely new records.

Then produce the final GF-STEP-1 assembly register.

The register must include every need ID from:

- GF1A-N01 through GF1A-N12;
- GF1B-N13 through GF1B-N18;
- GF1C-N19 through GF1C-N21;
- any justified GF1E records.

For each ID provide only:

- need_id
- short_title
- source_layer:
    concept_origin |
    research_prompt_original
- final_status:
    retained |
    retained_with_open_questions |
    prompt_checked |
    provisional_method_only |
    withdrawn
- related_open_question_ids
- replacement_record_location:
    STEP1A |
    STEP1B |
    STEP1C |
    STEP1D |
    STEP1E

Do not repeat full need descriptions in this table.

────────────────────────────────────
11. Anti-expansion stop rule
────────────────────────────────────

This step is intended to close the known original-prompt dependency.

Do not propose reading PROMPT-2026Q2-0001 through 0007 merely because original
prompts can theoretically contain hidden detail.

A further GF-STEP-1F prompt-read step is justified only if this step identifies:

- one exact initial-cycle prompt;
- one specific load-bearing need gap or contradiction;
- a concrete reason why the concept-origin evidence and existing need records
  cannot represent it;
- a clear statement of what must be checked in that exact prompt.

Generic residual uncertainty, completeness anxiety, or the fact that an original
exists is insufficient.

User-answer questions may remain open without preventing GF-STEP-1 closure when
the need and the uncertainty are both represented honestly.

Research-report evidence may remain pending without preventing GF-STEP-1
closure when it affects method selection rather than identification of the
underlying need.

────────────────────────────────────
12. Final GF-STEP-1 completion determination
────────────────────────────────────

Choose exactly one:

- GF_STEP_1_complete
- GF_STEP_1_complete_with_explicit_open_questions
- GF_STEP_1_incomplete_exact_initial_prompt_dependency
- GF_STEP_1_incomplete_source_integrity_failure
- GF_STEP_1_incomplete_other_specific_gap

Closure is allowed when:

- all three source SHAs match and all three files were inspected;
- GF1C-N19 and GF1C-N21 have final prompt-checked dispositions;
- the handoff prompt has been assessed against GF1A-N12;
- any newly discovered need is represented;
- all remaining user decisions are explicit open questions;
- all remaining report-dependent matters concern evidence or method selection,
  not an unidentified underlying need;
- no exact unread prompt remains necessary to identify a load-bearing need.

Do not require the research reports to be read merely to close the need-model
reconstruction step.

If GF-STEP-1 closes:

- state whether it is plain completion or completion with explicit open
  questions;
- produce a bounded proposal for GF-STEP-2 only;
- do not execute GF-STEP-2.

If GF-STEP-1 does not close:

- identify the exact blocking source or integrity failure;
- propose a bounded GF-STEP-1F only when the anti-expansion rule is satisfied;
- do not execute it.

────────────────────────────────────
13. Hard workload limits
────────────────────────────────────

- repository source paths: exactly 3
- maximum retrieval/query batteries: 3
- maximum decomposition entries: 27
- maximum new need records: 4
- maximum new questions: 3
- no research-report reads
- no index or summary reads
- no web search
- Research mode OFF
- no automatic continuation into GF-STEP-1F or GF-STEP-2
- stop after the downloadable file and brief chat summary

Word-budget handling policy:

- soft target: 2,200–3,300 words
- hard cap: 4,000 words
- the soft target is advisory, not mandatory
- if the first complete draft is above 3,300 but within 4,000 words, accept it
  without another compression pass
- at most one light compression pass is allowed
- remove repeated narration and duplicated prior-step description before
  evidence, record replacements, questions, ledgers, or closure reasoning
- never omit one of the three prompts from the source or decomposition tables
- never silently truncate a required record
- use compact tables for the final assembly register
- perform no more than one approximate word-count check
- differences between reasonable counting methods are acceptable
- do not repeat compression or counting solely because methods differ

────────────────────────────────────
14. Required deliverable
────────────────────────────────────

Create a downloadable Markdown file named exactly:

FABLE5-GREENFIELD-001-STEP1E-second-tier-prompts-and-final-closure.md

If downloadable artifact creation is unavailable, provide the exact complete
Markdown file body in one fenced block.

Required sections:

1. Metadata
2. Scope and hard limits
3. Allowed sources and anti-contamination policy
4. Evidence interpretation rules
5. Source-access and integrity table
6. MT-0001 decomposition
7. HO-0001 decomposition
8. FTDRE-0001 decomposition
9. GF1C-N19 reassessment and replacement record
10. GF1C-N21 reassessment and replacement record
11. Handoff-related requirement delta
12. Additional GF1E need records, if any
13. Cross-prompt constraint map
14. Updated unresolved-question register
15. Need-record change ledger
16. Final GF-STEP-1 assembly register
17. Incidental-exposure ledger
18. Coverage and limitation ledger
19. GF-STEP-1 completion determination
20. Proposed bounded next step:
    GF-STEP-2 if STEP-1 closes, otherwise GF-STEP-1F only if justified
21. Boundary statement

Metadata must include:

charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-1E
record_type: second_tier_original_prompt_check_and_step1_final_closure
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_steps:
  - GF-STEP-1A
  - GF-STEP-1B
  - GF-STEP-1C
  - GF-STEP-1D
research_mode: false
source_files:
  - path: raw/research-reports/cycles/2026Q2-memory-testing/research-prompts/originals/DR1_memory_testing_debugging_evidence_review_prompt.md
    expected_blob_sha: e6fc63b1548a442e238da4e5740c77eaf9f794fd
  - path: raw/research-reports/cycles/2026Q2-handoff-strategy/research-prompts/originals/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_prompt.md
    expected_blob_sha: 51f3927800b69d25d47e5a5dd86029cbf473c776
  - path: raw/research-reports/cycles/2026Q2-first-target-dry-run-evaluation/research-prompts/originals/DR5_v2_first_real_target_dry_run_evaluation_framework_prompt.md
    expected_blob_sha: 716166c5ae54e341f94909594d99de645a19054c

The coverage ledger must state:

- SHA verification result for each source;
- whether every source was read completely;
- retrieval batteries used;
- source sections covered;
- decomposition entries per prompt;
- need-record actions;
- question actions;
- unused record/question allowance;
- whether initial-cycle originals remain excluded;
- whether GF-STEP-1 can close;
- exact residual dependency if it cannot.

────────────────────────────────────
15. File-content discipline
────────────────────────────────────

Preserve:

- source-qualified prompt evidence;
- N19 and N21 final dispositions;
- handoff-need assessment;
- genuinely distinct new needs;
- question status changes;
- cross-prompt constraints;
- final assembly and closure determination;
- bounded continuation information.

Do not include:

- hidden chain-of-thought;
- long connector narration;
- raw tool logs;
- research-report conclusions;
- web-search content;
- architecture design;
- repair recommendations;
- current-design comparison;
- artifact-control lines;
- duplicated file-presentation messages.

Before presenting the file:

- perform one structural check;
- perform no more than one approximate word-count check;
- ensure all 21 sections exist;
- ensure all three source prompts appear in the integrity and decomposition
  sections;
- ensure the ending is clean;
- do not run another compression cycle when within the hard cap.

────────────────────────────────────
16. Chat response
────────────────────────────────────

After creating the file, provide only a brief summary stating:

- whether the task completed within limits;
- SHA result for each of the three prompts;
- decomposition-entry count for each prompt;
- action selected for GF1C-N19;
- action selected for GF1C-N21;
- handoff-related status for GF1A-N12;
- number and IDs of new need records;
- Q-08, Q-09, and Q-10 statuses;
- number and IDs of new questions;
- retrieval batteries used;
- whether incidental prohibited-tier exposure occurred;
- approximate word count;
- GF-STEP-1 completion determination;
- whether GF-STEP-2 or GF-STEP-1F was proposed;
- whether the downloadable file was created.

Do not repeat the full file in chat.

────────────────────────────────────
17. Boundaries
────────────────────────────────────

Do not:

- write repository files;
- generate Codex tasks;
- update execution source;
- execute any of the three research prompts;
- inspect any research report;
- inspect any other prompt original;
- perform web or external research;
- compare against or repair the existing GPT/Mnemosyne design;
- accept or reject prior Fable review findings;
- begin architecture design or GF-STEP-2;
- create target workspace/material/write/build/regression artifacts;
- resume or close the paused post-handoff route.

This output is non-execution-source advisory evidence only.
Stop after the downloadable file and brief chat summary.
```
