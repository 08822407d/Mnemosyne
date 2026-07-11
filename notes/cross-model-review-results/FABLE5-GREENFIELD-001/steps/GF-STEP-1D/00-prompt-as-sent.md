# FABLE5-GREENFIELD-001 — GF-STEP-1D Prompt as Sent

```text
Run the next bounded substep of FABLE5-GREENFIELD-001.

step_id: GF-STEP-1D
step_name: minimal_DR4_original_prompt_check_and_step1_closure_reassessment
relationship_to_charter: continuation of GF-STEP-1A, GF-STEP-1B, and GF-STEP-1C;
inspect only the source identified as blocking in STEP1C

Execution setting:
- Research mode must remain OFF.
- Continue in the same Fable 5 conversation.
- Attach and use:
  - FABLE5-GREENFIELD-001-STEP1A-core-needs-pilot.md
  - FABLE5-GREENFIELD-001-STEP1B-deferred-needs-and-questions.md
  - FABLE5-GREENFIELD-001-STEP1C-research-prompt-index-gap-map.md
- Do not retrieve the charter from the repository or conversation history.
- This prompt is self-contained and governs this bounded substep.

Purpose:
Read only the original DR4 / PROMPT-2026Q2-UIG-0001 research prompt that
GF-STEP-1C identified as the blocking unread source. Extract only the
user-requirement and governance signals that the prompt itself supports,
refine or downgrade GF1C-N20, reassess Q-07, and then re-run the GF-STEP-1
completion determination.

This is original-prompt evidence inspection. It is not execution of the
research prompt, not a review of a research report, not architecture design,
not comparison with the current GPT design, and not repair work.

────────────────────────────────────
1. Allowed inputs
────────────────────────────────────

Allowed attachments:
- FABLE5-GREENFIELD-001-STEP1A-core-needs-pilot.md
- FABLE5-GREENFIELD-001-STEP1B-deferred-needs-and-questions.md
- FABLE5-GREENFIELD-001-STEP1C-research-prompt-index-gap-map.md

Allowed repository source — exactly one path:
- raw/research-reports/cycles/2026Q2-user-input-governance/research-prompts/originals/DR4_user_originals_requirements_redaction_governance_prompt.md
- ref: master
- expected blob SHA:
  b5739bca54a98d589c2d153d4a92dd26c27675b0

Read no other repository path.

Explicitly excluded from this substep:
- PROMPT-2026Q2-MT-0001 original
- PROMPT-2026Q2-HO-0001 original
- PROMPT-2026Q2-FTDRE-0001 original
- PROMPT-2026Q2-0001 through PROMPT-2026Q2-0007 originals
- all research reports and report summaries
- research-cycle motivation files
- current/**
- handoff/**
- notes/**
- commands/**
- manual-import-inbox/**
- MNEMOSYNE task records
- FABLE5 review or triage records
- existing GPT-produced design artifacts
- external websites and web-search results

If repository retrieval incidentally exposes prohibited content, log it and do
not use it.

────────────────────────────────────
2. Evidence interpretation rules
────────────────────────────────────

The allowed file is an original research prompt. It is research input, not a
research conclusion and not execution source.

Classify prompt material using only:
- explicit_user_requirement_or_constraint
- research_question_or_requested_evidence
- research_delivery_or_process_instruction
- framing_assumption_to_verify
- mixed_or_uncertain

Apply these rules:
- Do not convert a research question into an already-settled requirement.
- Do not treat requested evidence as if the requested facts were proven.
- Do not infer any conclusion from an unread research report.
- Do not universalize a one-task delivery instruction into a permanent
  memory-system rule unless the wording explicitly supports that broader scope.
- Separate requirements about preserving originals from requirements about
  redaction, privacy, correction, deletion, publication, or repository
  visibility.
- Preserve uncertainty where the prompt deliberately asks research to compare
  alternatives.
- Continue the known prior-exposure disclosure: independent by derivation and
  disclosure, not by claimed amnesia.

────────────────────────────────────
3. Required work
────────────────────────────────────

A. Produce a DR4 prompt decomposition table.

For each load-bearing passage or compact passage group record:
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
    process_only
- rationale

Do not reproduce long prompt passages.

B. Reassess GF1C-N20.

Keep the identifier GF1C-N20. Do not create a duplicate record for the same
governance concern.

Choose one action:
- retain_as_is
- refine
- split
- downgrade_to_priority_signal
- withdraw_as_unsupported

If retained, refined, or split, provide a replacement record containing:
- need_id
- need_title
- source_anchor
- source_class
- interpreted_need
- scope
- relationship_to GF1A-N06, GF1B-N13, and GF1B-N14
- preservation_redaction_tension
- confidence
- unresolved_ambiguity
- possible_prior_exposure_echo
- derivation_note

Maximum additional new need records beyond N20: 3.
Create one only if the DR4 prompt explicitly supports a distinct,
load-bearing need that is not already represented by GF1A-N01 through
GF1C-N21. Continue numbering at GF1D-N22.

C. Produce a requirement-level preservation/redaction tension map.

This is not an architecture proposal. Record only what the prompt supports
about:
- verbatim or near-verbatim preservation
- minimization or selective retention
- redaction before storage or publication
- correction, deletion, or withdrawal expectations
- private versus public repository handling
- sensitive information and cloud exposure
- human confirmation or authority
- provenance after transformation

For each tension state:
- related_need_ids
- requirement_or_open_question
- compatibility_status:
    compatible |
    conditional |
    unresolved |
    apparent_conflict
- evidence_anchor
- temporary_handling

Do not invent schemas, workflows, permission systems, or repair proposals.

D. Reassess unresolved questions.

Carry Q-01 through Q-06 and Q-08 through Q-10 without silently answering them.

For Q-07, provide:
- previous_question
- evidence_found
- status:
    resolved |
    partially_resolved |
    unresolved
- updated_question_if_needed
- effect_on_GF1C-N20
- can_GF_STEP_1_close_without_further_Q07_evidence

You may refine Q-10 only if the DR4 original provides direct evidence that
changes the general risk assessment about original prompts carrying additional
user constraints.

Maximum newly created questions: 3.
Continue numbering at Q-11.

E. Produce a GF-STEP-1 assembly delta.

Do not repeat the complete STEP1C assembly table. Record only:
- changed need records
- newly added need records
- changed question statuses
- unchanged provisional records
- remaining known unread-source dependencies

F. Re-run the GF-STEP-1 completion determination.

Choose exactly one:
- GF_STEP_1_complete
- GF_STEP_1_complete_with_explicit_open_questions
- GF_STEP_1_incomplete_second_tier_prompt_check_required
- GF_STEP_1_incomplete_initial_prompt_check_required
- GF_STEP_1_incomplete_other_gap

Do not force closure.

GF-STEP-1 may close with explicit open questions only when:
- DR4 no longer leaves a hidden load-bearing gap;
- remaining uncertainties are honestly represented as questions or provisional
  signals;
- no known unread prompt is necessary merely to identify a missing
  load-bearing need.

If another prompt read is still required, propose one bounded GF-STEP-1E with
the minimum necessary source set. Do not execute it. Do not automatically include
all second-tier prompts.

────────────────────────────────────
4. Hard workload limits
────────────────────────────────────

- repository paths: exactly 1
- maximum repository retrieval/query batteries: 2
- maximum additional new need records: 3
- maximum new unresolved questions: 3
- no research-report reads
- no web search
- Research mode OFF
- no automatic continuation into STEP1E or GF-STEP-2
- stop after the downloadable file and brief chat summary

Word-budget handling policy:
- soft target: 1,400–2,200 words
- hard cap: 2,800 words
- the soft target is advisory, not mandatory
- if the first complete draft is above 2,200 but within 2,800 words, accept it
  without another compression pass
- at most one light compression pass is allowed
- remove repeated narration before evidence, records, questions, ledgers, or
  completion reasoning
- do not duplicate full STEP1A/1B/1C records
- never silently truncate a required section
- perform no more than one approximate word-count check
- differences between reasonable counting methods are acceptable
- do not repeat compression or counting solely because methods differ

────────────────────────────────────
5. Required deliverable
────────────────────────────────────

Create a downloadable Markdown file named exactly:

FABLE5-GREENFIELD-001-STEP1D-DR4-prompt-check-and-closure.md

If downloadable artifact creation is unavailable, provide the exact complete
Markdown file body in one fenced block.

Required sections:
1. Metadata
2. Scope and hard limits
3. Allowed-source and anti-contamination policy
4. Original-prompt evidence interpretation rules
5. DR4 prompt decomposition table
6. GF1C-N20 reassessment and replacement record
7. Additional GF1D need records, if any
8. Preservation/redaction tension map
9. Updated unresolved-question register
10. GF-STEP-1 assembly delta
11. Incidental-exposure ledger
12. Coverage and limitation ledger
13. GF-STEP-1 completion determination
14. Proposed bounded GF-STEP-1E, only if required
15. Boundary statement

Metadata must include:
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-1D
record_type: minimal_original_prompt_check_and_step1_closure_reassessment
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_steps:
  - GF-STEP-1A
  - GF-STEP-1B
  - GF-STEP-1C
research_mode: false
source_file: raw/research-reports/cycles/2026Q2-user-input-governance/research-prompts/originals/DR4_user_originals_requirements_redaction_governance_prompt.md
source_ref: master
source_blob_sha_expected:
  b5739bca54a98d589c2d153d4a92dd26c27675b0

The coverage ledger must state:
- whether the expected source blob SHA was verified
- retrieval batteries used
- which prompt sections were inspected
- new-record and new-question allowances used
- excluded prompt originals not read
- whether GF-STEP-1 can close
- exact residual source dependency if it cannot

────────────────────────────────────
6. File-content discipline
────────────────────────────────────

Preserve:
- source-qualified evidence
- the N20 decision and replacement text
- distinct new needs only when justified
- question status changes
- tension and uncertainty records
- completion or continuation determination

Do not include:
- hidden chain-of-thought
- long tool narration
- connector logs
- research-report conclusions
- web-search content
- architecture proposals
- repair advice
- artifact-control lines
- duplicated file-presentation messages

Before presenting the file:
- perform one structural check
- perform no more than one approximate word-count check
- ensure every required section exists
- ensure the ending is clean
- do not perform another compression cycle when within the hard cap

────────────────────────────────────
7. Chat response
────────────────────────────────────

After creating the file, provide only a brief summary stating:
- whether the task completed within limits
- source blob SHA verification result
- number of decomposition-table entries
- action selected for GF1C-N20
- number and IDs of additional new need records
- Q-07 status
- number of new questions
- retrieval batteries used
- whether incidental prohibited-tier exposure occurred
- reported approximate word count
- GF-STEP-1 completion determination
- whether STEP1E was proposed
- whether the downloadable file was created

Do not repeat the full file in chat.

────────────────────────────────────
8. Boundaries
────────────────────────────────────

Do not:
- write repository files
- generate Codex tasks
- update execution source
- execute the DR4 research prompt
- inspect its research report
- inspect any other original research prompt
- perform external research
- compare against or repair the current GPT/Mnemosyne design
- accept or reject earlier Fable review findings
- begin architecture design or GF-STEP-2
- create target workspace/material/write/build/regression artifacts
- resume or close the paused post-handoff route

This output is non-execution-source advisory evidence only.
Stop after the downloadable file and brief chat summary.
```
