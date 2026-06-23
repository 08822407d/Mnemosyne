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
- The run must reference `notes/first-target-project-dry-run-manifest-template.md` and a user-approved run manifest before any real target-project dry-run.
- The run must reference `notes/first-target-project-fresh-replay-protocol.md` and the reviewed post-050 replay result.
- Preserve target-specific schema tailoring; do not default target design to Mnemosyne's own schema.

## Verdict rules

- Check result enum for individual checks is `pass | fail | unknown | not_tested | not_applicable`.
- `critical_check := blocking: yes`; `critical_check_definition: blocking_yes`.
- `PASS` requires every `blocking: yes` check to be `pass` with evidence.
- `FAIL` is allowed and useful when issues are evidence-linked.
- `INVALID_RUN` applies when target/input/replay conditions are invalid.
- Do not claim a real dry-run PASS from synthetic smoke-test evidence.

## Result fields

```yaml
dry_run_id:
instrument_set_version:
manifest_path:
manifest_version:
replay_protocol_version:
replay_result_reference:
critical_check_definition: blocking_yes
target:
scope:
inputs:
outputs:
preflight_summary:
checklist_summary:
  pass:
  fail:
  unknown:
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
