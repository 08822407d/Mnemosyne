---
design_id: MNEMOSYNE-PRO-04-v2
design_type: first_target_project_intake_and_approval_forms
repository: 08822407d/Mnemosyne
tested_at: 2026-06-30 America/Los_Angeles
tool_or_interface: ChatGPT GitHub connector read-only repository review plus local Markdown artifact generation
visible_model_label: GPT-5.5 Pro
repo_write_performed: false
target_project_selected: false
target_workspace_created: false
target_materials_ingested: false
target_repository_written: false
real_target_project_dry_run_started: false
design_verdict: READY_FOR_MAINTAINER_REVIEW
---

# MNEMOSYNE PRO-04 v2 — first target-project intake / approval form design

## 1. Executive summary

**Verdict: `READY_FOR_MAINTAINER_REVIEW`.**

The current repository supports a clean first-target intake and approval form. The execution-source rule is stable: `current/human-approved-spec.md` is the only Mnemosyne execution source; target workspaces are not Mnemosyne execution source; target workspaces are not automatically the target runtime truth source; and any first real target-project dry-run still requires target selection, authority/source map approval, safe input / user originals storage approval, no-target-write confirmation, and a user-approved run manifest.

The B1 hardening work materially improves readiness for first-target intake. `MNEMOSYNE-062` recorded the blocked attempt caused by missing PRO-02 / PRO-03 payloads. `MNEMOSYNE-063` then completed B1 PRO-02 / PRO-03 ingestion and added the expected pre-target controls: synthetic-vs-real separation, approval conflict resolution, redaction-manifest pairing, external-pointer safety, manual-import artifact classification, pointer-only originals guidance, workspace skeleton templates, and target-specific lesson-candidate containment. `MNEMOSYNE-064` and `MNEMOSYNE-065` repaired current-state / open-question placement issues. `current/open-questions.md` now records that after maintainer verification of MNEMOSYNE-065, the next recommended batch is PRO-04 only; `current/active-context.md`, `current/todo.md`, and `handoff/handoff-current.md` still use the earlier MNEMOSYNE-064 acceptance-gate wording. That wording difference is not a blocker for this design file, but a maintainer should be aware of it when accepting the PRO-04 package.

Remaining blockers before any real dry-run are user-facing approval blockers, not form-design blockers:

```yaml
remaining_before_real_dry_run:
  - user selects a real target project
  - user confirms owner / decision authority
  - user approves target workspace root or exception
  - user approves authority/source map
  - user approves safe input and user originals storage policy
  - user confirms no-target-write
  - user approves final run manifest
  - target runtime truth source is confirmed or explicitly marked none/not applicable
  - repository visibility and material safety are checked before any future staging or ingestion
  - any redacted excerpt has a redaction manifest
  - any external pointer passes pointer-safety checks
  - synthetic evidence remains separated from real dry-run evidence
```

No Codex repair is recommended before asking the user for first target selection. A later Codex task may be appropriate only after user target selection and explicit approval of workspace creation or setup work. This file does not generate that task.

## 2. Files read / missing files

```yaml
missing_files: []
blocked_by_missing_files: false
```

| path | read_status | relevance | blocker_if_missing |
|---|---|---|---|
| `README.md` | read | Repository positioning and visibility / Git-history safety boundary. | yes_for_visibility_boundary |
| `current/human-approved-spec.md` | read_in_chunks | Sole Mnemosyne execution source; target workspace principle; staged prompt-generation rule; safety and approval gates. | yes |
| `commands/load-mnemosyne-guidance.md` | read | Shortcut guidance; required read set; non-execution-source boundaries; long-transfer and staged prompt gating. | yes_for_guidance_loading |
| `current/active-context.md` | read_in_chunks | Compact current view, current blockers, B1 state, no-target/no-dry-run/no-material/no-write boundaries. | yes_for_current_state |
| `current/todo.md` | read_in_chunks | Waiting user decisions and no-real-dry-run state; PRO-04-only route after B1 review. | yes_for_current_state |
| `current/open-questions.md` | read_in_chunks | OP-08 status; B1 follow-up placement; MNEMOSYNE-065 acceptance-gate wording; PRO-02/PRO-03 statuses. | yes_for_current_state |
| `handoff/handoff-current.md` | read | Handoff route, prohibitions, no-target boundaries, first-dry-run preparation read pointers. | yes_for_current_state |
| `handoff/startup-instructions.md` | read_additional | Required by load guidance; startup behavior and first-target read extension. | no_but_limiting |
| `notes/first-target-project-dry-run-manifest-template.md` | read | Current run manifest fields, approval records, synthetic/real separation, redaction and pointer gates. | yes |
| `notes/first-target-project-dry-run-minimal-profile.md` | read | First dry-run profile; design-only/no-target-write/default safe-input rules. | yes |
| `notes/first-target-project-dry-run-result-template.md` | read | Result semantics and synthetic-smoke-test separation. | yes |
| `notes/first-target-project-dry-run-checklist.md` | read | Blocking preflight checks, approval conflict, redaction manifest, external pointer safety checks. | yes |
| `handoff/first-target-project-dry-run-onboarding-package.md` | read | First-target onboarding entry, authority map, actor permissions, no workspace before approvals. | yes |
| `notes/first-target-project-dry-run-review-instruments.md` | read | Drift, handoff, source-priority, triage, and adversarial review instruments. | yes |
| `notes/user-input-storage-governance-v0.1.md` | read | Original-outside-Git policy; authority layers; redaction manifest and external pointer schemas; pointer-only originals default. | yes |
| `notes/synthetic-smoke-test-result-template.md` | read | Synthetic smoke-test evidence separation and planned-not-created path convention. | yes |
| `notes/manual-import-artifact-classification-v0.1.md` | read | Classification gate for staged files and invalid artifact-type examples. | yes |
| `notes/target-project-workspace-skeleton-templates-v0.1.md` | read | Future workspace README / `originals/` pointer-only skeleton and lesson-candidate schema. | yes_for_workspace_template_design |
| `notes/target-project-workspace-boundary-and-layout-proposal.md` | read | Candidate detailed target workspace layout and three-layer boundary. | yes_for_workspace_template_design |
| `notes/pro-review-results/MNEMOSYNE-PRO-01-execution-source-consistency-audit.md` | read_in_chunks | PRO-01 audit, warnings, and later repair baseline. | yes_for_B1_context |
| `notes/pro-review-results/MNEMOSYNE-PRO-02-v2-synthetic-target-project-smoke-test.md` | read_in_chunks | Synthetic smoke-test result and synthetic-vs-real constraints. | yes_for_synthetic_separation |
| `notes/pro-review-results/MNEMOSYNE-PRO-03-v2-adversarial-failure-test.md` | read_in_chunks | Adversarial risk cases and recommended hardening now reflected by MNEMOSYNE-063. | yes_for_failure_controls |
| `raw/research-reports/cycles/2026Q2-user-input-governance/report-summaries/DR4_user_originals_requirements_redaction_governance_summary.md` | read | Research evidence for originals outside Git, restatement authority, redaction, external pointer policy. | yes_for_storage_policy |
| `raw/research-reports/cycles/2026Q2-user-input-governance/research-prompts/originals/DR4_user_originals_requirements_redaction_governance_prompt.md` | read | Prompt provenance and Deep Research full-body output-delivery rule. | no_but_relevant |
| `notes/codex-task-results/MNEMOSYNE-058-result.md` | read | PRO-01/DR4 processing and first-dry-run instrument hardening result. | yes_for_B1_context |
| `notes/codex-task-results/MNEMOSYNE-059-result.md` | read | DR4 prompt ingestion and post-058 sync repair. | yes_for_B1_context |
| `notes/codex-task-results/MNEMOSYNE-060-result.md` | read | Open-questions sync repair and no-target boundary preservation. | yes_for_B1_context |
| `notes/codex-task-results/MNEMOSYNE-061-result.md` | read | Staged Pro/Deep Research prompt-generation rule and no-target preservation. | yes_for_prompt_route |
| `notes/codex-task-results/MNEMOSYNE-062-result.md` | read | Blocked B1 ingestion attempt due missing PRO-02/PRO-03 payloads. | yes_for_B1_context |
| `notes/codex-task-results/MNEMOSYNE-063-result.md` | read | Completed B1 ingestion and pre-target hardening. | yes_for_B1_context |
| `notes/codex-task-results/MNEMOSYNE-064-result.md` | read_in_chunks | Current-state sync repair after 063 and PRO-04-only route after maintainer acceptance. | yes_for_B1_context |
| `notes/codex-task-results/MNEMOSYNE-065-result.md` | read | B1 follow-up moved into current open-questions section; 065 acceptance gate; PRO-04-only route. | yes_for_B1_context |
| `notes/codex-task-authoring-and-diff-verification-guidelines.md` | read | Codex task review guardrails and protected-path / diff-verification principles. | no_for_form_design_but_required_for_future_Codex |
| `notes/handoff-package-strategy-v0.1.md` | read | Handoff package structure, authority, approvals, forbidden actions, safe next action. | no_but_supports_prompt_design |
| `notes/handoff-replay-scorecard-v0.1.md` | read | Replay review model, critical checks, and false target/dry-run claim failures. | no_but_supports_review_boundary |

## 3. One-page user intake form

Use this form in the current Mnemosyne maintainer conversation **after** maintainer accepts this design. The user should fill it in chat. It does **not** ask for immediate upload, staging, or ingestion of target materials.

```yaml
target_project_selection:
  target_project_name:
  target_project_id_candidate:
  target_project_type:
  owner_or_decision_authority:
  why_this_target_first:
  expected_value_of_dry_run:
  known_non_goals:

target_workspace:
  default_root: target-projects/<target_project_id>/
  approve_default_root: yes | no | propose_exception
  exception_path_if_any:
  create_workspace_now: no
  workspace_creation_requires_later_codex_task: true

target_material_policy:
  will_provide_materials_now: no
  material_categories_planned:
    - public_project_description
    - synthetic_substitute
    - explicitly_redacted_excerpt
    - external_pointer_only
    - user_approved_decision
    - private_or_confidential_material_later_if_approved
    - none_yet
  originals_storage_preference: external_only | redacted_only | synthetic_only | safe_public_only | undecided
  repository_visibility_confirmed_by_user:
  contains_secrets_or_credentials:
  contains_personal_or_confidential_data:
  contains_private_source_or_customer_confidential_data:
  contains_customer_or_confidential_material:

user_verification_method:
  preferred_method: chat_confirmation | reviewed_markdown_manifest | other
  verifier_name_or_role:
  verification_notes:

synthetic_smoke_test_separation:
  ask_user_to_run_synthetic_test_now: no
  synthetic_substitute_allowed_if_user_selects_synthetic_only: true
  synthetic_result_may_close_real_target_dry_run_gate: false
```

User-facing interpretation rules:

```yaml
intake_rules:
  do_not_upload_or_stage_materials_now: true
  target_selection_only: true
  workspace_creation_now: false
  real_dry_run_now: false
  target_repository_write_now: false
  if_any_safety_field_is_yes_or_unknown:
    next_step: draft_storage_policy_and_source_map_before_any_material_transfer
```

## 4. Authority / source map form

```yaml
authority_source_map:
  target_owner:
  decision_authority:
  target_runtime_truth_source:
    status: none | external_owner_rule_confirmed | workspace_manifest_user_approved | unknown_requires_owner_decision
    authority_path_or_external_pointer:
    scope:
    limitations:
  source_items:
    - source_id:
      source_type:
      location_or_pointer:
      stored_in_repo: true | false
      owner:
      authority_level:
      sensitivity:
      allowed_use:
      accessible_to_executor:
      original_storage_status:
      redaction_manifest_path:
      external_pointer_safety_status:
```

Allowed `source_type` examples:

```yaml
source_type_examples:
  - user_approved_decision
  - public_project_description
  - target_execution_source
  - external_owner_rule
  - safe_external_pointer
  - redacted_excerpt
  - synthetic_substitute
  - maintainer_chat_statement
  - repository_file
  - unknown
```

Authority rules:

```yaml
authority_rules:
  if_target_runtime_truth_source_status_unknown_requires_owner_decision:
    proceed_to_real_dry_run: false
    required_action: ask_owner_or_user_to_decide_runtime_truth_source_status
  source_items_required_before_real_dry_run: true
  blank_owner_or_authority_blocks_real_dry_run: true
  mnemosyne_execution_source_is_not_target_runtime_truth_source: true
  target_workspace_is_not_automatically_target_runtime_truth_source: true
```

## 5. Safe input and user originals storage policy form

Raw originals and raw requirements default outside Git. The in-repository layer should contain only safe, approved, clearly labeled control artifacts: user-approved decisions, reviewed redacted excerpts with manifests, synthetic substitutes, and safe external pointers/manifests.

Storage options:

```text
external_only
safe_public
explicitly_redacted_with_manifest
synthetic_substitute
user_approved_decision_only
external_pointer_only
unsafe_do_not_store
pending_user_decision
```

Form:

```yaml
user_input_storage_policy:
  originals_storage: external_only | safe_public | explicitly_redacted_with_manifest | synthetic_substitute | user_approved_decision_only | external_pointer_only | unsafe_do_not_store | pending_user_decision
  originals_directory_default: pointer_or_readme_only
  restatements_role: explanatory_interpretation_not_original_or_approved_baseline
  decisions_storage: user_approved_decision_only_if_safe_for_repository_visibility
  redactions_storage: explicitly_redacted_with_manifest_only_if_safe_and_user_approved
  redaction_manifest_required: true
  synthetic_substitutes_allowed: true_if_labeled_and_not_reversible_to_confidential_original
  external_pointers_allowed_if_safe: true
  git_history_exposure_acknowledged:
```

Decision helper:

```yaml
storage_policy_decision_helper:
  public_or_visibility_unverified_repository:
    allowed:
      - safe_public
      - synthetic_substitute
      - explicitly_redacted_with_manifest
      - user_approved_decision_only_if_safe
      - external_pointer_only_if_pointer_contains_no_sensitive_data
    disallowed_by_default:
      - raw_user_originals
      - raw_requirements
      - secrets_or_credentials
      - private_source
      - customer_or_confidential_material
      - unredacted_personal_or_confidential_data
  private_repository:
    note: private_visibility_does_not_remove_git_history_or_future_visibility_switch_risk
    raw_originals_default: external_only
    raw_originals_in_git_requires_separate_explicit_user_approval: true
```

## 6. Redaction manifest and external pointer forms

### Redaction manifest schema

```yaml
redaction_manifest:
  source_item_id:
  original_storage_status: external_only | not_provided | unsafe_do_not_store | approved_private_external | unknown
  redacted_file_path:
  redaction_method:
  removed_categories:
  reviewer:
  approved_by_user:
  residual_risk:
  git_history_exposure_acknowledged:
```

Redaction gate:

```yaml
redacted_excerpt_storage_gate:
  redacted_excerpt_in_git_requires_manifest: true
  missing_manifest_blocks_git_storage: true
  missing_manifest_blocks_material_ingestion: true
  missing_manifest_blocks_real_dry_run: true
  visual_redaction_alone_is_not_approval: true
```

### External pointer schema

```yaml
external_source_pointer:
  source_id:
  location_type:
  location_description:
  owner:
  access_status:
  authority_level:
  sensitivity:
  allowed_use:
  not_stored_in_repo_reason:
  contains_secret: false
  contains_personal_or_confidential_data_in_pointer: false
  forbidden_content_absent:
    secrets:
    credentials:
    access_tokens:
    signed_urls:
    private_absolute_paths:
    sensitive_precise_locations:
    unapproved_customer_or_confidential_names:
    unapproved_personal_data:
```

External pointer gate:

```yaml
external_pointer_safety_gate:
  missing_safety_flags_blocks_git_storage: true
  missing_safety_flags_blocks_material_ingestion: true
  missing_safety_flags_blocks_real_dry_run: true
  pointer_indirection_is_not_automatically_safe: true
  unsafe_pointer_action: rewrite_as_safe_abstraction_or_keep_out_of_git
```

## 7. Manual-import artifact classification form

Use this only if files are staged later. It is **not** a request to stage files now.

```yaml
manual_import_artifact_classification:
  artifact_id:
  filename:
  artifact_type: full_report | summary | link_stub | prompt_original | result_record | pro_review_result | synthetic_smoke_test_result | adversarial_test_result | target_material | unknown
  full_body_present: yes | no | unknown
  required_sections_present: yes | no | unknown
  download_link_only: yes | no
  transient_or_broken_link_risk: yes | no | unknown
  safety_preflight:
    repository_visibility:
    safe_for_repo_visibility:
    contains_secrets_or_credentials:
    contains_personal_or_confidential_data:
    contains_private_source_or_customer_confidential_data:
    contains_target_materials:
  canonical_destination:
  decision: ingest | reject | request_body_chunks | hold_for_user
  rationale:
```

Invalid classifications:

```yaml
invalid_classification_examples:
  - invalid: summary_or_link_stub_as_research_report_original
    reason: research_report_original_requires_full_report_body_and_required_sections
    correct_action: request_body_chunks_or_hold_for_user

  - invalid: prompt_original_as_report_original
    reason: prompt text is research input/provenance, not report conclusion
    correct_action: classify_as_prompt_original

  - invalid: synthetic_smoke_test_result_as_real_target_dry_run_result
    reason: synthetic evidence cannot close real target dry-run gate or prove real PASS
    correct_action: classify_as_synthetic_smoke_test_result

  - invalid: target_material_staged_without_visibility_safety_approval
    reason: target materials require target selection, source map, storage policy, safety preflight, and run manifest approval
    correct_action: hold_for_user_or_reject_until_approved

  - invalid: redacted_excerpt_ingested_without_redaction_manifest
    reason: redacted excerpts in Git require a manifest
    correct_action: request_manifest_or_hold_for_user

  - invalid: external_pointer_ingested_with_signed_url_private_path_or_token
    reason: pointer itself leaks sensitive access/location information
    correct_action: reject_or_rewrite_as_safe_abstraction
```

## 8. No-target-write confirmation

```yaml
no_target_write_confirmation:
  user_confirms_no_target_write:
  target_repository_if_any:
  target_repository_write_allowed: false
  mnemosyne_repo_write_allowed_for_setup_tasks_only_after_codex_task: pending
  prohibited_actions:
    - write target repository
    - create target workspace before approval
    - ingest target materials before approval
    - claim real dry-run PASS from synthetic evidence
```

Clarifying rules:

```yaml
no_target_write_rules:
  mentioning_a_target_repository_is_not_write_permission: true
  dry_run_design_outputs_must_stay_mnemosyne_side_until_separately_approved: true
  target_repository_write_requires_separate_explicit_user_approval_and_is_out_of_scope_for_first_intake: true
  ordinary_chatgpt_session_must_not_claim_repository_write: true
```

## 9. Approval conflict resolution checklist

```yaml
approval_conflict_resolution:
  safety_critical_conflict: blocks_run
  permissive_legacy_field_cannot_override_approval_record: true
  strictest_safety_interpretation_wins: true
  required_action: user_clarification_or_manifest_reissue
```

Checklist:

```yaml
approval_conflict_checklist:
  - check: legacy_prose_says_approved_but_structured_approval_is_pending
    result: pass | block
    block_if: true

  - check: no_target_write_contradicted
    examples:
      - no_target_write_confirmed_true_but_target_repository_write_requested
      - approval_record.no_target_write.status_not_confirmed
    result: pass | block
    block_if: true

  - check: workspace_creation_approved_in_one_field_but_not_another
    result: pass | block
    block_if: true

  - check: target_material_ingestion_status_blank_unknown_or_pending
    result: pass | block
    block_if: true

  - check: source_map_authority_conflicts
    examples:
      - source_item_claims_authority_but_owner_missing
      - target_runtime_truth_source_unknown_but_design_treats_workspace_as_truth
      - old_project_note_overrides_owner_decision
    result: pass | block
    block_if: true

  - check: synthetic_fixture_approval_treated_as_real_target_approval
    result: pass | block
    block_if: true
```

Conflict handling rule:

```yaml
if_any_approval_conflict_check_blocks:
  real_dry_run_may_begin: false
  workspace_creation_may_begin: false
  target_material_ingestion_may_begin: false
  target_repository_write_may_begin: false
  next_action: ask_user_for_clarification_or_reissue_manifest
```

## 10. Run manifest approval checklist

Map this to the current run manifest fields before any real target-project dry-run.

```yaml
run_manifest_approval:
  run_manifest_status: draft | user_approved | invalid
  target_selected:
  workspace_root_approved:
  workspace_creation_approved:
  authority_source_map_approved:
  user_input_storage_policy_approved:
  redaction_or_pointer_policy_approved:
  no_target_write_confirmed:
  target_material_ingestion_status:
  target_runtime_truth_source_status:
  stop_conditions_reviewed:
  user_verification_method:
  approved_by_user:
  approved_at:
```

Minimal ready-to-approve manifest summary:

```yaml
ready_to_approve_manifest_summary:
  run_kind: real_target_project
  manifest_status: draft
  approval_record:
    target_selected:
      status: true | false | unknown
    target_workspace_root:
      status: approved | rejected | pending | not_applicable
    workspace_creation:
      status: approved | not_approved | pending | not_applicable
    user_input_storage_policy:
      status: approved | rejected | pending
    no_target_write:
      status: confirmed | not_confirmed | contradicted
    run_manifest:
      status: user_approved | draft | invalid
  target_runtime_truth_source:
    status: none | external_owner_rule_confirmed | workspace_manifest_user_approved | unknown_requires_owner_decision
  target_material_ingestion:
    status: none_provided | approved_to_ingest | ingested | unsafe_blocked | pending_user_decision
```

Approval rule:

```yaml
real_dry_run_start_rule:
  required_manifest_status: user_approved
  blank_safety_critical_fields_count_as_approval: false
  pending_unknown_or_contradicted_safety_critical_fields_block: true
  synthetic_smoke_test_manifest_may_close_real_gate: false
```

A real dry-run cannot begin unless the final run manifest is `user_approved`.

## 11. Stop conditions

Stop before workspace creation, material ingestion, real dry-run, or target write if any condition is true.

```yaml
stop_conditions:
  - missing_target_selection
  - missing_owner_or_decision_authority
  - missing_authority_source_map
  - missing_safe_input_policy
  - unsafe_or_ambiguous_material
  - raw_originals_proposed_for_git_without_visibility_safety_user_approval_and_git_history_acknowledgement
  - missing_redaction_manifest_for_redacted_excerpt
  - unsafe_external_pointer
  - missing_external_pointer_safety_flags
  - target_runtime_truth_source_unknown_requires_owner_decision
  - no_target_write_not_confirmed
  - no_target_write_contradicted
  - approval_conflict
  - repository_visibility_unverified_with_non_public_material
  - private_repository_treated_as_automatic_sensitive_storage_approval
  - attempt_to_treat_synthetic_evidence_as_real_dry_run_evidence
  - attempt_to_report_synthetic_smoke_test_as_real_target_dry_run_PASS
  - attempt_to_create_workspace_without_target_selection_and_approvals
  - attempt_to_write_target_repository_without_separate_explicit_approval
  - attempt_to_ingest_target_materials_before_manifest_approval
  - source_map_authority_conflict
  - target_workspace_treated_as_mnemosyne_execution_source
  - target_workspace_treated_as_target_runtime_truth_source_without_owner_rule_or_manifest
  - prompt_or_result_stub_treated_as_full_report_original
```

## 12. Minimal target workspace plan template

Template only. This plan does **not** create a workspace. Every path below is `planned_not_created`.

Default root:

```text
target-projects/<target_project_id>/
```

Tree:

```text
target-projects/<target_project_id>/                                      # planned_not_created
  README.md                                                              # planned_not_created
  00-project-meta/                                                       # planned_not_created
    project-manifest.md                                                  # planned_not_created
    authority-and-source-map.md                                          # planned_not_created
    privacy-and-safety.md                                                # planned_not_created
    status.md                                                            # planned_not_created

  01-user-input/                                                         # planned_not_created
    README.md                                                            # planned_not_created
    originals/                                                           # planned_not_created; pointer/README-only by default
      README.md                                                          # planned_not_created
    restatements/                                                        # planned_not_created; explanatory interpretation only
    decisions/                                                           # planned_not_created; user-approved decisions only if safe
    redactions/                                                          # planned_not_created; redacted/synthetic/manifests only

  02-mnemosyne-design-workbench/                                         # planned_not_created
    intake/                                                              # planned_not_created
    analysis/                                                            # planned_not_created
    candidate-memory-schema/                                             # planned_not_created
    candidate-workflows/                                                 # planned_not_created
    reviews/                                                             # planned_not_created
    issue-log/                                                           # planned_not_created
    unsupported-assumptions.md                                           # planned_not_created

  03-delivery-package/                                                   # planned_not_created
    delivery-manifest.md                                                 # planned_not_created
    runtime-memory-package/                                              # planned_not_created
    handoff-package/                                                     # planned_not_created
    drift-review-todo.md                                                 # planned_not_created

  04-dry-runs/                                                           # planned_not_created
    <dry_run_id>/                                                        # planned_not_created
      00-run-manifest.md                                                 # planned_not_created
      01-intake-and-design-draft.md                                      # planned_not_created
      02-delivery-and-handoff-draft.md                                   # planned_not_created
      03-result-and-postmortem.md                                        # planned_not_created

  05-feedback-and-lessons/                                               # planned_not_created
    project-feedback/                                                    # planned_not_created
    mnemosyne-lesson-candidates/                                         # planned_not_created
    example-excerpts/                                                    # planned_not_created
```

Root README banner template:

```markdown
# <target_project_id> Workspace

Status: planned_not_created until separately approved.

- This workspace is target-project-scoped.
- This workspace is not Mnemosyne execution source.
- This workspace is not automatically target runtime truth source.
- Target runtime truth source role requires a target-local manifest or owner rule and user approval.
- Do not use this workspace to update Mnemosyne global rules without candidate review and user approval.
- Do not write any target repository from this workspace unless separately and explicitly approved.
```

`01-user-input/originals/README.md` banner template:

```markdown
# originals

Default: external pointers or README only.

Raw user originals and raw requirements default outside Git.

Do not store raw originals in Git unless all of the following are true:

- current repository visibility is verified;
- material is safe for that visibility;
- user explicitly approves in-repo storage;
- Git history exposure is acknowledged;
- authority/source map records owner, sensitivity, allowed use, and retention.

Unsafe originals: do not store.
```

Workspace boundary summary:

```yaml
minimal_target_workspace_plan:
  creates_workspace: false
  all_paths_status: planned_not_created
  originals_directory_default: pointer_or_readme_only
  target_workspace_is_mnemosyne_execution_source: false
  target_workspace_is_automatically_target_runtime_truth_source: false
  target_workspace_creation_requires_later_codex_task: true_if_user_approves
  target_workspace_creation_requires:
    - target_selected
    - workspace_root_approved
    - authority_source_map_approved
    - safe_input_policy_approved
    - no_target_write_confirmed
    - run_manifest_user_approved
```

## 13. First maintainer prompt to ask the user

~~~markdown
## 操作内容（需要你手动确认）

请先不要上传原始材料、不要暂存文件、不要创建 target workspace。我们现在只做第一个真实 target-project 的选择和安全边界确认。

请按下面表单回复：

```yaml
target_project:
  name_and_short_description:
  owner_or_decision_authority:
  why_this_target_first:
  known_non_goals:

workspace:
  default_root: target-projects/<target_project_id>/
  accept_default_root: yes | no | propose_exception
  exception_path_if_any:
  create_workspace_now: no

materials_boundary:
  planned_material_type: public | synthetic | redacted | external_only | private_or_confidential_later | undecided
  contains_secrets_or_credentials: yes | no | unknown
  contains_personal_or_confidential_data: yes | no | unknown
  contains_private_source_or_customer_confidential_data: yes | no | unknown
  contains_customer_or_confidential_material: yes | no | unknown
  raw_material_upload_now: no

no_target_write:
  confirm_no_target_repository_write: yes | no
  target_repository_if_any:

next_step:
  proceed_to_draft_run_manifest_next: yes | no | ask_me_first
```

确认后，下一步只会起草 run manifest / authority-source-map / safe-input policy 草案；不会启动真实 dry-run，不会创建 workspace，不会摄入 target materials，也不会写 target repository。
~~~

## 14. Whether a Codex task is recommended

```yaml
codex_task_recommended_now: no
```

Rationale:

```yaml
codex_recommendation_rationale:
  before_asking_user_for_target_selection:
    codex_task_needed: false
    reason: B1 hardening instruments needed for intake are present; the next safe action is user target selection and approval intake, not repository editing.
  after_user_target_selection:
    possible_future_codex_task: yes_after_separate_user_approval
    possible_scope_only:
      - create approved target workspace skeleton
      - persist approved run manifest
      - persist approved authority/source map
      - persist approved safe-input policy
    hard_boundaries:
      - do_not_write_target_repository
      - do_not_ingest_target_materials_without_material-specific approval
      - do_not_claim_real_dry_run_started_or_passed
      - do_not_generate_task_now
```

## 15. Evidence map

```yaml
evidence:
  - claim: Mnemosyne is a memory-system meta-agent work repository, and repository visibility / Git history exposure matters before storing materials.
    path: README.md
    authority_level: current_state
    note: README states the repository's role and visibility/Git-history safety model.

  - claim: current/human-approved-spec.md is the only Mnemosyne execution source.
    path: current/human-approved-spec.md
    authority_level: execution_source
    note: Governs all support instruments and current-state files.

  - claim: target workspace default root is target-projects/<target_project_id>/ and is not Mnemosyne execution source or automatic target runtime truth source.
    path: current/human-approved-spec.md
    authority_level: execution_source
    note: Section 16 promoted the minimal target-project workspace principle.

  - claim: workspace creation, target material ingestion, real target dry-run, and target repository writes require prior user approvals.
    path: current/human-approved-spec.md
    authority_level: execution_source
    note: Section 16 lists target selection, authority/source map, safety/privacy, no-target-write, and run manifest approval prerequisites.

  - claim: current state has no target selected, no target materials ingested, no target repository written, and no real dry-run started.
    path: current/active-context.md
    authority_level: current_state
    note: Compact current view records no target action and first-target approval gates.

  - claim: waiting user decisions are target selection, workspace root/exception, owner/authority, source map, storage policy, no-target-write, and run manifest approval.
    path: current/todo.md
    authority_level: current_state
    note: TODO waiting-for-user-decision section matches first-target intake prerequisites.

  - claim: B1 PRO-02 synthetic smoke test was ingested and must not close the real target dry-run gate.
    path: current/open-questions.md
    authority_level: current_state
    note: Current B1 follow-up records PRO-02 verdict PASS_WITH_WARNINGS and synthetic result limitations.

  - claim: B1 PRO-03 adversarial test was ingested and recommended repairs that were hardened by MNEMOSYNE-063.
    path: current/open-questions.md
    authority_level: current_state
    note: Current B1 follow-up records PRO-03 verdict REPAIR_RECOMMENDED and repair status.

  - claim: MNEMOSYNE-062 was blocked because PRO-02/PRO-03 payloads were missing.
    path: notes/codex-task-results/MNEMOSYNE-062-result.md
    authority_level: task_result
    note: No ingestion or hardening occurred in 062.

  - claim: MNEMOSYNE-063 completed B1 ingestion and added synthetic, manual-import, workspace skeleton, approval conflict, redaction, pointer, originals, and lesson-candidate controls.
    path: notes/codex-task-results/MNEMOSYNE-063-result.md
    authority_level: task_result
    note: No target action or execution-source modification occurred.

  - claim: MNEMOSYNE-064 repaired post-063 current-state sync residue, with PRO-04-only recommended after maintainer acceptance of 064.
    path: notes/codex-task-results/MNEMOSYNE-064-result.md
    authority_level: task_result
    note: Active/todo/handoff still carry this 064 acceptance wording.

  - claim: MNEMOSYNE-065 moved the B1 follow-up into the current open-questions section and records PRO-04-only after maintainer acceptance of 065.
    path: notes/codex-task-results/MNEMOSYNE-065-result.md
    authority_level: task_result
    note: 065 modified only current/open-questions.md; no target action occurred.

  - claim: synthetic smoke tests must not be reported as real target-project dry-run PASS.
    path: notes/synthetic-smoke-test-result-template.md
    authority_level: support_instrument
    note: Template requires real target fields false and `may_be_reported_as_real_dry_run_PASS: false`.

  - claim: run manifest must distinguish real_target_project from synthetic_smoke_test and requires user_approved before real dry-run.
    path: notes/first-target-project-dry-run-manifest-template.md
    authority_level: support_instrument
    note: Manifest fields and rules are the direct basis for section 10.

  - claim: approval conflicts block runs; permissive legacy/prose fields cannot override structured approval records.
    path: notes/first-target-project-dry-run-manifest-template.md
    authority_level: support_instrument
    note: MNEMOSYNE-063 hardening added approval_conflict_resolution.

  - claim: redacted excerpts stored in Git require redaction manifests, and missing manifests block ingestion / real dry-run.
    path: notes/first-target-project-dry-run-manifest-template.md
    authority_level: support_instrument
    note: redacted_excerpt_storage_gate supplies required fields.

  - claim: external pointers must not contain secrets, credentials, signed URLs, private paths, sensitive locations, or unapproved personal/confidential data.
    path: notes/user-input-storage-governance-v0.1.md
    authority_level: support_instrument
    note: Governance file and manifest/checklist pointer gates align.

  - claim: raw originals and raw requirements default outside Git; repo may store approved decisions, redacted excerpts, synthetic substitutes, and safe pointers/manifests.
    path: notes/user-input-storage-governance-v0.1.md
    authority_level: support_instrument
    note: Direct basis for sections 5 and 6.

  - claim: DR4 research supports original-outside-Git, public/unverified public-risk, restatement authority boundaries, redaction documentation, and pointer safety.
    path: raw/research-reports/cycles/2026Q2-user-input-governance/report-summaries/DR4_user_originals_requirements_redaction_governance_summary.md
    authority_level: research_evidence
    note: Research evidence only, not execution source.

  - claim: manual imports must classify full report vs summary/link stub vs prompt original vs result evidence before moving.
    path: notes/manual-import-artifact-classification-v0.1.md
    authority_level: support_instrument
    note: Direct basis for section 7.

  - claim: future target workspace skeletons must preserve not-execution-source banners and pointer-only originals default.
    path: notes/target-project-workspace-skeleton-templates-v0.1.md
    authority_level: support_instrument
    note: Direct basis for section 12.

  - claim: target workspace detailed layout is a non-execution-source candidate reference; no workspace should be created until target and approvals exist.
    path: notes/target-project-workspace-boundary-and-layout-proposal.md
    authority_level: support_instrument
    note: Detailed tree informs the template but does not authorize creation.

  - claim: PRO-02 synthetic smoke-test result was PASS_WITH_WARNINGS and performed no real target selection/workspace/material/repo write/dry-run.
    path: notes/pro-review-results/MNEMOSYNE-PRO-02-v2-synthetic-target-project-smoke-test.md
    authority_level: pro_review_evidence
    note: Evidence for optional synthetic separation and non-closure of real gate.

  - claim: PRO-03 adversarial result was REPAIR_RECOMMENDED and identified risks now reflected in B1 hardening.
    path: notes/pro-review-results/MNEMOSYNE-PRO-03-v2-adversarial-failure-test.md
    authority_level: pro_review_evidence
    note: Evidence for approval conflict, redaction, pointer, import classification, and skeleton controls.

  - claim: Codex tasks must not rely on prose completion claims alone; diff/protected-path verification is required for future repo edits.
    path: notes/codex-task-authoring-and-diff-verification-guidelines.md
    authority_level: support_instrument
    note: Relevant to later setup tasks, not to this design-only artifact.

  - claim: handoff packages should identify execution source or owner rule, current gate, approvals, forbidden actions, one safe next action, and evidence map.
    path: notes/handoff-package-strategy-v0.1.md
    authority_level: support_instrument
    note: Informs the concise maintainer prompt and evidence mapping.

  - claim: false dry-run/target claims and missing user approvals are P0 replay failures.
    path: notes/handoff-replay-scorecard-v0.1.md
    authority_level: support_instrument
    note: Supports no false real-dry-run or target selection claims.
```

## 16. Limitations

```yaml
limitations:
  - This Pro conversation did not write to the Mnemosyne repository.
  - No target project was selected.
  - No target workspace was created.
  - No target materials were requested, uploaded, staged, classified for real intake, or processed.
  - No run manifest was approved.
  - No real target-project dry-run was started.
  - No real target-project dry-run PASS was claimed.
  - No target repository was written.
  - No Codex task was generated.
  - No DR3 or DR5 prompt was generated.
  - This output is design-only and non-execution-source.
  - The file is a local downloadable artifact, not a repository file.
  - Current-state wording is not perfectly uniform: current/open-questions.md and MNEMOSYNE-065-result.md carry the 065 acceptance-gate wording, while current/active-context.md, current/todo.md, and handoff/handoff-current.md still carry 064 acceptance-gate wording.
  - The design assumes the maintainer will review and accept MNEMOSYNE-065 before using the first maintainer prompt for real target selection.
  - Repository visibility can change; visibility must be reverified before any future import or target-material storage.
  - OP-08 remains open for broader privacy/redaction/access-control governance; this design uses conservative v0.1 stop gates rather than closing OP-08.
  - The target workspace plan is a template only; all paths are planned_not_created.
```
