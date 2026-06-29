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
target_project_workspace:
  workspace_root:
  workspace_status: not_created | approved_to_create | created | not_applicable
  workspace_creation_approved:
  workspace_is_mnemosyne_execution_source: false
  workspace_is_target_runtime_truth_source: false | target_manifest_approved | unknown
  project_meta_path:
  user_input_path:
  mnemosyne_design_workbench_path:
  delivery_package_path:
  dry_run_path:
  feedback_and_lessons_path:
user_input_storage_policy:
  originals_storage: not_provided | in_workspace_safe_public_or_redacted | external_reference_only | unsafe_do_not_store | pending_user_decision
  restatements_path:
  decisions_path:
  redactions_path:
  external_pointer_or_redacted_reference:
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
- A real target-project dry-run manifest must identify `target_project_workspace.workspace_root` or explicitly justify `workspace_status: not_applicable`.
- Workspace creation is not authorized unless the user approves the target, authority/source map, safety/privacy boundary, no-target-write boundary, and run manifest.
- The target workspace is not Mnemosyne execution source.
- The target workspace is not automatically the target runtime truth source; it can hold that role only if a target manifest / owner rule explicitly and user-approvedly says so.
- User originals and raw requirements may be stored only under an approved repository visibility and safety policy; otherwise record only an external pointer or redacted reference.
- After target workspace approval, dry-run outputs should be target-scoped under `target-projects/<target_project_id>/04-dry-runs/<dry_run_id>/` instead of global notes, unless the user approves an exception.
- Do not create `notes/target-project-dry-runs/<dry_run_id>/`, `target-projects/<target_project_id>/04-dry-runs/<dry_run_id>/`, or any target workspace merely because this template exists.

## MNEMOSYNE-058 approval/status hardening

```yaml
approval_record:
  target_selected:
    status: true | false | unknown
    approved_by:
    approved_at:
  target_workspace_root:
    status: approved | rejected | pending | not_applicable
    path:
    approved_by:
    approved_at:
  workspace_creation:
    status: approved | not_approved | pending | not_applicable
    approved_by:
    approved_at:
  user_input_storage_policy:
    status: approved | rejected | pending
    approved_by:
    approved_at:
  no_target_write:
    status: confirmed | not_confirmed | contradicted
    approved_by:
    approved_at:
  run_manifest:
    status: user_approved | draft | invalid
    approved_by:
    approved_at:
target_runtime_truth_source:
  status: none | external_owner_rule_confirmed | workspace_manifest_user_approved | unknown_requires_owner_decision
  authority_path_or_external_pointer:
  approved_by:
  approved_at:
  scope:
  limitations:
target_material_ingestion:
  status: none_provided | approved_to_ingest | ingested | unsafe_blocked | pending_user_decision
  allowed_material_types:
  prohibited_material_types:
redaction_and_external_pointer:
  redaction_manifest_path:
  external_source_pointer_path:
  git_history_exposure_acknowledged:
```

Rules:

- Blank safety-critical approval fields are not approval.
- `not_confirmed`, `pending`, `unknown`, or blank on no-target-write / workspace creation / user-input storage policy blocks real dry-run.
- If first-dry-run support instruments conflict, follow: (1) `current/human-approved-spec.md`; (2) the user-approved actual run manifest; (3) onboarding/manifest templates; and record the conflict instead of merging instructions.
