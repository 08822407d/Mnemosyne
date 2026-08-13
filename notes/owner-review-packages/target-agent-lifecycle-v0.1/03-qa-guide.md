# Target-Lifecycle Capability and Q&A Guide

> Primary answer source for the next-tier interviewer. Explain in natural Chinese. Do not make the Owner decode English schemas or repository jargon.

```yaml
package_id: MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001
question_range: TLR-01_through_TLR-05
```

## 1. General explanation pattern

For every question, explain:

1. what problem the rule solves;
2. the smallest practical first implementation;
3. what is already fixed and not being reopened;
4. the strongest advantage;
5. the strongest risk or burden;
6. what happens if the Owner defers;
7. what would require Pro/frontier re-entry.

Do not present a recommendation as a fact or as a preselected answer.

## 2. Key terms in ordinary language

### Physical repository

The Git repository or other versioned storage container. One physical repository may hold several logical Agents.

### Logical Agent root

The clearly bounded part of that repository that belongs to one Agent. It contains or points to that Agent's current truth, state, instructions, and records.

### Authority owner

The person/system whose approved source decides what is current for that Agent. This is not the same as whichever model performs one write task.

### Task writer

The actor allowed to make a bounded change under one task authorization. It does not become an independent authority owner merely because it can write files.

### Write set

The exact files, directories, or logical objects one task may modify.

### Shared object

An object intentionally used by several Agents, such as common code or a shared schema. Merely being readable by several Agents does not make an object shared.

### Consumer-owned dependency declaration

Each project records which library/shared object and version it uses. The consumer owns this fact because it is part of that project's truth.

### Derived impact view

A list generated from consumer declarations to help identify affected projects. It is a convenience view, not a second truth source.

### Primary change axis

The main type of thing directly changed: Agent internals, business requirement, API, provider adapter, or physical container.

### Secondary effect

A separately justified consequence on another axis. It is not assumed automatically.

### Parent-owned design brief

A bounded record that Mnemosyne or Meta-Agent keeps because it designed something. It is not the target's runnable files or current state.

### Provisional baseline

A sufficiently frozen design used for validation. It is not proof, execution source, target adoption, or activation.

## 3. TLR-01 answer guide — Same-repository concurrency

### Plain meaning

Two Agents may share one repository. The question is whether two separate tasks can work at the same time when they touch truly separate parts.

### Smallest practical form

Each task declares:

- target Agent;
- exact files/directories it may change;
- whether it touches shared or repository-wide files;
- branch/PR identity;
- whether another active task overlaps.

A mechanical check compares the two write sets.

### Why not serialize everything

If Agent A changes only `targets/a/` and Agent B changes only `targets/b/`, a repository-wide lock wastes time and recreates the old single-project bottleneck.

### Why path separation alone is insufficient

Both tasks may still change a root lockfile, generated index, shared schema, CI configuration, or repository governance. The rule therefore distinguishes target-local, shared-object, repository-global, and unknown scope.

### Does this allow two PRs for one task

No. One-task/one-canonical-PR remains. The proposal allows distinct tasks for distinct target roots, not parallel variants of the same task.

### Does Git mergeability prove safety

No. Git may merge text cleanly while the changes are semantically inconsistent. Mechanical path checks and shared-object rules are additional controls.

### Deferral effect

Use serialization for same-repository writes until the Owner decides or validation passes.

### Frontier re-entry

Required if the Owner proposes uncontrolled concurrent writes, one shared live writer across targets, or changes the existing authority model.

## 4. TLR-02 answer guide — Dependencies and impact views

### Plain meaning

The code library should describe itself accurately. Each consuming project should record what it uses. The library need not manually maintain an endless list of every user.

### What the library owns

- API and version;
- compatibility and breaking changes;
- change log;
- migration instructions;
- deprecation/security notices;
- tests for the published contract.

### What the consumer owns

- dependency declaration and selected version;
- where/how it uses the API;
- upgrade timing;
- project-local changes and tests.

### Why a derived impact view can help

Within a shared repository or controlled organization, a tool can scan consumer declarations and produce a current list of potentially affected targets. This avoids asking a human or library Agent to maintain the same information twice.

### Is this still a reverse index

It is a reverse **view**, but not an independently edited authority. Its contents are derived from consumer-owned declarations and can be rebuilt.

### When manual registration is justified

- fixed participants in a coordinated migration;
- security notification;
- contractual support;
- dynamic/indirect usage that cannot be rediscovered;
- Owner accepts the maintenance burden.

### What if a consumer does not upgrade

The library publishes changes; the consumer decides when to upgrade unless a separate security, compatibility, or organizational policy requires action.

### Deferral effect

Keep candidate v0.1's library/consumer section provisional and do not run V6/V7 as acceptance tests for a frozen model.

### Frontier re-entry

Required if a universal mandatory consumer registry is introduced or if the library becomes authoritative over target-project dependency truth.

## 5. TLR-03 answer guide — Evolution axes

### Why the original correction matters

Improving Mnemosyne may change an Agent's memory files or behavior without changing the business function or API. A business request may change code without changing the Agent operating system. An API may change while the Agent's own memory design stays the same.

### Why secondary effects are needed

The axes are distinct, not isolated. A business change may genuinely require a new API. The model needs a place to record that link without treating it as automatic.

### Smallest practical form

One change record states:

- primary axis;
- direct effects;
- possible secondary effects;
- evidence/reason;
- required decision;
- accepted/rejected status.

### Why not multiple co-primary axes by default

Multiple co-primary labels can make the original cause and authority unclear. One primary axis plus explicit secondary effects provides better traceability. The Owner may nevertheless prefer co-primary treatment for genuinely inseparable changes.

### Physical-container axis

Moving or restructuring files can affect paths and recovery without changing Agent behavior, business semantics, or API. It therefore deserves its own axis.

### Provider-adapter axis

A Claude Skill or ChatGPT Project behavior change may require packaging changes without changing the provider-neutral capability.

### Deferral effect

Keep the separate-axis principle but do not create a v0.2 cross-axis mechanism.

### Frontier re-entry

Required if Agent-internal, business, and API changes are merged into one undifferentiated evolution category or automatic propagation is proposed.

## 6. TLR-04 answer guide — Parent-owned design brief

### Plain meaning

Mnemosyne and Meta-Agent need to remember what they designed. They should not host the target itself.

### Safe brief

A parent brief explains the problem, options, rationale, target destination, delivery identity, and later generalized lessons.

### Unsafe bootstrap

A parent repository becomes a target bootstrap when a fresh session can operate the target from it, or when it contains live target truth/state/handoff/memory intended to migrate later.

### Why pointers alone may be insufficient

The meta-system needs enough retained rationale to improve its own methods and assess upstream impacts. A bare link may not preserve the design problem or why a choice was made.

### Why a broad package is dangerous

A complete duplicate can drift, become a second writer, and make later migration unavoidable.

### Practical boundary test

Ask:

> If the target repository disappeared, could this parent-side material be mistaken for the current runnable target?

If yes, the exception is too broad.

### Deferral effect

Parent/meta systems keep only existing bounded pointers and do not expand target-related records.

### Frontier re-entry

Required if the Owner allows live target state or a complete target tree in the parent repository.

## 7. TLR-05 answer guide — Baseline and validation order

### Why accept a provisional baseline before testing

A test needs a fixed contract. Otherwise a failure can be dismissed by redefining the architecture after the fact.

### Why provisional acceptance is not target adoption

The baseline says “this is the design to test.” It does not tell Meta-Agent, the code Agent, or the language Agent to use it.

### Why not accept without validation

Same-repository concurrency, dependency discovery, and backup restore contain practical failure modes that pure reasoning cannot establish.

### Smallest validation

Use only public/synthetic fixtures and frozen tasks. No real target data or activation is necessary.

### Who does what

- Owner: confirms architecture and authorizes any run;
- Pro/frontier: freezes/adjudicates semantics;
- next-tier: executes frozen scenarios;
- mechanical tools: compare paths, identities, diffs, and restore outputs.

### Deferral effect

Keep v0.1 and adjudication evidence; no v0.2 and no validation run.

### Frontier re-entry

Required for target adoption, operational activation, automatic propagation, or changing truth/write authority.

## 8. Anticipated cross-question concerns

### “全都只是规则，会不会太空洞？”

Yes, until tested. The package separates semantic acceptance from implementation proof and requires bounded validation before target adoption.

### “为什么不能直接在真实项目里试？”

Real use will eventually be necessary, but the first checks concern authority isolation, concurrency, and backup restoration. A synthetic failure is cheaper and avoids contaminating real target truth.

### “多个 Agent 共仓库是不是等于 monorepo？”

It can resemble a monorepo, but the important decision is logical authority separation, not the label or directory style.

### “为什么还需要人确认，既然方向是我已经说过的？”

The fixed direction is preserved. The questions concern new operational consequences: concurrency, dependency views, cross-axis links, parent record scope, and what ‘accepted enough to test’ means.

### “确认后是不是马上运行验证？”

No. Saving the confirmed result, preparing v0.2, preparing a runnable validation package, and executing the validation are separate authorization gates.

### “这次是否需要 Deep Research 或 Fable？”

No for the five Owner decisions. Fable may later provide an independent challenge only after a precise non-duplicative question exists.
