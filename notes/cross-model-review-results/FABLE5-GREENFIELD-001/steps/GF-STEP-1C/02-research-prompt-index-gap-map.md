# FABLE5-GREENFIELD-001 — GF-STEP-1C Research-Prompt-Index Gap Map

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-1C
step_name: research_prompt_index_signal_extraction_and_step1_gap_map
record_type: research_prompt_index_need_signal_mapping
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_steps:
  - GF-STEP-1A
  - GF-STEP-1B
research_mode: false
date: 2026-07-10
source_file: raw/research-reports/current/current-research-prompts.md
source_ref: master
source_blob_sha_expected: a686ce7fe382d69754cf292c709870cfbb838e83
source_blob_sha_verified: true
step_status: STEP1C_complete_GF_STEP_1_incomplete_original_prompt_check_required
```

## 2. Scope and workload limits

Bounded continuation of GF-STEP-1A/1B, governed by its self-contained instruction; no charter retrieval performed. Limits observed: repository paths 1 of 1; retrieval batteries 1 of 2; new need records 3 of 6; new unresolved questions 4 of 5; no original prompt-file reads; no research-report reads; no web search; Research mode off; word policy applied (one post-write approximate count; accepted within the 2,800 hard cap); no automatic continuation into STEP1D or GF-STEP-2.

## 3. Allowed-source and anti-contamination policy

Inputs: the STEP1A and STEP1B deliverables (read from this conversation's outputs) and the single allowed index file. Retrieval: one single-path battery — the GitHub contents API returned a rate-limit response with no repository content, and the fetch was completed via the raw single-path endpoint for the same path; the local git blob SHA equals the expected `a686ce7fe382d69754cf292c709870cfbb838e83`. No `current/**`, `handoff/**`, `notes/**`, `commands/**`, `manual-import-inbox/**` path, original prompt file, research report, summary, or motivation file was read. The index names other repository paths and MNEMOSYNE task IDs; these are recorded as metadata only and were not opened. Provenance note: the index is a derived current view maintained in the GPT-track workflow; it is used here only as commissioning-signal and metadata evidence, never as design input. Prior-exposure disclosure carries forward from STEP1A: independence by derivation and disclosure, wording kept index-near, per-record echo flags below, selection-salience caveat standing.

## 4. Evidence-status rules

The file is a derived index, not user prose. Applied rules: topic titles are not verbatim user statements; commissioning a topic approves no mechanism; prompts are inputs, not conclusions; nothing is inferred beyond what the index states; only index rows were inspected, never original prompts. Evidence classes: the commissioning fact and topic of each entry → `research_commissioning_signal`; availability, status, cycle, path and review-note fields → `derived_index_metadata`; nothing here is labeled `user_origin_evidence`. Titles marked † in the table are compact English glosses of the index's Chinese titles; exact wording is in the source file.

## 5. Research-prompt-index coverage table

| prompt_id | topic_title | cycle_or_group | original_prompt_availability | evidence_class | mapped_existing_need_ids | possible_need_gap | original_prompt_read_needed | rationale |
|---|---|---|---|---|---|---|---|---|
| PROMPT-2026Q2-0001 | AI agent external persistent memory (pro) | RC-2026Q2-initial | available_original_prompt | research_commissioning_signal | GF1A-N01, GF1A-N02 | none | no | founding topic; directly corroborated by concept extract |
| PROMPT-2026Q2-0002 | non-dev long-term dialogue memory: real practice† | RC-2026Q2-initial | available_original_prompt | research_commissioning_signal | GF1A-N01, GF1A-N03, GF1B-N15 | none | no | confirms non-dev scenarios are first-class |
| PROMPT-2026Q2-0003 | ChatGPT/Claude pure-dialogue external-memory boundaries† | RC-2026Q2-initial | available_original_prompt | research_commissioning_signal | GF1A-N02, GF1A-N01 | none | no | capability-boundary honesty in chat scenarios |
| PROMPT-2026Q2-0004 | local dev agents' file-based memory† | RC-2026Q2-initial | available_original_prompt | research_commissioning_signal | GF1A-N09, GF1A-N11, GF1B-N15 | none | no | file-based externalization with local tools |
| PROMPT-2026Q2-0005 | cloud coding agents + GitHub write-back and audit† | RC-2026Q2-initial | available_original_prompt | research_commissioning_signal | GF1B-N15, GF1A-N11, GF1A-N02 | none | no | substrate write-back and audit concern |
| PROMPT-2026Q2-0006 | theory and engineering basis of external memory† | RC-2026Q2-initial | available_original_prompt | research_commissioning_signal | GF1A-N02, GF1A-N09 | none | no | demand for grounded, non-speculative design |
| PROMPT-2026Q2-0007 | dev-memory experience transfer to dialogue/learning† | RC-2026Q2-initial | available_original_prompt | research_commissioning_signal | GF1A-N01, GF1A-N03, GF1A-N05 | none; transfer nuance noted §6 | no | cross-scenario generalization question |
| PROMPT-2026Q2-MT-0001 | memory-system testing/debugging/evaluation/failure diagnosis | RC-2026Q2-memory-testing | available_original_prompt | research_commissioning_signal | GF1C-N19 (new); reinforces GF1A-N11, GF1A-N12 | yes → GF1C-N19 | uncertain | dedicated supplemental cycle = load-bearing signal |
| PROMPT-2026Q2-HO-0001 | handoff package strategy, quantitative evaluation | RC-2026Q2-handoff-strategy | original_available | research_commissioning_signal | GF1A-N12, GF1C-N19 | none new; evaluation emphasis | uncertain | need covered by N12; measurement emphasis feeds N19 |
| PROMPT-2026Q2-UIG-0001 | user originals / requirements / redaction governance | RC-2026Q2-user-input-governance | original_available | research_commissioning_signal | GF1C-N20 (new); adjacent GF1A-N06, GF1B-N13, GF1B-N14 | yes → GF1C-N20 | yes | governance shape not derivable from title; interacts with preservation rules |
| PROMPT-2026Q2-FTDRE-0001 | first real target-project dry-run evaluation framework | RC-2026Q2-first-target-dry-run-evaluation | original_available | research_commissioning_signal | GF1C-N21 (new); extends GF1A-N11, GF1A-N05 | yes → GF1C-N21 | uncertain | staged real-target validation cycle |

## 6. Existing-need coverage and gap analysis

Clearly covered signals: PROMPT-2026Q2-0001 through 0006 map directly onto GF1A-N01/N02/N03/N09/N11 and GF1B-N15; the initial research cycle mirrors the concept-origin themes. Partially covered: 0007's transfer question rests on GF1A-N01/N03/N05 but sharpens N01's open scenario-priority ambiguity — the commissioning shows non-dev transfer was a serious concern, not an afterthought; HO-0001's need is covered by GF1A-N12, while its quantitative-evaluation emphasis is new in degree and feeds GF1C-N19. Signals not represented in GF1A-N01…GF1B-N18: system testing/debugging/failure diagnosis (MT-0001 → GF1C-N19), user-input redaction governance (UIG-0001 → GF1C-N20), and first-real-target dry-run validation (FTDRE-0001 → GF1C-N21). Possible index-title artifacts: 0006's broad title could conceal user constraints; treated as low risk and covered by Q-10 rather than a record. Corroborations at metadata strength: the index's own front matter repeats execution-source precedence (consistent with GF1A-N07, GF1B-N18); the recovery notes record that the user personally recovered six light-prompt originals (consistent with GF1A-N06, GF1B-N13); the UIG note that the corrected prompt requires a full report body and forbids summary-plus-download-only delivery corroborates GF1B-N13's anti-summary stance and proves prompts can carry user-authored process requirements. Questions requiring original-prompt reads before further records: Q-07 (blocking), Q-08, Q-09, Q-10.

## 7. New GF1C need records

- need_id: GF1C-N19
- need_title: memory_system_testability_and_failure_diagnosis
- source_anchor: index row PROMPT-2026Q2-MT-0001 — "testing/debugging/evaluation/failure diagnosis", supplemental cycle RC-2026Q2-memory-testing
- source_class: research_commissioning_signal
- interpreted_need_or_priority_signal: The user judged testing, debugging, evaluation and failure diagnosis of the external memory system important enough to commission a dedicated supplemental cycle; evaluability and diagnosability belong in the need model as first-class concerns.
- mapped_prompt_ids: PROMPT-2026Q2-MT-0001; PROMPT-2026Q2-HO-0001 (evaluation emphasis)
- relationship_to_existing_need_records: absent from GF1A-N01…GF1B-N18; reinforces GF1A-N11's reviewability and GF1A-N12's handoff without duplicating them.
- confidence: medium
- unresolved_ambiguity: intended metrics, failure classes and methods unknown at index level (Q-08).
- original_prompt_read_needed: uncertain
- possible_prior_exposure_echo: false
- derivation_note: built from the commissioning fact and title only; no prompt content used or invented.

- need_id: GF1C-N20
- need_title: user_originals_requirements_redaction_governance
- source_anchor: DR4 block PROMPT-2026Q2-UIG-0001 — "user_originals_requirements_redaction_governance", corrected_deep_research_prompt, cycle RC-2026Q2-user-input-governance
- source_class: research_commissioning_signal
- interpreted_need_or_priority_signal: A governance layer for user originals, requirements and redaction is needed and must coexist with the preservation discipline; the intended balance between verbatim preservation and governed redaction cannot be derived from the index.
- mapped_prompt_ids: PROMPT-2026Q2-UIG-0001
- relationship_to_existing_need_records: new governance dimension adjacent to GF1A-N06, GF1B-N13 and GF1B-N14, and to GF1A-N03's cloud-exposure concern — a potential tension, not a duplicate.
- confidence: medium
- unresolved_ambiguity: what redaction governance covers (sensitivity classes, correction rights, removal scope) and how it reconciles with preservation (Q-07).
- original_prompt_read_needed: yes
- possible_prior_exposure_echo: false
- derivation_note: title-level signal only; the corrected-prompt delivery requirement is logged in §6 as corroboration of GF1B-N13, not folded into this record.

- need_id: GF1C-N21
- need_title: first_real_target_dry_run_validation
- source_anchor: index row PROMPT-2026Q2-FTDRE-0001 — "DR5 first real target-project dry-run evaluation framework", cycle RC-2026Q2-first-target-dry-run-evaluation
- source_class: research_commissioning_signal
- interpreted_need_or_priority_signal: Before the meta-agent's designs are trusted in real use, the user wants a framework for evaluating a dry run on a first real target project — staged, evidence-based validation of delivery.
- mapped_prompt_ids: PROMPT-2026Q2-FTDRE-0001
- relationship_to_existing_need_records: extends GF1A-N11's staged construction into staged adoption and touches GF1A-N05's factory-to-target delivery; shares the evaluation theme with GF1C-N19.
- confidence: medium
- unresolved_ambiguity: what counts as the first real target and what the framework must demonstrate (Q-09).
- original_prompt_read_needed: uncertain
- possible_prior_exposure_echo: false
- derivation_note: commissioning fact and title only; no prompt content invented.

## 8. GF-STEP-1 assembly map

| need_id | short_title | source_layer | status | related_questions |
|---|---|---|---|---|
| GF1A-N01 | durable_external_memory | concept_origin | retained | — |
| GF1A-N02 | capability_honesty_quarantine | concept_origin | retained | — |
| GF1A-N03 | per_scenario_meta_agent | concept_origin | retained | — |
| GF1A-N04 | continuous_evolution_intake | concept_origin | retained | — |
| GF1A-N05 | design_record_placement_tension | concept_origin | retained | Q-01 |
| GF1A-N06 | raw_preservation_digests | concept_origin | retained | Q-03, Q-07 |
| GF1A-N07 | human_confirmed_execution_layer | concept_origin | retained | Q-02 |
| GF1A-N08 | requirement_reconciliation | concept_origin | retained | Q-02 |
| GF1A-N09 | state_externalization | concept_origin | retained | — |
| GF1A-N10 | migration_constraint_lifecycle | concept_origin | retained | Q-03 |
| GF1A-N11 | small_step_staged_construction | concept_origin | retained | — |
| GF1A-N12 | self_bootstrap_handoff | concept_origin | retained | Q-08 |
| GF1B-N13 | evolution_evidence_commentary | concept_origin | retained | Q-03 |
| GF1B-N14 | minimal_edit_discipline | concept_origin | retained | Q-07 |
| GF1B-N15 | versioned_file_substrate | concept_origin | retained | Q-04 |
| GF1B-N16 | idea_capture_buffer | concept_origin | retained | Q-05 |
| GF1B-N17 | chinese_first_language | concept_origin | retained | Q-06 |
| GF1B-N18 | bounded_raw_usage_spec_precedence | concept_origin | retained | — |
| GF1C-N19 | testability_failure_diagnosis | research_commissioning_index | provisional | Q-08 |
| GF1C-N20 | redaction_governance | research_commissioning_index | requires_original_prompt_check | Q-07 |
| GF1C-N21 | first_target_dry_run_validation | research_commissioning_index | provisional | Q-09 |

## 9. Consolidated unresolved-question list

Carried from STEP1B, unanswered, texts unchanged (full wording in the STEP1B file):

- question_id: Q-01 | related: GF1A-N05 | dual-layer placement acceptance evidence | resolution_source: user_answer | can_GF_STEP_1_close_without_resolution: partially | temporary_handling: placement stays an open variable.
- question_id: Q-02 | related: GF1A-N07, GF1A-N08 | approval granularity for the human-confirmed layer | resolution_source: user_answer | can_close: partially | temporary_handling: granularity modeled as a parameter.
- question_id: Q-03 | related: GF1B-N13, GF1A-N06 | near-original sufficiency vs full transcripts | resolution_source: user_answer | can_close: partially | temporary_handling: current extract treated as the only guaranteed evidence.
- question_id: Q-04 | related: GF1B-N15 | substrate hard requirements vs GitHub specifically | resolution_source: user_answer | can_close: partially | temporary_handling: properties encoded, mechanism open.
- question_id: Q-05 | related: GF1B-N16 | idea-buffer activation conditions | resolution_source: user_answer | can_close: yes | temporary_handling: affirmed-but-deferred.
- question_id: Q-06 | related: GF1B-N17 | language-migration trigger and exception list | resolution_source: user_answer | can_close: yes | temporary_handling: Chinese-first assumed.

New in STEP1C:

- question_id: Q-07
- related_need_ids_or_prompt_ids: GF1C-N20, GF1A-N06, GF1B-N14; PROMPT-2026Q2-UIG-0001
- question_for_user_or_future_evidence_check: What does redaction governance for user originals and requirements cover, and how does it reconcile with the verbatim-preservation and minimal-edit rules?
- why_load_bearing: it shapes the raw/intake layer's core contract; preservation versus redaction is a structural tension.
- resolution_source: original_prompt_read
- can_GF_STEP_1_close_without_resolution: no
- temporary_handling: GF1C-N20 held at signal strength; no governance shape assumed.

- question_id: Q-08
- related_need_ids_or_prompt_ids: GF1C-N19; PROMPT-2026Q2-MT-0001, PROMPT-2026Q2-HO-0001
- question_for_user_or_future_evidence_check: Which metrics, failure classes and evaluation methods did the testing and handoff-evaluation prompts specify?
- why_load_bearing: determines whether evaluability introduces structural needs beyond a priority signal.
- resolution_source: original_prompt_read
- can_GF_STEP_1_close_without_resolution: partially
- temporary_handling: GF1C-N19 stays provisional.

- question_id: Q-09
- related_need_ids_or_prompt_ids: GF1C-N21; PROMPT-2026Q2-FTDRE-0001
- question_for_user_or_future_evidence_check: What defines the first real target project and the success criteria its dry-run evaluation must demonstrate?
- why_load_bearing: bounds the staged-adoption need.
- resolution_source: original_prompt_read
- can_GF_STEP_1_close_without_resolution: partially
- temporary_handling: GF1C-N21 stays provisional.

- question_id: Q-10
- related_need_ids_or_prompt_ids: PROMPT-2026Q2-0001 through 0007; all mapped rows
- question_for_user_or_future_evidence_check: Do the pro and light prompt originals contain user-authored constraints beyond their titles that belong in the need model?
- why_load_bearing: residual risk of the index-only method; mappings are title-level.
- resolution_source: original_prompt_read
- can_GF_STEP_1_close_without_resolution: partially
- temporary_handling: mapping confidence capped at title level; risk logged.

## 10. Incidental-exposure ledger

None. The single-path retrieval exposed no other repository path; the rate-limited API attempt returned only a rate-limit message with no repository content; the allowed index references prohibited-tier paths and MNEMOSYNE task IDs, which were recorded as metadata and not opened.

## 11. Coverage and limitation ledger

- Prompt entries inspected and mapped: all 11 — PROMPT-2026Q2-0001…0007, MT-0001, HO-0001, UIG-0001, FTDRE-0001; none omitted.
- Source blob SHA: verified equal to expected `a686ce7fe382d69754cf292c709870cfbb838e83`.
- Retrieval batteries: 1 of 2 used (single path; API rate-limit retry via raw endpoint disclosed above).
- New-record allowance: 3 of 6 used (GF1C-N19…N21); 3 unused, not filled.
- New-question allowance: 4 of 5 used (Q-07…Q-10).
- Original prompt files still necessary: PROMPT-2026Q2-UIG-0001 (required); PROMPT-2026Q2-MT-0001, PROMPT-2026Q2-HO-0001, PROMPT-2026Q2-FTDRE-0001 (uncertain, second tier).
- Sufficiency to close GF-STEP-1: not sufficient from the index alone; see §12.

## 12. GF-STEP-1 completion determination

Determination: **GF_STEP_1_incomplete_original_prompt_check_required**.

Against the completion criteria: concept-origin themes are represented (GF1A-N01…GF1B-N18); research-commissioning signals are represented at appropriate evidence strength (11 of 11 rows mapped, three signal-level records); but an unread original prompt is necessary to specify a potentially load-bearing need — the DR4 redaction-governance prompt defines a governance area whose direction cannot be stated from its title, and it structurally interacts with the preservation rules (GF1A-N06, GF1B-N14). The DR4 correction note also proves that prompt originals can carry user-authored requirements, so the supplemental-cycle prompts cannot be assumed title-complete. These dependencies are known unread sources, not honest open questions, so completion is not declared.

## 13. Proposed bounded GF-STEP-1D (not executed)

- step_name: minimal_original_prompt_check_and_step1_closure.
- Minimum inspection set: the PROMPT-2026Q2-UIG-0001 original (required). Second tier, if budget allows: the MT-0001, HO-0001 and FTDRE-0001 originals (each marked uncertain). Paths as listed in the index; expected blob SHAs to be pinned in the 1D instruction.
- Work: specify or amend GF1C-N20; confirm, refine or downgrade GF1C-N19 and GF1C-N21; resolve or convert Q-07…Q-10; re-run the completion determination and either close GF-STEP-1 (plain or with explicit open questions) or state the residual gap.
- Limits: ≤4 repository paths; ≤2 retrieval batteries; ≤6 new or amended records; ≤4 new questions; soft 1,200–1,800 words, hard cap 2,400; same evidence classes, ledgers and boundaries; stop after the file. The initial-cycle originals (0001…0007) stay excluded unless Q-10 is escalated by the user.

## 14. Boundary statement

This file is non-execution-source advisory evidence only. It authorizes no repository writes, no Codex tasks, no execution-source updates, no original-prompt or research-report inspection, no external research, no comparison against or repair of the existing design, no acceptance or rejection of prior Fable findings, no architecture design or GF-STEP-2 work, no target workspace/material/write/build/regression actions, and no resumption or closure of the paused post-handoff route. `current/human-approved-spec.md` remains Mnemosyne's only execution source; any conflict between this file and it is resolved in the execution source's favor and reported, never silently reconciled. GF-STEP-1C is complete; GF-STEP-1 is not complete.