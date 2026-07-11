# FABLE5-GREENFIELD-001 — GF-STEP-2A Research Evidence Catalog and Staged Reading Plan

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2A
step_name: research_evidence_catalog_and_staged_reading_plan
record_type: research_evidence_catalog_and_read_plan
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-1E
GF_STEP_1_status: complete_with_explicit_open_questions
research_mode: false
date: 2026-07-11
source_files:
  - path: raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md
    expected_blob_sha: f90f4854f8cdac903d919d6918d49e667e812f3f
  - path: raw/research-reports/current/research-report-index.md
    expected_blob_sha: 0efc2af50cd4ef37abb93aa67b33fdd4c812c9be
  - path: raw/research-reports/current/current-report-summaries.md
    expected_blob_sha: f22906d36613c70b686f5121f9b1d8e5091dab0b
step_status: GF_STEP_2A_complete_source_map_ready_for_STEP2B
```

## 2. Scope and limits

Planning substep for GF-STEP-2 only: catalog active reports, map them to STEP-1 needs, record evidence limits, select a bounded STEP2B batch. No model/service evaluation, final baseline, external research, architecture, or change recommendations. Limits: paths 3/3; batteries 3/3; active reports 11/11; domains 11; signals 15/16; date items 9/10; STEP2B reports 4/4; no original-report, individual-summary, prompt, or PDF reads; no external search; Research mode off; no automatic continuation into STEP2B. Word budget: the first draft exceeded the 3,400 cap; the single permitted light compression pass removed narration/connective wording only; final count in the step summary.

## 3. Allowed sources and anti-contamination policy

Inputs: the STEP1E deliverable (used only for need IDs, open-question references, topic relevance) and exactly the three pinned files, each fetched by one single-path raw-endpoint battery, SHA-verified before reading. No other repository file or prohibited tier was opened. The allowed files name other paths — summary files, prompt files, prompt index, report-topic map, `pdf-figure-review-index.md`, `current/human-approved-spec.md`, task IDs MNEMOSYNE-030C/038, question IDs OP-09/OP-10 — all metadata only, none opened. Prior-exposure disclosure carries forward: independence by derivation and disclosure.

## 4. Source-status rules

Source classes kept separate: motivation_context (why a topic exists; not a result), report_index_metadata (ID/cycle/path/format/topic/status/review notes; not a result), summary_index_signal (conclusion explicit in the summary index; weaker than the original), original_report_needed, visual_check_needed, date_refresh_candidate. Prohibitions applied: motivation text never treated as a report conclusion; no original claimed read; summaries never stronger than originals; unreviewed PDF figures never verified evidence; no report is execution source; topics never turned into detailed technical claims. Note: the summary index carries only status metadata for the seven initial-cycle reports — their present evidence is motivation_context + report_index_metadata; explicit summary_index_signals exist only for MT/HO/UIG.

## 5. Source-access and SHA table

| source | path | expected_sha | observed_sha | match | complete_read | lines | battery |
|---|---|---|---|---|---|---|---|
| motivation | raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md | f90f4854… | f90f4854… | true | true | 144 | 1 |
| report index | raw/research-reports/current/research-report-index.md | 0efc2af5… | 0efc2af5… | true | true | 79 | 2 |
| summary index | raw/research-reports/current/current-report-summaries.md | f22906d3… | f22906d3… | true | true | 94 | 3 |

Full SHAs in §1; abbreviations display-only.

## 6. Active-report inventory

Path prefixes (exact, per index): P1 = `raw/research-reports/cycles/2026Q2-initial/originals/`; S1 = `raw/research-reports/cycles/2026Q2-initial/report-summaries/`; supplemental cycles use `raw/research-reports/cycles/<cycle>/originals/` and `.../report-summaries/` with cycle in {2026Q2-memory-testing, 2026Q2-handoff-strategy, 2026Q2-user-input-governance, 2026Q2-first-target-dry-run-evaluation}.

| report_id | cycle_id | topic_as_listed | report_type | original_report_path | summary_path_or_none | active_evidence | source_format | summary_status | visual_review_status | related_research_domains | related_STEP1_need_ids | planning_value | proposed_reading_batch | reason_for_priority | date_sensitivity | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RPT-2026Q2-0001 | RC-2026Q2-initial | comprehensive AI-agent long-term memory deep research | pro | P1+`AI agent 长期记忆系统 pro深度研究.txt` | S1+`RPT-2026Q2-0001-summary.md` | yes | txt | completed_from_readable_txt | not_applicable_txt | RD-01,03,04,05,11 | GF1A-N01,N02,N09;GF1B-N15 | foundational | batch_1 | cross-surface boundary evidence anchoring RD-11; no visual dependency | high | index advises sampling verification |
| RPT-2026Q2-0002 | RC-2026Q2-initial | non-dev long-term dialogue memory practice | light | P1+`轻度研究子课题 1：非开发长期对话记忆是否已有真实实践.pdf` | S1+`RPT-2026Q2-0002-summary.md` | yes | pdf | completed_from_readable_pdf_text | pending_manual_review | RD-02,06 | GF1A-N03,N01 | medium | batch_2 | scenario-adaptation evidence; downstream of boundaries | medium | text-only summary caveat |
| RPT-2026Q2-0003 | RC-2026Q2-initial | ChatGPT/Claude pure-dialogue external-memory boundary | light | P1+`轻度研究子课题 2：ChatGPT,Claude 纯对话场景的外部记忆能力边界.pdf` | S1+`RPT-2026Q2-0003-summary.md` | yes | pdf | completed_from_readable_pdf_text | pending_manual_review | RD-01 | GF1A-N01,N02,N09 | high | batch_1 | default target surface; automation assumptions shape delivery commitments | high | figures pending |
| RPT-2026Q2-0004 | RC-2026Q2-initial | local dev-agent file memory | light | P1+`轻度研究子课题 3：Codex,Claude Code,Cursor 等本地开发 Agent 的文件式记忆能力.pdf` | S1+`RPT-2026Q2-0004-summary.md` | yes | pdf | completed_from_readable_pdf_text | pending_manual_review | RD-03,05 | GF1B-N15;GF1A-N09,N11 | high | batch_1 | file/repo capability is the design substrate | high | figures pending |
| RPT-2026Q2-0005 | RC-2026Q2-initial | cloud coding agent + GitHub write-back and audit | light | P1+`轻度研究子课题 4：云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计.pdf` | S1+`RPT-2026Q2-0005-summary.md` | yes | pdf | completed_from_readable_pdf_text | pending_manual_review | RD-04 | GF1B-N15,N13;GF1A-N07,N11 | high | batch_1 | audited write-back and claim-vs-diff risk shape the human gate | high | figures pending |
| RPT-2026Q2-0006 | RC-2026Q2-initial | theory and engineering basis of external persistent memory | light | P1+`轻度研究子课题 5：外部持久记忆的理论与工程依据.pdf` | S1+`RPT-2026Q2-0006-summary.md` | yes | pdf | completed_from_readable_pdf_text | pending_manual_review | RD-05,11 | GF1A-N01,N09;GF1B-N15 | high | batch_2 | low-drift grounding; batch 2 sufficient | low | figures pending |
| RPT-2026Q2-0007 | RC-2026Q2-initial | dev-scenario memory transfer to dialogue/learning scenarios | light | P1+`轻度研究子课题 6：开发场景的持久记忆经验能否迁移到普通长期对话和学习场景.pdf` | S1+`RPT-2026Q2-0007-summary.md` | yes | pdf | completed_from_readable_pdf_text | pending_manual_review | RD-06,02 | GF1A-N03,N10 | medium | batch_2 | transfer/tailoring evidence for scenario templates | medium | figures pending |
| RPT-2026Q2-MT-0001 | RC-2026Q2-memory-testing | memory-system testing/debugging/evaluation/failure diagnosis | deep_research | `.../2026Q2-memory-testing/originals/DR1_memory_testing_debugging_evidence_review_report.md` | `.../report-summaries/DR1_..._summary.md` | yes | markdown | completed_from_markdown_report | not_applicable_markdown | RD-07 | GF1C-N19;GF1A-N11 | high | batch_3 | Q-08-updated method-selection evidence, not boundary core | medium | index signal: no unified mature standard; reusable practices exist |
| RPT-2026Q2-HO-0001 | RC-2026Q2-handoff-strategy | handoff package strategy and quantitative evaluation | deep_research | `.../2026Q2-handoff-strategy/originals/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_report.md` | `.../report-summaries/DR2_..._summary.md` | yes | markdown | available_per_index | not_applicable_markdown | RD-08 | GF1A-N12;GF1C-N19 | high | batch_3 | rubric/tier/provenance method selection (Q-08-updated,Q-13 input) | medium | rich summary signals present |
| RPT-2026Q2-UIG-0001 | RC-2026Q2-user-input-governance | user originals, redaction, visibility, pointers, Git-history exposure | deep_research | `.../2026Q2-user-input-governance/originals/DR4_user_originals_requirements_redaction_governance_report.md` | `.../report-summaries/DR4_..._summary.md` | yes | markdown | available_per_index | not_applicable_markdown | RD-09 | GF1C-N20;GF1A-N06;GF1B-N14 | high | batch_3 | Q-07-updated/Q-11/Q-12 policy content, pre-adoption | medium | strong summary signals present |
| RPT-2026Q2-FTDRE-0001 | RC-2026Q2-first-target-dry-run-evaluation | first real target-project dry-run evaluation framework | deep_research | `.../2026Q2-first-target-dry-run-evaluation/originals/DR5_first_real_target_dry_run_evaluation_framework_report.md` | `.../report-summaries/DR5_..._summary.md` | yes | markdown | completed_from_markdown_report | not_applicable_markdown | RD-10 | GF1C-N21 | high | batch_3 | Q-09-updated framework content; need already prompt-checked | medium | evidence only per index |

## 7. Research-domain map

| domain_id | domain_title | related_STEP1_need_ids | relevant_report_ids | evidence_level_currently_available | original_reports_needed | visual_check_dependency | date_sensitivity | why_the_domain_matters |
|---|---|---|---|---|---|---|---|---|
| RD-01 | ordinary conversation continuity and platform-provided memory | GF1A-N01,N02,N09,N12 | 0003,0001 | motivation_context + report_index_metadata | yes (batch 1) | yes (0003 pdf) | high | default surface; automation assumptions bound commitments |
| RD-02 | non-development long-term dialogue, learning and research | GF1A-N03 | 0002,0007 | motivation_context + report_index_metadata | yes (batch 2) | yes | medium | per-scenario need requires scenario-specific feasibility |
| RD-03 | local project-file workflows | GF1B-N15;GF1A-N09,N11 | 0004,0001 | motivation_context + report_index_metadata | yes (batch 1) | yes (0004 pdf) | high | file substrate underpins the memory design |
| RD-04 | hosted repository and review workflows | GF1B-N15,N13;GF1A-N07,N11 | 0005,0001 | motivation_context + report_index_metadata | yes (batch 1) | yes (0005 pdf) | high | audited write-back and claim-vs-diff risk shape the human gate |
| RD-05 | external file and version-history engineering basis | GF1A-N01,N09;GF1B-N15 | 0006,0001 | motivation_context + report_index_metadata | yes (batch 2) | yes (0006 pdf) | low | grounds external files as persistence substrate |
| RD-06 | transfer between development and non-development scenarios | GF1A-N03,N10 | 0007,0002 | motivation_context + report_index_metadata | yes (batch 2) | yes | medium | tailoring rules for target-type templates |
| RD-07 | quality assurance, issue detection and evaluation evidence | GF1C-N19;GF1A-N11 | MT-0001 | + summary_index_signal | yes (batch 3) | no | medium | Q-08-updated method selection |
| RD-08 | handoff and continuation between sessions and tools | GF1A-N12;GF1C-N19 | HO-0001 | + summary_index_signal | yes (batch 3) | no | medium | handoff quantification and Q-13 inputs |
| RD-09 | user-input handling, visibility, redaction and external references | GF1C-N20;GF1A-N06;GF1B-N14 | UIG-0001 | + summary_index_signal (strong) | yes (batch 3, pre-adoption) | no | medium | Q-07-updated/Q-11/Q-12 policy content |
| RD-10 | first-target trial evaluation and decision boundaries | GF1C-N21 | FTDRE-0001 | report_index_metadata | yes (batch 3) | no | medium | Q-09-updated framework content |
| RD-11 | overall feasibility and scope of an external-memory meta-agent | GF1A-N01,N02,N03,N04 | 0001,0006 | motivation_context + report_index_metadata | yes (batch 1: 0001) | no (0001 txt) | high (product) / low (principles) | anchors the later baseline |

No final rule or design recommendation is written for any domain.

## 8. Preliminary evidence-signal register

Planning items only; none is a final factual rule. 15 signals.

| signal_id | concise_signal | domain_id | source_report_ids | current_source_level | current_confidence | original_report_needed | visual_check_possible | date_refresh_possible | claim_boundary_note | related_STEP1_need_ids |
|---|---|---|---|---|---|---|---|---|---|---|
| S-01 | model context/internal memory is no long-term truth source; external versioned files carry persistent state | RD-05 | 0001,0006 | motivation_only | medium | yes | uncertain | no | commissioned premise, not report-confirmed | GF1A-N09;GF1B-N15 |
| S-02 | plain chat surfaces cannot be assumed to write back to repositories automatically | RD-01 | 0003,0001 | motivation_only | medium | yes | yes | yes | never extend to "can never write files" — surface- and date-specific | GF1A-N01,N02 |
| S-03 | platform built-in memory is auxiliary, not a project truth source | RD-01 | 0003,0001 | motivation_only | medium | yes | uncertain | yes | no claim about future platform features | GF1A-N09,N02 |
| S-04 | local coding-agent file access is a prerequisite, not automatic reliable memory (needs execution source, write-back flow, audit, confirmation, handoff) | RD-03 | 0004 | motivation_only | medium | yes | yes | yes | prohibited-overclaim example; keep conditional | GF1B-N15;GF1A-N07,N11 |
| S-05 | cloud coding-agent completion claims can diverge from actual diffs; audit = task records + diff + review | RD-04 | 0005 | motivation_only | medium | yes | yes | yes | risk statement, not a measured frequency | GF1A-N07;GF1B-N13 |
| S-06 | non-dev scenarios may need lighter intake/handoff/review than dev repositories | RD-02 | 0002 | motivation_only | low | yes | yes | uncertain | adaptation direction only, not a template rule | GF1A-N03 |
| S-07 | dev-scenario file-memory experience transfers only with tailoring (privacy, cadence, maintenance cost, tool capability differ) | RD-06 | 0007 | motivation_only | medium | yes | yes | uncertain | transfer degree unquantified | GF1A-N03,N10 |
| S-08 | no unified mature memory-specific testing standard; reusable evaluation/debugging practices exist | RD-07 | MT-0001 | summary_index | medium | yes | no | uncertain | absence-of-standard claim dated 2026Q2 | GF1C-N19 |
| S-09 | handoff direction basically sound but insufficiently quantified; correctness measured by recovery of execution source, gate/state, authorities, prohibitions, next safe action, stale resistance, assumption handling, evidence paths | RD-08 | HO-0001 | summary_index | medium | yes | no | uncertain | rubric content requires original + user adoption | GF1A-N12;GF1C-N19 |
| S-10 | repeatable scored replay test precedes the first real dry run; blocker failures prevent proceeding | RD-08 | HO-0001 | summary_index | medium | yes | no | no | recommendation-level, pending adoption | GF1C-N21,N19 |
| S-11 | handoff packages tier into minimum/standard/extended; longer is not automatically safer | RD-08 | HO-0001 | summary_index | medium | yes | no | no | tier content is candidate method | GF1A-N12 |
| S-12 | model/tool provenance and hidden-context risks must be recorded for handoff tests | RD-08 | HO-0001 | summary_index | medium | yes | no | no | schema content is candidate | GF1A-N12;GF1C-N19 |
| S-13 | visibility_unverified is treated as public-equivalent for storage decisions | RD-09 | UIG-0001 | summary_index | medium | yes | no | uncertain | candidate policy rule, not adopted governance | GF1C-N20 |
| S-14 | originals, raw requirements, secrets, sensitive/unredacted materials default outside Git; approved decisions, reviewed redactions, synthetic substitutes, safe pointers Git-eligible if approved | RD-09 | UIG-0001 | summary_index | medium | yes | no | no | default-rule candidate pending user decision (Q-07-updated) | GF1C-N20;GF1A-N06;GF1B-N14 |
| S-15 | Git history exposure persists through delete/move/revert; private repo does not authorize originals | RD-09 | UIG-0001 | summary_index | high | no | no | no | stable VCS property; policy application still a user decision (Q-11) | GF1C-N20;GF1B-N15 |

## 9. STEP-1 linkage table

| need_id | related_research_domains | present_evidence_coverage | report_ids_to_read | related_open_questions | handling_note_for_later_STEP2_work |
|---|---|---|---|---|---|
| GF1A-N01 | RD-01,05,11 | partially_covered | 0001,0006,0003 | — | batch 1–2 feasibility boundaries |
| GF1A-N02 | RD-01,03,04,11 | partially_covered | 0001,0003,0004,0005 | — | boundary claims must carry dates + surface scope |
| GF1A-N03 | RD-02,06 | partially_covered | 0002,0007 | — | batch-2 scenario evidence |
| GF1A-N04 | RD-11 | partially_covered | 0001 | — | delta/refresh practice per motivation §8 |
| GF1A-N05 | — | user_decision_not_research_fact | — | Q-01 | placement acceptance ≠ capability fact |
| GF1A-N06 | RD-09 | partially_covered | UIG-0001 | Q-03,Q-07-updated | batch-3 governance evidence; digest sufficiency = user decision |
| GF1A-N07 | RD-04,10 | partially_covered | 0005,FTDRE-0001 | Q-02 | batch-1 audit-path evidence; granularity = user decision |
| GF1A-N08 | RD-09 | partially_covered | UIG-0001 | Q-02,Q-11 | mostly design/user; Git-history constraint from RD-09 |
| GF1A-N09 | RD-05,01 | partially_covered | 0006,0001,0003 | — | theory batch 2; surface facts batch 1 |
| GF1A-N10 | RD-06,11 | partially_covered | 0007,0001 | Q-03 | vendor-neutral evidence; migration mechanics later |
| GF1A-N11 | RD-04,07 | partially_covered | 0005,MT-0001 | — | audit/review capability supports staging |
| GF1A-N12 | RD-08,01 | partially_covered | HO-0001,0003 | Q-13 | batch-3 method selection; trigger = user decision |
| GF1B-N13 | RD-04,05 | partially_covered | 0005,0006 | Q-03 | audit-trail capability evidence |
| GF1B-N14 | RD-09 | partially_covered | UIG-0001 | Q-07-updated | redaction exception space from RD-09 |
| GF1B-N15 | RD-03,04,05 | partially_covered | 0004,0005,0006 | Q-04 | batches 1–2 substrate core; product choice = user decision |
| GF1B-N16 | RD-01,02 | not_yet_covered | 0002,0003 | Q-05 | activation = user decision; light check later |
| GF1B-N17 | — | user_decision_not_research_fact | — | Q-06 | language policy = preference |
| GF1B-N18 | RD-11 | apparently_covered | — | — | design principle restated by motivation; no read required |
| GF1C-N19 | RD-07,08 | partially_covered | MT-0001,HO-0001 | Q-08-updated | batch-3 method selection |
| GF1C-N20 | RD-09 | partially_covered | UIG-0001 | Q-07-updated,Q-11,Q-12 | batch 3 before policy adoption |
| GF1C-N21 | RD-10 | partially_covered | FTDRE-0001,HO-0001 | Q-09-updated | batch-3 framework content; target identity = user decision |

User choices (approval granularity, language, first-target identity, storage product, handoff trigger, placement acceptance, digest sufficiency, buffer activation) stay separate from evidence.

## 10. Visual-review limitation register

Six PDF reports; none inspected in this step.

| report_id | visual_review_status | possible_unreviewed_material | may_text_only_reading_be_used | required_handling_before_visual_dependent_claim | related_domain_ids |
|---|---|---|---|---|---|
| RPT-2026Q2-0002 | pending_manual_review | unknown | yes_with_caveat | manual figure review via named index; until then flag claims text_only | RD-02,06 |
| RPT-2026Q2-0003 | pending_manual_review | unknown | yes_with_caveat | same | RD-01 |
| RPT-2026Q2-0004 | pending_manual_review | unknown | yes_with_caveat | same | RD-03,05 |
| RPT-2026Q2-0005 | pending_manual_review | unknown | yes_with_caveat | same | RD-04 |
| RPT-2026Q2-0006 | pending_manual_review | unknown | yes_with_caveat | same | RD-05,11 |
| RPT-2026Q2-0007 | pending_manual_review | unknown | yes_with_caveat | same | RD-06,02 |

The indexes state generically that tables/figures/images/layout may carry unreviewed meaning; per-report material unknown. `pdf-figure-review-index.md` is the named tracking file (metadata only; not opened).

## 11. Date-sensitivity register

external_check_performed_now: false for every item. 9 items.

| item_id | affected_report_ids | affected_domain_ids | category | why_it_may_change_or_remain_stable | evidence_cycle | refresh_before_final_STEP2_output | proposed_handling |
|---|---|---|---|---|---|---|---|
| D-01 | 0001,0003 | RD-01 | product_behavior | chat/memory features iterate quickly | 2026Q2 | uncertain | use_with_date_note |
| D-02 | 0004,0001 | RD-03 | product_behavior | coding-agent file/memory mechanics change per release | 2026Q2 | uncertain | use_with_date_note |
| D-03 | 0005,0001 | RD-04 | workflow_behavior | hosted PR/diff/permission workflows evolve | 2026Q2 | uncertain | use_with_date_note |
| D-04 | 0001,0003 | RD-01,11 | service_limit | context/memory limits change per release | 2026Q2 | uncertain | use_with_date_note |
| D-05 | 0006 | RD-05 | stable_engineering_principle | version-control/persistence principles low-drift | 2026Q2 | no | stable_enough |
| D-06 | UIG-0001 | RD-09 | stable_engineering_principle | history exposure = inherent VCS property | 2026Q2 | no | stable_enough |
| D-07 | MT-0001 | RD-07 | workflow_behavior | evaluation-practice maturity evolves with tooling | 2026Q2 | uncertain | use_with_date_note |
| D-08 | HO-0001 | RD-08 | product_behavior | handoff/memory framework APIs evolve | 2026Q2 | uncertain | use_with_date_note |
| D-09 | UIG-0001 | RD-09 | product_behavior | repository-visibility mechanics may change | 2026Q2 | uncertain | use_with_date_note |

## 12. Recommended STEP2B source set

One coherent group — ordinary conversation and project-file workflows (tool-surface capability boundaries) — 4 reports:

1. RPT-2026Q2-0001 — `raw/research-reports/cycles/2026Q2-initial/originals/AI agent 长期记忆系统 pro深度研究.txt` — foundational cross-surface boundary evidence (RD-11 + RD-01/03/04/05); txt, no visual dependency; confirms/refines/rejects S-01–S-03.
2. RPT-2026Q2-0003 — `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 2：ChatGPT,Claude 纯对话场景的外部记忆能力边界.pdf` — plain-chat boundary (RD-01), largest assumption risk for delivery commitments (GF1A-N01/N02); signals S-02/S-03; PDF: text-only with caveat, visual-dependent conclusions excluded pending review.
3. RPT-2026Q2-0004 — `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 3：Codex,Claude Code,Cursor 等本地开发 Agent 的文件式记忆能力.pdf` — local file-workflow substrate (RD-03) for GF1B-N15; signal S-04; same PDF caveat.
4. RPT-2026Q2-0005 — `raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 4：云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计.pdf` — hosted write-back/audit (RD-04) for GF1A-N07/GF1B-N13; signal S-05; same PDF caveat.

Paths copied exactly from the index. Current blob SHAs must be pinned in the STEP2B instruction before reading. The three PDFs need a separate visual check before any chart/table/image-dependent conclusion; STEP2B confines itself to text-derived claims flagged text_only, with PDF text-extraction handling specified in its instruction.

## 13. Deferred-report batches

- batch_2 (engineering basis and cross-scenario transfer): RPT-2026Q2-0006, RPT-2026Q2-0002, RPT-2026Q2-0007 — theory grounding and scenario tailoring; lower date sensitivity or downstream of boundaries.
- batch_3 (quality assurance, handoff, input handling, first-target trial evidence): RPT-2026Q2-MT-0001, RPT-2026Q2-HO-0001, RPT-2026Q2-UIG-0001, RPT-2026Q2-FTDRE-0001 — method/policy-selection evidence tied to Q-07/08/09-updated and Q-11–Q-13; needs already prompt-checked; summary signals suffice for planning.
- defer_unless_needed: none.

## 14. Incidental-exposure ledger

None. Three single-path retrievals exposed no other file; paths, task IDs, and question IDs named inside the allowed sources were metadata only (§3), never opened.

## 15. Coverage and limitations

- SHA results: all three sources verified, exact match (§1,§5).
- Complete reads: all three read in full (144/79/94 lines).
- Retrieval batteries: 3/3, one per pinned path.
- Active reports inventoried: 11/11; no additional active report found.
- Domains mapped: 11/11, each with a source plan.
- Preliminary signals: 15/16 max, each with claim-boundary note.
- PDF limitations: 6 (all initial-cycle PDFs, pending manual review).
- Date-sensitive items: 9/10 max; no external check performed.
- STEP2B selection: 4 reports (0001,0003,0004,0005).
- Deferred: 7 reports across batches 2–3.
- Limitations: initial-cycle evidence = motivation_context + report_index_metadata only (summary files exist, unopened); MT/HO/UIG signals rest on the summary index, weaker than originals; FTDRE has index metadata only; no original content claimed.
- STEP2A completed: yes.

## 16. STEP2A status determination

Determination: **GF_STEP_2A_complete_source_map_ready_for_STEP2B**. All three SHAs match; every active report inventoried; every domain has a source plan; source-strength distinctions explicit; PDF and date limitations recorded; four reports selected for STEP2B. GF-STEP-2 is not complete.

## 17. Proposed bounded STEP2B

- step_name: tool_surface_capability_boundary_original_read.
- Sources: exactly the four §12 paths, expected blob SHAs pinned in the STEP2B instruction, verified before reading; PDF text-extraction handling specified; visual-dependent conclusions forbidden pending figure review.
- Work: extract capability-boundary statements for RD-01/03/04/05/11; confirm/refine/reject S-01…S-05; record per-claim evidence class (report_text_confirmed vs visual_dependent_unverified), surface scope, evidence date; carry the date-sensitivity register forward; no design, comparison, or repair.
- Suggested limits: ≤4 paths; ≤5 batteries; per-claim register cap; soft/hard word budgets; one structural and one word-count check; stop after one file and a brief summary.
- Not executed here.

## 18. Boundary statement

This file is non-execution-source advisory evidence only. It authorizes no repository writes, no execution tasks, no execution-source updates, no reading of any original report, individual summary, or PDF, no external research, no comparison against or change to the existing design, no architecture work, and no target-project artifacts; the paused route stays paused. `current/human-approved-spec.md` remains Mnemosyne's only execution source; any conflict between this file and it is resolved in the execution source's favor and reported, never silently reconciled. GF-STEP-2A is complete; GF-STEP-2 is not complete.
