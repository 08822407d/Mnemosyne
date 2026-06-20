# First Mnemosyne Application Test — Handoff Package

## 1. Purpose

This handoff package is the transfer artifact for starting a new ChatGPT conversation that will run the first Mnemosyne application test: using Mnemosyne to design a persistent external memory system for a target project.

This package is not execution source. The current execution source remains `current/human-approved-spec.md`. If any instruction in this package conflicts with `current/human-approved-spec.md`, preserve `current/human-approved-spec.md` and record the conflict for review.

## 2. Current known repository state

Mnemosyne is a memory-system meta-agent work repository. It is intended to design, evolve, and deliver external persistent memory systems for other projects, long-running research, learning systems, development agents, and multi-agent teams.

The repository currently treats `current/human-approved-spec.md` as the only execution source. Active context, handoff files, startup instructions, candidate requirements, research reports, report summaries, template packs, and this handoff package are not execution source.

The old/current conversation remains responsible for the two Pro work tracks described in the current repository context: the Priority 1 Deep Research track and the ordinary ChatGPT-Pro comprehensive Mnemosyne health review track.

MNEMOSYNE-039 / Pro quota refresh work is a separate or parallel work track. If its Deep Research and ordinary ChatGPT-Pro health review have not yet been completed, the first application test may still proceed as an application-test draft, but it must not claim that the target-project dry-run has already been validated by the comprehensive health review.

## 3. Required repository files to read

Before running the first application test, the new conversation should read at minimum:

1. `current/human-approved-spec.md`
2. `current/active-context.md`
3. `handoff/handoff-current.md`
4. `handoff/startup-instructions.md`
5. `current/todo.md`
6. `current/open-questions.md`
7. `notes/codex-task-authoring-and-diff-verification-guidelines.md`
8. `notes/mnemosyne-construction-stage-understanding.md`
9. `notes/target-project-memory-system-template-pack.md`
10. `notes/delivery-manifest-template-pack.md`
11. `notes/template-pack-review-and-first-scenario-selection.md`
12. `raw/research-reports/current/research-report-index.md`
13. `raw/research-reports/current/current-research-prompts.md`
14. `raw/research-reports/current/current-report-summaries.md`
15. `raw/research-reports/current/current-evidence-map.md`
16. `raw/research-reports/current/current-capability-boundaries.md`

If MNEMOSYNE-039 has already been merged by the time the new conversation starts, also read its task result record and any updated files identified by that result record before making claims about the repository's current health-review or research-refresh status.

## 4. Execution-source boundary for the new conversation

Use `current/human-approved-spec.md` as the execution source. Do not treat any of the following as execution source:

- `current/active-context.md`
- `handoff/handoff-current.md`
- `handoff/startup-instructions.md`
- `notes/candidate-requirements.md`
- `current/open-questions.md`
- `raw/`
- `raw/research-reports/`
- research prompts
- report summaries
- template packs
- this handoff package

If these materials conflict with `current/human-approved-spec.md`, preserve the execution source and record the conflict as an issue or open question.

## 5. Intended application-test workflow

The new conversation should run a manual, user-steered first application test. It should not introduce repository automation, MCP/RAG configuration, GitHub Actions, or execution scripts.

Recommended flow:

1. Confirm the target project scenario with the user.
2. Fill or adapt the Target Project Intake from the template pack.
3. Draft a target-project Memory System Design Spec.
4. Draft the delivery manifest and handoff package for the target project.
5. Identify unsupported assumptions and drift-review TODOs.
6. Clearly separate draft artifacts from any validated repository changes.

## 6. What the new conversation should not claim

The new conversation should not claim that:

- research reports are execution source;
- template packs are already final user-approved execution rules;
- the first target-project dry-run has passed a comprehensive health review unless that review has actually happened;
- PDF figures, tables, images, or layouts have been fully manually reviewed unless the repository records that review;
- high-risk multi-agent designs are validated merely because a first low-risk application-test draft was produced.

## 7. Expected outputs from the first application test

The first application test should produce draft target-project artifacts suitable for user review, such as:

- completed or partially completed Target Project Intake;
- Memory System Design Spec draft;
- target-project delivery manifest draft;
- target-project handoff package draft;
- unsupported assumptions list;
- drift-review TODO list;
- concise notes about what worked, what failed, and what should be improved in Mnemosyne templates.

## 8. Review and writeback boundary

The first application test may identify Mnemosyne improvements, but it should not directly update the execution source. Proposed improvements should be captured as candidate requirements, task prompts, or review notes for later user-confirmed writeback.

Any repository modification should be handled through a separate reviewed Codex task and should preserve `current/human-approved-spec.md` unless the user explicitly approves an execution-source update.

## 9. User-facing startup message suggestion

A suitable opening message for the new conversation is:

> We are starting the first Mnemosyne application test. Please load the required repository files, treat `current/human-approved-spec.md` as the only execution source, and help me choose or confirm a target project scenario before drafting any target-project memory-system artifacts.

## 10. Suggested target project scenario choice

When the user asks for a default first scenario, recommend `software_development_project` first.

Acceptable first scenario options remain:

1. `software_development_project`
2. `source_code_learning`
3. `learning_system`

software_development_project is the strongest default because the existing scenario matrix rates it highly for validating the chain `intake → design spec → delivery manifest → handoff → review` under a low-to-medium-risk, manually executable workflow.

Do not choose high-risk multi-agent team scenarios as the first default unless the user explicitly selects them. They can be considered later after the lower-risk first application-test workflow has been exercised and reviewed.

## 11. Completion signal for the new conversation

The new conversation should finish by reporting:

- selected target project scenario;
- files and templates read;
- draft artifacts produced;
- unsupported assumptions;
- manual review required;
- gaps or blockers;
- recommended follow-up Codex tasks, if any.
