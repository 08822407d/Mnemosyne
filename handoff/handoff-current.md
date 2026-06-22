# Handoff Current

## 仓库

Mnemosyne

## 定位

Mnemosyne 是记忆系统元 Agent 工作仓库，用于设计、演化和交付 AI Agent 外部持久记忆系统。

## Immediate current continuation

- MNEMOSYNE-047 corrects the final Batch A residuals; Batch A small fixes are complete subject to ordinary-conversation post-047 verification.
- Do not begin Batch B until ordinary Mnemosyne conversation post-047 verification returns PASS.
- D-01–D-07 execution status comes from `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md` plus `current/human-approved-spec.md`.
- Unpromoted checkpoint content is not executable.
- First target-project dry-run remains design-only and uses public/synthetic/explicitly redacted input by default until separately approved; no real target-project dry-run has occurred and no target project has been selected.
- Repository visibility is intentionally user-controlled; do not propose a visibility change merely because the repository is public.
- Always verify visibility before importing material and apply the MNEMOSYNE-043 safety gate.

## Current execution source

- `current/human-approved-spec.md` is the only execution source.
- If any handoff/current/research/candidate/result file conflicts with the spec, follow the spec and record an open question.

## Key prohibitions

- Do not treat raw records, research reports, candidate requirements, decision logs, active-context, handoff, startup instructions, or task result records as execution source.
- Do not claim PDF figure/table/image/layout review unless it was actually performed.
- Do not commit secrets, credentials, private source, customer/confidential material, unapproved personal data, or other sensitive material.
- Do not treat multi-model review as truth voting, execution source, or automatic writeback authority.
- Do not create AGENTS.md, CLAUDE.md, GitHub Actions, automation, MCP, RAG, or auto-writeback unless explicitly approved by a current task.
- Do not use unpromoted MNEMOSYNE-031 R4/R5 material as executable requirements; use the coverage map for promotion status.

## Recent checkpoints

- MNEMOSYNE-040: DR1 memory-testing/debugging/evaluation evidence ingested; OP-09 and OP-10 are partially answered, not closed.
- MNEMOSYNE-041: manual import inbox workflow established.
- MNEMOSYNE-042: user-action-first reply format added to execution source.
- MNEMOSYNE-043: manual-import safety gate established.
- MNEMOSYNE-044: D-01–D-07 execution-source coverage map created.
- MNEMOSYNE-045: compact current state/startup cleanup completed.
- MNEMOSYNE-046: minimal dry-run profile, checklist, issue-log template, and result template created as non-execution-source instruments.
- MNEMOSYNE-047: final Batch A residuals corrected; result records compacted, dry-run schema tailoring added, manifest safety fields aligned, and the post-047 verification gate synchronized.

## Next route

1. Return to the ordinary Mnemosyne conversation for post-047 verification of Batch A results.
2. If post-047 verification returns PASS, the user may start Batch B Pro work.
3. Keep the first target-project dry-run design-only unless separately approved otherwise.
4. Do not claim Batch B has started, a target project has been selected, or a real target-project dry-run has occurred.
