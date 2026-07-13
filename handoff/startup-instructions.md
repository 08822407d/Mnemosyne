# Startup Instructions

This file is not an execution source. The current execution source is `current/human-approved-spec.md`.

## Startup scope

These startup instructions are for Mnemosyne-related conversations and tasks. They separate behavior-guidance refresh from work handoff.

Loading Mnemosyne guidance does not start handoff, does not import the Mnemosyne maintenance live route, and does not replace the current conversation's local task.

Work handoff is a separate explicit artifact-mediated workflow:

- Prepare a handoff package in the old conversation only when the user explicitly requests handoff preparation.
- Receive a handoff package in the new conversation only when the user explicitly provides a handoff package or authorized handoff-package path and asks to continue from it.

Do not try to detect a handoff pair across hidden conversation contexts. A receiving conversation can verify only the current user instruction, the provided handoff package or authorized path, and accessible evidence paths.

## Guidance refresh startup

When the user says "Load Mnemosyne guidance" / "加载 Mnemosyne 指导约束" / "加载 MNEMOSYNE 约束指导" / "加载最新指导", use `commands/load-mnemosyne-guidance.md`.

For behavior-guidance refresh, read or ask the user to provide:

- `README.md`
- `current/human-approved-spec.md`
- `commands/load-mnemosyne-guidance.md`, if available

Then continue the current local task under the refreshed behavior constraints.

Do not require these files as local action-plan sources merely for guidance refresh:

- `current/active-context.md`
- `handoff/handoff-current.md`
- `current/todo.md`
- `current/open-questions.md`

## Handoff prepare startup

When the user explicitly asks the current / old conversation to prepare a handoff package, use `commands/prepare-mnemosyne-handoff.md`.

A handoff package is a transfer artifact, not an execution source. It should identify the execution source, non-execution-source boundaries, current task or phase, completed and unresolved work, forbidden actions, evidence paths, freshness limits, one safe next action, and an explicit `receiver_guidance_load` block.

A Mnemosyne-owned handoff package must explicitly tell the new conversation to perform three separate operations in order: receive the package, execute `Load Mnemosyne guidance` / `加载 Mnemosyne 指导约束`, and then continue the received task. Do not assume that merely listing `current/human-approved-spec.md` makes the explicit guidance-refresh instruction unnecessary.

A target-project business-conversation handoff must tell the receiver to load the target project's confirmed constraints or owner rule and record:

```yaml
receiver_guidance_load:
  project_guidance: required
  mnemosyne_guidance: yes | no | unknown_requires_user_decision
```

Whether it should also load Mnemosyne guidance remains an open question; use `current/handoff-guidance-open-question.md`. A task-local choice is not a global precedent.

## Handoff receive startup

When the user explicitly asks a new conversation to receive a handoff package, use `commands/receive-mnemosyne-handoff.md`.

A receiving conversation must not infer old-conversation state from hidden memory. If no handoff package content or authorized handoff-package path is present, the receiving conversation is not in handoff mode and must not invent the missing package.

For handoff receive, read or ask the user to provide:

- `README.md`
- `current/human-approved-spec.md`
- `commands/receive-mnemosyne-handoff.md`, if available
- the handoff package content or authorized package path
- task-relevant evidence files cited by the package, as needed and accessible

For a Mnemosyne-owned handoff, complete the receive report first, then separately execute `commands/load-mnemosyne-guidance.md` before continuing the received task. The guidance refresh preserves that task and does not replace it with unrelated maintenance live state.

For a target-project business handoff, follow the package's explicit project-guidance and task-local Mnemosyne-guidance values. If the value is `unknown_requires_user_decision`, preserve the decision gate rather than selecting an answer silently.

Do not treat the handoff package, `current/active-context.md`, `handoff/handoff-current.md`, `current/todo.md`, `current/open-questions.md`, task result records, review outputs, or research reports as execution source.

## Task-extended reads

Read additional files only when the task needs them:

- Research current views for tool/capability/new mechanism/target-project design.
- Target-project template files for target-project work.
- Manual-import docs for import tasks.
- For first target-project dry-run preparation or execution, read `handoff/first-target-project-dry-run-onboarding-package.md` first, then the minimal profile/checklist/review instruments listed there.
- `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md` for MNEMOSYNE-031 authority/promotion questions.
- Historical v0.1 files only for historical/audit work.
- For handoff package generation, tier selection, replay review, or model/tool handoff comparison, read `notes/handoff-package-strategy-v0.1.md` and `notes/handoff-replay-scorecard-v0.1.md`.

`notes/v0.1-scope-and-consistency-check.md` is not part of mandatory ordinary startup or Codex startup; use it only for historical/audit work.

## Visibility instruction

Visibility is operator-controlled and may change. Do not treat public/private state alone as a defect. Verify current visibility only when relevant, especially before imports.

## Startup behavior

- Do not rely on old conversation context or model memory.
- State the current execution source and non-execution-source boundaries before making execution claims.
- Apply objective neutral engineering style, user-action-first response structure, and long-transfer guidance from `current/human-approved-spec.md`.
- For guidance refresh, report that the current conversation task is preserved and no handoff was started.
- For handoff receive, report package identity, non-execution-source status, `receiver_guidance_load`, evidence paths checked or missing, and one safe next action.
- If required files for the selected explicit workflow are missing, say so; do not invent repository state.
