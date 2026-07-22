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
- `current/artifact-delivery-and-direct-generation-guard.md`
- this command file, if available

When the current task may create or update a GitHub branch or pull request, also read:

- `current/github-single-active-pr-lineage-guard.md`
- `current/run-context-and-pr-provenance-guard.md`

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
6. Apply the long-transfer file/chunking guidance from `current/human-approved-spec.md` and `current/artifact-delivery-and-direct-generation-guard.md` when producing content for transfer, backup, archival, or later machine/operator reuse.
7. When the user explicitly requests a low-risk downloadable artifact and no additional content decision or external-action authorization is required, create the local artifact in the same response when an available tool can do so safely; do not merely promise later generation.
8. Before claiming delivery, verify that file creation succeeded and provide a real artifact link or available transfer pointer. Never invent a path or attachment.
9. Keep safe local artifact generation separate from any independently gated repository write, upload, email, forwarding, or other external action.
10. Apply the Deep Research output exception from `current/human-approved-spec.md`: the final Deep Research report body remains in the final report/answer, while prompts and other transfer artifacts remain file-first when applicable.
11. Apply dependency-aware staged batch-gating from `current/human-approved-spec.md` when generating multiple Pro / Deep Research / cross-conversation prompts.
12. Treat repository visibility as operator-controlled and stage-dependent; verify visibility when relevant, especially before imports, and apply the MNEMOSYNE-043 safety gate.
13. Treat platform/model/tool behavior as time-sensitive when relevant and verify current facts when possible.
14. Preserve the current conversation's local task mainline.
15. Do not import the Mnemosyne maintenance live route as the current conversation's next step.
16. Do not infer that the user wants handoff merely because this command was invoked.
17. If this command follows an explicit handoff receive, preserve the received package's task intent, boundaries, and safe next action; do not erase or replace them with maintenance live-state files.
18. When repository branch or PR creation is in scope, apply `current/github-single-active-pr-lineage-guard.md`: perform duplicate-lineage preflight before branch creation and again before PR creation, continue an existing related PR instead of creating an unapproved parallel PR, and present exactly one merge target to the user.
19. When repository branch or PR creation is in scope, apply `current/run-context-and-pr-provenance-guard.md`: record actual actor/action source, the operator-visible or operator-reported product selection using current official terminology when verifiable, the provider-documented mapping separately, backend identity as unknown unless strongly attested, model/surface switches, reviewer independence, and the later-review boundary.
20. If required files for behavior guidance are unavailable, state the limitation and do not invent repository state.

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
    - artifact_file_first_delivery_when_relevant
    - same_response_low_risk_artifact_generation_when_relevant
    - verified_artifact_link_and_no_invented_path
    - Deep_Research_full_report_body_exception
    - staged_prompt_generation_when_relevant
    - visibility_and_manual_import_safety_when_relevant
    - platform_freshness_check_when_relevant
    - single_active_pr_lineage_when_repository_write_is_relevant
    - run_context_and_PR_model_disclosure_when_repository_write_is_relevant
```

Do not report Mnemosyne maintenance current phase, current active task, paused route, or next-route options as the receiving conversation's local task state merely because this command was invoked.

## Boundaries

- This command is a shortcut for refreshing existing behavior guidance in the current conversation.
- This command is not an execution source.
- This command does not approve new design content.
- Loading the artifact-delivery guard does not authorize repository writes, uploads, email, forwarding, or other external actions.
- This command does not authorize edits, automation, MCP, RAG, auto-writeback, or changes outside the user-approved task scope.
- This command does not authorize target workspace creation, target material ingestion, target repository write, operational build, regression formalization, or execution-source update.
- Loading the single-active PR lineage guard does not itself authorize branch creation, PR creation, parallel PRs, merges, or task-number reuse.
- Loading the run-context and PR provenance guard does not attest a backend model, authorize a model switch, or make a model label an execution source.
- This command does not authorize importing Mnemosyne maintenance live route into the current conversation.
- This command does not start handoff. No handoff exists unless the user explicitly provides or requests an artifact-mediated handoff through the separate prepare/receive workflow.
