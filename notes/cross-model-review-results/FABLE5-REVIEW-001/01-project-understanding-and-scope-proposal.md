# FABLE5 Independent Review — Project Understanding and Scope Proposal

## 1. Access and Evidence Caveats

```yaml
access_mode: DIRECT_GITHUB_CONNECTOR_READ_OK
access_caveats:
  retrieval_based_not_path_sequential: true
  branch_not_independently_verifiable_by_you: true
  snapshot_freshness_not_guaranteed_by_you: true
evidence_discipline_applied:
  no_single_chunk_completeness_claims: true
  no_strong_absence_claims_without_query_coverage: true
  distinguish_live_sections_from_historical_sections: true
  distinguish_current_file_content_from_embedded_historical_grep_outputs: true
```

All repository evidence below came from the conversation's GitHub connector / attached project knowledge (retrieval-based). No web search was used for repository facts. Roughly a dozen distinct query batteries have been run across this session, directly retrieving content from: `current/human-approved-spec.md`, `current/active-context.md`, `current/todo.md`, `current/open-questions.md` (chunks), `handoff/handoff-current.md` (chunks), `handoff/meta-agent-next-conversation-startup-prompt.md`, `handoff/meta-agent-post-079-phase-closure-handoff-package.md` (large chunks), all seven of `notes/codex-task-results/MNEMOSYNE-079..085-result.md`, plus incidentally surfaced context files (`notes/first-target-project-intake-records/README.md`, `handoff/first-target-project-dry-run-onboarding-package.md`, `notes/object-templates-and-id-rules.md`, `notes/pro-review-results/MNEMOSYNE-PRO-01-execution-source-consistency-audit.md`).

Standing caveats on every statement in this document: quotes are exact, but chunk boundaries mean no claim here asserts full-file completeness; embedded `grep`/`git` outputs inside task result records are historical snapshots of other files, not their current content; branch identity and sync freshness are not independently verifiable by me, though all retrieved state is consistent with the MNEMOSYNE-085 baseline.

Two wording rules applied throughout: repository statements are reported as claims ("the file records…", "the task result states…"), not adopted as verified conclusions; and nothing below is a review finding — Section 6 items are claims queued for verification, not defects.

## 2. Project Understanding Map

```yaml
project_understanding:
  what_is_Mnemosyne: >
    A meta-agent workspace repository for designing external persistent memory
    systems for other AI-agent projects — a design factory and design archive,
    not itself an operational memory system and not an ordinary project memory store.
  what_problem_it_appears_to_solve: >
    Model-independent continuity and auditability: models are treated as
    replaceable compute; files/Git are the long-term memory and audit base, so
    work survives model swaps, session resets, and multi-model workflows, with
    human-gated authority over what counts as approved design.
  what_files_define_authority: >
    current/human-approved-spec.md (sole execution source), reinforced by
    execution_source flags in object templates and restated in every
    current-state and handoff file retrieved.
  what_files_define_live_state: >
    current/active-context.md (compact current view + checkpoints),
    current/todo.md (live route/boundaries), current/open-questions.md
    (live question blocks; file also appears to contain historical duplicated regions).
  what_files_define_handoff: >
    handoff/handoff-current.md (cross-session card); official MNEMOSYNE-083
    artifacts: handoff/meta-agent-post-079-phase-closure-handoff-package.md and
    handoff/meta-agent-next-conversation-startup-prompt.md; plus
    handoff/first-target-project-dry-run-onboarding-package.md as an older,
    still-maintained entry point.
  what_files_record_task_history: >
    notes/codex-task-results/MNEMOSYNE-0NN-result.md per task; prior
    model-review outputs exist under notes/pro-review-results/.
  what_is_currently_paused_or_pending: >
    The post_084_handoff_validation_and_migration route is paused by the
    user-approved MNEMOSYNE-085 interruption marker while user-inserted long
    work (this review effort, per conversation context — not yet named in
    repository state) proceeds; user decisions on resuming migration via the
    official 083 artifacts remain open.
  what_types_of_work_are_not_authorized: >
    Target workspace creation; target material ingestion; target repository
    write; regression formalization; operational build/installation;
    execution-source update; plus repository-specific prohibitions (no
    AGENTS.md/CLAUDE.md/automation without approval; multi-model review is not
    truth voting or writeback authority; PASS_WITH_WARNINGS is not
    production-ready or write approval).
  what_you_do_not_yet_understand:
    - the concrete content of the "warnings" behind PASS_WITH_WARNINGS (verdict and score are restated everywhere; the warning list itself has not been retrieved)
    - the provenance/authority of the "maintainer review" that produced ACCEPT_FOR_NON_EXECUTION_SOURCE_INGESTION_WITH_WARNINGS (user? model? which?)
    - how current/open-questions.md delimits live vs historical/archive regions (duplicate blocks observed at distant line numbers)
    - the full text of the two official 083 artifacts and the onboarding package beyond retrieved chunks
    - where a heterogeneous (non-Codex, non-GPT) review output like this one is supposed to be stored or ingested — notes/pro-review-results/ is an observed precedent, not a verified rule
    - the content of regression candidates REG-META-DRYRUN-001..007
  what_requires_more_reading:
    - targeted retrieval of the dry-run result and maintainer-review files (see Section 10)
    - completeness passes over the two official 083 artifacts and open-questions live region (retrieval-first; exact dump only if coverage stays insufficient)
```

Supporting quotes (exact):

`current/human-approved-spec.md`:

```text
- Mnemosyne 是记忆系统元 Agent 工作仓库。
- 用于为其他项目、长期研究、学习系统、开发 Agent、多 Agent 团队等设计外部持久记忆系统。
- 不是某个具体项目的普通记忆库。
```

```text
- 模型负责计算，文件负责记忆。
- 模型是可替换计算单元，不是长期真相源。
- 外部文件 / Git 仓库是长期记忆和审计基础。
```

```text
- Mnemosyne 仓库是设计工厂和设计档案。
- 目标项目仓库或目录是目标项目运行真相源。
```

## 3. Repository Authority Map

The expected authority model in the charter is corroborated by repository evidence; no contradiction with it was observed in retrieved content.

Execution source — the spec self-declares, and the declaration is restated independently:

- `current/human-approved-spec.md`:

```text
# Human-Approved Spec（v0.1 当前执行源）

本文档是 Mnemosyne 当前唯一执行源（source of execution）。
```

- `current/active-context.md` (section `### current execution source`):

```text
- `current/human-approved-spec.md` is the current and only execution source.
- Active context, handoff, TODO, open questions, research reports, candidates, decision logs, dry-run/replay templates, and Codex result records are not execution source.
```

- `handoff/handoff-current.md` (section `## Current execution source`):

```text
- `current/human-approved-spec.md` is the only execution source.
- If any handoff/current/research/candidate/result file conflicts with the spec, follow the spec and record an open question.
```

Conflict-handling rule at the source, spec section `## 4. 执行源原则`:

```text
- 如果其他文件与 `human-approved-spec` 冲突，应以 `human-approved-spec` 为准，并登记 open question。
```

Update gate, spec section 6: `- 用户确认后才可更新 Human-Approved Spec。` and section 6.1: `- 只有用户确认后才可更新 \`current/human-approved-spec.md\`。`

Object-level convention, `notes/object-templates-and-id-rules.md`: `- 只有 Human-Approved Spec Entry 是执行源。`

Two authority nuances relevant to this review's own status: research reports are recorded as a high-weight evidence layer that still `不能直接覆盖执行源` (spec section 5); and `handoff/handoff-current.md` (Key prohibitions) records:

```text
- Do not treat multi-model review as truth voting, execution source, or automatic writeback authority.
```

So by the repository's own rules, this Fable 5 review — like the prior GPT work it examines — is advisory evidence only.

## 4. Current-State Map

The repository records a paused route under a user-approved marker. `notes/codex-task-results/MNEMOSYNE-085-result.md`:

```text
task_type: current_state_marker_only
post_084_residue_found: false
used_for_residue_repair: false
user_explicitly_approved_task_number_reuse: true
interrupted_route: post_084_handoff_validation_and_migration
interruption_status: suspended_by_user_inserted_long_work
resume_condition: after_inserted_long_work_is_completed_or_user_asks_to_resume
resume_action: remind_user_to_continue_or_choose_the_paused_post_handoff_path
```

The live route, `current/todo.md` (`## Active`):

```text
- Inserted long work may proceed only when specified by the user.
- After inserted long work completes, remind the user to resume the paused post-handoff path or choose another post-handoff path.
- The paused route remains: review MNEMOSYNE-084 if needed; use `handoff/meta-agent-next-conversation-startup-prompt.md`; reference `handoff/meta-agent-post-079-phase-closure-handoff-package.md`; choose a post-handoff path only after explicit user decision.
```

Boundaries, `current/todo.md` (`## Current boundaries`):

```text
- MNEMOSYNE-085 has been used for a user-approved interruption marker and resume guard, not for residue repair.
- Future residue or handoff-defect repair tasks require later validation and a new explicit user-approved task number.
- No target workspace has been created.
- No target materials have been uploaded/ingested.
- No target repository has been written.
```

Marker guard, `handoff/handoff-current.md` (`## Next route`, steps 2, 5, 6):

```text
2. Inserted long work may proceed only when specified by the user; do not use this marker to begin that work.
5. Do not propose MNEMOSYNE-080/081/082 again.
6. This marker does not approve workspace/material/target-write/build/regression-formalization, target repository write, operational memory-system installation, or execution-source update.
```

Number-reuse context, `current/active-context.md`: the file records that the `previous guard was \`MNEMOSYNE_085_only_if_residue_found\`` and that `user authorization now explicitly approved using MNEMOSYNE-085 for this interruption marker before inserted long work.`

One gap the repository itself records — `notes/codex-task-results/MNEMOSYNE-085-result.md` (Known gaps): `- The user has not yet specified the inserted long work in repository state.` The conversation context identifies this Fable 5 review as that inserted work, but the repository does not yet name it; that identification is conversation-level, not repository evidence.

PASS_WITH_WARNINGS bounding as restated in live state, `current/active-context.md`:

```text
- PASS_WITH_WARNINGS does not approve target workspace creation, target material ingestion, target repository write, operational memory-system installation, production-ready status, or Mnemosyne execution-source update.
```

## 5. Handoff and Task-History Map

Reconstructed 079→085 chain, from each task's own result record plus cross-file restatements. Legend: "self-attested" = claimed by the task's own record (often with embedded command outputs, which are historical snapshots); "corroborated" = restated by independently edited files.

- **MNEMOSYNE-079** — ingested the external controlled no-target-write dry-run result as non-execution-source evidence. The result record states: `maintainer_review_summary: Maintainer review accepts the result for non-execution-source ingestion with warnings; PASS_WITH_WARNINGS score 89/100 and no critical blockers are not production-ready or write approval.` Notably it also states: `no_write_evidence_review_summary: Equivalent no-write evidence is accepted for this run because git diff proof was unavailable and the result reports read-only/no-write boundaries.` — i.e., the no-write property of the dry run rests on equivalent evidence, not direct diff proof. Corroborated as ingested by active-context, todo, open-questions, handoff-current, onboarding package, intake README.
- **MNEMOSYNE-080** — `task_name: Repair post-079 current-state residue and prepare phase-closure decision`; `residue_confirmed: true`. Its record states `files_not_modified: - current/todo.md` with `todo_status: >- Inspected only. …` Cross-file asymmetry observed: `current/active-context.md`'s checkpoints list includes an MNEMOSYNE-080 line, while `current/todo.md`'s `## Recently completed` list (retrieved twice) shows 081 followed directly by 079. Whether that omission is harmless is queued in Section 6.
- **MNEMOSYNE-081** — created stabilization roadmap + regression triage: `regression candidates REG-META-DRYRUN-001 through REG-META-DRYRUN-007 triaged only; formalize_now is false and no executable/global tests were created.` Known gaps state phase closure and handoff package were intentionally not done.
- **MNEMOSYNE-082** — recorded phase closure and baseline freeze. Self-flagged limitation in its own record: `started_from_latest_master: unverified_locally_no_fetch_performed`. Summary: accepted PASS_WITH_WARNINGS `as the current non-execution-source evidence baseline and deferring high-risk follow-ups until after handoff.`
- **MNEMOSYNE-083** — created the two official handoff artifacts. Its record states: `startup_prompt_summary: Pasteable next-conversation prompt created in handoff/; says completed_through MNEMOSYNE-083; forbids proposing MNEMOSYNE-080/081/082 again; permits MNEMOSYNE-084 only if post-083 residue or handoff correction is needed.` Known gap recorded at the time: `- No user acceptance review of the generated handoff package has occurred yet.`
- **MNEMOSYNE-084** — repaired post-083 residue (its record quotes the pre-edit stale lines it fixed) and states the official artifacts were left unchanged: `files_not_modified:` includes both `handoff/meta-agent-post-079-phase-closure-handoff-package.md` and `handoff/meta-agent-next-conversation-startup-prompt.md`. Known gap recorded at the time: `- User or next-conversation review of MNEMOSYNE-084 result is still pending.`
- **MNEMOSYNE-085** — the interruption marker (Section 4). Its edits updated open-questions to record `reviewed_in_maintenance_conversation` and `post_084_residue_found: false` for post-084 validation.

Frozen vs live tension inherent in this design: the official startup prompt is a frozen artifact stating

```text
completed_through: MNEMOSYNE-083
```

and

```text
After validating MNEMOSYNE-083, the only possible immediate next task number is MNEMOSYNE-084, and only if post-083 residue repair or handoff correction is needed.
```

while live files record 084 and 085 as consumed and the route as paused. The live files do route readers around this (`todo` Active step: "review MNEMOSYNE-084 if needed; use [startup prompt]…"), but whether the combination is safe for a literal fresh session is a central verification target, not a settled fact.

Evidence-quality pattern across the chain: every "no prohibited change occurred" claim is task-local self-attestation supported by embedded command outputs; cross-file corroboration exists for state pointers and status lines (which the same task usually edited); no heterogeneous-model verification of the chain exists in the retrieved evidence prior to this effort.

## 6. Claims That Need Verification

All items below carry `status: claim_to_be_verified_from_repository_evidence`.

1. **"post-084 validation found no current residue requiring a repair task"** (`current/todo.md`, `current/active-context.md`). The recorded basis is `reviewed_in_maintenance_conversation` — a conversation-level review, self-reported into the repository. Heterogeneous re-check of the residue definition against current files is the core value target.
2. **"official MNEMOSYNE-083 handoff artifacts were not modified"** through 084/085 (`handoff_artifacts_modified: false`, `official_handoff_artifacts_modified: false`). Basis: embedded git snapshots at task time. Verify current content still matches what 083's record describes.
3. **"No target workspace/material/target-write"** boundary claims. Basis: embedded `find`/`grep` snapshots (e.g., `find target-projects … no output`). These are historical; current-state re-check needed within retrieval limits.
4. **Fresh-session safety of the frozen startup prompt** given `completed_through: MNEMOSYNE-083` and its 084-only task-number guard, now that 084 and 085 are consumed and the route is paused. The repository claims the live files re-route correctly; unverified.
5. **PASS_WITH_WARNINGS restatement integrity.** All retrieved restatements so far preserve the non-approval qualifiers; full-file coverage is incomplete, and the underlying warnings content has not been retrieved at all.
6. **`current/todo.md` omission of MNEMOSYNE-080** from Recently completed: harmless bookkeeping artifact or chain-readability defect?
7. **`current/open-questions.md` live-vs-archive structure**: duplicate blocks at distant line numbers (e.g., `interruption_status` at 81 and 591; `repaired_by_MNEMOSYNE-080` at 49 and 543), and a retrieved block reading `Post-083 handoff validation: status: pending_user_or_next_conversation_review` coexisting with post-084 blocks — which regions are live, and can a reader tell?
8. **"Maintainer review" provenance** behind `ACCEPT_FOR_NON_EXECUTION_SOURCE_INGESTION_WITH_WARNINGS` — who or what performed it, and is its authority level stated?
9. **The no-write evidence exception** in 079 (`git diff proof was unavailable`, equivalent evidence accepted) — is the exception's scope recorded as one-time, and is it quarantined from becoming precedent?
10. **Repository representation of the current inserted work** — 085's record states the user has not specified it in repository state; does anything else contradict or resolve this?

## 7. Candidate Deep-Review Slices

- **S1 — Post-079→085 handoff authority and state-machine review.** Coherence, authority-boundedness, and continuation safety of the live chain and paused route; includes frozen-vs-live artifact tension and prohibition-list consistency. Covers verification items 1, 2, 4, 5, 6, 7 and parts of 3.
- **S2 — Self-attestation vs corroboration audit of boundary claims.** For each 079–085 "no prohibited change / no residue" claim: classify evidence type (self-attestation, embedded snapshot, cross-file restatement), re-check what is currently checkable, and flag claims resting solely on same-family self-verification. Covers items 1, 2, 3, 8, 9.
- **S3 — Fresh-session recoverability slice only** (startup prompt + package vs live state). A subset of S1; too narrow alone to answer continuation safety.
- **S4 — Review-output ingestion process slice** (where heterogeneous review results should live; `notes/pro-review-results/` precedent). Real question, but process-design rather than defect review; better raised as a user question than consumed as the first deep slice.

## 8. Selected First Deep-Review Slice

```yaml
slice_selection:
  selected_scope: >
    FABLE5-REVIEW-001: post_079_to_085_handoff_authority_and_state_machine_review,
    executed with an explicit self-attestation-vs-corroboration evidence audit
    (S1 as the frame, S2 as the method; S3 subsumed as a phase).
  why_this_scope: >
    Every continuation path a fresh session could take runs through exactly these
    files; the repository's own records flag unclosed loops here (083 known gap:
    no user acceptance review; 084 known gap: review pending; 085 known gap:
    inserted work unnamed); concrete verification seeds already surfaced from
    retrieval (frozen startup prompt task-number guard vs consumed 084/085;
    todo's 080 omission; open-questions duplicate regions; the 079 no-write
    evidence exception); and the highest heterogeneous-model value lies in
    re-checking claims that were only ever self-verified by the same model family.
  what_is_in_scope:
    - the 14 Stage A/B files
    - authority and prohibition statements as expressed in them
    - the 079→085 state machine and task-number semantics
    - frozen 083 artifacts as migration baseline vs live paused route
    - evidence-type classification of boundary and residue claims
    - PASS_WITH_WARNINGS restatement integrity across these files
  what_is_out_of_scope:
    - pre-079 history except where in-scope files depend on it
    - research reports, raw records, templates, target-project design content
    - spec content quality (the spec is the yardstick, not the reviewed object)
    - any repository modification, task generation, or route resumption
  why_not_full_repository_review: >
    Retrieval-based access makes broad-shallow coverage unreliable (partial
    chunks over many files inflate false findings and make absence claims
    irresponsible); continuation risk is concentrated in the live chain; the
    spec itself prescribes need-based reading over full reads
    (`raw 和 research reports 按需回查，不默认全量读取`); and a bounded slice keeps
    the evidence/coverage ledger achievable.
  evidence_paths_used:
    - current/human-approved-spec.md
    - current/active-context.md
    - current/todo.md
    - current/open-questions.md
    - handoff/handoff-current.md
    - handoff/meta-agent-next-conversation-startup-prompt.md
    - handoff/meta-agent-post-079-phase-closure-handoff-package.md
    - notes/codex-task-results/MNEMOSYNE-079-result.md … MNEMOSYNE-085-result.md
    - notes/first-target-project-intake-records/README.md
    - handoff/first-target-project-dry-run-onboarding-package.md
  expected_value_of_fable5_review: >
    Heterogeneous corroboration or challenge of same-family self-attested
    claims; adversarial literal-reader simulation of handoff entry points;
    cross-file divergence detection across redundant boundary restatements;
    evidence-type transparency so the user can see which safety claims rest on
    what kind of proof.
  risks_if_this_scope_is_not_reviewed:
    - a fresh session literally following the frozen startup prompt could act on a stale task-number guard or miss the 085 pause
    - "no residue / no prohibited change" confidence could rest on unexamined self-attestation
    - subtle divergence among repeated prohibition lists could open an authority-leakage loophole undetected
    - stale or ambiguous open-questions regions could mislead future maintenance tasks
```

## 9. Why This Is Independent From GPT Prior Work

First, transparency about anchoring: a scope with the same name was suggested in earlier prompt material. This selection does not rest on that suggestion; it is re-derived here from repository evidence gathered by my own retrievals, with the trail cited in Sections 5–7, and it is materially modified — the evidence-audit method (S2) is elevated to co-equal status because the single strongest pattern in the retrieved evidence is that safety-critical claims are same-family self-attestations supported by task-time snapshots.

Second, the seeds driving the selection are ones the prior work either flags only as open gaps in its own records (083/084 known-gap lines) or does not flag at all (the frozen startup prompt's now-stale task-number guard; todo's 080 omission; open-questions duplicate regions; the 079 equivalent-evidence exception). None of these were asserted to me as facts by any prompt; each was surfaced by retrieval and is quoted above.

Third, what would have changed the selection: if Stage A/B evidence had shown an unresolved execution-source conflict, a live route pointing elsewhere, or a contradiction between the 085 marker and the user-stated baseline, the first slice would have targeted that instead. It did not.

Fourth, the review's authority posture follows the repository's own rule rather than any model's preference: multi-model review is not truth voting (`handoff/handoff-current.md`, quoted in Section 3). Findings from this review will be advisory evidence, subject to the same non-execution-source discipline as the GPT-generated artifacts it examines — including the possibility that the review concludes the prior work is sound.

## 10. Files Needed Next, If Any

```yaml
additional_file_request:
  - path: notes/first-target-project-intake-records/meta-agent/controlled-dry-run-results/META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-result.md
    reason: primary record of the PASS_WITH_WARNINGS verdict
    specific_question_it_answers: what the actual warnings are, so restatement-integrity (Section 6, item 5) can be judged against the source
    why_current_files_are_insufficient: every retrieved file restates verdict/score/blockers but never the warnings content

  - path: notes/first-target-project-intake-records/meta-agent/controlled-dry-run-results/META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-maintainer-review.md
    reason: source of the maintainer-review verdict
    specific_question_it_answers: provenance and stated authority of ACCEPT_FOR_NON_EXECUTION_SOURCE_INGESTION_WITH_WARNINGS (Section 6, item 8) and the recorded scope of the no-write equivalent-evidence exception (item 9)
    why_current_files_are_insufficient: only one-line summaries of the review exist in retrieved files

  - path: current/open-questions.md
    reason: live-vs-archive region structure (Section 6, item 7)
    specific_question_it_answers: which blocks are live; whether the pending_user_or_next_conversation_review block is superseded history or stale live state
    why_current_files_are_insufficient: retrieval shows duplicate blocks at distant line numbers without their delimiting section headers
    note: retrieval-first; exact file dump requested only if targeted queries cannot resolve region boundaries

  - path: handoff/meta-agent-post-079-phase-closure-handoff-package.md and handoff/meta-agent-next-conversation-startup-prompt.md
    reason: completeness for the literal fresh-session simulation
    specific_question_it_answers: whether any section beyond retrieved chunks contains route or authority wording now stale relative to the 085 pause
    why_current_files_are_insufficient: large chunks retrieved, but the simulation requires confidence there are no unseen sections
    note: retrieval-first; dump only on insufficiency
```

No other files are requested. Historical, raw, research, and template files remain unread by default.

## 11. What This Does Not Authorize

This document and the eventual FABLE5-REVIEW-001 result are non-execution-source, advisory evidence only. They grant no permission to: create a target workspace; ingest target materials; write any target repository; formalize regression candidates (including REG-META-DRYRUN-001..007); build or install an operational memory system; modify `current/human-approved-spec.md`; modify the official MNEMOSYNE-083 artifacts; generate Codex tasks; treat PASS_WITH_WARNINGS as production-ready or target-write approval; treat any review output as execution source or truth voting; or resume, close, or redirect the paused `post_084_handoff_validation_and_migration` route. Any eventual repair requires later validation and a new explicit user-approved task number. The MNEMOSYNE-085 resume obligation stands: after this inserted work completes, the user should be reminded to resume or choose the paused post-handoff path.

## 12. Proposed Next Step

Stopping here per the charter. On explicit user approval, I will execute Output 2 — the formal FABLE5-REVIEW-001 result on the selected slice: re-verifying the Section 6 claims against current retrievable state, running the literal fresh-session simulations, classifying evidence types for every boundary claim, and delivering findings/non-findings with exact quotes, severity, evidence_mode caveats, and a retrieval coverage ledger. If the two dry-run evidence files (first two items in Section 10) can be retrieved by connector I will do so as part of the review; if not, I will pause and request them rather than proceed on summaries.
