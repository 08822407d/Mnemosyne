# Mnemosyne Frontier Clarification Validation — New-Conversation Startup Prompt

Use this prompt in a **fresh Pro / frontier-capable Mnemosyne maintenance conversation** after the canonical MNEMOSYNE-180 handoff PR has merged.

Repository: `08822407d/Mnemosyne`

## Task

Receive the repository-backed handoff for the PR #231 post-adjudication frontier-clarification validation route.

This first operation is **receive-only**. Do not prepare the validation package, execute validation, write the repository, modify an execution source, continue Meta-Agent product work or take over the non-FABLE health-review route in the first response.

## Mandatory first read order

Read these files separately and preserve their roles:

```text
handoff/mnemosyne-frontier-clarification-validation-handoff-package.md
commands/receive-mnemosyne-handoff.md
current/human-approved-spec.md
current/frontier-planning-clarification-handoff-research-status.md
current/frontier-planning-clarification-handoff-adjudication-guard.md
current/deep-research-report-delivery-correction-guard.md
notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md
notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/03-cross-report-consensus-conflict-and-adjudication.md
notes/research-batch-reviews/2026-07-frontier-planning-clarification-handoff/04-interim-architecture-and-validation-decision.md
```

Read additional files only if the package's claims require them. Do not use `current/active-context.md`, `handoff/handoff-current.md`, `current/todo.md` or `current/open-questions.md` as this conversation's action plan.

## Baseline to verify, not assume

```yaml
expected_baseline:
  handoff_package_id: MNEMOSYNE-FRONTIER-CLARIFICATION-VALIDATION-HANDOFF-001
  source_checkpoint:
    PR: 231
    merge_commit: 96eb9757b6554d397267501dd29e4682c155d830
  research:
    Pro: complete_accepted_with_corrections
    Fable: complete_accepted_with_corrections_no_rerun
    additional_same_topic_research: not_needed
  architecture:
    universal_default: rejected
    direct_frontier: high_impact_low_clarity
    structured_owner_package: available_route
    next_tier_interviewer: validation_gated_candidate
    gated_mixed_escalation: preferred_validation_candidate_not_validated_default
  validation:
    design_exists: true
    package_prepared: false
    selected_for_execution: false
    executed: false
  transferred_task: PREPARE_READ_ONLY_VALIDATION_PACKAGE
  Meta_Agent_route_owner: existing_dedicated_Meta_Agent_conversation
  non_FABLE_health_review_owner: existing_separate_conversation
```

If repository evidence conflicts with a material baseline claim, report the conflict and stop.

## First-response output contract

Return only:

```yaml
mnemosyne_handoff_receive:
  package_present: true | false
  package_id:
  package_status: non_execution_source_transfer_artifact
  repository: 08822407d/Mnemosyne
  verified_master_sha:
  handoff_PR_merged: true | false | unknown
  receiver_guidance_load:
    project_guidance: not_applicable
    mnemosyne_guidance: required
    refresh_completed: pending
  execution_source: current/human-approved-spec.md
  evidence_paths_checked: []
  evidence_paths_missing_or_unchecked: []
  current_task_from_package: PREPARE_READ_ONLY_VALIDATION_PACKAGE
  research_state:
    Pro:
    Fable:
    additional_research:
  validation_state:
    design_exists:
    package_prepared:
    selected:
    executed:
  route_ownership:
    local_route: this_new_Mnemosyne_conversation_after_successful_receive_and_guidance_refresh
    Meta_Agent_product_build: existing_dedicated_Meta_Agent_conversation
    non_FABLE_health_review: existing_separate_conversation
  Meta_Agent_route_imported: false
  non_FABLE_health_review_route_imported: false
  repository_write_performed: false
  forbidden_actions: []
  safe_next_action: wait_for_separate_guidance_refresh_and_continuation_instruction
  limitations_or_unknowns: []
  status: RECEIVED_AWAITING_GUIDANCE_REFRESH | INPUT_OR_STATE_CONFLICT
```

After the YAML, add no more than a short paragraph explaining the single next user operation. Then stop.

## Receiver guidance load

```yaml
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
  ordered_operations:
    - receive_authorized_handoff_package
    - execute_Load_Mnemosyne_guidance_as_separate_operation
    - confirm_received_task_preserved
    - continue_received_task_under_refreshed_constraints
```

Do not automatically load guidance in the receive response.

After a successful receive, wait for the user to send this separate instruction:

```text
加载 MNEMOSYNE 约束指导。刷新后确认已接收的 PREPARE_READ_ONLY_VALIDATION_PACKAGE 任务未被替换，然后继续执行该任务：只准备完整验证包和单一 PR，不运行 V0/V1/V2/V3 验证，不使用真实用户数据，不修改 Meta-Agent 或 non-FABLE health-review 路线。
```

## Hard prohibitions

- Do not treat the handoff package as execution source.
- Do not execute validation during receive.
- Do not generate synthetic validation results that were never run.
- Do not modify `current/human-approved-spec.md`.
- Do not modify `target-projects/meta-agent/` or perform Meta-Agent owner acceptance.
- Do not take over `handoff/handoff-current.md` or the non-FABLE health-review route.
- Do not run more Pro Deep Research or Fable research by default.
- Do not infer exact backend identity from the visible selection, latency, style or self-report.
- Do not create a repository branch or PR until the separate guidance refresh/continuation instruction has been received and latest-master/open-PR preflight has passed.
