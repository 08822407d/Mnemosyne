# MNEMOSYNE-036 Result

- task_id: MNEMOSYNE-036
- task_name: Construction Stage Understanding and Artifact Boundary Backfill

## files_created

- `notes/mnemosyne-construction-stage-understanding.md`
- `notes/codex-task-results/MNEMOSYNE-036-result.md`

## files_modified

- `notes/idea-capture-buffer.md`
- `current/open-questions.md`
- `notes/candidate-requirements.md`
- `current/active-context.md`
- `current/todo.md`
- `handoff/handoff-current.md`

## files_not_modified

- `current/human-approved-spec.md` was not modified.
- `raw/**` was not modified.
- `raw/research-reports/**` was not modified.
- `raw/user-design-restatements/**` was not modified.
- PDF files were not modified.
- `commands/**` was not modified.
- `handoff/startup-instructions.md` was not modified.
- `notes/decision-log.md` was not modified.
- `AGENTS.md` was not created or modified.
- `CLAUDE.md` was not created or modified.
- `.github/workflows/**` was not modified.

## summary

MNEMOSYNE-036 captured construction-stage understanding and artifact-boundary clarifications in non-execution-source locations. The new construction-stage note records prototype-stage framing, the ordinary ChatGPT-to-Codex writeback loop, evidence-guided self-improvement, the boundary between human-readable basis materials and agent-operational artifacts, HADB terminology, and indexing as a research-gated performance optimization candidate. Idea buffer, open questions, candidate cleanup seeds, active context, todo, and handoff were updated accordingly. `current/human-approved-spec.md` remains the only execution source and was not changed.

## verification commands and outputs

Verification evidence was collected after staging the intended changes so `git diff HEAD` includes newly created files.

```
$ git status --short
M  current/active-context.md
M  current/open-questions.md
M  current/todo.md
M  handoff/handoff-current.md
M  notes/candidate-requirements.md
AM notes/codex-task-results/MNEMOSYNE-036-result.md
M  notes/idea-capture-buffer.md
A  notes/mnemosyne-construction-stage-understanding.md

$ git diff HEAD --stat
 current/active-context.md                          |  8 ++
 current/open-questions.md                          |  9 ++
 current/todo.md                                    |  5 ++
 handoff/handoff-current.md                         |  8 ++
 notes/candidate-requirements.md                    | 11 +++
 notes/codex-task-results/MNEMOSYNE-036-result.md   | 53 ++++++++++++
 notes/idea-capture-buffer.md                       | 96 +++++++++++++++++++++
 .../mnemosyne-construction-stage-understanding.md  | 99 ++++++++++++++++++++++
 8 files changed, 289 insertions(+)

$ git diff HEAD --name-only
current/active-context.md
current/open-questions.md
current/todo.md
handoff/handoff-current.md
notes/candidate-requirements.md
notes/codex-task-results/MNEMOSYNE-036-result.md
notes/idea-capture-buffer.md
notes/mnemosyne-construction-stage-understanding.md

$ git diff HEAD -- notes/mnemosyne-construction-stage-understanding.md notes/idea-capture-buffer.md current/open-questions.md notes/candidate-requirements.md current/active-context.md current/todo.md handoff/handoff-current.md notes/codex-task-results/MNEMOSYNE-036-result.md
diff --git a/current/active-context.md b/current/active-context.md
index bd2b0e2..e1e8dbd 100644
--- a/current/active-context.md
+++ b/current/active-context.md
@@ -1,5 +1,13 @@
 # Active Context

+
+## MNEMOSYNE-036 status
+
+- MNEMOSYNE-036 records construction-stage understanding and artifact-boundary clarifications as non-execution-source notes / candidates / open questions.
+- current/human-approved-spec.md was not modified by this task.
+- Core additions include prototype-stage framing, ChatGPT-to-Codex writeback loop, evidence-guided self-improvement, HADB terminology, agent-operational artifact boundary, and indexing as research-gated performance optimization.
+- Current execution source remains `current/human-approved-spec.md`.
+
 ## 当前阶段

 MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 dry-run independent verification 已完成，final verdict 为 PASS。当前等待用户选择下一路线：PDF 图表复核、Idea Capture Buffer / candidate cleanup、template review / small fixes 或 memory-system testing/debugging feasibility research。
diff --git a/current/open-questions.md b/current/open-questions.md
index b050308..871bde1 100644
--- a/current/open-questions.md
+++ b/current/open-questions.md
@@ -186,3 +186,12 @@
   - 说明：当前规则只说明可在重要对话或 Codex 任务后追加，仍需确定 cadence 和触发条件。
 - 任务结果记录保存范围应如何定义？
   - 说明：是否只保存有警告、限制、失败、未完成、人工复核需求的精简记录，而不是保存所有 Codex 完成回复，仍需策略确认。
+
+## MNEMOSYNE-036 construction-stage open questions
+
+- How should HADB relate to raw records, candidate requirements, and `current/human-approved-spec.md`?
+- When should a settled HADB require a clarification addendum during artifact generation?
+- How should agent-operational artifacts be tested or verified for reproducible use by later agents?
+- What minimum evidence is needed before indexing/retrieval acceleration becomes a real Mnemosyne mechanism?
+- What cadence should research-to-improvement review use, and how should it map research findings to open questions and failure modes?
+- Which real target projects should be used to test whether Mnemosyne's prototype memory-system designs actually work?
diff --git a/current/todo.md b/current/todo.md
index 674e460..829994d 100644
--- a/current/todo.md
+++ b/current/todo.md
@@ -145,3 +145,8 @@ Pending / next:
 - [ ] 明确 AI 回复在 raw/context evidence 中保存粒度
 - [ ] 处理模型能力差异 / Codex 模型选择等 open questions
 - [ ] 继续 Pro Deep Research prompt / PDF review / template review / onboarding rehearsal / first target selection 路线选择
+
+
+## MNEMOSYNE-036 construction-stage understanding backfill
+
+- [x] MNEMOSYNE-036：construction-stage understanding and artifact-boundary clarifications captured.
diff --git a/handoff/handoff-current.md b/handoff/handoff-current.md
index 429b63f..ef5760e 100644
--- a/handoff/handoff-current.md
+++ b/handoff/handoff-current.md
@@ -8,6 +8,14 @@ Mnemosyne

 Mnemosyne 是记忆系统元 Agent 工作仓库，用于设计、演化和交付 AI Agent 外部持久记忆系统。

+
+## MNEMOSYNE-036 construction-stage understanding / artifact boundary
+
+- Read `notes/mnemosyne-construction-stage-understanding.md` when discussing Mnemosyne construction-stage assumptions, HADB, artifact boundaries, or indexing.
+- The note is not execution source.
+- Do not treat the new ideas as approved spec.
+- The ChatGPT-to-Codex writeback loop is recognized as normal construction workflow: ordinary ChatGPT can generate Codex tasks; Codex performs reviewed repo writes.
+
 ## 当前阶段

 MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 first dry-run independent verification 已完成，final verdict 为 PASS。当前等待用户选择下一路线：PDF 图表复核、Idea Capture Buffer / candidate cleanup、template review / small fixes 或 memory-system testing/debugging feasibility research。
diff --git a/notes/candidate-requirements.md b/notes/candidate-requirements.md
index a7b4702..6c46ecf 100644
--- a/notes/candidate-requirements.md
+++ b/notes/candidate-requirements.md
@@ -676,3 +676,14 @@ All entries in this section are candidate cleanup items derived from `historical
 - 状态：pending_triage
 - 来源：RAW-0055 / IDEA-2026-0014
 - cleanup 方向：roadmap / active-context / startup 中持续保持非执行源边界。
+
+## MNEMOSYNE-036 candidate cleanup seeds
+
+These are candidate cleanup seeds. They are not approved spec, are not execution source, and require deduplication against existing candidate requirements plus user confirmation before any promotion.
+
+- Prototype-stage construction and feedback-driven maturation.
+- Ordinary ChatGPT discussion to Codex writeback workflow.
+- Evidence-guided self-improvement loop.
+- Human-readable basis materials vs agent-operational artifact boundary.
+- HADB terminology and lifecycle.
+- Indexing as research-gated performance optimization, not core requirement.
diff --git a/notes/codex-task-results/MNEMOSYNE-036-result.md b/notes/codex-task-results/MNEMOSYNE-036-result.md
new file mode 100644
index 0000000..b079edd
--- /dev/null
+++ b/notes/codex-task-results/MNEMOSYNE-036-result.md
@@ -0,0 +1,141 @@
+# MNEMOSYNE-036 Result
+
+- task_id: MNEMOSYNE-036
+- task_name: Construction Stage Understanding and Artifact Boundary Backfill
+
+## files_created
+
+- `notes/mnemosyne-construction-stage-understanding.md`
+- `notes/codex-task-results/MNEMOSYNE-036-result.md`
+
+## files_modified
+
+- `notes/idea-capture-buffer.md`
+- `current/open-questions.md`
+- `notes/candidate-requirements.md`
+- `current/active-context.md`
+- `current/todo.md`
+- `handoff/handoff-current.md`
+
+## files_not_modified
+
+- `current/human-approved-spec.md` was not modified.
+- `raw/**` was not modified.
+- `raw/research-reports/**` was not modified.
+- `raw/user-design-restatements/**` was not modified.
+- PDF files were not modified.
+- `commands/**` was not modified.
+- `handoff/startup-instructions.md` was not modified.
+- `notes/decision-log.md` was not modified.
+- `AGENTS.md` was not created or modified.
+- `CLAUDE.md` was not created or modified.
+- `.github/workflows/**` was not modified.
+
+## summary
+
+MNEMOSYNE-036 captured construction-stage understanding and artifact-boundary clarifications in non-execution-source locations. The new construction-stage note records prototype-stage framing, the ordinary ChatGPT-to-Codex writeback loop, evidence-guided self-improvement, the boundary between human-readable basis materials and agent-operational artifacts, HADB terminology, and indexing as a research-gated performance optimization candidate. Idea buffer, open questions, candidate cleanup seeds, active context, todo, and handoff were updated accordingly. `current/human-approved-spec.md` remains the only execution source and was not changed.
+
+## verification commands and outputs
+
+Verification evidence was collected after staging the intended changes so `git diff HEAD` includes newly created files.
+
+```
+$ git status --short
+M  current/active-context.md
+M  current/open-questions.md
+M  current/todo.md
+M  handoff/handoff-current.md
+M  notes/candidate-requirements.md
+AM notes/codex-task-results/MNEMOSYNE-036-result.md
+M  notes/idea-capture-buffer.md
+A  notes/mnemosyne-construction-stage-understanding.md
+
+$ git diff HEAD --stat
+ current/active-context.md                          |  8 ++
+ current/open-questions.md                          |  9 ++
+ current/todo.md                                    |  5 ++
+ handoff/handoff-current.md                         |  8 ++
+ notes/candidate-requirements.md                    | 11 +++
+ notes/codex-task-results/MNEMOSYNE-036-result.md   | 53 ++++++++++++
+ notes/idea-capture-buffer.md                       | 96 +++++++++++++++++++++
+ .../mnemosyne-construction-stage-understanding.md  | 99 ++++++++++++++++++++++
+ 8 files changed, 289 insertions(+)
+
+$ git diff HEAD --name-only
+current/active-context.md
+current/open-questions.md
+current/todo.md
+handoff/handoff-current.md
+notes/candidate-requirements.md
+notes/codex-task-results/MNEMOSYNE-036-result.md
+notes/idea-capture-buffer.md
+notes/mnemosyne-construction-stage-understanding.md
+
+$ git diff HEAD -- notes/mnemosyne-construction-stage-understanding.md notes/idea-capture-buffer.md current/open-questions.md notes/candidate-requirements.md current/active-context.md current/todo.md handoff/handoff-current.md notes/codex-task-results/MNEMOSYNE-036-result.md
+diff --git a/current/active-context.md b/current/active-context.md
+index bd2b0e2..e1e8dbd 100644
+--- a/current/active-context.md
++++ b/current/active-context.md
+@@ -1,5 +1,13 @@
+ # Active Context
+
++
++## MNEMOSYNE-036 status
++
++- MNEMOSYNE-036 records construction-stage understanding and artifact-boundary clarifications as non-execution-source notes / candidates / open questions.
++- current/human-approved-spec.md was not modified by this task.
++- Core additions include prototype-stage framing, ChatGPT-to-Codex writeback loop, evidence-guided self-improvement, HADB terminology, agent-operational artifact boundary, and indexing as research-gated performance optimization.
++- Current execution source remains `current/human-approved-spec.md`.
++
+ ## 当前阶段
+
+ MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 dry-run independent verification 已完成，final verdict 为 PASS。当前等待用户选择下一路线：PDF 图表复核、Idea Capture Buffer / candidate cleanup、template review / small fixes 或 memory-system testing/debugging feasibility research。
+diff --git a/current/open-questions.md b/current/open-questions.md
+index b050308..871bde1 100644
+--- a/current/open-questions.md
++++ b/current/open-questions.md
+@@ -186,3 +186,12 @@
+   - 说明：当前规则只说明可在重要对话或 Codex 任务后追加，仍需确定 cadence 和触发条件。
+ - 任务结果记录保存范围应如何定义？
+   - 说明：是否只保存有警告、限制、失败、未完成、人工复核需求的精简记录，而不是保存所有 Codex 完成回复，仍需策略确认。
++
++## MNEMOSYNE-036 construction-stage open questions
++
++- How should HADB relate to raw records, candidate requirements, and `current/human-approved-spec.md`?
++- When should a settled HADB require a clarification addendum during artifact generation?
++- How should agent-operational artifacts be tested or verified for reproducible use by later agents?
++- What minimum evidence is needed before indexing/retrieval acceleration becomes a real Mnemosyne mechanism?
++- What cadence should research-to-improvement review use, and how should it map research findings to open questions and failure modes?
++- Which real target projects should be used to test whether Mnemosyne's prototype memory-system designs actually work?
+diff --git a/current/todo.md b/current/todo.md
+index 674e460..829994d 100644
+--- a/current/todo.md
++++ b/current/todo.md
+@@ -145,3 +145,8 @@ Pending / next:
+ - [ ] 明确 AI 回复在 raw/context evidence 中保存粒度
+ - [ ] 处理模型能力差异 / Codex 模型选择等 open questions
+ - [ ] 继续 Pro Deep Research prompt / PDF review / template review / onboarding rehearsal / first target selection 路线选择
++
++
++## MNEMOSYNE-036 construction-stage understanding backfill
++
++- [x] MNEMOSYNE-036：construction-stage understanding and artifact-boundary clarifications captured.
+diff --git a/handoff/handoff-current.md b/handoff/handoff-current.md
+index 429b63f..ef5760e 100644
+--- a/handoff/handoff-current.md
++++ b/handoff/handoff-current.md
+@@ -8,6 +8,14 @@ Mnemosyne
+
+ Mnemosyne 是记忆系统元 Agent 工作仓库，用于设计、演化和交付 AI Agent 外部持久记忆系统。
+
++
++## MNEMOSYNE-036 construction-stage understanding / artifact boundary
++
++- Read `notes/mnemosyne-construction-stage-understanding.md` when discussing Mnemosyne construction-stage assumptions, HADB, artifact boundaries, or indexing.
++- The note is not execution source.
++- Do not treat the new ideas as approved spec.
++- The ChatGPT-to-Codex writeback loop is recognized as normal construction workflow: ordinary ChatGPT can generate Codex tasks; Codex performs reviewed repo writes.
++
+ ## 当前阶段
+
+ MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 first dry-run independent verification 已完成，final verdict 为 PASS。当前等待用户选择下一路线：PDF 图表复核、Ide
\ No newline at end of file
diff --git a/notes/idea-capture-buffer.md b/notes/idea-capture-buffer.md
index 99dbe5c..a20a7ee 100644
--- a/notes/idea-capture-buffer.md
+++ b/notes/idea-capture-buffer.md
@@ -440,3 +440,99 @@ All entries in this section are `historical_conversation_derived_insight`. They
 - target_followup_file: `current/open-questions.md`; `notes/candidate-requirements.md`
 - status: captured_pending_triage
 - promotion_condition: 用户确认任务结果记录策略。
+
+### IDEA-2026-0026
+
+- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
+- source_type: user_supplemental_explanation
+- captured_at: 2026-06-17
+- short_title: Prototype-stage Mnemosyne construction understanding
+- raw_note: Mnemosyne is currently a prototype-stage exploratory system aiming to establish a usable external persistent memory framework; maturity should come through real target-project use, observed failures, and feedback rather than premature perfect architecture.
+- classification: `candidate_requirement` / `design_rationale`
+- confidence: high
+- evidence_needed: target-project dry-runs and observed memory-system failure records.
+- conflicts_or_risks: Could be misread as permission for careless execution; must remain bounded by `current/human-approved-spec.md`.
+- proposed_next_action: Deduplicate against existing construction rationale and decide whether any wording belongs in future approved rationale.
+- target_followup_file: `notes/candidate-requirements.md`; `current/open-questions.md`
+- status: captured_pending_triage
+- promotion_condition: User confirms the formulation after deduplication and conflict review.
+
+### IDEA-2026-0027
+
+- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
+- source_type: user_supplemental_explanation
+- captured_at: 2026-06-17
+- short_title: Ordinary ChatGPT to Codex repository writeback loop
+- raw_note: Ordinary ChatGPT discussions are read-only for repositories but may generate strict Codex tasks; Codex performs reviewed repository writes through PRs, followed by user review/merge and possible read-only verification.
+- classification: `tool_or_process_lesson` / `candidate_requirement`
+- confidence: high
+- evidence_needed: Review against current Codex task authoring guidance and repository workflow notes.
+- conflicts_or_risks: "Do not write the repository in this conversation" could be overgeneralized to block Codex task generation.
+- proposed_next_action: Consider adding a workflow clarification to future process guidance if approved.
+- target_followup_file: `notes/candidate-requirements.md`; `handoff/handoff-current.md`
+- status: captured_pending_triage
+- promotion_condition: User confirms this should become stable workflow guidance.
+
+### IDEA-2026-0028
+
+- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
+- source_type: user_supplemental_explanation
+- captured_at: 2026-06-17
+- short_title: Evidence-guided self-improvement
+- raw_note: Mnemosyne should improve through self-use and project feedback plus periodic deep research and current best practices; agents should map research findings to open questions, failure modes, target-project feedback, template gaps, capability boundaries, and outdated assumptions.
+- classification: `candidate_requirement` / `research_gated_item`
+- confidence: high
+- evidence_needed: Research-to-improvement cadence and mapping template validation.
+- conflicts_or_risks: Research evidence must not be promoted directly into execution source or override human-approved spec.
+- proposed_next_action: Triage into research evidence usage and self-improvement workflow cleanup.
+- target_followup_file: `notes/candidate-requirements.md`; `current/open-questions.md`
+- status: captured_pending_triage
+- promotion_condition: User approves the research-to-improvement loop and its safeguards.
+
+### IDEA-2026-0029
+
+- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
+- source_type: user_supplemental_explanation
+- captured_at: 2026-06-17
+- short_title: Human-readable basis materials vs agent-operational artifacts
+- raw_note: Mnemosyne should distinguish human-readable basis materials that preserve intent and reviewability from agent-operational artifacts designed for later agents to load, follow, transform, or verify reproducibly.
+- classification: `candidate_requirement` / `design_rationale`
+- confidence: high
+- evidence_needed: Artifact inventory review and verification criteria for agent-operational files.
+- conflicts_or_risks: Operational artifacts may be mistaken for deterministic machine code or silently reinterpreted by later agents.
+- proposed_next_action: Add to candidate cleanup and open questions about artifact verification.
+- target_followup_file: `notes/candidate-requirements.md`; `current/open-questions.md`
+- status: captured_pending_triage
+- promotion_condition: User confirms the boundary and lifecycle implications.
+
+### IDEA-2026-0030
+
+- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
+- source_type: user_supplemental_explanation
+- captured_at: 2026-06-17
+- short_title: HADB terminology
+- raw_note: Human-Approved Design Basis (HADB), Chinese 人类确认设计依据稿, names a settled human-readable design-basis text formed after discussion, contradiction resolution, feasibility analysis, research-evidence checking, and user confirmation; it is not raw record and not automatically execution source.
+- classification: `candidate_requirement`
+- confidence: high
+- evidence_needed: Lifecycle review against raw records, candidate requirements, and execution-source promotion rules.
+- conflicts_or_risks: HADB could be confused with approved spec unless its non-execution-source boundary is explicit.
+- proposed_next_action: Triage HADB terminology and lifecycle into candidate cleanup.
+- target_followup_file: `notes/candidate-requirements.md`; `current/open-questions.md`
+- status: captured_pending_triage
+- promotion_condition: User confirms terminology, Chinese label, and lifecycle rules.
+
+### IDEA-2026-0031
+
+- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
+- source_type: user_supplemental_explanation
+- captured_at: 2026-06-17
+- short_title: Indexing as research-gated performance optimization
+- raw_note: The user's index idea comes from PC hardware / operating-system / file-system analogies and has not been verified for AI agent external memory; it should be treated as a research-gated retrieval acceleration candidate, not a core Mnemosyne requirement.
+- classification: `research_gated_item` / `performance_optimization_candidate` / `weak_or_outdated_assumption`
+- confidence: high
+- evidence_needed: Evidence that indexing improves agent retrieval without stale or misleading authority risks.
+- conflicts_or_risks: Stale indexes, misleading indexes, and agents treating indexes as authority rather than retrieval aids.
+- proposed_next_action: Keep as research-gated candidate until memory scale and retrieval failure evidence justify evaluation.
+- target_followup_file: `notes/candidate-requirements.md`; `current/open-questions.md`
+- status: captured_pending_triage
+- promotion_condition: Research evidence and user confirmation support a specific indexing mechanism.
diff --git a/notes/mnemosyne-construction-stage-understanding.md b/notes/mnemosyne-construction-stage-understanding.md
new file mode 100644
index 0000000..9d3e5ce
--- /dev/null
+++ b/notes/mnemosyne-construction-stage-understanding.md
@@ -0,0 +1,99 @@
+# Mnemosyne Construction-Stage Understanding
+
+This file is not an execution source. It is a non-execution-source construction-stage understanding note for preserving user supplemental explanations, candidate rationale, open-question material, and idea-buffer material.
+
+`current/human-approved-spec.md` remains the only execution source. If this note conflicts with `current/human-approved-spec.md`, the spec wins and the conflict should be recorded as an open question rather than silently resolved here.
+
+## 1. Mnemosyne as prototype-stage exploratory engineering
+
+Mnemosyne is currently closer to a prototype-stage exploratory system than a mature conventional software project. The current goal is not perfect architecture or complete process formalization.
+
+The initial goal is to establish a usable external persistent memory framework that is better than relying only on model context or platform-internal memory. Real maturity should come from using Mnemosyne to design persistent memory systems for real target projects, observing problems, and feeding those problems back into Mnemosyne.
+
+Defects are acceptable at this stage because both the human user and AI agents have some intelligence and can work around imperfect memory-system behavior.
+
+Core problems remain:
+
+- model context is limited and lossy;
+- platform/internal memory is not a stable truth source;
+- new conversations/tasks need more reliable handoff;
+- long-term projects need AI help to compensate for limited human memory.
+
+## 2. Ordinary ChatGPT to Codex repository writeback loop
+
+Ordinary ChatGPT conversations are generally read-only with respect to GitHub repositories. Ordinary ChatGPT conversations may and often should generate strict Codex tasks when a discussion result needs to be landed in the repository.
+
+Codex tasks are the reviewed writeback mechanism: Codex edits repository files, opens PRs, the user reviews and merges, and then a ChatGPT/Codex read-only verification can confirm the result on master.
+
+Therefore "do not write the repository in this conversation" must not be misread as "do not generate Codex tasks." The correct distinction is:
+
+- discussion / planning stage;
+- Codex task prompt generation stage;
+- Codex execution / PR stage;
+- user review and merge stage;
+- post-merge verification stage.
+
+## 3. Evidence-guided self-improvement
+
+Mnemosyne does not improve only through self-use and project feedback. It should also use periodic deep research and current best practices in adjacent fields.
+
+Mnemosyne-affiliated AI conversations/tasks should actively compare research findings with:
+
+- current open questions;
+- failure modes;
+- target-project feedback;
+- template gaps;
+- capability boundaries;
+- outdated assumptions.
+
+The user is not expected to read all research reports or manually identify every applicable best practice.
+
+Research evidence is evidence, not execution source. It can generate candidate improvements, open questions, or research-gated items, but cannot directly override `current/human-approved-spec.md`.
+
+## 4. Human-readable basis materials vs agent-operational artifacts
+
+Two broad material classes are useful for discussing Mnemosyne artifacts.
+
+Human-readable basis materials:
+
+- raw user text;
+- original requirements and feedback;
+- Human-Approved Design Basis / HADB;
+- research prompts and research reports.
+
+Agent-operational artifacts:
+
+- startup instructions;
+- handoff;
+- active context;
+- commands;
+- templates;
+- task prompts;
+- delivery manifests;
+- verification checklists;
+- Codex task result records;
+- other model/agent-facing operational files.
+
+Human-readable basis materials preserve human intent, user reviewability, model-migration evidence, and design grounding.
+
+Agent-operational artifacts are generated for later agents to load, follow, transform, or verify. Agent-operational artifacts are similar to software source code, intermediate representations, or compiled artifacts in the sense that they should be structured, role-specific, and used consistently by agents.
+
+They are still natural-language/Markdown artifacts, so they are not deterministic machine code, but they should be designed to maximize reproducibility and reduce interpretation drift. They must not be invented or silently reinterpreted by later agents.
+
+## 5. Human-Approved Design Basis / HADB
+
+Human-Approved Design Basis (HADB), Chinese: 人类确认设计依据稿.
+
+HADB is a human-readable settled design-basis text formed after discussion, contradiction resolution, feasibility analysis, research-evidence checking, and user confirmation.
+
+HADB is not the raw original record. HADB is not automatically the execution source. HADB is the direct input for generating agent-operational artifacts and later design documents.
+
+After user confirmation, a HADB version should not be silently modified within the same design round. If later generation of operational artifacts reveals missing details, the agent should request clarification and record a clarification addendum or next revision rather than inventing missing details.
+
+## 6. Indexing / retrieval acceleration as research-gated performance optimization
+
+The user's "index" idea was borrowed from PC hardware / operating-system / file-system analogies. It has not been verified as suitable for AI agent external memory.
+
+It should not be treated as a core Mnemosyne requirement. It should be classified as a research-gated performance optimization candidate.
+
+It may later be studied as a retrieval acceleration mechanism when persistent memory grows large. Risks include stale indexes, misleading indexes, and agents treating indexes as authority rather than retrieval aids.

$ grep -n "Human-Approved Design Basis" notes/mnemosyne-construction-stage-understanding.md
61:- Human-Approved Design Basis / HADB;
83:## 5. Human-Approved Design Basis / HADB
85:Human-Approved Design Basis (HADB), Chinese: 人类确认设计依据稿.

$ grep -n "人类确认设计依据稿" notes/mnemosyne-construction-stage-understanding.md
85:Human-Approved Design Basis (HADB), Chinese: 人类确认设计依据稿.

$ grep -n "Codex" notes/mnemosyne-construction-stage-understanding.md
22:## 2. Ordinary ChatGPT to Codex repository writeback loop
24:Ordinary ChatGPT conversations are generally read-only with respect to GitHub repositories. Ordinary ChatGPT conversations may and often should generate strict Codex tasks when a discussion result needs to be landed in the repository.
26:Codex tasks are the reviewed writeback mechanism: Codex edits repository files, opens PRs, the user reviews and merges, and then a ChatGPT/Codex read-only verification can confirm the result on master.
28:Therefore "do not write the repository in this conversation" must not be misread as "do not generate Codex tasks." The correct distinction is:
31:- Codex task prompt generation stage;
32:- Codex execution / PR stage;
74:- Codex task result records;

$ grep -n "research-gated performance optimization" notes/mnemosyne-construction-stage-understanding.md
93:## 6. Indexing / retrieval acceleration as research-gated performance optimization
97:It should not be treated as a core Mnemosyne requirement. It should be classified as a research-gated performance optimization candidate.

$ grep -n "MNEMOSYNE-036" current/active-context.md current/todo.md handoff/handoff-current.md notes/codex-task-results/MNEMOSYNE-036-result.md
current/active-context.md:4:## MNEMOSYNE-036 status
current/active-context.md:6:- MNEMOSYNE-036 records construction-stage understanding and artifact-boundary clarifications as non-execution-source notes / candidates / open questions.
current/todo.md:150:## MNEMOSYNE-036 construction-stage understanding backfill
current/todo.md:152:- [x] MNEMOSYNE-036：construction-stage understanding and artifact-boundary clarifications captured.
handoff/handoff-current.md:12:## MNEMOSYNE-036 construction-stage understanding / artifact boundary

$ grep -n "current/human-approved-spec.md was not modified" current/active-context.md notes/codex-task-results/MNEMOSYNE-036-result.md
current/active-context.md:7:- current/human-approved-spec.md was not modified by this task.

$ git diff HEAD --name-only | grep -E '^(current/human-approved-spec\.md$|raw/|AGENTS\.md$|CLAUDE\.md$|\.github/workflows/|commands/)' || true
```

## protected file check

The protected file check output listed no protected files.

## known gaps

- This task records construction-stage understanding, candidate rationale, open-question material, and idea-buffer material only.
- It does not promote any new content into `current/human-approved-spec.md`.
- It does not resolve the newly added open questions.

## whether task claims completion

Yes. This task claims completion because the required non-execution-source note exists, required target files were updated, `current/human-approved-spec.md` was not modified, no protected files were modified, and verification evidence is recorded above.

## post-record presence recheck

```
$ grep -n "MNEMOSYNE-036" current/active-context.md current/todo.md handoff/handoff-current.md notes/codex-task-results/MNEMOSYNE-036-result.md
current/active-context.md:4:## MNEMOSYNE-036 status
current/active-context.md:6:- MNEMOSYNE-036 records construction-stage understanding and artifact-boundary clarifications as non-execution-source notes / candidates / open questions.
current/todo.md:150:## MNEMOSYNE-036 construction-stage understanding backfill
current/todo.md:152:- [x] MNEMOSYNE-036：construction-stage understanding and artifact-boundary clarifications captured.
handoff/handoff-current.md:12:## MNEMOSYNE-036 construction-stage understanding / artifact boundary
notes/codex-task-results/MNEMOSYNE-036-result.md:1:# MNEMOSYNE-036 Result
notes/codex-task-results/MNEMOSYNE-036-result.md:3:- task_id: MNEMOSYNE-036
notes/codex-task-results/MNEMOSYNE-036-result.md:9:- `notes/codex-task-results/MNEMOSYNE-036-result.md`
notes/codex-task-results/MNEMOSYNE-036-result.md:36:MNEMOSYNE-036 captured construction-stage understanding and artifact-boundary clarifications in non-execution-source locations. The new construction-stage note records prototype-stage framing, the ordinary ChatGPT-to-Codex writeback loop, evidence-guided self-improvement, the boundary between human-readable basis materials and agent-operational artifacts, HADB terminology, and indexing as a research-gated performance optimization candidate. Idea buffer, open questions, candidate cleanup seeds, active context, todo, and handoff were updated accordingly. `current/human-approved-spec.md` remains the only execution source and was not changed.
notes/codex-task-results/MNEMOSYNE-036-result.md:49:AM notes/codex-task-results/MNEMOSYNE-036-result.md
notes/codex-task-results/MNEMOSYNE-036-result.md:59: notes/codex-task-results/MNEMOSYNE-036-result.md   | 53 ++++++++++++
notes/codex-task-results/MNEMOSYNE-036-result.md:70:notes/codex-task-results/MNEMOSYNE-036-result.md
notes/codex-task-results/MNEMOSYNE-036-result.md:74:$ git diff HEAD -- notes/mnemosyne-construction-stage-understanding.md notes/idea-capture-buffer.md current/open-questions.md notes/candidate-requirements.md current/active-context.md current/todo.md handoff/handoff-current.md notes/codex-task-results/MNEMOSYNE-036-result.md
notes/codex-task-results/MNEMOSYNE-036-result.md:83:+## MNEMOSYNE-036 status
notes/codex-task-results/MNEMOSYNE-036-result.md:85:+- MNEMOSYNE-036 records construction-stage understanding and artifact-boundary clarifications as non-execution-source notes / candidates / open questions.
notes/codex-task-results/MNEMOSYNE-036-result.md:102:+## MNEMOSYNE-036 construction-stage open questions
notes/codex-task-results/MNEMOSYNE-036-result.md:120:+## MNEMOSYNE-036 construction-stage understanding backfill
notes/codex-task-results/MNEMOSYNE-036-result.md:122:+- [x] MNEMOSYNE-036：construction-stage understanding and artifact-boundary clarifications captured.
notes/codex-task-results/MNEMOSYNE-036-result.md:132:+## MNEMOSYNE-036 construction-stage understanding / artifact boundary
notes/codex-task-results/MNEMOSYNE-036-result.md:151:+## MNEMOSYNE-036 candidate cleanup seeds
notes/codex-task-results/MNEMOSYNE-036-result.md:161:diff --git a/notes/codex-task-results/MNEMOSYNE-036-result.md b/notes/codex-task-results/MNEMOSYNE-036-result.md
notes/codex-task-results/MNEMOSYNE-036-result.md:165:+++ b/notes/codex-task-results/MNEMOSYNE-036-result.md
notes/codex-task-results/MNEMOSYNE-036-result.md:167:+# MNEMOSYNE-036 Result
notes/codex-task-results/MNEMOSYNE-036-result.md:169:+- task_id: MNEMOSYNE-036
notes/codex-task-results/MNEMOSYNE-036-result.md:175:+- `notes/codex-task-results/MNEMOSYNE-036-result.md`
notes/codex-task-results/MNEMOSYNE-036-result.md:202:+MNEMOSYNE-036 captured construction-stage understanding and artifact-boundary clarifications in non-execution-source locations. The new construction-stage note records prototype-stage framing, the ordinary ChatGPT-to-Codex writeback loop, evidence-guided self-improvement, the boundary between human-readable basis materials and agent-operational artifacts, HADB terminology, and indexing as a research-gated performance optimization candidate. Idea buffer, open questions, candidate cleanup seeds, active context, todo, and handoff were updated accordingly. `current/human-approved-spec.md` remains the only execution source and was not changed.
notes/codex-task-results/MNEMOSYNE-036-result.md:215:+AM notes/codex-task-results/MNEMOSYNE-036-result.md
notes/codex-task-results/MNEMOSYNE-036-result.md:225:+ notes/codex-task-results/MNEMOSYNE-036-result.md   | 53 ++++++++++++
notes/codex-task-results/MNEMOSYNE-036-result.md:236:+notes/codex-task-results/MNEMOSYNE-036-result.md
notes/codex-task-results/MNEMOSYNE-036-result.md:240:+$ git diff HEAD -- notes/mnemosyne-construction-stage-understanding.md notes/idea-capture-buffer.md current/open-questions.md notes/candidate-requirements.md current/active-context.md current/todo.md handoff/handoff-current.md notes/codex-task-results/MNEMOSYNE-036-result.md
notes/codex-task-results/MNEMOSYNE-036-result.md:249:++## MNEMOSYNE-036 status
notes/codex-task-results/MNEMOSYNE-036-result.md:251:++- MNEMOSYNE-036 records construction-stage understanding and artifact-boundary clarifications as non-execution-source notes / candidates / open questions.
notes/codex-task-results/MNEMOSYNE-036-result.md:268:++## MNEMOSYNE-036 construction-stage open questions
notes/codex-task-results/MNEMOSYNE-036-result.md:286:++## MNEMOSYNE-036 construction-stage understanding backfill
notes/codex-task-results/MNEMOSYNE-036-result.md:288:++- [x] MNEMOSYNE-036：construction-stage understanding and artifact-boundary clarifications captured.
notes/codex-task-results/MNEMOSYNE-036-result.md:298:++## MNEMOSYNE-036 construction-stage understanding / artifact boundary
notes/codex-task-results/MNEMOSYNE-036-result.md:320:+- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
notes/codex-task-results/MNEMOSYNE-036-result.md:336:+- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
notes/codex-task-results/MNEMOSYNE-036-result.md:352:+- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
notes/codex-task-results/MNEMOSYNE-036-result.md:368:+- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
notes/codex-task-results/MNEMOSYNE-036-result.md:384:+- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
notes/codex-task-results/MNEMOSYNE-036-result.md:400:+- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
notes/codex-task-results/MNEMOSYNE-036-result.md:540:$ grep -n "MNEMOSYNE-036" current/active-context.md current/todo.md handoff/handoff-current.md notes/codex-task-results/MNEMOSYNE-036-result.md
notes/codex-task-results/MNEMOSYNE-036-result.md:541:current/active-context.md:4:## MNEMOSYNE-036 status
notes/codex-task-results/MNEMOSYNE-036-result.md:542:current/active-context.md:6:- MNEMOSYNE-036 records construction-stage understanding and artifact-boundary clarifications as non-execution-source notes / candidates / open questions.
notes/codex-task-results/MNEMOSYNE-036-result.md:543:current/todo.md:150:## MNEMOSYNE-036 construction-stage understanding backfill
notes/codex-task-results/MNEMOSYNE-036-result.md:544:current/todo.md:152:- [x] MNEMOSYNE-036：construction-stage understanding and artifact-boundary clarifications captured.
notes/codex-task-results/MNEMOSYNE-036-result.md:545:handoff/handoff-current.md:12:## MNEMOSYNE-036 construction-stage understanding / artifact boundary
notes/codex-task-results/MNEMOSYNE-036-result.md:547:$ grep -n "current/human-approved-spec.md was not modified" current/active-context.md notes/codex-task-results/MNEMOSYNE-036-result.md

$ grep -n "current/human-approved-spec.md was not modified" current/active-context.md notes/codex-task-results/MNEMOSYNE-036-result.md
current/active-context.md:7:- current/human-approved-spec.md was not modified by this task.
notes/codex-task-results/MNEMOSYNE-036-result.md:86:+- current/human-approved-spec.md was not modified by this task.
notes/codex-task-results/MNEMOSYNE-036-result.md:252:++- current/human-approved-spec.md was not modified by this task.
notes/codex-task-results/MNEMOSYNE-036-result.md:547:$ grep -n "current/human-approved-spec.md was not modified" current/active-context.md notes/codex-task-results/MNEMOSYNE-036-result.md
notes/codex-task-results/MNEMOSYNE-036-result.md:548:current/active-context.md:7:- current/human-approved-spec.md was not modified by this task.
```
