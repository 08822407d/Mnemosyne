# FABLE5-GREENFIELD-001 — GF-STEP-2B3 Local Project-File Workflow Text Evidence

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-2B3
step_name: local_project_file_workflow_report_text_evidence_review
record_type: local_project_file_pdf_text_evidence_review
authority_level: non_execution_source_advisory_evidence
author_model: Fable 5
prior_step: GF-STEP-2B2A
research_mode: false
date: 2026-07-11
source_file:
  path: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 3：Codex,Claude Code,Cursor 等本地开发 Agent 的文件式记忆能力.pdf
  expected_blob_sha: 5fe68eb33fabcecd3bc23b8a38451f03bd0bbc2e
  observed_blob_sha: 5fe68eb33fabcecd3bc23b8a38451f03bd0bbc2e
  sha_match: true
report_id: RPT-2026Q2-0004
execution_mode: full_text_mode
report_stated_evidence_date: none_stated_in_text (cycle-level period 2026Q2)
step_status: GF_STEP_2B3_complete_full_text_layer_reviewed
```

## 2. Scope and selected execution mode

Bounded text-layer review of one archived PDF. Mode decision: 4 pages (≤ ~10) and ~17,301 extracted characters (≤ ~25,000) → **Mode A full_text_mode**; complete text layer inspected. No visual-object or layout interpretation; no OCR; every conclusion text_only. Limits: paths 1/1; batteries 1/2; PDFs 1/1; evidence records 5/5 max; signal reassessed exactly S-04; boundary rows 4/4 max; linkage entries 4/4 max; limitations 3/3 max; no other reads; no web search; Research mode off; no automatic continuation.

## 3. Allowed-source and anti-contamination policy

Inputs: the STEP2B2A deliverable (used only for domain/need IDs, S-04's restated wording, and date/surface/overclaim discipline; its S-02/S-03 findings used only for the short dialogue-vs-local contrast the report itself draws) and exactly the one pinned PDF, fetched by one single-path raw-endpoint battery and SHA-verified before extraction. No other repository file or prohibited tier opened. File names, rule files, URLs, and products named inside the PDF are report-internal metadata only, none opened. No knowledge outside the report was used to update or correct it. Prior-exposure disclosure carries forward: independence by derivation and disclosure.

## 4. Source integrity and PDF text-access result

- Expected SHA `5fe68eb33fabcecd3bc23b8a38451f03bd0bbc2e`; observed identical; match: true (475,207 bytes).
- Text layer: usable — embedded CJK fonts; clean `pdftotext -layout` extraction; no OCR; no truncation.
- Size: 4 pages; ~17,301 extracted characters.
- Selected mode: full_text_mode; batteries used: 1 of 2 (single fetch + extraction, no retries).
- File size vs text volume implies rendered/graphic content may exist; visual objects not inspected.

## 5. Evidence interpretation rules

Categories: report_direct_finding, report_author_synthesis, report_recommendation, cited_external_claim_not_independently_checked, dated_product_or_workflow_statement, low_drift_engineering_principle, mixed_or_uncertain. Applied: the report is evidence, not execution source; referenced documentation unverified here; recommendations ≠ verified capabilities; statements keep the report's period and named surface; no cross-tool generalization; file access ≠ reliable memory; rule files are context, not enforcement; access, persistence, semantic correctness, authority, auditability, and portability kept separate; no training-knowledge updates; no self/model discussion; no visual inspection; no existing-design imports.

## 6. Text-layer coverage record

Complete text layer inspected: overall conclusion; Codex boundary section (rule loading, apply_patch, diff/commit, candidate memory files); Claude Code boundary section (CLAUDE.md, sessions, auto memory, hooks/permissions, file-update safety); Cursor boundary section (rules, Notepads, Agent mode, other); local-agent-vs-dialogue advantages; risk list; recommended high-trust practices; the report's own uncertainty declaration; reference list (official docs plus blog/community sources — metadata only). Not inspected: none at text level; all visual content excluded by rule. Leftover citation tokens (e.g. "【3†L19-L27】") noted, consistent with a saved research output.

## 7. Local project-file evidence register

Register-wide: text_only = true; visual_review_status = not_performed; source_evidence_date_or_period = none stated in text, cycle 2026Q2; underlying citations unverified. 5 items.

| evidence_id | source_anchor | concise_statement | evidence_category | named_product_or_workflow_scope | confidence_as_report_evidence | date_sensitivity | access_persistence_correctness_distinction | related_research_domain_ids | related_STEP1_need_ids | supports_or_challenges_S04 | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F2B3-E01 | 总体结论; 优势 pp.1,3 | local dev agents fit file-based external memory better than dialogue: direct file/repo/terminal access; layered rule files loaded at startup; memory files version-controlled with Git diffs for audit and rollback | report_author_synthesis | Codex CLI, Claude Code, Cursor | high | high | access and persistence strong; correctness not addressed by access | RD-03 | GF1B-N15; GF1A-N09 | supports (context) | overclaim: "better suited" ≠ automatic reliable memory |
| F2B3-E02 | Codex 能力边界 p.1 | Codex loads layered AGENTS.md (global, project, parents; first non-empty per directory, top-down merge); apply_patch edits any file with an automatic Git commit per patch; /diff and /review for inspection; no auto-update of existing remote PRs; no built-in memory-management logic — which files are "memory" is user/team convention; recommended flow patch → user review → commit | cited_external_claim_not_independently_checked | Codex CLI | high | high | patch writes automatic; persistence via Git; memory semantics purely convention | RD-03 | GF1B-N15; GF1A-N07,N11 | supports | auto-commit ≠ reviewed acceptance; preliminary S-05 corroboration only |
| F2B3-E03 | Claude Code 能力边界 pp.1–2 | CLAUDE.md read each session (user/project levels, @imports, subdirectory scoping) but is best-effort guidance — enforcement comes from client-side permissions/sandbox (permissions.deny, hooks); sessions saved locally and resumable, yet conversation history does not auto-carry — a new session gets only CLAUDE.md plus a memory summary; auto memory (~/.claude/projects/<project>/memory/, MEMORY.md, first 200 lines/25KB loaded) is machine-local, no cloud or cross-device sync | cited_external_claim_not_independently_checked | Claude Code | high | high | access high; persistence machine-scoped; compliance best-effort | RD-03 | GF1B-N15; GF1A-N09,N12 | supports strongly | instruction file ≠ enforcement; local memory ≠ portable memory |
| F2B3-E04 | Cursor 能力边界 p.2 | Cursor uses .cursor/rules/ (.mdc activation modes) plus AGENTS.md compatibility; Notepads are manually maintained context in a local SQLite store, not Git-managed, with deprecation planned (important content should be versioned as files); no built-in auto-memory database; no built-in Git commit — patches applied by the user | cited_external_claim_not_independently_checked | Cursor | medium | high | rules give access-time context; persistence weak and local; no memory subsystem | RD-03 | GF1B-N15; GF1A-N10 | supports | community-sourced parts flagged uncertain by the report itself |
| F2B3-E05 | 风险; 推荐实践 pp.3–4 | risks: agents may mis-edit or delete memory files under loose auto-approval; conflicting rule files yield unpredictable behavior; local memories do not cross devices; over-broad default permissions; memory rot (stale/vague entries ignored or misused). recommended practices: Git-manage all instruction files; patch/diff review before commit; human confirmation of memory updates; protected or read-only paths; short, layered, versioned rules with a single source of truth | mixed_or_uncertain | local dev agents generally | high | medium | authority, review, and quality controls are not provided by access — they must be added | RD-03; RD-04 (adjacent) | GF1A-N07,N11,N04; GF1B-N15 | supports (mirrors the "additionally requires" clause) | recommendations ≠ measured failure data |

## 8. S-04 reassessment

- signal_id: S-04. previous_wording: local coding-agent file access is a prerequisite, not automatic reliable memory; reliable continuity additionally requires an explicit source of truth, write-back rules, review or audit, conflict handling, user confirmation where authority is involved, and a handoff or state-recovery mechanism.
- Disposition: **dedicated_report_refines**.
- replacement_wording_if_refined: on local development agents (2026Q2; Codex CLI, Claude Code, Cursor), file access and layered instruction loading are prerequisites, not reliable memory: instruction files are best-effort context while enforcement exists only in client-side permission/sandbox configuration; built-in memories (Claude Code auto memory, Cursor Notepads) are machine-local and non-synced; which files count as memory is user convention; sessions resume but conversation history does not auto-carry. Reliable continuity therefore additionally requires an explicit Git-versioned source of truth, patch/diff review before commit, human-confirmed memory updates, protected paths, conflict-free short layered rules, and an explicit handoff/state-recovery mechanism.
- supporting_F2B3_evidence_ids: E01–E05. named_tool_and_surface_scope: Codex CLI, Claude Code, Cursor local workflows.
- access_vs_memory_distinction: access and patching are automatic; memory semantics, compliance, portability, quality, and authority are not resolved by access.
- report_date_caveat: no self-stated date; cycle-level 2026Q2; mechanics volatile. remaining_visual_dependency: none identified for these claims; visuals unreviewed. remaining_current_fact_refresh_dependency: yes (STEP2A D-02). remaining_original_report_dependency: RPT-2026Q2-0005 (hosted write-back/audit), 0006.
- prohibited_overclaim: never "local coding agents provide reliable memory automatically."
- S-01/S-02/S-03/S-05 not reassessed; E02/E05 give S-05 preliminary corroboration only — 0005 remains its dedicated source.

## 9. Compact workflow-boundary table

| boundary_id | workflow_or_file_type_as_named_in_report | report_text_supported_role | what_it_does_not_guarantee | automation_level | evidence_date_or_period | date_sensitivity | visual_dependency |
|---|---|---|---|---|---|---|---|
| B-1 | AGENTS.md hierarchy (Codex; Cursor-compatible) | layered startup instruction loading, global-to-project merge | compliance or semantic consistency | automatic | 2026Q2 | high | none_identified |
| B-2 | CLAUDE.md (+ subdirectory scoping, imports) | per-session persistent instructions | enforcement — best-effort only; vague/conflicting rules unreliable | automatic | 2026Q2 | high | none_identified |
| B-3 | Claude Code auto memory (MEMORY.md set) | auto-written, auto-loaded cross-session project summary | cross-device availability; content quality without review | mixed | 2026Q2 | high | none_identified |
| B-4 | Codex apply_patch + auto-commit + /diff; Cursor Notepads | patch-based edits with local commits and diff review; local notepad context | remote-PR updates; reviewed acceptance; Git management of Notepads (deprecation planned) | mixed | 2026Q2 | high | none_identified |

## 10. Minimal STEP-1 linkage delta

| need_id | coverage_change | supporting_evidence_ids | remaining_report_dependency | user_decision_not_resolved |
|---|---|---|---|---|
| GF1B-N15 | strengthened: concrete substrate mechanics — layered rule loading, patch edits with Git commits, protected-path configuration | F2B3-E01,E02,E03 | 0005, 0006 | Q-04 storage product |
| GF1A-N09 | strengthened: built-in agent memories are machine-local and non-synced, reinforcing external versioned files as the portable state source | F2B3-E03,E04 | 0006 | — |
| GF1A-N10 | strengthened: cross-tool AGENTS.md format vs tool-specific rules and deprecating Notepads evidence the adapter/migration need | F2B3-E02,E04 | 0007, 0006 | — |
| GF1A-N11 | strengthened: patch → diff review → commit and human-confirmed memory updates corroborate staged, reviewed construction | F2B3-E02,E05 | 0005 | Q-02 approval granularity |

## 11. Visual, date, and remaining-coverage limitations

1. Visual content unreviewed: 475 KB file vs ~17 K characters of text implies graphic content may exist; all conclusions text_only; figure/table/layout meaning unverified pending the repository's manual figure review (index not opened).
2. Dating and sourcing: no evidence date stated in the text — cycle-level 2026Q2 only; product mechanics volatile (STEP2A D-02); citations mix official docs with blog and community sources, all unverified here; the report's own uncertainty declaration flags community-inferred parts (notably Cursor futures).
3. Feature-vs-practice boundary: the high-trust practices section is recommendation, not observed product behavior; the auto-commit vs reviewed-acceptance distinction rests on text reading alone.

## 12. Status determination and bounded continuation

Determination: **GF_STEP_2B3_complete_full_text_layer_reviewed**. Full text layer inspected in Mode A; STEP2B3B is unnecessary — no relevant text remains unread. Proposed next report step (not executed): a bounded review of RPT-2026Q2-0005 only (`raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 4：云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计.pdf`), expected blob SHA pinned in its instruction; same PDF text-only rules and mode gate; ≤2 batteries; small evidence register; reassessment focused on S-05. GF-STEP-2 is not complete.

## 13. Boundary statement

This file is non-execution-source advisory evidence only. It authorizes no repository writes, no execution tasks, no execution-source updates, no reading of any other report, summary, prompt, index, or PDF, no OCR or visual interpretation, no external research, no model or vendor evaluation, no comparison against or modification of the existing design, no architecture work, and no target-project artifacts; the paused route stays paused. `current/human-approved-spec.md` remains Mnemosyne's only execution source; any conflict between this file and it is resolved in the execution source's favor and reported, never silently reconciled. GF-STEP-2B3 is complete; GF-STEP-2 is not complete.
