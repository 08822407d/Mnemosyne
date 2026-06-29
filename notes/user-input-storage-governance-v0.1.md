# User Input Storage Governance v0.1

## Positioning

- Non-execution-source governance guidance.
- Research basis: `RPT-2026Q2-UIG-0001`, if ingested.
- Does not override `current/human-approved-spec.md`.
- Target materials still require target selection, authority/source map, safety/privacy boundary, no-target-write, and run manifest approval.

## 1. Default model

- Original layer outside Git; approved/control layer inside Git.
- User originals, raw requirements, sensitive project/customer material, secrets, credentials, private source, and unredacted personal/confidential data default to outside Git.
- Repository may store user-approved decisions, reviewed redacted excerpts, clearly labeled synthetic substitutes, and external pointer/manifests that contain no secrets.
- AI/human restatements are explanatory draft/interpretation layer and must not be treated as original requirements or approved baseline.

## 2. Repository visibility rule

- If visibility is public or unverified, treat storage as public-equivalent / public-risk.
- Only public, synthetic, or explicitly redacted material may be stored.
- Private visibility does not erase Git history risk and does not automatically authorize sensitive originals.

## 3. Authority model

```yaml
authority_layers:
  original_external_source:
    role: evidentiary_authority_outside_git
    git_storage_default: no
  user_approved_decision:
    role: highest_in_repo_target_authority_within_scope
    git_storage_default: yes_if_safe
  ai_or_human_restatement:
    role: explanatory_interpretation
    git_storage_default: yes_if_safe_and_labeled
    cannot_replace_original: true
    cannot_be_approved_baseline_without_user_decision: true
  redacted_excerpt:
    role: reviewed_safe_excerpt
    git_storage_default: yes_if_approved
  synthetic_substitute:
    role: test_or_design_fixture
    git_storage_default: yes_if_labeled
  external_pointer:
    role: non_secret_reference_to_external_source
    git_storage_default: yes_if_safe
```

## 4. Redaction manifest schema

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

## 5. External pointer schema

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
```

## 6. Target workspace placement

- Target-scoped safe user inputs go under `target-projects/<target_project_id>/01-user-input/`.
- `originals/` should store only pointers/README by default; raw originals should remain outside Git.
- `restatements/` stores labeled interpretation, not original truth.
- `decisions/` stores user-approved decisions and authority choices.
- `redactions/` stores redacted/synthetic substitutes and redaction manifests.
- Unsafe originals remain outside the repository.

## 7. Leak / mistaken-storage response

If sensitive material is found in Git or staged for Git:

1. Stop processing.
2. Do not copy it further.
3. Record the risk without repeating the secret/private content.
4. Notify user that Git history exposure may persist.
5. Use a separate incident/remediation workflow if history cleanup is required.
6. Do not rely on ordinary delete/revert as proof of complete removal.

## 8. Open items

- This file is not execution source.
- Broader OP-08 privacy/redaction/access-control remains open until explicitly closed.
- Per-target storage policy still requires user approval.
