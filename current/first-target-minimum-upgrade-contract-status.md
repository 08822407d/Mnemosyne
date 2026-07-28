# First-Target Minimum Upgrade Contract Status

> Non-execution-source live candidate status. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
status_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-STATUS-002
created_by_task: MNEMOSYNE-166
last_status_task: MNEMOSYNE-167
candidate_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-001
candidate_path: notes/first-target-minimum-upgrade-contract-v0.1.md
advisory_pilot_checklist: notes/first-target-minimum-upgrade-contract-advisory-pilot-checklist-v0.1.md
source_research_cycle: RC-2026Q3-target-memory-governance-and-learning
status: accepted_as_advisory_pilot_only
disposition: ACCEPT_AS_ADVISORY_PILOT_ONLY
execution_source: current/human-approved-spec.md
execution_source_modified: false
formal_target_project_selected: false
template_pack_modified: false
implementation_authorized: false
```

## User route selection and disposition

The user instructed the current conversation to continue according to the maintainer-recommended route after the four-topic research batch. The highest-ranked near-term route was `FIRST_TARGET_MINIMUM_UPGRADE_CONTRACT`, and MNEMOSYNE-166 prepared the candidate for review.

After PR #217 merged, the user again instructed the conversation to verify the merge and continue the planned work. The immediately preceding maintainer recommendation was to adopt the candidate as an advisory pilot rather than a mandatory global rule. This task records that bounded disposition.

```yaml
selected_route:
  id: FIRST_TARGET_MINIMUM_UPGRADE_CONTRACT
  objective: test_a_target_tailorable_upgrade_contract_during_the_first_real_target_design
  original_selection_ref: current_conversation_user_instruction_2026-07-28_continue_recommended_route

disposition:
  value: ACCEPT_AS_ADVISORY_PILOT_ONLY
  recorded_by_task: MNEMOSYNE-167
  decision_ref: current_conversation_user_instruction_after_PR_217_merge
  interpretation_basis:
    - user_requested_continuation_of_the_previously_planned_work
    - immediately_preceding_recommendation_was_ACCEPT_AS_ADVISORY_PILOT_ONLY
    - prior_user_preference_was_advisory_pilot_not_global_mandate
  scope:
    - preserve_the_candidate
    - include_it_in_a_first_target_review_checklist
    - evaluate_value_and_burden_in_the_first_real_target_design
  excludes:
    - global_template_mandate
    - execution_source_change
    - target_project_selection
    - target_write
    - automatic_migration
    - automatic_promotion_after_pilot
```

## Effect of the disposition

The candidate is accepted only as a testable review instrument for the first real target-project design.

```yaml
advisory_pilot_effect:
  use_during_first_real_target_design: yes_after_explicit_target_and_run_manifest
  mandatory_for_all_targets: false
  target_tailoring_required: true
  target_owner_may_simplify_or_mark_not_applicable_with_rationale: true
  pilot_result_may_inform_later_candidate_revision: true
  global_promotion_requires_fresh_user_decision_and_repository_task: true
```

A first-target pilot may use the candidate to check stable identities, source and authority boundaries, versions, migration mapping, validation, rollback and rebuildable derived views. It must also measure whether those controls create excessive burden for a small or temporary Agent.

## Candidate scope retained

The candidate covers:

- stable identity for authority-bearing objects;
- source references and object lineage;
- design, schema, policy and delivery versions;
- preserved raw evidence and approved authority;
- migration manifests and explicit old-to-new mappings;
- preserve/transform/recompute/retire decisions;
- validation and acceptance criteria;
- previous-state and rollback references;
- rebuildable derived views where practical;
- target-specific escalation by change class.

It does **not** make the following universal:

- full event-sourced runtime;
- dual-write;
- shadow cutover;
- bitemporal storage;
- automated migration service;
- a six-layer memory architecture.

## Checklist relationship

The advisory implementation surface is limited to:

```text
notes/first-target-minimum-upgrade-contract-advisory-pilot-checklist-v0.1.md
```

The checklist:

- activates only after a target project and run manifest are explicitly approved;
- is non-blocking for the target design by default;
- may be made target-locally blocking only by an explicit approved run manifest;
- allows `minimal`, `standard`, `enhanced` or `not_applicable_with_rationale` profiles;
- tests next-tier model executability and frontier-escalation points;
- records burden and value before any global promotion decision.

## Existing-template relationship

The current target-project template pack already contains adjacent hooks:

```yaml
existing_fields:
  intake:
    - migration_requirement
  design_spec:
    - design_version
    - model_migration_policy
    - drift_review_policy
  execution_source_rule:
    - versioning_rule
  delivery:
    - rollback_or_revision_plan
```

MNEMOSYNE-167 does not modify that template pack. The advisory pilot remains a separate review instrument until a real target-project pilot produces evidence and the user later decides whether any small template patch is justified.

## Pilot result options

```yaml
pilot_result_options:
  PASS_FOR_TARGET_SPECIFIC_USE:
    meaning: useful_and_proportionate_for_this_target_only
  PASS_WITH_SIMPLIFICATION:
    meaning: useful_after_reducing_fields_or_gates
  REVISE_CONTRACT:
    meaning: candidate_structure_requires_revision
  DEFER_UNTIL_REAL_MIGRATION_EVIDENCE:
    meaning: design_only_evidence_is_insufficient
  REJECT_AS_TOO_BURDENSOME:
    meaning: process_cost_exceeds_demonstrated_value_for_this_target
```

No pilot result automatically changes Mnemosyne or target-project execution sources.

## Boundaries

- No target project, workspace, material or repository is selected or modified.
- No target runtime truth source is created.
- No execution-source or target-project template-pack change is authorized.
- No research TODO or open question is closed.
- No automatic migration, writeback, model routing, cross-Agent sharing or learner profiling is authorized.
- The non-FABLE health review and all other conversation-owned routes remain separate.
- The four original Deep Research conversations may be archived in the product UI but are not recommended for permanent deletion yet.

## Safe next action

```yaml
safe_next_action:
  current_task:
    - publish_and_human_review_the_single_MNEMOSYNE_167_PR
  after_merge:
    - verify_latest_master_contains_the_disposition_and_advisory_checklist
    - continue_the_maintainer_recommended_sequence_with_a_fresh_bounded_task
  planned_follow_on_route:
    id: LEARNER_STATE_AND_ADAPTIVE_EXPLANATION_SYNTHESIS
    reason: next_ranked_research_route_and_MNEMOSYNE_164_requires_fresh_high_reasoning_reanalysis_before_prompt_generation
    automatic_target_or_research_execution: false
```
