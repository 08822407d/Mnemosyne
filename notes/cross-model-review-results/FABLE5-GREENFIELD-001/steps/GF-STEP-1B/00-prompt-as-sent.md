# FABLE5-GREENFIELD-001 — GF-STEP-1B Prompt as Sent

```text
Run the next bounded substep of FABLE5-GREENFIELD-001.

step_id: GF-STEP-1B
step_name: deferred_origin_need_extraction_and_question_consolidation
relationship_to_charter: continuation of GF-STEP-1A; GF-STEP-1 remains incomplete

Execution setting:
- Research mode must remain OFF.
- Continue in this same Fable 5 conversation.
- Use the attached
  FABLE5-GREENFIELD-001-STEP1A-core-needs-pilot.md
  as the prior-step input.
- Do not search conversation history or repository notes for the charter.
- This prompt is self-contained and governs this bounded substep.

Purpose:
Extract the remaining explicitly deferred user-origin themes from the same
near-original concept source, avoid duplicating GF-STEP-1A records, consolidate
the unresolved user-question list, and prepare—but not execute—the next bounded
GF-STEP-1C.

This is still need-model reconstruction. It is not architecture design,
comparison, review of the current design, or repair work.

────────────────────────────────────
1. Allowed inputs
────────────────────────────────────

Allowed attachment:
- FABLE5-GREENFIELD-001-STEP1A-core-needs-pilot.md

Allowed repository source:
- raw/concept-origin-extract-001.md
- ref: master
- expected blob SHA:
  b47248f1052ecac679c2e3a0afab4d93ca2c6649

Use the STEP1A attachment only to:
- avoid duplicate need records;
- continue numbering after GF1A-N12;
- consolidate unresolved questions;
- preserve continuity of classifications and ledgers.

Read no other repository path.

Do not read or search:
- current/**
- handoff/**
- notes/**
- commands/**
- manual-import-inbox/**
- research reports, research summaries or research prompts
- MNEMOSYNE task results
- FABLE5 review or triage outputs
- existing GPT-produced designs, templates, schemas or decisions
- external websites or web-search results

Do not search for the charter. The current prompt provides the necessary
step-level authority and limits.

If retrieval exposes prohibited material incidentally, log it and do not use it.

────────────────────────────────────
2. Themes to inspect
────────────────────────────────────

Inspect only the STEP1A-deferred themes from the concept-origin source:

- §0 and §16:
  preservation-method and source-sufficiency meta-needs
- §4:
  GitHub/file-based substrate exploration, extracting the underlying user need
  rather than treating an early mechanism as already approved
- §9:
  idea-capture / candidate-buffer need
- §12:
  language-policy need and its evolving status
- §17:
  usage-boundary and raw-material sufficiency questions

Do not broaden into unrelated sections merely to fill the record allowance.

Section §18 import sequencing remains outside this substep unless a short
cross-reference is necessary to explain an unresolved question. Do not create a
full need record for it in STEP1B.

────────────────────────────────────
3. Classification rule
────────────────────────────────────

Continue using only:

- user_origin_evidence
- assistant_origin_era_proposal
- mixed_or_uncertain

For this step, the following methodological point is confirmed:

The “理由和考量” blocks may be used only as compiler-attributed motivation or
context. They must not be quoted or represented as standalone original user
statements.

“助手核心回应” material may be listed in the assistant-era mechanism register,
but must not be silently converted into user requirements.

For every new need record include:

- need_id
- need_title
- source_anchor
- source_class
- interpreted_need
- motivation_or_fear
- confidence: high | medium | low
- stability_assessment:
    stable_looking |
    evolving |
    unclear
- unresolved_ambiguity
- possible_prior_exposure_echo: true | false
- derivation_note

Continue numbering from:

GF1B-N13

Do not renumber or rewrite GF1A-N01 through GF1A-N12.

────────────────────────────────────
4. Hard workload limits
────────────────────────────────────

- maximum new need records: 8
- maximum repository retrieval/query batteries: 2
- repository source paths: exactly 1
- no web search
- no Research mode
- no automatic continuation into GF-STEP-1C
- stop after the downloadable file and brief chat summary

Word-budget handling policy:

- soft target: 1,100–1,700 words
- hard cap: 2,200 words
- the soft target is advisory, not mandatory
- if the first complete draft is above 1,700 but within 2,200 words, accept it
  without another compression pass
- do not rewrite the whole file merely to reach the soft target
- at most one light compression pass is allowed, and only to remove clear
  repetition, tool narration, or redundant explanation
- never remove source evidence, required fields, mechanism provenance,
  unresolved questions, ledgers, or continuation information merely to reduce
  word count
- if complete required content would exceed 2,200 words:
  - shorten optional explanation first
  - preserve every complete required record
  - move optional elaboration into the proposed STEP1C continuation
  - never silently truncate
- perform no more than one final approximate word-count check
- differences between reasonable word-count methods are acceptable
- do not repeat counting or compression solely because two counting methods
  produce different totals
- prioritize a complete, structurally valid downloadable artifact over stylistic
  compression

────────────────────────────────────
5. Assistant-era mechanism register
────────────────────────────────────

Create a short register of mechanisms proposed by the concept-time assistant in
the inspected themes.

For each register item state:

- mechanism_id
- short_description
- source_section
- relationship_to_user_need
- status:
    context_only_not_user_approved |
    mixed_or_uncertain |
    explicitly_user_accepted_if_source_proves_it
- must_not_be_treated_as_requirement: true | false

Keep this register short. It is provenance clarification, not design work.

────────────────────────────────────
6. Consolidated unresolved-question list
────────────────────────────────────

Produce one question list covering STEP1A and STEP1B.

Carry forward unresolved questions that remain unanswered, including:

- whether raw evidence outside prohibited tiers records user acceptance or
  amendment of the dual-layer design-record placement proposal;
- intended approval granularity for the human-confirmed execution layer.

Do not answer these questions by inference.

The prior STEP1A charter-availability question is resolved for this substep:
this prompt is self-contained, and no charter retrieval is permitted.

For every question include:

- question_id
- related_need_ids
- question_for_user
- why_load_bearing
- can_design_continue_without_answer: yes | partially | no
- temporary_handling

Do not ask the user in chat during this execution. Preserve the questions in the
file for later human handling.

────────────────────────────────────
7. Required deliverable
────────────────────────────────────

Create a downloadable Markdown file named exactly:

FABLE5-GREENFIELD-001-STEP1B-deferred-needs-and-questions.md

If downloadable artifact creation is unavailable, provide the exact complete
Markdown file body in one fenced block.

Required sections:

1. Metadata
2. Scope and workload limits
3. Allowed sources and anti-contamination policy
4. Prior-step linkage and non-duplication rule
5. Deferred-theme need inventory
6. Assistant-era mechanism register
7. Consolidated unresolved-question list
8. Incidental-exposure ledger
9. Coverage ledger
10. Proposed bounded GF-STEP-1C
11. Boundary statement

Metadata must include:

charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-1B
record_type: independent_need_model_continuation
authority_level: non_execution_source_advisory_evidence
step_status: STEP1B_complete_GF_STEP_1_not_complete
author_model: Fable 5
prior_step: GF-STEP-1A

The coverage ledger must state:

- which deferred themes were inspected;
- which were converted into records;
- which were inspected but not extracted;
- number of retrieval batteries used;
- whether any record allowance remained;
- why GF-STEP-1 is still incomplete.

The proposed GF-STEP-1C must be bounded and should address the charter’s
research-prompt-index input layer. Do not execute STEP1C.

────────────────────────────────────
8. File-content discipline
────────────────────────────────────

Preserve only:

- source evidence;
- classifications;
- extracted needs;
- assistant-era mechanism provenance;
- unresolved questions;
- limitations and exposure records;
- continuation information.

Do not include:

- hidden chain-of-thought;
- long planning narration;
- repository connector logs;
- word-count optimization narration;
- artifact-control messages;
- duplicated “presented file” text.

Before presenting the file:

- perform one structural check;
- perform no more than one approximate word-count check;
- ensure all required sections exist;
- ensure the file ending is clean;
- do not perform another compression cycle if the file is within the hard cap.

────────────────────────────────────
9. Chat response
────────────────────────────────────

After creating the file, provide a brief summary stating:

- whether the task completed within limits;
- number and ID range of new need records;
- number of retrieval batteries used;
- number of assistant-era mechanism entries;
- number of consolidated unresolved questions;
- whether incidental prohibited-tier exposure occurred;
- reported approximate word count;
- whether the downloadable file was created;
- confirmation that GF-STEP-1 remains incomplete.

Do not repeat the full file in chat.

────────────────────────────────────
10. Boundaries
────────────────────────────────────

Do not:

- write repository files;
- generate Codex tasks;
- update execution source;
- compare against the current GPT/Mnemosyne design;
- accept or reject prior Fable findings;
- recommend or perform repairs;
- begin architecture design;
- inspect research reports or research prompts;
- create target workspace/material/write/build/regression artifacts;
- resume or close the paused post-handoff route.

This output is non-execution-source advisory evidence only.
Stop after the downloadable file and brief chat summary.
```
