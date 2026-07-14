# Load Mnemosyne Guidance

This file is not an execution source. It defines a user-facing shortcut for refreshing Mnemosyne behavior guidance in the current conversation; it does not override `current/human-approved-spec.md`.

## Command names

- Load Mnemosyne guidance
- 加载 Mnemosyne 指导约束
- 加载 MNEMOSYNE 约束指导
- 加载最新指导

## Invocation examples

- “Load Mnemosyne guidance.”
- “加载 Mnemosyne 指导约束。”
- “加载 MNEMOSYNE 约束指导。”
- “加载最新指导。”

## Purpose

Use this command when the current conversation should apply the latest Mnemosyne-approved behavior constraints.

This command means behavior-constraint refresh only. It preserves the current conversation's local task mainline.

It does not start, prepare, receive, infer, or auto-detect a handoff. Work handoff is a separate explicit artifact-mediated workflow handled by:

- `commands/prepare-mnemosyne-handoff.md`
- `commands/receive-mnemosyne-handoff.md`

A Mnemosyne handoff package may explicitly require the receiving conversation to invoke this command after the package has been received. In that sequence, handoff receive and guidance refresh remain two distinct operations: the receive step establishes the transferred local task, and this command refreshes behavior constraints without replacing that task.

## Required files

Read or ask the user to provide:

- `README.md`
- `current/human-approved-spec.md`
- this command file, if available

When the current task may create or update a GitHub branch or pull request, also read:

- `current/github-single-active-pr-lineage-guard.md`

Read additional files only when the current local task independently requires them, for example:

- relevant platform guides when platform/model/tool facts are part of the local task;
- research current views when capability boundaries, new mechanisms, or target-project memory-system design claims are part of the local task;
- user-provided or authorized target-project materials when the local task is target-project work.

## Files not loaded as action-plan sources by this command

Do not read these files as the current conversation's action plan merely because the user invoked this command:

- `current/active-context.md`
- `handoff/handoff-current.md`
- `current/todo.md`
- `current/open-questions.md`

If any of those files are read for a separate explicit task, treat their maintenance route as non-execution-source background unless the user has separately invoked an explicit handoff receive or Mnemosyne maintenance task.

## Required behavior

1. Do not rely on old conversation context or model memory as repository truth.
2. Treat `current/human-approved-spec.md` as the only Mnemosyne execution source.
3. Apply the objective neutral engineering stance from `current/human-approved-spec.md`.
4. Apply the operation/conclusion separation principle from `current/human-approved-spec.md`.
5. Apply the handoff/continuation correctness principle from `current/human-approved-spec.md` when handoff artifacts or continuation claims are actually part of the local task.
6. Apply the long-transfer file/chunking guidance from `current/human-approved-spec.md` when producing long content for the user to manually forward.
7. Apply the Deep Research output exception from `current/human-approved-spec.md` when designing Deep Research prompts.
8. Apply dependency-aware staged batch-gating from `current/human-approved-spec.md` when generating multiple Pro / Deep Research / cross-conversation prompts.
9. Treat repository visibility as operator-controlled and stage-dependent; verify visibility when relevant, especially before imports, and apply the MNEMOSYNE-043 safety gate.
10. Treat platform/model/tool behavior as time-sensitive when relevant and verify current facts when possible.
11. Preserve the current conversation's local task mainline.
12. Do not import the Mnemosyne maintenance live route as the current conversation's next step.
13. Do not infer that the user wants handoff merely because this command was invoked.
14. If this command follows an explicit handoff receive, preserve the received package's task intent, boundaries, and safe next action; do not erase or replace them with maintenance live-state files.
15. When repository branch or PR creation is in scope, apply `current/github-single-active-pr-lineage-guard.md`: perform duplicate-lineage preflight before branch creation and again before PR creation, continue an existing related PR instead of creating an unapproved parallel PR, and present exactly one merge target to the user.
16. If required files for behavior guidance are unavailable, state the limitation and do not invent repository state.

## Required first response after loading

Report the refresh as behavior guidance only:

```yaml
mnemosyne_guidance_refresh:
  operation: behavior_constraint_refresh
  current_conversation_task_preserved: true_or_unknown
  handoff_started: false
  maintenance_live_route_imported: false
  auto_handoff_detection_performed: false
  execution_source: current/human-approved-spec.md
  applied_constraints:
    - execution_source_boundary
    - objective_neutral_engineering_style
    - operation_conclusion_explanation_separation
    - handoff_correctness_when_handoff_is_explicitly_in_scope
    - long_transfer_guidance_when_relevant
    - staged_prompt_generation_when_relevant
    - visibility_and_manual_import_safety_when_relevant
    - platform_freshness_check_when_relevant
    - single_active_pr_lineage_when_repository_write_is_relevant
```

Do not report Mnemosyne maintenance current phase, current active task, paused route, or next-route options as the receiving conversation's local task state merely because this command was invoked.

## Boundaries

- This command is a shortcut for refreshing existing behavior guidance in the current conversation.
- This command is not an execution source.
- This command does not approve new design content.
- This command does not authorize edits, automation, MCP, RAG, auto-writeback, or changes outside the user-approved task scope.
- This command does not authorize target workspace creation, target material ingestion, target repository write, operational build, regression formalization, or execution-source update.
- Loading the single-active PR lineage guard does not itself authorize branch creation, PR creation, parallel PRs, merges, or task-number reuse.
- This command does not authorize importing Mnemosyne maintenance live route into the current conversation.
- This command does not start handoff. No handoff exists unless the user explicitly provides or requests an artifact-mediated handoff through the separate prepare/receive workflow.
