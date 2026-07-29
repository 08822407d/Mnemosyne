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
- `current/user-operation-next-step-capability-and-intent-guard.md`
- this command file, if available

When the current task may perform any GitHub or connected-repository write—including a direct file update, repository comment, branch or pull-request operation—or may create or modify an important record intended for repository publication, also read:

- `current/run-context-and-pr-provenance-guard.md`

When the current task may create or update a GitHub branch or pull request, also read:

- `current/github-single-active-pr-lineage-guard.md`

Purely read-only repository inspection does not trigger these additional reads.

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
5. Apply `current/user-operation-next-step-capability-and-intent-guard.md`:
   - put current user operations in the opening `操作内容（需要你手动执行）` section, or state `无需用户操作`;
   - put a meaningful follow-on in a closing, visually explicit `下一步` section;
   - never hide a current mandatory user action only at the end;
   - explicitly state whether the next stage requires, recommends, or does not require frontier/Pro-class reasoning;
   - re-estimate model capability after research, failure, safety, surface-capability, or scope changes;
   - separately assess whether Pro Deep Research is unnecessary, optional, recommended, required before a high-impact decision, or premature because of an upstream dependency;
   - separately assess whether an independent Fable-class or other-provider frontier review has a distinct non-duplicative role;
   - when research is recommended or required and the topic is sufficiently frozen, automatically deliver a complete ready-to-run task and report contract without requiring another frontier turn merely to ask for the prompt;
   - never fabricate a research report before the designated run exists and never treat task generation as quota or execution authorization;
   - route owner preferences to user clarification and external evidence gaps to verification/research rather than asking the wrong actor;
   - treat user wording as primary evidence but not automatically a complete final specification;
   - preserve likely intent, alternatives, assumptions, uncertainty, and user correction rights without mind-reading or overriding confirmed decisions;
   - when a next-tier model can conduct interactive clarification, provide a self-contained clarification package with question context, meaning, consequences, options, recommendations, answer formats, stop rules, and escalation triggers;
   - require the next-tier interviewer to maintain an answer ledger, explain why questions matter, capture corrections, and return high-impact conflicts to frontier review.
6. Apply the handoff/continuation correctness principle from `current/human-approved-spec.md` when handoff artifacts or continuation claims are actually part of the local task.
7. Apply the long-transfer file/chunking guidance from `current/human-approved-spec.md` and `current/artifact-delivery-and-direct-generation-guard.md` when producing content for transfer, backup, archival, or later machine/operator reuse.
8. When designing a prompt, taskbook, handoff, Work task, Pro task, Deep Research task, Codex task, or future-Agent task whose complete final response must be returned to another conversation or preserved for review, explicitly require a separately downloadable `<TASK_ID>-complete-response.md` or stable equivalent in the same final response. Distinguish it from named substantive artifacts; do not make the operator send a second prompt solely to export the already-issued response.
9. When the user explicitly requests a low-risk downloadable artifact and no additional content decision or external-action authorization is required, create the local artifact in the same response when an available tool can do so safely; do not merely promise later generation.
10. Before claiming delivery, verify that file creation succeeded and provide a real artifact link or available transfer pointer. Never invent a path or attachment.
11. Keep safe local artifact generation separate from any independently gated repository write, upload, email, forwarding, quota spend, research execution, or other external action.
12. Apply the Deep Research output exception from `current/human-approved-spec.md`: the final Deep Research report body remains in the final report/answer, while prompts and other transfer artifacts remain file-first when applicable. If the full Deep Research response must be transferred, require an auxiliary complete-response file without replacing the inline canonical report.
13. Apply dependency-aware staged batch-gating from `current/human-approved-spec.md` when generating multiple Pro / Deep Research / cross-conversation prompts. Do not generate downstream tasks that are likely to be invalidated by an upstream report unless the user explicitly accepts that risk.
14. Treat repository visibility as operator-controlled and stage-dependent; verify visibility when relevant, especially before imports, and apply the MNEMOSYNE-043 safety gate.
15. Treat platform/model/tool behavior as time-sensitive when relevant and verify current facts when possible.
16. Preserve the current conversation's local task mainline.
17. Do not import the Mnemosyne maintenance live route as the current conversation's next step.
18. Do not infer that the user wants handoff merely because this command was invoked.
19. If this command follows an explicit handoff receive, preserve the received package's task intent, boundaries, and safe next action; do not erase or replace them with maintenance live-state files.
20. When repository branch or PR creation is in scope, apply `current/github-single-active-pr-lineage-guard.md`: perform duplicate-lineage preflight before branch creation and again before PR creation, continue an existing related PR instead of creating an unapproved parallel PR, and present exactly one merge target to the user.
21. When any GitHub or connected-repository write, or creation or modification of an important record intended for repository publication, is in scope, apply `current/run-context-and-pr-provenance-guard.md`: record actual actor/action source, the operator-visible or operator-reported product selection verbatim, any provider-documented normalization separately, backend status under the guard's discriminated schema, model/surface switches, component review relations, human adjudication, task-scoped user authorization, and the later-review boundary.
22. If required files for behavior guidance are unavailable, state the limitation and do not invent repository state.

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
    - opening_user_operation_or_no_operation_section
    - closing_next_step_section_when_meaningful
    - explicit_next_step_model_capability_estimate
    - explicit_Pro_Deep_Research_need_assessment
    - parallel_frontier_research_role_assessment
    - automatic_ready_to_run_research_task_delivery_when_recommended_and_ready
    - no_fabricated_report_or_automatic_quota_spend
    - human_expression_and_intent_reconstruction_with_user_correction
    - context_rich_clarification_package_for_next_tier_interaction
    - cumulative_answer_ledger_and_frontier_escalation
    - handoff_correctness_when_handoff_is_explicitly_in_scope
    - artifact_file_first_delivery_when_relevant
    - complete_response_transfer_file_when_full_reply_return_is_required
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
- Loading the user-operation/capability/research/clarification/intent guard does not authorize model switching, quota use, research execution, psychological profiling, repository writes, or changes to a target project's truth source.
- Loading the artifact-delivery guard does not authorize repository writes, uploads, email, forwarding, or other external actions.
- This command does not authorize edits, automation, MCP, RAG, auto-writeback, or changes outside the user-approved task scope.
- This command does not authorize target workspace creation, target material ingestion, target repository write, operational build, regression formalization, or execution-source update.
- Loading the single-active PR lineage guard does not itself authorize branch creation, PR creation, parallel PRs, merges, or task-number reuse.
- Loading the run-context and PR provenance guard does not attest a backend model, authorize a model switch, or make a model label an execution source.
- This command does not authorize importing Mnemosyne maintenance live route into the current conversation.
- This command does not start handoff. No handoff exists unless the user explicitly provides or requests an artifact-mediated handoff through the separate prepare/receive workflow.
