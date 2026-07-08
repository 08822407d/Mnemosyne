# Startup Instructions

This file is not an execution source. The current execution source is `current/human-approved-spec.md`.

## Startup scope

These startup instructions are for Mnemosyne repository startup. They must not be read as a rule that every conversation loading Mnemosyne guidance should adopt the current Mnemosyne maintenance route as its local task.

Use the load-mode rules from `commands/load-mnemosyne-guidance.md` when the user says "Load Mnemosyne guidance" / "加载 Mnemosyne 指导约束".

## Minimum maintenance startup set

Read these files for a Mnemosyne maintenance handoff or repository-maintenance continuation:

- `README.md`
- `current/human-approved-spec.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `current/todo.md`
- `current/open-questions.md`
- `notes/codex-task-authoring-and-diff-verification-guidelines.md`

This set imports the Mnemosyne maintenance live route only when the applied load mode is `maintenance_handoff`.

## Guidance-only / target-project startup set

For behavior-guidance-only, external review, or target-project support conversations, read at minimum:

- `README.md`
- `current/human-approved-spec.md`
- `commands/load-mnemosyne-guidance.md`, if available

Then read only task-relevant files:

- target-project handoff/intake/manifest/source-map files supplied or authorized for the local task;
- platform guides when platform/model/tool facts are part of the task;
- research current views when the task involves capability boundaries, new mechanisms, or target-project memory-system design.

Do not require `current/active-context.md`, `handoff/handoff-current.md`, `current/todo.md`, or `current/open-questions.md` as local action-plan files for guidance-only or target-project conversations. If read, treat their maintenance route as `background_only`.

## Task-extended reads

Read additional files only when the task needs them:

- Research current views for tool/capability/new mechanism/target-project design.
- Target-project template files for target-project work.
- Manual-import docs for import tasks.
- For first target-project dry-run preparation or execution, read `handoff/first-target-project-dry-run-onboarding-package.md` first, then the minimal profile/checklist/review instruments listed there.
- `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md` for MNEMOSYNE-031 authority/promotion questions.
- Historical v0.1 files only for historical/audit tasks.
- For handoff package generation, tier selection, replay review, or model/tool handoff comparison, read `notes/handoff-package-strategy-v0.1.md` and `notes/handoff-replay-scorecard-v0.1.md`.

`notes/v0.1-scope-and-consistency-check.md` is not part of mandatory ordinary startup or Codex startup; use it only for historical/audit work.

## Dialogue-locality guard

Before stating "next step", determine whether "next step" means:

```yaml
next_step_scope:
  local_conversation_task:
    source: current user request and visible local context
  mnemosyne_maintenance_route:
    source: current/active-context.md + handoff/handoff-current.md + current/todo.md + current/open-questions.md
    allowed_as_action_plan_only_when: applied_load_mode == maintenance_handoff
  target_project_route:
    source: target-project authority/source map, handoff package, manifest, intake package, or user-provided target materials
```

If a local task exists and the user only asks to load Mnemosyne guidance, preserve the local task. Do not replace it with the Mnemosyne maintenance route.

## Visibility instruction

Visibility is operator-controlled and may change. Do not treat public/private state alone as a defect. Verify current visibility only when relevant, especially before imports.

## Startup behavior

- Do not rely on old conversation context or model memory.
- Apply handoff/continuation correctness guidance from `current/human-approved-spec.md`; do not rely on old conversation memory as current truth, and mark missing, stale, conflicting, or uncertain handoff information explicitly.
- State the current execution source and non-execution-source boundaries before making execution claims.
- Apply objective neutral engineering style, user-action-first response structure, and long-transfer guidance from `current/human-approved-spec.md`.
- Report the applied load mode and local-task binding.
- If maintenance live-state files are missing in `maintenance_handoff`, say so; do not invent repository state.
- If maintenance live-state files are not read in `behavior_guidance_only` or `target_project_support`, say that the maintenance route was not imported.
