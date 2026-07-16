# FABLE5-GREENFIELD-001 — GF-STEP-2C Independent Capability-Boundary Baseline

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2C
step_name: independent_capability_boundary_baseline
record_type: capability_boundary_baseline_synthesis
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-2B6
GF_STEP_1_status: complete_with_explicit_open_questions
research_mode: false
date: 2026-07-16
synthesis_inputs: this track's own deliverables only (STEP1A–STEP1E need model; STEP2A source map; STEP2B1–STEP2B6 evidence registers)
new_repository_reads: none
retrieval_batteries_used: 0
step_status: GF_STEP_2_complete_capability_boundary_baseline_established
```

## 2. Scope and hard limits

Synthesis substep closing GF-STEP-2: consolidate the five signal dispositions, the load-bearing evidence of all six reading substeps, and the limitation registers into one independent capability-boundary baseline for the STEP-1 need model. Limits observed: repository paths 0; retrieval batteries 0; no report, prompt, summary, index, or web reads; no model/vendor evaluation; no design, architecture, comparison, or repair work; no instrument adoption; Research mode off; no automatic continuation into GF-STEP-3.

## 3. Allowed sources and anti-contamination policy

Inputs are exactly this track's own thirteen deliverables (verified present on disk before synthesis; no external source touched). Every statement below is traceable to a prior register ID; nothing new is asserted about tools, platforms, or reports beyond what those registers already carry. Other-track design state referenced inside sources remains framing, never imported. Prior-exposure disclosure carries forward: independence by derivation and disclosure. Q-10's residue stands: the seven initial-cycle prompt originals remain unread (their reports were read; the prompts stay excluded under the anti-expansion rule).

## 4. Synthesis inputs and integrity note

Need model: GF1A-N01…N12 (N12 delta), GF1B-N13…N18, GF1C-N19…N21 — closed in STEP1E with explicit open questions. Evidence layer: F2B1-E01…E14 (foundational txt report); F2B2A-E01…E06 (plain-dialogue PDF text); F2B3-E01…E05 (local workflows PDF text); F2B4-E01…E05 (hosted workflows PDF text, superseding F2B4A-P01…P03); F2B5-T01…T07, ND01…ND05, TR01…TR06 (theory, non-development practice, transfer); F2B6-MT/HO/UG/FT-01…06 (method and policy instruments). All 11 active reports read at full-text level; all source SHAs matched at read time; the six initial-cycle PDFs carry the standing visual-review limitation.

## 5. Evidence-class and grading rules

Classes used below: low_drift_engineering_principle; dated_product_or_workflow_observation (period cycle 2026Q2 unless a report stated a date — only RPT-0001 did: 2026-05-23); cited_external_claim_not_independently_checked; report_author_synthesis; report_recommendation (candidate instruments, never capability facts); analogy_or_transfer_hypothesis; unresolved_question. Grading rules: every dated observation keeps its surface scope and refresh register; every absence claim is survey-bounded; recommendations never upgrade to facts; nothing here is validated by execution; text_only flags persist for PDF-derived items; no statement binds the execution source.

## 6. Final signal dispositions S-01…S-05

- **S-01** (disposition chain: STEP2B1 report_confirmed → STEP2B5 batch_reports_refine). Final wording: externalized, versioned records can carry durable state across sessions and surfaces, grounded in low-drift arguments (bounded context windows with quadratic cost and positional degradation; retrieval-on-demand; immutable event logs with projections; hierarchical memory tiers) and early framework and community practice; platform-provided memory stays auxiliary, high-level, and only partially portable; externalization alone guarantees nothing — retrieval relevance, structured state, reconciliation, human maintenance, privacy/retention governance, and per-scenario adaptation remain required. Evidence: F2B1-E01,E07,E11,E14; F2B5-T01…T06, ND01…ND04, TR01/03/04. Guards: never "long context is useless" or "platform memory is useless"; theory + early practice ≠ turnkey reliability.
- **S-02** (STEP2B1 report_refined → STEP2B2A dedicated_report_refines). Final wording: on plain ChatGPT and Claude dialogue surfaces (2026Q2; RPT-0001 layer dated 2026-05-23), repository/file write-back is not native — the official GitHub connector is read-only without exact-filename search; Claude connectors offer no GitHub write path and Google-ecosystem writes are per-action user-confirmed; Agent/Apps writes are admin/config-gated and per-action confirmed; Tasks cannot write externally; automated write-back requires external API/MCP/scripts/Actions. Evidence: F2B1-E02…E05; F2B2A-E01…E05. Guards: never "chat can never write files"; volatile — refresh register D-01.
- **S-03** (STEP2B1 report_confirmed → STEP2B2A dedicated_report_confirms). Final wording: platform-provided memory is auxiliary, high-level, partially controllable, and not an auditable, migratable, rollbackable project truth source; Projects-type containers are bounded (file limits, context-window bounds, no cross-project auto-sync). Evidence: F2B1-E05,E08,E14; F2B2A-E01,E03,E04,E06; F2B5-ND02. Guards: "auxiliary" ≠ "useless"; refresh D-01/D-04.
- **S-04** (STEP2B3 dedicated_report_refines). Final wording: on local development agents (2026Q2; Codex CLI, Claude Code, Cursor), file access and layered instruction loading are prerequisites, not reliable memory — instruction files are best-effort context while enforcement lives only in client-side permission/sandbox configuration; built-in memories are machine-local and non-synced; memory semantics are user convention; sessions resume but conversation history does not auto-carry; reliable continuity additionally requires a Git-versioned source of truth, patch/diff review before commit, human-confirmed memory updates, protected paths, conflict-free short layered rules, and explicit handoff/state recovery. Evidence: F2B3-E01…E05. Guards: never "local agents provide reliable memory automatically"; refresh D-02.
- **S-05** (STEP2B4A provisional present → STEP2B4B dedicated_report_refines). Final wording: on the Copilot-cloud-agent + GitHub surface (2026Q2), write-back is PR-mediated with platform-enforceable, opt-in review gates (no self-merge, CODEOWNERS, protected branches, status checks) and full log/artifact trails — verification rests on observable repository evidence rather than agent claims; trails establish traceability, never semantic correctness; default tokens are current-repo-scoped (MCP read-only), cross-repo writes need elevated credentials; Copilot content-exclusion does not bind the agent, so sensitive material requires placement outside the agent's reach. Evidence: F2B4-E01…E05. Guards: never "hosted write-back is audited by default"; the claim-vs-diff divergence premise rests on the foundational layer, not this report; refresh D-03.

## 7. Capability-boundary baseline: conversation surfaces (RD-01)

| boundary_id | statement | evidence_class | supporting_ids | surface_scope | date_or_refresh_caveat | overclaim_guard |
|---|---|---|---|---|---|---|
| CB-01 | automated external persistent memory in pure dialogue entry is very limited: no background cross-session read/write of external storage | cited_external_claim + synthesis | F2B2A-E01; F2B1-E02 | ChatGPT + Claude web/app | 2026Q2; D-01 | limited ≠ impossible with tooling |
| CB-02 | official GitHub connector reads/searches only (repo-level, no exact-filename query); write-back unsupported | cited_external_claim | F2B1-E03; F2B2A-E02 | ChatGPT + GitHub connector | 2026-05-23 / 2026Q2; D-01 | one connector snapshot |
| CB-03 | connector/Agent/Apps write actions exist but are admin/config-gated and per-action user-confirmed; Tasks cannot upload or write externally | cited_external_claim | F2B1-E04; F2B2A-E03 | ChatGPT surface | 2026Q2; D-01 | conditional writes ≠ assumable defaults |
| CB-04 | Claude connectors: GitHub read-side with manual sync; no documented auto file-write or push; Google-ecosystem writes per-action confirmed; chat UI lacks Claude Code's auto memory | cited_external_claim | F2B1-E05; F2B2A-E04 | Claude surface | 2026Q2; D-01 | absence of documented feature ≠ impossibility |
| CB-05 | platform memory stores high-level information with partial user control and limited portability; Projects are bounded project-scoped containers | cited_external_claim | F2B2A-E01,E03,E04; F2B5-ND02 | major-vendor surfaces | 2026Q2; D-01/D-04 | auxiliary ≠ useless |
| CB-06 | reliable dialogue-surface continuity is user-mediated: handoff cards, uploaded packages, project hubs, pasted structured memory, external storage intermediaries | report_recommendation + practice | F2B2A-E05,E06; F2B1-E08 | dialogue surfaces | low drift as workflow | recommendation ≠ measured effectiveness |

## 8. Capability-boundary baseline: local and hosted project workflows (RD-03, RD-04)

| boundary_id | statement | evidence_class | supporting_ids | surface_scope | date_or_refresh_caveat | overclaim_guard |
|---|---|---|---|---|---|---|
| CB-07 | local agents load layered instruction files at startup (global→project merge; imports; subdirectory scoping) and can patch any file with local Git commits and diff review | cited_external_claim | F2B3-E01,E02 | Codex CLI, Claude Code, Cursor | 2026Q2; D-02 | loading ≠ compliance |
| CB-08 | instruction files are best-effort context; enforcement exists only in client-side permissions/sandbox | cited_external_claim | F2B3-E03,E06(F2B1) | local agents | 2026Q2; D-02 | rule file ≠ guarantee |
| CB-09 | built-in agent memories (auto memory, Notepads) are machine-local, non-synced, quality-unreviewed; which files count as memory is user convention | cited_external_claim | F2B3-E02,E03,E04 | local agents | 2026Q2; D-02 | local ≠ portable memory |
| CB-10 | sessions resume locally but conversation history does not auto-carry; a new session gets rules plus a memory summary only | cited_external_claim | F2B3-E03 | Claude Code (named) | 2026Q2; D-02 | one product's mechanics |
| CB-11 | local risks are concrete: mis-edits under loose auto-approval, rule conflicts, memory rot, over-broad permissions — mitigated by Git-managed rules, diff review, human-confirmed updates, protected paths | synthesis + recommendation | F2B3-E05 | local agents | pattern durable | recommendations ≠ failure statistics |
| CB-12 | hosted write-back is PR-mediated with opt-in enforceable gates (no self-merge, CODEOWNERS, protected branches, status checks) and full log/artifact trails | synthesis + cited claims | F2B4-E01,E02 | Copilot agent + GitHub | 2026Q2; D-03 | gates are configuration, not defaults |
| CB-13 | verification rests on observable repository evidence (branch, commit, diff, PR, review, checks, logs, artifacts, merge), never on agent claims; trails prove events, not correctness | synthesis | F2B4-E02; F2B1-E10 | hosted workflows | low drift as principle | audit ≠ semantic verification |
| CB-14 | token scoping splits placement options: same-repo default token read/write vs separate memory repo needing elevated credentials (default MCP token read-only); both placements are unresolved tradeoffs | cited_external_claim | F2B4-E03 | GitHub workflows | 2026Q2; D-03 | no placement is endorsed universal |
| CB-15 | Copilot content-exclusion does not bind the cloud agent — excluded files stay visible and modifiable; sensitive material must live outside the agent's reach entirely | cited_external_claim | F2B4-E04 | Copilot agent | 2026Q2; D-03 | one product's documented behavior |
| CB-16 | Actions can automate validation, artifact archiving, and scripted commits, while the PR human-confirmation step is retained by practice | mixed | F2B4-E05 | GitHub Actions | 2026Q2; D-03 | automatable ≠ recommended unattended |

## 9. Capability-boundary baseline: engineering basis and overall feasibility (RD-05, RD-11)

| boundary_id | statement | evidence_class | supporting_ids | surface_scope | date_or_refresh_caveat | overclaim_guard |
|---|---|---|---|---|---|---|
| CB-17 | the externalized-memory pattern (rules/state/tasks/handoff/raw/eval in versioned files, model reads, reviewed write-back) is engineering-feasible and variously validated as a cross-tool workflow/governance architecture — not a native chat feature | report_author_synthesis | F2B1-E01; F2B5-T01 | cross-surface | principle low-drift; instances dated | feasible pattern ≠ equal automation everywhere |
| CB-18 | long context cannot substitute external memory: quadratic cost, positional degradation, latency, no cross-session persistence via the window | cited research | F2B1-E14; F2B5-T02 | model architecture | low drift | never "long context is useless" |
| CB-19 | on-demand retrieval over full-history loading is the supported read-path principle; retrieval quality is a separate, unguaranteed property | cited research | F2B1-E07; F2B5-T03; F2B5-TR04 | cross-surface | low drift | availability ≠ relevance |
| CB-20 | immutable event logs with projections support rebuild and audit; snapshots equal compaction; full archiving trades replay/compliance value against privacy/legal exposure | mixed | F2B5-T06 | engineering principle + legal environment | principle low-drift; legal dated | one legal case ≠ settled law |
| CB-21 | Git/GitHub is the strongest-evidenced audit substrate; audits cover file change, not memory quality — human review, citations, sensitive-info scanning still needed | low_drift_engineering_principle | F2B1-E10 | hosted repositories | low drift | Git audit ⇒ traceability only |
| CB-22 | a model-agnostic external core (Markdown/Git/refs/index) with short per-tool adapters is the supported portability route; hierarchical-memory frameworks remain exploratory; platform memories and rule syntaxes need adapters | mixed | F2B1-E11; F2B5-T05; F2B3-E04 | cross-surface | adapter specifics dated | no cross-tool auto-sync exists |

## 10. Capability-boundary baseline: non-development scenarios and transfer (RD-02, RD-06)

| boundary_id | statement | evidence_class | supporting_ids | surface_scope | date_or_refresh_caveat | overclaim_guard |
|---|---|---|---|---|---|---|
| CB-23 | non-development persistent-memory practice is emerging but immature: platform containers plus education deployments exist; ordinary users still maintain manually; no unified automated external persistence | report_author_synthesis | F2B5-ND01…ND04 | non-development landscape | 2026Q2 | "immature" is dated |
| CB-24 | only high-level information persists systematically; free-chat detail memory and standardized cross-topic handoff lack solutions in the surveyed landscape | synthesis (absence, survey-bounded) | F2B5-ND05 | ordinary dialogue | 2026Q2 | absence-in-survey bounded |
| CB-25 | structured-record formats transfer as formats (state docs, decision records, task lists, ledgers, handoff cards, archives); content schemas must be rebuilt per scenario | analogy_or_transfer_hypothesis | F2B5-TR01,TR02 | dev → non-dev | hypothesis | format ≠ workflow transfer |
| CB-26 | heavyweight development toolchains (branching, PR review, CI gates, enforced merges) are judged non-transferable to learning/dialogue scenarios — substrate weight is scenario-dependent | report_author_synthesis | F2B5-TR03 | non-dev targets | scenario-scoped | not a claim about dev-like targets |
| CB-27 | no surveyed work proposes a memory-design meta-agent; per-scenario schema design is manual today — the meta-agent goal is novel, not invalidated | report_direct_finding (absence) | F2B5-TR06 | meta-level | 2026Q2 survey | absence ≠ nonexistence |

## 11. Method and policy instrument inventory (RD-07…RD-10)

Delivered candidate instruments — commissioned evidence awaiting user adoption; never capability facts:

| instrument | source_register | adoption_question |
|---|---|---|
| operational "working correctly" definition; 10-metric starter set; 15-class maturity-graded failure taxonomy; stage-fitted method map; attribution/routing rules | F2B6-MT-02…06 | Q-08-final |
| operational correct-handoff definition; three-tier package model with templates and token ranges; 14-metric rubric with 7 blocking gates and verdicts; 8-test self-bootstrap suite; fixed replay prompt; per-test provenance schema; 16-mode failure taxonomy; v0.1 recommendations and deferrals | F2B6-HO-02…06 | Q-08-final, Q-13-updated |
| five-layer input-governance model with five authority types; nine-item storage decision matrix; visibility-pessimism rule; pointer and redaction-manifest schemas; approval workflow with linked IDs and rejected-artifact retention; five candidate buckets | F2B6-UG-01…06 | Q-07-final, Q-11, Q-14 |
| five-object dry-run model with claim boundaries; 14 evaluation dimensions with deterministic/LLM-judge/user-confirmation split; ten critical blockers; decoupled scorecard and verdicts; minimum evidence package; postmortem and regression schemas; integration buckets | F2B6-FT-01…06 | Q-09-final |
| cross-report convergences: gates-before-scores, LLM-judge never sole, evidence-path mandates, staleness first-class, lesson containment, anti-automation v0.1 staging | STEP2B6 §12 matrix | — (method principles) |

## 12. STEP-1 need coverage closure table

| need_id | final_evidence_coverage | key_supporting_registers | open_decision |
|---|---|---|---|
| GF1A-N01 | covered_at_baseline_level | CB-01…06,17…19,23 | — |
| GF1A-N02 | covered: per-surface dated boundaries + maturity-grading practice | CB-02…04,08,15; F2B6-MT-05 | — |
| GF1A-N03 | covered: scenario differences, adaptation map, meta-agent novelty | CB-23…27 | scenario priorities |
| GF1A-N04 | covered_at_principle_level: routing/refresh/delta practice | F2B6-MT-06; STEP2A D-registers | — |
| GF1A-N05 | user_decision_not_research_fact | — | Q-01 |
| GF1A-N06 | covered with reconciliation: preservation outside Git; derivations never substitute | F2B6-UG-01,02,06; CB-20 | Q-03, Q-07-final, Q-15 |
| GF1A-N07 | covered: enforceable review gates, check-split, approval workflows | CB-12,13,16; F2B6-FT-03; F2B6-UG-06 | Q-02 |
| GF1A-N08 | partially covered: change notes + rejected-artifact retention as correction path | F2B6-UG-06 | Q-02, Q-11 |
| GF1A-N09 | covered: architectural grounding + surface facts | CB-17…20; CB-05,09 | — |
| GF1A-N10 | covered: model-agnostic core + adapters; partial import/export | CB-22; F2B5-ND02 | Q-03 |
| GF1A-N11 | covered: staged, reviewed, anti-automation discipline across all instruments | CB-11,16; STEP2B6 §12 | — |
| GF1A-N12 | covered at method level: definition, tiers, protocol, taxonomy | F2B6-HO-01…06; CB-06,10 | Q-13-updated |
| GF1B-N13 | covered: trails, packages, postmortems, regression records | CB-13,20,21; F2B6-FT-05 | Q-03 |
| GF1B-N14 | covered: redaction as separate governed artifacts, never silent replacement | F2B6-UG-05 | Q-07-final |
| GF1B-N15 | covered: substrate mechanics, placements, token scopes, scenario-dependent weight | CB-07,12,14,21,26 | Q-04, Q-14 |
| GF1B-N16 | thinly covered: capture remains manual in surveyed practice | CB-24; F2B5-ND02 | Q-05 |
| GF1B-N17 | user_decision_not_research_fact | — | Q-06 |
| GF1B-N18 | covered: precedence and containment reaffirmed by every instrument | F2B6-FT-02; STEP2B6 §12 | — |
| GF1C-N19 | covered at instrument level | F2B6-MT-01…06; F2B6-HO-04,05 | Q-08-final |
| GF1C-N20 | covered at policy-candidate level | F2B6-UG-01…06; CB-15,20 | Q-07-final, Q-11, Q-12, Q-14 |
| GF1C-N21 | covered at framework-candidate level | F2B6-FT-01…06 | Q-09-final; target identity |

## 13. Open-question register final state

Carried, user-held: Q-01 (placement acceptance), Q-02 (approval granularity), Q-03 (raw/digest sufficiency and retention depth), Q-04 (substrate hard requirements vs GitHub), Q-05 (buffer activation), Q-06 (language-migration trigger). Evidence-completed, adoption open: Q-07-final, Q-08-final, Q-09-final (per STEP2B6). Q-10: second tier resolved; initial-cycle prompt originals remain a low-priority non-blocking note. Q-11 (correction/deletion vs history immutability): partial report input (change notes, rejected-artifact retention, prevention-first history rule); user decision open. Q-12 (governance scope extension to the workspace's own raw layer): untouched by evidence; open. Q-13-updated (initiation trigger): open. Q-14 (external storage + retention for originals layer): open. Q-15 (minimal must-preserve state-class set): open. Total: 15 registered questions, none blocking baseline validity; all blocking only adoption and design steps downstream.

## 14. Date-sensitivity and refresh register (carried forward)

STEP2A items D-01…D-09 stand unchanged: use_with_date_note for platform chat/memory features (D-01), local-agent mechanics (D-02), hosted workflow behavior (D-03), service limits (D-04), evaluation-practice maturity (D-07), handoff tooling (D-08), visibility mechanics (D-09); stable_enough for external-memory theory (D-05) and Git-history exposure persistence (D-06). No external check has been performed at any point in this track; all dated statements above carry cycle 2026Q2 (RPT-0001 layer: 2026-05-23). Whether the final adopted baseline triggers a delta refresh is a user decision.

## 15. Visual-review limitation register (carried forward)

The six initial-cycle PDFs authority types; nine-item storage decision matrix; visibility-pessimism rule; pointer and redaction-manifest schemas; approval workflow with linked IDs and rejected-artifact retention; five candidate buckets | F2B6-UG-01…06 | Q-07-final, Q-11, Q-14 |
| five-object dry-run model with claim boundaries; 14 evaluation dimensions with deterministic/LLM-judge/user-confirmation split; ten critical blockers; decoupled scorecard and verdicts; minimum evidence package; postmortem and regression schemas; integration buckets | F2B6-FT-01…06 | Q-09-final |
| cross-report convergences: gates-before-scores, LLM-judge never sole, evidence-path mandates, staleness first-class, lesson containment, anti-automation v0.1 staging | STEP2B6 §12 matrix | — (method principles) |

## 12. STEP-1 need coverage closure table

| need_id | final_evidence_coverage | key_supporting_registers | open_decision |
|---|---|---|---|
| GF1A-N01 | covered_at_baseline_level | CB-01…06,17…19,23 | — |
| GF1A-N02 | covered: per-surface dated boundaries + maturity-grading practice | CB-02…04,08,15; F2B6-MT-05 | — |
| GF1A-N03 | covered: scenario differences, adaptation map, meta-agent novelty | CB-23…27 | scenario priorities |
| GF1A-N04 | covered_at_principle_level: routing/refresh/delta practice | F2B6-MT-06; STEP2A D-registers | — |
| GF1A-N05 | user_decision_not_research_fact | — | Q-01 |
| GF1A-N06 | covered with reconciliation: preservation outside Git; derivations never substitute | F2B6-UG-01,02,06; CB-20 | Q-03, Q-07-final, Q-15 |
| GF1A-N07 | covered: enforceable review gates, check-split, approval workflows | CB-12,13,16; F2B6-FT-03; F2B6-UG-06 | Q-02 |
| GF1A-N08 | partially covered: change notes + rejected-artifact retention as correction path | F2B6-UG-06 | Q-02, Q-11 |
| GF1A-N09 | covered: architectural grounding + surface facts | CB-17…20; CB independent persistent-memory architecture candidate from exactly two inputs — the STEP-1 need model and this STEP-2C baseline — honoring every open question as an explicit design parameter rather than a silent assumption; no repository reads beyond this track's own outputs unless the instruction pins them; no comparison with the existing design (comparison remains a later, separately authorized phase); limits, section list, and word budget pinned in the GF-STEP-3 instruction.

## 20. Boundary statement

This file is non-execution-source advisory evidence only. It authorizes no repository writes, no execution tasks, no execution-source updates, no adoption of any instrument or policy, no reading of any report, prompt, summary, or index, no external research, no model or vendor evaluation, no comparison against or modification of the existing design, no architecture work, and no target-project artifacts; the paused route stays paused. `current/human-approved-spec.md` remains Mnemosyne's only execution source; any conflict between this file and it is resolved in the execution source's favor and reported, never silently reconciled. GF-STEP-2C is complete; GF-STEP-2 is complete; GF-STEP-3 is not started.
