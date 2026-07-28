# Meta-Agent v0.1 M0 — Requirements and Authority Baseline

> Target-specific, non-execution-source build-start baseline. It becomes the accepted M0 input for Meta-Agent v0.1 construction only if the canonical MNEMOSYNE-170 PR is human-merged. It does not itself create the target workspace or become the Meta-Agent runtime truth source.

```yaml
baseline_id: META-AGENT-V0.1-M0-REQUIREMENTS-AUTHORITY-BASELINE-001
created_by_task: MNEMOSYNE-170
target_project_id: meta-agent
target_project_name: Meta-Agent
route: META_AGENT_PRODUCT_BUILD_LAUNCH_PREPARATION
status: proposed_for_acceptance_by_merging_the_canonical_MNEMOSYNE_170_PR
effective_on_merge: true
M0_complete_on_merge: true
execution_source: current/human-approved-spec.md
execution_source_modified: false
target_workspace_created: false
target_files_created: false
operational_build_started: false
```

## 1. User route selection

The user explicitly selected:

```text
META_AGENT_PRODUCT_BUILD_LAUNCH_PREPARATION
```

with the required order:

```text
complete M0 and M1
  -> only then begin v0.1 target-file construction
```

This supersedes the former `Meta_Agent_product_build_selected: false` field only for the new product-build route. It does not reopen or alter the completed historical Meta-Agent behavioral-test route and does not take ownership of the separately assigned non-FABLE health-review route.

```yaml
route_selection:
  Meta_Agent_product_build_selected: true
  selected_scope_now:
    - M0_requirements_and_authority_closure
    - M1_workspace_safety_manifest_and_upgrade_profile
  target_file_construction_in_this_task: prohibited
  M2_after_M0_M1_merge: requires_fresh_task_local_authorization
```

## 2. Target identity

```yaml
target_identity:
  target_project_id: meta-agent
  target_project_name: Meta-Agent
  target_project_type:
    primary: ai_agent_project
    secondary:
      - long_term_research
      - agent_design_methodology
      - software_development_methodology
      - external_memory_system_design
  classification: general_purpose_with_software_engineering_heavy_incubation
  owner: user
  final_decision_authority: user
  intended_lifespan: long_lived_and_versioned
  initial_implementation_style: file_based_human_reviewed_v0_1
```

Meta-Agent is a general-purpose upper-level Agent-design and methodology system. Software engineering is the dominant early incubation domain because it offers frequent use, rich engineering practice and observable artifacts, but it does not define the full scope of Meta-Agent.

## 3. Confirmed v0.1 requirements

Each requirement has a stable target-specific identity. Later target files must preserve these IDs or record an explicit mapping.

```yaml
confirmed_requirements:
  - id: MA-REQ-0001
    requirement: Meta-Agent designs AI Agents, workflows and supporting methodology for concrete user goals.
  - id: MA-REQ-0002
    requirement: Meta-Agent may design one specialized Agent or a multi-Agent/team arrangement; multi-Agent is not the default.
  - id: MA-REQ-0003
    requirement: Meta-Agent remains general-purpose while using software engineering as a heavy early incubation domain.
  - id: MA-REQ-0004
    requirement: Designs may include roles, workflows, memory structures, handoff rules, model/tool routing, evaluation and human-decision boundaries.
  - id: MA-REQ-0005
    requirement: The system should reduce repetitive work without removing the user's valuable learning, architecture, engineering, performance, management or high-risk judgment opportunities.
  - id: MA-REQ-0006
    requirement: Project feedback cannot automatically rewrite general methodology; it must pass through review, abstraction, candidate improvement, user confirmation and an approved update.
  - id: MA-REQ-0007
    requirement: General methodology, target-specific cases, research evidence, current state, raw/source evidence, candidate ideas and approved target truth must remain distinguishable.
  - id: MA-REQ-0008
    requirement: v0.1 is file-based and human-reviewed; no RAG, MCP, auto-indexing, auto-writeback, autonomous self-modification or multi-Agent runtime coordination is assumed.
  - id: MA-REQ-0009
    requirement: The bootstrap public repository stores only public, synthetic, explicitly redacted or safe-pointer material; private originals remain outside Git unless separately approved.
  - id: MA-REQ-0010
    requirement: The first version must include stable identity, compact versions, migration mapping, validation and rollback so later Mnemosyne/model/tool improvements can be applied without rebuilding from scratch.
  - id: MA-REQ-0011
    requirement: Work must be split by capability demand; bounded routine execution should be usable by a validated next-tier model, while novel, ambiguous, authority-changing or high-impact work escalates to a frontier model and human decision.
  - id: MA-REQ-0012
    requirement: Project cases may inform methodology only as scoped evidence; target-specific lessons must not silently become global methods.
  - id: MA-REQ-0013
    requirement: The user is owner and final authority for product purpose, target truth, methodology promotion, privacy, repository/write scope and operational acceptance.
  - id: MA-REQ-0014
    requirement: Meta-Agent has exactly one declared runtime truth source; Mnemosyne remains design archive/control plane and is not a second runtime truth source.
  - id: MA-REQ-0015
    requirement: A fresh qualified session must be able to resume from the target truth source, current context and handoff without hidden prior-conversation assumptions.
  - id: MA-REQ-0016
    requirement: Important methodology changes require evidence, acceptance criteria, issue/postmortem records where relevant and regression or semantic review proportionate to impact.
```

## 4. v0.1 non-goals

```yaml
non_goals:
  - production_grade_autonomous_Meta_Agent_runtime
  - automatic_methodology_rewrite
  - automatic_cross_project_or_cross_Agent_memory_sharing
  - persistent_global_user_or_cognitive_profile
  - learner_state_or_GPT_Live_module_implementation
  - universal_HO_GUIDANCE_policy
  - full_event_sourcing_dual_write_shadow_cutover_or_bitemporal_storage
  - storing_secrets_credentials_private_source_customer_or_confidential_material_in_public_Git
  - reconstructing_the_lost_original_Meta_Agent_conversation_as_fact
  - making_research_reports_or_Mnemosyne_current_files_target_runtime_truth
  - fixing_or_closing_every_Mnemosyne_TODO_before_start
```

## 5. Pending requirements

Pending items are real design questions but do not block the bounded file-based v0.1 unless the M1 manifest marks one as required.

```yaml
pending_requirements:
  - id: MA-PEND-0001
    topic: exact_long_term_product_surface
    candidates:
      - ChatGPT_Project_or_custom_configuration
      - dedicated_repository_and_manual_workflow
      - local_CLI_or_agent_framework
      - hybrid
  - id: MA-PEND-0002
    topic: dedicated_external_Meta_Agent_repository_after_bootstrap
  - id: MA-PEND-0003
    topic: detailed_single_Agent_vs_multi_Agent_routing_thresholds
  - id: MA-PEND-0004
    topic: mature_evaluation_rubrics_and_automated_regression_tooling
  - id: MA-PEND-0005
    topic: private_target_material_store_and_access_method
  - id: MA-PEND-0006
    topic: advanced_model_provider_tool_routing_matrix
  - id: MA-PEND-0007
    topic: learner_adaptive_explanation_GPT_Live_and_cross_Agent_shared_memory_modules
  - id: MA-PEND-0008
    topic: automation_RAG_MCP_indexing_and_writeback
```

## 6. Unknowns and unsupported assumptions

```yaml
unknowns:
  - exact_operational_UI_or_framework
  - exact_future_private_storage_location
  - expected_case_volume_and_update_frequency_after_real_use
  - future_provider_and_platform_capabilities
  - whether_a_dedicated_repository_will_be_preferred_after_v0_1
  - final_cost_latency_and_review_tolerance

unsupported_assumptions:
  - Meta_Agent_already_has_an_operational_memory_system
  - the_bootstrap_workspace_already_exists
  - current_Deep_Research_or_model_capability_claims_are_permanent
  - multi_Agent_is_always_better
  - all_future_work_will_use_frontier_models
  - target_project_files_can_contain_private_user_material_because_the_user_is_owner
  - a_newer_summary_or_model_inference_is_more_authoritative
  - a_path_becomes_runtime_truth_merely_because_it_is_created
```

## 7. Owner and runtime-truth rule

The M0 recommended bootstrap authority arrangement is selected for acceptance through this PR:

```yaml
target_authority:
  owner: user
  bootstrap_workspace_root: target-projects/meta-agent/
  runtime_truth_source:
    path: target-projects/meta-agent/current/approved-spec.md
    role: sole_Meta_Agent_v0_1_runtime_truth_source
    exists_now: false
    creation_authorized_in_MNEMOSYNE_170: false
  Mnemosyne_role:
    repository: 08822407d/Mnemosyne
    role: design_archive_control_plane_and_bootstrap_host
    current_human_approved_spec_scope: Mnemosyne_process_and_safety_only
    target_runtime_truth: false
  non_execution_sources:
    - target-projects/meta-agent/current/active-context.md
    - target-projects/meta-agent/authority/source-and-owner-map.md
    - target-projects/meta-agent/methodology/core-methodology.md
    - target-projects/meta-agent/cases/case-and-feedback-ledger.md
    - target-projects/meta-agent/history/decision-version-and-migration-log.md
    - target-projects/meta-agent/handoff/handoff-current.md
```

The bootstrap target workspace and its single runtime-truth file may later migrate to a dedicated repository. Such a move requires an explicit migration manifest, old-to-new mapping, owner decision, validation and rollback plan. The old path becomes historical/non-current after successful migration and must not remain a competing truth source.

## 8. Conflict precedence and update rule

```yaml
conflict_precedence:
  - current_explicit_user_Meta_Agent_decision
  - target-projects/meta-agent/current/approved-spec.md_after_creation
  - user_approved_target_build_or_change_manifest_within_its_exact_scope
  - user_approved_target_decision_records
  - current_context_and_handoff_for_operational_navigation_only
  - reviewed_evidence_and_research
  - model_inference_marked_as_inference

update_rule:
  target_truth_update_requires:
    - explicit_target_scoped_user_authorization
    - identified_change_scope
    - source_and_authority_review
    - version_change_or_recorded_no_version_change_rationale
    - validation_and_rollback_or_revision_plan
  silent_promotion_prohibited: true
  target_specific_feedback_to_general_methodology_requires:
    - feedback_record
    - abstraction_review
    - candidate_improvement
    - user_confirmation
    - approved_methodology_update
```

## 9. M0 acceptance criteria

M0 is complete when the canonical PR containing this file is human-merged and all of the following are true:

```yaml
M0_acceptance:
  product_build_route_selected: true
  v0_1_identity_and_purpose_bounded: true
  confirmed_pending_unknown_unsupported_split_present: true
  owner_rule_explicit: true
  sole_future_runtime_truth_source_path_explicit: true
  Mnemosyne_second_truth_source_prohibited: true
  initial_non_goals_and_deferred_items_explicit: true
  target_files_created_before_M1_completion: false
```

## 10. Boundary

- This file is not the Meta-Agent runtime truth source.
- It does not create `target-projects/meta-agent/` or any target file.
- It does not authorize material ingestion, target repository access, operational installation or automated execution.
- It does not close pending requirements or claim that v0.1 is production-ready.
- It does not take over the non-FABLE health-review route.
- Any target write requires M1 acceptance plus a fresh M2 task-local authorization.
