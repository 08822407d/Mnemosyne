# Memory System Issue Log Template

## Positioning and boundaries

- Current Mnemosyne execution source remains `current/human-approved-spec.md`; this issue-log template is not execution source.
- The target project must eventually have its own execution source.
- The first run is design-only unless separately approved; do not write to the target project.
- Use public / synthetic / explicitly_redacted material by default.
- Do not introduce automation, MCP, RAG, Actions, or multi-agent coordination.
- Template completeness is not success; next-executor usability is part of success.
- Unpromoted D-01-D-07 content is not execution source.
- This template uses DR1 failure-mode vocabulary as diagnostic categories only.

## DR1-derived failure modes

Use one or more values from this list when applicable:

- stale handoff
- wrong source priority
- memory drift
- memory overwrite
- missing critical context
- over-retention
- under-retention
- hallucinated memory
- retrieval failure
- stale tool capability assumption
- implicit automation assumption
- privacy leakage
- handoff/active-context inconsistency
- user decision not propagated
- artifact not actually landable

## Issue entry template

```yaml
issue_id:
dry_run_id:
observed_at:
symptom:
failure_mode:
affected_artifact:
expected_behavior:
actual_behavior:
evidence_paths:
suspected_layer:
root_cause_status:
user_impact:
severity:
repair_candidate:
user_decision_needed:
regression_test:
regression_result:
status:
```
