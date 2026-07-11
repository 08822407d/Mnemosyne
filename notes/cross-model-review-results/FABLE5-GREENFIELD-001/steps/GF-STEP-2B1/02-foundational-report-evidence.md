# FABLE5-GREENFIELD-001 — GF-STEP-2B1 Foundational Report Evidence Review

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2B1
step_name: foundational_external_memory_report_evidence_review
record_type: foundational_original_report_evidence_review
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-2A
research_mode: false
date: 2026-07-11
source_file:
  path: raw/research-reports/cycles/2026Q2-initial/originals/AI agent 长期记忆系统 pro深度研究.txt
  expected_blob_sha: 1c4a48c53d7ac126eb29a0ea7ab1e0e8a0f5c82a
  observed_blob_sha: 1c4a48c53d7ac126eb29a0ea7ab1e0e8a0f5c82a
  sha_match: true
report_id: RPT-2026Q2-0001
report_stated_evidence_date: 2026-05-23
step_status: GF_STEP_2B1_complete_foundational_report_review_ready_for_STEP2B2
```

## 2. Scope and hard limits

Bounded document-evidence review of one archived original report. No model/vendor evaluation or ranking, no model-internals work, no web verification of current product behavior, no architecture, no comparison with the existing design, no repairs. Limits: paths 1/1; batteries 1/2; reports read 1/1; evidence records 14/14 max; signals directly reassessed exactly S-01/S-02/S-03; no PDF, summary, or prompt reads; no external research; Research mode off; no automatic continuation.

## 3. Allowed sources and anti-contamination policy

Inputs: the STEP2A deliverable (used only for report/domain/signal/need IDs and the source-strength, PDF, and freshness rules) and exactly the one pinned txt original, fetched by one single-path raw-endpoint battery (URL-encoded path) and SHA-verified before reading. No other repository file or prohibited tier was opened. The report internally names many products, mechanism files (AGENTS.md, CLAUDE.md, Cursor rules, MCP configs), frameworks, and the user's uploaded research definition — all report-internal metadata only, none opened. Prior-exposure disclosure carries forward: independence by derivation and disclosure. Per rule, this review does not update, correct, or supplement the report from any knowledge outside it.

## 4. Source integrity and access result

- Expected SHA `1c4a48c53d7ac126eb29a0ea7ab1e0e8a0f5c82a`; observed identical; match: true.
- Complete text inspected: yes — 287 lines, 33,062 bytes, read in full; no truncation or unreadable section.
- Report's own stated evidence date: conclusions based on sources verifiable as of **2026-05-23** (l.3); §14 explicitly excludes future capabilities from the current feasibility basis.
- Format note: the file is a saved deep-research output (opening line "Thought for 9m 26s"), addressed to the user in second person; treated as research evidence only.
- Batteries used: 1 of 2.

## 5. Evidence interpretation rules

Categories used: report_direct_finding, report_author_synthesis, report_recommendation, cited_external_claim_not_independently_checked, dated_product_or_workflow_statement, low_drift_engineering_principle, mixed_or_uncertain. Applied: the report is evidence, not execution source; cited vendor statements stay unverified here; recommendations are not capability facts; product/workflow statements keep the 2026-05-23 date and their surface scope; no statement about one interface or mode is universalized; principles, dated observations, recommendations, and uncertainty are separated; no training-knowledge updates or corrections; no self/model discussion; the report is not treated as proving every project should use GitHub; no implementation detail imported from the existing design.

## 6. Report coverage map

| section_or_anchor | topic | inspected | reason_if_partial_or_no | relevant_research_domain_ids | relevant_STEP1_need_ids | candidate_evidence_item_ids |
|---|---|---|---|---|---|---|
| §1 ll.5–16 | overall feasibility; surface stratification | yes | — | RD-11,RD-01,RD-03,RD-04 | GF1A-N01,N02 | E01,E02 |
| §2 ll.18–32 | non-dev practice classes (containers, notebooks, tutors, PKM/RAG) | yes | — | RD-02 (corroboration only) | GF1A-N03 | E—(context) |
| §3 ll.34–43 | dev→non-dev transfer; verification adaptation; write gating | yes | — | RD-06 (corroboration only) | GF1A-N03,N07 | E13(context) |
| §4.1 ll.46–59 | rule-loading chain | yes | — | RD-03,RD-01 | GF1B-N15 | E06 |
| §4.2 ll.61–76 | memory-reading chain | yes | — | RD-01,RD-03,RD-05 | GF1A-N01,N09 | E07 |
| §4.3 ll.78–93 | handoff generation/recovery chain | yes | — | RD-08 (corroboration), RD-01 | GF1A-N12 | E08 |
| §4.4 ll.95–108 | write-back chain | yes | — | RD-01,RD-03,RD-04 | GF1A-N07; GF1B-N15 | E03,E04,E05,E09,E13 |
| §4.5 ll.110–119 | version-audit chain | yes | — | RD-04,RD-05 | GF1B-N15,N13; GF1A-N11 | E10 |
| §4.6 ll.121–132 | cross-environment migration chain | yes | — | RD-05,RD-06 | GF1A-N10,N09 | E11 |
| §5 ll.134–174 | scenarios A–D (dialogue, local agent, cloud agent, multi-agent) | yes | — | RD-01,RD-03,RD-04 | GF1A-N03; GF1B-N15 | E09,E12 |
| §6 ll.176–188 | per-tool capability boundary table | yes | — | RD-01,RD-03,RD-04 | GF1A-N02 | E02–E05 |
| §7–§10 ll.189–241 | strong-evidence mechanisms; semi-automatic; extra-tooling; anti-patterns | yes | — | RD-11,RD-01,RD-05 | GF1A-N01,N09; GF1B-N15 | E13,E14 |
| §11–§12 ll.243–267 | source list with evaluations; mechanism→case maturity map | yes | — | RD-11 | GF1A-N02 | E—(citation layer) |
| §13–§14 ll.268–286 | drafting reference points; future-watch list excluded from current basis | yes | — | RD-05,RD-11 | GF1A-N05,N06(adjacent) | E13,E14 |

## 7. Foundational evidence register

Register-wide: report_evidence_date_or_cutoff = 2026-05-23 for every item; underlying_source_independently_checked_in_this_step = false for every item. 14 items.

| evidence_id | source_anchor | concise_statement | evidence_category | scope | confidence_as_report_evidence | date_sensitivity | related_research_domain_ids | related_STEP1_need_ids | supports_or_challenges_preliminary_signal_ids | prohibited_overclaim |
|---|---|---|---|---|---|---|---|---|---|---|
| F2B1-E01 | ll.7,15–16 | externalizing rules/state/tasks/handoff/raw/eval to Git/Markdown/DB/RAG with model reads and reviewed write-back is engineering-feasible and variously validated; it is a cross-tool workflow/governance architecture, not a native chat feature | report_author_synthesis | cross_surface | high | medium | RD-11 | GF1A-N01,N09 | supports S-01 | "feasible pattern" ≠ equal automation everywhere |
| F2B1-E02 | ll.9–13 | automation is stratified: local/cloud coding agents strongest and most auditable; plain ChatGPT/Claude dialogue medium — auto repo pull, auto write-back, auto PR, auditable version chains are not default chat capabilities | dated_product_or_workflow_statement | cross_surface | high | high | RD-01,RD-11 | GF1A-N01,N02 | supports S-02 | not "chat can never do it" — dated, per-surface |
| F2B1-E03 | ll.11,99,179,209 | ChatGPT GitHub app per official docs: read/analyze/search only; cannot push, update, or open PRs; cannot search specific filenames; write paths pointed to Codex | cited_external_claim_not_independently_checked | conversation_surface | high | high | RD-01 | GF1A-N02 | supports S-02 | one connector as of 2026-05-23, not all apps/futures |
| F2B1-E04 | ll.101,180,227 | some ChatGPT Apps/Agent can perform write actions app/config-dependent; MCP write actions plan/permission-limited; Tasks do not access Project files | cited_external_claim_not_independently_checked | conversation_surface | medium | high | RD-01 | GF1A-N02 | refines S-02 | conditional tool-mediated writes ≠ assumable auto write-back |
| F2B1-E05 | ll.103,182,184 | Claude web Projects: knowledge/instructions/RAG strong; no official evidence of auto write-back to external Git; Cowork reads/writes local files but desktop-only, local-only, no cloud sync | cited_external_claim_not_independently_checked | conversation_surface | medium | high | RD-01 | GF1A-N02 | supports S-02,S-03 | absence of evidence ≠ impossibility |
| F2B1-E06 | ll.50–56,127,241 | rule files are mature in dev agents (AGENTS.md global/repo/nested; CLAUDE.md read at session start; Cursor rules); rules are context, not enforced config; overlong rule files reduce adherence — keep short, layered, reviewable | mixed_or_uncertain | local_project_workflow | high | medium | RD-03 | GF1B-N15 | preliminary corroboration toward S-04 | rule file ≠ guaranteed compliance |
| F2B1-E07 | ll.63–76 | external-memory reading is feasible on all surfaces but modes differ; on-demand retrieval beats loading everything; chat needs upload/Project/connector; dev agents read repos natively; smart retrieval needs RAG/graph/MCP/scripts | report_author_synthesis | cross_surface | high | medium | RD-01,RD-03,RD-05 | GF1A-N01,N09 | supports S-01 | reading feasibility ≠ reliable targeted retrieval everywhere |
| F2B1-E08 | ll.80–93,213 | handoff is feasible everywhere; plain-dialogue recovery is weak, so manual handoff cards are most reliable; dev tooling has sessions/resume/compact/fork/checkpoints; platform-internal continuity is not external auditable handoff | mixed_or_uncertain | cross_surface | high | medium | RD-08(corroboration),RD-01 | GF1A-N12 | preliminary corroboration only (HO-0001 unread) | platform continuity ≠ auditable external handoff |
| F2B1-E09 | ll.97–108 | write-back is the biggest divide: coding agents strongly capable (diff/commit/push/PR; Actions with read-write perms; cloud agents branch+PR); plain web chat weak or tool-dependent | dated_product_or_workflow_statement | cross_surface | high | high | RD-03,RD-04 | GF1A-N07; GF1B-N15 | supports S-01,S-02; preliminary corroboration toward S-04,S-05 | write capability ≠ semantic reliability of writes |
| F2B1-E10 | ll.112–119,164 | Git/GitHub is the strongest-evidenced audit substrate (diff/branch/rollback/PR/review/Actions/CODEOWNERS/protected branches); audit covers file change, not memory quality — human review, citations, sensitive-info scanning still needed; cloud write-back best via PR | low_drift_engineering_principle | hosted_repository_workflow | high | low | RD-04,RD-05 | GF1B-N15,N13; GF1A-N07,N11 | preliminary corroboration toward S-05 | Git audit ⇒ change traceability, not memory correctness |
| F2B1-E11 | ll.123–132 | Markdown/Git/artifact refs/RAG index are relatively model-agnostic; platform memories and rule syntaxes need adapters (CLAUDE.md imports AGENTS.md; memory export experimental); keep one external source of truth plus short per-tool rules/state/handoff | mixed_or_uncertain | cross_surface | high | medium | RD-05,RD-06 | GF1A-N10,N09 | supports S-01 | no cross-tool automatic sync exists |
| F2B1-E12 | ll.162,237 | sensitive memory (privacy, secrets, internal policy, customer data) should not be exposed to cloud agents; Codex cloud removes secrets before the agent phase; minimal permission, isolation, logs, PR review required | cited_external_claim_not_independently_checked | governance | medium | medium | RD-04,RD-09(corroboration) | GF1A-N03; GF1C-N20(adjacent) | preliminary corroboration (UIG-0001 unread) | cloud config ≠ safety guarantee |
| F2B1-E13 | ll.43,108,205–207,235,270–273 | recommended plain-dialogue flow: AI generates a memory-update proposal, the user confirms, then it is written to Git/Markdown; unreviewed automatic modification of long-term memory advised against (contamination amplifies); three layers recommended — short rule layer, state layer, evidence layer retrieved on demand | report_recommendation | governance | high | low | RD-01,RD-05 | GF1A-N07,N11,N05(adjacent) | consistent with S-01 governance framing | recommendation ≠ measured failure data |
| F2B1-E14 | ll.233–241 | do not stuff all memory into one giant prompt — "lost in the middle" and long-context degradation are research-cited; proprietary platform memory must not be the only source of truth (not auditable/migratable/rollbackable) | mixed_or_uncertain | engineering_principle | high | low | RD-05,RD-11,RD-01 | GF1A-N09,N01; GF1B-N15 | supports S-01,S-03 | degradation risk, not "long context is useless" |

## 8. STEP2A signal reassessment

- signal_id: S-01 — previous wording: model context/internal memory is no long-term truth source; external versioned files carry persistent state. Disposition: **report_confirmed**. Supporting evidence: E01,E07,E11,E14. Evidence scope: cross-surface, as a workflow/governance architecture. Date caveat: principle low-drift; the validating product instances are dated 2026-05-23. Remaining original-report dependency: 0004/0005/0006 for substrate-specific depth. Remaining refresh dependency: product instances only. Prohibited overclaim: external files do not by themselves guarantee memory quality — governance still required.
- signal_id: S-02 — previous wording: plain conversation surfaces cannot be assumed to write back to repositories automatically. Disposition: **report_refined**. Replacement wording: as of 2026-05-23, plain-dialogue surfaces have no default repository write-back — the official ChatGPT GitHub app is read-only and cannot target specific filenames; conditional write paths exist only via apps/agents/MCP with per-app permissions and are not assumable defaults. Supporting evidence: E02,E03,E04,E05. Scope: conversation_surface. Date caveat: high — connector and app capabilities are volatile. Remaining dependency: RPT-2026Q2-0003 (dedicated report). Refresh dependency: yes (STEP2A D-01). Overclaim: never say "chat can never write files."
- signal_id: S-03 — previous wording: platform-provided memory is auxiliary, not a project truth source. Disposition: **report_confirmed**. Supporting evidence: E05,E08,E14 (platform memory not complete history, not auditable/migratable/rollbackable; export experimental). Scope: conversation_surface. Date caveat: medium-high. Remaining dependency: RPT-2026Q2-0003. Refresh dependency: yes (D-01/D-04). Overclaim: "auxiliary" is not "useless."
- S-04/S-05 note: E06,E09,E10,E12 provide broad corroboration only; S-04 and S-05 remain unconfirmed — their dedicated reports (0004, 0005) are unread.

## 9. Principle-versus-product separation

| evidence_id | class | concise_content | why_it_belongs_in_this_class | may_be_used_in_final_STEP2_without_external_refresh | later_source_needed |
|---|---|---|---|---|---|
| E01 | A low_drift_principles | externalized, reviewed file-based memory as workflow architecture | engineering approach independent of any one product | yes_with_date_caveat | 0004,0005,0006 |
| E10 | A | Git version/diff/rollback/review as audit substrate; audits change, not quality | inherent VCS properties | yes | 0005 (workflow detail) |
| E11 | A | model-agnostic core (Markdown/Git/refs/index) + per-tool adapters | format neutrality is structural | yes_with_date_caveat (adapter specifics dated) | 0007,0006 |
| E14 | A | long-context degradation; platform memory not sole truth source | research-cited + structural auditability argument | yes | 0006 |
| E02 | B dated_product_or_workflow_observations | stratified automation across surfaces | product-state snapshot | yes_with_date_caveat | 0003,0004,0005; delta refresh |
| E03 | B | ChatGPT GitHub app read-only, no filename search | official-doc snapshot | yes_with_date_caveat | 0003; delta refresh |
| E04 | B | conditional app/MCP writes; Tasks exclude Project files | plan/config-dependent snapshot | yes_with_date_caveat | 0003; delta refresh |
| E05 | B | Claude web no write-back evidence; Cowork local-only | official-doc snapshot | yes_with_date_caveat | 0003; delta refresh |
| E06 | B | rule-file mechanics mature; context-not-config; short/layered | product mechanics + practice guidance | yes_with_date_caveat | 0004 |
| E08 | B | session/resume/checkpoint mechanisms; weak chat recovery | product mechanics snapshot | yes_with_date_caveat | HO-0001 (batch 3) |
| E09 | B | write-back divide across surfaces | product-state snapshot | yes_with_date_caveat | 0004,0005 |
| E12 | B | cloud-agent secret handling and exposure limits | vendor-doc snapshot | yes_with_date_caveat | 0005; UIG-0001 |
| E13 | C report_recommendations_or_design_options | proposal-confirm write flow; no unreviewed auto-writes; three-layer structure | prescriptive, pending user adoption | yes (as recommendation, flagged) | user decision + batch 3 |

## 10. Contradiction and uncertainty register

| issue_id | source_anchor | issue_type | description | affected_evidence_ids | handling_for_later_STEP2 |
|---|---|---|---|---|---|
| U-01 | §4,§6,§11 | vendor-doc dependence | many boundary claims cite official documentation, unverified here | E03,E04,E05,E06,E12 | keep cited_external class; verify only via later delta research, not in-step |
| U-02 | §4.4,§6 | surface dependence | the same capability differs by product mode (web vs apps vs agent tooling) | E02–E05,E09 | per-claim surface scope mandatory in any final baseline statement |
| U-03 | l.3,§14 | freshness load-bearing | report brackets future capabilities out; product statements dated 2026-05-23 | all class-B items | date caveats + STEP2A D-01…D-04 refresh path |
| U-04 | §2 vs §10 | apparent tension, resolved | platform containers praised as useful while platform memory rejected as truth source | E05,E14 | preserve auxiliary-vs-truth-source distinction; not a contradiction |
| U-05 | ll.101,129,209,211 | explicit residual uncertainty | MCP write availability plan/permission-dependent; memory export experimental; connector filename retrieval "not to be assumed stable"; notebook source sync manual | E04,E05,E11 | carry as open capability uncertainty; no assumption either way |

## 11. STEP-1 linkage delta

| need_id | previous_coverage | coverage_after_this_report | supporting_evidence_ids | remaining_report_dependencies | user_decision_not_resolved_by_evidence |
|---|---|---|---|---|---|
| GF1A-N01 | partially_covered | partially_covered, strengthened | E01,E02,E07,E14 | 0003,0006 | — |
| GF1A-N02 | partially_covered | partially_covered, strengthened | E02,E03,E04,E05,E09,E12 | 0003,0004,0005 | — |
| GF1A-N04 | partially_covered | partially_covered, marginally strengthened | E13; §14 future-watch framing | batch-3 reports | — |
| GF1A-N09 | partially_covered | partially_covered, strengthened | E01,E07,E11,E14 | 0006 | — |
| GF1A-N10 | partially_covered | partially_covered, strengthened | E11 | 0007,0006 | — |
| GF1B-N15 | partially_covered | partially_covered, strengthened | E06,E09,E10,E11 | 0004,0005,0006 | Q-04 storage-product choice |

## 12. Deferred-source register

Kept unread: RPT-2026Q2-0003, RPT-2026Q2-0004, RPT-2026Q2-0005; all STEP2A batch-2 reports (0006, 0002, 0007) and batch-3 reports (MT-0001, HO-0001, UIG-0001, FTDRE-0001). Without them this report cannot settle: plain-dialogue boundary depth and its volatile connector specifics (0003); local-agent substrate mechanics (0004); hosted write-back, permission, and audit workflow detail (0005); theoretical grounding (0006); scenario adaptation (0002, 0007); evaluation, handoff, governance, and dry-run method/policy selection (batch 3). No further report is read in this substep.

## 13. Incidental-exposure ledger

None. One single-path retrieval exposed no other file; product names, mechanism files, frameworks, and the user's research definition referenced inside the report were treated as report-internal metadata only, never opened.

## 14. Coverage and limitation ledger

- SHA: expected `1c4a48c5…` = observed; match true.
- Full text inspected: yes (287 lines; every report section §1–§14 covered per §6 map).
- Retrieval batteries: 1 of 2.
- Evidence records created: 14 (F2B1-E01…E14).
- Signal dispositions: S-01 report_confirmed; S-02 report_refined; S-03 report_confirmed; S-04/S-05 preliminary corroboration only, unconfirmed.
- Low-drift items: 4 (E01,E10,E11,E14); dated items: 9; recommendations: 1 (E13).
- Unresolved freshness dependencies: all class-B items dated 2026-05-23; refresh path per STEP2A D-01…D-04; no external check performed.
- Deferred reports: 10 (§12).
- Limitation: all external citations inside the report remain unverified in this step; no training-knowledge correction was applied.
- STEP2B1 completion: yes.

## 15. STEP2B1 status determination

Determination: **GF_STEP_2B1_complete_foundational_report_review_ready_for_STEP2B2**. Integrity verified, full report inspected, evidence register and signal dispositions produced within limits. GF-STEP-2 is not complete.

## 16. Proposed bounded STEP2B2

- step_name: plain_dialogue_boundary_report_evidence_review.
- Source: exactly RPT-2026Q2-0003 — `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 2：ChatGPT,Claude 纯对话场景的外部记忆能力边界.pdf` — expected blob SHA to be pinned in the STEP2B2 instruction and verified before reading.
- PDF handling: text extraction method specified in the instruction; text-derived claims flagged text_only; no chart/table/image/layout-dependent conclusion pending the manual figure review (STEP2A §10).
- Work: deepen and re-test S-02 (refined) and S-03; extend or challenge E02–E05; per-claim surface scope and evidence date mandatory; ≤2 batteries; evidence-record cap; word budget; one structural and one word-count check; stop after one file and a brief summary.
- Not executed here.

## 17. Boundary statement

This file is non-execution-source advisory evidence only. It authorizes no repository writes, no execution tasks, no execution-source updates, no reading of any other report, summary, prompt, or PDF, no external research, no model or vendor evaluation, no comparison against or modification of the existing design, no architecture work, and no target-project artifacts; the paused route stays paused. `current/human-approved-spec.md` remains Mnemosyne's only execution source; any conflict between this file and it is resolved in the execution source's favor and reported, never silently reconciled. GF-STEP-2B1 is complete; GF-STEP-2 is not complete.
