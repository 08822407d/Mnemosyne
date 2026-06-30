# Manual Import Artifact Classification v0.1

## Positioning

- Non-execution-source support guidance.
- Used before moving files from `manual-import-inbox/` to canonical paths.
- Does not override `current/human-approved-spec.md`.
- Complements `notes/manual-import-inbox-workflow.md`.

## Classification schema

```yaml
manual_import_artifact_classification:
  artifact_id:
  filename:
  artifact_type: full_report | summary | link_stub | prompt_original | result_record | pro_review_result | synthetic_smoke_test_result | adversarial_test_result | unknown
  full_body_present: yes | no | unknown
  required_sections_present: yes | no | unknown
  download_link_only: yes | no
  transient_or_broken_link_risk: yes | no | unknown
  safety_preflight:
    repository_visibility:
    safe_for_repo_visibility: yes | no | unknown
    contains_secrets_or_credentials:
    contains_personal_or_confidential_data:
    contains_private_source_or_customer_confidential_data:
    contains_target_materials:
  canonical_destination:
  decision: ingest | reject | request_body_chunks | hold_for_user
  rationale:
```

## Rules

- A research report original must be `artifact_type: full_report` and `full_body_present: yes`.
- A summary/link/download-stub must not become a canonical research report original.
- A prompt original must not be stored as a report original.
- A Pro review result must not be stored as a Deep Research report.
- A synthetic smoke-test result must not be stored as a real target dry-run result.
- If classification is uncertain, hold for user instead of guessing.
- Classify before moving; then verify after moving.
