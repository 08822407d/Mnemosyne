# Project Research Display-Name Registry v0.1

> Non-execution-source registry for compact UI aliases used by Deep Research, Fable-class research, and equivalent one-run external work. Canonical task IDs and project truth remain elsewhere.

```yaml
registry_id: MNEMOSYNE-PROJECT-RESEARCH-DISPLAY-NAME-REGISTRY-001
created_by_task: MNEMOSYNE-189
version: 0.1.3
last_updated_by_task: MNEMOSYNE-214
status: active_after_MNEMOSYNE_189_merge
source_guard: current/external-research-display-name-guard.md
execution_source: false
owner: user
```

## 1. Project abbreviations

```yaml
projects:
  Mnemosyne:
    project_id: mnemosyne
    abbreviation: MNE
    sequence_width: 3
    allocation_owner: Mnemosyne_owner_or_authorized_Mnemosyne_task
    next_unallocated_sequence: 006

  Meta_Agent:
    project_id: meta-agent
    abbreviation: MA
    sequence_width: established_two_digit_canonical_convention
    allocation_owner: Meta_Agent_owner_route
    highest_observed_canonical_research_sequence: 15
    next_sequence: must_be_allocated_by_Meta_Agent_target_route
```

This registry records Meta-Agent's established abbreviation and observed numbering only. It does not allocate a new Meta-Agent task from the Mnemosyne maintenance route.

## 2. Issued Mnemosyne display aliases

```yaml
issued_aliases:
  - display_name: MNE-DR-001 验证包审计
    sequence: 001
    canonical_task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
    project: Mnemosyne
    status: issued_paused_not_completed
    notes:
      - alias_only_no_canonical_rename
      - R0_and_R1_use_phase_suffixes

  - display_name: MNE-DR-002 表面威胁
    sequence: 002
    canonical_task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
    project: Mnemosyne
    status: issued_deferred_not_executed
    notes:
      - alias_only_no_canonical_rename

  - display_name: MNE-DR-003 生命周期验证
    sequence: 003
    canonical_task_id: MNE-TARGET-LIFECYCLE-V1-001
    project: Mnemosyne
    status: issued_owner_authorized_execution_complete_pending_fresh_Pro
    allocation_task: MNEMOSYNE-212
    execution_package: notes/target-agent-lifecycle-v1-execution-package-001/README.md
    notes:
      - alias_only_no_canonical_rename
      - one_V1_run_with_logical_multicell_execution
      - three_conversation_operator_flow
      - use_suffixes_Execute_S8_Review
      - no_Deep_Research_or_Fable_execution_implied

  - display_name: MNE-DR-004 能力归属
    sequence: 004
    canonical_task_id: FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001
    project: Mnemosyne
    status: completed_pending_Owner_disposition
    allocation_task: MNEMOSYNE-213
    report_cycle: raw/research-reports/cycles/2026Q3-reusable-agent-capability-ownership/
    notes:
      - Fable_run_used_historical_UI_name_MNE_DR_003_能力归属
      - stored_alias_changed_only_for_navigation_after_parallel_sequence_collision
      - canonical_task_id_and_original_report_unchanged

  - display_name: MNE-DR-005 跨仓库并发
    sequence: 005
    canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
    project: Mnemosyne
    status: issued_prepared_not_selected
    allocation_task: MNEMOSYNE-214
    execution_package: handoff/fable5-ready/FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001/
    notes:
      - roadmap_F2
      - may_run_in_parallel_with_V1_fresh_Pro_review
      - V1_controller_results_remain_provisional_input
      - one_fresh_Project_one_Research_invocation
```

## 3. Historical Meta-Agent compatibility

Meta-Agent research already uses canonical IDs such as:

```text
MA-DR-08
MA-DR-09
...
MA-DR-15
```

These IDs remain unchanged. The Mnemosyne route must not reissue or renumber Meta-Agent sequences.

## 4. Allocation procedure

```yaml
allocation:
  required_inputs:
    - project_identity
    - canonical_task_id
    - short_topic
    - latest_project_registry
  checks:
    - abbreviation_exists
    - canonical_task_not_already_mapped_to_another_base_alias
    - sequence_not_previously_issued
    - short_topic_is_compact
  result:
    - update_registry_in_authorized_project_route
    - expose_display_name_in_operator_flow
```

Do not use an issue or pull-request number as the DR sequence. A prepared but not durably registered alias is vulnerable to a cross-conversation allocation race; incident `MNE-RESEARCH-DISPLAY-NAME-COLLISION-001` records the first observed case.

## 5. Migration rule

When a project moves to a dedicated repository:

1. copy this project's abbreviation and full issued-sequence history into the destination repository;
2. verify no collision;
3. designate one active allocator;
4. mark the old registry entry historical with the destination repository and cutover commit;
5. prohibit simultaneous allocation in both repositories.

## 6. Boundaries

- This registry does not authorize an external run or quota spend.
- It does not make aliases canonical research IDs.
- It does not modify Meta-Agent target truth or allocate its next task.
- It does not guarantee that a UI accepts every character in the suggested short topic.
