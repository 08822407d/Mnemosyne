# FABLE5-GREENFIELD-001 — GF-STEP-1E Second-Tier Prompt Check and Final Closure

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-1E
step_name: second_tier_prompt_check_and_step1_final_closure
record_type: second_tier_original_prompt_check_and_step1_final_closure
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_steps:
  - GF-STEP-1A
  - GF-STEP-1B
  - GF-STEP-1C
  - GF-STEP-1D
research_mode: false
date: 2026-07-10
source_files:
  - path: raw/research-reports/cycles/2026Q2-memory-testing/research-prompts/originals/DR1_memory_testing_debugging_evidence_review_prompt.md
    expected_blob_sha: e6fc63b1548a442e238da4e5740c77eaf9f794fd
  - path: raw/research-reports/cycles/2026Q2-handoff-strategy/research-prompts/originals/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_prompt.md
    expected_blob_sha: 51f3927800b69d25d47e5a5dd86029cbf473c776
  - path: raw/research-reports/cycles/2026Q2-first-target-dry-run-evaluation/research-prompts/originals/DR5_v2_first_real_target_dry_run_evaluation_framework_prompt.md
    expected_blob_sha: 716166c5ae54e341f94909594d99de645a19054c
step_status: STEP1E_complete_GF_STEP_1_complete_with_explicit_open_questions
```

## 2. Scope and hard limits

Bounded continuation of GF-STEP-1A…1D under its self-contained instruction; no charter retrieval. Limits observed: repository paths 3 of 3; retrieval batteries 3 of 3; decomposition entries 24 of 27 max (within the 15–24 target); new need records 0 of 4; new questions 1 of 3; no research-report, index, or summary reads; no web search; Research mode off; no automatic continuation into GF-STEP-1F or GF-STEP-2. Word budget: the first draft exceeded the 4,000-word cap; the single permitted light compression pass removed narration/connective wording only; final count in the step summary.

## 3. Allowed sources and anti-contamination policy

Inputs: the four prior deliverables (this conversation's outputs) and exactly the three pinned prompt originals, each fetched by a single-path raw-endpoint battery and SHA-verified before reading. No other repository path or prohibited-tier material was read or opened by any means. All three prompts internally name other-track files, task IDs, and implementation state; these are prompt-internal framing, recorded by name only in §5, never opened, never imported. Prior-exposure disclosure carries forward: independence by derivation and disclosure; prompt-near wording; per-record echo flags; selection-salience caveat standing.

## 4. Evidence interpretation rules

Each source is an original research prompt: research input, evidence of what was considered important — not conclusions, not proof of requested facts, not execution source, not schema approval. Applied: research questions stay questions; requested metrics, taxonomies, benchmarks, templates, and schemas are candidates, not validated methods; nothing inferred from unread reports; delivery instructions treated as task-scoped; needs (testability, reliable handoff, first-target validation) stay distinct from proposed methods, package strategies, frameworks; embedded current-design context is framing only; source-specific uncertainty preserved; near-duplicate records avoided in favor of refinement. Provenance caveat: "explicit" means explicit in prompt text — all three are GPT-workflow-drafted, user-commissioned (DR1 first-person user voice; DR2 third-person "the user") — not proven verbatim user prose.

## 5. Source-access and integrity table

| prompt_id | repository_path | expected_blob_sha | observed_blob_sha | sha_match | complete_file_inspected | approximate_line_count | retrieval_battery | prohibited_reference_names_seen | referenced_material_opened | access_notes |
|---|---|---|---|---|---|---|---|---|---|---|
| MT-0001 | …/2026Q2-memory-testing/…/DR1_…_prompt.md | e6fc63b1… | e6fc63b1… | true | true | 186 | 1 | design-conception bullets; layer vocabulary | false | raw endpoint; full read; full paths/SHAs in §1 |
| HO-0001 | …/2026Q2-handoff-strategy/…/DR2_…_prompt.md | 51f39278… | 51f39278… | true | true | 450 | 2 | current/handoff/notes/commands file names (§3.2); MNEMOSYNE-034–050 | false | raw endpoint; full read |
| FTDRE-0001 | …/2026Q2-first-target-dry-run-evaluation/…/DR5_v2_…_prompt.md | 716166c5… | 716166c5… | true | true | 293 | 3 | MNEMOSYNE-053; PRO-01…04; B1 items; gate names | false | raw endpoint; full read |

Path/SHA abbreviations are display-only.

## 6. MT-0001 decomposition

| prompt_id | source_anchor | evidence_category | concise_content | directness | related_existing_need_ids | effect_on_need_model | report_evidence_would_still_be_required | rationale |
|---|---|---|---|---|---|---|---|---|
| MT-0001 | ll.14–24 exclusions | research_delivery_or_process_instruction | evidence review only; no framework/product/template design; multi-model review only as evaluation method | explicit | GF1C-N19 | refines | true | user-imposed need/method separation |
| MT-0001 | ll.30–39 background conception | framing_assumption_to_verify | embedded design conception (files-as-memory, layering, no auto write-back, handoff startup) | explicit | GF1A-N09, GF1A-N07, GF1A-N12, GF1B-N15 | framing_only | false | other-track framing; not imported |
| MT-0001 | l.40 current-stage priority | explicit_user_requirement_or_constraint | present focus: verify Mnemosyne can design usable frameworks for real targets | explicit | GF1C-N21 | confirms | false | validation-first priority signal |
| MT-0001 | ll.44–53 goals, esp. 5–6 | research_question_or_requested_evidence | define "working correctly"; grade method maturity (mature/prototype/inference); fit to semi-automatic stage | explicit | GF1C-N19, GF1A-N02, GF1A-N11 | refines | true | maturity grading and stage fit demanded of any evaluation |
| MT-0001 | ll.57–102 test targets + failure floor | research_question_or_requested_evidence | 13 test-target capabilities; ≥15 failure classes with symptoms, tests, repairs, evidence maturity | question_only | GF1C-N19, GF1C-N20, GF1C-N21 | refines | true | requested floors reveal evaluability scope; taxonomy stays candidate |
| MT-0001 | ll.131–143 dry-run advice | research_question_or_requested_evidence | observation set; success/failure signal recording; defect attribution (template/model/user-need/tool); issue routing | explicit | GF1C-N21, GF1C-N19, GF1A-N04 | refines | true | evidence, attribution and routed follow-up as dry-run properties |
| MT-0001 | ll.176–186 output constraints | explicit_user_requirement_or_constraint | no auto-writeback or MCP/RAG/Actions assumptions; internal memory not truth source; multi-model opinions not factual evidence; dated uncertainty labels | explicit | GF1A-N02, GF1A-N09 | confirms | false | epistemic honesty constraints restated at evaluation layer |

## 7. HO-0001 decomposition

| prompt_id | source_anchor | evidence_category | concise_content | directness | related_existing_need_ids | effect_on_need_model | report_evidence_would_still_be_required | rationale |
|---|---|---|---|---|---|---|---|---|
| HO-0001 | §1 ll.26–36 unanswered questions | explicit_user_requirement_or_constraint | after many real handoffs the user cannot define correct handoff, required content, detail level, quantitative evaluation, per-tool variation | explicit | GF1A-N12, GF1C-N19 | refines | true | declared correctness gap: operational definition is a need |
| HO-0001 | §1 l.37 imperfect-but-usable | explicit_user_requirement_or_constraint | "not too far from correct" quantitative starting framework, usable now, refined through use | explicit | GF1C-N19, GF1A-N04, GF1A-N11 | refines | true | iterative-adoption stance; quantitative baseline demanded |
| HO-0001 | §1 ll.39–42 self-history dual role | explicit_user_requirement_or_constraint | own construction history = research sample and test case | explicit | GF1A-N12, GF1C-N19 | refines | false | self-application extended to self-evaluation |
| HO-0001 | §2 ll.52–63 scope surfaces | research_delivery_or_process_instruction | handoff surfaces to cover: chat↔chat, chat→Codex, Codex→chat, maintainer→fresh, cross-model/tool; failure list | explicit | GF1A-N12 | refines | false | user-salient transition surfaces |
| HO-0001 | RQ1 ll.118–134 correctness floor | research_question_or_requested_evidence | ≥11 correctness dimensions incl. authority/approval recovery, stale resistance, unsupported-assumption handling, privacy preservation, provenance recovery, no re-asking | explicit | GF1A-N12, GF1A-N07, GF1C-N20 | refines | true | definition floor; content still commissioned |
| HO-0001 | RQ2 ll.136–146; RQ7 ll.242–243 | research_question_or_requested_evidence | min/standard/extended tiers with exclusions; overlong→instruction loss and too-short→missing constraints both failures | explicit | GF1A-N12 | refines | true | balance is need-level; tiers candidate |
| HO-0001 | RQ3 ll.148–171; RQ6 ll.211–226; Del.F ll.356–374 | research_question_or_requested_evidence | ≥14-metric weighted rubric with gates and verdicts; per-test model/tool provenance schema; cross-model robustness metric | explicit | GF1C-N19, GF1A-N10, GF1A-N12 | refines | true | quantified, provenance-recorded, model-aware evaluation; methods candidate |
| HO-0001 | §5.1 l.260; Del.G ll.376–380 | explicit_user_requirement_or_constraint | report must state what to do before the first real dry run; "more research" alone forbidden as recommendation | explicit | GF1C-N21, GF1C-N19 | refines | true | pre-dry-run readiness coupling; anti-deferral constraint |
| HO-0001 | §8 ll.401–412 constraints | explicit_user_requirement_or_constraint | no assumed writes; no auto-writeback requirement; old exports not truth; reports not execution source; automation mechanisms research-gated; no single-vendor overfit; facts vs recommendations; v0.1 vs v0.2 | explicit | GF1A-N02, GF1A-N10, GF1B-N18, GF1A-N11 | confirms | false | vendor neutrality reinforces model-replaceability needs |

## 8. FTDRE-0001 decomposition

| prompt_id | source_anchor | evidence_category | concise_content | directness | related_existing_need_ids | effect_on_need_model | report_evidence_would_still_be_required | rationale |
|---|---|---|---|---|---|---|---|---|
| FTDRE-0001 | ll.3–9, 18–30 header + delivery rule | research_delivery_or_process_instruction | v2 rerun; full report body mandatory; download only backup; chunking fallback | explicit | GF1B-N13 | confirms | false | DR4-pattern corrected delivery; task-scoped |
| FTDRE-0001 | ll.36–46 background state | framing_assumption_to_verify | other-track state: replay PASS, workspace principle, DR4/PRO/B1 done, gates, nothing selected/ingested/written | explicit | GF1C-N21, GF1A-N05 | framing_only | false | design-state vocabulary excluded by firewall |
| FTDRE-0001 | l.48 pre-validation framework | explicit_user_requirement_or_constraint | an evidence-supported, operational evaluation framework must exist before real-need validation; synthetic tests, drafts, single outputs must not pass as real validation | explicit | GF1C-N21, GF1C-N19, GF1A-N02 | refines | true | sequencing plus anti-self-deception requirement |
| FTDRE-0001 | goals 2, 5, 9, 10 ll.57–70 | research_question_or_requested_evidence | five-stage object model (smoke/tabletop/real dry-run/delivery/write); governance compliance checks; findings routed to improvement candidates without execution-source contamination; target vs global lesson separation | explicit | GF1C-N21, GF1C-N20, GF1A-N07, GF1B-N18, GF1A-N04 | refines | true | staged object model and contamination-safe feedback loop |
| FTDRE-0001 | goal 7 l.67; Del.A columns; l.287 | explicit_user_requirement_or_constraint | checks split into deterministic, LLM-judge, and user-confirmed; LLM-as-judge never sole reviewer | explicit | GF1A-N07, GF1C-N19, GF1C-N21 | refines | true | evaluation-authority split is need-level; allocation is method |
| FTDRE-0001 | Del.A ll.148–165; Del.B ll.171–183 | research_question_or_requested_evidence | 14 mandated dimensions and 10 critical blockers incl. no-target-write, synthetic-vs-real separation, unsafe originals, missing approvals | explicit | GF1C-N21, GF1C-N20, GF1A-N12 | refines | true | mandated floors reveal minimum gates; scorecard candidate |
| FTDRE-0001 | Del.C ll.198–211; ll.281–288 | explicit_user_requirement_or_constraint | PASS ≠ production-ready ≠ target-write approval ≠ global rule update; one success never updates execution source; report not execution source; private repo ≠ sensitive-original permission; history exposure real | explicit | GF1A-N07, GF1B-N18, GF1C-N20, GF1C-N21 | refines | false | authority containment of validation results; DR4 governance echoes |
| FTDRE-0001 | Del.D/E ll.213–265; goal 11 | research_question_or_requested_evidence | minimal postmortem and regression-record schemas: lessons split, user decisions needed, evidence paths, forbidden claims, failure class, follow-up | explicit | GF1C-N21, GF1C-N19, GF1B-N13 | refines | true | requested evidence-preservation structure; schemas candidate |

## 9. GF1C-N19 reassessment and replacement record

Action selected: **refine**.

- need_id: GF1C-N19
- need_title: memory_system_testability_evaluability_and_failure_diagnosis
- source_anchors: MT-0001 ll.44–53, 57–102, 131–143, 176–186; HO-0001 §1 ll.26–42, RQ3–RQ4, RQ6, Deliverable F; STEP1C index row
- source_class: explicit_user_requirement_or_constraint
- interpreted_need: The external memory system — its layering, source priority, handoff, state recovery, staleness and conflict handling, confirmation and privacy boundaries — must be testable, debuggable, and diagnosable. "Working correctly" needs an operational definition (user-declared undefined); failure modes need a named taxonomy with observable symptoms and repair paths; evaluation must be quantitative or semi-quantitative with blocking gates, imperfect-but-usable now and refined through use; methods must be graded by evidence maturity and by fit to the current semi-automatic stage; evaluations must record model/tool provenance; the system's own construction history serves as sample and test bed.
- scope: the memory system's evaluability and the evaluation practice around it; method selection deferred to research evidence and user adoption.
- relationship_to GF1A-N11 and GF1A-N12: extends N11's reviewability from construction diffs to system behavior; gives N12's handoff a correctness-measurement dimension while the handoff continuity need itself remains N12.
- distinction_between_need_and_candidate_metrics: the need is evaluability with operational definitions, taxonomy, quantitative gates, provenance, and stage fit; the specific metric sets, weights, benchmark comparisons, test suites, and rubrics the prompts request are candidate methods — none validated by being requested.
- confidence: high
- unresolved_ambiguity: which metrics, failure classes, methods, and rubric are adopted (Q-08-updated); how the deterministic/LLM-judge/user-confirmation split is allocated (split existence required by FTDRE; contents open).
- related_question_ids: Q-08-updated
- possible_prior_exposure_echo: false
- derivation_note: refined from the STEP1C signal using only the three prompt texts and the index; prompt-near wording; embedded design conception treated as framing; provenance caveat per §4.

## 10. GF1C-N21 reassessment and replacement record

Action selected: **refine**.

- need_id: GF1C-N21
- need_title: staged_first_target_validation_with_gated_authority
- source_anchors: FTDRE-0001 l.48, ll.57–70, 148–183, 198–211, 213–265, 279–289; MT-0001 l.40, ll.131–143; HO-0001 §5.1, Deliverable G; DR4 l.75 via STEP1D
- source_class: explicit_user_requirement_or_constraint
- interpreted_need: The meta-agent's first application to a real target must be validated through an explicitly staged process that: separates synthetic smoke tests, tabletop runs, real target dry runs, delivery, and repository writes, and never lets synthetic or draft evidence pass as real validation; is judged by a pre-defined, evidence-supported framework combining deterministic, model-assisted, and user-confirmed checks — the model never sole judge; verifies governance compliance (authority and source mapping, target runtime truth source, no-target-write, safe input storage); preserves dry-run evidence through postmortem and regression records with defect attribution, issue routing, and target-versus-global lesson separation, so findings feed improvement candidates without contaminating the execution source; and confers no authority on success — a pass approves neither target writes nor global rule updates without user decision.
- scope: first-target validation and its evidence practice; framework, dimensions, blockers, scorecard, templates = candidate method content.
- prerequisites (per prompt evidence), existing before the real dry run: a practical v0.1 user-input governance policy (DR4, STEP1D), a workable handoff baseline (HO-0001 §5.1, Deliverable G), and the evaluation framework itself (FTDRE-0001 l.48).
- relationship_to GF1A-N05, GF1A-N11, GF1C-N19, and GF1C-N20: exercises N05's delivery side under explicit truth-source checks; extends N11's staging into staged adoption; consumes N19's evaluability; is gated by N20's governance policy.
- distinction_between_validation_need_and_candidate_framework: the need is staged, gated, evidence-preserving validation with authority containment; the 14-dimension table, blocker list, scorecard, verdict taxonomy, and templates remain candidates pending report evidence and user adoption.
- confidence: high
- unresolved_ambiguity: first-target identity (user decision); adopted framework content (report evidence plus user decision); ordering and sufficiency of the prerequisite gates.
- related_question_ids: Q-09-updated, Q-07-updated, Q-08-updated
- possible_prior_exposure_echo: false
- derivation_note: refined using only the three prompt texts plus the STEP1D DR4 finding; DR5's background state vocabulary treated as framing and not imported; prompt-near wording; provenance caveat per §4.

## 11. Handoff-related requirement delta

Status: **GF1A_N12_requires_refinement** — delta only; all other GF1A-N12 fields stand as in STEP1A.

Delta to GF1A-N12 (self_bootstrap_and_handoff_continuity), supported by HO-0001: the handoff need explicitly extends to (a) heterogeneous transition surfaces — chat↔chat, chat→coding-agent task, task-result→chat verification, maintainer→fresh session, cross-model/version; (b) resistance to stale-state import and old-conversation contamination — old exports are historical examples, never current truth; (c) recovery of authority, approvals, boundaries, forbidden actions — not only content and next steps; (d) continuation without re-asking already-answered questions; and (e) deliberate completeness-versus-compactness balance — overlong and too-short packages are both named failures. Operational definition and quantification of handoff correctness sit in refined GF1C-N19; tiers, rubrics, protocols remain candidate methods. New ambiguity: handoff trigger criteria remain undefined (Q-13). No distinct new need: every load-bearing HO-0001 signal lands in GF1A-N12, GF1C-N19, or existing records.

## 12. Additional GF1E need records, if any

None created (0 of 4). Synthetic-versus-real separation, verdict containment, evaluation-authority split, provenance recording, and vendor neutrality all land within refined GF1C-N19/N21, the GF1A-N12 delta, or confirmations of GF1A-N02/N07/N09/N10 and GF1B-N18.

## 13. Cross-prompt constraint map

| concern | source_prompt_ids | related_need_ids | prompt_supported_requirement_or_question | candidate_method_or_metric | status | research_report_needed_for_method_selection |
|---|---|---|---|---|---|---|
| testability and observability | MT, HO | GF1C-N19, GF1A-N11 | operational "working correctly" definition with observable properties | DR1 §C method families | refined_need | true |
| debugging and failure diagnosis | MT | GF1C-N19 | named failure taxonomy with triggers, symptoms, tests, repairs, maturity | 15-class floor (§B) | refined_need | true |
| evaluation criteria and metrics | MT, HO, FTDRE | GF1C-N19 | quantitative/semi-quantitative scoring with blocking gates | RQ3 metrics; scorecard B | refined_need | true |
| handoff triggers | HO | GF1A-N12 | handoff timing undefined; tiers requested, thresholds open | tier "when to use" guidance | open_question | true |
| handoff package completeness vs compactness | HO | GF1A-N12 | both over- and under-packaging are named failures; balance is need-level | min/standard/extended tiers | refined_need | true |
| quantitative comparison of handoff strategies | HO | GF1C-N19, GF1A-N12 | strategies comparable via protocol on own construction history | RQ4 protocol; 8-case suite | refined_need | true |
| first-target dry-run prerequisites | FTDRE, HO, DR4 via STEP1D | GF1C-N21, GF1C-N20, GF1A-N12 | governance policy, handoff baseline, and evaluation framework precede the real dry run | Deliverable F integration classes | refined_need | true |
| first-target success/failure criteria | FTDRE | GF1C-N21 | pre-defined verdict semantics with critical blockers | dimension table; blocker list; verdicts | refined_need | true |
| dry-run evidence preservation | FTDRE, MT | GF1C-N21, GF1C-N19, GF1B-N13 | postmortem and regression records with evidence paths, attribution, forbidden claims | schemas D/E | refined_need | true |
| dry run ↔ user-input governance | FTDRE, DR4 via STEP1D | GF1C-N21, GF1C-N20 | safe-input/redaction/pointer compliance are dry-run gates; unsafe ingestion/storage are blockers | blocker rows | confirmed_need | true |
| human approval and authority | MT, HO, FTDRE | GF1A-N07, GF1C-N21, GF1B-N18 | user-confirmed checks mandatory; LLM-judge never sole reviewer; approvals recovered in handoff; pass confers no authority | check-split allocation | confirmed_need | true |
| report recommendations vs prompt requirements | MT, HO, FTDRE | GF1A-N02, GF1B-N18 | reports never execution source; facts and recommendations separated; automation mechanisms research-gated | — | confirmed_need | false |

## 14. Updated unresolved-question register

Carried unchanged, unanswered: Q-01…Q-06, Q-07-updated, Q-11, Q-12 (full wording in STEP1B/1C/1D).

Q-08 reassessment:

- previous_question_or_status: which metrics, failure classes, and evaluation methods the MT and HO prompts specify; whether the need is sufficiently represented though method choice requires report evidence.
- prompt_evidence_found: MT: 13-item test-target floor; ≥15-class failure floor with per-class fields and maturity grading; method families; stage-fit demand. HO: 11-dimension correctness floor; ≥14-metric weighted rubric with gates and verdicts; 10-test protocol; 8-case self-history suite; provenance schema.
- status: converted_to_method_selection_question
- updated_question_if_needed: Q-08-updated — which methods, metrics, failure taxonomy, rubric, and authority-split allocation do you adopt once report evidence is reviewed?
- related_need_record_effect: GF1C-N19 refined (§9).
- can_GF_STEP_1_close_without_further_prompt_reading: yes

Q-09 reassessment:

- previous_question_or_status: what the FTDRE prompt defines as the first real target and what the dry run must demonstrate.
- prompt_evidence_found: no target is named — target-selection validity is itself a dimension and "target_not_selected" a critical blocker, so selection is a pending user decision; what the dry run must demonstrate is defined at need level (stage separation, governance compliance, usable delivery without target writes, evidence preservation, contained authority).
- status: partially_resolved
- updated_question_if_needed: Q-09-updated — which project is the first real target, and which evaluation-framework content do you adopt for its dry run?
- related_need_record_effect: GF1C-N21 refined (§10).
- can_GF_STEP_1_close_without_further_prompt_reading: yes

Q-10 reassessment (second-tier portion):

- previous_question_or_status: second-tier deep prompts elevated to a closure dependency after DR4's precedent; initial-cycle originals low priority.
- prompt_evidence_found: all three contained load-bearing content invisible at index level (MT: maturity grading, stage fit, attribution/routing; HO: correctness gap, completeness/compactness pair, provenance schema, anti-deferral; FTDRE: five-stage separation, verdict containment, prerequisite coupling, model-never-sole-judge) — all now captured in refined records, the N12 delta, and the constraint map.
- status: partially_resolved — second-tier portion resolved; the initial-cycle portion remains an explicit low-priority, non-blocking note under the anti-expansion rule (no exact prompt, no specific gap; initial-cycle topics independently corroborated by concept-origin evidence).
- updated_question_if_needed: none; the initial-cycle note stands inside Q-10 as worded.
- related_need_record_effect: none beyond §9–§11.
- can_GF_STEP_1_close_without_further_prompt_reading: yes

New question (1 of 3):

- question_id: Q-13
- related_need_ids_or_prompt_ids: GF1A-N12; HO-0001
- question_for_user_or_future_evidence_check: What should trigger a handoff (context-length threshold, state-based trigger, or event-based rule), and which package tier applies to which trigger?
- why_load_bearing: N12's founding ambiguity ("too long" undefined) survives DR2, which covers strategy and evaluation, not triggers.
- resolution_source: user_answer (with later_research_evidence as input)
- can_GF_STEP_1_close_without_resolution: yes
- temporary_handling: no trigger assumed; explicit open parameter of GF1A-N12.

## 15. Need-record change ledger

- Retained unchanged: GF1A-N01…N11; GF1B-N13…N18.
- Refined: GF1A-N12 (delta only, §11); GF1C-N19 (replacement, §9); GF1C-N21 (replacement, §10).
- Split: none. Downgraded: none. Withdrawn: none. Genuinely new: none.

## 16. Final GF-STEP-1 assembly register

| need_id | short_title | source_layer | final_status | related_open_question_ids | replacement_record_location |
|---|---|---|---|---|---|
| GF1A-N01 | durable_external_memory | concept_origin | retained | — | STEP1A |
| GF1A-N02 | capability_honesty_quarantine | concept_origin | retained | — | STEP1A |
| GF1A-N03 | per_scenario_meta_agent | concept_origin | retained | — | STEP1A |
| GF1A-N04 | continuous_evolution_intake | concept_origin | retained | — | STEP1A |
| GF1A-N05 | design_record_placement_tension | concept_origin | retained_with_open_questions | Q-01 | STEP1A |
| GF1A-N06 | raw_preservation_digests | concept_origin | retained_with_open_questions | Q-03, Q-07-updated | STEP1A |
| GF1A-N07 | human_confirmed_execution_layer | concept_origin | retained_with_open_questions | Q-02 | STEP1A |
| GF1A-N08 | requirement_reconciliation | concept_origin | retained_with_open_questions | Q-02, Q-11 | STEP1A |
| GF1A-N09 | state_externalization | concept_origin | retained | — | STEP1A |
| GF1A-N10 | migration_constraint_lifecycle | concept_origin | retained_with_open_questions | Q-03 | STEP1A |
| GF1A-N11 | small_step_staged_construction | concept_origin | retained | — | STEP1A |
| GF1A-N12 | self_bootstrap_handoff | concept_origin | prompt_checked | Q-13 | STEP1E(delta)+STEP1A |
| GF1B-N13 | evolution_evidence_commentary | concept_origin | retained_with_open_questions | Q-03 | STEP1B |
| GF1B-N14 | minimal_edit_discipline | concept_origin | retained_with_open_questions | Q-07-updated | STEP1B |
| GF1B-N15 | versioned_file_substrate | concept_origin | retained_with_open_questions | Q-04 | STEP1B |
| GF1B-N16 | idea_capture_buffer | concept_origin | retained_with_open_questions | Q-05 | STEP1B |
| GF1B-N17 | chinese_first_language | concept_origin | retained_with_open_questions | Q-06 | STEP1B |
| GF1B-N18 | bounded_raw_usage_spec_precedence | concept_origin | retained | — | STEP1B |
| GF1C-N19 | testability_evaluability_failure_diagnosis | research_prompt_original | prompt_checked | Q-08-updated | STEP1E |
| GF1C-N20 | user_input_layering_redaction_exposure_governance | research_prompt_original | prompt_checked | Q-07-updated, Q-11, Q-12 | STEP1D |
| GF1C-N21 | staged_first_target_validation_gated_authority | research_prompt_original | prompt_checked | Q-09-updated, Q-07-updated, Q-08-updated | STEP1E |

## 17. Incidental-exposure ledger

None. Three single-path retrievals exposed no other path; prompt-internal references to other-track files, task IDs, and state were recorded by name only (§5), never opened.

## 18. Coverage and limitation ledger

- SHA verification: all three sources verified, exact match (§1, §5).
- Complete reads: all three read in full (186, 450, 293 lines; every section covered).
- Retrieval batteries: 3 of 3 used, one per pinned path.
- Decomposition entries: MT-0001 7; HO-0001 9; FTDRE-0001 8; total 24 of 27 max.
- Need-record actions: GF1C-N19 refined; GF1C-N21 refined; GF1A-N12 refined by delta; no splits, downgrades, withdrawals, or new records (0 of 4).
- Question actions: Q-08 converted_to_method_selection_question; Q-09 partially_resolved, updated; Q-10 second tier resolved, initial-cycle note non-blocking; Q-13 added (1 of 3).
- Initial-cycle originals (0001…0007): remain excluded; anti-expansion rule unsatisfied for all.
- GF-STEP-1 can close: yes — with explicit open questions.
- Exact residual dependency: none blocking; remaining items: user decisions (Q-01…Q-07-updated, Q-09-updated, Q-11…Q-13) and report-gated method selection (Q-08-updated).

## 19. GF-STEP-1 completion determination

Determination: **GF_STEP_1_complete_with_explicit_open_questions**.

Closure criteria: all three SHAs match, all three files fully inspected; GF1C-N19 and GF1C-N21 hold final prompt-checked dispositions; HO-0001 assessed against GF1A-N12 with a bounded refinement delta; every load-bearing second-tier signal is represented in a refined record, the N12 delta, or a confirmation; remaining user decisions are explicit open questions; remaining report-dependent matters concern evidence and method selection, not need identification; no exact unread prompt is necessary to identify a load-bearing need — the initial-cycle originals fail the anti-expansion test. The GF-STEP-1 need model comprises GF1A-N01…N12 (with the N12 delta), GF1B-N13…N18, and prompt-checked GF1C-N19…N21, carrying open questions Q-01…Q-13 as registered.

## 20. Proposed bounded next step (GF-STEP-2)

GF-STEP-1 closes, so GF-STEP-2 is proposed; GF-STEP-1F is not justified.

- step_name: independent_capability_boundary_baseline (per the charter step sequence recorded in this track's prior deliverables).
- Purpose: an independent baseline of what current tools, models, and platforms can actually do — capability facts with evidence grading — as the second input to a later independent architecture step; no design work.
- Allowed sources: to be pinned by the user in the GF-STEP-2 instruction (report-layer access needs explicit authorization with exact paths and blob SHAs — every Step-1 substep prohibited report reads — plus rules for evidence-classing report conclusions).
- Suggested limits: exact pinned paths; per-path SHA verification; a battery cap; evidence classes (mature practice / prototype / inference / vendor claim); question-register carry-forward; soft/hard word budgets; stop after one file; no architecture, comparison, or repair work.
- Not executed here.

## 21. Boundary statement

This file is non-execution-source advisory evidence only. It authorizes no repository writes, no Codex tasks, no execution-source updates, no execution of any research prompt, no inspection of any research report or further prompt original, no external research, no comparison against or repair of the existing design, no acceptance or rejection of prior Fable findings, no architecture design or GF-STEP-2 work, no target workspace/material/write/build/regression actions, and no resumption or closure of the paused post-handoff route. `current/human-approved-spec.md` remains Mnemosyne's only execution source; any conflict between this file and it is resolved in the execution source's favor and reported, never silently reconciled. GF-STEP-1E is complete; GF-STEP-1 is complete with explicit open questions.
