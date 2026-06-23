# First Target-Project Dry-Run Manifest Template

## Positioning

- Positioning: non-execution-source run-input/control template.
- This template is not execution source.
- This template is not target-project delivery.
- This template does not authorize target writes.
- This template does not prove a real dry-run occurred.

## Required run manifest fields

```yaml
run_manifest_version:
dry_run_id:
run_kind: real_target_project | synthetic_smoke_test
manifest_status: draft | user_approved | invalid
target_project_name:
target_project_type:
owner_or_decision_authority:
bounded_scope:
current_stage:
project_goal:
memory_problem_to_solve:
target_execution_source_or_owner_rule:
target_execution_source_status: confirmed | unknown_requires_owner_decision | not_applicable
source_items:
  - path_or_link:
    role:
    authority:
    owner:
    date_or_version:
    sensitivity:
    allowed_use:
    accessible_to_executor:
current_task_or_milestone:
recent_user_or_owner_decision:
known_stale_or_superseded_item:
challenge_case:
  type: real_conflict | test_fixture_not_target_truth
  description:
privacy_and_repository_boundary:
current_repository_visibility:
input_safety_status: public | synthetic | explicitly_redacted | separately_approved_non_public | unsafe
no_target_write_confirmed:
target_materials_uploaded_or_ingested:
expected_dry_run_outputs:
user_verification_method:
unsupported_assumptions:
user_approvals:
  target_selected:
  authority_confirmed:
  source_use_approved:
  privacy_boundary_approved:
  no_target_write_approved:
stop_conditions_triggered:
```

## Rules

- `real_target_project` requires a real, user-verifiable target.
- `synthetic_smoke_test` must never be reported as a real dry-run.
- `manifest_status: user_approved` is required before a real target-project dry-run.
- Any unsafe or ambiguous material stops the run.
- The manifest must record unsupported assumptions instead of allowing the executor to invent missing target facts.
- The manifest must confirm `no_target_write_confirmed` before any real dry-run begins.
- Do not create `notes/target-project-dry-runs/<dry_run_id>/` merely because this template exists.
