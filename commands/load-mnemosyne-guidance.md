# Load Mnemosyne Guidance

This file is not an execution source. It defines user-facing shortcuts for loading Mnemosyne repository guidance; it does not override `current/human-approved-spec.md`.

## Command names

General:

- Load Mnemosyne guidance
- 加载 Mnemosyne 指导约束

Explicit modes:

- Load Mnemosyne behavior guidance only
- 只加载 Mnemosyne 行为指导
- Load Mnemosyne maintenance handoff
- 接手当前 Mnemosyne 仓库维护
- Load Mnemosyne target-project support guidance
- 加载 Mnemosyne 目标项目支持指导

## Invocation examples

- “Load Mnemosyne guidance.”
- “加载 Mnemosyne 指导约束。”
- “Load Mnemosyne behavior guidance only.”
- “只加载 Mnemosyne 行为指导。”
- “Load Mnemosyne maintenance handoff.”
- “接手当前 Mnemosyne 仓库维护。”
- “Load Mnemosyne target-project support guidance.”
- “加载 Mnemosyne 目标项目支持指导。”

## Purpose

Use this command when Mnemosyne guidance is not automatically loaded.

This command is mode-aware. Loading guidance does not by itself mean the receiving conversation should take over the current Mnemosyne maintenance live route.

## Load mode resolution

Before reading maintenance live-state files as an action plan, classify the requested mode.

```yaml
load_mode_resolution:
  maintenance_handoff:
    apply_when:
      - user explicitly asks to take over current Mnemosyne repository maintenance
      - user explicitly asks to resume or choose the paused Mnemosyne post-handoff route
      - user explicitly asks for the current Mnemosyne repository next route as the local task
    imports_maintenance_live_route: true

  behavior_guidance_only:
    apply_when:
      - user only says "Load Mnemosyne guidance" / "加载 Mnemosyne 指导约束"
      - current conversation already has a local non-maintenance task
      - user asks for objective/style/authority/process constraints
      - external review conversation needs Mnemosyne constraints
    imports_maintenance_live_route: false

  target_project_support:
    apply_when:
      - user asks to continue or review a target project
      - user names a target project, package, handoff, intake, manifest, or requirements task
      - local conversation has target-project materials or a target-project mainline
    imports_maintenance_live_route: false
    preserves_local_task: true

  ambiguous:
    if_existing_local_task: default_to_behavior_guidance_only_or_target_project_support
    if_no_existing_local_task: default_to_behavior_guidance_only
    do_not_import_maintenance_live_route_without_explicit_user_intent: true
```

## Required files by mode

### Always read or ask the user to provide

- `README.md`
- `current/human-approved-spec.md`
- this command file, if available

### `behavior_guidance_only`

Read only the files needed to apply durable behavior guidance.

Do not require these files as local action-plan sources:

- `current/active-context.md`
- `handoff/handoff-current.md`
- `current/todo.md`
- `current/open-questions.md`

If those files are read for background, explicitly label repository current route as `background_only`, not the receiving conversation's local task.

### `maintenance_handoff`

Read or ask the user to provide:

- `README.md`
- `current/human-approved-spec.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `handoff/startup-instructions.md`
- `current/todo.md`
- `current/open-questions.md`
- `notes/codex-task-authoring-and-diff-verification-guidelines.md`

If the task involves tool capability, platform capability, model behavior, automation feasibility, GitHub writes, Claude/Fable review, or target-project memory-system design, also read the relevant platform guides / research current views referenced by startup instructions.

### `target_project_support`

Read or ask the user to provide:

- `README.md`
- `current/human-approved-spec.md`
- this command file, if available
- target-project authority/source map, handoff package, intake package, manifest, or user-provided local materials relevant to the target task

Do not use Mnemosyne maintenance live route as the target project's next step unless the user explicitly asks to switch to Mnemosyne maintenance handoff.

## Required behavior

1. Do not rely on old conversation context or model memory.
2. Treat `current/human-approved-spec.md` as the only Mnemosyne execution source.
3. Apply the handoff/continuation correctness principle from `current/human-approved-spec.md`.
4. Preserve the receiving conversation's local task mainline unless the user explicitly asks to take over Mnemosyne maintenance.
5. Separate durable behavior guidance from maintenance live state.
6. For handoff/replay work, do not rely on old conversation memory as current truth; recover critical state from authorized files and mark missing, stale, conflicting, or uncertain information explicitly.
7. When applicable, also read the task-relevant research evidence current views referenced by `handoff/startup-instructions.md`.
8. Apply the objective neutral engineering stance from `current/human-approved-spec.md`.
9. Apply the operation/conclusion separation principle from `current/human-approved-spec.md`.
10. If the response asks the user to do something, put the operation steps/content in a clearly marked section before explanation.
11. If the response reports findings or conclusions, put the conclusion/problem/result in a clearly marked section before supporting explanation.
12. Apply the long-transfer file/chunking guidance from `current/human-approved-spec.md`. When producing long content for the user to manually forward, prefer generating a downloadable file and show only a concise summary in the chat. If the content must be split, label chunks with package/task title, stable ID, chunk number, total chunk count if known, and wait-for-all-chunks instruction. When designing Deep Research prompts, apply the Deep Research exception: require the full report body in the final Deep Research answer/report body; do not ask Deep Research to provide only a summary plus downloadable link; any downloadable file may be optional backup only.
13. When generating multiple Pro / Deep Research / cross-conversation prompts, apply dependency-aware staged batch-gating: remind/ask the user to switch current conversation intelligence/reasoning level before high-risk or high-cost prompt packages when needed, state each prompt's `execute_in` location, and do not generate downstream prompts if upstream results may change them. Deep Research prompts must require the full report body in the final answer.
14. Treat repository visibility as operator-controlled and stage-dependent; do not treat public/private state alone as a defect. Verify visibility when relevant, especially before imports, and apply the MNEMOSYNE-043 safety gate.
15. If required files for the selected mode are unavailable, ask for the missing files or clearly state the limitation. Do not invent repository state.

## Required first response after loading

Include a guidance load binding report:

```yaml
guidance_load_binding:
  detected_local_task:
  requested_load_mode:
  applied_load_mode:
  imported_maintenance_live_route: true_or_false
  repo_current_route_used_as: action_plan | background_only | not_used
  local_task_preserved: true_or_false_or_unknown
  possible_context_misbinding: none_detected | risk_detected | unknown
  next_action_basis:
    - local_user_request
    - repository_maintenance_live_route
    - target_project_route
    - unknown_pending_user_confirmation
```

For `maintenance_handoff`, also report:

- current execution source;
- current phase;
- non-execution-source boundaries;
- current forbidden actions;
- current next-route options;
- whether any conflict or missing file was found.

For `behavior_guidance_only` or `target_project_support`, do not report Mnemosyne maintenance current phase as the receiving conversation's local next step. If maintenance files were read, label them `background_only`.

## Boundaries

- This command is a shortcut for loading existing repository guidance.
- This command is not an execution source.
- This command does not approve new design content.
- This command does not authorize edits, automation, MCP, RAG, auto-writeback, or changes outside the user-approved task scope.
- This command does not authorize target workspace creation, target material ingestion, target repository write, operational build, regression formalization, or execution-source update.
- This command does not authorize importing Mnemosyne maintenance live route into a target/project-specific conversation.
