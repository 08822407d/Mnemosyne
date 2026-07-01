# First Target Project Intake and Approval Forms v0.1

## Positioning

This file is a non-execution-source support instrument derived from PRO-04 v2. It supports first target selection and approval intake only. It does not select a target, create a workspace, ingest materials, start a real dry-run, or authorize target repository write. At first contact, do not ask the user to upload raw materials immediately.

## One-page user intake form

```yaml
target_project_selection:
  target_project_name:
  target_project_id_candidate:
  target_project_type:
  owner_or_decision_authority:
  why_this_target_first:
  expected_value_of_dry_run:
  known_non_goals:
  raw_material_upload_now: no
```

## Authority/source map form

```yaml
authority_source_map:
  user_decision_authority:
  target_owner:
  allowed_sources:
  forbidden_sources:
  source_priority_order:
  target_runtime_truth_source: none_declared_yet | declared_below
  conflict_resolution_rule:
  approval_status: pending
```

## Safe input / user originals storage policy form

```yaml
safe_input_policy:
  repository_visibility_checked:
  permitted_material_categories:
    - public_project_description
    - synthetic_substitute
    - explicitly_redacted_excerpt
    - external_pointer_only
  user_originals_storage_default: outside_git_pointer_only
  store_raw_originals_in_repo: no
  retention_note:
  approval_status: pending
```

## Redaction manifest and external pointer forms

```yaml
redaction_manifest:
  redacted_artifact_id:
  source_original_pointer:
  redaction_method:
  removed_sensitive_categories:
  residual_risk:
  approved_for_repo_visibility:
external_pointer:
  pointer_id:
  location_description:
  access_requirements:
  contains_sensitive_material:
  pointer_safe_for_repo_visibility:
```

## Manual-import artifact classification form

```yaml
manual_import_artifact_classification:
  artifact_id:
  filename:
  artifact_type:
  full_body_present:
  required_sections_present:
  download_link_only:
  safety_preflight:
    repository_visibility:
    safe_for_repo_visibility:
    contains_secrets_or_credentials:
    contains_personal_or_confidential_data:
    contains_private_source_or_customer_confidential_data:
    contains_target_materials:
  canonical_destination:
  decision:
  rationale:
```

## No-target-write confirmation

```yaml
no_target_write_confirmation:
  target_repository_write_allowed: false
  target_workspace_write_allowed: false_until_explicit_approval
  operator_confirmed:
  user_confirmed:
  proof_required_after_run: git_diff_or_equivalent_no_write_evidence
```

## Approval conflict resolution checklist

- Identify conflicting approvals or source claims.
- Prefer current user/owner approval over stale notes.
- Do not invent authority when missing.
- Record unresolved conflicts in the run manifest.
- Stop if conflict affects write permission, material safety, or truth-source priority.

## Run manifest approval checklist

- Target selected.
- Workspace root or exception approved.
- Authority/source map approved.
- Safe input and user-originals policy approved.
- No-target-write confirmed.
- Runtime truth source declared or marked not applicable.
- Evidence and scorecard paths listed.

## Stop conditions

Stop if target is not selected, authority is missing, raw materials are offered before storage policy approval, unsafe material is staged, no-target-write is not confirmed, or run manifest approval is missing.

## Minimal target workspace plan template

```yaml
minimal_target_workspace_plan:
  target_project_id:
  proposed_root: target-projects/<target_project_id>/
  exception_requested: false
  create_now: false
  creation_requires_explicit_later_approval: true
```

## First maintainer prompt to ask the user

“Please choose the first target project for Mnemosyne’s no-target-write dry-run intake. Do not upload raw materials yet. For now, provide the target name, owner/decision authority, why this target is first, expected dry-run value, known non-goals, and whether the default future workspace root `target-projects/<target_project_id>/` is acceptable or needs an exception.”
