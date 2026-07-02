# Meta-Agent Controlled No-Target-Write Dry-Run Preparation Plan v0.1

## Positioning

- Non-execution-source pre-workspace preparation plan.
- Prepared after user approval of final manifest candidate v0.1 for dry-run preparation only.
- Does not execute the dry-run.
- Does not approve workspace creation, target material ingestion, target repository write, or operational memory-system installation.

## Current approval status

```yaml
approved_for_preparation: true
approved_for_actual_dry_run_execution_now: false
target_workspace_created: false
target_workspace_creation_approved: false
target_materials_ingested: false
target_material_ingestion_approved: false
target_repository_written: false
target_repository_write_approved: false
operational_memory_system_installation_approved: false
```

## Controlled dry-run objective

```yaml
objective:
  run_kind: controlled_no_target_write_real_target_evaluation_design_package_generation
  purpose: >
    Evaluate whether Mnemosyne can use the approved Meta-Agent pre-workspace records and non-execution-source support instruments to produce an offline Meta-Agent memory-system design/evaluation package without target workspace creation, target material ingestion, target repository write, or operational installation.
  expected_outputs:
    - offline_meta_agent_memory_system_design_package
    - authority_source_map
    - safe_input_policy
    - handoff_delivery_drafts
    - evidence_and_postmortem_artifacts
    - regression_candidates
  not_expected_outputs:
    - operational_meta_agent_memory_system
    - target_repository_write
    - production_ready_meta_agent_system
    - global_mnemosyne_execution_source_update
```

## Allowed inputs

```yaml
allowed_inputs:
  - notes/first-target-project-intake-records/meta-agent/meta-agent-target-project-selection-complete-draft.yaml
  - notes/first-target-project-intake-records/meta-agent/meta-agent-requirements-analysis-handoff-intake-alignment-package.md
  - notes/first-target-project-intake-records/meta-agent/meta-agent-first-target-draft-run-manifest-package-v0.2.md
  - notes/first-target-project-intake-records/meta-agent/meta-agent-post-v0.2-next-gate-decision-record.md
  - notes/first-target-project-intake-records/meta-agent/meta-agent-final-run-manifest-candidate-v0.1.md
  - notes/first-target-project-intake-records/meta-agent/meta-agent-final-run-manifest-candidate-review-checklist.md
  - notes/first-real-target-dry-run-evaluation-framework-v0.1.md
  - notes/first-real-target-dry-run-scorecard-v0.1.md
  - notes/first-real-target-dry-run-postmortem-template.md
  - notes/mnemosyne-regression-test-record-template.md
  - current/human-approved-spec.md for Mnemosyne process/safety boundaries only
```

## Prohibited inputs/actions

```yaml
prohibited_inputs_or_actions:
  - raw_user_originals
  - private_source
  - secrets_or_credentials
  - unredacted_personal_or_confidential_data
  - customer_or_confidential_material
  - reconstructed_lost_original_conversation_as_fact
  - target_workspace_creation
  - target_material_ingestion
  - target_repository_write
  - operational_memory_system_installation
  - Mnemosyne execution-source update
```

## Preparation completion criteria

```yaml
preparation_completion_criteria:
  - operator_prompt_package_ready
  - evidence_and_no_write_proof_plan_ready
  - current_state_records_preparation_only
  - user_must_still_approve_actual_dry_run_execution
```
