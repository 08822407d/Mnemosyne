---
target_project_id: meta-agent
artifact_id: META-AGENT-V0.1-SOURCE-OWNER-MAP-001
artifact_role: source_and_owner_authority_map
status: proposed_v0_1_pending_owner_acceptance
authority_level: user_approved_support_record_when_activated
target_runtime_truth_source: false
created_by_task: MNEMOSYNE-171
policy_version: 0.1.0
source_refs:
  - target-projects/meta-agent/current/approved-spec.md
  - notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M0-requirements-and-authority-baseline.md
  - notes/first-target-project-intake-records/meta-agent/meta-agent-v0.1-M1-workspace-safety-build-manifest.md
known_limits:
  - does_not_grant_permission_by_itself
  - platform_permission_is_not_task_authorization
---

# Meta-Agent Source and Owner Map v0.1

## 1. Owner and final authority

```yaml
target_owner:
  actor: user
  final_authority_for:
    - product_purpose_scope_and_non_goals
    - target_runtime_truth
    - methodology_promotion
    - privacy_and_material_use
    - repository_and_write_scope
    - migration_and_operational_acceptance
```

No Agent, model, research report, repository path or tool permission can replace the user's authority.

## 2. Runtime truth and repository roles

```yaml
runtime_truth:
  designated_path: target-projects/meta-agent/current/approved-spec.md
  current_effect: pending_owner_acceptance
  entire_directory_is_truth_source: false

Mnemosyne:
  repository: 08822407d/Mnemosyne
  role:
    - design_archive
    - control_plane
    - bootstrap_host
  target_runtime_truth: false
  root_execution_source_scope: Mnemosyne_process_and_safety_only
```

After activation, the designated spec is the sole Meta-Agent runtime truth source. Other files provide methods, evidence, current state, history or navigation only.

## 3. Source classes

| Source class | Examples | Authority and permitted use |
|---|---|---|
| `target_truth` | activated `current/approved-spec.md` | Governs Meta-Agent runtime behavior. |
| `current_user_decision` | explicit target-scoped user instruction with authorization record | Highest target authority; must be recorded through an approved change when it changes truth. |
| `approved_target_decision` | `MA-DEC-*` record accepted by user | Supports and explains target truth. |
| `approved_method` | `MA-METHOD-*` referenced by target truth | General method library; cannot override requirements or owner decisions. |
| `current_state` | `current/active-context.md` | Operational navigation; may be stale and is not execution source. |
| `handoff` | `handoff/handoff-current.md` | Fresh-session navigation only. |
| `case_or_feedback_evidence` | `MA-CASE-*`, `MA-FEEDBACK-*` | Scoped evidence/candidate input; no automatic methodology promotion. |
| `research_evidence` | reviewed reports and evidence ledgers | Supports decisions; never target truth by itself. |
| `raw_or_external_evidence` | public, redacted, pointer or outside-Git material | Historical evidence subject to safety and authority review. |
| `model_inference` | analysis not confirmed by user/evidence | Low authority; must be labeled and revisable. |
| `platform_or_tool_fact` | official current documentation or observed surface state | Time-sensitive evidence; requires freshness checks. |

## 4. Source priority and conflict handling

```yaml
source_priority:
  - current_explicit_user_decision_with_target_scope
  - activated_target_approved_spec
  - approved_target_change_manifest_within_scope
  - approved_MA_DEC_record
  - approved_methodology_referenced_by_spec
  - current_state_and_handoff_for_navigation_only
  - reviewed_case_feedback_and_research_evidence
  - model_inference

conflict_rule:
  mark_conflict: required
  stop_affected_action: required
  silent_resolution_or_promotion: prohibited
  user_decision_required_for:
    - requirement_or_non_goal_change
    - target_truth_change
    - owner_or_authority_change
    - privacy_or_material_scope_change
    - methodology_promotion
```

A newer artifact is not automatically more authoritative.

## 5. Allowed material classes

```yaml
allowed_after_applicable_preflight:
  - public_information
  - synthetic_material
  - explicitly_redacted_excerpt_with_manifest
  - safe_external_pointer
  - outside_git_reference
  - high_level_non_sensitive_user_confirmed_requirement_or_decision
  - reviewed_non_sensitive_research_or_method_summary
```

The default route for private or large originals is `outside_git`.

## 6. Prohibited material classes

```yaml
prohibited_in_public_bootstrap_Git:
  - secrets
  - credentials
  - tokens_or_account_material
  - private_source_code
  - customer_or_confidential_material
  - unredacted_personal_or_sensitive_learning_records
  - raw_voice_or_chat_transcripts_without_separate_approval
  - sensitive_payload_hidden_inside_a_pointer
  - invented_reconstruction_of_lost_material
  - unverified_platform_or_model_claim_as_stable_truth
```

Ownership does not equal storage authorization.

## 7. Repository and target action authority

Every write must have a canonical task-local action context.

```yaml
repository_action_context_minimum:
  task_id:
  actor:
  product_surface:
  exact_repository_or_target:
  base_ref:
  allowed_paths: []
  allowed_actions: []
  prohibited_paths_or_actions: []
  user_authorization_ref:
  safety_preflight_ref:
  expires_with_task: true
```

Rules:

1. App connection, persistent permission, approval card or repository access does not authorize the current action.
2. Read authorization does not imply write authorization.
3. Mnemosyne write authorization does not imply target-repository or runtime-store write authorization.
4. One task's authorization is not precedent for a later task.
5. Ambiguous path or authority scope is a stop condition.

## 8. Write and promotion authority by object

| Object/action | Who may propose | Required approval |
|---|---|---|
| target truth update | Agent or user | explicit user authorization and validated change record |
| current-context/handoff sync | bounded executor | task-local authorization; must remain consistent with truth |
| new methodology | Agent/research/user | frontier review when novel; user acceptance before approved status |
| case/feedback entry | bounded executor or user | evidence/source review; no automatic promotion |
| methodology promotion | reviewer/Agent candidate | user confirmation and policy/version update |
| private material use | user | explicit material and storage approval |
| operational activation | user | explicit owner disposition after M2 validation |
| migration | Agent/user proposal | approved `MA-MIG-*`, validation and rollback |

## 9. Evidence, support, candidate and inference labeling

```yaml
role_labels:
  evidence:
    meaning: observed_or_sourced_material_supporting_a_claim
  support:
    meaning: navigation_process_or_non_authoritative_structure
  candidate:
    meaning: proposed_requirement_method_or_change_not_yet_accepted
  inference:
    meaning: model_generated_interpretation_with_uncertainty
  approved_target_truth:
    meaning: only_content_accepted_in_the_designated_runtime_truth_source
```

A role change requires an explicit decision; it cannot be implied by moving a file.

## 10. Freshness and external facts

- Tool, product and model capabilities must carry a date/source when material to a decision.
- Consumer UI labels record operator-visible selection, not exact served backend.
- Response speed, style and model self-identification are not backend attestation.
- Stale or conflicting external facts are marked unknown and must not drive high-impact execution.

## 11. Review and supersession

This map is reviewed whenever:

- owner or runtime-truth arrangement changes;
- repository visibility or storage policy changes;
- a new material class is introduced;
- cross-Agent sharing or private storage is proposed;
- migration to an external repository is considered.

Changes require versioning, source review and an owner decision.
