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

## Result scale

`result` must be one of: `pass/fail/not_tested/not_applicable`.

## Checklist rows

```yaml
- check_id: DRYRUN-CHECK-01-execution-source-read
  result: not_tested
  evidence_path:
  finding: "Execution source was actually read and preferred over summaries, candidates, and stale notes."
  severity: high
  next_action:

- check_id: DRYRUN-CHECK-02-ordinary-thinking-handoff
  result: not_tested
  evidence_path:
  finding: "Handoff can be executed by a fresh ordinary Thinking-model session without hidden context."
  severity: high
  next_action:

- check_id: DRYRUN-CHECK-03-decision-propagation
  result: not_tested
  evidence_path:
  finding: "Active decisions propagate to current context and handoff without creating execution-source claims."
  severity: high
  next_action:

- check_id: DRYRUN-CHECK-04-layer-separation
  result: not_tested
  evidence_path:
  finding: "Raw, evidence, candidate, decision, and execution layers remain distinct."
  severity: high
  next_action:

- check_id: DRYRUN-CHECK-05-stale-conflict-surfaced
  result: not_tested
  evidence_path:
  finding: "Stale or conflicting information is surfaced with source priority instead of silently merged."
  severity: medium
  next_action:

- check_id: DRYRUN-CHECK-06-unknowns-not-invented
  result: not_tested
  evidence_path:
  finding: "Unknowns are marked rather than invented."
  severity: high
  next_action:

- check_id: DRYRUN-CHECK-07-capability-assumptions
  result: not_tested
  evidence_path:
  finding: "Tool/platform capability assumptions are verified or marked unverified."
  severity: high
  next_action:

- check_id: DRYRUN-CHECK-08-public-safe-boundary
  result: not_tested
  evidence_path:
  finding: "Repository visibility and public-safe input boundary are respected."
  severity: high
  next_action:

- check_id: DRYRUN-CHECK-09-next-executor-usability
  result: not_tested
  evidence_path:
  finding: "Output artifacts are usable by a next executor, not merely complete-looking."
  severity: high
  next_action:

- check_id: DRYRUN-CHECK-10-design-only-no-target-write
  result: not_tested
  evidence_path:
  finding: "Design-only/no-target-write boundary is respected."
  severity: high
  next_action:

- check_id: DRYRUN-CHECK-11-unsupported-assumptions-complete
  result: not_tested
  evidence_path:
  finding: "Unsupported assumptions are complete enough for user review."
  severity: medium
  next_action:

- check_id: DRYRUN-CHECK-12-criteria-evaluated
  result: not_tested
  evidence_path:
  finding: "Acceptance and failure criteria are explicitly evaluated."
  severity: high
  next_action:
```
