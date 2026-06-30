# Synthetic Smoke-Test Result Template

## Positioning

- Non-execution-source support template.
- A synthetic smoke-test is not a real target-project dry-run.
- A synthetic smoke-test may validate template usability and boundary preservation.
- A synthetic smoke-test may not validate real target material flow.
- A synthetic smoke-test may not close the real target-project dry-run gate.
- A synthetic smoke-test may not be reported as real dry-run PASS.

## Minimal fields

```yaml
synthetic_smoke_test_result:
  smoke_test_id:
  run_kind: synthetic_smoke_test
  synthetic_fixture_used: true
  real_target_project: false
  real_target_project_selected: false
  real_target_project_dry_run_started: false
  real_target_project_dry_run_passed: false
  repo_write_performed: false
  target_workspace_created: false
  target_materials_ingested: false
  target_repository_written: false
  smoke_test_verdict: PASS | PASS_WITH_WARNINGS | FAIL | BLOCKED
  synthetic_target_profile:
  planned_paths:
    path_status: planned_path_not_created
  approval_interpretation:
    status: synthetic_fixture_only | draft_only_not_real_approval | not_applicable_synthetic
  evidence_map:
  limitations:
```

## Rules

- Use `smoke_test_verdict`, not `final_verdict`, for synthetic smoke tests.
- Every planned target workspace path must be marked `planned_path_not_created`.
- All real target approval fields must be false, pending, draft, not approved, or not applicable.
- Synthetic fixture authorization is task-local; it does not select a target, approve a workspace, approve target material ingestion, or approve target repository write.
- `may_be_reported_as_real_dry_run_PASS: false` is mandatory for synthetic smoke-test reporting.
- If a synthetic result is later persisted, it must be under review/result evidence paths, not under a real target dry-run path.
