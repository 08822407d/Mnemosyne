# Current Mnemosyne Live Wayfinding

> Non-execution-source route map. `current/human-approved-spec.md` remains Mnemosyne's only execution source. Route-status files do not authorize external research, quota use, validation, or target-project writes.

```yaml
record_type: live_wayfinding_selection
latest_updated_by_task: MNEMOSYNE-195
recorded_at: 2026-08-07
route: Mnemosyne_frontier_clarification_validation
status: FRONTIER_CLARIFICATION_VALIDATION_RESUMED_AFTER_META_AGENT_MIGRATION_CLOSEOUT
execution_source: current/human-approved-spec.md
execution_source_modified: false
```

## 1. Completed temporary diversion

Meta-Agent repository migration support is complete on the Mnemosyne side.

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

Meta-Agent product work no longer runs under `target-projects/meta-agent/` in current Mnemosyne `master`. The old paths are retired redirects and the pinned historical snapshot remains rollback evidence only.

## 2. Current conversation route ownership

```yaml
current_conversation:
  role: Mnemosyne_self_development_and_maintenance
  selected_mainline: FRONTIER_CLARIFICATION_VALIDATION_STAGE_A

Meta_Agent_product_build:
  owner_conversation: dedicated_Meta_Agent_conversation
  repository: 08822407d/Meta-Agent
  takeover_by_current_conversation: prohibited

non_FABLE_health_review:
  owner_conversation: separate_existing_conversation
  takeover_by_current_conversation: prohibited
```

## 3. Selected Mnemosyne mainline

```yaml
current_mainline:
  route: Mnemosyne_frontier_clarification_validation
  package: notes/frontier-clarification-validation-package/README.md
  status: package_merged_A1_substantive_audit_not_yet_received
  route_status: current/frontier-clarification-validation-handoff-status.md
  Fable_status: current/fable5-research-delivery-status.md
  workflow: notes/research-operations/claude-fable5-project-knowledge-research-v0.4.md
```

### A1

```yaml
A1:
  task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
  display_name: MNE-DR-001 验证包审计
  current_state: PAUSED_QUOTA_READY_NOT_SELECTED
  Project_knowledge_access: empirically_supported
  valid_substantive_report: absent
  active_contract: notes/research-prompts/FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001-execution-contract-v0.4.md
```

### A2

```yaml
A2:
  task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
  display_name: MNE-DR-002 表面威胁
  current_state: DEFERRED_PENDING_VALID_A1_ADJUDICATION
```

## 4. Automatic progress completed by MNEMOSYNE-195

```yaml
completed:
  - verify_PR261_merge_and_final_source_retirement
  - verify_only_master_branch_remains
  - close_stale_Meta_Agent_live_wayfinding_in_Mnemosyne
  - adjudicate_A1_Project_Search_mode_probe
  - replace_separate_paid_R0_with_single_invocation_G0_G1_workflow
  - prepare_A1_and_A2_v0_4_contracts_and_operator_packages
  - preserve_A1_pause_and_A2_defer_state
```

No Fable run or validation was executed.

## 5. Other prepared or completed routes not selected here

```yaml
other_routes:
  ADAPTIVE_EXPLANATION:
    Stage_A: completed_and_accepted_with_corrections
    Stage_B0_protocol_design: selected_and_prepared
    Stage_B0_smoke_execution_authorized: false
    selected_now: false
    status_ref: current/adaptive-explanation-stage-a-research-status.md

  MODEL_CAPABILITY_PLANNING_001:
    selected_now: false

  HO_GUIDANCE_001:
    selected_now: false

  GPT_LIVE_REALTIME_VOICE_LEARNING_SURFACE:
    selected_now: false

  LONGITUDINAL_LEARNER_MEMORY_AND_CROSS_AGENT_INTEGRATION:
    selected_now: false
```

Listing does not authorize execution or change the current conversation's selected frontier-clarification route.

## 6. Safe next action

```yaml
safe_next_action:
  current:
    - human_review_and_merge_MNEMOSYNE_195_PR_or_request_changes
  after_merge:
    - keep_A1_paused_until_Fable_quota_is_available
    - require_explicit_user_RUN_selection_before_external_execution
    - when_selected_run_one_v0_4_A1_Research_invocation
  automatic_Deep_Research: false
  automatic_Fable: false
  automatic_validation: false
```
