# Source Map and On-Demand Reading Plan

> The next-tier interview should use the smallest sufficient verified working set. Repository existence does not mean a file was loaded or influenced the answer.

```yaml
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-001
reading_policy: package_first_source_on_demand_cold_history_excluded
execution_source: current/human-approved-spec.md
```

## 1. Required reading set

Read these files from execution-time latest `08822407d/Mnemosyne@master`, in order:

| Order | Path | Role |
|---|---|---|
| 1 | `current/human-approved-spec.md` | sole Mnemosyne execution source and authority boundary |
| 2 | `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.1/README.md` | package identity, purpose, scope, and flow |
| 3 | `.../01-context-and-fixed-boundaries.md` | verified state, fixed Owner inputs, terms, and uncertainty routes |
| 4 | `.../02-decision-workbook.md` | exact contextualized questions, options, recommendations, and escalation |
| 5 | `.../03-capability-and-qa-reference.md` | primary explanation/FAQ reference |
| 6 | `.../04-next-tier-interviewer-contract.md` | allowed/prohibited behavior and escalation |
| 7 | `.../05-answer-ledger-and-result-template.md` | answer capture and final result contract |
| 8 | `.../06-source-map-and-on-demand-reading.md` | source and cold-reading boundary |

The interviewer does **not** need to run the full `Load Mnemosyne guidance` command merely to conduct this frozen owner-review package. The relevant rules are captured by the execution source and self-contained package. If the interaction later changes into repository writing, external research, target work, or another task class, stop and load the then-applicable current guidance before acting.

## 2. Permitted on-demand source files

Read only when a specific Owner question cannot be answered accurately from the package.

### Exact capability definition, basis, or portability

```text
notes/reusable-agent-capability-catalog-v0.1.md
```

Use when the Owner asks:

- the exact current catalogue wording;
- whether an entry is active, accepted Meta-Agent method, candidate, or research-needed;
- why two entries are separate;
- portability/generalization rules.

### Exact original three-system classification

```text
notes/first-three-system-capability-selection-v0.1.md
```

Use when the Owner asks:

- how PR #268 originally classified an item;
- whether the planner's revised workbook recommendation differs from the source candidate;
- target-specific functions and cross-system comparison.

### Target-local repository/store model

```text
notes/target-local-repository-operating-model-candidate-v0.1.md
```

Use when the Owner asks:

- what each repository should retain;
- how primary/secondary cross-repository writes work;
- concurrency and serialization;
- no-dual-writer, bootstrap, cutover, or upstream impact.

### Minimum real-use launch baseline

```text
notes/minimum-real-use-launch-baseline-candidate-v0.1.md
```

Use when the Owner asks:

- what must exist before first bounded use;
- what is deliberately not a launch prerequisite;
- first task candidates, stop conditions, or model/tool split.

### Provider/product catalogue design

```text
notes/provider-product-capability-catalog-candidate-v0.1.md
```

Use only to explain:

- why portable capabilities and provider facts are separate;
- what fields/evidence/freshness a future catalogue should use;
- how current facts should be routed.

It does **not** establish current product facts.

### Meta-Agent current accepted status

Read only if the Owner asks for exact current Meta-Agent authority/status:

```text
08822407d/Meta-Agent@master:current/approved-spec.md
08822407d/Meta-Agent@master:current/active-context.md
```

Use the Meta-Agent repository as the authority. Do not use historical Mnemosyne `target-projects/meta-agent/` paths as current truth.

### Existing Mnemosyne clarification/guidance source

Read only if the package contract appears ambiguous or the interviewer must verify a specific process rule:

```text
current/user-operation-next-step-capability-and-intent-guard.md
current/frontier-planning-clarification-handoff-adjudication-guard.md
current/source-artifact-preservation-and-design-rationale-guard.md
```

If the question becomes a different task class, stop and load all applicable current guidance under `commands/load-mnemosyne-guidance.md` before acting.

## 3. Files deliberately excluded from default reading

Do not read these merely because the review occurs in Mnemosyne:

```text
README.md
current/active-context.md
handoff/handoff-current.md
current/todo.md
current/open-questions.md
current/post-interruption-live-wayfinding-status.md
current/review-and-validation-status.md
notes/codex-task-results/** other than a specifically needed result
raw/research-reports/**
raw/** complete source archives
handoff/** historical or route-specific packages
notes/frontier-clarification-validation-package/**
target-projects/meta-agent/** historical bootstrap tree
```

Reason:

- they are navigation, current route, historical evidence, completed-task records, research, cold originals, or unrelated paused-route material;
- they are not needed to answer the frozen Owner questions;
- loading them may import irrelevant mainlines and increase context burden.

## 4. Cold-source triggers

Complete historical conversations, research reports, old handoffs, and task archives may be read only if the Owner separately selects one of these tasks:

- reconstruct original intent disputed by the package/source files;
- audit whether the capability catalogue distorted a source;
- evaluate an actual cross-conversation handoff;
- design/validate a migration;
- investigate an incident or contradiction;
- perform a separately authorized longitudinal/full-history review.

The current owner-review is not such a trigger.

## 5. Source receipt required from the interviewer

At receive time, report:

```yaml
owner_review_source_receipt:
  package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-001
  repository: 08822407d/Mnemosyne
  master_commit:
  required_paths_loaded: []
  missing_required_paths: []
  on_demand_paths_loaded_initially: []
  cold_sources_deliberately_not_read: []
  execution_source: current/human-approved-spec.md
  repository_write_authorized: false
  external_research_or_quota_authorized: false
  current_question: OR-01
```

A path listed in the repository but not loaded must not be described as evidence used by the interviewer.

## 6. On-demand read disclosure

When the interviewer reads an optional source, state briefly:

```text
为回答 OR-XX 的这个问题，我额外读取了 `<path>` 的相关部分；没有读取其他历史材料。
```

Do not repeatedly display machine metadata unless it affects trust or the Owner asks.

## 7. Source conflict rule

If:

- this package conflicts with `current/human-approved-spec.md`, the execution source controls and the affected question is escalated;
- the workbook recommendation differs from the PR #268 source candidate, disclose the difference and ask the Owner which classification to adopt;
- a target-source fact conflicts with a Mnemosyne summary, the current target repository controls;
- current official product evidence later conflicts with the provider catalogue candidate, update the dated provider entry rather than redefining the portable capability;
- the package is stale relative to a later merged amendment, stop and request a refreshed package or frontier adjudication.

## 8. Reading adequacy rule

The package is sufficient when the interviewer can:

- explain every question and option;
- distinguish fixed facts, recommendations, Owner preferences, external facts, and frontier issues;
- answer capability questions without invention;
- preserve answer identity and corrections;
- identify when more source is genuinely needed.

If it cannot, do not compensate by indiscriminately reading the whole repository. Identify the specific gap and load only the relevant authoritative source or return to frontier review.
