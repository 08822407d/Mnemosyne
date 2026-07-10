# GF-STEP-1A prompt as sent

```yaml
record_type: reconstructed_prompt_preservation
source: current_maintenance_conversation_visible_text
verbatim_status: prompt_body_copied_from_visible_conversation_text
research_setting: not_checked
conversation: same_Fable_5_conversation
```

```text
Run the next bounded substep of FABLE5-GREENFIELD-001.

step_id: GF-STEP-1A
step_name: core_user_need_extraction_pilot
relationship_to_charter: bounded pilot of GF-STEP-1, not completion of GF-STEP-1

Use the FABLE5-GREENFIELD-001 charter already present in this conversation as
the governing task charter. Do not retrieve the charter from the repository if
doing so would require opening the prohibited notes/** design tier.

Purpose:
Test the Fable 5 usage window with a small but independently valuable task,
while beginning the greenfield reconstruction from original user-need evidence.

This step must reconstruct a limited set of high-confidence user needs from the
near-original concept material. It must not design the architecture, compare
against the GPT/Mnemosyne design, or inspect research evidence yet.

────────────────────────────────────
1. Allowed source
────────────────────────────────────

Read only:

- raw/concept-origin-extract-001.md

Do not read:

- current/**
- handoff/**
- notes/**
- commands/**
- any MNEMOSYNE task result
- any FABLE5 review or triage result
- any existing GPT-produced design, template, schema, decision record or
  execution-source document
- research reports, research summaries or research prompts during this pilot

Do not use web search or external sources.

If repository retrieval accidentally exposes material from a prohibited path,
record it in the incidental-exposure ledger and do not use it.

────────────────────────────────────
2. Hard workload limits
────────────────────────────────────

You must obey all of these limits:

- maximum repository retrieval/query batteries: 4
- maximum extracted need records: 12
- target downloadable-file length: 1,200–1,800 words
- maximum absolute file length: 2,200 words
- stop after producing the requested file
- do not continue automatically into GF-STEP-1B or any later step
- do not attempt complete coverage of the source document
- do not compensate for incomplete coverage by broadening the source scope

If the limits prevent full coverage, preserve that fact in the coverage ledger.

────────────────────────────────────
3. Extraction method
────────────────────────────────────

For each extracted item, distinguish the origin of the statement carefully.

Use only these source_class values:

- user_origin_evidence
- assistant_origin_era_proposal
- mixed_or_uncertain

Do not silently convert a concept-time assistant proposal into a user
requirement.

Every need record must contain:

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

Source anchors should be short. Do not reproduce long passages.

Extract only high-confidence, load-bearing needs. Prefer needs that influence the
purpose, authority model, lifecycle, evidence handling, human control, model
replaceability, multi-project operation or long-term evolution of a persistent
memory meta-agent.

Do not propose implementation mechanisms unless they are needed to explain an
ambiguity. This step is a need-model extraction, not architecture design.

────────────────────────────────────
4. Known-contamination disclosure
────────────────────────────────────

Fable 5 has previously reviewed parts of the current Mnemosyne design.

Therefore:

- do not claim clean-room independence by amnesia;
- state that this step is independent by derivation and disclosure;
- mark an item possible_prior_exposure_echo: true when its formulation may have
  been influenced by prior exposure and the origin evidence does not force the
  same wording;
- do not reduce confidence merely because a genuine user need also appears in
  the existing design;
- do not mention details of the existing design.

────────────────────────────────────
5. Required deliverable
────────────────────────────────────

Create a downloadable Markdown file named exactly:

FABLE5-GREENFIELD-001-STEP1A-core-needs-pilot.md

If downloadable artifact creation is unavailable, provide the exact complete
Markdown file body in one fenced block and clearly label it as the file to
preserve.

The file must contain these sections:

1. Metadata
2. Scope and workload limits
3. Source and anti-contamination policy
4. Known prior-exposure disclosure
5. Core need inventory
6. Incidental-exposure ledger
7. Coverage ledger
8. Unresolved questions
9. Proposed bounded continuation for GF-STEP-1B
10. Boundary statement

Metadata must include:

charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-1A
record_type: independent_need_model_pilot
authority_level: non_execution_source_advisory_evidence
step_status: pilot_complete_GF_STEP_1_not_complete
author_model: Fable 5

The coverage ledger must state:

- which portions or themes of the source were inspected;
- which portions or themes were not covered;
- whether the four-retrieval limit was reached;
- why the result must not be treated as the complete GF-STEP-1 output.

The proposed GF-STEP-1B continuation must be bounded. It should identify the
next source themes to inspect, but it must not execute them.

────────────────────────────────────
6. File-content discipline
────────────────────────────────────

The downloadable file should preserve:

- source evidence;
- classifications;
- extracted needs;
- uncertainties;
- coverage limitations;
- exposure disclosures;
- continuation information.

Do not place hidden chain-of-thought, long conversational reasoning, artifact UI
messages or tool-operation narration in the file.

Before presenting the file, verify that its ending is clean and contains no
stray artifact-control lines or duplicated presentation text.

────────────────────────────────────
7. Chat response
────────────────────────────────────

After creating the file, provide only a brief chat summary containing:

- whether the task completed within the workload limits;
- number of need records extracted;
- number of retrieval batteries used;
- whether incidental prohibited-tier exposure occurred;
- whether the downloadable file was created successfully;
- confirmation that GF-STEP-1 remains incomplete.

Do not restate the full file in chat if a downloadable file was successfully
created.

────────────────────────────────────
8. Boundaries
────────────────────────────────────

Do not:

- write repository files;
- generate Codex tasks;
- update execution source;
- compare against the existing GPT design;
- recommend repairs to the existing design;
- begin architecture design;
- inspect research reports or prompts;
- create target workspace/material/write/build/regression artifacts;
- resume or close the paused post-handoff route.

This output is non-execution-source advisory evidence only.
Stop after the downloadable file and brief chat summary.
```
