# Source Map and On-Demand Reading Plan — OR-02 through OR-09

> Use the smallest sufficient verified working set. Repository existence does not mean a file was loaded or influenced an answer.

```yaml
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-002
reading_policy: package_first_source_on_demand_cold_history_excluded
execution_source: current/human-approved-spec.md
```

## 1. Required reading set

Read from execution-time latest `08822407d/Mnemosyne@master` in this order:

| Order | Path | Role |
|---|---|---|
| 1 | `current/human-approved-spec.md` | sole Mnemosyne execution source and authority boundary |
| 2 | `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.2/README.md` | package identity, purpose, scope, and flow |
| 3 | `.../01-context-and-fixed-boundaries.md` | verified state, fixed OR-01 decisions, terms, and escalation |
| 4 | `.../02-decision-workbook.md` | exact OR-02 through OR-09 questions and options |
| 5 | `.../03-capability-selection-and-qa-guide.md` | primary detailed answer guide |
| 6 | `.../04-next-tier-interviewer-contract.md` | allowed/prohibited behavior and escalation |
| 7 | `.../05-answer-ledger-and-result-template.md` | capture and final result contract |
| 8 | `.../06-source-map-and-on-demand-reading.md` | source and cold-reading boundary |

The interviewer does not need the full Mnemosyne guidance loader solely for this frozen interview. If the task changes into repository writing, external research, target work, activation, private-material intake, or product configuration, stop and load all currently applicable guidance before acting.

## 2. Initial source receipt

Return:

```yaml
owner_review_source_receipt_v2:
  package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-002
  repository: 08822407d/Mnemosyne
  master_commit:
  required_paths_loaded: []
  missing_required_paths: []
  on_demand_paths_loaded_initially: []
  cold_sources_deliberately_not_read: []
  OR_01_status: complete
  execution_source: current/human-approved-spec.md
  repository_write_authorized: false
  Meta_Agent_activation_authorized: false
  private_material_ingestion_authorized: false
  external_research_or_quota_authorized: false
  current_question: OR-02-A
```

A listed repository path that was not read must not be described as evidence used.

## 3. Permitted on-demand sources

Read only when the package guide cannot answer the Owner's specific question accurately.

### Exact capability definition or maturity

```text
notes/reusable-agent-capability-catalog-v0.2.md
```

Use for:

- exact v0.2 wording;
- catalogue status, portability, or selection schema;
- whether an entry is provisional, active-basis, provider-adapter, or retired;
- exact relationship among capabilities.

Freshness note: v0.2 was written before PR #271 activated the periodic branch-retention audit. For current Mnemosyne behavior, `current/pr-merge-branch-disposition-guard.md` controls ACAP-031 status.

### Exact OR-01 Owner amendment

```text
notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-OR-01-RESULT-001.md
```

Use for:

- exact Owner-review disposition;
- whether an item was accepted, amended, provisional, merged, or retired;
- the execution-source terminology agreement;
- checking whether a new answer conflicts with fixed OR-01 decisions.

### Exact first-three-system planner classification

```text
notes/first-three-system-capability-selection-v0.2.md
```

Use for:

- exact required/triggered/experimental/deferred classification;
- target-specific object lists;
- cross-system comparison;
- differences between the Q&A explanation and source candidate.

### Target-local repository/store model

```text
notes/target-local-repository-operating-model-candidate-v0.1.md
```

Use for:

- repository roles;
- primary/secondary cross-repository writes;
- concurrency and serialization;
- bootstrap/cutover/no-dual-writer;
- meta-system pointers and upstream impact.

### Minimum bounded-real-use baseline

```text
notes/minimum-real-use-launch-baseline-candidate-v0.1.md
```

Use for:

- what must exist before first use;
- what is deliberately not a launch prerequisite;
- first task candidates and stop conditions;
- preparation versus activation and pilot requirements;
- model/tool/human split.

Interpret “rollback” in this older file according to OR-01's later controlled-evolution clarification: rollback is one option, not the default evolution model.

### Provider/product catalogue design

```text
notes/provider-product-capability-catalog-candidate-v0.1.md
```

Use only to explain:

- why portable capabilities and provider facts are separate;
- what fields/evidence/freshness a future product record should use;
- which fact categories matter to the first targets;
- official facts versus operator observations versus bounded tests.

It does not establish any current product fact.

### Execution-source terminology

```text
notes/terminology/execution-source-target-truth-and-supporting-memory-v0.1.md
```

Use when the Owner asks for precise distinctions among execution source, target truth, current state, handoff, raw evidence, and backup.

### Current Mnemosyne active guard status

Read only for a specific active-behavior question:

```text
current/source-artifact-preservation-and-design-rationale-guard.md
current/artifact-delivery-and-direct-generation-guard.md
current/pr-merge-branch-disposition-guard.md
current/user-operation-next-step-capability-and-intent-guard.md
current/frontier-planning-clarification-handoff-adjudication-guard.md
```

Examples:

- byte versus substantive-content status;
- “排版不对” repair behavior;
- periodic retained-branch audit;
- current clarification/escalation contract.

### Meta-Agent current truth and state

Read only for exact Meta-Agent authority, blocker, P0, or activation questions:

```text
08822407d/Meta-Agent@master:current/approved-spec.md
08822407d/Meta-Agent@master:current/active-context.md
```

The dedicated Meta-Agent repository controls. Do not use historical Mnemosyne `target-projects/meta-agent/` paths as current truth.

## 4. Sources deliberately excluded by default

Do not read merely because the review occurs in Mnemosyne:

```text
README.md
commands/load-mnemosyne-guidance.md
current/active-context.md
handoff/handoff-current.md
current/todo.md
current/open-questions.md
current/post-interruption-live-wayfinding-status.md
current/review-and-validation-status.md
raw/**
raw/research-reports/**
handoff/** historical or route-specific packages
notes/codex-task-results/** other than a specifically needed result
notes/frontier-clarification-validation-package/**
notes/cross-model-review-results/**
target-projects/meta-agent/** historical bootstrap tree
complete historical conversations
full research reports
old owner-review package v0.1 except for a specific audit
```

Reasons:

- navigation, maintenance routes, historical evidence, cold originals, completed task records, or unrelated paused work are not needed for the frozen choices;
- loading them may import irrelevant mainlines, stale assumptions, or context burden;
- OR-01 and v0.2 sources already synthesize the relevant capability history.

## 5. Cold-source triggers

Complete historical conversations, research reports, old handoffs, and task archives may be read only for a separately selected task such as:

- disputing whether OR-01 or v0.2 distorted original intent;
- auditing a catalogue source;
- evaluating a real handoff;
- designing/validating a migration;
- investigating an incident or contradiction;
- performing a separately authorized longitudinal/full-history review.

The OR-02 through OR-09 owner review is not itself such a trigger.

## 6. On-demand read disclosure

When reading an optional source, say briefly:

> 为回答 OR-XX 的这个问题，我额外读取了 `<path>`；没有读取其他冷历史材料。

Do not repeatedly display Git metadata unless it affects trust or the Owner asks.

## 7. Source precedence and conflict

- If the package conflicts with `current/human-approved-spec.md`, the execution source controls and the affected item is escalated.
- If the package conflicts with fixed OR-01 decisions, stop and request a refreshed Pro adjudication.
- If the workbook differs from catalogue/selection wording, disclose the difference; the Owner chooses the candidate classification.
- If a Meta-Agent summary conflicts with its current dedicated repository, the Meta-Agent repository controls.
- If a target repository later conflicts with a Mnemosyne summary, the target repository controls.
- If current active guard status differs from a stale catalogue maturity note, the current guard controls Mnemosyne behavior; target propagation remains separate.
- If current official product evidence later differs from a provider-catalogue candidate, update the dated provider entry rather than redefining the portable capability.
- If later merged amendments make the package materially stale, stop and request a refreshed package.

## 8. Reading adequacy rule

The package is sufficient when the interviewer can:

- explain every checklist item and option in natural language;
- distinguish stable semantics, provisional mechanisms, target objects, Owner values, external facts, and frontier issues;
- answer item-level questions without invention;
- preserve answer identity and correction;
- identify exactly when another source is needed.

If it cannot, do not compensate by loading the whole repository. Identify the specific gap and read only the relevant authoritative source or return to Pro/frontier.
