# First Target-Project Dry-Run Result Template

## Positioning and boundaries

- Current Mnemosyne execution source remains `current/human-approved-spec.md`; this result template is not execution source.
- The target project must eventually have its own execution source.
- The first run is design-only unless separately approved; do not write to the target project.
- Use public / synthetic / explicitly_redacted material by default.
- Do not introduce automation, MCP, RAG, Actions, or multi-agent coordination.
- Template completeness is not success; next-executor usability is part of success.
- Unpromoted D-01-D-07 content is not execution source.
- This template records evidence from a run; it does not itself prove a real target-project dry-run occurred.
- A synthetic smoke test must not be reported as a real target-project dry-run.

## Verdict rules

- `PASS` requires all critical checks to pass with evidence.
- `FAIL` is allowed and useful when issues are evidence-linked.
- `INVALID_RUN` applies when target/input/replay conditions are invalid.
- Do not claim a real dry-run PASS from synthetic smoke-test evidence.

## Result fields

```yaml
dry_run_id:
instrument_set_version:
target:
scope:
inputs:
outputs:
preflight_summary:
checklist_summary:
  pass:
  fail:
  not_tested:
  not_applicable:
source_priority_conflicts:
drift_review_summary:
handoff_replay_summary:
triage_summary:
issues_found:
invalid_run_reasons:
containment_actions:
what_worked:
what_failed:
root_cause_summary:
schema_tailoring_result:
unnecessary_file_roles_found:
ordinary_thinking_model_handoff_result:
must_fix_before_next_run:
can_defer:
Codex_task_candidates:
user_decisions_needed:
final_verdict: PASS | FAIL | INVALID_RUN
```
