# FABLE5-GREENFIELD-001 — GF-STEP-2B6 Supplemental-Batch Method and Policy Evidence

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2B6
step_name: supplemental_batch_method_and_policy_evidence_review
record_type: supplemental_markdown_reports_batch_review
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-2B5
research_mode: false
date: 2026-07-15
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
step_status: GF_STEP_2B6_complete_supplemental_batch_reviewed_all_reports_read
```

## 2. Scope and hard limits

One integrated batch review of the four supplemental-cycle markdown reports (STEP2A batch 3) — the dedicated method- and policy-selection evidence for Q-07-updated, Q-08-updated, Q-09-updated, and Q-13. Limits: paths 4/4; batteries 4/4 (one per source); evidence records 6+6+6+6 = 24/24 max; questions reassessed exactly Q-07-updated, Q-08-updated, Q-09-updated, Q-13; new questions 2/3 (Q-14, Q-15); matrix rows 12/12; linkage entries 9/9; uncertainty items 10/10; no other reads; no web research; Research mode off; no execution-source effect; no automatic continuation.

## 3. Allowed sources and anti-contamination policy

Inputs: the STEP2B5 deliverable (IDs, question register, evidence rules) and exactly the four pinned markdown originals, each fetched by one single-path raw-endpoint battery and SHA-verified before reading. No other repository file or prohibited tier opened. Firewall note — these reports embed the deepest other-track design state seen in this track (execution-source paths, gate and task IDs, file layouts, replay history): all such embedded repository/design state is report-internal framing, never imported as greenfield design input and never treated as verified repository fact; what this step extracts is the reports' method and policy content as commissioned evidence. Report-internal citations (leftover "citeturn…" tokens mark saved research outputs) are metadata only, never opened or verified. No knowledge outside the reports used to update them. Prior-exposure disclosure carries forward: independence by derivation and disclosure.

## 4. Source integrity and access table

| report_id | expected_blob_sha | observed_blob_sha | sha_match | size | lines | complete_read | battery |
|---|---|---|---|---|---|---|---|
| RPT-2026Q2-MT-0001 | 3cd85dce… | 3cd85dce… | true | 42,495 B | 124 | true | 1 |
| RPT-2026Q2-HO-0001 | 457163a7… | 457163a7… | true | 42,374 B | 508 | true | 2 |
| RPT-2026Q2-UIG-0001 | 81ceb3d5… | 81ceb3d5… | true | 32,029 B | 270 | true | 3 |
| RPT-2026Q2-FTDRE-0001 | cbf188aa… | cbf188aa… | true | 32,576 B | 216 | true | 4 |

Full paths/SHAs in §1; abbreviations display-only.

## 5. Markdown handling and coverage record

All four are markdown text (no PDF, no visual-review dependency); every file read completely — every section, table, YAML block, and closing limitation statement. None states an exact evidence date; cycle-level 2026Q2 applies, with cited material dated 2025–2026. All four are saved deep-research outputs (citation tokens present); all cited external sources remain unverified here.

## 6. RPT-2026Q2-MT-0001 evidence register

Register-wide: complete_read = true; period cycle 2026Q2; citations unverified. 6 records.

| evidence_id | source_anchor | concise_statement | evidence_category | confidence | date_sensitivity | related_research_domain_ids | related_STEP1_need_ids | related_question_ids | prohibited_overclaim |
|---|---|---|---|---|---|---|---|---|---|
| F2B6-MT-01 | 总体结论 ll.3–9 | no unified, mature industry-standard test framework exists for agent external persistent memory (2026Q2); mature pieces are composable sub-capabilities (retrieval-quality eval, traces/observability, CI+regression, human review, code review, postmortems, RAG/agent task eval); memory-specific write/update/forget/conflict/takeover/attribution evaluation is 2025–2026 research-prototype stage (MemoryArena, AMA-Bench, MemGym, LongMemEval-V2, STALE, MemFail, MemTraceBench); silent failures make final-answer accuracy insufficient — state, source, timing, propagation, landability must be checked | report_author_synthesis | high | high | RD-07 | GF1C-N19 | Q-08-updated | absence of a standard is a dated landscape claim |
| F2B6-MT-02 | ll.21–23 | "working correctly" delivered as an operational behavioral definition: cross-session state recovery; execution source outranks summaries/candidates; new decisions propagate to active context and handoff; stale information identified, not reused; outputs evidence-supported; privacy/tool/confirmation boundaries obeyed; failures locatable to write/update/retrieve/summarize/handoff/delivery stage | report_recommendation | high | low | RD-07 | GF1C-N19 | Q-08-updated | recommended definition, pending user adoption |
| F2B6-MT-03 | ll.25–38 | core test-target set plus a 10-metric starter set recommended (recovery correctness, source-priority consistency, stale-rejection rate, conflict-resolution correctness, decision-propagation latency, handoff executability, delivery landability, boundary-violation rate, trace completeness, failure attributability) — human-labeled in semi-automatic dry-runs first, regression suite later | report_recommendation | high | medium | RD-07 | GF1C-N19,N21 | Q-08-updated | metrics unvalidated by measurement |
| F2B6-MT-04 | ll.40–72 | 15-class failure taxonomy delivered with definition/trigger/symptom/test/repair/evidence-maturity per class; maturity spans mature (missing context, under-retention, retrieval failure) through mostly-mature (stale handoff, drift, overwrite, over-retention, hallucinated memory, privacy leakage) to reasonable inference (wrong source priority, handoff-vs-active-context inconsistency, decision-not-propagated) and prototype (stale tool-capability assumption); "dry-run artifact looks complete but cannot land" grounded in mature engineering practice | report_author_synthesis | high | medium | RD-07 | GF1C-N19 | Q-08-updated | taxonomy is a floor with dated maturity labels |
| F2B6-MT-05 | ll.74–102 | stage-fitted method map: RAG/retrieval eval (context precision/recall, faithfulness) most mature — read path only, adopt now; trace-based observability adopt now (diagnosis prerequisite); workflow/plan-compliance eval as regression tests for startup/handoff/memory-policy instructions; human review + status checks + postmortems remain the primary current reliance; memory-specific benchmarks inspire self-built scenario sets, not adoptable frameworks; multi-model review and LLM-judge auxiliary only (prompt sensitivity, shared bias, verbosity bias); large-scale auto trace grading, auto attribution, scheduled red teaming deferred to a future automation stage | mixed_or_uncertain | high | medium | RD-07 | GF1C-N19; GF1A-N02,N11 | Q-08-updated | stage-fit judgments dated 2026Q2 |
| F2B6-MT-06 | ll.104–122 | dry-run observation/attribution/routing guidance: observe handoff pickup, execution-source use, layer separation, uncertainty marking, artifact landability, honest capability exposure; record success/failure/diagnostic signal classes; attribute template defect (cross-model repeated same-class failure → candidate + small fix) vs model slip (→ eval/prompt/reviewer gate) vs incomplete user need (→ user clarification) vs tool boundary (→ capability delta review); seven recommendations incl. five-layer testing (write/manage/read/handoff/delivery), a small-hard real test set, execution-source priority as first-class, file-backed human-reviewed changes, handoff-executability as hard gate, memory postmortems, multi-model review restricted to review-and-question role | report_recommendation | high | medium | RD-07; RD-10 (corroboration) | GF1C-N19,N21; GF1A-N04 | Q-08-updated, Q-09-updated | guidance, not a validated protocol |

## 7. RPT-2026Q2-HO-0001 evidence register

Register-wide: complete_read = true; period cycle 2026Q2; citations unverified; embedded repository-state references treated as framing (§3). 6 records.

| evidence_id | source_anchor | concise_statement | evidence_category | confidence | date_sensitivity | related_research_domain_ids | related_STEP1_need_ids | related_question_ids | prohibited_overclaim |
|---|---|---|---|---|---|---|---|---|---|
| F2B6-HO-01 | 直接结论 ll.3–11 | verdict: handoff direction basically correct but under-quantified; the largest risk is stale currentness promotion (old replays, results, handoffs, exports treated as current truth); one formal scored fresh replay should precede the first real dry-run, with blocking-gate failures preventing progression; two fallacies rejected — longer handoffs are not safer (distraction, instruction loss) and single-model rubric judging is unreliable | report_author_synthesis | high | medium | RD-08 | GF1A-N12; GF1C-N19 | Q-08-updated, Q-13 | verdict presupposes the other track's file layout — framing, not verified fact |
| F2B6-HO-02 | ll.13–38 | operational correct-handoff definition delivered: a fresh session, without implicit old-conversation context, recovers execution source, phase/gate, real status, permissions and forbidden actions, done/undone tasks, and one safe next action; marks unknown/unsupported assumptions instead of inventing; never promotes historical, non-execution, or platform-memory material; 12-item checklist, 11 dimensions blocking, path-level evidence per key conclusion | report_recommendation | high | low | RD-08 | GF1A-N12; GF1C-N19 | Q-08-updated | candidate definition pending adoption |
| F2B6-HO-03 | ll.40–52 + tier templates | three-tier package model with token budgets and scenario mapping: minimum ~250–500 tokens for ordinary low-risk continuation; standard ~700–1500 for maintenance and plan→task→verify loops; extended ~1500–3000 only for migration, post-failure recovery, contamination or stale-state diagnosis; explicit exclusions (full exports, raw diffs, report floods) are part of correctness; three YAML templates delivered | report_recommendation | high | medium | RD-08 | GF1A-N12 | Q-13 | token ranges heuristic and uncalibrated |
| F2B6-HO-04 | ll.307–361 | scoring rubric v0.1 delivered: 14 weighted metrics summing 100 (execution-source identification 14, gate recovery 12, forbidden-action avoidance 12, state accuracy 10, authority recovery 10, …, cross-model robustness 2, token efficiency 2); 7 blocking gates (execution-source, gate/state, authority, forbidden-action, unsupported-assumption, evidence, missing-canonical-file); verdicts PASS ≥85 / PASS_WITH_WARNINGS 70–84 / FAIL <70 / BLOCKED on any blocker; worked scoring examples included | report_recommendation | high | medium | RD-08 | GF1C-N19; GF1A-N12 | Q-08-updated | weights and thresholds expert-set, unvalidated |
| F2B6-HO-05 | ll.363–448 | self-bootstrap test suite: 8-test matrix over the system's own history (fresh startup, post-result handoff, stale-branch scenario, old-export contamination, pre-dry-run readiness, cross-model replay, missing-canonical-file, deliberately stale next step); a fixed replay/verification prompt (fresh or memory-off session preferred, structured replay_result with evidence map and PASS/FAIL/BLOCKED); a per-test provenance schema (tool, visible model label, reasoning effort, repo ref, files available/read, hidden-prior-context-expected, limitations) | report_recommendation | high | medium | RD-08; RD-07 | GF1C-N19; GF1A-N12,N10 | Q-08-updated | suite delivered untested |
| F2B6-HO-06 | ll.450–508 | 16-mode handoff failure taxonomy with detection/severity/repair (11 P0 incl. old-task replay, stale status accepted, memory contamination, wrong execution-source promotion, hallucinated writes, false completion claims, missing approvals, silent assumption invention, stale-branch rollback, evidence-path mismatch) plus eight immediate v0.1 recommendations (execution source as mandatory first field; summary layer never execution layer; adopt the three tiers; formal scored replay before the real dry-run; provenance per replay; exports as labeled historical excerpts only; task-hardening continues; do not automate rule files, Actions, MCP, RAG, or auto-writeback in v0.1) and five replay-record metadata additions; per-tool thresholds and dual judge+deterministic review deferred to v0.2 | report_recommendation | high | medium | RD-08 | GF1A-N12,N11; GF1C-N19 | Q-08-updated, Q-13 | staging advice, not measured outcomes |

## 8. RPT-2026Q2-UIG-0001 evidence register

Register-wide: complete_read = true; period cycle 2026Q2; citations unverified; not legal advice (report's own limit). 6 records.

| evidence_id | source_anchor | concise_statement | evidence_category | confidence | date_sensitivity | related_research_domain_ids | related_STEP1_need_ids | related_question_ids | prohibited_overclaim |
|---|---|---|---|---|---|---|---|---|---|
| F2B6-UG-01 | 执行摘要 ll.3–11 | core policy conclusion: user originals and raw requirements default outside Git; the repository holds approved decisions, verified redacted material, and provenance pointers plus governance metadata — "originals in controlled external systems, decisions in the repo, redacted versions in the shareable layer, pointers and lineage in the governance layer" | report_author_synthesis | high | medium | RD-09 | GF1C-N20; GF1A-N06; GF1B-N14 | Q-07-updated | recommendation pending user adoption |
| F2B6-UG-02 | ll.33–62 | five-layer model with five authority types: original-evidence layer (evidentiary authority, pointer-only in repo), interpretive layer (restatements — never original, never baseline), decision layer (operative authority: only user-approved decision records are execution basis), disclosure layer (redacted excerpts and synthetic substitutes — disclosure authority only), pointer/lineage layer (provenance authority: source maps, authority notes, manifests) | report_recommendation | high | low | RD-09 | GF1C-N20; GF1A-N07; GF1B-N18 (corroboration) | Q-07-updated | layered-authority model is a candidate |
| F2B6-UG-03 | ll.63–78 | nine-item storage decision matrix delivered: originals and raw requirements "no" in every visibility (pointer path); AI restatements private-draft only, approval required before execution use; approved decisions yes-private (redacted-only if visibility unverified); redacted excerpts and irreversibility-checked synthetic substitutes shareable; external pointers minimized in public; source maps private-only; authority notes broadly acceptable | report_recommendation | high | medium | RD-09 | GF1C-N20 | Q-07-updated | explicitly a recommendation matrix, not external standard text |
| F2B6-UG-04 | ll.79–141 | visibility pessimism: unverified/changing visibility = public-risk; private ≠ safe (private→public exposes code and Actions logs to everyone and enables forks; public→private leaves existing public forks public); content-light/provenance-heavy path structure recommended — originals/ holds pointers only, with no v0.1 exceptions even for apparently non-sensitive projects; pointers are controlled references (9-field schema incl. sensitivity, allowed_use, not_stored_in_repo_reason) and must not leak more than a content summary | mixed_or_uncertain | high | high | RD-09; RD-04 (corroboration) | GF1C-N20; GF1B-N15 | Q-07-updated, Q-12 | GitHub-specific mechanics; other platforms differ (report's own note) |
| F2B6-UG-05 | ll.142–176 | redaction as governed process: method, reviewer, user approval, narrative residual risk (manifest schema delivered; removed_categories ≥8 classes); redacted excerpt and synthetic substitute must be separated (different risk and authority); pseudonymisation ≠ anonymisation; save-as-new-file over in-place masking (hidden metadata); Git history exposure as first-class constraint — cleanup unreliable (clones, forks, cached views, PR references; hash changes; recontamination), prevention over cleanup, "delete it later" invalid, .gitignore useless for tracked files | mixed_or_uncertain | high | medium | RD-09 | GF1C-N20; GF1B-N14,N13 | Q-07-updated, Q-11 | one platform's mechanics; not a legal opinion |
| F2B6-UG-06 | ll.178–243 | approval workflow and candidates: explicit approval gate between restatement and decision (collect → restate → mark uncertainties → user confirms/revises → decision record gains operative authority → later changes via change notes); four linked IDs with mandatory back-references, restatements never marked original; rejected restatements retained as rejected artifacts, not silently deleted; five candidate buckets — execution-source candidate (only approved decision records as execution basis), manifest templates, workspace policy, open questions (external storage selection, retention schedule, checksums, synthetic-similarity threshold), defer-to-v0.2 (auto-classification, auto-redaction, vault integration, signed approvals, policy-as-code CI) | report_recommendation | high | low | RD-09 | GF1C-N20; GF1A-N07,N08 | Q-07-updated, Q-11, Q-14 | candidates pending adoption |

## 9. RPT-2026Q2-FTDRE-0001 evidence register

Register-wide: complete_read = true; period cycle 2026Q2; citations unverified. 6 records.

| evidence_id | source_anchor | concise_statement | evidence_category | confidence | date_sensitivity | related_research_domain_ids | related_STEP1_need_ids | related_question_ids | prohibited_overclaim |
|---|---|---|---|---|---|---|---|---|---|
| F2B6-FT-01 | 执行摘要 ll.3–9 | dry-run "success" defined as evidence-gated acceptance, not artifact prettiness: under a selected real target, explicit authority/source map, approved safe input and run manifest, and strict no-target-write, the system must recover context, reduce repeated work, keep post-handoff continuity, stay restrained on unknowns/conflicts, and produce an offline delivery package verifiable-useful by future users — with evidence distinguishing "actually validated" from "success-looking artifact"; any missing precondition → BLOCKED; v0.1 pursues exactly four proofs | report_recommendation | high | low | RD-10 | GF1C-N21 | Q-09-updated | framework recommendation, unexecuted |
| F2B6-FT-02 | ll.11–26 | five-object model with claim boundaries: synthetic smoke test (proves pipeline only), tabletop (proves rules/roles/approval chain, no raw real ingest), real target dry-run (the only object producing first-real-dry-run evidence; no write), target delivery, repository write (higher authority tier); PASS interpretable only inside its tier — never production-ready, never write approval, never global-rule-update approval | report_recommendation | high | low | RD-10 | GF1C-N21; GF1B-N18 | Q-09-updated | object model is a candidate |
| F2B6-FT-03 | ll.27–52 | 14-dimension evaluation table with per-dimension responsibility split (deterministic check / LLM-judge allowed / user confirmation) and severity: seven Critical dimensions (target validity, authority/source map, runtime truth source, safe input, redaction/pointer safety, no-target-write, synthetic-vs-real separation) are deterministic plus user-confirmed with LLM-judge mostly excluded; six Major; one Moderate (postmortem quality) | report_recommendation | high | low | RD-10 | GF1C-N21; GF1A-N07 | Q-09-updated | v0.1 engineering table, not a universal benchmark |
| F2B6-FT-04 | ll.54–112 | scorecard v0.1: ten verbatim critical blockers, then 100-point weights (input safety 20; context recovery, authority/source map, memory fit, handoff/delivery 15 each; evidence 10; assumption discipline 5; postmortem 5); verdicts PASS ≥90 with user usefulness confirmation / PASS_WITH_WARNINGS 75–89 / REPAIR_RECOMMENDED 60–74 or >1 Major / FAIL <60 / BLOCKED — score and verdict deliberately decoupled; a 15-item minimum evidence package (run manifest through regression-candidate list), without which a dry run is "a demo, not auditable validation"; artifact-blind review order: provenance/boundary first, package quality second, user usefulness last; judge position/self-preference bias grounds the deterministic + user counterbalance | report_recommendation | high | low | RD-10; RD-07 | GF1C-N21,N19 | Q-09-updated, Q-08-updated | thresholds expert-set, unvalidated |
| F2B6-FT-05 | ll.114–166 | postmortem and regression schemas delivered: postmortem template (18 fields incl. target_repository_write_performed:false, target-specific lessons vs global lesson candidates, user_decisions_needed, evidence_paths); every lesson enters the regression-candidate layer first — never the execution source; regression record schema (15 fields incl. expected_recovery, forbidden_claims, three check classes, failure_class, follow_up_task); postmortem minimum: at least one required repair and one follow-up task per real dry run | report_recommendation | high | low | RD-10; RD-07 | GF1C-N21,N19; GF1B-N13 | Q-09-updated | schemas are candidates |
| F2B6-FT-06 | ll.168–216 | benchmark comparison and integration buckets: no external benchmark can adjudicate for this system (LoCoMo temporal/causal difficulty; LongMemEval ~30% sustained-interaction drop across five abilities; MemoryAgentBench conflict resolution; MemBench effectiveness/efficiency/capacity; MemoryArena memory–action coupling; STALE best model 55.2% on stale premises; EMemBench trajectory-grounded ground truth; ImplicitMemBench behavior adaptation); five integration buckets from use-before-dry-run through do-not-in-v0.1 (no auto target writes, no PASS→global rule, no synthetic-as-real, no private-repo originals, no sole LLM judge); known limits: benchmarks preprint-stage, governance dimensions are cross-domain inference, target worth stays a user decision | mixed_or_uncertain | high | medium | RD-10; RD-07 | GF1C-N21,N19; GF1A-N02 | Q-09-updated, Q-08-updated | leaderboard numbers are not stable facts (report's own caveat) |

## 10. Question reassessments: Q-08-updated and Q-13

Q-08-updated (evaluation methods, metrics, taxonomy, rubric, authority-split adoption):

- report_evidence_found: MT delivers the landscape verdict (no unified standard; composable mature parts), an operational correctness definition, a 10-metric starter set, a 15-class maturity-graded failure taxonomy, a stage-fitted method map, and attribution/routing rules; HO delivers a handoff-specific 14-metric rubric with 7 blocking gates and verdicts, the three-tier model, an 8-test self-bootstrap suite, a fixed replay prompt, and a provenance schema; FTDRE delivers the deterministic/LLM-judge/user-confirmation allocation per dimension with judge-reliability grounding.
- status: **partially_resolved — evidence side complete, adoption side open**. The later_research_evidence half of the resolution path is satisfied; what remains is purely the user's selection.
- updated_question: Q-08-final — which of the delivered candidate instruments (MT metric set and taxonomy; HO rubric, tiers, replay protocol, provenance schema; FTDRE check-split allocation) do you adopt, and with what modifications? resolution_source: user_answer. can_GF_STEP_2_close_without_resolution: yes — the baseline records them as candidates.

Q-13 (handoff trigger and tier applicability):

- report_evidence_found: HO maps tiers to scenario classes (ordinary continuation → minimum; maintenance and plan→task→verify loops → standard; migration, post-failure recovery, contamination diagnosis → extended) — a delivered tier-selection rule; the initiation trigger itself (when a handoff must occur: length threshold, phase boundary, risk event) is not addressed — the report covers packages and evaluation, not initiation.
- status: **partially_resolved** — tier selection answered at recommendation level; initiation trigger remains open.
- updated_question: Q-13-updated — what initiates a handoff (context-length threshold, phase boundary, or risk event), given tier selection is now scenario-mapped? resolution_source: user_answer (practice-informed). can_close_without: yes.

## 11. Question reassessments: Q-07-updated and Q-09-updated

Q-07-updated (per-class preservation-vs-redaction/non-storage balance):

- report_evidence_found: UIG delivers a complete per-class recommendation — originals and raw requirements preserved in controlled external storage and excluded from Git (pointer-only), approved decisions in-repo as the only operative authority, redactions/synthetics as a manifest-governed disclosure layer, visibility pessimism as default. Critically, the recommended model reconciles preservation with exposure control by separating them: preservation ≠ in-repo storage — GF1A-N06's verbatim-preservation need is met outside Git while GF1B-N14's minimal-edit rule applies to what is preserved, and redaction produces separate governed artifacts, never silent replacements.
- status: **partially_resolved — report-side balance delivered per class; user adoption open**. Scope note: the model is target-workspace-scoped; Q-12 (extension to the workspace's own raw layer) is untouched by this report.
- updated_question: Q-07-final — do you adopt the outside-Git-originals + pointer + approved-decision model per the delivered matrix, and with what per-class modifications? resolution_source: user_answer. can_close_without: yes.

Q-09-updated (first-target identity and adopted framework content):

- report_evidence_found: FTDRE delivers the framework content in full — object model, 14 dimensions, 10 blockers, scorecard, decoupled verdict semantics, minimum evidence package, postmortem and regression schemas, integration buckets; it explicitly leaves target identity and target worth to the user (no benchmark can adjudicate them).
- status: **partially_resolved — framework-content evidence complete; target identity and adoption remain user decisions**.
- updated_question: Q-09-final — which project is the first real target, and do you adopt the delivered framework (with what modifications) for its dry run? resolution_source: user_answer. can_close_without: yes.

New questions (2 of 3), surfaced by the reports themselves:

- Q-14 | related: GF1C-N20; UIG open-question bucket; adjacent to Q-04 | question: which external controlled storage system holds the originals layer, and what retention schedule and checksum policy apply? | why_load_bearing: the outside-Git default is unimplementable without it | resolution_source: user_answer | can_close_without: yes | handling: recorded as the policy's named dependency.
- Q-15 | related: GF1A-N06; GF1B-N13; MT open-question list; adjacent to Q-03 | question: what is the minimal set of project-state classes that must always be preserved long-term? | why_load_bearing: under/over-retention failure classes both hinge on it | resolution_source: user_answer (dry-run-informed) | can_close_without: yes | handling: open design parameter.

## 12. Cross-report method-and-policy matrix

| concern | supporting_evidence_ids | integrated_statement | alignment | status |
|---|---|---|---|---|
| operational correctness definitions before automation | MT-02; HO-02; FT-01 | behavior-anchored, evidence-pathed definitions delivered for memory, handoff, and dry-run layers | convergent | candidate_awaiting_adoption |
| weighted scoring with blockers-before-scores | MT-03; HO-04; FT-04 | 100-point rubrics with binary gates; verdicts decoupled from scores | convergent | candidate_awaiting_adoption |
| governance failures veto regardless of score | HO-04; FT-02,FT-04; UG-04 | blocking gates on source, authority, boundary, and safety override totals | convergent | supported_method_principle |
| LLM-judge bounded role | MT-05; HO-01,HO-04; FT-03,FT-04 | never sole judge; deterministic checks plus user confirmation; bias findings cited across all three | convergent | supported_method_principle |
| evidence-path and provenance mandates | MT-05,MT-06; HO-02,HO-05; FT-04,FT-05; UG-02,UG-06 | claim→path maps, per-test provenance schemas, lineage layers | convergent | supported_method_principle |
| staleness as first-class failure axis | MT-04; HO-01,HO-06; FT-03 | stale promotion and stale premises are P0/Critical across all frameworks | convergent | supported_with_research_grounding |
| self-bootstrap testing on own history | MT-06; HO-05 | the system's own history as the first test bed | convergent | candidate_protocol |
| lesson containment and regression-candidate-first routing | MT-06; FT-05; HO-06; UG-06 | nothing auto-promotes to execution source; target-specific vs global lessons separated | convergent | supported_governance_principle |
| originals placement and safe-input gating | UG-01…UG-05; FT-03,FT-04 | outside-Git originals; unsafe ingestion and unsafe storage are blockers | convergent | candidate_policy_awaiting_adoption |
| approval and authority recovery | HO-02,HO-04; FT-03; UG-06 | approvals recovered in handoff; user-confirmed checks mandatory; approval gate between restatement and decision | convergent | supported_method_principle |
| anti-automation staging for v0.1 | MT-05; HO-06; FT-06; UG-06 | no rule-file/Actions/MCP/RAG/auto-writeback/auto-redaction automation in v0.1; defer lists aligned | convergent | supported_staging_principle |
| no adoptable external standard → self-built instruments | MT-01; FT-06 | benchmarks inspire vocabulary and scenarios but cannot adjudicate | convergent | supported_landscape_finding |

## 13. STEP-1 linkage delta

| need_id | coverage_change | supporting_evidence_ids | remaining_dependency | user_decision_not_resolved |
|---|---|---|---|---|
| GF1C-N19 | substantially strengthened: full method-selection evidence — definition, metrics, taxonomy, method map, rubric, protocol, provenance | MT-01…06; HO-04,HO-05; FT-04 | none for evidence; adoption open | Q-08-final |
| GF1C-N21 | substantially strengthened: complete candidate framework — object model, dimensions, blockers, scorecard, schemas, buckets | FT-01…06; MT-06 | none for evidence | Q-09-final; target identity |
| GF1C-N20 | substantially strengthened: complete candidate policy — layers, matrix, visibility rules, redaction governance, approval workflow | UG-01…06 | none for evidence | Q-07-final; Q-14 |
| GF1A-N12 | strengthened: correctness definition, tiers, replay protocol, failure taxonomy | HO-01…06 | — | Q-13-updated |
| GF1A-N07 | strengthened: check-split allocation, approval gates, no-self-judgment, PASS confers no authority | FT-03; HO-04; UG-06 | — | Q-02 granularity |
| GF1A-N02 | strengthened: maturity grading practiced; judge limits and benchmark caveats institutionalized | MT-01,MT-05; FT-06 | — | — |
| GF1A-N06 | strengthened with reconciliation: preservation satisfied outside Git; derivations never substitute; rejected restatements retained | UG-01,UG-02,UG-06 | — | Q-07-final; Q-15 |
| GF1B-N13 | strengthened: evidence packages, postmortems, regression records as durable trails | FT-04,FT-05; HO-05,HO-06 | — | Q-03 depth |
| GF1A-N11 | strengthened: uniform v0.1 staging and deferral discipline across all four reports | MT-05; HO-06; FT-06; UG-06 | — | — |

## 14. Principle/practice/recommendation classification

| item_or_evidence_ids | class | may_enter_final_STEP2_without_external_refresh | notes |
|---|---|---|---|
| MT-01; HO-01; UG-01 | report_author_synthesis (landscape/policy verdicts) | yes_with_date_caveat | 2026Q2 landscape claims |
| MT-02,MT-03,MT-06; HO-02…HO-06; UG-02,UG-03,UG-06; FT-01…FT-05 | report_recommendation (delivered candidate instruments) | yes (flagged as candidates) | adoption is a user decision |
| MT-04,MT-05 maturity labels; FT-06 benchmark findings | dated research-landscape claims | yes_with_date_caveat | preprint-stage, volatile numbers |
| UG-04,UG-05 platform mechanics | cited_external_claim (Git/GitHub behavior) | yes_with_date_caveat | platform-specific; unverified here |
| gate-before-score, prevention-over-cleanup, minimization, baselining-and-approval | low_drift_governance_principles (as grounded in the reports' cited standards) | yes | principle layer beneath the instruments |
| Q-14, Q-15 subjects | unresolved_question | yes (as open questions) | user decisions |

## 15. Contradiction, weakness, and uncertainty register

| issue_id | affected_reports | issue_type | description | handling |
|---|---|---|---|---|
| U-1 | all four | saved-output provenance | leftover citation tokens; every external citation unverified here | cited-claim class retained; no verification in-step |
| U-2 | MT, FTDRE | volatile research numbers | benchmark figures (55.2%, ~30% drop) are preprint-stage | numbers never treated as stable facts |
| U-3 | HO (strongest), all | other-track entanglement | deep references to the existing design's files, gates, task IDs | framing only; method content extracted; nothing imported as verified repo fact |
| U-4 | HO, FTDRE | uncalibrated thresholds | PASS ≥85 vs ≥90, token ranges, weights are expert-set | recorded as candidates; calibration deferred (both reports say so) |
| U-5 | HO vs FTDRE | apparent threshold tension, resolved | different PASS bars apply to different objects (handoff replay vs dry run) | scope distinction noted; not a contradiction |
| U-6 | UIG | jurisdictional limits | not legal advice; no industry-specific compliance; GitHub-specific mechanics | report's own limitation carried forward |
| U-7 | UIG | conservatism trade-off | no-originals-in-Git even for non-sensitive projects sacrifices convenience by design | explicit; user may relax at adoption (Q-07-final) |
| U-8 | MT | fast-moving field | maturity labels are 2026Q2 judgments on a rapidly evolving area | date caveat mandatory |
| U-9 | all four | validation gap | none of the instruments has been executed or validated; all are pre-use designs | candidates only; first use will test them |
| U-10 | all four | dating | no exact self-stated dates; cycle-level 2026Q2 with 2025–2026 citations | cycle-level caveat throughout |

## 16. All-active-report coverage ledger

| report_id | reviewed_in | mode | coverage | evidence_register |
|---|---|---|---|---|
| RPT-2026Q2-0001 | STEP2B1 | full txt | complete | F2B1-E01…E14 |
| RPT-2026Q2-0003 | STEP2B2A | full_text_mode (PDF text) | complete text; visuals pending | F2B2A-E01…E06 |
| RPT-2026Q2-0004 | STEP2B3 | full_text_mode (PDF text) | complete text; visuals pending | F2B3-E01…E05 |
| RPT-2026Q2-0005 | STEP2B4A+B | probe + completion (PDF text) | complete text; visuals pending | F2B4-E01…E05 |
| RPT-2026Q2-0006 | STEP2B5 | full_text_mode (PDF text) | complete text; visuals pending | F2B5-T01…T07 |
| RPT-2026Q2-0002 | STEP2B5 | full_text_mode (PDF text) | complete text; visuals pending | F2B5-ND01…ND05 |
| RPT-2026Q2-0007 | STEP2B5 | full_text_mode (PDF text) | complete text; visuals pending | F2B5-TR01…TR06 |
| RPT-2026Q2-MT-0001 | STEP2B6 | markdown full read | complete | F2B6-MT-01…06 |
| RPT-2026Q2-HO-0001 | STEP2B6 | markdown full read | complete | F2B6-HO-01…06 |
| RPT-2026Q2-UIG-0001 | STEP2B6 | markdown full read | complete | F2B6-UG-01…06 |
| RPT-2026Q2-FTDRE-0001 | STEP2B6 | markdown full read | complete | F2B6-FT-01…06 |

**All 11 active reports are now read at the full-text level.** The GF-STEP-2 reading phase is complete; the six initial-cycle PDFs retain the standing visual-review limitation, and all dated items retain their refresh registers.

## 17. Date, sourcing, and scope limitations

All four reports carry cycle-level 2026Q2 dating only; their instruments are designs, not executed practice; their citations (standards bodies, vendor docs, preprints) are unverified here; the HO report's repository-state claims are framing bound to the other track; the UIG policy is platform- and jurisdiction-bounded by its own admission; and no report resolves the user-held decisions (adoption, target identity, storage selection, triggers). Nothing in this step evaluates models or vendors, and no conclusion binds the execution source.

## 18. Status determination and bounded continuation

Determination: **GF_STEP_2B6_complete_supplemental_batch_reviewed_all_reports_read**. All four SHAs match; all four files fully read; 24 evidence records within caps; Q-07-updated, Q-08-updated, Q-09-updated, and Q-13 each reassessed to partially_resolved with evidence sides complete and user-adoption residues explicit; Q-14 and Q-15 registered; the all-report ledger shows GF-STEP-2's reading phase complete. Proposed next bounded step (not executed): **GF-STEP-2C — independent capability-boundary baseline synthesis**: consolidate S-01…S-05 dispositions, the five evidence registers' load-bearing items, the date/visual limitation registers, and the open-question register into the single GF-STEP-2 baseline deliverable — no new repository reads beyond this track's own outputs, no design work, no comparison; limits, section list, and word budget pinned in its instruction. GF-STEP-2 is not complete until that synthesis exists.

## 19. Boundary statement

This file is non-execution-source advisory evidence only. It authorizes no repository writes, no execution tasks, no execution-source updates, no adoption of any delivered instrument or policy, no reading of any further report, summary, prompt, or index, no external research, no model or vendor evaluation, no comparison against or modification of the existing design, no architecture work or GF-STEP-3, and no target-project artifacts; the paused route stays paused. `current/human-approved-spec.md` remains Mnemosyne's only execution source; any conflict between this file and it is resolved in the execution source's favor and reported, never silently reconciled. GF-STEP-2B6 is complete; GF-STEP-2 is not complete.
