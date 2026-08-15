# 2026-08 Urgent Research and Validation Roadmap — Candidate v0.1

> Non-execution-source roadmap for Issue #265 TODOs 1, 3 and 4 after the minimum real-use/capability-catalogue work. It prepares priorities and validation structure but does not launch Fable, Deep Research, Claude, GPT or handoff archive evaluation, consume quota, create Projects, or authorize external execution.

```yaml
roadmap_id: MNEMOSYNE-URGENT-RESEARCH-VALIDATION-ROADMAP-001
task_id: MNEMOSYNE-200
status: candidate_preparation_only
execution_disposition: DO_NOT_RUN
external_execution_or_quota_authorized: false
execution_source_modified: false
```

## 1. Shared principle

Use the strongest open-ended reasoning condition for unresolved architecture, problem reconstruction, methodology promotion and severe failures. Use next-tier models only on frozen, self-contained tasks with exact boundaries, checks and escalation. Use mechanical tools for identity, path, schema, diff and test evidence.

The three workstreams below share source artifacts and should not be designed as independent abstract campaigns:

- the reusable capability catalogue supplies frozen Agent behaviors;
- the first three target packages supply real task contexts;
- the runtime-guidance candidate supplies a context/load-profile comparison;
- complete conversation exports supply cold evidence for handoff evaluation;
- provider/product records capture current execution conditions without claiming hidden backend identity.

## 2. Fable independent research priorities

### Priority F1 — Ownership and lifecycle of reusable Agent capabilities

**Question:** How should Mnemosyne, Meta-Agent and target repositories divide ownership of reusable Agent capability definitions, design methodology, source evidence, provider adapters and target selections without creating competing truth sources?

Why this is open:

- Mnemosyne already owns persistent-memory design/evidence and many reusable guards;
- Meta-Agent already owns an accepted but incomplete general Agent-design methodology;
- target systems need local capability selections and adaptations;
- a shared common library could reduce duplication but may create another authority layer.

Decision it should change:

- canonical home of capability definitions;
- promotion and versioning workflow;
- impact tracking for existing targets;
- which records each repository retains.

Distinct Fable role:

- independently reconstruct the problem;
- propose competing ownership architectures;
- identify failure modes and migration consequences;
- challenge the candidate catalogue and target-local operating model without treating them as accepted premises.

Run timing: after the first catalogue/matrix is merged and before promoting it into Meta-Agent or an execution source.

### Priority F2 — Cross-repository target work and safe concurrency

**Question:** What is the minimum governance and validation needed for one Agent/conversation to design/build in target repositories while writing only bounded evidence or methodology feedback to Mnemosyne/Meta-Agent, and for independent target projects to proceed concurrently?

Decision it should change:

- whether the target-local operating model can become a standard default;
- which cross-repository operations require serialization;
- what evidence proves no dual writer and correct action order;
- how to distinguish shared-library conflicts from independent target work.

Distinct Fable role:

- adversarially test the current candidate against races, stale refs, partial failure, privacy and rollback;
- compare simple task-local manifests with heavier orchestration alternatives;
- identify what should remain unautomated.

Run timing: after a small public/synthetic cross-repository behavior test or in parallel with its result review, not before the exact candidate is frozen.

### Priority F3 — Portable Agent capabilities versus provider-specific Skills/instructions

**Question:** How should portable Agent capability semantics be mapped to current provider mechanisms such as Skills, project instructions, system prompts, commands, tools and repository files, while preserving behavior across providers and avoiding false equivalence?

Decision it should change:

- provider adapter schema;
- what belongs in the portable catalogue;
- which Skills/product facts require separate current evidence;
- how target packages are versioned and validated across providers.

Distinct Fable role:

- current official product research plus alternative adapter designs;
- identify platform lock-in, injection, context and update risks;
- propose tests of semantic consistency rather than identical prompt text.

Run timing: only after one of the first targets selects a likely product surface, so the research changes a concrete packaging decision.

### Priority F4 — Upstream capability changes and deployed-target impact

**Question:** How should changes to Mnemosyne memory capabilities or Meta-Agent methods identify, assess and migrate affected existing target systems and completed work without automatic unsafe propagation?

Decision it should change:

- target selection/version records;
- impact registry and review triggers;
- preserve/transform/recompute/retire categories;
- human approval and rollback boundaries.

Distinct Fable role:

- challenge candidate impact semantics using realistic split/merge/retire cases;
- compare simple indexed selection records with heavier dependency graph designs;
- identify when completed artifacts require re-evaluation rather than data migration.

Run timing: after at least two target systems have actual capability selections; otherwise the task remains too abstract.

### Fable ordering recommendation

1. F1 first, because ownership affects all later common-library work.
2. F2 after the first cross-repository test package is frozen.
3. F3 when a real provider packaging choice is imminent.
4. F4 after actual target selections exist.

No Fable run is selected or authorized by this roadmap. The indefinitely paused FCV/A1/A2/V0–V3 route remains separate and is not resumed.

## 3. Next-tier and cross-provider reliability validation

### 3.1 Objective

Evaluate whether user-labelled next-tier conditions such as GPT-5.6 Sol and Claude Opus 5 can reliably execute frozen, relatively mechanical work produced by frontier planning, and whether key semantics remain consistent across providers.

The names are user planning labels. At execution time record the exact visible product/surface selection and current official facts; do not infer hidden backend identity.

### 3.2 Efficient first batch

Combine the first next-tier reliability batch with the PR #267 runtime-guidance profile validation instead of creating a separate synthetic campaign.

Conditions:

- current full-load guidance baseline;
- candidate core plus triggered modules;
- each available next-tier provider/model condition;
- a frontier reference/adjudication condition for disputed cases, not as an automatic truth source.

### 3.3 Candidate task families

1. **Frozen extraction** — extract source, requirement, rationale and unknowns into a specified record without changing meaning.
2. **Bounded current-state update** — update current state/handoff from a frozen event set and avoid importing unrelated route history.
3. **Exact file repair** — make a low-risk specified documentation change with path allowlist and mechanical diff checks.
4. **Missing-authority stop** — detect a requested write or truth change that lacks task-local authority.
5. **Stale/conflicting input** — detect inconsistent current refs and escalate instead of guessing.
6. **Capability selection application** — instantiate a frozen subset from the Agent capability catalogue without copying all capabilities or inventing target requirements.
7. **Provider adapter separation** — keep portable capability semantics separate from a supplied product-specific packaging contract.
8. **Cross-repository action plan** — produce ordered per-repository action contexts without performing writes.
9. **Handoff receive** — recover target truth/current stage from allowed inputs and state missing material.
10. **Negative case** — refuse to promote one target outcome into general methodology automatically.

### 3.4 Evaluation dimensions

- semantic correctness;
- exact scope/path/action adherence;
- truth-source and authority recovery;
- source/candidate/decision/current-state separation;
- unknown and conflict handling;
- correct stop/escalation;
- acceptance-criteria coverage;
- fabricated fact, permission, file or result rate;
- unnecessary module/cold-source loading;
- user-facing readability and YAML/terminology burden;
- mechanical verifiability;
- human review time and rework;
- cost, latency and quota observations when available;
- consistency of critical behavior across providers.

Output style differences are not failures unless they change meaning, burden or required operations.

### 3.5 Pass boundary

A next-tier condition is a candidate for a task class only when:

- no critical authority, privacy, source or fabricated-action failure occurs;
- semantic result is correct or safely escalated;
- mechanical checks pass where applicable;
- human rework is materially lower than redoing the task with frontier reasoning;
- repeated cases show stable boundary adherence.

One successful run is not a permanent model assignment.

### 3.6 Execution boundary

This roadmap does not authorize any model run. Before execution, freeze taskbooks, provider/surface observations, contamination rules, return artifacts, scoring, quota and user authorization.

## 4. Real handoff archive evaluation

### 4.1 Objective

Evaluate whether Mnemosyne’s actual old-to-new conversation handoffs preserved the work mainline, authority, decisions, unknowns and safe continuation—not merely whether a frontier reviewer can reconstruct the truth afterward from the complete archive.

### 4.2 Evidence package per handoff

- exact or identified export of the pre-handoff conversation;
- handoff package/startup prompt used at the time;
- repository truth/current files available at receive time;
- exact or identified export of the receiving conversation;
- actual repository/result outcome;
- user corrections and later incident/repair records;
- preservation level and privacy authorization for each source.

Complete conversations are cold evaluation evidence, not ordinary runtime input.

### 4.3 Three separate judgments

1. **Handoff sufficiency:** Using only the handoff and inputs the receiving conversation was supposed to read, can a qualified fresh Agent recover the correct target, authority, current stage, boundaries and safe next action?
2. **Actual receiver performance:** What did the real receiving conversation load, infer, omit or incorrectly import, and what outcome followed?
3. **Archive audit:** With the complete pre/post archive, what handoff defects, receiver errors, stale repository state or user-operation problems can a frontier reviewer identify?

Do not treat success in judgment 3 as proof of judgment 1.

### 4.4 Sampling

Choose several real work lines with variety:

- a clean successful handoff;
- a handoff with stale current state;
- a route-contamination or wrong-mainline risk;
- a repository-write/PR lineage transition;
- a long research or Meta-Agent transition;
- at least one case with an explicit user correction.

Do not sample only cases already known to pass.

### 4.5 Evaluation dimensions

- target identity and purpose recovery;
- sole truth source and authority;
- fixed decisions versus open questions;
- completed/pending/blocked/superseded state;
- exact safe next action;
- prohibited action and authorization retention;
- dependency completeness;
- stale or historical route resurrection;
- unrelated context contamination;
- user correction preservation;
- unnecessary repeated reading/context cost;
- actual downstream correctness and rework;
- defect attribution: handoff artifact, receiver, repository live state, product surface, or user operation.

### 4.6 Output

- case inventory and source identities;
- per-case sufficiency/receiver/archive verdicts;
- severity and defect taxonomy;
- effective and ineffective handoff fields/rules;
- unnecessary material and context burden;
- concrete revisions and regression cases;
- confidence on whether current handoff is a stable long-term capability;
- minimum additional evidence if confidence is insufficient.

### 4.7 Privacy and execution boundary

Conversation exports may contain personal, private or repository-sensitive material. Keep exact originals outside public Git unless separately approved; store only safe identities, pointers or redacted evidence in the public repository. No archive review is authorized by this roadmap.

## 5. Shared artifact and review strategy

- Use one canonical task package per run, with exact identity and return route.
- Preserve full task/report/conversation exports at an honest preservation level.
- Keep hidden answer keys separate from workers when controlled testing needs them.
- Use mechanical checks for files, IDs, paths and hashes; use frontier review for semantic/high-impact adjudication.
- Record which guidance/cold sources each executor actually read.
- Preserve failures and contradictory results.
- Do not automatically update execution sources or target truth from a validation result.

## 6. Immediate next preparation after this roadmap

After the capability catalogue and first-three-system selection are reviewed:

1. freeze a small target-local repository validation package;
2. select the first actual target repositories/stores and storage boundaries;
3. derive the first minimum real-use taskbooks;
4. then freeze the next-tier comparison and handoff archive sample manifests;
5. prepare Fable F1 only when the catalogue/ownership problem is stable enough for independent research.

## 7. Design rationale

A single coordinated roadmap was selected instead of three disconnected campaigns. The same target packages and capability catalogue should generate real-use tasks, next-tier validation cases, handoff evidence and Fable research questions. This reduces duplicate design and keeps the urgent week focused on systems that can be used afterward.
