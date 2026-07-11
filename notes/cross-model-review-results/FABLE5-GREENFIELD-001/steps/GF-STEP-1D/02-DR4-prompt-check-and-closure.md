# FABLE5-GREENFIELD-001 — GF-STEP-1D DR4 Prompt Check and Closure Reassessment

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-1D
step_name: minimal_DR4_original_prompt_check_and_step1_closure_reassessment
record_type: minimal_original_prompt_check_and_step1_closure_reassessment
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_steps:
  - GF-STEP-1A
  - GF-STEP-1B
  - GF-STEP-1C
research_mode: false
date: 2026-07-10
source_file: raw/research-reports/cycles/2026Q2-user-input-governance/research-prompts/originals/DR4_user_originals_requirements_redaction_governance_prompt.md
source_ref: master
source_blob_sha_expected: b5739bca54a98d589c2d153d4a92dd26c27675b0
source_blob_sha_verified: true
step_status: STEP1D_complete_GF_STEP_1_incomplete_second_tier_prompt_check_required
```

## 2. Scope and hard limits

Bounded continuation of GF-STEP-1A/1B/1C under its self-contained instruction; no charter retrieval. Limits observed: repository paths 1 of 1; retrieval batteries 1 of 2; additional new need records 0 of 3; new unresolved questions 2 of 3; no research-report reads; no web search; Research mode off; word policy applied (one post-write approximate count; accepted within the 2,800 cap); no automatic continuation into STEP1E or GF-STEP-2.

## 3. Allowed-source and anti-contamination policy

Inputs: the STEP1A/1B/1C deliverables (this conversation's outputs) and the single allowed DR4 original. Retrieval: one single-path raw-endpoint battery; local git blob SHA equals the expected `b5739bca54a98d589c2d153d4a92dd26c27675b0`. No other repository path, prompt original, report, summary, motivation file, or prohibited tier was read. Transparency note: the allowed prompt itself embeds other-track design context — a MNEMOSYNE-057 workspace rule and a candidate `01-user-input` path structure. This is allowed-source-internal content; it is classified `framing_assumption_to_verify`, excluded from the need model by the greenfield firewall, and no prohibited path was opened to pursue it. Prior-exposure disclosure carries forward: independence by derivation and disclosure; wording kept prompt-near; per-record echo flags below; selection-salience caveat standing.

## 4. Original-prompt evidence interpretation rules

The source is an original research prompt: research input, not conclusion, not execution source. Provenance caveat: it is a corrected deep-research prompt produced in the GPT workflow and commissioned/corrected by the user per the STEP1C index; "explicit" below means explicit in the prompt text, not proven verbatim user prose. Applied rules: research questions stay questions; requested evidence and requested schemas are candidates, not proven facts or adopted designs (the prompt itself invites alternatives); nothing is inferred from the unread DR4 report; the delivery rule is treated as task-scoped because its wording binds this rerun, not the memory system; preservation requirements are recorded separately from redaction, visibility, correction and exposure concerns; comparison spaces the prompt deliberately opens are preserved as open.

## 5. DR4 prompt decomposition table

| source_anchor | evidence_category | concise_content | directness | related_existing_need_ids | effect_on_need_model | rationale |
|---|---|---|---|---|---|---|
| ll.1–38 header + "Critical output-delivery rule" | research_delivery_or_process_instruction | full report body mandatory in the final answer; download only backup; chunking fallback; no "summary + link only" | explicit | GF1B-N13 | confirms | user-corrected delivery robustness; corroborates anti-summary stance; task-scoped, not universalized |
| l.16 language rule | research_delivery_or_process_instruction | report in Chinese with English technical terms | explicit | GF1B-N17 | confirms | language policy reaches commissioned outputs; task-scoped |
| l.42 title; ll.52–63 "most sensitive unresolved issue" class list | explicit_user_requirement_or_constraint | ten governed classes: original ideas, raw requirements, restatements, approved decisions, redacted versions, synthetic substitutes, external pointers, sensitive material, Git-history exposure, visibility switching | explicit | GF1C-N20; GF1A-N06, GF1B-N14, GF1A-N03 | refines | defines the governance object set — the core of N20's refinement |
| ll.46–50, 65–73 MNEMOSYNE-057 rule + candidate `01-user-input` structure | framing_assumption_to_verify | other-track workspace rule and candidate paths given as background | explicit | GF1A-N05 | raises_question | firewall: not imported; placement acceptance remains Q-01 territory |
| l.75; l.90 (Q10) | explicit_user_requirement_or_constraint | a practical v0.1 input-governance policy must exist before the first real target-project dry run | explicit | GF1C-N20, GF1C-N21 | refines | load-bearing sequencing constraint invisible at index-title level |
| ll.81–89 research questions 1–9 | research_question_or_requested_evidence | layer separation, per-layer authority, discipline practice, Git vs outside-Git plus pointers, visibility risk, history exposure, redaction verification, restatement linkage, visibility policy | question_only | GF1C-N20; GF1B-N15; GF1A-N06, GF1A-N07 | refines | maps N20's ambiguity structure; deliberately unsettled |
| l.214; l.88 framing | explicit_user_requirement_or_constraint | AI restatements must never be treated as original requirements; restatements link back to user-approved decisions | explicit | GF1A-N06, GF1A-N07 | confirms | governance-layer restatement of the concept-origin preservation and gate principles |
| ll.211–213 constraints | explicit_user_requirement_or_constraint | do not assume Git storage of originals is safe; private repo removes not all risk; Git-history exposure must be considered | explicit | GF1B-N15, GF1C-N20 | refines | adds an explicit exposure-risk dimension to the substrate context |
| ll.215–217 constraints | explicit_user_requirement_or_constraint | no automatic ingestion in v0.1; separate evidence from recommendations; report is not execution source | explicit | GF1A-N11, GF1A-N02, GF1A-N07, GF1B-N18 | confirms | reaffirms staged human-gated intake, epistemic quarantine, and source-of-truth precedence |
| ll.124–207 deliverables A–E | research_question_or_requested_evidence | requested candidate artifacts: per-class storage decision matrix (visibility, authority, redaction, approval), path policy or alternatives, redaction manifest (user approval, residual risk), external-pointer schema (sensitivity, allowed use, non-storage reason), candidate/open-question separation | explicit | GF1C-N20; GF1A-N07, GF1A-N02 | refines | reveals the governance dimensions sought; schemas are candidates with alternatives invited (l.166) |

## 6. GF1C-N20 reassessment and replacement record

Action selected: **refine**.

- need_id: GF1C-N20
- need_title: user_input_layering_redaction_and_exposure_governance (former title: user_originals_requirements_redaction_governance)
- source_anchor: DR4 prompt ll.42, 52–63 (governed classes), l.75 (pre-dry-run policy), ll.81–90 (governance questions), ll.209–217 (constraints)
- source_class: explicit_user_requirement_or_constraint
- interpreted_need: The user-input layer of a target-project memory system needs a governance model that treats as distinct governed classes: original ideas, raw requirements, AI restatements, user-approved decisions, redacted versions, synthetic substitutes, and external pointers — with per-class authority levels; redaction that is documented, verifiable, and user-approved; storage decisions conditioned on repository visibility (public, private, unverified, changing) and Git-history exposure; and provenance links from every transformed form back to originals and approved decisions. A minimal practical version of this policy must exist before the first real target-project dry run.
- scope: explicitly target-project user-input handling; extension to the workspace's own raw layer is plausible but unstated (Q-12).
- relationship_to GF1A-N06, GF1B-N13, and GF1B-N14: confirms GF1A-N06 (restatements never substitute for originals; linkage demanded) and corroborates GF1B-N13 (full-body evidence, anti-summary); GF1B-N14's minimal-edit rule now meets a governed exception space — redaction and synthetic substitution are contemplated as separate, documented, user-approved derivatives, while whether every original is stored in-repo at all becomes an explicit open matter.
- preservation_redaction_tension: the prompt simultaneously preserves originals as a protected class and contemplates redaction, synthetic substitutes, non-storage with external pointers, and visibility-conditioned storage; the reconciliation model is exactly what the research was commissioned to determine and remains unresolved at need level.
- confidence: high
- unresolved_ambiguity: reconciliation model between default preservation and sensitivity-driven redaction/non-storage (Q-07-updated); correction/deletion/withdrawal expectations (Q-11); scope generalization (Q-12); per-class authority levels and visibility policy content (commissioned research territory).
- possible_prior_exposure_echo: false
- derivation_note: refined from the STEP1C signal-level record using only DR4 prompt text; prompt is GPT-workflow-drafted and user-commissioned/corrected, so content is treated as prompt-explicit, not verbatim user prose; embedded other-track design state excluded as framing.

## 7. Additional GF1D need records, if any

None created (0 of 3). External pointers, synthetic substitutes, visibility policy, and provenance mapping are all within the refined GF1C-N20 scope; the sequencing constraint is a dependency between GF1C-N20 and GF1C-N21, not a separate need; the exposure-risk constraints refine context for GF1B-N15 without justifying a new record.

## 8. Preservation/redaction tension map

| tension_aspect | related_need_ids | requirement_or_open_question | compatibility_status | evidence_anchor | temporary_handling |
|---|---|---|---|---|---|
| verbatim/near-verbatim preservation | GF1A-N06, GF1B-N13, GF1B-N14, GF1C-N20 | originals are a protected class; restatements never treated as originals | compatible | ll.52–63, 214 | retained as confirmed |
| minimization / selective retention | GF1C-N20, GF1A-N06 | whether some originals are deliberately not stored in-repo (matrix contemplates it) | unresolved | deliverable A columns; ll.84–85 | preservation-by-default stands until the user decides |
| redaction before storage/publication | GF1C-N20, GF1B-N14 | redaction must be documented, verified, user-approved, as a separate derived artifact | conditional | l.87; deliverable C | compatible with minimal-edit rule iff redactions never silently replace originals |
| correction / deletion / withdrawal | GF1C-N20, GF1A-N08, GF1B-N15 | no explicit expectation appears in the prompt; retention/redaction sources only hint adjacency | unresolved | l.99; manifest `removed_categories` | not assumed; raised as Q-11 |
| private vs public repository handling | GF1C-N20, GF1B-N15 | storage policy must be conditioned on visibility, including unverified and changing states | unresolved | ll.85, 89; matrix columns | visibility-conditioned policy required; content open |
| sensitive information and cloud exposure | GF1C-N20, GF1A-N03, GF1B-N15 | Git storage of originals not assumed safe; private repo not riskless; history exposure real | conditional | ll.211–213 | substrate evaluation must include exposure risk; GF1B-N15 text unchanged |
| human confirmation / authority | GF1C-N20, GF1A-N07, GF1A-N11 | per-layer authority sought; approval fields required; no automatic ingestion in v0.1; report not execution source | compatible | l.82; deliverables A/C; ll.215, 217 | confirms existing gates; granularity stays Q-02 |
| provenance after transformation | GF1C-N20, GF1A-N06, GF1B-N13 | transformed forms link back to originals and approved decisions; source map requested | compatible | l.88; deliverable A "source map" | provenance linkage recorded as governance requirement; schema open |

## 9. Updated unresolved-question register

Carried unchanged and unanswered: Q-01, Q-02, Q-03, Q-04, Q-05, Q-06, Q-08, Q-09 (full wording in STEP1B/STEP1C files).

Q-07 reassessment:

- previous_question: what redaction governance covers for user originals and requirements, and how it reconciles with the verbatim-preservation and minimal-edit rules.
- evidence_found: DR4 defines the governed object classes; demands documented, verified, user-approved redaction; requires visibility- and history-aware storage; requires provenance linkage; imposes a pre-dry-run minimal policy; and deliberately leaves the preservation-vs-redaction/non-storage reconciliation to the commissioned research and user decision.
- status: partially_resolved
- updated_question_if_needed: Q-07-updated — For each governed class, what preservation-vs-redaction/non-storage balance did you decide (or will you decide), independent of any research recommendation? (resolution_source: user_answer; can_GF_STEP_1_close_without_resolution: yes, as an explicit open question; temporary_handling: refined GF1C-N20 carries the tension explicitly.)
- effect_on_GF1C-N20: refined (replacement record in §6).
- can_GF_STEP_1_close_without_further_Q07_evidence: yes

Q-10 refinement (permitted: DR4 provides direct evidence changing the risk assessment): DR4 contained a load-bearing constraint invisible at index-title level (the pre-dry-run sequencing rule) plus substantive governance constraints. Risk is therefore raised for the supplemental-cycle deep prompts (MT-0001, HO-0001, FTDRE-0001 — FTDRE additionally shows a v2 iteration marker), and remains low for the initial-cycle prompts 0001–0007, whose topics are independently corroborated by the concept extract. resolution_source: original_prompt_read; can_close: partially for the second tier, yes for the initial cycle; temporary_handling: second tier escalated to a closure dependency (§13).

New questions (2 of 3):

- question_id: Q-11
- related_need_ids_or_prompt_ids: GF1C-N20, GF1A-N08, GF1B-N15; PROMPT-2026Q2-UIG-0001
- question_for_user_or_future_evidence_check: Do you expect correction, deletion, or withdrawal rights over stored user originals, and how should they interact with Git-history immutability and exposure?
- why_load_bearing: deletion expectations against an append-only, history-exposing substrate shape the raw layer's core contract.
- resolution_source: user_answer
- can_GF_STEP_1_close_without_resolution: partially
- temporary_handling: no correction/deletion/withdrawal behavior assumed.

- question_id: Q-12
- related_need_ids_or_prompt_ids: GF1C-N20, GF1A-N06
- question_for_user_or_future_evidence_check: Does the DR4 governance model apply only to target-project user input, or also to Mnemosyne's own raw layer (concept extract, research materials)?
- why_load_bearing: determines whether one governance need or two differently-scoped needs exist.
- resolution_source: user_answer
- can_GF_STEP_1_close_without_resolution: partially
- temporary_handling: recorded as target-project-explicit; own-layer application flagged, not assumed.

## 10. GF-STEP-1 assembly delta

- Changed records: GF1C-N20 — refined (title updated; scope, tension, and ambiguities specified); status provisional → retained (prompt-checked); related questions now Q-07-updated, Q-11, Q-12.
- Newly added records: none.
- Changed question statuses: Q-07 → partially_resolved with updated wording; Q-10 → refined risk split (second tier elevated, initial cycle low); Q-11 and Q-12 added.
- Unchanged provisional records: GF1C-N19 (Q-08), GF1C-N21 (Q-09) — both awaiting the second-tier check.
- Remaining known unread-source dependencies: PROMPT-2026Q2-MT-0001, PROMPT-2026Q2-HO-0001, PROMPT-2026Q2-FTDRE-0001 originals (closure-blocking, §13); PROMPT-2026Q2-0001…0007 originals (low priority per refined Q-10); the DR4 research report exists but is not a Step-1 dependency — the user's decisions, not the report, resolve need-level questions.

## 11. Incidental-exposure ledger

None. The single-path retrieval exposed no other repository path. The allowed prompt's embedded references to other-track design state (MNEMOSYNE-057, candidate paths) are allowed-source-internal content, handled as framing only (§3, §5); no prohibited path was opened.

## 12. Coverage and limitation ledger

- Source blob SHA: verified equal to expected `b5739bca54a98d589c2d153d4a92dd26c27675b0`.
- Retrieval batteries: 1 of 2 used.
- Prompt sections inspected: all 217 lines — header/delivery rule, language rule, title, background, research questions 1–10, sources list, output structure, deliverables A–E, constraints.
- Allowances: additional new records 0 of 3 used; new questions 2 of 3 used.
- Excluded originals not read: MT-0001, HO-0001, FTDRE-0001, and 0001…0007; no report, summary, or motivation file read.
- Can GF-STEP-1 close: not yet.
- Exact residual source dependency: the three supplemental-cycle prompt originals — MT-0001, HO-0001, FTDRE-0001 (paths as listed in the STEP1C index; expected SHAs to be pinned in the STEP1E instruction).

## 13. GF-STEP-1 completion determination

Determination: **GF_STEP_1_incomplete_second_tier_prompt_check_required**.

Reasoning against the closure criteria: DR4 itself no longer leaves a hidden load-bearing gap — the governance need is specified (refined GF1C-N20) and its residue is honest open questions (Q-07-updated, Q-11, Q-12). However, DR4 demonstrated that a supplemental-cycle deep prompt can carry a load-bearing constraint invisible at index-title level (the pre-dry-run sequencing rule). The three unread supplemental-cycle deep prompts share that class (dedicated cycles; FTDRE shows a v2 iteration marker like DR4's correction), and two of them anchor records that are still provisional (GF1C-N19, GF1C-N21). A known unread prompt class with a demonstrated pattern of embedded load-bearing constraints fails the criterion that no unread prompt be necessary merely to identify a missing load-bearing need. The initial-cycle originals do not block closure: their topics are independently corroborated by the concept extract and remain covered by refined Q-10 at low priority. Closure is therefore deferred to one bounded second-tier check, not forced.

## 14. Proposed bounded GF-STEP-1E (not executed)

- step_name: second_tier_prompt_check_and_step1_final_closure.
- Minimum necessary source set (each justified, not blanket-included): FTDRE-0001 original — strongest necessity: v2 iteration marker plus direct coupling to the DR4 pre-dry-run sequencing constraint; anchors provisional GF1C-N21. MT-0001 original — anchors provisional GF1C-N19; dedicated supplemental cycle of the demonstrated risk class. HO-0001 original — same risk class; quantitative-evaluation emphasis feeding GF1C-N19 and touching GF1A-N12. Initial-cycle originals 0001…0007 excluded unless the user escalates refined Q-10.
- Work: confirm, refine, or downgrade GF1C-N19 and GF1C-N21; extract only prompt-supported constraints; resolve or convert Q-08 and Q-09; then re-run the completion determination and either close GF-STEP-1 (plain or with explicit open questions) or state the exact residual gap.
- Limits: ≤3 repository paths with pinned expected SHAs; ≤3 retrieval batteries; ≤4 new or amended records (GF1E numbering if new); ≤3 new questions; soft 1,400–2,200 words, hard cap 2,800; same evidence categories, interpretation rules, ledgers, and boundaries; stop after the file.

## 15. Boundary statement

This file is non-execution-source advisory evidence only. It authorizes no repository writes, no Codex tasks, no execution-source updates, no execution of the DR4 research prompt, no inspection of its report or of any other prompt original, no external research, no comparison against or repair of the existing design, no acceptance or rejection of prior Fable findings, no architecture design or GF-STEP-2 work, no target workspace/material/write/build/regression actions, and no resumption or closure of the paused post-handoff route. `current/human-approved-spec.md` remains Mnemosyne's only execution source; any conflict between this file and it is resolved in the execution source's favor and reported, never silently reconciled. GF-STEP-1D is complete; GF-STEP-1 is not complete.
