# First Target-Project Dry-Run Checklist

## Positioning and boundaries

- Current Mnemosyne execution source remains `current/human-approved-spec.md`; this checklist is not execution source.
- The target project must eventually have its own execution source.
- The first run is design-only unless separately approved; do not write to the target project.
- Use public / synthetic / explicitly_redacted material by default.
- Do not introduce automation, MCP, RAG, Actions, or multi-agent coordination.
- Template completeness is not success; next-executor usability is part of success.
- Unpromoted D-01-D-07 content is not execution source.
- Use this checklist as a small DR1-derived instrument; reference template packs rather than duplicating them.

## Result scale and PASS gate

`result` must be one of: `pass | fail | unknown | not_tested | not_applicable`.

Definitions:

- `pass`: evidence proves expected behavior.
- `fail`: evidence proves a violation.
- `unknown`: the check was attempted, but available evidence is insufficient or ambiguous.
- `not_tested`: the check was not attempted.
- `not_applicable`: outside the approved bounded scope, with a recorded rationale.

Mechanical rule: `critical_check := blocking: yes`.

Overall dry-run `PASS` requires every `blocking: yes` check to be `pass`. `severity` describes impact and does not define criticality. `unknown`, `not_tested`, or `fail` on `blocking: yes` prevents PASS. `not_applicable` on a blocking check prevents PASS unless the user-approved scope explicitly reclassifies that row to `blocking: no`, with rationale. Replay verdict is separate and remains `PASS | FAIL | BLOCKED`.

## Checklist rows

```yaml
- check_id: DRYRUN-PREFLIGHT-01-target-owner-scope
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Target project, owner, and bounded scope are explicit."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-PREFLIGHT-02-input-safety-approval
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Input materials are safe and user-approved for the current repository visibility/use."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-PREFLIGHT-03-target-source-map-authority
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Target source map and authority are explicit before design work begins."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-PREFLIGHT-04-stale-conflict-challenge
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "At least one stale/conflict challenge exists, or a synthetic challenge is explicitly marked `test_fixture_not_target_truth`."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-CHECK-01-execution-source-read
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Execution source was actually read and preferred over summaries, candidates, and stale notes."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-CHECK-02-ordinary-thinking-handoff
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Handoff can be executed by a fresh ordinary Thinking-model session without hidden context."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-CHECK-03-decision-propagation
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Active decisions propagate to current context and handoff without creating execution-source claims."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-CHECK-04-layer-separation
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Raw, evidence, candidate, decision, and execution layers remain distinct."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-CHECK-05-stale-conflict-surfaced
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Stale or conflicting information is surfaced with source priority instead of silently merged."
  severity: medium
  blocking: yes
  next_action:

- check_id: DRYRUN-CHECK-06-unknowns-not-invented
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Unknowns are marked rather than invented."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-CHECK-07-capability-assumptions
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Tool/platform capability assumptions are verified or marked unverified."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-CHECK-08-public-safe-boundary
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Repository visibility and public-safe input boundary are respected."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-CHECK-09-next-executor-usability
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Output artifacts are usable by a next executor, not merely complete-looking."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-CHECK-10-design-only-no-target-write
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Design-only/no-target-write boundary is respected."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-CHECK-11-unsupported-assumptions-complete
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Unsupported assumptions are complete enough for user review."
  severity: medium
  blocking: no
  next_action:

- check_id: DRYRUN-CHECK-12-criteria-evaluated
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Acceptance and failure criteria are explicitly evaluated."
  severity: high
  blocking: yes
  next_action:

- check_id: DRYRUN-CHECK-13-target-schema-tailoring
  result: not_tested
  evidence_path:
  result_rationale:
  finding: "Target schema was tailored to the target project: only 3 to 7 necessary core files/roles were selected, Mnemosyne's own directory layout was not copied without justification, and each selected file has clear authority and update responsibility."
  severity: high
  blocking: yes
  next_action:
```
