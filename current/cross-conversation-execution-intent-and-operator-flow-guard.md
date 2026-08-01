# Cross-Conversation Execution Intent and Dedicated Operator Flow Guard

> User-approved Mnemosyne behavior guard for making it unmistakable whether a cross-conversation or external task is being analyzed, prepared, offered, or actually requested for execution. This file is not a standalone execution source; `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
guard_id: MNEMOSYNE-CROSS-CONVERSATION-EXECUTION-INTENT-001
created_by_task: MNEMOSYNE-187
status: active_after_MNEMOSYNE_187_merge
execution_source: current/human-approved-spec.md
execution_source_modified: false
applies_to:
  - Pro_or_Deep_Research_tasks
  - Fable_or_other_independent_frontier_tasks
  - new_ChatGPT_conversation_prompts_and_handoffs
  - Codex_tasks
  - replay_validation_review_and_adjudication_tasks
  - other_cross_conversation_or_external_Agent_work_packages
scope_relation:
  complements:
    - current/user-operation-next-step-capability-and-intent-guard.md
    - current/artifact-delivery-and-direct-generation-guard.md
  controls_more_specifically:
    - execution_intent_declaration
    - current_vs_later_user_action
    - dedicated_operator_flow_placement
```

## 1. Problem addressed

A response can contain all required facts and even a complete operator procedure while still leaving the user unsure whether:

- the response is analysis only;
- a task is merely prepared for future use;
- execution is optional or required;
- execution may begin now or only after a gate;
- the user should spend quota in the current stage;
- detailed steps are explanatory examples or actual instructions.

A long explanation followed later by launch steps is especially ambiguous. Merely saying a task is `ready`, that the user `may run` it, or that it is a `safe next action` does not by itself select or request execution.

## 2. Required execution-intent declaration

Whenever a substantial response discusses, designs, repairs, publishes, or delivers a cross-conversation/external task, the opening operation section must explicitly declare the task's execution intent before long analysis.

Use this schema or a plain-language equivalent with the same semantics:

```yaml
execution_intent:
  response_role:
    ANALYSIS_ONLY |
    ANALYSIS_AND_PREPARATION |
    ANALYSIS_AND_LAUNCH |
    LAUNCH_ONLY
  task_id:
  execution_disposition:
    DO_NOT_RUN |
    DEFERRED |
    READY_NOT_SELECTED |
    RUN_NOW_OPTIONAL |
    RUN_NOW_REQUIRED |
    RUN_AFTER_GATE_OPTIONAL |
    RUN_AFTER_GATE_REQUIRED
  current_required_user_action:
  current_optional_user_action:
  prerequisite_gates: []
  external_execution_or_quota_authorized: true | false
```

Rules:

1. `READY_NOT_SELECTED` means the task package is usable but the current response does not ask the user to launch it.
2. `RUN_AFTER_GATE_OPTIONAL` means the gate is a current action only when explicitly required; the later run remains optional and must not be presented as a current mandatory operation.
3. `DO_NOT_RUN` and `DEFERRED` must use direct wording such as `本回复不要求启动该任务` or `当前不要执行该任务`.
4. `RUN_NOW_REQUIRED` and `RUN_AFTER_GATE_REQUIRED` require an explicit user-side execution instruction and must not be inferred from recommendation language.
5. Quota use, model switching, connector activation, external research execution, and repository writes remain separately authorized actions.
6. An analysis or repair task may prepare a runnable package without selecting its execution. In that case use `ANALYSIS_AND_PREPARATION` plus `READY_NOT_SELECTED` or `RUN_AFTER_GATE_OPTIONAL`, not `ANALYSIS_AND_LAUNCH`.

## 3. Dedicated operator-flow section

When `execution_disposition` is any `RUN_*` value, or when a complete future flow is supplied for a ready task, the response must include a dedicated major section immediately after the opening operation/intent section and before extended findings or analysis.

Use a heading that carries both task identity and timing, for example:

```text
## FABLE5-EXAMPLE-001 操作流程（现在可选执行）
## FABLE5-EXAMPLE-001 操作流程（合并 PR 后可选执行）
## FABLE5-EXAMPLE-001 操作流程（当前必须执行）
## 当前不执行 FABLE5-EXAMPLE-001
```

The dedicated section must contain all material executable steps in one place, including as applicable:

- prerequisite merge, approval, artifact, or model gate;
- exact product surface, model/mode/effort, and feature state;
- clean-context, Project, Memory, Files, connector, and independence requirements;
- exact files, folders, links, downloads, repository, branch/ref, or attachments;
- complete preflight message and pass criteria;
- complete launch message;
- ordered operator steps;
- stop and fallback conditions;
- result/export requirements and return destination;
- whether another task requires a separate context;
- whether external execution or quota use is authorized.

## 4. Separation from analysis

1. Do not scatter executable steps across failure analysis, design explanation, findings, limitations, and the closing `下一步` section.
2. Analysis may explain why the flow is designed as it is, but the user must be able to execute the task by reading the dedicated operator-flow section alone.
3. The closing `## 下一步` section may summarize the selected or possible continuation; it may not be the first or only place where execution intent appears.
4. When the response is analysis only, do not include imperative launch steps that appear active. A future example must be labelled `prepared example — current execution not requested`.
5. When the only current required action is PR review or merge, say explicitly that research execution remains false until the stated post-merge selection. Do not make the user infer this from repository state.
6. For multiple tasks, give each task a separate disposition and separate dedicated operator-flow section. Do not combine independent runs into one ambiguous checklist.

## 5. Required distinction between readiness and selection

```yaml
readiness_is_not_selection:
  task_files_exist: does_not_mean_run_requested
  ready_queue_entry_exists: does_not_mean_run_requested
  task_is_recommended: does_not_mean_run_now
  user_may_run: optional_only_unless_explicitly_upgraded
  safe_next_action: candidate_continuation_not_automatic_authorization
```

A task becomes a current user operation only when the response explicitly states a `RUN_*` disposition or the user directly selects execution.

## 6. Verification before delivery

Before sending a substantial cross-conversation task response, verify:

```yaml
response_execution_clarity_check:
  execution_intent_declared: true
  current_required_vs_optional_actions_separated: true
  current_vs_post_gate_timing_separated: true
  quota_or_external_execution_status_explicit: true
  dedicated_operator_flow_present_when_applicable: true
  executable_steps_not_scattered: true
  analysis_only_or_launch_role_unambiguous: true
  closing_next_step_not_the_only_execution_signal: true
```

If any material field is ambiguous or the operator-flow artifact conflicts with the visible response, execution must remain `DO_NOT_RUN` until corrected.

## 7. Boundaries

This guard does not:

- authorize research, quota use, model switching, connector activation, repository write, merge, upload, or another external action;
- require every analysis to include a full task workflow;
- require duplication of a long task body when a verified downloadable or repository artifact is supplied;
- make a task authoritative or executable merely because it is ready;
- change a target project's truth source or owner rule;
- replace the separate file-first, artifact-verification, PR-lineage, provenance, safety, privacy, or human-decision controls.
