# First Real Target Dry-run Postmortem Template

```yaml
first_target_dry_run_postmortem:
  dry_run_id:
  target_project_id:
  run_kind: real_target_project
  target_repository_write_performed: false
  target_materials_ingested:
  materials_safety_status:
  verdict:
  score:
  critical_blockers:
  what_worked:
  what_failed:
  unsupported_assumptions_found:
  stale_context_found:
  authority_conflicts_found:
  user_input_storage_issues:
  handoff_continuity_issues:
  delivery_package_issues:
  target_specific_lessons:
  mnemosyne_global_lesson_candidates:
  required_repairs:
  user_decisions_needed:
  evidence_paths:
  follow_up_tasks:
  regression_candidates:
```

Each real dry-run postmortem should include at least one `required_repairs` item or explicitly say none with evidence. If any issue was found, include at least one `follow_up_task` or `regression_candidate`. Target-specific lessons remain target-specific unless later candidate review and user approval promote them.
