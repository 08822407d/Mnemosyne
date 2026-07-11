# FABLE5-GREENFIELD-001 — GF-STEP-2B2A Plain-Dialogue Report Core Text Evidence

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2B2A
step_name: plain_dialogue_report_core_text_evidence_review
record_type: plain_dialogue_pdf_core_text_evidence_review
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-2B1
research_mode: false
date: 2026-07-11
source_file:
  path: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 2：ChatGPT,Claude 纯对话场景的外部记忆能力边界.pdf
  expected_blob_sha: a1146ad6bfee5cbdc431f35fb0b7a442e162aab7
  observed_blob_sha: a1146ad6bfee5cbdc431f35fb0b7a442e162aab7
  sha_match: true
report_id: RPT-2026Q2-0003
execution_mode: full_text_mode
report_stated_evidence_date: none_stated_in_text (cycle-level period 2026Q2)
step_status: GF_STEP_2B2A_complete_full_text_layer_reviewed
```

## 2. Scope and selected execution mode

Bounded text-layer review of one archived PDF. Mode decision: 5 pages (≤ ~30) and extracted text ~16,924 characters / ~394 space-separated tokens (≪ ~12,000 words) → **Mode A full_text_mode**; the complete text layer was inspected. No image, chart, table-as-visual, or layout interpretation; no OCR; every conclusion is text_only. Limits: paths 1/1; batteries 1/2; PDFs 1/1; evidence records 6/6 max; signals reassessed exactly S-02 and S-03; surface/date rows 5/5 max; uncertainty items 3/3 max; no other report/summary/prompt; no web search; Research mode off; no automatic continuation.

## 3. Allowed-source and anti-contamination policy

Inputs: the STEP2B1 deliverable (used only for S-02/S-03 wording, F2B1-E02…E05, domain/need IDs, and date/surface/overclaim discipline) and exactly the one pinned PDF, fetched by one single-path raw-endpoint battery (URL-encoded path) and SHA-verified before extraction. No other repository file or prohibited tier was opened. References inside the PDF (help-center article names, URLs, product names, Claude Code paths) are report-internal metadata only, none opened. No knowledge outside the report was used to update or correct it. Prior-exposure disclosure carries forward: independence by derivation and disclosure.

## 4. Source integrity and PDF text-access result

- Expected SHA `a1146ad6bfee5cbdc431f35fb0b7a442e162aab7`; observed identical; match: true (457,024 bytes).
- Text layer: usable — embedded CJK fonts present; `pdftotext -layout` extraction clean; no OCR needed; no truncation.
- Size: 5 pages; ~16,924 extracted characters.
- Selected mode: full_text_mode; batteries used: 1 of 2 (single fetch + extraction; no retries).
- Note: file size vs text volume implies rendered/graphic content may exist; visual objects were not inspected.

## 5. Evidence interpretation rules

Categories: report_direct_finding, report_author_synthesis, report_recommendation, cited_external_claim_not_independently_checked, dated_product_or_workflow_statement, low_drift_engineering_principle, mixed_or_uncertain. Applied: the report is evidence, not execution source; its cited help-center sources stay unverified here; statements keep their surface and period; no product-mode generalization; absence of a documented feature is not impossibility; recommendations are not capability facts; no training-knowledge updates; no self/model discussion; no visual inspection; no existing-design imports.

## 6. Text-layer coverage record

Complete text layer inspected: overall conclusion; ChatGPT boundary section (file reading, GitHub reading, GitHub write-back, Projects memory, Tasks/Agent/Apps); Claude boundary section (Projects/knowledge base, file reading, external write-back, Claude Code contrast); the four automation-tier sections (fully automatic / semi-automatic / manual / requires API-MCP-scripts-external tools); five cross-conversation relay recommendations; reference list (citation URLs recorded as metadata only). Portions not inspected: none at text level; all visual content excluded by rule. One extraction artifact noted: a leftover citation token "【5†L137-L142】", consistent with a saved research output.

## 7. Core text evidence register

Register-wide: text_only = true; visual_review_status = not_performed; source_evidence_date_or_period = none stated in text, cycle 2026Q2; underlying citations unverified. 6 items.

| evidence_id | source_anchor | concise_statement | evidence_category | interaction_surface | confidence_as_report_evidence | date_sensitivity | related_STEP2B1_evidence_ids | related_research_domain_ids | related_STEP1_need_ids | prohibited_overclaim |
|---|---|---|---|---|---|---|---|---|---|---|
| F2B2A-E01 | 总体结论 p.1 | in pure-dialogue entry (web/app) automated external memory is very limited: no background cross-session read/write; reading via manual upload or authorized connectors; write-back nearly always user-mediated or unsupported; Projects give bounded cross-session context, not background storage | report_author_synthesis | ChatGPT + Claude dialogue | high | high | F2B1-E02,E05 | RD-01 | GF1A-N01,N02,N09 | "very limited" ≠ impossible with external tooling |
| F2B2A-E02 | ChatGPT GitHub 读取/写回 p.1 | ChatGPT GitHub app: authorized read/search of repo content; repo-level search only, no exact-filename query; write-back unsupported per official docs — pushes require Codex or GitHub API via user scripts | cited_external_claim_not_independently_checked | ChatGPT dialogue + GitHub connector | high | high | F2B1-E03 | RD-01 | GF1A-N02 | one connector snapshot, not all apps or futures |
| F2B2A-E03 | ChatGPT Projects/Tasks/Agent/Apps pp.1–2 | Projects: project-scoped memory over chats+files with plan file limits (free 5, Plus/Pro 25–40) and project-only-memory mode, no cross-project sync; Tasks: scheduled prompts, no uploads or external writes; Agent: tool-mediated writes with per-action user confirmation; Apps: admin-enabled writes, confirmed per action | cited_external_claim_not_independently_checked | ChatGPT dialogue | high | high | F2B1-E04 | RD-01 | GF1A-N02,N12 | "Agent can write" ≠ unattended auto write-back |
| F2B2A-E04 | Claude 能力边界 p.2 | Claude Projects: knowledge base prioritized, paid RAG expansion near context limit, uploads bounded by context window; GitHub integration read-side with manual Sync; no documented auto file-write or GitHub push; Google-ecosystem connector writes each user-confirmed (draft-not-send email, calendar, Drive save); Claude Code auto memory (.claude/, MEMORY.md, rules/) exists only in that separate environment, not the chat UI | cited_external_claim_not_independently_checked | Claude dialogue | high | high | F2B1-E05 | RD-01 | GF1A-N02,N09 | absence of a documented feature ≠ impossibility |
| F2B2A-E05 | 自动/半自动/人工/工具 pp.3–4 | task-step stratification: automatic = connector reads, project-context persistence, Agent execution, scheduled tasks, Drive source sync; semi-automatic = AI-drafted memory updates user-merged, per-action write confirmations, manual Sync; manual = uploads, copy-paste of updates, OAuth authorization, approvals, project setup; automated writes to GitHub/DB, custom MCP connectors, and pipelines require API/scripts/Actions | report_author_synthesis | ChatGPT + Claude dialogue | high | high | F2B1-E02,E04,E13 | RD-01 | GF1A-N01,N07,N09 | stratification is a 2026Q2 snapshot, not permanent |
| F2B2A-E06 | 跨对话接力建议 pp.4–5 | recommended relay patterns: quick handoff card; full handoff package uploaded as file; project knowledge base as hub; manually pasted structured memory (e.g. JSON); external storage (Drive/GitHub) as intermediary — externalize memory/handoff as user-maintained documents, AI generates and references | report_recommendation | ChatGPT + Claude dialogue | high | low | F2B1-E08,E13 | RD-01,RD-08 (corroboration) | GF1A-N12,N07 | recommendation ≠ measured effectiveness |

## 8. S-02 and S-03 reassessment

- signal_id: S-02. Disposition: **dedicated_report_refines**. Replacement wording: on plain ChatGPT and Claude dialogue surfaces (2026Q2 evidence; this report states no exact date), repository/file write-back is not native — ChatGPT's GitHub app is read-only without exact-filename search; Claude connectors offer no GitHub write path, and Google-ecosystem writes require per-action user confirmation; ChatGPT Agent/Apps writes are admin/config-gated and per-action confirmed; Tasks cannot write externally; automated write-back requires external API/MCP/scripts/Actions. Supporting: F2B2A-E01…E05. Surface scope: ChatGPT + Claude web/app dialogue plus their official connectors. Date caveat: cycle-level 2026Q2 only; volatile. Remaining visual dependency: none identified for these text claims; visuals unreviewed. Refresh dependency: yes (STEP2A D-01). Overclaim: never "chat can never write files."
- signal_id: S-03. Disposition: **dedicated_report_confirms**. Supporting: F2B2A-E01,E03,E04,E06. Text adds: Projects are bounded containers (file limits, context-window bounds, no cross-project/session auto-sync), and the report's own recommendation is to externalize memory into user-maintained documents. Scope note: this report treats Projects-type containers in depth; account-level memory features appear only in the overall claim that the assistants cannot themselves remember across sessions — the auditability/migratability/rollback dimensions of S-03 continue to rest on F2B1-E14. Date caveat: 2026Q2. Visual dependency: none identified. Refresh: yes (D-01/D-04). Overclaim: "auxiliary" ≠ "useless."
- S-01, S-04, S-05: not reassessed here.

## 9. Compact surface-and-date register

| item_id | product_or_surface_as_named_in_report | report_text_statement | evidence_date_or_period | volatility | may_enter_final_STEP2 | visual_dependency |
|---|---|---|---|---|---|---|
| R-1 | ChatGPT GitHub app | read/search only; no writes, commits, or exact-filename search | 2026Q2 | high | text_evidence_with_date_caveat | none_identified |
| R-2 | ChatGPT Projects | project-scoped memory; plan file limits (5 / 25–40); project-only-memory mode; no cross-project sync | 2026Q2 | high | needs_later_refresh | none_identified |
| R-3 | ChatGPT Tasks / Agent / Apps | Tasks no uploads/external writes; Agent and Apps writes per-action confirmed, admin-gated | 2026Q2 | high | text_evidence_with_date_caveat | none_identified |
| R-4 | Claude Projects + connectors | knowledge base + paid RAG expansion; GitHub read with manual Sync; Google-ecosystem writes confirmed per action; no GitHub write | 2026Q2 | high | text_evidence_with_date_caveat | none_identified |
| R-5 | Claude Code (contrast only) | auto memory via .claude/ files exists only in that environment, not the chat UI | 2026Q2 | medium | text_evidence_with_date_caveat | none_identified |

## 10. Minimal STEP-1 linkage delta

| need_id | coverage_change | supporting_evidence_ids | remaining_report_dependency | user_decision_not_resolved |
|---|---|---|---|---|
| GF1A-N01 | strengthened: durable memory on dialogue surfaces works only as externalized, user-maintained documents plus bounded platform containers | F2B2A-E01,E05,E06 | 0004, 0005, 0006 | — |
| GF1A-N02 | strengthened: per-surface, confirmation-gated write boundaries sharpen honest capability claims | F2B2A-E02,E03,E04,E05 | 0004, 0005 | — |
| GF1A-N09 | strengthened: report's own recommendation externalizes state; platform containers bounded by context windows | F2B2A-E01,E04,E06 | 0006 | — |
| GF1A-N12 | strengthened: handoff-card / handoff-package / project-hub relay patterns corroborate manual handoff as the reliable dialogue mechanism | F2B2A-E06 | HO-0001 (batch 3) | Q-13 trigger choice |

## 11. Visual, date, and remaining-coverage limitations

1. Visual content unreviewed: 457 KB file vs ~17 K characters of text implies graphic/rendered content may exist; every conclusion here is text_only; figure/table/layout meaning remains unverified pending the manual review tracked by the repository's figure-review index (not opened).
2. Dating: the text states no evidence date; all product statements carry only the cycle-level 2026Q2 period and are volatile (STEP2A D-01/D-04 refresh path); all cited help-center URLs are unverified report-internal metadata.
3. Coverage note: account-level memory features are only glancingly treated in the text, so parts of S-03 (auditability, export, rollback) continue to rest on STEP2B1 evidence rather than this report.

## 12. Status determination and bounded continuation

Determination: **GF_STEP_2B2A_complete_full_text_layer_reviewed**. Full text layer inspected in Mode A; no STEP2B2B is needed — no relevant text remains uncovered. Proposed next report-reading step (not executed): GF-STEP-2B3 on RPT-2026Q2-0004 (`raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 3：Codex,Claude Code,Cursor 等本地开发 Agent 的文件式记忆能力.pdf`), expected blob SHA to be pinned in its instruction; same PDF text-only rules, mode gate, ≤2 batteries, small evidence register, and reassessment focused on S-04. GF-STEP-2B2 and GF-STEP-2 are not complete.

## 13. Boundary statement

This file is non-execution-source advisory evidence only. It authorizes no repository writes, no execution tasks, no execution-source updates, no reading of any other report, summary, prompt, or PDF, no OCR or visual interpretation, no external research, no model or vendor evaluation, no comparison against or modification of the existing design, no architecture work, and no target-project artifacts; the paused route stays paused. `current/human-approved-spec.md` remains Mnemosyne's only execution source; any conflict between this file and it is resolved in the execution source's favor and reported, never silently reconciled. GF-STEP-2B2A is complete; GF-STEP-2B2 and GF-STEP-2 are not complete.
