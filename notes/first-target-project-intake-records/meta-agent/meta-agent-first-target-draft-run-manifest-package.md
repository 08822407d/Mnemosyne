# Meta-Agent First Target-Project Draft Run Manifest Package

```yaml
package_id: META-AGENT-FIRST-TARGET-DRAFT-RUN-MANIFEST-PACKAGE-2026-07-01
status: draft_for_user_review_not_approved
artifact_role: pre-workspace first-target draft run-manifest / authority-source-map / safe-input package
execution_source: false
target_project_id: meta-agent
target_project_name: Meta-Agent
target_selected_for_manifest_drafting: true
target_workspace_created: false
target_materials_ingested: false
target_repository_written: false
real_target_project_dry_run_started: false
run_manifest_approved_for_real_dry_run: false
source_intake_file: meta-agent-target-project-selection-complete-draft.yaml
user_confirmation_basis: user confirmed yes to target selection for manifest drafting and yes to using the intake draft as source
```

## 1. Positioning

This package is a **draft control package**, not an approved run manifest.

It exists to convert the user-confirmed Meta-Agent target-project intake draft into a structured draft manifest package for review.

It does **not** authorize:

- real target-project dry-run;
- target workspace creation;
- target material ingestion;
- target repository write;
- target runtime truth-source assignment;
- execution-source update;
- global Mnemosyne rule promotion.

## 2. User confirmation recorded in maintainer conversation

```yaml
user_confirmation:
  approve_target_selection_for_manifest_drafting: yes
  approve_using_this_intake_draft_as_source_for_draft_run_manifest: yes
  scope:
    - draft_manifest_preparation
    - authority_source_map_drafting
    - safe_input_policy_drafting
    - no_target_write_confirmation_drafting
  explicitly_not_approved:
    - real_target_project_dry_run
    - target_workspace_creation
    - target_material_ingestion
    - target_repository_write
    - execution_source_update
```

## 3. Draft run manifest

```yaml
run_manifest_version: v0.1-meta-agent-draft-2026-07-01
dry_run_id: meta-agent-first-target-dry-run-draft-001
run_kind: real_target_project
manifest_status: draft
target_project_name: Meta-Agent
target_project_id: meta-agent
target_project_type:
  primary: ai_agent_project
  secondary:
    - long_term_research
    - software_development_methodology
  classification_status: hybrid
owner_or_decision_authority: user
bounded_scope: >
  Prepare a draft run manifest for using Meta-Agent as the first real/semireal target-project
  intake case for Mnemosyne. This draft is limited to manifest/source-map/storage/no-target-write
  planning. It does not start the dry-run.
current_stage: first_target_selection_confirmed_for_manifest_drafting
project_goal: >
  Meta-Agent is a general-purpose target project for designing single-agent, multi-agent-team,
  workflow, memory, tool/model-routing, and human-decision-boundary systems. Early practice may
  focus on software-development scenarios, but that does not collapse the general Meta-Agent
  purpose into software development only.
memory_problem_to_solve: >
  Determine whether Mnemosyne can transform an incomplete high-level agent concept into structured
  intake, project-level memory design, handoff/delivery/review drafts, and an auditable target
  workspace/run-manifest path without fabricating missing context or violating no-write/no-ingest
  boundaries.
target_execution_source_or_owner_rule: none_declared_yet
target_execution_source_status: unknown_requires_owner_decision
source_items:
  - source_id: meta-agent-intake-draft-2026-07-01
    path_or_link: meta-agent-target-project-selection-complete-draft.yaml
    role: user_supplied_first_target_selection_intake_draft
    authority: user_confirmed_source_for_draft_manifest_preparation
    owner: user
    date_or_version: 2026-07-01
    sensitivity: public_safe_selection_draft
    allowed_use: draft_manifest_preparation_only
    accessible_to_executor: true
  - source_id: mnemosyne-execution-source
    path_or_link: current/human-approved-spec.md
    role: Mnemosyne_execution_source
    authority: highest_for_Mnemosyne_operation_boundaries
    owner: Mnemosyne_maintainer
    sensitivity: repository_file
    allowed_use: govern_Mnemosyne_behavior_and_boundaries
    accessible_to_executor: true
  - source_id: intake-form-support-instrument
    path_or_link: notes/first-target-project-intake-and-approval-forms-v0.1.md
    role: non_execution_source_intake_support_form
    authority: support_instrument_under_execution_source
    owner: Mnemosyne_maintainer
    sensitivity: repository_file
    allowed_use: shape_intake_and_approval_fields
    accessible_to_executor: true
  - source_id: dry-run-manifest-template
    path_or_link: notes/first-target-project-dry-run-manifest-template.md
    role: non_execution_source_run_manifest_template
    authority: support_instrument_under_execution_source
    owner: Mnemosyne_maintainer
    sensitivity: repository_file
    allowed_use: shape_manifest_fields
    accessible_to_executor: true
current_task_or_milestone: draft_meta_agent_first_target_run_manifest_package
recent_user_or_owner_decision: >
  User confirmed Meta-Agent may be treated as the first target for draft manifest preparation,
  and confirmed that the received intake draft may be used as the source for that draft.
known_stale_or_superseded_item:
  - item: lost_full_original_meta_agent_conversation
    disposition: do_not_reconstruct_as_fact; use only user-provided summaries and confirmations
  - item: Meta-Agent deep research reports
    disposition: research_evidence_or_design_input_candidates_only; not execution source
challenge_case:
  type: incomplete_real_target_concept
  description: >
    Meta-Agent is sufficiently real to test Mnemosyne target intake and memory-system design,
    but not yet sufficiently specified to permit real dry-run execution without further manifest,
    authority/source-map, and runtime-truth-source decisions.
privacy_and_repository_boundary:
  current_repository_visibility: checked_public_in_intake_draft_but_must_reverify_before_import_or_staging
  input_safety_status: public | synthetic | explicitly_redacted | external_pointer_only
  raw_material_upload_now: false
  contains_secrets_or_credentials: false_or_not_provided
  contains_personal_or_confidential_data: false_or_not_provided
  contains_private_source_or_customer_confidential_data: false_or_not_provided
  contains_customer_or_confidential_material: false_or_not_provided
target_project_workspace:
  workspace_root: target-projects/meta-agent/
  workspace_status: not_created
  workspace_creation_approved: false
  workspace_is_mnemosyne_execution_source: false
  workspace_is_target_runtime_truth_source: false
  project_meta_path: target-projects/meta-agent/00-project-meta/
  user_input_path: target-projects/meta-agent/01-user-input/
  mnemosyne_design_workbench_path: target-projects/meta-agent/02-mnemosyne-design-workbench/
  delivery_package_path: target-projects/meta-agent/03-delivery-package/
  dry_run_path: target-projects/meta-agent/04-dry-runs/meta-agent-first-target-dry-run-draft-001/
  feedback_and_lessons_path: target-projects/meta-agent/05-feedback-and-lessons/
  path_status: planned_not_created
user_input_storage_policy:
  originals_storage: external_reference_only
  originals_directory_default: pointer_or_readme_only
  restatements_path: target-projects/meta-agent/01-user-input/restatements/
  decisions_path: target-projects/meta-agent/01-user-input/decisions/
  redactions_path: target-projects/meta-agent/01-user-input/redactions/
  external_pointer_or_redacted_reference: future_if_needed
  policy_status: draft_pending_final_manifest_approval
no_target_write_confirmed: true
target_materials_uploaded_or_ingested: false
expected_dry_run_outputs:
  - memory_system_design_spec_draft
  - target_project_workspace_plan
  - authority_source_map
  - safe_input_policy
  - handoff_package_draft
  - delivery_package_inventory
  - unsupported_assumptions_log
  - postmortem_and_regression_candidates_after_actual_dry_run
user_verification_method: reviewed_markdown_manifest_or_chat_confirmation
unsupported_assumptions:
  - target_runtime_truth_source_is_not_yet_declared
  - external_target_repository_is_not_selected_or_approved
  - target_workspace_is_not_created
  - no_target_materials_are_ingested
  - operator_confirmation_is_pending_until_final_manifest_review
  - full_original_meta_agent_conversation_is_lost_and_must_not_be_reconstructed_as_fact
user_approvals:
  target_selected_for_manifest_drafting: true
  target_selected_for_real_dry_run: false
  workspace_root_approved_for_planning: true
  workspace_creation_approved: false
  authority_confirmed_for_manifest_drafting: true
  source_use_approved_for_manifest_drafting: true
  privacy_boundary_approved_for_no_material_draft: true
  no_target_write_approved: true
  run_manifest_approved_for_real_dry_run: false
approval_record:
  target_selected:
    status: true
    approved_by: user
    approved_at: 2026-07-01
    scope: draft_manifest_preparation_only
  target_workspace_root:
    status: approved
    path: target-projects/meta-agent/
    approved_by: user_via_intake_draft_confirmation
    approved_at: 2026-07-01
    limitations: planning_only_not_creation
  workspace_creation:
    status: not_approved
    approved_by: null
    approved_at: null
  user_input_storage_policy:
    status: pending
    approved_by: null
    approved_at: null
    note: no raw materials now; final policy still requires manifest approval
  no_target_write:
    status: confirmed
    approved_by: user
    approved_at: 2026-07-01
  run_manifest:
    status: draft
    approved_by: null
    approved_at: null
target_runtime_truth_source:
  status: unknown_requires_owner_decision
  authority_path_or_external_pointer: none_declared_yet
  approved_by: null
  approved_at: null
  scope: Meta-Agent target project design
  limitations:
    - target-projects/meta-agent/ is planned workspace only and not runtime truth source
    - external Meta-Agent repository is not selected or approved
    - future approved run manifest or owner rule must define this before real dry-run
target_material_ingestion:
  status: none_provided
  allowed_material_types:
    - public_project_description
    - synthetic_substitute
    - explicitly_redacted_excerpt_after_manifest
    - external_pointer_only_after_pointer_safety_review
  prohibited_material_types:
    - raw_user_originals
    - lost_conversation_reconstruction_as_fact
    - unredacted_personal_or_confidential_data
    - secrets_or_credentials
    - private_source
    - customer_or_confidential_material
redaction_and_external_pointer:
  redaction_manifest_path: not_applicable_no_materials
  external_source_pointer_path: not_applicable_no_external_pointer
  git_history_exposure_acknowledged: true_for_policy_no_repository_write_performed
stop_conditions_triggered:
  - target_runtime_truth_source_unknown_requires_owner_decision_for_real_dry_run
  - final_run_manifest_not_user_approved
  - workspace_creation_not_approved
  - target_material_ingestion_not_approved
```

## 4. Draft authority/source map

```yaml
authority_source_map:
  user_decision_authority: user
  target_owner: user
  allowed_sources:
    - current_maintainer_chat_user_confirmations
    - meta-agent-target-project-selection-complete-draft.yaml
    - user_provided_meta_agent_summary_descriptions
    - uploaded_meta_agent_deep_research_reports_after_classification_and_review
    - current Mnemosyne execution source for Mnemosyne operation boundaries
    - current first-target intake/run-manifest/evaluation support instruments
    - public/official/current verifiable sources when tool/platform facts matter
    - explicitly redacted excerpts, synthetic substitutes, or safe external pointers if later approved
  forbidden_sources:
    - lost full original conversation reconstructed as fact
    - unconfirmed model memory
    - unredacted private source
    - secrets, credentials, tokens, account data
    - unapproved personal/confidential/customer material
    - unverified current tool/model/service capability assumptions
    - research reports, handoff, active-context, task result, scorecard, replay output, or this draft as execution source
  source_priority_order:
    - current user explicit decisions/corrections
    - current/human-approved-spec.md for Mnemosyne operation boundaries
    - future user-approved actual run manifest
    - current maintainer chat Meta-Agent confirmations
    - user-provided Meta-Agent summary/raw description
    - Meta-Agent Deep Research reports after ingestion/classification as evidence
    - verifiable current public/official sources
    - AI inferences explicitly labeled assumption/needs_user_confirmation
  conflict_resolution_rule: >
    For Mnemosyne operation boundaries, current/human-approved-spec.md wins. For Meta-Agent target
    design, current user-confirmed target decisions and future approved target spec/run manifest win.
    If sources conflict, record open question / needs_user_confirmation; do not merge silently.
  approval_status: draft_for_manifest_review
```

## 5. Draft safe input / originals storage policy

```yaml
safe_input_policy:
  repository_visibility_checked: intake_draft_says_checked_public_for_selection_draft_only
  must_reverify_before_import_or_staging: true
  permitted_material_categories_now:
    - current_chat_user_confirmations
    - public_project_description
    - synthetic_substitute
    - explicitly_redacted_excerpt_if_later_manifested
    - external_pointer_only_if_later_safety_checked
  raw_material_upload_now: false
  user_originals_storage_default: outside_git_pointer_only
  store_raw_originals_in_repo: no
  complete_lost_original_conversation_handling: do_not_reconstruct_as_fact
  future_import_requires:
    - repository_visibility_reverification
    - material_sensitivity_preflight
    - manual_import_artifact_classification
    - approved source map
    - approved safe-input policy
    - user approval
  approval_status: draft_pending_manifest_approval
```

## 6. Draft no-target-write confirmation

```yaml
no_target_write_confirmation:
  target_repository_if_any: none_declared_yet_future_external_meta_agent_repository_possible_but_not_selected_or_approved
  target_repository_write_allowed: false
  target_workspace_write_allowed: false_until_explicit_approval
  user_confirmed: confirmed_for_selection_and_draft_manifest_preparation
  operator_confirmed: pending_until_manifest_execution_planning
  prohibited_actions:
    - write target repository
    - create target workspace before approval
    - ingest target materials before approval
    - claim real dry-run started or passed
    - use synthetic or draft evidence as real dry-run evidence
```

## 7. Draft stop conditions before real dry-run

```yaml
stop_conditions_before_real_dry_run:
  - final_run_manifest_not_user_approved
  - target_runtime_truth_source_unknown_requires_owner_decision
  - workspace_creation_not_approved
  - target_material_ingestion_not_approved
  - safe_input_policy_not_final_approved
  - operator_confirmation_pending
  - repository_visibility_not_reverified_before_any_material_staging
  - raw_materials_uploaded_before_storage_policy
  - attempt_to_reconstruct_lost_original_conversation_as_fact
  - target_repository_write_requested_without_separate_approval
```

## 8. Draft result / next route

```yaml
draft_package_assessment:
  ready_for_user_review: true
  ready_for_real_dry_run: false
  ready_for_workspace_creation: false
  ready_for_target_material_ingestion: false
  ready_for_target_repository_write: false

recommended_next_action:
  - review this draft package
  - decide target_runtime_truth_source status
  - decide whether to approve the draft run manifest for a controlled no-target-write dry-run preparation phase
  - decide whether and when to create target-projects/meta-agent/ workspace skeleton through a separate Codex task
```
