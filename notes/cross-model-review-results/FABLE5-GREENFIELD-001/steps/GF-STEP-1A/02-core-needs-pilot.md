# FABLE5-GREENFIELD-001 — GF-STEP-1A Core User Need Extraction Pilot

## 1. Metadata

```yaml
charter_id: FABLE5-GREENFIELD-001-CHARTER
step_id: GF-STEP-1A
step_name: core_user_need_extraction_pilot
record_type: independent_need_model_pilot
authority_level: non_execution_source_advisory_evidence
step_status: pilot_complete_GF_STEP_1_not_complete
author_model: Fable 5
date: 2026-07-10
source_file: raw/concept-origin-extract-001.md
source_ref: master
source_blob_sha: b47248f1052ecac679c2e3a0afab4d93ca2c6649
source_language: zh-CN
```

## 2. Scope and workload limits

Bounded pilot of GF-STEP-1, not its completion. Governing charter: FABLE5-GREENFIELD-001-CHARTER, recovered from this project's conversation record; no repository tier was opened for it. The narrower step instruction governs (single source; no research materials). Limits: retrieval batteries 2 of 4; records 12 of 12 cap; word count 1,792 (within target); no web search; no auto-continuation into GF-STEP-1B.

## 3. Source and anti-contamination policy

Extraction used only `raw/concept-origin-extract-001.md`, fetched once via a single-path GitHub API call (no other repository paths exposed) and read locally in full (909 lines, §0–18). No `current/**`, `handoff/**`, `notes/**`, `commands/**` file, MNEMOSYNE task result, FABLE5 review/triage result, GPT design artifact, or research report/summary/prompt was read. Provenance: the source is a ChatGPT-compiled near-original extract (`is_full_transcript: false`, revision `v2_reason_enriched`); 用户近原文 blocks are curated near-quotes and 理由和考量 blocks are compiler-attributed reasons. Accordingly: 用户近原文 anchors → `user_origin_evidence`; 助手核心回应 content → `assistant_origin_era_proposal`, kept in derivation notes, never converted into user requirements; reasons-layer material is attributed motivation, not standalone user quotes.

## 4. Known prior-exposure disclosure

Fable 5 previously reviewed parts of the current Mnemosyne design (REVIEW-001..003, triage). This step is independent by derivation and disclosure, not amnesia: every record is anchored to the allowed source, wording stays source-near, and no existing-design detail is used or described. No record required wording the source does not force, so no per-record echo flag is true. The residual echo channel is selection salience — which themes were judged load-bearing may be shaped by prior exposure — so the ranking, not record content, is the exposure-sensitive layer. Needs are not down-weighted because the existing design may also address them.

## 5. Core need inventory

- need_id: GF1A-N01
- need_title: durable_external_memory_for_long_horizon_ai_work
- source_anchor: §1 用户近原文 — “跨对话记忆断裂…进度丢失…不够可见、可编辑、可迁移、可审计”
- source_class: user_origin_evidence
- interpreted_need: Long-horizon AI work (learning, research, automated development, multi-agent projects) needs memory that survives conversation resets and lives outside any platform’s internal memory — visible, editable, migratable, auditable.
- motivation_or_fear: Progress/context loss across sessions; opaque, non-portable platform memory.
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: Priority among scenario families (dev, learning, general dialogue) not fixed in user text.
- possible_prior_exposure_echo: false
- derivation_note: Founding problem statement; purpose anchor.

- need_id: GF1A-N02
- need_title: capability_honesty_and_uncertainty_quarantine
- source_anchor: §2 用户近原文 — “绝对尊重研究报告结论…不确定内容单独列出”
- source_class: user_origin_evidence
- interpreted_need: Formal design stays strictly within researched, real tool capability; unverifiable or infeasible-today items are listed separately, never blended into the formal plan.
- motivation_or_fear: Reasons layer: models may present “theoretically possible” as “currently available” (connectors auto-writing repos; future capability as present).
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: The user specified the demand; the grading mechanism is assistant-era.
- possible_prior_exposure_echo: false
- derivation_note: A–E evidence grading = assistant_origin, context only.

- need_id: GF1A-N03
- need_title: per_scenario_memory_system_design_meta_agent
- source_anchor: §5 用户近原文 — “是否有必要建立一个 AI Agent…专门…定制记忆系统？”
- source_class: user_origin_evidence
- interpreted_need: An upper-layer agent deciding, per project/scenario: what to remember; long-term vs buffer; what needs human confirmation; what agents may update; what enters Git; what must not reach the cloud.
- motivation_or_fear: Scenario schemas differ widely; manual per-project design is costly, incomplete (reasons layer).
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: Long-run autonomy ceiling beyond “not unsupervised at first” unstated by the user.
- possible_prior_exposure_echo: false
- derivation_note: User-initiated question; role split (designer/generator/reviewer/maintainer) = assistant_origin.

- need_id: GF1A-N04
- need_title: continuous_evolution_multi_source_intake
- source_anchor: §6 用户近原文 — “无法一开始考虑完善…持续改进”；“其他 AI Agent…转交给 Mnemosyne”
- source_class: user_origin_evidence
- interpreted_need: No one-shot design: continuously absorb intermittent new needs and usage feedback, from the user directly and from other agents forwarding memory-related needs.
- motivation_or_fear: User cannot design completely upfront; long projects keep generating feedback.
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: Format/authority protocol for agent-forwarded needs unspecified.
- possible_prior_exposure_echo: false
- derivation_note: Self-bootstrapping treated in GF1A-N12.

- need_id: GF1A-N05
- need_title: design_record_placement_tension
- source_anchor: §6 用户近原文 — “设计书保存在哪里：…目标项目中，还是…自己仓库中，再交付”
- source_class: user_origin_evidence
- interpreted_need: Design records live where cross-project experience accumulates, while each target project keeps an operative record that does not drift from what was delivered.
- motivation_or_fear: Scattered designs block learning; centralized-only designs risk runtime divergence (reasons layer).
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: User acceptance of the assistant’s dual-layer 设计工厂/运行真相源 answer is not evidenced in this file.
- possible_prior_exposure_echo: false
- derivation_note: Tension = user need; dual-repo/主副本/sync mechanisms = assistant_origin.

- need_id: GF1A-N06
- need_title: raw_preservation_with_derived_model_digests
- source_anchor: §7 用户近原文 — “需要保留原文…让各模型…形成自己用的整理版、精简版、索引版”
- source_class: user_origin_evidence
- interpreted_need: Originals preserved as evidence; models build their own condensed/indexed derivations for cheap routine reading; derivations never replace originals.
- motivation_or_fear: Model replacement (even same-family upgrades) must not inherit another model’s misreadings; user forgetting requires re-checkable originals.
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: Raw sufficiency bar (full transcript still open per §17) and digest refresh cadence unspecified.
- possible_prior_exposure_echo: false
- derivation_note: Settled via an explicit in-source user self-correction.

- need_id: GF1A-N07
- need_title: human_confirmed_execution_layer
- source_anchor: §7 用户近原文 — “人类思考会变化…需要一层…用户决定实施到项目中的版本”
- source_class: user_origin_evidence
- interpreted_need: Beyond raw history and model analysis, a human-confirmed “currently implemented” layer; “user once said” must never execute as “user now decides.”
- motivation_or_fear: Originals are stage-bound, repetitive, sometimes conflicting; newer thoughts not necessarily better (reasons layer: three truths).
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: Approval granularity (per need? per release?) unspecified.
- possible_prior_exposure_echo: false
- derivation_note: Layer name Human-Approved Spec appears in-source; six-layer stack detail = assistant_origin.

- need_id: GF1A-N08
- need_title: requirement_similarity_and_reconciliation
- source_anchor: §8 用户近原文 — “查重找出…旧版本，主动…说明差异…让用户决定”
- source_class: user_origin_evidence
- interpreted_need: On new input, proactively find similar prior needs, explain differences and implementation consequences; the user decides implemented wording; “latest input auto-wins” is prohibited.
- motivation_or_fear: Repeated re-proposals with drift; fear of overwriting maturer old versions or accumulating clutter.
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: Similarity thresholds and triggers unquantified; option vocabulary (merge/replace/…) = assistant_origin.
- possible_prior_exposure_echo: false
- derivation_note: Motivates GF1A-N07’s gate.

- need_id: GF1A-N09
- need_title: von_neumann_style_state_externalization
- source_anchor: §10 用户近原文 — “模型只作为运算器…其他所有内容作为存储数据”
- source_class: user_origin_evidence
- interpreted_need: Models are swappable compute; rules/prompts (instructions) and working content (data) are separate external files; internal model memory is cache only; handoff files carry work between sessions.
- motivation_or_fear: Decouple long-term state from any model so upgrades, restarts, handovers cannot destroy it; rules stay uncontaminated by history.
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: Where evolving rules sit while rules themselves are under design is unaddressed.
- possible_prior_exposure_echo: false
- derivation_note: Analogy user-proposed; “not a deterministic CPU” caveats = assistant_origin.

- need_id: GF1A-N10
- need_title: migration_policy_and_constraint_lifecycle
- source_anchor: §11 用户近原文 — “从原文重新整理…还是从旧模型加工版继承？…约束…可能变成废话”
- source_class: user_origin_evidence
- interpreted_need: Migration must neither blindly inherit old-model digests (bias fossilization) nor force full raw re-analysis (cost); model-specific constraints get lifecycle handling; new capabilities get deliberate adoption.
- motivation_or_fear: Inherited misreadings, dead-weight behavioral patches, unbounded re-analysis cost.
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: Cost tolerance and per-migration decision authority unspecified; layer/level/state machinery = assistant_origin.
- possible_prior_exposure_echo: false
- derivation_note: Posed as an open question plus concerns, not a chosen mechanism.

- need_id: GF1A-N11
- need_title: human_reviewed_small_step_staged_construction
- source_anchor: §14 用户近原文 — “逐步…正式建立”；§13 — 两台机器、远程保存、先做核心
- source_class: user_origin_evidence
- interpreted_need: Staged tasks producing small, diff-reviewable Markdown changes under user review; defer environments and automation until the core stabilizes; fit cross-machine, remote-save constraints.
- motivation_or_fear: Reduce agent mis-edit risk; keep changes auditable; avoid premature automation; core first (reasons layer plus §13).
- confidence: high
- stability_assessment: evolving
- unresolved_ambiguity: Exit criteria beyond “after the core stabilizes” undefined.
- possible_prior_exposure_echo: false
- derivation_note: Explicitly stage-bound; tool choice fit-to-constraints, not maximalism.

- need_id: GF1A-N12
- need_title: self_bootstrap_and_handoff_continuity
- source_anchor: §15 用户近原文 — “实现自身的持久记忆行为…把工作交接到新对话或任务”
- source_class: user_origin_evidence
- interpreted_need: The workspace runs on the discipline it designs: preserving its own design state, with simple stage-saving and handoff when a conversation or task grows too long.
- motivation_or_fear: Bootstrap credibility; long contexts overflow, so continuity must not depend on one session.
- confidence: high
- stability_assessment: stable_looking
- unresolved_ambiguity: Quantitative handoff trigger (“too long”) undefined.
- possible_prior_exposure_echo: false
- derivation_note: §15 assistant reply bounds v0.1 to process-level self-memory = assistant_origin scoping.

## 6. Incidental-exposure ledger

- E-1 — Battery 1 (project-knowledge search, query “FABLE5-GREENFIELD-001 charter”) returned chunks from prohibited-class paths: `notes/cross-model-review-results/**` (TRIAGE-001 raw file; REVIEW-001 manifest; REVIEW-003 result, multiple chunks) and `manual-import-inbox/FABLE5-*` (review outputs 001 and 002). Not used; charter not found there.
- E-2 — Conversation-history search (not a repository battery) for the charter also surfaced a FABLE5 research-study summary snippet (research-report class, prohibited here). Not used.

No prohibited material influenced any need record.

## 7. Coverage ledger

- Inspected: the entire allowed file (909 lines, §0–18); single-path fetch; sha in Metadata.
- Extracted: 12 records covering §1, §2, §5, §6 (two), §7 (two), §8, §10, §11, §13–14, §15.
- Inspected, not extracted (record cap; deferred): §0/§16 preservation-method meta-need; §3 research-conclusion synthesis (mostly assistant); §4 GitHub-as-substrate exploration; §9 idea capture buffer (user need, in-source deferred TODO); §12 language policy (user-settled, evolving); §17 usage boundaries; §18 import sequencing. Assistant-era mechanisms (A–E grades, Git levels, six-layer stack, reconciliation options, migration/constraint machinery) appear only in derivation notes.
- Retrieval batteries: 2 of 4 used.
- Why not GF-STEP-1 output: the 12-record cap deferred at least five user-origin themes; the charter’s second Step-1 source (research-prompt index) was excluded by pilot scope; the charter-required user question list is not yet assembled. Treating this file as complete would silently drop known user-origin evidence.

## 8. Unresolved questions

- UQ-1 (method): Confirm GF-STEP-1B keeps treating 理由和考量 blocks as attributed motivation only, never as standalone user quotes.
- UQ-2 (GF1A-N05): Is there raw evidence, outside prohibited tiers, of the user accepting or amending the dual-layer placement answer?
- UQ-3 (GF1A-N07): What approval granularity does the user intend for the human-confirmed layer (per need, per batch, per release)?
- UQ-4 (governance): The charter was recovered from project conversation history, not visible current-conversation text. Confirm this satisfies charter availability, or attach the charter to future step prompts.

## 9. Proposed bounded continuation for GF-STEP-1B (not executed)

- Scope: deferred user-origin themes (§0/§16, §4, §9, §12, §17) from the same source; continue numbering (GF1B-N13…); assemble the charter-required user question list from 1A+1B ambiguities; short assistant-era mechanism register (context only, no design).
- Limits: ≤8 new records; ≤2 retrieval batteries (single-path re-fetch of the same file only); 900–1,400 words; same schema, ledgers, boundaries; stop after the file.
- Non-completion: even after 1B, GF-STEP-1 stays incomplete until the research-prompt-index source is handled under a user-authorized 1C, or the user narrows Step-1 to the concept extract alone.

## 10. Boundary statement

This file is non-execution-source advisory evidence only. It authorizes no repository writes, no Codex tasks, no execution-source updates, no comparison against or repair of the existing design, no architecture design, no target workspace/material/write/build/regression actions, and no resumption or closure of the paused post-handoff route. `current/human-approved-spec.md` remains Mnemosyne’s only execution source; any conflict between this file and it is resolved in the execution source’s favor and reported, never silently reconciled. GF-STEP-1A is complete as a pilot; GF-STEP-1 is not complete.
