# Cross-Conversation Execution Intent and Dedicated Operator Flow — Adoption Record

```yaml
record_id: MNEMOSYNE-CROSS-CONVERSATION-EXECUTION-INTENT-ADOPTION-001
created_by_task: MNEMOSYNE-187
artifact_role: non_execution_behavior_guard_adoption_record
status: pending_human_review_and_merge
execution_source: false
execution_source_modified: false
```

## 1. User-observed problem

The user reviewed the MNEMOSYNE-186 response and could not determine whether it was:

- only an explanation of the failed A1 run and repaired workflow; or
- also a direct request to begin a new Fable5 run.

The user required a behavior constraint under which any requested research/external-task execution has a clearly separated operation-flow section rather than steps mixed into analysis.

## 2. Adjudication of the prior response

```yaml
MNEMOSYNE_186_response:
  response_role: ANALYSIS_AND_PREPARATION
  current_required_action:
    - review_and_merge_PR_239
  A1:
    execution_disposition: RUN_AFTER_GATE_OPTIONAL
    gate: PR_239_merge
    immediate_execution_required: false
    complete_operator_flow_present: true
    placement: after_extended_analysis_and_repair_explanation
  A2:
    execution_disposition: DEFERRED
    immediate_execution_required: false
  analysis_only: false
  immediate_launch_request: false
  ambiguity_finding: VALID
```

The response technically contained an `A1 完整操作流程` section and said A1 was optional after the PR merge. It therefore delivered a future executable workflow. However, it did not use one explicit execution-disposition label, and the detailed flow appeared after substantial analysis. The user could reasonably read the response as a repair explanation rather than an optional post-gate launch package.

## 3. Adopted repair

The new guard requires every cross-conversation/external task response to distinguish:

```yaml
- ANALYSIS_ONLY
- ANALYSIS_AND_PREPARATION
- ANALYSIS_AND_LAUNCH
- LAUNCH_ONLY
```

and to use one explicit execution disposition:

```yaml
- DO_NOT_RUN
- DEFERRED
- READY_NOT_SELECTED
- RUN_NOW_OPTIONAL
- RUN_NOW_REQUIRED
- RUN_AFTER_GATE_OPTIONAL
- RUN_AFTER_GATE_REQUIRED
```

When a run is requested or a complete future flow is supplied, a dedicated major section such as:

```text
## <TASK_ID> 操作流程（现在可选执行）
```

must appear immediately after the opening operation/intent section and before extended analysis. All material executable steps must be kept together there.

## 4. Fable route clarification

After PR #239 merged, revised A1 became technically ready, but readiness did not select execution.

```yaml
A1:
  current_state: READY_NOT_SELECTED
  current_execution_requested: false
  current_execution_required: false
A2:
  current_state: DEFERRED_PENDING_A1_ADJUDICATION
  current_execution_requested: false
```

A future run requires an explicit user selection or a future response that clearly uses a `RUN_*` disposition.

## 5. Files implementing the repair

```text
current/cross-conversation-execution-intent-and-operator-flow-guard.md
commands/load-mnemosyne-guidance.md
current/fable5-research-delivery-status.md
```

## 6. Boundaries

This adoption record and guard do not:

- execute A1 or A2;
- authorize Fable5, Deep Research, quota use, connector activation, model switching, or repository write;
- change `current/human-approved-spec.md`;
- change the A1/A2 research questions or validation package;
- modify Meta-Agent target truth or take over its product route;
- make ready-task existence equivalent to user selection.
