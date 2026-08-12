# Owner Decision Workbook — OR-02 through OR-09

> Ask these questions in order, one coherent sub-group at a time. The Owner may answer in ordinary language, request item-by-item explanation, revise an earlier answer, defer, reject an option, or reject the premise. Option labels are navigation aids, not mandatory answer formats.

```yaml
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-002
question_set_version: 0.2.0
question_range: OR-02_through_OR-09
repository_write_during_interview: false
```

## How to use this workbook

For each question or sub-group:

1. explain only the context needed for that choice;
2. present the relevant capability names in natural Chinese, not IDs alone;
3. answer questions from `03-capability-selection-and-qa-guide.md`;
4. if the Owner requests an OR-01-style review, explain items one by one and record each disposition;
5. preserve the Owner's wording separately from the interviewer interpretation;
6. restate the interpretation and ask for correction;
7. mark the item `CONFIRMED`, `PROVISIONAL`, `DEFERRED`, `REJECTED`, `NOT_APPLICABLE`, or an escalation status;
8. update the concise visible ledger before proceeding.

Do not force repository names, provider products, private storage, or operational activation before their consequences are understood.

---

# OR-02 — What should remain in the shared semantic floor for all three systems?

## Background

The 41 active catalogue entries were already reviewed in `OR-01`. The planner now proposes 18 capabilities as the common first-version floor. “Shared floor” means the semantics must exist compactly; it does **not** mean 18 separate files, 18 always-loaded modules, or 18 mature implementations.

Review six groups. By default ask one group at a time. The Owner may approve a whole group, move named items to triggered/experimental/deferred status, or request item-by-item review.

## OR-02-A — Durable source and current authority

Capabilities:

- `ACAP-001` — durable external memory;
- `ACAP-002` — one currently adopted authority boundary;
- `ACAP-003` — artifact-role and storage organization;
- `ACAP-004` — source preservation with byte/semantic distinction;
- `ACAP-005` — requirement intake, approval, and semantic conflict review;
- `ACAP-006` — decision rationale, supersession, and lineage.

Practical first-version form:

- one compact target spec/authority map;
- one requirements/source intake record;
- one decision/change history;
- exact/normalized/pointer source roles stated where material.

Omission risks:

- dependence on one chat context;
- latest summary or handoff silently becoming authority;
- original purpose becoming unrecoverable;
- new ideas changing behavior without approval;
- future models unable to understand why a design exists.

Planner recommendation: **keep all six initially required**, implemented compactly.

Owner choices:

- keep the group as initially required;
- move named items to triggered/experimental status;
- replace the group with a simpler formulation;
- remove named items from the shared floor;
- defer or reject the group.

Escalation: rejecting durable source, one current authority boundary, or approved requirement change materially changes the architecture and requires Pro/frontier re-entry.

## OR-02-B — Current work, fresh-session continuity, and target-local truth

Capabilities:

- `ACAP-007` — current-state navigation;
- `ACAP-008` — fresh-session and handoff continuity;
- `ACAP-009` — cold source as evidence/synthesis input;
- `ACAP-011` — target-local truth, no dual writer, and non-authoritative backup.

Practical first-version form:

- one short current-state/handoff view;
- a source map and cold-reading rule;
- one declared active target writer;
- optional identity-pinned recovery snapshot that cannot become a competing writer.

Omission risks:

- every new conversation rescans history or recovers the wrong route;
- cold archives become routine runtime input;
- Mnemosyne, Meta-Agent, and target all look authoritative;
- backups drift into second truth sources.

Planner recommendation: **keep all four initially required as semantics**; keep backup optional.

Escalation: rejecting target-local truth/no-dual-writer or proposing a shared live database/runtime requires Pro/frontier review.

## OR-02-C — Controlled evolution

Capability:

- `ACAP-012` — controlled evolution, migration, compatibility, and optional rollback.

Practical first-version form:

- stable IDs for important objects;
- compact version/change record;
- previous-state reference;
- when a real change occurs, classify preserve/transform/recompute/retire and validate the result.

Why it is still proposed despite limited evidence:

The first target need not have a universal migration engine. It only needs to avoid anonymous destructive overwrite and preserve enough identity to evolve later. Detailed thresholds remain provisional and should come from real changes.

Planner recommendation: **keep lightweight required semantics; treat the mechanism as an early experiment.**

Owner choices:

- required semantics + experimental mechanism;
- triggered only when the first material change occurs;
- deferred until a real change;
- another formulation.

Escalation: broad irreversible migration, authority change, or automatic cross-target update requires Pro/frontier review.

## OR-02-D — Objective, readable, and correctable interaction

Capabilities:

- `ACAP-014` — objective evidence-bound engineering;
- `ACAP-016` — human-readable concise presentation;
- `ACAP-017` — staged intent reconstruction with correction rights.

Practical first-version form:

- distinguish fact, user goal/value, interpretation, and uncertainty;
- explain decisions in concise natural language;
- preserve the user's ability to correct the inferred need;
- invoke the heavier next-tier/frontier staged flow only for material ambiguity.

Omission risks:

- flattering or unsupported conclusions;
- large unreadable output blocks;
- literal wording implemented even when it misses the real need;
- AI interpretation becoming a hidden permanent goal.

Planner recommendation: **keep all three initially required**, with heavy staged clarification triggered only when needed.

## OR-02-E — Capability routing and safe limits

Capabilities:

- `ACAP-021` — capability-aware work decomposition;
- `ACAP-022` — bounded effort and calibrated stop/escalation.

Practical first-version form:

- split frontier reasoning, bounded execution, mechanical checks, and human decisions;
- use observable triggers, acceptance checks, and bounded correction attempts rather than model self-confidence alone;
- stop on authority/privacy/architecture/missing-input conflicts.

Omission risks:

- expensive frontier work used for mechanical tasks;
- bounded models silently decide architecture or privacy;
- models either hard-persist beyond competence or escalate at the first difficulty.

Planner recommendation: **keep as required routing/stop semantics; treat calibration details as an experiment.**

## OR-02-F — Real-use learning and controlled improvement

Capabilities:

- `ACAP-034` — real-use evaluation, feedback, and postmortem;
- `ACAP-038` — early bounded use with controlled evolution.

Practical first-version form:

- record intended value, observed result, user usefulness/burden, correction, and repeated/severe failure;
- do not write a formal postmortem for every task;
- begin useful work before theoretical completion while preserving source, authority, privacy, and change paths.

Omission risks:

- “files created successfully” substitutes for actual value;
- system never learns from user friction;
- first version becomes frozen or theoretical design continues indefinitely.

Planner recommendation: **keep both initially required as lightweight semantics; learn thresholds through real use.**

## OR-02 shared-trigger question

The planner excludes the following from the always-on shared floor and treats them as common triggered modules:

- user-operation separation (`015`);
- contextual clarification/answer ledger (`018`, `019`);
- research/independent challenge (`023`, `024`);
- external-task output/transfer (`025`–`028`);
- repository/authority/provenance (`029`–`033`);
- retrieval/provider packaging (`039`–`042`).

Ask whether the Owner accepts this distinction or wants any named triggered item moved into the common required floor.

Safe deferral: preserve the planner floor as a candidate and do not instantiate it in any target until later confirmation.

---

# OR-03 — Which additional capabilities should Meta-Agent initially use?

## Background

Meta-Agent designs Agents and methodology that may affect many targets. Its repository-backed target truth remains operationally inactive. This question selects inputs for a later Meta-Agent-owned review/package; it does not activate or modify Meta-Agent.

Review four groups.

## OR-03-A — Proposed required additions

- `ACAP-013` — upstream change impact assessment;
- `ACAP-018` — context-rich clarification;
- `ACAP-019` — answer ledger and correction tracking;
- `ACAP-023` — research-value and quota gate;
- `ACAP-032` — run context and provenance;
- `ACAP-035` — controlled generalization and method-promotion filter;
- `ACAP-037` — capability selection/adoption record;
- `ACAP-040` — capability-to-instruction packaging.

Planner rationale:

- Meta-Agent may change designs used by multiple targets, so it needs impact and promotion controls;
- its output depends on understanding and recording Owner choices;
- research and provenance matter for important design work;
- every designed target should receive an explicit capability selection;
- its practical value depends on producing usable target instructions, while `ACAP-040` remains an unresolved design problem rather than a proven packaging standard.

Planner recommendation: **accept these as initial semantics**, but mark `013` and `040` as lightweight/provisional.

## OR-03-B — Proposed triggered additions

- `ACAP-020` when Meta-Agent models recurring user/organization patterns;
- `ACAP-024` for novel, disputed, high-impact, or acceptance-critical design;
- `ACAP-025`–`028` when it prepares external research/review or cross-conversation tasks;
- `ACAP-029`–`031` when it performs actual repository/PR actions.

Planner recommendation: **triggered, not always loaded**.

## OR-03-C — Proposed early experiments

- `ACAP-010` — small core, task-triggered modules, and uncovered-behavior receipt;
- `ACAP-033` — ordered target/meta repository work;
- `ACAP-041` — Skills/module adapter after current verification;
- `ACAP-042` — decision-driven provider/product entries.

Planner recommendation: **experiment only when a concrete target/provider task exists.**

## OR-03-D — Meta-Agent-specific objects

- method registry and version/impact links;
- target case/evidence pointers;
- design package and acceptance record;
- methodology-promotion history;
- designed-target index without target authority.

Ask whether these objects are sufficient, excessive, or missing something.

Owner choices for OR-03:

- accept each group as proposed;
- move named items among required/triggered/experimental/deferred;
- add a missing capability/object;
- defer the whole Meta-Agent extension;
- reject capability-based extension until Meta-Agent's current P0 work is resolved.

Mandatory frontier re-entry:

- operational activation;
- ownership of a future common capability library;
- target-truth or write-authority change;
- private-material access;
- automatic methodology promotion;
- major change to the six accepted Meta-Agent methods.

Safe deferral: retain the v0.2 planner selection as non-authoritative input and leave Meta-Agent unchanged.

---

# OR-04 — Which additional capabilities and objects should the code-library system use?

## Background

The target should accumulate real development requirements, business rules, implementation, tests, compatibility, and reuse evidence. Portable Agent controls and domain-specific software records must remain distinct.

Review four groups.

## OR-04-A — Proposed required portable additions

- `ACAP-029` — exact platform permission versus task authorization;
- `ACAP-037` — explicit capability selection/adoption record.

Why only two beyond the shared floor:

Most code-specific needs are domain objects rather than universal Agent-operating capabilities. Repository, PR, transfer, provenance, and cross-repository controls should trigger only when the actual toolchain/action requires them.

Planner recommendation: **keep both required.**

## OR-04-B — Proposed target-specific initial objects

1. requirement and business-rule source;
2. requirement → design decision → implementation → test/acceptance trace;
3. reusable versus project-local scope and rejected-reuse cases;
4. function/API/dependency/compatibility record;
5. private source/customer/credential boundary;
6. consuming-project links and migration impact;
7. useful-result, rework, and failure record.

Ask item by item if requested. These are not common capability IDs and should remain target-local.

## OR-04-C — Proposed triggered modules

- `ACAP-015` when user operations/approvals exist;
- `ACAP-025` when work crosses conversations/tools;
- `ACAP-027` for long patch/task transfer;
- `ACAP-030` when GitHub PR workflow is used;
- `ACAP-031` only when a live branch must be retained;
- `ACAP-032` for important changes/reviews;
- `ACAP-033` when both the library and a consuming project are read/written;
- `ACAP-040` after a coding surface/package is selected.

Planner recommendation: **triggered by actual workflow, not loaded for every coding task.**

## OR-04-D — Experiments and deferrals

Early evidence candidates:

- `ACAP-010` runtime-load/coverage-gap handling;
- `ACAP-012`, `013`, `033`, `034` real migration/impact/cross-repository/value evidence.

Deferred until evidence or tool choice:

- research/independent challenge for ordinary bounded implementation;
- `ACAP-039` retrieval automation;
- `ACAP-041` Skill/module packaging;
- broad `ACAP-042` provider catalogue population.

Owner choices:

- accept the lighter selection;
- require named triggered controls from day one;
- remove/add capabilities or objects;
- postpone until repository/toolchain and representative task are selected;
- reject the target framing.

Frontier re-entry:

- private work code/customer data/credentials;
- repository visibility and target truth;
- cross-repository write authority;
- disputed business-rule or reuse architecture;
- high-impact migration.

Safe deferral: preserve target-specific traceability/privacy objects and wait to instantiate provider/GitHub adapters until the toolchain is selected.

---

# OR-05 — Which additional capabilities and objects should the language-teacher system use?

## Background

The target should provide useful teaching and practice, preserve multidimensional evidence, adapt plans, and avoid turning sparse or noisy interaction into permanent learner/user labels.

Review four groups.

## OR-05-A — Proposed required portable additions

- `ACAP-018` — context-rich clarification;
- `ACAP-019` — answer ledger and correction tracking;
- `ACAP-020` — evidence-calibrated user-state inference;
- `ACAP-037` — capability selection/adoption record.

Planner recommendation: **keep all four required**, while ordinary lessons use lightweight forms.

## OR-05-B — Proposed target-specific initial objects

1. multidimensional language evidence, only for dimensions actually observed;
2. evidence provenance: independent, hinted, repeated, translated, or affected by speech recognition/noise;
3. observed error, alternative explanation, correction, recurrence, and uncertainty;
4. current goals, teaching plan, exercise history, and burden;
5. immediate performance versus delayed retention/transfer/independence;
6. private complete-conversation archive or verified pointer;
7. teaching-method change rationale and keep/revise criteria;
8. user correction, deletion, and dispute path.

Ask item by item if requested. These are target-specific teaching/memory objects, not universal capability entries.

## OR-05-C — Proposed triggered modules

- `ACAP-015` when a current user operation exists;
- `ACAP-023` for external teaching-method/product facts;
- `ACAP-024` after enough longitudinal evidence exists for independent review;
- `ACAP-025`–`028` for external research/review/export tasks;
- `ACAP-032` for important formal assessment, teaching-policy change, or cross-model review.

Planner recommendation: **triggered rather than present in every lesson.**

## OR-05-D — Experiments and deferrals

Early experiments:

- `ACAP-010` separating current lesson context from cold archives;
- `ACAP-017` staged intent reconstruction for major goal/plan changes;
- `ACAP-034` minimal useful/burdensome/misleading event records;
- `ACAP-040` packaging for the selected text/voice surface;
- `ACAP-042` decision-relevant text/voice/memory/file/transcript/privacy/quota facts.

Deferred:

- repository/PR controls unless the target uses them;
- `ACAP-039` until real retrieval misses occur;
- `ACAP-041` until current Skill semantics are verified and useful;
- stable profile features unsupported by repeated evidence and a clear teaching purpose.

Owner choices:

- accept the proposed package;
- move named items among required/triggered/experimental/deferred;
- add a missing teaching/memory object;
- begin with teaching/practice only and defer longitudinal assessment;
- defer or reject the target.

Frontier re-entry:

- private storage approval;
- formal proficiency-assessment policy;
- learner-model architecture;
- voice/transcription evidence policy;
- major teaching-method redesign.

Safe deferral: permit only low-risk practice and evidence capture after private storage/correction rights are chosen; do not issue stable proficiency/personality/learning-style claims.

---

# OR-06 — Should target work normally use a target-local repository or approved store?

## Background

Keeping several targets inside Mnemosyne created coupling, irrelevant loading, privacy risk, and competing truth. Meta-Agent migration shows a dedicated repository and no-dual-writer cutover can work, but does not prove every future workflow.

## Options

### OR-06-A — Target-local truth by default; bounded meta-system pointers **(planner recommendation)**

- target owns truth, implementation, current state, handoff, tests, and migrations;
- Mnemosyne keeps memory-system design/evaluation and impact references;
- Meta-Agent keeps safe design-case/method evidence;
- no competing writer remains.

Advantages:

- independent project work and safer concurrency;
- smaller runtime context;
- clearer privacy and authority;
- easier replacement/evolution of meta-system processes.

Risks:

- cross-repository tasks need exact order and authorization;
- more repositories/stores require navigation discipline;
- common capability updates need impact tracking.

### OR-06-B — Temporary bootstrap inside a meta-system, followed by explicit cutover

Use only if a destination cannot yet be selected. Required:

- bootstrap marked non-final;
- planned destination;
- destination-only recovery;
- no-dual-writer check;
- explicit cutover gate.

### OR-06-C — Keep a selected target inside Mnemosyne or Meta-Agent long-term

This would preserve setup simplicity but reintroduce coupling and possible competing roles. Choose only with a specific reason and explicit truth/write boundaries.

### OR-06-D — Another model or reject the premise

The Owner may propose a different repository/store architecture.

Deferral default: use target-local as planning direction, but create no repository/store and authorize no writes.

Frontier re-entry: any new shared runtime database, live mirrored truth, cross-target shared writer, or long-term co-location architecture.

---

# OR-07 — Where should structured truth, code, complete private originals, and backups live?

## Background

This question intentionally separates four material classes. The Owner may choose constraints/preferences now without naming a provider or authorizing ingestion.

## OR-07-A — Structured target truth and compact current records

Options:

- private target Git repository;
- another versioned private store;
- local version-controlled store;
- temporary bootstrap location pending cutover;
- defer until target preflight.

Record desired properties:

- privacy level;
- version history;
- accessibility from selected Agents;
- backup expectations;
- portability/export;
- who can write.

## OR-07-B — Work source, customer/confidential material, and credentials

Safe default:

- remain in existing approved work repositories/stores;
- never place credentials in Git;
- do not move private/customer source into Mnemosyne's public repository;
- decide exact Agent access separately.

Ask for Owner constraints, not sensitive material itself.

## OR-07-C — Complete personal learning conversations and other private originals

Options at the requirement level:

- private local cold archive;
- approved private cloud/archive;
- private Git only if size, history, privacy, and access are acceptable;
- product-native export/library plus verified external backup;
- another approved route;
- defer.

Safe default: compact structured teaching truth in a private target store; complete conversations in separate private cold storage or verified pointers.

Current product privacy/export/retention facts require verification.

## OR-07-D — Non-authoritative recovery snapshots

Ask whether each target should have a compact identity-pinned backup elsewhere.

If yes, require:

- explicitly non-authoritative;
- read-only/immutable or no independent edits;
- exact source/version identity;
- recovery purpose and test;
- no second active writer.

Frontier re-entry:

- approving a concrete private-material store/service;
- creating a trust/permission relationship;
- allowing complete private data into Git or another provider;
- changing target truth/write authority.

Deferral default: no private ingestion; preserve only safe non-sensitive planning records.

---

# OR-08 — What preparation and bounded-real-use order should the three systems follow?

## Background

Separate **preparation order** from **operational activation/pilot order**. Meta-Agent remains inactive and has existing P0 candidate work. A target can be prepared without being activated; Meta-Agent can be prepared for a bounded pilot without that pilot being authorized.

## Option A — Meta-Agent preparation first, then target packages

- first align its current P0/behavior/memory prerequisites;
- later use it to design both targets;
- no target pilot until Meta-Agent is ready.

Advantage: directly tests the intended design factory.

Risk: delays real target evidence and may recreate “wait for Meta-Agent completion.”

## Option B — Language-teacher target first

- decide private storage and minimal package;
- start low-risk practice/evidence capture;
- prepare Meta-Agent separately.

Advantage: frequent, low-cost real feedback and direct personal value.

Risk: privacy/product/voice evidence may require preflight; early learner evidence can be noisy.

## Option C — Code-library target first

- choose a safe repository/toolchain and non-sensitive representative tasks;
- accumulate requirement-to-code/test/reuse evidence;
- prepare Meta-Agent separately.

Advantage: concrete engineering artifacts and strong mechanical checks.

Risk: private work/customer/credential boundaries may complicate the first task.

## Option D — Parallel preparation; one target starts bounded use after storage/preflight **(planner recommendation)**

- prepare Meta-Agent's later review/activation package without activating it;
- prepare both target-local minimum packages;
- start the first bounded target whose storage, allowed material, and representative task become ready first;
- keep shared capability/method writes serialized.

Advantage: avoids idle time and generates evidence quickly.

Risk: more planning threads and human review burden.

## Option E — Owner-defined sequence or reject the three-system framing

The Owner may choose another order, start only one system, or change the target set.

Questions to capture:

1. Which package should be designed first?
2. Which system should perform the first actual bounded task?
3. May preparation proceed in parallel?
4. What prerequisite blocks each system?
5. What is explicitly not being activated?

Frontier re-entry:

- Meta-Agent operational activation;
- pilot scope and acceptance/stop criteria;
- target truth/storage authority;
- private-material access;
- a new architecture or changed target purpose.

Deferral default: prepare target packages only; no operational activation or pilot.

---

# OR-09 — Which provider/model/product/Skills questions should be verified now, and which should wait?

## Background

Portable capability choices should not be delayed by unnecessary product research. However, implementation requires current facts. The Owner should choose **which decisions matter first**, not guess the facts.

## OR-09-A — Meta-Agent implementation facts

Potential fact checks when a bounded Meta-Agent package is imminent:

- repository access and write surfaces;
- project/system instruction behavior;
- Skill/module loading, scope, precedence, versioning, tool relation, context cost, and security;
- file/context limits relevant to design packages;
- cross-conversation/project isolation and export;
- validated frontier versus next-tier task reliability.

## OR-09-B — Code-library toolchain facts

Potential checks when the code target is imminent:

- repository read/write, branch/PR, review, and test capabilities;
- local/cloud execution and build support;
- repository indexing/context behavior;
- private source and secret handling;
- transfer and artifact limits;
- model reliability for frozen code work versus architecture.

## OR-09-C — Language-teacher surface facts

Potential checks when the language target is imminent:

- text/voice availability and interruption behavior;
- transcript quality/export and speech-recognition limitations;
- Project/conversation memory and isolation;
- file/structured-output support;
- private learner-record storage and data-use boundaries;
- target package loading;
- sustained-use cost, quota, latency, and device behavior.

## OR-09-D — Timing choices

The Owner may choose:

- verify only facts needed for the first selected target;
- prioritize Claude Skills/Project/instruction facts because near-term work is expected to use Claude;
- verify ChatGPT/Claude cross-provider portability before any target package;
- postpone all product facts until target storage/order is decided;
- request a bounded behavior test after official documentation review;
- another order.

Planner recommendation: **decision-driven verification only**. Start with the first target's smallest relevant product facts; do not build a complete provider encyclopedia.

Required status when facts are asked:

```text
CURRENT_PRODUCT_FACT_VERIFICATION_REQUIRED — <fact and affected decision>
```

Research routing:

- ordinary official-document verification for most current product facts;
- bounded behavior test when documentation cannot establish reliability;
- Deep Research only when evidence is distributed and can materially change a high-impact choice;
- Fable/frontier research for open architecture/ownership questions, not simple product lookup.

Completion condition for OR-09:

- list the fact categories to verify first;
- list deferred categories and revisit triggers;
- preserve Owner priorities and constraints;
- do not claim current product facts or authorize a run.

---

# Completion sequence

After `OR-02` through `OR-09`:

1. show the complete answer ledger;
2. distinguish confirmed, provisional, deferred, rejected, current-fact, missing-artifact, and frontier-reentry items;
3. summarize the selected shared floor and each target's additions in natural language;
4. summarize repository/storage preference without claiming implementation authorization;
5. distinguish preparation order from activation/pilot order;
6. list exact current-product facts to verify later;
7. state what no-write/no-run boundaries remained intact;
8. ask the Owner to correct the final summary;
9. wait for separate authorization before saving the result or modifying any target.
