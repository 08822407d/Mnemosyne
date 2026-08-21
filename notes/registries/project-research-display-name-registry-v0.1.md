# Project Research Display-Name Registry v0.1

> Non-execution-source registry for compact UI aliases used by Deep Research, Fable-class research, and equivalent one-run external work. Canonical task IDs and project truth remain elsewhere.

```yaml
registry_id: MNEMOSYNE-PROJECT-RESEARCH-DISPLAY-NAME-REGISTRY-001
created_by_task: MNEMOSYNE-189
version: 0.1.4
last_updated_by_task: MNEMOSYNE-240
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
    next_unallocated_sequence: 007
  Meta_Agent:
    project_id: meta-agent
    abbreviation: MA
    sequence_width: established_two_digit_canonical_convention
    allocation_owner: Meta_Agent_owner_route
    highest_observed_canonical_research_sequence: 15
    next_sequence: must_be_allocated_by_Meta_Agent_target_route
```

## 2. Issued Mnemosyne display aliases

```yaml
issued_aliases:
  - display_name: MNE-DR-001 验证包审计
    sequence: 001
    canonical_task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
    project: Mnemosyne
    status: issued_paused_not_completed
    notes: [alias_only_no_canonical_rename, R0_and_R1_use_phase_suffixes]
  - display_name: MNE-DR-002 表面威胁
    sequence: 002
    canonical_task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
    project: Mnemosyne
    status: issued_deferred_not_executed
    notes: [alias_only_no_canonical_rename]
  - display_name: MNE-DR-003 生命周期验证
    sequence: 003
    canonical_task_id: MNE-TARGET-LIFECYCLE-V1-001
    project: Mnemosyne
    status: issued_owner_authorized_execution_complete_pending_fresh_Pro
    allocation_task: MNEMOSYNE-212
    execution_package: notes/target-agent-lifecycle-v1-execution-package-001/README.md
    notes: [alias_only_no_canonical_rename, one_V1_run_with_logical_multicell_execution, three_conversation_operator_flow, use_suffixes_Execute_S8_Review, no_Deep_Research_or_Fable_execution_implied]
  - display_name: MNE-DR-004 能力归属
    sequence: 004
    canonical_task_id: FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001
    project: Mnemosyne
    status: completed_pending_Owner_disposition
    allocation_task: MNEMOSYNE-213
    report_cycle: raw/research-reports/cycles/2026Q3-reusable-agent-capability-ownership/
    notes: [Fable_run_used_historical_UI_name_MNE_DR_003_能力归属, stored_alias_changed_only_for_navigation_after_parallel_sequence_collision, canonical_task_id_and_original_report_unchanged]
  - display_name: MNE-DR-005 跨仓库并发
    sequence: 005
    canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
    project: Mnemosyne
    status: A1_readiness_pass_corrected_G2A_template_publication_pending
    allocation_task: MNEMOSYNE-214
    execution_package: handoff/fable5-ready/FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001/
    notes: [roadmap_F2, A0_complete, A1_not_authorized, G2A_not_issued]
  - display_name: MNE-DR-006 交接加固
    sequence: 006
    canonical_task_id: FABLE5-MNE-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-001
    project: Mnemosyne
    status: repository_audit_and_HVAL_design_audit_complete_Pro_adjudicated
    allocation_task: MNEMOSYNE-240_durable_registration_after_235_236_237_238_239_blocked
    report_source_roots:
      - raw/validation-reviews/MNE-DR-006-handoff-protocol-repository-audit-001/
      - raw/validation-reviews/MNE-DR-006-HVAL001-preexecution-design-audit-001/
    notes:
      - Fable_5_Work_Ultra_Research_OFF
      - repository_only_public_evidence_audit
      - HVAL_design_002_accepted_for_separate_Owner_authorization
      - cross_route_god_view_claims_remain_blocked
```

## 3. Historical Meta-Agent compatibility

Meta-Agent canonical IDs such as `MA-DR-08` through `MA-DR-15` remain unchanged. Mnemosyne does not allocate a Meta-Agent sequence.

## 4. Allocation procedure

```yaml
allocation:
  required_inputs: [project_identity, canonical_task_id, short_topic, latest_project_registry]
  checks: [abbreviation_exists, canonical_task_not_already_mapped, sequence_not_previously_issued, short_topic_is_compact]
  result: [update_registry_in_authorized_project_route, expose_display_name_in_operator_flow]
```

Prepared but unregistered aliases remain vulnerable to cross-conversation races. Issue/PR numbers are never DR sequences.

## 5. Migration rule

On repository migration: copy the full issued history, verify collisions, designate one allocator, mark the old registry historical, and prohibit simultaneous allocation.

## 6. Boundaries

- This registry does not authorize external runs or quota.
- Aliases are not canonical task IDs.
- It does not modify Meta-Agent target truth.
- It does not guarantee UI character support.
