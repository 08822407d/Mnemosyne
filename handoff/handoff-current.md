# Handoff Current

## 仓库

Mnemosyne

## 定位

Mnemosyne 是记忆系统元 Agent 工作仓库，用于设计、演化和交付 AI Agent 外部持久记忆系统。

## Immediate current continuation

- Batch A small fixes: PASS after post-047 and post-048 verification.
- Batch B Pro review: READY_AFTER_SMALL_FIXES.
- MNEMOSYNE-048 has created the onboarding package and review instruments.
- MNEMOSYNE-049 synchronizes current state.
- The pre-050 fresh ordinary replay was user-supplied and verified PASS for the pre-050 package.
- MNEMOSYNE-050 changes the onboarding/replay/check semantics, so the prior replay does not close the post-050 gate.
- MNEMOSYNE-051: DR2 handoff-strategy research ingested as evidence under `RC-2026Q2-handoff-strategy`; it is not execution source and does not close the post-050 replay gate.
- MNEMOSYNE-053 adopted a minimal DR2 handoff-correctness principle into execution source, created handoff strategy and scorecard instruments, and updated the first-target replay protocol.
- Next gate: post-MNEMOSYNE-053 fresh ordinary Thinking replay with maintainer scorecard review using `notes/first-target-project-fresh-replay-protocol.md`.
- No pre-053 replay result closes this new gate.
- Do not start real dry-run until post-053 replay reviewed PASS and later user target/authority/safe-input/no-target-write/run-manifest approval.
- No real target-project dry-run has occurred.
- No target project has been selected.
- No target-project materials have been uploaded or ingested.
- No target-project repository has been written.

## Read for first dry-run preparation

- `notes/first-target-project-fresh-replay-protocol.md`
- `notes/handoff-package-strategy-v0.1.md` for package-author/reviewer handoff tier strategy.
- `notes/handoff-replay-scorecard-v0.1.md` for maintainer replay review.
- `handoff/first-target-project-dry-run-onboarding-package.md`
- `notes/first-target-project-dry-run-manifest-template.md`
- Instruments listed by the onboarding package.

## Current execution source

- `current/human-approved-spec.md` is the only execution source.
- If any handoff/current/research/candidate/result file conflicts with the spec, follow the spec and record an open question.

## Key prohibitions

- Do not use non-execution sources as execution source.
- Do not treat raw records, research reports, candidate requirements, decision logs, active-context, handoff, startup instructions, or task result records as execution source.
- Do not claim PDF figure/table/image/layout review unless it was actually performed.
- Do not commit secrets, credentials, private source, customer/confidential material, unapproved personal data, or other sensitive material.
- Do not treat multi-model review as truth voting, execution source, or automatic writeback authority.
- Do not create AGENTS.md, CLAUDE.md, GitHub Actions, automation, MCP, RAG, or auto-writeback unless explicitly approved by a current task.
- Do not use unpromoted MNEMOSYNE-031 R4/R5 material as executable requirements; use the coverage map for promotion status.
- Do not promote D-01-D-07 candidate wording without separate user approval.
- Do not claim dry-run/pass/target selection occurred.
- Do not write target project.
- Do not use unsafe inputs.

## Recent checkpoints

- MNEMOSYNE-040: DR1 memory-testing/debugging/evaluation evidence ingested; OP-09 and OP-10 are partially answered, not closed.
- MNEMOSYNE-041: manual import inbox workflow established.
- MNEMOSYNE-042: user-action-first reply format added to execution source.
- MNEMOSYNE-043: manual-import safety gate established.
- MNEMOSYNE-044: D-01–D-07 execution-source coverage map created.
- MNEMOSYNE-045: compact current state/startup cleanup completed.
- MNEMOSYNE-046: minimal dry-run profile, checklist, issue-log template, and result template created as non-execution-source instruments.
- MNEMOSYNE-047: final Batch A residuals corrected; post-047 ordinary Mnemosyne conversation verification returned PASS.
- MNEMOSYNE-048: ordinary Mnemosyne conversation verification returned PASS; onboarding package and review instruments created for first target-project dry-run preparation.
- MNEMOSYNE-049: current state synchronized after 048; fresh ordinary Thinking startup/handoff replay became the next gate.
- MNEMOSYNE-050: stable manifest/replay protocols and unified result semantics added; post-050 fresh ordinary Thinking replay is now required.
- MNEMOSYNE-051: DR2 handoff-strategy research ingested as evidence; future sessions should read the DR2 summary when discussing handoff scoring, provenance, replay readiness, or first-dry-run readiness. DR2 is not execution source and does not close the post-050 replay gate.
- MNEMOSYNE-053: minimal DR2 handoff-correctness principle adopted into execution source; handoff package strategy and replay scorecard created as non-execution-source instruments; first-target replay protocol updated to post-053 scoring/review semantics.

## Next route

1. Run post-MNEMOSYNE-053 fresh ordinary Thinking startup/handoff replay using `notes/first-target-project-fresh-replay-protocol.md` and `handoff/first-target-project-dry-run-onboarding-package.md`, followed by maintainer scorecard review.
2. Do not treat any pre-053 replay result as closing this new gate.
3. After post-053 replay reviewed PASS, the user must still select a target, approve authority/safe input/no-target-write, and approve the run manifest before a real dry-run.
4. Keep the first target-project dry-run design-only unless separately approved otherwise.
5. Do not claim a target project has been selected, target materials have been uploaded/ingested, target repository has been written, or a real target-project dry-run has occurred.

## MNEMOSYNE-051 / DR2 handoff-strategy evidence

- DR2 handoff-strategy research has been ingested as evidence under `RC-2026Q2-handoff-strategy`.
- Future sessions should read `raw/research-reports/cycles/2026Q2-handoff-strategy/report-summaries/DR2_mnemosyne_handoff_strategy_quantitative_evaluation_summary.md` when discussing handoff package correctness, quantitative scoring, replay strategy, model/tool provenance, or pre-first-target-dry-run readiness.
- DR2 is not execution source and does not by itself modify current gates.
- DR2 changed the current required gate only through user-approved MNEMOSYNE-053: the gate is now post-MNEMOSYNE-053 replay with maintainer scorecard review.
