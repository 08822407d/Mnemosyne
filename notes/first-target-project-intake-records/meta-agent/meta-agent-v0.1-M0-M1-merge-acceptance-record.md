# Meta-Agent v0.1 M0/M1 Merge-Acceptance Record

> Non-execution-source target decision record. The decisions below become accepted M0/M1 build-start inputs when the canonical MNEMOSYNE-170 PR is human-merged. They do not create the target runtime files or authorize operational use.

```yaml
decision_record_id: MA-DEC-0001
created_by_task: MNEMOSYNE-170
target_project_id: meta-agent
decision_status: pending_human_merge_acceptance
effective_event: merge_of_the_single_canonical_MNEMOSYNE_170_PR
source_user_instruction: current_conversation_user_message_after_PR_220_merge
execution_source: current/human-approved-spec.md
execution_source_modified: false
```

## Accepted on merge

```yaml
decisions:
  product_build_route:
    value: META_AGENT_PRODUCT_BUILD_LAUNCH_PREPARATION
    status: selected

  build_order:
    value:
      - complete_M0
      - complete_M1
      - then_start_M2_v0_1_target_file_construction

  M0_baseline:
    ref: notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M0-requirements-and-authority-baseline.md
    accepted_on_merge: true

  owner:
    value: user

  bootstrap_workspace:
    value: target-projects/meta-agent/
    role: bootstrap_target_workspace_and_initial_file_based_runtime_store

  sole_target_runtime_truth_source:
    value: target-projects/meta-agent/current/approved-spec.md
    exists_before_M2: false

  Mnemosyne_role:
    value: design_archive_control_plane_and_bootstrap_host_not_second_target_runtime_truth

  repository_visibility_treatment:
    value: public_risk

  safe_input_default:
    value: public_synthetic_explicitly_redacted_safe_pointer_or_outside_git

  M1_manifest:
    ref: notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M1-workspace-safety-build-manifest.md
    accepted_on_merge: true

  exact_M2_substantive_target_scope:
    file_count: 7
    extra_target_paths_without_new_authorization: prohibited

  upgrade_contract:
    contract_id: META-AGENT-V0.1-UPGRADE-CONTRACT-001
    profile: standard
    global_mandate: false
    event_sourcing_or_service_architecture_required: false

  model_capability_policy:
    value: frontier_reasoning_for_ambiguous_high_impact_or_authority_work_next_tier_for_frozen_bounded_execution_mechanical_tools_for_exact_checks_human_for_acceptance
    named_model_mapping: intentionally_not_fixed

  health_review_boundary:
    canonical_result_found_on_base: false
    route_owner: separate_conversation
    M0_M1_blocked: false
    M2_bootstrap_blocked: false_unless_applicable_high_severity_finding_appears
    operational_use_requires_later_check_or_explicit_deferral: true

  M2_authorization:
    status: not_granted_by_this_record
    requirement: fresh_task_local_user_authorization_after_M0_M1_merge
```

## Rationale

This decision set chooses the smallest practical start that still protects future migration:

- a single target truth file prevents duplicate authority;
- a seven-file target scope avoids copying Mnemosyne's full directory structure;
- stable IDs and version fields begin before target history accumulates;
- public-safe storage avoids importing private materials into the public repository;
- the standard upgrade profile supports a long-lived methodology target without requiring event sourcing, dual-write, RAG or automated services;
- the capability split preserves frontier-model quota by delegating frozen, bounded implementation while escalating ambiguity and authority changes;
- the other conversation's health review remains separate and cannot be silently ignored before operational use.

## Supersession and mapping

When M2 creates the target decision/version log, this record must be mapped as follows:

```yaml
future_mapping:
  old_id: MA-DEC-0001
  new_id_or_ids:
    - MA-DEC-0001
  relation: unchanged_or_moved
  source_refs_preserved: true
  authority_changed: false
```

If the target workspace later moves to another repository, this record remains historical evidence and the target decision ID must retain an explicit migration mapping.

## Boundary

- Human merge accepts the M0/M1 defaults, not the M2 implementation output.
- No target path is created by this record.
- No private material, target repository write outside the future seven-file scope, operational installation or automatic migration is approved.
- Later changes to workspace, truth source, owner, privacy or trust boundary require a new explicit user decision.
