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

## Mnemosyne-specific supplemental diagnostic modes

These supplemental modes are Mnemosyne-specific diagnostics, not direct DR1-derived findings:

- template maximalism / schema overfit
- unnecessary file-role proliferation

## Issue entry template

```yaml
issue_id:
dry_run_id:
observed_at:
symptom:
failure_mode:
failed_check_ids:
affected_artifact:
expected_behavior:
actual_behavior:
evidence_paths:
suspected_layer: input | write | manage | read | handoff | delivery | governance | unknown
confirmed_faulty_layer: input | write | manage | read | handoff | delivery | governance | not_confirmed
root_cause_status: confirmed | suspected | unknown
blocking: yes | no
user_impact:
severity: P0 | P1 | P2
containment_action:
repair_candidate:
user_decision_needed:
reproduction_status: reproducible | not_reproduced | unknown
reproduction_steps:
regression_test:
regression_result:
route: codex_fix | user_clarification | open_question | candidate | capability_check | defer
next_action:
owner:
status: open | contained | fixed_pending_regression | closed | deferred
```

## Layer and status rules

- `suspected_layer` may be populated before root cause confirmation.
- `confirmed_faulty_layer` may only name a layer when `root_cause_status: confirmed` and evidence paths support it.
- Otherwise set `confirmed_faulty_layer: not_confirmed`.
- P0 requires containment.
- `closed` requires regression result.
- Do not claim confirmed root cause from plausibility alone.

## Failure conditions

An issue record fails review if:

- no evidence path is provided;
- symptom is treated as confirmed root cause without evidence;
- P0 has no containment action;
- the issue is closed without a regression result;
- execution-source repair is proposed without separate user approval.
