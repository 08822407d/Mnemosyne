# DR6 Follow-Up Work Package Plan

```yaml
created_by_task: MNEMOSYNE-123
authority_level: non_execution_source_candidate_plan
execution_source: current/human-approved-spec.md
```

## Dependency-aware order

### C1 — Artifact delivery and direct generation repair — recommended first

Purpose:

- close the user-facing failure represented by Issues #170 and #171;
- strengthen the existing §13 file-first rule;
- add an explicit same-response generation rule for requested low-risk artifacts;
- add a deterministic response checklist;
- preserve the Deep Research full-report-body exception.

Requires explicit user approval because it may modify `current/human-approved-spec.md`.

### B1 — Provenance and no-write candidate pack

Create non-execution-source templates for:

- surface/plan/Project memory;
- operator-visible model/reasoning labels;
- app/plugin/auth/sync/action state;
- repository authorization scope;
- before/after evidence classes;
- `not_detected` versus mechanically verified levels.

Do not change §19 in this first template task.

### D1 — Surface playbooks

Create one-page candidate playbooks for:

- Chat;
- Project Chat;
- Deep Research;
- Work;
- Agent mode;
- Codex.

Each should state appropriate tasks, context/memory risk, app/action risk, evidence expectations and handoff rules.

### A1 — Targeted live tests

Run only tests whose result changes a pending decision, such as:

- Project Chat versus Deep Research GitHub availability;
- sync versus search/fetch behavior;
- Library interaction with project-only;
- audit-log availability in the user's actual plan/workspace.

Avoid broad exploratory retesting.

### Optional observer-assisted proof

Only if high-assurance combined no-write closure becomes valuable again. It is not the default next task.

## Non-actions

This plan does not authorize execution-source changes, issue closure, live tests, target-project work, or another replay.
