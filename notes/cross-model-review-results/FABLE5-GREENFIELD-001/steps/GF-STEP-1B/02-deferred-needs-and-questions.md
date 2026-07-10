# FABLE5-GREENFIELD-001 — GF-STEP-1B Deferred Needs and Consolidated Questions

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-1B
step_name: deferred_origin_need_extraction_and_question_consolidation
record_type: independent_need_model_continuation
authority_level: non_execution_source_advisory_evidence
step_status: STEP1B_complete_GF_STEP_1_not_complete
author_model: Fable 5
prior_step: GF-STEP-1A
date: 2026-07-10
source_file: raw/concept-origin-extract-001.md
source_ref: master
source_blob_sha_expected: b47248f1052ecac679c2e3a0afab4d93ca2c6649
source_blob_sha_verified: true
source_language: zh-CN
allowed_attachment: FABLE5-GREENFIELD-001-STEP1A-core-needs-pilot.md
```

## 2. Scope and workload limits

Bounded continuation of GF-STEP-1; GF-STEP-1 remains incomplete. This substep is governed by its self-contained instruction; no charter retrieval was performed or permitted. Limits observed: new records 6 of 8; repository retrieval batteries 0 of 2; repository paths 1 of 1; no web search; no Research mode; word-budget policy applied (one post-write approximate count; within the 2,200 hard cap); no automatic continuation into GF-STEP-1C.

## 3. Allowed sources and anti-contamination policy

Two inputs only: the GF-STEP-1A deliverable (read from this conversation's outputs) and `raw/concept-origin-extract-001.md`. Source access mode: the local copy retained from the GF-STEP-1A single-path fetch in this same conversation was re-verified by computing its git blob SHA, which equals the expected `b47248f1052ecac679c2e3a0afab4d93ca2c6649`; content identity to `master` is therefore proven and no new repository query was issued. No `current/**`, `handoff/**`, `notes/**`, `commands/**`, `manual-import-inbox/**` path, research material, MNEMOSYNE result, FABLE5 review/triage output, or GPT design artifact was read or searched. Confirmed methodology applied: 理由和考量 blocks are used only as compiler-attributed motivation or context, never as standalone user statements; 助手核心回应 material appears only in the mechanism register. The STEP1A provenance caveat carries forward: the source is a compiled near-original extract (`is_full_transcript: false`, `v2_reason_enriched`), not a transcript.

## 4. Prior-step linkage and non-duplication rule

GF1A-N01 through GF1A-N12 stand unmodified; numbering continues at GF1B-N13. Overlap handling: GF1B-N13/N14 concern the raw layer's compilation content and edit discipline, distinct from GF1A-N06 (preservation plus per-model digests) and GF1A-N07 (human-confirmed layer); GF1B-N18 records the compiler-authored usage-boundary consolidation, whose load-bearing principle is already user-origin in GF1A-N07. During linkage checking, the GF1A-N12 anchor was re-verified against §15 of the source: the quoted user text is present; the anchor is accurate. No 1A record required correction.

## 5. Deferred-theme need inventory

- need_id: GF1B-N13
- need_title: evolution_evidence_with_assistant_commentary_and_reasons
- source_anchor: §16 用户近原文 — “不仅应该包含用户的构想和意见原文，也需要包含助手的相应评论和建议”；§0 — “最好尽量包含提出各种构想细节的理由”
- source_class: user_origin_evidence
- interpreted_need: The raw evidence layer preserves the idea-evolution process near-verbatim: user ideas and corrections, the reasons behind them, and the concept-time assistant commentary that shaped later thinking — not a summary.
- motivation_or_fear: Summaries lose why designs were adopted; the user may forget a requirement's background; some rules are defenses against tool-capability limits; some TODOs come from strong real pain (reasons layer).
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: How much assistant commentary is enough; near-original sufficiency vs full transcript remains open (Q-03).
- possible_prior_exposure_echo: false
- derivation_note: Inclusion rule stated directly by the user in §16 and reinforced in §0; the itemized reasons taxonomy is compiler-attributed.

- need_id: GF1B-N14
- need_title: minimal_edit_discipline_for_raw_compilation
- source_anchor: §16 用户近原文 — “允许删除几乎完全重复内容，但希望不要做更多修改…保留连贯版本，删除回顾重述版本”
- source_class: user_origin_evidence
- interpreted_need: Raw compilation edits are limited to removing near-duplicates; when deduplicating, the version in the more coherent context is kept and retrospective restatements are dropped; no further modification is permitted.
- motivation_or_fear: Protect the evidentiary fidelity of the raw layer so evolution evidence stays trustworthy (reasons layer).
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: The “几乎完全重复” threshold is left to compiler judgment; no user-stated test.
- possible_prior_exposure_echo: false
- derivation_note: A concrete user-origin curation policy, distinct from GF1A-N06’s preservation principle.

- need_id: GF1B-N15
- need_title: versioned_auditable_file_substrate_across_scenarios
- source_anchor: §4 用户近原文 — “如果所有使用场景都使用 GitHub 或类似工具存储，是否也能提升各场景下自动化记忆程度？”
- source_class: user_origin_evidence
- interpreted_need: Long-term memory artifacts across scenarios — not only development — should gain versioning, diff/review, audit trail, a shared traceable external state, and reduced manual maintenance from a file-plus-VCS-style substrate. Whether GitHub specifically becomes the unified base was posed as an exploration, not a decision.
- motivation_or_fear: Reuse mature automation (triggers, workflows) instead of bespoke storage; let different agents and models share one traceable external state (reasons layer).
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: GitHub-specificity vs any equivalent substrate; per-scenario applicability; the sensitive-content-to-cloud boundary for non-dev scenarios (Q-04).
- possible_prior_exposure_echo: false
- derivation_note: The user’s own “或类似工具” keeps the mechanism open; the Levels 0–6 ladder and capability caveats are assistant_origin (M-01, M-04).

- need_id: GF1B-N16
- need_title: low_friction_idea_capture_buffer
- source_anchor: §9 用户近原文 — “突然跳出来的想法需要速记和单独存储…暂时作为 TODO”
- source_class: user_origin_evidence
- interpreted_need: A capture layer for fleeting, rough ideas, stored separately so they never pollute formal requirements; the need is affirmed but its detailed design is deferred until the workspace exists and external device/tool cooperation is settled.
- motivation_or_fear: Poor memory; ideas vanish quickly or crowd each other out; rough ideas are unfit for direct entry into originals or implementation.
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: Capture channels, tooling, and activation timing undefined (Q-05); the three-class intake split (formal needs / usage feedback / temporary ideas) is compiler-attributed.
- possible_prior_exposure_echo: false
- derivation_note: The layer-0 pipeline (capture→triage→dedup→user confirmation) and the v0.1 exclusion are assistant_origin (M-02).

- need_id: GF1B-N17
- need_title: chinese_first_language_policy_with_ascii_exceptions
- source_anchor: §12 用户近原文 — “最好全部采用中文，除了文件名、路径名、命令等天然适合英文的内容”
- source_class: user_origin_evidence
- interpreted_need: All repository body text in Chinese; naturally-English artifacts (filenames, paths, commands and similar) stay English; any future switch to English or bilingual happens only deliberately, after fluency or careful bilingual design.
- motivation_or_fear: Stated by the user: Chinese is the current working language; repeated read/write plus translation risks semantic drift; bilingual duplication wastes space. Reasons layer adds: long-term review cognitive load and subtle-meaning stability.
- confidence: high
- stability_assessment: evolving
- unresolved_ambiguity: Migration trigger and criteria undefined (Q-06); the extended exception enumeration (IDs, status values, YAML keys, Git terms, product names) is assistant elaboration.
- possible_prior_exposure_echo: false
- derivation_note: Documented in-source user self-correction: an initial bilingual lean was revised to Chinese-first; the dedicated migration process is assistant_origin (M-03).

- need_id: GF1B-N18
- need_title: bounded_purpose_raw_usage_with_spec_precedence
- source_anchor: §17（compiler-authored usage note）— “本文件不应用于：直接替代 `current/human-approved-spec.md`…应以 `current/human-approved-spec.md` 为准”
- source_class: mixed_or_uncertain
- interpreted_need: The extract is bounded-purpose evidence — usable for model migration, session handover, requirement re-verification, dedup, motivation review, and source citation — and must never substitute for or auto-overwrite the human-confirmed execution layer; conflicts resolve to the execution source and are logged as open questions or reconciliations.
- motivation_or_fear: Prevent raw history from being executed as current decision.
- confidence: medium
- stability_assessment: stable_looking
- unresolved_ambiguity: §17 has no 用户近原文 block; explicit user review of this enumerated allow/deny list is not evidenced in this file.
- possible_prior_exposure_echo: false
- derivation_note: Classified mixed because the enumeration is compiler-authored while its core principle is already user-origin (GF1A-N07); recorded for provenance completeness, not as a new user statement.

## 6. Assistant-era mechanism register

- mechanism_id: M-01 | short_description: Git adoption ladder Levels 0–6, from local Markdown to controlled write-back via MCP/API | source_section: §4 | relationship_to_user_need: candidate mechanism menu for GF1B-N15’s substrate properties | status: context_only_not_user_approved | must_not_be_treated_as_requirement: true
- mechanism_id: M-02 | short_description: idea-buffer “layer 0” pipeline: capture→hold→periodic triage→dedup→status marking→user confirmation; excluded from v0.1 | source_section: §9 | relationship_to_user_need: implements GF1B-N16 | status: context_only_not_user_approved | must_not_be_treated_as_requirement: true
- mechanism_id: M-03 | short_description: dedicated language-migration process for any future English/bilingual switch, plus extended English-exception enumeration | source_section: §12 | relationship_to_user_need: operationalizes GF1B-N17’s future-switch clause | status: context_only_not_user_approved | must_not_be_treated_as_requirement: true
- mechanism_id: M-04 | short_description: capability caveats: chat windows cannot auto-write repositories; automation requires Codex/Claude Code/Actions/MCP/scripts or manual action; sensitive content not sent to cloud agents; non-dev scenarios need no full PR/CI at first | source_section: §4 | relationship_to_user_need: feasibility bounds on GF1B-N15, consistent with GF1A-N02’s honesty demand | status: context_only_not_user_approved | must_not_be_treated_as_requirement: true
- mechanism_id: M-05 | short_description: compilation-time restatement of the three-truths split (historical evidence / candidate understanding / current execution) | source_section: §0 整理说明 | relationship_to_user_need: mirrors user-origin GF1A-N06/N07; itself compiler-authored | status: mixed_or_uncertain | must_not_be_treated_as_requirement: true

## 7. Consolidated unresolved-question list

Resolved since STEP1A: UQ-1 is closed by this substep’s confirmed methodology (理由和考量 = compiler-attributed motivation only); UQ-4 is closed for this substep (the instruction is self-contained; no charter retrieval permitted). Open questions:

- question_id: Q-01（carried from STEP1A UQ-2）
- related_need_ids: GF1A-N05
- question_for_user: Does any raw evidence outside prohibited tiers record your acceptance or amendment of the dual-layer design-record placement proposal?
- why_load_bearing: Placement decides how cross-project accumulation and target-runtime fidelity are reconciled; assuming acceptance would convert an assistant-era proposal into a requirement.
- can_design_continue_without_answer: partially
- temporary_handling: Placement stays an open design variable; only the tension in GF1A-N05 is treated as need.

- question_id: Q-02（carried from STEP1A UQ-3）
- related_need_ids: GF1A-N07, GF1A-N08
- question_for_user: What approval granularity do you intend for the human-confirmed layer — per need, per batch, or per release?
- why_load_bearing: Gate design and the reconciliation flow both depend on confirmation granularity.
- can_design_continue_without_answer: partially
- temporary_handling: Granularity is modeled as an explicit parameter with no default.

- question_id: Q-03
- related_need_ids: GF1B-N13, GF1A-N06
- question_for_user: Is the near-original extract sufficient as the founding evidence layer, or should full transcripts/originals also be archived later? (§16 states the file is not a full transcript; §18 itself proposes logging this as an open question.)
- why_load_bearing: Sets the evidence ceiling for future re-derivation and for migration-time re-analysis depth (GF1A-N10).
- can_design_continue_without_answer: partially
- temporary_handling: The current extract is treated as the only guaranteed evidence; transcript archiving stays unsettled.

- question_id: Q-04
- related_need_ids: GF1B-N15
- question_for_user: Which substrate properties (versioning, diff review, audit, shared traceable state) are hard requirements across scenarios — and is GitHub itself required, or is any equivalent substrate acceptable, given the sensitive-content boundary for non-dev scenarios?
- why_load_bearing: Determines whether the need model encodes properties or a specific product.
- can_design_continue_without_answer: partially
- temporary_handling: Only properties are encoded; GitHub remains a candidate mechanism (M-01).

- question_id: Q-05
- related_need_ids: GF1B-N16
- question_for_user: What conditions (tooling, external-device workflow, workspace maturity) unblock the deferred idea-buffer design, and which capture channels are in scope?
- why_load_bearing: Affects intake-layer completeness of the need model.
- can_design_continue_without_answer: yes
- temporary_handling: Recorded as an affirmed-but-deferred need.

- question_id: Q-06
- related_need_ids: GF1B-N17
- question_for_user: What would trigger the future English/bilingual switch, and does the extended English-exception list (beyond filenames, paths, commands) match your intent?
- why_load_bearing: The language of long-lived artifacts shapes every layer’s readability contract.
- can_design_continue_without_answer: yes
- temporary_handling: Chinese-first is assumed for all designed artifacts; migration only via a dedicated process if ever triggered.

## 8. Incidental-exposure ledger

No incidental prohibited-tier exposure occurred in GF-STEP-1B: no repository query was issued, and only the SHA-verified local source copy and the STEP1A deliverable were read. STEP1A entries E-1 and E-2 remain on record in the prior deliverable.

## 9. Coverage ledger

- Deferred themes inspected: §0, §4, §9, §12, §16, §17 — the full STEP1A-deferred set.
- Converted into records: §16 → GF1B-N13, GF1B-N14 (with §0 co-anchoring N13); §4 → GF1B-N15; §9 → GF1B-N16; §12 → GF1B-N17; §17 → GF1B-N18.
- Inspected but not extracted: §0 整理说明 (compiler restatement, registered as M-05); §15 (re-read solely to verify the GF1A-N12 anchor during linkage checking; anchor confirmed; no record created); §18 (read only for the Q-03 cross-reference permitted by the instruction; no record created).
- Retrieval batteries used: 0 of 2 (local copy, git blob SHA verified against the expected value).
- Record allowance remaining: 2 of 8 unused; no records were added to fill the allowance.
- Why GF-STEP-1 is still incomplete: the charter’s research-prompt-index input layer is unprocessed (designated for GF-STEP-1C); the unified need model and final question resolution with the user are pending; load-bearing questions Q-01 through Q-04 remain open.

## 10. Proposed bounded GF-STEP-1C (not executed)

- step_name: research_prompt_index_need_extraction_and_step1_assembly.
- Scope: extract user-origin needs and constraints evidenced by the research-prompt index (what the user commissioned research on reveals priorities, fears, and capability concerns); distinguish prompt-embedded assumptions from needs; then assemble the unified GF-STEP-1 need model (GF1A-N01…GF1B-N18 plus 1C records) and the final consolidated question list, declaring GF-STEP-1 complete or listing residual gaps.
- Allowed source: the charter-designated research-prompt-index file, path and expected blob SHA to be pinned in the 1C instruction (recorded during STEP1A charter recovery as `raw/research-reports/current/current-research-prompts.md`; to be confirmed in that instruction). Research reports themselves stay excluded unless the user widens scope.
- Supporting in-source context: §18 states research reports serve as “证据和能力边界来源，不直接作为执行源”, and §15’s reasons layer attributes the intent to use them as high-weight evidence — consistent with an evidence-layer 1C, not design work.
- Limits: ≤8 new records (GF1C-N19…); ≤2 retrieval batteries; 1 repository path; soft 1,100–1,700 / hard 2,200 words; same schema, ledgers, and boundaries; stop after the file.

## 11. Boundary statement

This file is non-execution-source advisory evidence only. It authorizes no repository writes, no Codex tasks, no execution-source updates, no comparison against or repair of the existing design, no acceptance or rejection of prior Fable findings, no architecture design, no inspection of research reports or prompts, no target workspace/material/write/build/regression actions, and no resumption or closure of the paused post-handoff route. `current/human-approved-spec.md` remains Mnemosyne’s only execution source; any conflict between this file and it is resolved in the execution source’s favor and reported, never silently reconciled. GF-STEP-1B is complete; GF-STEP-1 is not complete.