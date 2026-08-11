# Mnemosyne Runtime-Guidance Utilization Review — 2026-08

> Non-execution-source static review. This file evaluates whether current Mnemosyne execution and behavior guidance can be loaded and used proportionately by real conversations/tasks. It does not change `current/human-approved-spec.md`, activate a new loader profile, or authorize external execution.

```yaml
review_id: MNEMOSYNE-RUNTIME-GUIDANCE-UTILIZATION-REVIEW-001
task_id: MNEMOSYNE-199
repository: 08822407d/Mnemosyne
pinned_master: 37a4bb62239c03c0cf42a63386e25079d11b732f
review_date: 2026-08-11
review_type: static_authority_scope_trigger_and_context_burden_review
execution_source_modified: false
active_guidance_modified: false
external_research_executed: false
```

## 1. Review question

The repository now contains a growing execution source and multiple active behavior guards. The central question is not whether these files contain useful rules, but whether a real task can reliably:

1. load the rules it must not miss;
2. avoid loading unrelated route, historical, research and completed-task material;
3. resolve scope and precedence without spending disproportionate context and reasoning effort;
4. expose which rules and source files actually influenced the result;
5. remain usable by both frontier and validated next-tier models.

The review is motivated by Owner feedback that:

- many important Agent-operating ideas are reusable beyond one project;
- complete conversations, research reports and historical task records should normally be preserved but not routinely read;
- long YAML/English-key blocks and verbose explanations impose avoidable human and token burden;
- rules existing in the repository do not guarantee that a working conversation actually loads and uses them.

Owner-source references:

- `https://github.com/08822407d/Mnemosyne/issues/265#issuecomment-5248414221`
- `https://github.com/08822407d/Mnemosyne/issues/265#issuecomment-5248467581`
- `https://github.com/08822407d/Mnemosyne/issues/265#issuecomment-5248547713`
- current maintenance conversation, 2026-08-11

## 2. Inputs reviewed

The current guidance refresh command requires these files for every refresh:

1. `README.md`;
2. `current/human-approved-spec.md`;
3. `current/artifact-delivery-and-direct-generation-guard.md`;
4. `current/cross-conversation-execution-intent-and-operator-flow-guard.md`;
5. `current/external-research-display-name-guard.md`;
6. `current/deep-research-report-delivery-correction-guard.md`;
7. `current/source-artifact-preservation-and-design-rationale-guard.md`;
8. `current/user-operation-next-step-capability-and-intent-guard.md`;
9. `current/frontier-planning-clarification-handoff-adjudication-guard.md`;
10. `current/pr-merge-branch-disposition-guard.md`;
11. `commands/load-mnemosyne-guidance.md`.

For important repository writes it additionally requires:

- `current/run-context-and-pr-provenance-guard.md`.

For branch or PR creation it additionally requires:

- `current/github-single-active-pr-lineage-guard.md`.

The review also used the newly merged source-preservation guard, which establishes `preserve first, read on demand` and classifies complete old conversations, research prompts/reports, historical handoffs and completed-task records as default cold/on-demand sources.

## 3. Cold sources deliberately not read

This review did not read full historical conversations, complete research reports, old handoff packages, completed task records unrelated to the live question, or target-project archives. They were not necessary to determine the current loader structure and guard scopes.

Repository existence was not treated as evidence that those materials influenced this review.

## 4. Verified post-MNEMOSYNE-198 baseline

```yaml
post_merge_verification:
  PR_266:
    state: merged
    merge_commit: 37a4bb62239c03c0cf42a63386e25079d11b732f
  source_preservation_guard_on_master: true
  loader_references_source_preservation_guard: true
  accessible_open_PRs_at_review_start: []
```

The new guard is now active repository guidance. It does not modify the sole execution source.

## 5. Main findings

### F1 — The current loader is safe-oriented but over-broad

The current loader treats eleven files as mandatory before it knows the task type. Several are narrow modules that cannot affect most ordinary tasks:

- display-name allocation matters only for selected external research/workspaces;
- the Deep Research correction matters only for Deep Research delivery;
- branch disposition matters only when asking the user to review/merge a PR or releasing a prior retention obligation;
- source-artifact exactness and detailed rationale apply only to material inputs or important design choices;
- frontier clarification adjudication matters only for material clarification/research-trigger routing.

Loading all of them for every ordinary maintenance explanation, read-only repository check or target-project discussion is disproportionate.

### F2 — `README.md` is navigation, not a stable behavior core

`README.md` contains useful repository identity and safety framing, but it also contains numerous route/status pointers, completed migrations, paused research routes and historical navigation. Loading it on every behavior refresh can consume context and increase the risk that a conversation imports maintenance route state unrelated to its local task.

The loader itself already says guidance refresh must preserve the local mainline and must not import maintenance live routes. Making a route-heavy navigation document mandatory works against that objective.

Recommended classification: `README.md` should be read for repository identity/navigation or when the current task needs a referenced route, not as a universal behavior module.

### F3 — The loader already acts as a compact compiled view

`commands/load-mnemosyne-guidance.md` restates thirty-four high-signal behavior requirements and names the authoritative source/guard for each scope. Requiring every full guard in addition to the condensed loader duplicates a substantial amount of material before any task-specific trigger is known.

The loader is not an execution source and must not become one. However, it can safely act as a compact dispatch/index layer when it requires the full source guard to be loaded whenever a task activates that module.

### F4 — Multiple guards deliberately repeat the same visibility controls

Repeated requirements are often justified repairs, but they increase context and precedence burden when all sources are loaded together.

Examples:

- opening user operation and closing next-step rules appear in the execution source, user-operation guard, clarification adjudication guard and loader;
- external operator-flow visibility appears in the artifact guard, cross-conversation guard and loader;
- branch-retention visibility appears in the PR-disposition guard, PR-lineage guard, cross-conversation guard and loader;
- Deep Research output semantics appear in the execution source and artifact guard but are more specifically corrected by the Deep Research guard;
- model capability and research-need assessment appear in the user-operation guard, clarification guard and loader.

This is not automatically a semantic conflict. It is a utilization problem: a model must identify which text is general, which is a narrow correction and which takes precedence.

### F5 — Repository presence, loading and application are not currently separated in a receipt

Current records may show that a file exists or that the loader names it. They do not uniformly record:

- which core files were actually loaded;
- which task triggers were detected;
- which conditional guards were actually read;
- which cold sources were intentionally excluded;
- which required source was missing or stale;
- which rule caused a stop or escalation.

Without this receipt, later review may incorrectly infer that a repository rule influenced a result merely because the file existed.

### F6 — The sole execution source remains authoritative but is monolithic

`current/human-approved-spec.md` must remain the sole execution source unless the Owner separately changes that architecture. It contains both foundational invariants and increasingly detailed operational rules.

This review does not recommend bypassing it with an unverified digest. Splitting or compiling the execution source would be a later high-impact design decision requiring semantic equivalence review and explicit Owner approval.

Near-term burden reduction should therefore come first from conditional guard loading, not from pretending the execution source can be omitted.

### F7 — The cold-source principle should be extended to guidance modules

MNEMOSYNE-198 correctly separates preservation from routine reading. The same proportionality principle applies to detailed behavior guards:

- a guard may remain active and authoritative for its scope;
- the loader may preserve its core stop/trigger rule;
- the full guard should be read when the scope is activated or when uncertainty exists;
- unrelated narrow guards should not consume every task's working context.

## 6. Candidate classification

### 6.1 Always-loaded core candidate

The safest near-term core is:

- `current/human-approved-spec.md` — sole execution source;
- `commands/load-mnemosyne-guidance.md` — compact dispatch, precedence and trigger summary;
- `current/user-operation-next-step-capability-and-intent-guard.md` — broad reply layout, capability, research and intent behavior used by most substantial work.

This reduces the default set without omitting the broadest operational behavior guard.

### 6.2 Conditional modules

| Module | Load trigger | Full source files |
|---|---|---|
| artifact delivery | downloadable/transfer artifact, long structured output, complete-response transfer | `current/artifact-delivery-and-direct-generation-guard.md` |
| external task flow | another conversation, Codex, Fable, replay, validation or external Agent task is designed/discussed/delivered | `current/cross-conversation-execution-intent-and-operator-flow-guard.md` |
| external research identity | user is asked to create/name a Deep Research, Fable or one-run external workspace | `current/external-research-display-name-guard.md` and registry |
| Deep Research delivery | Deep Research task/report delivery semantics are involved | `current/deep-research-report-delivery-correction-guard.md` |
| source preservation and rationale | material source artifact or important architecture/behavior/schema/migration choice | `current/source-artifact-preservation-and-design-rationale-guard.md` |
| clarification/research routing | material ambiguity, owner decision package, research trigger or next-tier interviewer decision | `current/frontier-planning-clarification-handoff-adjudication-guard.md` |
| repository write provenance | important GitHub/connected-repository write or publication record | `current/run-context-and-pr-provenance-guard.md` |
| branch/PR creation | branch or PR creation/update | `current/github-single-active-pr-lineage-guard.md` |
| PR merge/retention | response asks user to review/merge a PR, or releases a prior retention obligation | `current/pr-merge-branch-disposition-guard.md` |

When several triggers apply, load the union. When scope is uncertain, load the possibly applicable guard before acting rather than assuming it is irrelevant.

### 6.3 Navigation and cold material

Default not loaded merely for behavior refresh:

- `README.md`, unless repository identity/navigation is needed;
- `current/active-context.md`, `handoff/handoff-current.md`, `current/todo.md`, `current/open-questions.md`, unless separately authorized task state/navigation requires them;
- route-specific current/status files unrelated to the local task;
- full research reports, prompts and source conversations;
- historical task results and old handoffs.

## 7. Risk assessment

### Risk of keeping the current all-files loader

- growing context and latency;
- narrow rules distracting from the local task;
- precedence errors between general and specific corrections;
- route contamination through README/status material;
- reduced reliability for next-tier models;
- false confidence that every loaded rule was actually applied.

### Risk of conditional loading

- a trigger may be missed;
- an abbreviated loader statement may omit a material detail;
- a task may under-classify its own risk;
- a stale profile may point to outdated guards.

### Required compensating controls

- trigger table in the loader/profile;
- fail-open-to-more-reading: uncertainty loads the full module;
- exact repository/ref receipt;
- explicit list of loaded modules and cold sources read;
- missing guard blocks the affected external/write/high-impact action;
- static mapping from compact rule to canonical source section;
- comparison against the current full-load baseline before adoption.

## 8. Review verdict

```yaml
review_verdict: REVISE_LOAD_ARCHITECTURE_BEFORE_REAL_USE_SCALE
current_guidance_semantics_rejected: false
current_real_use_blocked: false
recommended_direction: core_plus_triggered_modules
execution_source_split_recommended_now: false
active_loader_change_authorized_by_this_review: false
```

The current guidance set contains valuable controls and may continue to be used. The problem is default loading and observability, not a finding that the rules are generally invalid.

A core-plus-triggered-module candidate should be validated before replacing the current loader behavior. Real-use work need not wait for a perfect guidance compiler, but its task manifests should begin recording what guidance was actually loaded.

## 9. Limitations

- This is a static review, not a measured token/latency experiment.
- It did not test hidden model backends or claim provider-neutral equivalence.
- It did not read every current/status/history file.
- It did not decide whether any individual behavior rule should be removed from Mnemosyne.
- It did not propagate rules into Meta-Agent or a business Agent.
- It did not alter execution source, loader or active guards.
