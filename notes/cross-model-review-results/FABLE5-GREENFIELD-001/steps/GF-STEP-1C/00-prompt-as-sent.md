# FABLE5-GREENFIELD-001 — GF-STEP-1C Prompt as Sent

```text
Run the next bounded substep of FABLE5-GREENFIELD-001.

step_id: GF-STEP-1C
step_name: research_prompt_index_signal_extraction_and_step1_gap_map
relationship_to_charter: continuation of GF-STEP-1A and GF-STEP-1B;
GF-STEP-1 completion must be assessed, not assumed

Execution setting:
- Research mode must remain OFF.
- Continue in the same Fable 5 conversation.
- Attach and use:
  - FABLE5-GREENFIELD-001-STEP1A-core-needs-pilot.md
  - FABLE5-GREENFIELD-001-STEP1B-deferred-needs-and-questions.md
- Do not retrieve the charter from the repository or conversation history.
- This prompt is self-contained and governs this bounded substep.

Purpose:
Examine the repository's current research-prompt index as an evidence layer
about what the user considered important enough to commission research on.

Map those research-commissioning signals to the needs already extracted in
GF-STEP-1A and GF-STEP-1B, identify genuine need-model gaps or unresolved
assumptions, and determine whether GF-STEP-1 can honestly be completed from the
available index alone.

This is not external research, capability analysis, architecture design,
comparison with the current GPT design, or repair work.

────────────────────────────────────
1. Allowed inputs
────────────────────────────────────

Allowed attachments:

- FABLE5-GREENFIELD-001-STEP1A-core-needs-pilot.md
- FABLE5-GREENFIELD-001-STEP1B-deferred-needs-and-questions.md

Allowed repository source:

- raw/research-reports/current/current-research-prompts.md
- ref: master
- expected blob SHA:
  a686ce7fe382d69754cf292c709870cfbb838e83

Read no other repository path.

In particular, do not open:

- the original individual research-prompt files named by the index;
- research reports or report summaries;
- research-cycle motivation files;
- current/**
- handoff/**
- notes/**
- commands/**
- manual-import-inbox/**
- MNEMOSYNE task results;
- FABLE5 review or triage outputs;
- existing GPT-produced designs, schemas, templates or decisions;
- external websites or web-search results.

Do not use Research mode.

If retrieval incidentally exposes a prohibited source, log it and do not use it.

────────────────────────────────────
2. Evidence-status discipline
────────────────────────────────────

The allowed repository file is a derived current index.

It records:

- which research prompts exist;
- their identifiers and topic titles;
- which research cycle or report they relate to;
- whether original prompt files are available.

It does not, by itself, contain the complete wording of every original user
research prompt.

Therefore:

- do not treat a topic title as a verbatim user statement;
- do not treat a research prompt as a research conclusion;
- do not treat commissioning a research topic as automatic approval of any
  design mechanism;
- do not infer detailed requirements that the index does not contain;
- do not claim that an original prompt was inspected when only its index row
  was inspected.

Use these evidence classes for this step:

- research_commissioning_signal
- derived_index_metadata
- mixed_or_uncertain

Do not label an index-derived record as user_origin_evidence.

────────────────────────────────────
3. Required analytical work
────────────────────────────────────

A. Build a prompt-index coverage table.

Cover every prompt or prompt group present in the allowed index, including:

- PROMPT-2026Q2-0001 through PROMPT-2026Q2-0007;
- PROMPT-2026Q2-MT-0001;
- PROMPT-2026Q2-HO-0001;
- PROMPT-2026Q2-UIG-0001;
- PROMPT-2026Q2-FTDRE-0001.

For each entry record:

- prompt_id
- topic_title
- cycle_or_group
- original_prompt_availability
- evidence_class
- mapped_existing_need_ids
- possible_need_gap
- original_prompt_read_needed: yes | no | uncertain
- rationale

B. Map the commissioning signals to GF-STEP-1A and GF-STEP-1B.

Do not rewrite the full prior need records.

Use references such as:

- GF1A-N01
- GF1B-N15

Identify:

- clearly covered signals;
- partially covered signals;
- signals not represented in GF1A-N01 through GF1B-N18;
- apparent gaps that may only be index-title artifacts;
- questions that require reading the original prompt before creating a new
  need record.

C. Create new need records only when justified by the index itself.

Maximum new records: 6.

Continue numbering from:

GF1C-N19

A new record is allowed only when:

- the index provides a clear, load-bearing commissioning signal;
- the signal is not already represented by GF1A-N01 through GF1B-N18;
- the record can be stated without inventing content from an unread original
  prompt.

Every new record must contain:

- need_id
- need_title
- source_anchor
- source_class:
    research_commissioning_signal |
    derived_index_metadata |
    mixed_or_uncertain
- interpreted_need_or_priority_signal
- mapped_prompt_ids
- relationship_to_existing_need_records
- confidence: high | medium | low
- unresolved_ambiguity
- original_prompt_read_needed: yes | no | uncertain
- possible_prior_exposure_echo: true | false
- derivation_note

Do not add records merely to use the allowance.

D. Produce a GF-STEP-1 assembly map.

The assembly map must list:

- GF1A-N01 through GF1A-N12;
- GF1B-N13 through GF1B-N18;
- any justified GF1C records.

For each need ID provide only:

- need_id
- short title
- source layer:
    concept_origin |
    research_commissioning_index
- status:
    retained |
    provisional |
    requires_original_prompt_check
- related open-question IDs

Do not duplicate the full descriptions from STEP1A or STEP1B.

E. Consolidate the unresolved-question list.

Carry forward Q-01 through Q-06 without answering them by inference.

Add new questions only when the research-prompt index introduces a genuinely
load-bearing uncertainty.

For each question state:

- question_id
- related_need_ids_or_prompt_ids
- question_for_user_or_future_evidence_check
- why_load_bearing
- resolution_source:
    user_answer |
    original_prompt_read |
    later_research_evidence
- can_GF_STEP_1_close_without_resolution:
    yes |
    partially |
    no
- temporary_handling

────────────────────────────────────
4. GF-STEP-1 completion decision
────────────────────────────────────

At the end, make one of these status determinations:

- GF_STEP_1_complete
- GF_STEP_1_complete_with_explicit_open_questions
- GF_STEP_1_incomplete_original_prompt_check_required
- GF_STEP_1_incomplete_other_gap

Do not declare GF-STEP-1 complete merely because all index rows were mapped.

Completion is allowed only if:

- the concept-origin themes are represented;
- the research-commissioning signals are represented at the appropriate
  evidence strength;
- no unread original prompt is necessary to identify a potentially
  load-bearing missing need;
- remaining uncertainties can honestly remain explicit open questions rather
  than hidden gaps.

If original prompt text is required, propose a bounded GF-STEP-1D identifying
the minimum prompt files to inspect. Do not execute STEP1D.

────────────────────────────────────
5. Hard workload limits
────────────────────────────────────

- repository paths: exactly 1
- maximum repository retrieval/query batteries: 2
- maximum new need records: 6
- maximum new unresolved questions: 5
- no original prompt-file reads
- no research-report reads
- no web search
- no Research mode
- no automatic continuation into STEP1D or GF-STEP-2
- stop after the downloadable file and brief chat summary

Word-budget handling policy:

- soft target: 1,500–2,300 words
- hard cap: 2,800 words
- the soft target is advisory, not mandatory
- if the first complete draft is above 2,300 but within 2,800 words, accept it
  without another compression pass
- at most one light compression pass is allowed
- remove repetition and optional narration before removing evidence,
  mappings, questions, ledgers or completion criteria
- do not duplicate full prior-step need descriptions
- never silently omit an index entry
- if required content would exceed the hard cap, shorten the assembly-map
  descriptions and preserve the full coverage table
- perform no more than one final approximate word-count check
- differences between reasonable word-count methods are acceptable
- do not repeat compression or counting solely because different methods
  produce different totals

────────────────────────────────────
6. Required deliverable
────────────────────────────────────

Create a downloadable Markdown file named exactly:

FABLE5-GREENFIELD-001-STEP1C-research-prompt-index-gap-map.md

If downloadable artifact creation is unavailable, provide the exact complete
Markdown file body in one fenced block.

Required sections:

1. Metadata
2. Scope and workload limits
3. Allowed-source and anti-contamination policy
4. Evidence-status rules
5. Research-prompt-index coverage table
6. Existing-need coverage and gap analysis
7. New GF1C need records, if any
8. GF-STEP-1 assembly map
9. Consolidated unresolved-question list
10. Incidental-exposure ledger
11. Coverage and limitation ledger
12. GF-STEP-1 completion determination
13. Proposed bounded GF-STEP-1D, only if required
14. Boundary statement

Metadata must include:

charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-1C
record_type: research_prompt_index_need_signal_mapping
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_steps:
  - GF-STEP-1A
  - GF-STEP-1B
research_mode: false
source_file: raw/research-reports/current/current-research-prompts.md
source_ref: master
source_blob_sha_expected:
  a686ce7fe382d69754cf292c709870cfbb838e83

The coverage ledger must state:

- every prompt ID or prompt group inspected;
- whether the expected source blob SHA was verified;
- retrieval batteries used;
- new-record allowance used and unused;
- which original prompt files, if any, remain necessary;
- whether the result is sufficient to close GF-STEP-1.

────────────────────────────────────
7. File-content discipline
────────────────────────────────────

Preserve:

- prompt-index evidence;
- mappings to existing need IDs;
- properly qualified new records;
- uncertainty and source-strength distinctions;
- completion or residual-gap determination;
- continuation information.

Do not include:

- hidden chain-of-thought;
- long planning narration;
- repository connector logs;
- word-count optimization narration;
- web-search content;
- research-report conclusions;
- artifact-control lines;
- duplicated file-presentation messages.

Before presenting the file:

- perform one structural check;
- perform no more than one approximate word-count check;
- ensure every required section exists;
- ensure the ending is clean;
- do not perform another compression cycle when within the hard cap.

────────────────────────────────────
8. Chat response
────────────────────────────────────

After creating the file, provide only a brief summary stating:

- whether the task completed within limits;
- number of prompt-index entries or groups mapped;
- number and ID range of new need records;
- number of new unresolved questions;
- number of retrieval batteries used;
- whether incidental prohibited-tier exposure occurred;
- reported approximate word count;
- GF-STEP-1 completion determination;
- whether a bounded STEP1D was proposed;
- whether the downloadable file was created.

Do not repeat the full file in chat.

────────────────────────────────────
9. Boundaries
────────────────────────────────────

Do not:

- write repository files;
- generate Codex tasks;
- update execution source;
- inspect original research-prompt files;
- inspect research reports or summaries;
- perform new external research;
- compare against the existing GPT/Mnemosyne design;
- accept or reject earlier Fable findings;
- recommend or perform repairs;
- begin architecture design or GF-STEP-2;
- create target workspace/material/write/build/regression artifacts;
- resume or close the paused post-handoff route.

This output is non-execution-source advisory evidence only.
Stop after the downloadable file and brief chat summary.
```
