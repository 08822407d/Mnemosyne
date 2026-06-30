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

## 9. MNEMOSYNE-063 deterministic pre-target controls

### Redacted excerpt storage gate

Any redacted excerpt stored in Git requires a paired redaction manifest. Missing manifest blocks ingestion and blocks real target dry-run use. The manifest should record source item id, original storage status, redacted file path, redaction method, removed categories, reviewer, user approval, residual risk, and Git history exposure acknowledgement. This section corresponds to `redacted_excerpt_storage_gate` in the first-target run manifest.

### External pointer safety gate

External pointers must not contain secrets, credentials, access tokens, signed URLs, private absolute paths, sensitive precise locations, customer/confidential names unless approved, or personal data unless approved and safe. Missing pointer safety flags block Git storage, ingestion, and real target dry-run use. This section corresponds to `external_pointer_safety_gate` in the first-target run manifest.

### `originals/` pointer-only default

`originals/` remains pointer/README-only by default. Raw originals and raw requirements stay outside Git unless repository visibility, safety, explicit user approval, Git history exposure, owner/authority, allowed use, and retention are all recorded.

### Restatement authority boundary

AI/human restatements are explanatory interpretation only. They are not original requirements and not an approved baseline unless separately approved in a decision record.

### Target-specific lesson candidates

A target-specific `lesson_candidate` is non-execution-source by default. It must stay target-project-specific and requires candidate review, scope analysis, sensitivity review, and user approval before any global Mnemosyne promotion.
