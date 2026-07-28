# First-Target Minimum Upgrade Contract Status

> Non-execution-source live candidate status. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
status_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-STATUS-001
created_by_task: MNEMOSYNE-166
candidate_id: FIRST-TARGET-MINIMUM-UPGRADE-CONTRACT-001
candidate_path: notes/first-target-minimum-upgrade-contract-v0.1.md
source_research_cycle: RC-2026Q3-target-memory-governance-and-learning
status: candidate_prepared_pending_user_disposition
execution_source: current/human-approved-spec.md
execution_source_modified: false
formal_target_project_selected: false
implementation_authorized: false
```

## User route selection

The user instructed the current conversation to continue according to the maintainer-recommended route after the four-topic research batch. The highest-ranked near-term route in the merged decision-preparation package was:

```yaml
selected_route:
  id: FIRST_TARGET_MINIMUM_UPGRADE_CONTRACT
  objective: prepare_a_candidate_minimum_upgrade_contract_for_user_review
  selection_ref: current_conversation_user_instruction_2026-07-28
  selection_scope: candidate_preparation_only
```

This selection does not mean that the candidate is accepted, that the target-project template pack is changed, or that a target project has been selected.

## Candidate scope

The candidate addresses the user's requirement that Mnemosyne can be used before it is nearly perfect without locking early target-Agent memory systems to the current templates, models, storage implementation or derived artifacts.

It proposes a bounded minimum covering:

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

It explicitly does **not** make the following universal:

- full event-sourced runtime;
- dual-write;
- shadow cutover;
- bitemporal storage;
- automated migration service;
- a six-layer memory architecture.

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

The candidate fills in the missing minimum contract and migration semantics. MNEMOSYNE-166 does not edit the template pack. A later accepted disposition may authorize a small template patch or defer all template changes until the first real target-project pilot.

## Required user disposition

After the candidate is published and reviewed, select exactly one:

```yaml
user_disposition_options:
  ACCEPT_FOR_FIRST_TARGET_DESIGN_PROCESS:
    meaning: use_the_candidate_as_a_required_but_target_tailorable_part_of_the_first_real_target_design_process
    next_action: prepare_a_bounded_template_or_first_target_integration_spec

  ACCEPT_AS_ADVISORY_PILOT_ONLY:
    meaning: keep_the_candidate_non_mandatory_and_test_it_during_the_first_target_project_before_any_global_template_promotion
    next_action: preserve_candidate_and_include_it_in_first_target_review_checklist_only

  ACCEPT_WITH_MODIFICATIONS:
    meaning: revise_named_fields_scope_or_mandatory_vs_conditional_boundaries
    required_input: explicit_modifications

  DEFER:
    meaning: preserve_the_candidate_without_using_it_in_the_next_target_project_yet

  REJECT:
    meaning: do_not_use_this_candidate_as_the_upgrade_contract_baseline
```

No option is selected by this status record.

## Acceptance questions

The later user review should focus on:

1. Is the contract small enough for a temporary or low-risk Agent?
2. Which fields must apply to all first-target designs, and which should apply only to long-lived or high-risk targets?
3. Should the target-project template pack be updated before the first target, or should the candidate be tested as a separate pilot instrument first?
4. What migration rehearsal is proportionate for the first target?
5. Does the contract remain executable by the intended next-tier model for bounded implementation work, with frontier escalation only where needed?

## Boundaries

- No target project, workspace, material or repository is selected or modified.
- No target runtime truth source is created.
- No execution-source or template-pack change is authorized.
- No research TODO or open question is closed.
- No automatic migration, writeback or model routing is authorized.
- The non-FABLE health review and all other conversation-owned routes remain separate.

## Safe next action

```yaml
safe_next_action:
  - publish_and_human_review_the_single_MNEMOSYNE_166_PR
  - then_record_one_explicit_user_disposition_for_the_candidate
  - create_a_fresh_task_for_any_accepted_template_or_first_target_integration_work
```
