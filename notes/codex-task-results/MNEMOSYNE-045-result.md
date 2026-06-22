# MNEMOSYNE-045 Codex Task Result

## task_id

MNEMOSYNE-045

## task_name

Current-State Consolidation, Startup Read-Path Cleanup, and Visibility Context Normalization

## user_confirmed_visibility_context

- The repository would normally be private.
- It is intentionally public during the current construction stage to improve accessibility.
- The user may switch it to private later and may switch it back to public in another stage.
- Public/private visibility is an operator-controlled stage setting, not by itself a Mnemosyne defect or repair trigger.
- Future agents should not repeatedly recommend changing visibility merely because it is public.
- The durable requirement is to verify current visibility before importing material and apply the MNEMOSYNE-043 safety gate.

## files_intended_to_edit

- `README.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `handoff/startup-instructions.md`
- `current/todo.md`
- `current/open-questions.md`
- `notes/v0.1-scope-and-consistency-check.md`
- `commands/load-mnemosyne-guidance.md` if needed
- `notes/codex-task-results/MNEMOSYNE-045-result.md`

## files_actually_edited

- `README.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `handoff/startup-instructions.md`
- `current/todo.md`
- `current/open-questions.md`
- `notes/v0.1-scope-and-consistency-check.md`
- `commands/load-mnemosyne-guidance.md`
- `notes/codex-task-results/MNEMOSYNE-045-result.md`

## replacement_strategy

Used deterministic full-file or top-block replacement through a Python patch script. High-risk current/startup files received compact current sections at the top. Historical content was either replaced when obsolete as a startup surface or retained below explicit historical/superseded headings.

## visibility_wording_normalization

- README no longer hard-codes a permanent public repository state.
- Active context, handoff, startup instructions, and load command now state that repository visibility is user/operator-controlled and may change by stage.
- Public/private state alone is not described as a defect or repair trigger.
- MNEMOSYNE-043 safety gate remains intact: verify visibility before imports; public or unverified visibility permits only public, synthetic, or explicitly redacted material; later visibility changes do not erase Git-history exposure.

## startup_path_changes

- `handoff/startup-instructions.md` now defines the minimum ordinary startup set as README, spec, active context, handoff, TODO, open questions, and Codex authoring/diff guidelines.
- `notes/v0.1-scope-and-consistency-check.md` was removed from mandatory ordinary startup / Codex startup and marked historical only.
- Task-extended reads are limited to research current views, target-project templates, manual-import docs, the D-01–D-07 coverage map, and historical v0.1 files for historical/audit tasks.

## stale_phrase_checks

The requested stale-phrase grep still finds phrases only inside clearly marked historical sections:

- `current/todo.md` historical detailed task list retains old memory-testing feasibility TODO wording for audit/history.
- `current/open-questions.md` historical open-question list retains the old recovered-light-prompt hypothetical for audit/history.

These are preceded by current correction sections stating the live status and by historical headings warning not to use the retained material as current state.

## verification_outputs

### `git status --short`

```text
 M README.md
 M commands/load-mnemosyne-guidance.md
 M current/active-context.md
 M current/open-questions.md
 M current/todo.md
 M handoff/handoff-current.md
 M handoff/startup-instructions.md
 M notes/v0.1-scope-and-consistency-check.md
?? notes/codex-task-results/MNEMOSYNE-045-result.md
```

### `git diff HEAD --stat`

```text
 README.md                                 |   2 +-
 commands/load-mnemosyne-guidance.md       |   6 +-
 current/active-context.md                 | 124 ++++-------
 current/open-questions.md                 |  30 +++
 current/todo.md                           |  39 ++++
 handoff/handoff-current.md                | 284 +++-----------------------
 handoff/startup-instructions.md           | 329 ++----------------------------
 notes/v0.1-scope-and-consistency-check.md |   7 +
 8 files changed, 167 insertions(+), 654 deletions(-)
```

### `git diff HEAD --name-only`

```text
README.md
commands/load-mnemosyne-guidance.md
current/active-context.md
current/open-questions.md
current/todo.md
handoff/handoff-current.md
handoff/startup-instructions.md
notes/v0.1-scope-and-consistency-check.md
```

### `git diff HEAD --   README.md   current/active-context.md   handoff/handoff-current.md   handoff/startup-instructions.md   current/todo.md   current/open-questions.md   notes/v0.1-scope-and-consistency-check.md   commands/load-mnemosyne-guidance.md   notes/codex-task-results/MNEMOSYNE-045-result.md`

```text
diff --git a/README.md b/README.md
index 7a0eafc..4a95468 100644
--- a/README.md
+++ b/README.md
@@ -2,7 +2,7 @@
 
 Mnemosyne 是一个用于设计、演化和交付 AI Agent 外部持久记忆系统的“记忆系统元 Agent”工作仓库。
 
-这是一个公开（public）设计工作仓库，不是传统软件开发项目。请勿向本仓库提交敏感/私有材料；仓库可见性未来即使改变，也不会自动消除既有 Git 历史中的暴露。
+这是一个设计工作仓库，不是传统软件开发项目。仓库可见性由用户控制，可能随 construction / operation 阶段在 public/private 之间变化。向仓库放入材料前必须核验当前可见性；当仓库为 public 或可见性未核实时，只允许放入公开、合成或已明确脱敏的材料。后续可见性变化不会消除既有 Git 历史暴露。
 
 核心原则：**模型负责计算，文件负责记忆。**
 
diff --git a/commands/load-mnemosyne-guidance.md b/commands/load-mnemosyne-guidance.md
index 1bd47b3..3c94f67 100644
--- a/commands/load-mnemosyne-guidance.md
+++ b/commands/load-mnemosyne-guidance.md
@@ -20,6 +20,7 @@ Use this one-line command at the beginning of a new ChatGPT conversation, Codex
 
 At minimum, read or ask the user to provide:
 
+- `README.md`
 - `current/human-approved-spec.md`
 - `current/active-context.md`
 - `handoff/handoff-current.md`
@@ -41,14 +42,15 @@ If the task involves tool capability, platform capability, model behavior, autom
 7. If the response asks the user to do something, put the operation steps/content in a clearly marked section before explanation.
 8. If the response reports findings or conclusions, put the conclusion/problem/result in a clearly marked section before supporting explanation.
 9. Apply the long-transfer file/chunking guidance from `current/human-approved-spec.md`. When producing long content for the user to manually forward, prefer generating a downloadable file and show only a concise summary in the chat. If the content must be split, label chunks with package/task title, stable ID, chunk number, total chunk count if known, and wait-for-all-chunks instruction.
-10. The first response after loading should include:
+10. Treat repository visibility as operator-controlled and stage-dependent; do not treat public/private state alone as a defect. Verify visibility when relevant, especially before imports, and apply the MNEMOSYNE-043 safety gate.
+11. The first response after loading should include:
    - current execution source;
    - current phase;
    - non-execution-source boundaries;
    - current forbidden actions;
    - current next-route options;
    - whether any conflict or missing file was found.
-11. If required files are unavailable, ask for the missing files or clearly state the limitation. Do not invent repository state.
+12. If required files are unavailable, ask for the missing files or clearly state the limitation. Do not invent repository state.
 
 ## Boundaries
 
diff --git a/current/active-context.md b/current/active-context.md
index f3509a1..c30059a 100644
--- a/current/active-context.md
+++ b/current/active-context.md
@@ -1,110 +1,56 @@
 # Active Context
 
+## Current compact view
 
-## MNEMOSYNE-043 public repository and manual-import safety gate
+### current phase
 
-- Current GitHub metadata checked on 2026-06-22 reports `08822407d/Mnemosyne` as `public`; future sessions must reverify repository visibility when relevant because visibility is time-sensitive.
-- For public or unverified repository visibility, do not upload secrets, credentials, private source, customer/confidential material, unapproved personal data, or other sensitive material into `manual-import-inbox/`; use only public, synthetic, or explicitly redacted material.
-- Removing or moving a staged file later does not itself remove the file from Git history.
-- OP-08 remains open/partially addressed: this task adds a safety default for manual imports, not a complete privacy/redaction/access-control policy.
-- Current execution source remains `current/human-approved-spec.md`.
+- Post-MNEMOSYNE-044 Batch A current-state cleanup.
+- Batch A small fixes are being completed before any Batch B work begins.
+- Near-term construction priority remains target-project readiness: make Mnemosyne practically usable for designing and helping build persistent-memory frameworks for real target projects.
 
-## MNEMOSYNE-042 user-action-first reply format
+### current execution source
 
-- MNEMOSYNE-042 clarifies user-action-first reply format for Mnemosyne-affiliated ordinary ChatGPT conversations.
-- `操作内容` means user-required manual actions; use `## 无需用户操作` when no user action is needed.
-- Current execution source remains `current/human-approved-spec.md`.
+- `current/human-approved-spec.md` is the current and only execution source.
+- Active context, handoff, TODO, open questions, research reports, candidates, decision logs, and Codex result records are not execution source.
 
+### latest completed checkpoints
 
+- MNEMOSYNE-040: DR1 memory-system testing/debugging/evaluation evidence ingested as `RC-2026Q2-memory-testing`; DR1 is evidence only, not execution source.
+- MNEMOSYNE-041: manual import inbox workflow established for current Codex Cloud non-image attachment limitations.
+- MNEMOSYNE-042: user-action-first reply format added to the execution source.
+- MNEMOSYNE-043: manual-import safety gate established; public or unverified visibility allows only public, synthetic, or explicitly redacted material.
+- MNEMOSYNE-044: D-01–D-07 execution-source coverage map created; execution status comes from the coverage map plus `current/human-approved-spec.md`.
 
+### current blockers/gates
 
-## MNEMOSYNE-041 status
+- Do not begin Batch B until the current gate says ready.
+- Unpromoted checkpoint/candidate/research content is not executable.
+- First target-project dry-run remains design-only and uses public/synthetic/explicitly redacted input by default until separately approved.
+- Manual imports must apply the MNEMOSYNE-043 safety gate and stop on unsafe or ambiguous material.
 
-- MNEMOSYNE-041 adds a manual import inbox workflow for current Codex Cloud non-image attachment limitations.
-- `manual-import-inbox/` is temporary staging only: not execution source, raw evidence, canonical research/report storage, or delivery storage.
-- Future inbox-handling tasks must preflight-inventory files, verify names/types/destinations, and stop on missing or ambiguous files rather than guessing.
-- Current execution source remains `current/human-approved-spec.md`.
+### current next route
 
-## MNEMOSYNE-040 DR1 memory-testing evidence ingestion
+- Finish Batch A small fixes, including this current-state consolidation and startup read-path cleanup.
+- After the gate says ready, MNEMOSYNE-046 should convert DR1 implications into a minimal checklist/profile for the first target-project dry-run.
+- Do not treat old pre-039 route-selection text as the current route.
 
-- MNEMOSYNE-040 normalized and ingested DR1 memory-system testing/debugging/evaluation evidence as `RC-2026Q2-memory-testing`.
-- DR1 report id: `RPT-2026Q2-MT-0001`; prompt id: `PROMPT-2026Q2-MT-0001`.
-- DR1 is research evidence only, not execution source; current execution source remains `current/human-approved-spec.md`.
-- OP-09 and OP-10 are partially answered by DR1, not fully answered.
-- Current-stage implication: favor a half-automatic, file-backed, human-reviewable, traceable evaluation loop instead of a fully automated meta-agent/test framework.
-- First target-project dry-run should observe execution-source reading, handoff executability, active-context decision propagation, layer separation, uncertainty handling, artifact usability by a next executor, and honest tool-capability boundaries.
-- Multi-model independent review is an auxiliary second-opinion method only; it is not truth voting, execution source, or automatic writeback authority.
+### important non-execution-source references
 
-## MNEMOSYNE-039 Pro quota refresh plan
+- `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md` for D-01–D-07 reflection/promotion status.
+- `notes/codex-task-results/MNEMOSYNE-039-result.md` through `notes/codex-task-results/MNEMOSYNE-044-result.md` for recent task outcomes.
+- `manual-import-inbox/README.md` and `notes/manual-import-inbox-workflow.md` for import tasks only.
+- Research current views under `raw/research-reports/current/` for tool/capability/new mechanism/target-project design questions.
 
-- MNEMOSYNE-039 records the Pro quota refresh work plan.
-- Priority 1 Deep Research is memory-system testing/debugging/evaluation/failure diagnosis.
-- Ordinary ChatGPT-Pro should run a comprehensive Mnemosyne health review before or alongside the first target-project dry-run.
-- These are planning/TODO items, not execution-source changes.
-- Current execution source remains `current/human-approved-spec.md`.
+### visibility context
 
-## MNEMOSYNE-038 status
+- Repository visibility is user-controlled and may alternate between public/private by stage.
+- Current visibility must be reverified when material is imported.
+- Visibility state alone is not a repair issue.
+- MNEMOSYNE-043 safety rules remain applicable.
 
-- MNEMOSYNE-038 recovered and indexed six light-research prompt originals for `PROMPT-2026Q2-0002` through `PROMPT-2026Q2-0007`.
-- The previous `missing_original_prompt` status for those six prompts is superseded by `available_original_prompt`.
-- The recovered prompts are research inputs, not execution source and not research conclusions.
-- Current execution source remains `current/human-approved-spec.md`.
+## Historical / superseded context below
 
-## MNEMOSYNE-037 status
-
-- MNEMOSYNE-037 adds long-transfer file/chunking guidance to the execution source.
-- MNEMOSYNE-037 records near-term target-project readiness as the current construction priority in non-execution-source construction/context notes.
-- The current near-term goal is to reach a practical ability to design and help build persistent-memory frameworks for other projects, rather than endlessly refining Mnemosyne internal process details.
-- No `AGENTS.md`, `CLAUDE.md`, GitHub Actions, or automation was added.
-- Current execution source remains `current/human-approved-spec.md`.
-
-
-## MNEMOSYNE-036 status
-
-- MNEMOSYNE-036 records construction-stage understanding and artifact-boundary clarifications as non-execution-source notes / candidates / open questions.
-- current/human-approved-spec.md was not modified by this task.
-- Core additions include prototype-stage framing, ChatGPT-to-Codex writeback loop, evidence-guided self-improvement, HADB terminology, agent-operational artifact boundary, and indexing as research-gated performance optimization.
-- Current execution source remains `current/human-approved-spec.md`.
-
-## 当前阶段
-
-MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 dry-run independent verification 已完成，final verdict 为 PASS。当前近程 construction priority 是尽快让 Mnemosyne 可用于为真实 target projects 设计并帮助构建 persistent-memory frameworks；后续路线仍可在 PDF 图表复核、Idea Capture Buffer / candidate cleanup、template review / small fixes、memory-system testing/debugging feasibility research 或 first real target-project dry-run 之间选择，但应优先评估其是否直接支持 target-project readiness。
-
-## MNEMOSYNE-035 status
-
-- Operation/conclusion separation guidance has been added to the execution source.
-- The load command has been updated to apply the guidance.
-- No `AGENTS.md`, `CLAUDE.md`, GitHub Actions, or automation was added.
-- Current execution source remains `current/human-approved-spec.md`.
-
-## MNEMOSYNE-034 status
-
-- Objective neutral engineering stance has been added to the execution source.
-- `commands/` registry has been added for lightweight user-facing guidance shortcuts.
-- No `AGENTS.md`, `CLAUDE.md`, GitHub Actions, or automation was added.
-- Current execution source remains `current/human-approved-spec.md`.
-
-## MNEMOSYNE-031 current status
-
-MNEMOSYNE-031 final writeback checkpoint status:
-
-- R1/R2/R3 user review completed; no major issue reported by user.
-- R4A prompt list completed.
-- R4B user restatement completed: 9 main records + 1 addendum.
-- R4B manifest/index completed.
-- R4C synthesis completed as candidate draft, not execution source.
-- R5 review completed through user confirmation of D-01 to D-07.
-- Final writeback package prepared and checkpointed.
-- Current execution source remains `current/human-approved-spec.md`.
-- No PDF figure/table/image/layout review should be claimed.
-- Original R5 draft is superseded by final user-confirmed decisions where they differ.
-
-Next route should be selected by the user:
-
-- PDF figure/table/image review;
-- MNEMOSYNE-032 first dry-run has completed independent verification with verdict `PASS`;
-- Idea Capture Buffer / candidate requirements cleanup;
-- template pack review / small fixes if needed.
+The material below is retained for audit/history and may include superseded route wording. Do not use it as the current route when it conflicts with the compact current view above or with later task result records.
 
 ## 当前执行源
 
diff --git a/current/open-questions.md b/current/open-questions.md
index 049f6ec..3bdd2b2 100644
--- a/current/open-questions.md
+++ b/current/open-questions.md
@@ -1,5 +1,35 @@
 # Open Questions
 
+> Current execution source remains `current/human-approved-spec.md`. This file is not execution source.
+
+## Current corrections
+
+- Recovered light prompts are no longer a future hypothetical; MNEMOSYNE-038 recovered and indexed them.
+- R4/R5 route-selection wording is superseded; use the MNEMOSYNE-044 coverage map for D-01–D-07 promotion/reflection status.
+- DR1 research priority is answered for the current cycle; DR1 research and ingestion are complete.
+- OP-09 and OP-10 remain partially answered by DR1, not closed.
+- OP-08 remains open/partially addressed as a broader privacy/redaction/access-control question.
+- Repository public/private selection is not an open defect question because visibility is user-controlled. Verify visibility before imports and apply the safety gate.
+- D-promotion questions point to `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md`.
+
+## Current open questions
+
+- OP-08: What broader privacy/redaction/access-control rule should govern original-source materials if sensitive content appears?
+  - status: partially_addressed_by_MNEMOSYNE_043
+- OP-09: Can current models reliably perform memory-system testing / debugging / root-cause diagnosis?
+  - status: partially_answered_by_DR1
+- OP-10: Are there mature industry practices or successful examples for memory-system testing/debugging in AI-Agent teams?
+  - status: partially_answered_by_DR1
+- OP-11: When should handoff-local exceptions be promoted into global execution-source changes, and what approval form is required?
+- Which template-pack small fixes, if any, should precede the first target-project dry-run?
+- Which first target-project scenario should be used when dry-run work is approved?
+
+## Historical open-question list below
+
+The material below is retained for history and may include superseded route wording. Use the current corrections above for live status.
+
+# Open Questions
+
 > MNEMOSYNE-031 final checkpoint records are non-execution-source review/restatement records. Current execution source remains `current/human-approved-spec.md`.
 
 ## answered
diff --git a/current/todo.md b/current/todo.md
index 13c1999..a4f30ac 100644
--- a/current/todo.md
+++ b/current/todo.md
@@ -1,5 +1,44 @@
 # TODO
 
+## Active now
+
+- Complete Batch A small fixes and current/startup cleanup.
+- Keep current execution source unchanged unless a future user-approved task explicitly edits `current/human-approved-spec.md`.
+- Maintain the MNEMOSYNE-043 manual-import safety gate when imports occur.
+
+## Waiting for user decision
+
+- Whether to review or revise existing template packs before the first target-project dry-run.
+- Which first target-project scenario to use when dry-run work is approved.
+- Whether any D-01–D-07 candidate wording from the MNEMOSYNE-044 coverage map should be promoted into the execution source.
+
+## Waiting for dry-run evidence
+
+- First target-project dry-run remains design-only and public/synthetic/explicitly redacted by default until separately approved.
+- DR1 checklist/minimal-profile work should be handled by MNEMOSYNE-046, not by treating DR1 research itself as executable.
+
+## Deferred / future
+
+- PDF figure/table/image manual review.
+- Candidate/idea cleanup beyond this current-state consolidation.
+- Optional DR2 or additional research only if a future design question needs it.
+- Platform/visibility reverification when importing files or when repository visibility materially affects the task. Do not add a recurring TODO to change repository visibility merely because it is public.
+
+## Recently completed
+
+- Comprehensive Health Review is completed by Batch A current-state work.
+- DR1 research and ingestion are completed by MNEMOSYNE-040.
+- Idea Capture Buffer creation is completed.
+- Old “choose route after 032” items are superseded by the current Batch A -> gate -> MNEMOSYNE-046/dry-run route.
+- Manual-import safety gate is complete in MNEMOSYNE-043.
+- D-decision mapping is complete in MNEMOSYNE-044.
+
+## Historical detailed task list below
+
+The material below is retained for history and may contain superseded pending/completed wording. Use the current view above for live status.
+
+# TODO
+
 > MNEMOSYNE-031 final checkpoint records are non-execution-source review/restatement records. Current execution source remains `current/human-approved-spec.md`.
 
 ## v0.1-final
diff --git a/handoff/handoff-current.md b/handoff/handoff-current.md
index 76f57b6..468907f 100644
--- a/handoff/handoff-current.md
+++ b/handoff/handoff-current.md
@@ -8,267 +8,41 @@ Mnemosyne
 
 Mnemosyne 是记忆系统元 Agent 工作仓库，用于设计、演化和交付 AI Agent 外部持久记忆系统。
 
+## Immediate current continuation
 
+- Batch A small fixes are being completed.
+- Do not begin Batch B until the current gate says ready.
+- D-01–D-07 execution status comes from `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md` plus `current/human-approved-spec.md`.
+- Unpromoted checkpoint content is not executable.
+- First target-project dry-run remains design-only and uses public/synthetic/explicitly redacted input by default until separately approved.
+- Repository visibility is intentionally user-controlled; do not propose a visibility change merely because the repository is public.
+- Always verify visibility before importing material and apply the MNEMOSYNE-043 safety gate.
 
-## MNEMOSYNE-043 public repository and manual-import safety gate
+## Current execution source
 
-- Current GitHub metadata checked on 2026-06-22 reports `08822407d/Mnemosyne` as `public`; future sessions must reverify repository visibility when relevant because visibility is time-sensitive.
-- For public or unverified repository visibility, do not upload secrets, credentials, private source, customer/confidential material, unapproved personal data, or other sensitive material into `manual-import-inbox/`; use only public, synthetic, or explicitly redacted material.
-- Removing or moving a staged file later does not itself remove the file from Git history.
-- OP-08 remains open/partially addressed: this task adds a safety default for manual imports, not a complete privacy/redaction/access-control policy.
-- Current execution source remains `current/human-approved-spec.md`.
+- `current/human-approved-spec.md` is the only execution source.
+- If any handoff/current/research/candidate/result file conflicts with the spec, follow the spec and record an open question.
 
-## MNEMOSYNE-042 user-action-first reply format
+## Key prohibitions
 
-- MNEMOSYNE-042 clarifies that `操作内容` means human-required manual steps, not assistant internal plans, tool calls, or background analysis.
-- Use `## 操作内容（需要你手动执行）` when manual user action is required.
-- Use `## 无需用户操作` when no manual user action is required.
-- Current execution source remains `current/human-approved-spec.md`.
+- Do not treat raw records, research reports, candidate requirements, decision logs, active-context, handoff, startup instructions, or task result records as execution source.
+- Do not claim PDF figure/table/image/layout review unless it was actually performed.
+- Do not commit secrets, credentials, private source, customer/confidential material, unapproved personal data, or other sensitive material.
+- Do not treat multi-model review as truth voting, execution source, or automatic writeback authority.
+- Do not create AGENTS.md, CLAUDE.md, GitHub Actions, automation, MCP, RAG, or auto-writeback unless explicitly approved by a current task.
+- Do not use unpromoted MNEMOSYNE-031 R4/R5 material as executable requirements; use the coverage map for promotion status.
 
+## Recent checkpoints
 
+- MNEMOSYNE-040: DR1 memory-testing/debugging/evaluation evidence ingested; OP-09 and OP-10 are partially answered, not closed.
+- MNEMOSYNE-041: manual import inbox workflow established.
+- MNEMOSYNE-042: user-action-first reply format added to execution source.
+- MNEMOSYNE-043: manual-import safety gate established.
+- MNEMOSYNE-044: D-01–D-07 execution-source coverage map created.
 
+## Next route
 
-## MNEMOSYNE-041 manual import inbox workflow
-
-- MNEMOSYNE-041 adds `manual-import-inbox/` as the preferred temporary staging location when non-image files must be manually placed into the repository for Codex Cloud work.
-- Tasks must inventory and verify inbox files and canonical destinations before processing; do not assume file existence, guess ambiguous names, or treat inbox files as canonical storage.
-- Current execution source remains `current/human-approved-spec.md`.
-
-## MNEMOSYNE-040 DR1 memory-testing evidence
-
-- DR1 memory-system testing/debugging/evaluation Deep Research has been normalized and ingested as supplemental current research evidence cycle `RC-2026Q2-memory-testing`.
-- Report: `RPT-2026Q2-MT-0001`; prompt: `PROMPT-2026Q2-MT-0001`.
-- Summary: `raw/research-reports/cycles/2026Q2-memory-testing/report-summaries/DR1_memory_testing_debugging_evidence_review_summary.md`.
-- OP-09 and OP-10 are now `partially_answered_by_DR1`.
-- DR2 optional multi-model independent review research is not currently required unless future template/review-package design needs deeper evidence.
-- Multi-model review is auxiliary second-opinion review only, not truth voting, execution source, or automatic writeback authority.
-- Before or during the first real target-project dry-run, convert DR1 implications into a minimal checklist for execution-source reading, handoff executability, active-context propagation, layer separation, uncertainty handling, artifact landability, and honest tool capability limits.
-
-## MNEMOSYNE-039 Pro quota refresh plan
-
-- Next high-value Pro work is the MNEMOSYNE-039 plan.
-- If the user says the Pro quota has refreshed, guide them to run the Priority 1 Deep Research prompt first: AI Agent external persistent memory system testing/debugging/evaluation/failure diagnosis.
-- Then perform or continue the ordinary ChatGPT-Pro Comprehensive Health Review.
-- Do not treat research outputs as execution source.
-- Any repo changes after review/research should go through Codex tasks and PR review.
-
-## MNEMOSYNE-038 recovered light research prompts
-
-- MNEMOSYNE-038 recovered and indexed six light-research prompt originals for `PROMPT-2026Q2-0002` through `PROMPT-2026Q2-0007`.
-- The previous `missing_original_prompt` status for those six prompts is superseded by `available_original_prompt`.
-- The recovered prompts are research inputs, not execution source and not research conclusions.
-- Current execution source remains `current/human-approved-spec.md`.
-
-## MNEMOSYNE-036 construction-stage understanding / artifact boundary
-
-- Read `notes/mnemosyne-construction-stage-understanding.md` when discussing Mnemosyne construction-stage assumptions, HADB, artifact boundaries, or indexing.
-- The note is not execution source.
-- Do not treat the new ideas as approved spec.
-- The ChatGPT-to-Codex writeback loop is recognized as normal construction workflow: ordinary ChatGPT can generate Codex tasks; Codex performs reviewed repo writes.
-
-## MNEMOSYNE-037 long-transfer guidance / target-project readiness
-
-- MNEMOSYNE-037 adds long-transfer file/chunking guidance.
-- Long content intended for manual forwarding should prefer downloadable files.
-- Multi-message transfer should use clear chunk metadata.
-- MNEMOSYNE-037 also records near-term target-project readiness as the current construction priority.
-- Current execution source remains `current/human-approved-spec.md`.
-
-## 当前阶段
-
-MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 first dry-run independent verification 已完成，final verdict 为 PASS。当前近程 construction priority 是尽快让 Mnemosyne 可用于为真实 target projects 设计并帮助构建 persistent-memory frameworks；后续路线仍可在 PDF 图表复核、Idea Capture Buffer / candidate cleanup、template review / small fixes、memory-system testing/debugging feasibility research 或 first real target-project dry-run 之间选择，但应优先评估其是否直接支持 target-project readiness。
-
-## MNEMOSYNE-034 objective engineering stance / command registry
-
-- MNEMOSYNE-034 adds an objective neutral engineering stance to the execution source and adds a lightweight `commands/` registry.
-- New sessions can use “Load Mnemosyne guidance.” / “加载 Mnemosyne 指导约束。” when repository guidance is not automatically loaded.
-- Command files are not execution source.
-
-## MNEMOSYNE-035 operation/conclusion separation guidance
-
-- MNEMOSYNE-035 adds operation/conclusion separation guidance.
-- Mnemosyne-affiliated sessions should not bury required user actions, problems, or conclusions inside long analysis.
-- Current execution source remains `current/human-approved-spec.md`.
-
-## 当前执行源
-
-`current/human-approved-spec.md`
-
-以下文件不是执行源：
-
-- `raw/`
-- `raw/research-reports/`
-- `raw/research-reports/current/current-research-prompts.md`
-- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
-- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`
-- `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
-- `raw/research-reports/cycles/2026Q2-initial/report-summaries/`
-- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
-- `raw/research-reports/current/current-report-summaries.md`
-- `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md`
-- `raw/user-design-restatements/MNEMOSYNE-031-user-design-intent-restatement.md`
-- `notes/candidate-requirements.md`
-- `notes/decision-log.md`
-- `current/active-context.md`
-- `handoff/handoff-current.md`
-- `handoff/startup-instructions.md`
-- `notes/system-construction-baseline.md`
-- `notes/overall-target-and-roadmap-snapshot.md`
-- `notes/self-improvement-template-pack.md`
-- `notes/target-project-memory-system-template-pack.md`
-- `notes/delivery-manifest-template-pack.md`
-- `notes/template-pack-review-and-first-scenario-selection.md`
-
-如果其他文件与 `human-approved-spec` 冲突，以 `human-approved-spec` 为准，并登记 open question。
-
-## 研究证据层状态
-
-7 份研究报告已作为 `RC-2026Q2-initial` 入库；MNEMOSYNE-030C 已补充该轮研究的 origin / motivation 文件。DR1 memory-testing report 已作为补充当前证据轮次 `RC-2026Q2-memory-testing` 入库。
-
-当前研究证据入口：
-
-- `raw/research-reports/current/research-report-index.md`
-- `raw/research-reports/current/current-evidence-map.md`
-- `raw/research-reports/current/current-capability-boundaries.md`
-- `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
-- `raw/research-reports/current/current-report-summaries.md`
-- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
-- `raw/research-reports/current/current-research-prompts.md`
-- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
-- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`
-
-研究报告主要供元 Agent 使用，是高权重证据层，不是执行源；不要求或假定用户已经通读、掌握全部报告。元 Agent 应据此进行可行性评价、能力边界确认、当前实践对照和现代化优化建议。PDF 图表和图片仍需人工复核。
-
-MNEMOSYNE-031 增加用户构想重述：先由 AI 整理待重述清单，再由用户口语化重述。重述结果不是原始需求、不是最终设计、不是执行源。
-
-## MNEMOSYNE-031 continuation point
-
-MNEMOSYNE-031 has reached the final writeback checkpoint.
-
-Completed:
-- R1 Research Motivation Review.
-- R2 Research Prompts and Topic Mapping Review.
-- R3 Report Summaries Review.
-- R4A User Design Intent Restatement Prompt List.
-- R4B user oral restatement: 9 main records + 1 addendum.
-- R4B manifest/index.
-- R4C user design intent synthesis / candidate requirements draft.
-- R5 final D-01 to D-07 user decision review.
-- Final checkpoint records.
-
-Current continuation:
-- Do not resume from R4B.
-- Do not regenerate R4B, R4C, or R5.
-- Use `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md` to distinguish final D-01 to D-07 checkpoint records from content currently executable through `current/human-approved-spec.md`; do not use the unsuperseded R5 draft alone.
-- Next route should be selected by the user: PDF figure review / Idea Capture Buffer / candidate cleanup / template review / memory-system testing-debugging feasibility research.
-
-Historical note:
-- Earlier MNEMOSYNE-031 checkpoint/status-sync files that say R4B/R4C/R5 are pending are historical records from before the final checkpoint.
-- They are superseded for current continuation purposes by the final checkpoint record and this handoff section.
-
-## MNEMOSYNE-032 dry-run independent verification status
-
-- A read-only independent verification of the MNEMOSYNE-032 dry-run artifacts on `master` has completed.
-- Final independent verdict: `PASS`.
-- Invalid-test trigger: `false`.
-- Blocking issues: none.
-- Verification detail report: `notes/dry-runs/MNEMOSYNE-032/MNEMOSYNE-032-independent-verification-detail.md`.
-- Dry-run artifacts remain validation evidence only. They are not execution source, not final Mnemosyne design, and do not modify `current/human-approved-spec.md`.
-- Status files were intentionally not updated by the dry-run itself because status updates were outside the dry-run permission scope; MNEMOSYNE-032F records the authorized status update.
-
-## Codex / ChatGPT task verification reminder
-
-MNEMOSYNE-031 showed that natural-language Codex task descriptions may fail to produce all intended file edits. For future repository-editing tasks, read:
-
-- `notes/codex-task-authoring-and-diff-verification-guidelines.md`
-
-When generating or executing Codex tasks that modify files, require actual diff evidence: `git status --short`, `git diff HEAD --stat`, `git diff HEAD --name-only`, targeted `git diff HEAD -- <target files>`, protected-file checks, and task result records comparing intended files with actual changed files.
-
-## 新会话推荐读取顺序
-
-1. `README.md`
-2. `current/human-approved-spec.md`
-3. `current/active-context.md`
-4. `handoff/handoff-current.md`
-5. `handoff/startup-instructions.md`
-6. `current/open-questions.md`
-7. `current/todo.md`
-8. `notes/codex-task-authoring-and-diff-verification-guidelines.md`
-9. `notes/v0.1-scope-and-consistency-check.md`
-10. `notes/v0.1-final-review.md`
-11. `notes/requirement-intake-workflow.md`
-12. `notes/self-improvement-workflow.md`
-13. `notes/self-improvement-template-pack.md`
-14. `notes/target-project-memory-system-template-pack.md`
-15. `notes/delivery-manifest-template-pack.md`
-16. `notes/template-pack-review-and-first-scenario-selection.md`
-17. `notes/research-review-and-user-intent-restatement-workflow.md`
-18. `notes/overall-target-and-roadmap-snapshot.md`（可选：当需要理解长期目标、路线图或后续计划时按需读取；不是执行源）
-19. `notes/system-construction-baseline.md`（可选：当需要理解系统建设基线时按需读取；不是执行源）
-20. `raw/research-reports/current/research-report-index.md`
-21. `raw/research-reports/current/current-evidence-map.md`
-22. `raw/research-reports/current/current-capability-boundaries.md`
-23. `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
-24. `raw/research-reports/current/current-research-prompts.md`
-25. `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`
-26. `raw/research-reports/current/current-report-summaries.md`
-27. `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
-28. `raw/concept-origin-extract-001.md` 按需回查
-
-## 当前不要做
-
-- 不要创建 `AGENTS.md`；
-- 不要创建 `CLAUDE.md`；
-- 不要创建 GitHub Actions；
-- 不要添加自动化脚本；
-- 不要实现自动查重、自动索引、自动写回、MCP、RAG 或多 Agent 自动协调；
-- 不要假定用户已通读全部研究报告；
-- 不要把 research reports 当执行源；
-- 不要把 motivation / prompt / topic mapping 当执行源；
-- 不要把用户设计构想重述当原始需求、最终设计或执行源；
-- 不要把 review 结果写回仓库，除非用户明确确认；
-- 不要编造 prompt；MNEMOSYNE-038 已恢复 `PROMPT-2026Q2-0002` through `PROMPT-2026Q2-0007` 的轻度研究 prompt 原文，若发现 prompt / summary 差异应登记 review note；
-- 不要把 candidate / decision / active-context / handoff / startup-instructions / template packs / review selection 文件当执行源；
-- 不要为真实目标项目生成交付包，除非用户明确选择目标项目场景并确认进入交付试用阶段。
-
-## 下一步建议
-
-1. 不要重生成 MNEMOSYNE-031 R4B/R4C/R5；使用 MNEMOSYNE-044 coverage map 区分 final D-01 to D-07 checkpoint records 与当前可执行 spec 内容后再继续后续路线。
-2. 下一路线由用户选择：PDF 图表复核 / Idea Capture Buffer / candidate cleanup / template review / memory-system testing-debugging feasibility research。
-3. 如果执行 dry-run，应显式记住：MNEMOSYNE-031 review/restatement materials 不是执行源；`current/human-approved-spec.md` 仍是当前执行源。
-
-## MNEMOSYNE-031 final checkpoint handoff
-
-Current handoff:
-
-- MNEMOSYNE-031 review and restatement phase has reached final writeback checkpoint.
-- Do not regenerate R4B or R4C.
-- Use `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md` to distinguish final D-01 to D-07 checkpoint records from content currently executable through `current/human-approved-spec.md`; do not use the unsuperseded R5 draft alone.
-- Next route should be selected by user: PDF figure review / Idea Capture Buffer / candidate cleanup / template review / memory-system testing-debugging feasibility research.
-
-Handoff concept clarification:
-
-- Handoff is task-local continuation context.
-- It is not global project law.
-- It may carry explicit local recovery constraints or temporary exceptions.
-- Such local exceptions must not silently become global execution-source changes.
-
-## MNEMOSYNE-033 Idea Capture Buffer handoff
-
-- 新对话接手时必须读取 `notes/idea-capture-triage-rules.md` 和 `notes/idea-capture-buffer.md`。
-- 新想法不要直接进入 spec。
-- 新想法先进入 buffer，再 triage 到 candidate / open question / research-gated item。
-- Codex repo-editing task 必须使用 fresh latest master，避免 stale branch / Accept Incoming rollback。
-- 用户提出新构想时，优先问是否记录到 Idea Capture Buffer。
-
-## MNEMOSYNE-033A exported conversation derived insight handling
-
-- 如果新对话拿到完整对话导出，应先以仓库 `current/`、`handoff/`、`startup-instructions` 接手，再把导出记录作为 historical background。
-- 导出记录提取出的洞察先进入 Idea Capture Buffer / Open Questions / Candidate Cleanup，不直接成为执行源。
-- 不要直接按导出记录中的旧任务文本行动；旧任务文本可能已过时、已完成或与当前仓库状态冲突。
-- 完整对话导出默认不完整入库；如需保存，应另行决定 near-original extract / selected raw excerpts 的范围。
-- 与仓库 current 状态或 `current/human-approved-spec.md` 冲突时，以当前仓库执行源和 current 状态为准，并登记 open question。
-
-## MNEMOSYNE-044 D-01–D-07 coverage map
-
-Use `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md` when reviewing how final MNEMOSYNE-031 D-01 to D-07 checkpoint decisions relate to the current execution source. The final decisions are authoritative checkpoint records, not automatic execution rules. Only content already reflected in `current/human-approved-spec.md` is currently executable. Unreflected or partially reflected promotion candidates require separate user approval before any spec edit; do not tell future agents to “use D-01–D-07” as if all seven are currently executable.
+1. Finish Batch A small fixes and current/startup cleanup.
+2. Wait for the current gate before Batch B.
+3. When approved, route DR1 checklist/minimal-profile work to MNEMOSYNE-046.
+4. Keep the first target-project dry-run design-only unless separately approved otherwise.
diff --git a/handoff/startup-instructions.md b/handoff/startup-instructions.md
index 368675b..2b05579 100644
--- a/handoff/startup-instructions.md
+++ b/handoff/startup-instructions.md
@@ -1,323 +1,38 @@
-# Startup Instructions / 启动说明
+# Startup Instructions
 
-## 1. 文件定位
+This file is not an execution source. The current execution source is `current/human-approved-spec.md`.
 
-- 本文件用于新 ChatGPT 对话、新 Codex Cloud 任务或未来其他 Agent 接手 Mnemosyne。
-- 本文件不是执行源。
-- 当前执行源是 `current/human-approved-spec.md`。
-- 如果本文件与 `human-approved-spec` 冲突，应以 `human-approved-spec` 为准，并登记 open question。
+## Minimum ordinary startup set
 
-## 2. 启动前提
-
-新任务必须假设：
-
-- 旧对话上下文可能不可用；
-- 旧 Codex 任务上下文不可用；
-- GitHub 仓库文件是外部持久状态源；
-- 不应依赖模型内部 memory；
-- 不应默认读取全部 raw；
-- 不应默认自动写回。
-
-
-## 2.1 客观中立工程风格与命令入口
-
-- Mnemosyne 所属 ChatGPT 对话、Codex 任务或未来 Agent 任务应遵循 `current/human-approved-spec.md` 中的客观中立工程风格原则：以执行源、仓库规则、可验证仓库状态、可验证当前工具 / 平台事实、可靠科学技术事实和明确不确定性为依据。
-- 如果新的 ChatGPT 对话或 Codex 任务不能自动加载仓库指导，用户可以说：
-  - “Load Mnemosyne guidance.”
-  - “加载 Mnemosyne 指导约束。”
-- 可用命令列在 `commands/README.md`。
-- `commands/` 命令注册表不是执行源，不能覆盖 `current/human-approved-spec.md`。
-- Mnemosyne 所属会话应将操作步骤 / 操作内容与说明性分析分离，并将问题报告、结论和验证结果与支撑性说明分离。
-- For Mnemosyne-affiliated ordinary ChatGPT replies, distinguish user-required actions from assistant work: if the user must do something, start with `## 操作内容（需要你手动执行）`; if not, start with `## 无需用户操作`.
-- 这对 Codex task prompts、GitHub 操作、onboarding verification 和新旧对话 handoff 尤其重要。
-- 该规则的执行源位于 `current/human-approved-spec.md`。
-- Mnemosyne 所属会话在生成需要用户手动转发到另一段对话或 Codex Cloud task 的长内容时，应优先使用 downloadable file，并在聊天中只保留简明摘要 / 指针。
-- 如果内容必须跨多个用户消息分片转发，应使用 chunk metadata 和 continuation markers，让接收方理解这些片段属于一个逻辑输入。
-- 这对 Codex task prompts、handoff packages、onboarding packages、verification packages 和长指令尤其重要；执行源规则位于 `current/human-approved-spec.md`。
-- When non-image files need to enter the repository and the user wants to avoid manually creating deep directories, prefer the temporary staging folder `manual-import-inbox/`.
-- After the user says files have been added, verify `manual-import-inbox/` and any canonical destination paths before acting; do not invent file existence or locations.
-- Inbox files are not canonical until verified and moved/copied to the correct repository paths.
-- Current GitHub metadata checked on 2026-06-22 reports `08822407d/Mnemosyne` as `public`; reverify repository visibility when relevant because visibility can change.
-- If repository visibility is public or unverified, only public, synthetic, or explicitly redacted material may be uploaded to `manual-import-inbox/`; do not upload secrets, credentials, private source, customer/confidential material, or unapproved personal data.
-- Removing or moving an uploaded file later does not itself remove it from Git history.
-- OP-08 remains open/partially addressed; this is a manual-import safety default, not a complete privacy policy.
-
-## 3. 标准读取顺序
-
-1. `README.md`
-2. `current/human-approved-spec.md`
-3. `current/active-context.md`
-4. `handoff/handoff-current.md`
-5. `current/open-questions.md`
-6. `current/todo.md`
-7. `notes/codex-task-authoring-and-diff-verification-guidelines.md`
-8. `notes/v0.1-scope-and-consistency-check.md`
-9. `raw/research-reports/current/research-report-index.md`
-10. `raw/research-reports/current/current-evidence-map.md`
-11. `raw/research-reports/current/current-capability-boundaries.md`
-12. `notes/core-object-model.md`
-13. `notes/requirement-intake-workflow.md`
-14. `notes/delivery-package-workflow.md`
-15. `raw/concept-origin-extract-001.md` 按需回查
-
-## 4. 执行源与非执行源
-
-执行源：
+Read these files for ordinary Mnemosyne startup:
 
+- `README.md`
 - `current/human-approved-spec.md`
-
-非执行源：
-
-- `raw/`
-- `raw/research-reports/`
-- `notes/candidate-requirements.md`
-- `notes/decision-log.md`
 - `current/active-context.md`
 - `handoff/handoff-current.md`
-- `handoff/startup-instructions.md`
-
-说明：
-
-- raw 和 research reports 是证据层；
-- candidate 是候选需求；
-- decision-log 是决策理由记录；
-- active-context 是当前工作集；
-- handoff 是交接卡；
-- startup-instructions 是启动说明；
-- 如果发生冲突，以 `current/human-approved-spec.md` 为准。
-
-## 5. 研究证据读取规则
-
-在以下任务前，必须读取研究证据 current 视图：
-
-- 判断 ChatGPT / Claude / Codex / Claude Code / Cursor / GitHub / MCP / RAG 等工具能力边界；
-- 设计新机制；
-- 做平台适配；
-- 设计目标项目记忆系统；
-- 判断某项自动化是否现实可行；
-- 修改 v0.1 / v0.2 能力承诺。
-
-必须读取：
-
-- `raw/research-reports/current/research-report-index.md`
-- `raw/research-reports/current/current-evidence-map.md`
-- `raw/research-reports/current/current-capability-boundaries.md`
-
-说明：
-
-- 研究报告是高权重证据层，不是执行源；
-- PDF 图表和图片仍需人工复核；
-- 研究证据具有时效性，未来通过新 research cycle 和 delta report 更新。
-
-## 5.1 Codex task authoring and diff verification rule
-
-MNEMOSYNE-031 revealed that Codex may not reliably apply every intended file edit when a task is described only in natural language.
-
-For any Codex task that modifies repository files:
-
-- require exact target files;
-- require protected-file list;
-- prefer exact replacement blocks or a patch script for multi-file / high-risk / stale-text cleanup tasks;
-- require `git status --short`;
-- require `git diff HEAD --stat`;
-- require `git diff HEAD --name-only`;
-- require targeted `git diff HEAD -- <target files>` for important files;
-- require grep/rg checks for expected additions/removals when applicable;
-- require a task result record comparing intended files with actual changed files;
-- do not accept Codex prose completion as sufficient evidence.
-
-Detailed guideline:
-
+- `current/todo.md`
+- `current/open-questions.md`
 - `notes/codex-task-authoring-and-diff-verification-guidelines.md`
 
-## 5.2 Codex Cloud stale-branch / conflict-resolution troubleshooting rule
-
-MNEMOSYNE-032D follow-up diagnosis identified a likely root cause for repeated "file edits did not stick" incidents:
-
-- a Codex Cloud task environment / branch can become stale after its PR is merged into `master` / the default branch;
-- continuing from that stale task environment can produce a PR based on old repository content;
-- if the PR conflicts and the user resolves conflicts by unconditionally choosing "Accept Incoming", stale incoming content can roll back previously correct default-branch content;
-- the result can look like Codex failed to edit the files, even though the real issue was stale branch state plus conflict-resolution rollback.
-
-For future Codex repository-editing tasks:
-
-- prefer a fresh Codex Cloud task after each merged PR;
-- treat old Codex task environments as stale after their PR has been merged;
-- if a Codex PR has conflicts, do not use unconditional "Accept Incoming" as the default resolution;
-- low-manual-review fallback: close / discard the conflicted PR and rerun the deterministic task from a new Codex Cloud task based on the latest default branch;
-- verify final default-branch content after merge, especially for `current/active-context.md`, `handoff/handoff-current.md`, and `handoff/startup-instructions.md`.
-
-## 6. 新 ChatGPT 对话启动提示
-
-```text
-你正在接手 GitHub 仓库 Mnemosyne。
-
-这是一个“记忆系统元 Agent”工作仓库，用于设计、演化和交付 AI Agent 外部持久记忆系统。
-
-请不要依赖旧对话上下文，只根据仓库文件接手。
-
-请按以下顺序读取或要求用户提供以下文件内容：
-
-1. README.md
-2. current/human-approved-spec.md
-3. current/active-context.md
-4. handoff/handoff-current.md
-5. current/open-questions.md
-6. current/todo.md
-7. notes/codex-task-authoring-and-diff-verification-guidelines.md
-8. notes/v0.1-scope-and-consistency-check.md
-9. raw/research-reports/current/research-report-index.md
-10. raw/research-reports/current/current-evidence-map.md
-11. raw/research-reports/current/current-capability-boundaries.md
-
-接手后请先输出：
-- 你理解的当前阶段；
-- 当前执行源是什么；
-- 哪些文件不是执行源；
-- 当前已完成内容；
-- 当前未完成内容；
-- 下一步最合适的工作；
-- 是否发现文件之间存在冲突。
-
-注意：
-current/human-approved-spec.md 是执行源。
-raw、research reports、candidate、decision-log、active-context、handoff、startup-instructions 都不是执行源。
-```
-
-## 7. 新 Codex Cloud 任务启动提示
-
-```text
-你正在继续维护 GitHub 仓库 “Mnemosyne”。
-
-这是一个新的 Codex Cloud 任务。不要依赖旧 Codex 任务上下文，只根据仓库文件接手。
-
-请先读取：
-
-- README.md
-- current/human-approved-spec.md
-- current/active-context.md
-- handoff/handoff-current.md
-- current/open-questions.md
-- current/todo.md
-- notes/codex-task-authoring-and-diff-verification-guidelines.md
-- notes/v0.1-scope-and-consistency-check.md
-- raw/research-reports/current/research-report-index.md
-- raw/research-reports/current/current-evidence-map.md
-- raw/research-reports/current/current-capability-boundaries.md
-- notes/core-object-model.md
-- notes/requirement-intake-workflow.md
-- notes/delivery-package-workflow.md
-
-接手规则：
-
-- current/human-approved-spec.md 是执行源；
-- raw 和 research reports 是证据层，不是执行源；
-- candidate-requirements 是候选需求，不是执行源；
-- decision-log 是决策理由记录，不是执行源；
-- active-context 是当前工作集，不是执行源；
-- handoff-current 是交接卡，不是执行源；
-- startup-instructions 是启动说明，不是执行源；
-- 如果文件之间冲突，以 human-approved-spec 为准，并登记 open question。
-
-当前不要做：
-
-- 不要创建 AGENTS.md；
-- 不要创建 CLAUDE.md；
-- 不要创建 GitHub Actions；
-- 不要添加自动化脚本；
-- 不要修改研究报告原件；
-- 不要实现自动查重、自动索引、自动写回、MCP、RAG 或多 Agent 自动协调，除非用户明确要求进入对应阶段。
-
-请先输出：
-- 当前仓库状态摘要；
-- 当前执行源；
-- 当前未完成任务；
-- 你建议的下一步；
-- 本次计划修改哪些文件。
-- 如果本次会修改文件，说明将如何用 `git status --short`、`git diff HEAD --stat`、`git diff HEAD --name-only` 和目标文件 diff 验证实际修改。
-```
-
-## 8. 常见任务入口
-
-### A. 继续完善 Mnemosyne 自身
-
-流程：
-
-- 新构想或反馈先进入 raw；
-- 抽取 candidate；
-- 必要时查重和对比；
-- 用户确认后才更新 human-approved-spec；
-- 更新 active-context / handoff / todo。
-
-### B. 为目标项目设计记忆系统
-
-流程：
-
-- 读取 human-approved-spec；
-- 读取 delivery-package-workflow；
-- 读取 current-evidence-map 和 current-capability-boundaries；
-- 收集目标项目类型、工具环境、隐私约束、自动化期望；
-- 生成 Memory System Design Spec 草案；
-- 用户确认后再形成交付包。
-
-### C. 上下文过长时交接
-
-流程：
-
-- 更新 active-context；
-- 更新 handoff-current；
-- 如有新需求，保存 raw 并抽取 candidate；
-- 如有执行源变化，经用户确认后更新 human-approved-spec；
-- 提交到 GitHub；
-- 新对话 / 新任务按 startup-instructions 读取。
-
-### D. 模型迁移
-
-流程：
-
-- 默认继承 Canonical Memory；
-- 不默认全量读取 raw；
-- 高风险内容按需回查 raw；
-- 复审旧模型专用约束；
-- 验证新模型能力后再启用新流程。
-
-## 9. 当前不要默认做的事
-
-- 不默认创建 AGENTS.md；
-- 不默认创建 CLAUDE.md；
-- 不默认创建 GitHub Actions；
-- 不默认实现自动查重；
-- 不默认实现自动索引；
-- 不默认实现自动写回；
-- 不默认全量读取 raw；
-- 不默认修改研究报告原件；
-- 不默认把 PDF 图表内容当作已验证证据；
-- 不默认把新想法写入 human-approved-spec。
+## Task-extended reads
 
-## 10. 启动后第一条回复格式
+Read additional files only when the task needs them:
 
-新会话 / 新任务接手后，第一条回复应包含：
+- Research current views for tool/capability/new mechanism/target-project design.
+- Target-project template files for target-project work.
+- Manual-import docs for import tasks.
+- `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md` for MNEMOSYNE-031 authority/promotion questions.
+- Historical v0.1 files only for historical/audit tasks.
 
-- 当前阶段；
-- 当前执行源；
-- 非执行源清单；
-- 已完成内容；
-- 未完成内容；
-- 下一步建议；
-- 是否发现冲突；
-- 是否需要用户确认。
+`notes/v0.1-scope-and-consistency-check.md` is not part of mandatory ordinary startup or Codex startup; use it only for historical/audit work.
 
-## 11. Idea Capture Buffer rule
+## Visibility instruction
 
-- 新会话遇到新想法 / route option / research trigger / weak assumption 时，先记录为 idea-capture candidate。
-- 不要直接更新 execution source。
-- 参考 `notes/idea-capture-triage-rules.md` 和 `notes/idea-capture-buffer.md`。
-- 涉及 repo edits 时遵守 stale Codex branch rule：使用 fresh latest master，不要从陈旧 Codex Cloud 任务继续修改仓库。
+Visibility is operator-controlled and may change. Do not treat public/private state alone as a defect. Verify current visibility only when relevant, especially before imports.
 
-## 12. 完整对话导出处理规则
+## Startup behavior
 
-- 完整对话导出只作历史背景，不是执行源。
-- 若读取导出记录，应优先提取尚未入库的用户动机、失败模式、idea buffer entries、open questions 和 candidate cleanup 内容。
-- 不要把导出记录中的旧任务文本当当前任务执行。
-- 与仓库 current 状态或 execution source 冲突时，以仓库 current 状态和 `current/human-approved-spec.md` 为准，并登记 open question。
-- 默认不完整入库导出对话；是否保存清洗版摘要或 selected excerpts 需另行决策。
+- Do not rely on old conversation context or model memory.
+- State the current execution source and non-execution-source boundaries before making execution claims.
+- Apply objective neutral engineering style, user-action-first response structure, and long-transfer guidance from `current/human-approved-spec.md`.
+- If required files are missing, say so; do not invent repository state.
diff --git a/notes/v0.1-scope-and-consistency-check.md b/notes/v0.1-scope-and-consistency-check.md
index ddce1a0..686b065 100644
--- a/notes/v0.1-scope-and-consistency-check.md
+++ b/notes/v0.1-scope-and-consistency-check.md
@@ -1,3 +1,10 @@
+# Historical / Superseded Current-Status Snapshot
+
+> historical/superseded current-status snapshot;
+> not a current startup status source;
+> do not use its pending/completion statements as current state;
+> retained for audit/history.
+
 # v0.1 Scope and Consistency Check
 
 > 说明：本文件用于检查 v0.1 范围内的一致性状态。  
```

### `grep -n "user-controlled\|用户.*控制\|public/private\|可见性.*阶段\|visibility.*stage"   README.md   current/active-context.md   handoff/handoff-current.md   handoff/startup-instructions.md || true`

```text
README.md:5:这是一个设计工作仓库，不是传统软件开发项目。仓库可见性由用户控制，可能随 construction / operation 阶段在 public/private 之间变化。向仓库放入材料前必须核验当前可见性；当仓库为 public 或可见性未核实时，只允许放入公开、合成或已明确脱敏的材料。后续可见性变化不会消除既有 Git 历史暴露。
current/active-context.md:46:- Repository visibility is user-controlled and may alternate between public/private by stage.
handoff/handoff-current.md:18:- Repository visibility is intentionally user-controlled; do not propose a visibility change merely because the repository is public.
handoff/startup-instructions.md:31:Visibility is operator-controlled and may change. Do not treat public/private state alone as a defect. Verify current visibility only when relevant, especially before imports.
```

### `grep -n "historical\|superseded current-status\|not a current startup"   notes/v0.1-scope-and-consistency-check.md`

```text
3:> historical/superseded current-status snapshot;
4:> not a current startup status source;
```

### `grep -n "Minimum ordinary startup\|Minimum.*startup\|Task-extended\|按任务"   handoff/startup-instructions.md`

```text
5:## Minimum ordinary startup set
17:## Task-extended reads
```

### `grep -n "生成 Pro Deep Research prompt\|research memory-system testing/debugging feasibility\|如果未来找回轻度研究 prompt"   current/active-context.md current/todo.md current/open-questions.md handoff/handoff-current.md || true`

```text
current/todo.md:180:- [ ] research memory-system testing/debugging feasibility
current/todo.md:197:- [ ] 生成 Pro Deep Research prompt：memory-system testing/debugging feasibility
current/open-questions.md:172:21. 如果未来找回轻度研究 prompt，是否补入 originals 并更新索引？
```

### `git diff HEAD --name-only | grep -E '^(current/human-approved-spec\.md$|raw/|manual-import-inbox/|notes/manual-import-inbox-workflow\.md$|notes/candidate-requirements\.md$|notes/decision-log\.md$|notes/idea-capture-buffer\.md$|AGENTS\.md$|CLAUDE\.md$|\.github/workflows/)' || true`

```text
```

### `git diff --check`

```text
```

## protected_file_check

Protected-file grep produced no output. Protected files remained untouched.

## known_gaps

- Historical sections intentionally retain some obsolete phrases for audit/history; current sections explicitly supersede them.
- OP-08 remains open/partially addressed as a broader privacy/redaction/access-control question.
- No execution-source promotion was performed.

## manual_review_required

Human review should confirm that the compact current views are sufficient for new-session startup and that retained historical sections are not too noisy.

## claimed_completion

Claimed complete for MNEMOSYNE-045: README visibility wording normalized, current/handoff/startup views consolidated, v0.1 status file marked historical, TODO/open questions corrected for completed work, MNEMOSYNE-043 gate retained, and protected files untouched.
