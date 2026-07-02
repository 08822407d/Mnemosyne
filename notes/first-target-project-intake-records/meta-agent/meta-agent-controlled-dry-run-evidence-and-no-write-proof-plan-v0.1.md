# Meta-Agent Controlled Dry-Run Evidence and No-Write Proof Plan v0.1

## Positioning

- Non-execution-source evidence/proof plan.
- Used only if the user later approves actual controlled dry-run execution.
- Does not execute the dry-run.

## Required evidence if later run is approved

```yaml
required_evidence:
  pre_run:
    - approved_actual_dry_run_execution_record
    - operator_no_target_write_confirmation
    - allowed_input_list
    - prohibited_input_list
    - no_workspace_creation_statement
    - no_target_material_ingestion_statement
    - no_target_repository_write_statement
  during_run:
    - action_log
    - assumption_log
    - evidence_map
    - boundary_check_log
    - prohibited_action_checkpoints
  post_run:
    - offline_delivery_package_inventory
    - scorecard_result
    - postmortem_record
    - regression_test_candidates
    - git_diff_or_equivalent_no_write_evidence
```

## No-write proof

```yaml
no_write_proof:
  required: true
  accepted_forms:
    - git_diff_or_equivalent_no_write_evidence
    - explicit statement that no target repository existed or was accessed
    - explicit statement that no target workspace was created or written
  must_cover:
    - target_repository_written: false
    - target_workspace_created: false
    - target_workspace_written: false
    - target_materials_ingested: false
```

## Failure conditions

```yaml
failure_conditions:
  - no_write_proof_missing
  - target_repository_write_detected
  - target_workspace_created_without_approval
  - target_material_ingested_without_approval
  - operational_memory_system_installation_claimed
  - synthetic_or_draft_evidence_reported_as_production_ready
```
