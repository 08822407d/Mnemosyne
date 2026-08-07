# Current Mnemosyne Live Wayfinding

> Non-execution-source route map. `current/human-approved-spec.md` remains Mnemosyne's only execution source. Route-status files do not authorize external research, quota use, validation, target-project writes, or automatic route selection.

```yaml
record_type: live_wayfinding_selection
latest_updated_by_task: MNEMOSYNE-196
recorded_at: 2026-08
route: no_active_selected_mainline_after_FCV_indefinite_pause
status: CURRENT_CONVERSATION_ARCHIVE_ELIGIBLE_AFTER_MNEMOSYNE_196_MERGE
execution_source: current/human-approved-spec.md
execution_source_modified: false
```

## 1. Completed temporary Meta-Agent diversion

```yaml
Meta_Agent:
  current_repository: 08822407d/Meta-Agent
  current_target_truth: current/approved-spec.md
  cutover_merge: eb71ed350e7cf1783d73580466a3656fad2a3b69
  operational_activation: false

Mnemosyne_source_retirement:
  PR: 261
  merge_commit: c85ebba5425da4daf6f3344690778682b9f79d66
  live_Meta_Agent_writer: false
  branches_after_hygiene:
    - master
```

Meta-Agent product work no longer runs under `target-projects/meta-agent/` in current Mnemosyne `master`.

## 2. Frontier-clarification validation route

The route was restored after Meta-Agent migration and then explicitly paused indefinitely by the Owner.

```yaml
frontier_clarification_validation:
  state: INDEFINITELY_PAUSED_BY_OWNER
  current_conversation_selected_for_execution: false
  future_resumption_conversation: separate_dedicated_conversation_selected_by_user
  pause_record: notes/route-pauses/frontier-clarification-validation-fable5-indefinite-pause-2026-08.md
  route_status: current/frontier-clarification-validation-handoff-status.md
  Fable_status: current/fable5-research-delivery-status.md
  resumption_handoff: handoff/mnemosyne-frontier-clarification-validation-fable-resumption-package.md

A1:
  task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  display_name: MNE-DR-001 验证包审计
  state: DEFERRED_INDEFINITELY_BY_OWNER
  valid_substantive_report: absent
  quota_authorized: false

A2:
  task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
  display_name: MNE-DR-002 表面威胁
  state: DEFERRED_INDEFINITELY_BY_OWNER_AND_PENDING_VALID_A1_ADJUDICATION
  quota_authorized: false
```

Task artifacts remain preserved. They are not selected or runnable during the pause.

## 3. Current conversation closure

```yaml
current_conversation:
  role: Mnemosyne_self_development_and_maintenance
  selected_mainline: none
  selected_substantive_work_remaining: none
  repository_work_remaining_after_MNEMOSYNE_196_merge: none
  external_work_remaining_here: none
  archive_eligible_after_merge: true
```

The absence of an active mainline is intentional. This conversation must not take over another route merely to continue working.

## 4. Other routes not selected here

```yaml
other_routes:
  Meta_Agent_product_build:
    repository: 08822407d/Meta-Agent
    owner_conversation: dedicated_Meta_Agent_conversation
    selected_here: false

  non_FABLE_health_review:
    owner_conversation: separate_existing_conversation
    selected_here: false

  ADAPTIVE_EXPLANATION:
    Stage_A: completed_and_accepted_with_corrections
    Stage_B0_protocol_design: selected_and_prepared
    Stage_B0_smoke_execution_authorized: false
    selected_here: false
    status_ref: current/adaptive-explanation-stage-a-research-status.md

  MODEL_CAPABILITY_PLANNING_001:
    selected_here: false

  HO_GUIDANCE_001:
    selected_here: false

  GPT_LIVE_REALTIME_VOICE_LEARNING_SURFACE:
    selected_here: false

  LONGITUDINAL_LEARNER_MEMORY_AND_CROSS_AGENT_INTEGRATION:
    selected_here: false
```

Listing does not authorize or transfer route ownership.

## 5. Work completed by MNEMOSYNE-196

```yaml
completed:
  - verify_PR262_merge
  - record_owner_indefinite_Fable_pause
  - prepare_future_receive_only_resumption_handoff
  - mark_A1_and_A2_non_runnable_until_explicit_future_resumption
  - adopt_prominent_PR_post_merge_branch_disposition_guard
  - determine_current_conversation_has_no_remaining_selected_work
```

## 6. Safe next action

```yaml
safe_next_action:
  current:
    - human_review_and_merge_MNEMOSYNE_196_PR_or_request_changes
  after_merge:
    - archive_this_conversation_if_no_new_user_task
  automatic_route_selection: false
  automatic_Deep_Research: false
  automatic_Fable: false
  automatic_validation: false
```
