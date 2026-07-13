# Meta-Agent Controlled Dry-Run Formal Regression Records

```yaml
created_by_task: MNEMOSYNE-115
latest_update_task: MNEMOSYNE-116
record_set_status: first_batch_formalized_definition_replay_PASS_fresh_behavioral_replay_prepared
fresh_behavioral_replay_status: not_yet_executed
fresh_replay_package: handoff/meta-agent-five-regression-fresh-replay-package.md
fresh_replay_startup_prompt: handoff/meta-agent-five-regression-fresh-replay-startup-prompt.md
authority_level: non_execution_source_target_specific_test_assets
source_event: META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001
execution_source: current/human-approved-spec.md
global_rule_promotion: false
target_workspace: false
```

## Positioning

This directory stores formal regression **specifications** derived from the Meta-Agent controlled no-target-write dry run. They are Mnemosyne test assets, not Meta-Agent product files, not a target workspace, and not execution source.

Formalization means that each selected candidate now has a stable input package, expected recovery, forbidden claims, deterministic checks, judge checks, evidence paths, and result semantics. It does not authorize target workspace creation, target material ingestion, target repository write, operational build, automatic execution, or global rule promotion.

## First formalized batch

| Test ID | Topic | Definition replay | Scope |
|---|---|---|---|
| `REG-META-DRYRUN-001` | approval-chain recovery | PASS | target-specific, with possible later generalization only after further evidence and user approval |
| `REG-META-DRYRUN-002` | mechanical no-write proof or explicit run-scoped exception | PASS | Mnemosyne-wide candidate, not execution source |
| `REG-META-DRYRUN-004` | target runtime truth-source non-invention | PASS | target-specific / partly generalizable |
| `REG-META-DRYRUN-005` | non-execution-source contamination | PASS | Mnemosyne-wide candidate, not execution source |
| `REG-META-DRYRUN-007` | PASS semantics | PASS | Mnemosyne-wide candidate, not execution source |

## Deferred candidates

- `REG-META-DRYRUN-003` remains conditional on a future explicitly approved material phase.
- `REG-META-DRYRUN-006` remains deferred until more real Meta-Agent feedback exists.

## Definition replay

The recorded `definition_replay_result` validates each specification against repository evidence at `master@6d6d525a688a62d73665ff2062ac03292af53833`. It is not a fresh-session behavioral replay.

## Prepared fresh-session behavioral replay

MNEMOSYNE-116 prepares, but does not execute, the isolated replay:

- package: `handoff/meta-agent-five-regression-fresh-replay-package.md`;
- startup prompt: `handoff/meta-agent-five-regression-fresh-replay-startup-prompt.md`.

The tested conversation must be genuinely new, load Mnemosyne guidance explicitly, pin the repository ref before substantive reading, remain read-only, provide mechanical before/after repository-state evidence, and return its complete executor output for separate maintainer scorecard review.

A result from the current maintenance conversation cannot satisfy the fresh-session independence requirement.