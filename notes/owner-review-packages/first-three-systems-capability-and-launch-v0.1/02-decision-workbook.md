# Owner Decision Workbook

> The next-tier interviewer should ask these questions in order, one question or coherent sub-group at a time. The Owner may answer in ordinary language, revise an earlier answer, defer, reject an option, or reject the premise. Option labels are navigation aids, not mandatory answer formats.

```yaml
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-001
question_set_version: 0.1.0
question_count: 9
repository_write_during_interview: false
```

## How to use the workbook

For each question:

1. explain the background and practical consequence briefly;
2. answer questions from the package reference or permitted source files;
3. capture the Owner's answer or safe reference;
4. restate the interpreted answer and ask for correction;
5. mark the item `confirmed`, `provisional`, `deferred`, `rejected`, or `escalate`;
6. update the visible ledger before proceeding.

Do not force the Owner to decide repository names, product facts, or private-material handling before the relevant implications are understood.

---

# OR-01 — Is the capability catalogue usable as the first working inventory?

## Background

MNEMOSYNE-200 created 42 candidate capabilities so the Owner and future Agent designers do not have to remember every behavior developed across long conversations. The catalogue is deliberately incomplete and may contain entries that are too broad, overlapping, confusing, or placed in the wrong category.

The immediate decision is not whether the catalogue is permanently correct. It is whether it is good enough to use as a selection aid for the first three systems while real use supplies corrections.

## What this changes

- acceptance allows target package design to proceed without another complete catalogue redesign;
- requested edits can be incorporated before target selections become approved target records;
- a major-rebuild decision delays capability-based target design but may reduce later rework;
- rejection means another method is needed to avoid reliance on human memory.

## Options

### OR-01-A — Accept as a working candidate, with corrections during use **(planner recommendation)**

Practical effect:

- keep the 42 entries as version 0.1;
- record omissions, duplicates, renames, and scope corrections;
- do not treat catalogue completeness as a launch gate;
- revise after target use provides evidence.

Main advantage: fastest path to real use and tests whether the catalogue actually helps.

Main risk: early target packages may expose duplicated or poorly scoped entries.

### OR-01-B — Accept only after a bounded reorganization

Possible changes:

- merge overlapping entries;
- change categories;
- rewrite names/descriptions for readability;
- preserve IDs or issue a v0.2 mapping.

Main advantage: lower review burden for later selections.

Main risk: another abstract cleanup cycle before evidence of actual use.

### OR-01-C — Require a major redesign before use

Main advantage: opportunity for a more systematic capability model.

Main risk: recreates the “wait until complete” pattern the Owner has decided to stop.

### OR-01-D — Reject the catalogue approach

The Owner may propose another way to remember and select reusable Agent capabilities.

## Free-form prompts

- Which entries are clearly missing?
- Which entries appear duplicated or too vague?
- Which names are difficult to understand?
- Should the catalogue remain a checklist rather than a formal ontology?

## Deferral

Safe default if deferred: use version 0.1 as a provisional checklist only; do not promote it to execution source or Meta-Agent methodology.

## Escalation

Return to frontier review if the Owner proposes a new canonical common-library architecture or changes the ownership relationship among Mnemosyne, Meta-Agent, and targets.

---

# OR-02 — What should remain in the shared minimum for all three systems?

## Background

The candidate selection contains 18 shared capabilities. “Shared minimum” means the first bounded version should preserve the semantics, not that it must create 18 files or apply every capability on every turn.

To reduce cognitive burden, review them as five groups.

## Group OR-02-A — Durable source and truth

- `ACAP-001` file-backed persistent memory;
- `ACAP-002` one target truth source;
- `ACAP-003` role separation among truth, evidence, raw, candidate, current state, and handoff;
- `ACAP-004` original/source preservation;
- `ACAP-005` requirement intake and approval;
- `ACAP-006` decision, supersession, and lineage.

What omission risks:

- dependence on one chat context;
- archive or summary becoming competing truth;
- loss of original purpose;
- silent requirement changes;
- inability to understand why a later design exists.

Planner recommendation: **required initially for all three**, implemented compactly.

## Group OR-02-B — Continuity, loading, and evolution

- `ACAP-007` current-state navigation;
- `ACAP-008` fresh-session/handoff continuity;
- `ACAP-009` cold/on-demand source loading;
- `ACAP-011` target-local truth and no dual writer;
- `ACAP-012` version, migration, and rollback.

What omission risks:

- new conversations cannot continue reliably;
- full archives overload every task;
- Mnemosyne/Meta-Agent/target become competing writers;
- later improvements overwrite existing work without compatibility or recovery.

Planner recommendation: **required semantics**, with `ACAP-009` and `ACAP-012` initially lightweight rather than infrastructure-heavy.

## Group OR-02-C — Human understanding and correction

- `ACAP-014` objective evidence-bound engineering;
- `ACAP-016` human-readable concise presentation;
- `ACAP-017` intent reconstruction with correction rights.

What omission risks:

- confident but unsupported conclusions;
- unreadable process burden;
- incomplete user wording treated as final target truth.

Planner recommendation: **required initially**.

## Group OR-02-D — Capability split and stop behavior

- `ACAP-021` capability-aware work decomposition;
- `ACAP-022` stop and escalation contract.

What omission risks:

- scarce frontier work used for mechanical tasks;
- bounded models silently making architecture, privacy, or authority decisions;
- missing inputs filled by invention.

Planner recommendation: **required as routing/stop semantics**, not necessarily exposed in every user response.

## Group OR-02-E — Real-use learning

- `ACAP-034` evaluation, feedback, and postmortem;
- `ACAP-038` reversible real-use iteration.

What omission risks:

- systems report artifact completion without learning from failures;
- first versions become hard to revise;
- abstract design continues without real evidence.

Planner recommendation: **required initially**.

## Answer choices

For each group, the Owner may choose:

- keep as initially required;
- keep but mark some entries triggered/experimental;
- remove named entries from the shared set and place them only on specific targets;
- replace with a simpler semantic formulation;
- defer the group;
- reject the premise of one shared minimum.

## Deferral

Safe default: preserve all five groups in target design, but allow compact implementations and explicitly label untested components as provisional.

## Escalation

Return to frontier review if the Owner rejects single target truth, target-local authority, original-source preservation, or safe stop/escalation as general principles, because that materially changes the current architecture.

---

# OR-03 — Which additional capabilities should Meta-Agent initially own or use?

## Background

Meta-Agent designs Agents, workflows, memory structures, handoffs, model/tool routing, evaluation, and human-decision boundaries. It already has six Owner-accepted but operationally inactive methods. The candidate catalogue must not silently replace those methods.

The decision here is which additional capabilities should appear in a future Meta-Agent target-owned review/package, not whether Meta-Agent is activated now.

## Planner's revised recommendation

### Initially required semantics

- `ACAP-013` upstream impact assessment;
- `ACAP-018` context-rich clarification;
- `ACAP-019` answer ledger and correction tracking;
- `ACAP-023` research-value and quota gate;
- `ACAP-032` run context and provenance for important design/review work;
- `ACAP-035` no automatic case-to-method promotion;
- `ACAP-036` generalization/portability filter;
- `ACAP-037` capability selection record;
- `ACAP-040` prompt/instruction packaging.

### Triggered capability, not invoked on every design

- `ACAP-024` independent frontier challenge.

Reason: Meta-Agent should know when and how to request an independent challenge, but ordinary bounded design work should not automatically require another frontier run.

### Early experiments

- `ACAP-010` runtime load profile and receipt;
- `ACAP-033` cross-repository ordered work;
- `ACAP-041` Skill/module packaging;
- `ACAP-042` provider/model/product capability catalogue.

### Later/triggered

- external-task and Deep Research delivery controls when Meta-Agent actually prepares those tasks;
- repository/PR controls when exact repository actions occur;
- retrieval/index automation only after measured need.

## What this changes

- approval supplies the capability boundary for a later Meta-Agent-owned review and bounded pilot package;
- it does not modify `08822407d/Meta-Agent` now;
- it does not authorize operational activation;
- it helps identify what Meta-Agent should remember about Agents it previously designed.

## Options

- accept the planner's revised classification;
- keep the original PR #268 classification, where `ACAP-024` was listed among initial requirements;
- move named items between required/triggered/experimental/deferred;
- add a missing Meta-Agent capability;
- reject capability-based extension until the current six methods are revised;
- defer the whole question.

## Questions the interviewer may ask

- Should Meta-Agent itself maintain the capability catalogue, or only consume a Mnemosyne/common catalogue? **This ownership question requires frontier review; record the Owner's preference but do not finalize architecture.**
- Should Meta-Agent be able to inspect target outcomes? Only through approved safe case/evidence pointers; not as automatic target authority.
- Does “prompt packaging” include Skills? Portable packaging is required; current Skills implementation remains product-fact research.

## Deferral

Safe default: keep these as candidate inputs only and do not change Meta-Agent truth.

## Escalation

Any Meta-Agent activation, methodology promotion, truth-source change, private-material access, or shared-library ownership decision returns to frontier/human adjudication.

---

# OR-04 — Which additional capabilities should the code-library system initially require?

## Background

The code-library target is intended to accumulate real development requirements, business rules, design decisions, reusable functions/code, tests, compatibility, and reuse evidence. The original selection made several GitHub/cross-repository controls unconditional initial requirements.

The planner now recommends distinguishing the **target's hard semantic floor** from controls triggered by the eventual toolchain.

## Planner's revised recommendation

### Initially required beyond the shared minimum

- `ACAP-029` platform permission versus exact task authorization;
- `ACAP-037` capability selection record.

Target-specific initial objects, not common capabilities:

- requirement-to-code traceability;
- reusable versus project-local boundary;
- implementation/test/acceptance evidence;
- dependency and compatibility records;
- private source/customer/credential boundary.

### Early experiment

- `ACAP-010` runtime load profile and receipt, because the library may accumulate many projects and modules.

### Triggered by actual workflow

- `ACAP-025` cross-conversation execution intent — when analysis and repository-changing work cross conversations/tools;
- `ACAP-030` single active PR lineage — when GitHub PR workflow is used;
- `ACAP-032` run context and provenance — for important changes/reviews;
- `ACAP-033` cross-repository ordered work — when a library and consuming project are both involved;
- `ACAP-027` file-first transfer — when long task/patch packages move between tools;
- `ACAP-031` branch-retention lifecycle — only when a real dependency requires retention;
- `ACAP-040` provider packaging — after the coding surface is selected.

### Deferred until evidence

- external research/independent frontier review for ordinary bounded code work;
- Skills packaging until the selected product supports a relevant mechanism;
- RAG/index automation until deterministic repository navigation repeatedly fails.

## Why this differs from PR #268

PR #268 intentionally produced a broad candidate. This revision reduces initial burden by making repository adapters conditional on the actual toolchain. A capability can remain available without being a mandatory first-version runtime rule.

## Options

- accept the revised lighter initial package **(planner recommendation)**;
- keep the broader PR #268 initial package;
- require one or more triggered controls from day one;
- remove or add named capabilities;
- postpone code-library capability selection until a repository/toolchain is chosen;
- reject the target as currently framed.

## Deferral

Safe default: preserve the target-specific traceability/privacy requirements and wait to instantiate GitHub/Skills/provider controls until the toolchain and repository are selected.

## Escalation

Private work code, customer data, credentials, target repository visibility, and cross-repository write authority require explicit later decisions. The interviewer may capture preferences but must not authorize ingestion or writes.

---

# OR-05 — Which additional capabilities should the language-teacher system initially require?

## Background

The language Agent should teach and practice over time, preserve evidence of ability and progress, adapt the plan, and avoid converting sparse interaction or transcription error into permanent learner labels.

The original selection listed research/provenance controls among initial requirements. The planner recommends separating everyday teaching needs from triggered review/research needs.

## Planner's revised recommendation

### Initially required beyond the shared minimum

- `ACAP-018` context-rich clarification;
- `ACAP-019` answer ledger and correction tracking;
- `ACAP-020` no hidden profiling;
- `ACAP-037` capability selection record.

Target-specific initial objects, not common capabilities:

- multidimensional language evidence;
- evidence provenance, including hints/repetition/transcription noise;
- error/hypothesis/correction history;
- current teaching-plan state;
- delayed retention/transfer evidence;
- private conversation/source boundary;
- teaching-method change rationale.

### Triggered

- `ACAP-023` research-value and quota gate — when teaching method or product facts genuinely require research;
- `ACAP-032` run context and provenance — for important formal assessments, method changes, or cross-model reviews;
- `ACAP-024` independent frontier challenge — after enough complete conversation evidence exists for a meaningful longitudinal review.

### Early experiments

- `ACAP-010` runtime profile separating current lesson context from complete cold archives;
- `ACAP-040` packaging for the chosen text/voice surface;
- `ACAP-042` provider/product catalogue for text, voice, memory, file, and app decisions.

### Deferred

- repository/PR controls unless this target actually uses them;
- Skills packaging until current product semantics are verified;
- retrieval automation until conversation volume creates repeated misses.

## Options

- accept the revised lighter initial package **(planner recommendation)**;
- keep the broader PR #268 initial package;
- move named controls into or out of the first version;
- add a missing teaching/memory capability;
- begin with a teaching-only Agent and defer longitudinal assessment;
- defer the whole target.

## Deferral

Safe default: begin only low-risk practice and evidence capture after private storage and correction rights are selected; do not issue stable proficiency/personality/learning-style claims.

## Escalation

Privacy/storage, voice/transcript interpretation, formal assessment policy, or material redesign of the learner model requires frontier/human review. Current product features require external verification.

---

# OR-06 — Should target work normally use a target-local repository or approved store?

## Background

Keeping multiple target projects inside Mnemosyne caused write-lineage coupling, concurrency constraints, irrelevant context loading, and risk that Mnemosyne would become both design archive and target truth. Meta-Agent migration provides practical evidence for a dedicated target repository and no-dual-writer cutover, but not a general proof for every future target.

## Options

### OR-06-A — Target-local truth by default; meta-systems keep bounded pointers/evidence **(planner recommendation)**

Practical effect:

- each target owns its truth, implementation, current state, handoff, tests, and migrations;
- Mnemosyne keeps memory-system design/evaluation references and generalized lessons;
- Meta-Agent keeps safe design-case/methodology records;
- no competing live writer remains.

Advantages:

- independent target work and safer concurrency;
- smaller runtime context;
- clearer privacy and authority;
- easier replacement of Mnemosyne/Meta-Agent processes without rewriting target truth.

Risks:

- cross-repository tasks need explicit ordering and separate authorization;
- common capability updates require impact tracking;
- more repositories/stores require navigation discipline.

### OR-06-B — Temporary bootstrap inside a meta-system, followed by explicit cutover

Use only when a target repository/store cannot yet be selected. Required controls:

- bootstrap state clearly labelled non-final;
- one planned destination;
- destination-only recovery;
- no-dual-writer check;
- explicit cutover gate.

Advantage: lower initial setup friction.

Risk: temporary location may become permanent or be mistaken for target truth.

### OR-06-C — Continue keeping target truth inside Mnemosyne

Advantage: one repository to inspect.

Risks:

- repeats the coordination and context burden already observed;
- prevents clean target independence;
- increases accidental cross-project reads/writes;
- conflicts with the direction established by Meta-Agent cutover.

Not recommended except as a tightly bounded temporary bootstrap.

### OR-06-D — Another model

The Owner may propose a private database, local directory, cloud drive, provider-native workspace, monorepo, or hybrid arrangement. The answer should explain which store owns target truth and how meta-system pointers remain non-authoritative.

## Deferral

Safe default: use target-local truth as the design assumption but do not create a repository/store until OR-07 and the first target are decided.

## Escalation

A new shared runtime database, automated cross-target synchronization, or competing-writer model requires frontier architecture review.

---

# OR-07 — Where should target truth and private originals be stored?

## Background

This question has two layers:

1. **structured target truth and current state** — compact files/records used by normal operation;
2. **complete private originals** — source code, customer/work material, complete personal conversations, exports, and other cold evidence.

They need not use the same store.

## OR-07A — Work/business-function code-library storage

### Option C1 — Dedicated private repository

Best when the library itself becomes a distinct governed asset with code, tests, versions, and reuse metadata.

Advantages:

- clear target truth and independent PR/history;
- easier to separate reusable library from consuming projects;
- compatible with repository-backed Agent workflows.

Risks:

- private/business-source policy and employer/customer constraints must be checked;
- cross-repository consumption needs compatibility and ordered-write rules.

### Option C2 — Existing approved private work repository

Best when the library is inseparable from an existing codebase.

Advantages:

- avoids duplicate code and source movement;
- existing build/test/security controls may apply.

Risks:

- target truth may become mixed with one project;
- reuse scope and Meta-Agent/Mnemosyne access may be constrained;
- the current GitHub connector may not have access or task authority.

### Option C3 — Public-safe skeleton plus private external source/pointers

Advantages:

- permits methodology/design work without exposing code.

Risks:

- higher synchronization and pointer burden;
- cannot validate implementation from public skeleton alone;
- easy to overclaim what was actually inspected.

### Option C4 — Design-only for now

No real source is ingested; use synthetic/non-sensitive examples until an approved private target exists.

Advantage: safest immediate preparation.

Risk: delays proof of real business value.

### Planner recommendation

Use a dedicated or existing **approved private repository** when real source is selected. Until then, keep this target design-only or use non-sensitive representative tasks; do not create a public repository that later receives private code.

## OR-07B — Language-teacher target and conversation archive

### Option L1 — Private structured target repository/store plus separate private cold archive **(planner recommendation)**

- compact target truth, learner evidence, plan, corrections, and versions in a private approved structured store;
- complete conversation exports in a private local/cloud archive outside public Git;
- repository/store keeps hashes, safe pointers, preservation level, and approved summaries.

Advantages:

- normal runtime remains compact;
- complete evidence is available for longitudinal review;
- large or sensitive exports do not clutter Git history.

Risks:

- pointers/backups must be tested;
- archive access and retention need an Owner policy.

### Option L2 — All material in a private Git repository

Advantages:

- one versioned location;
- hashes and history are straightforward.

Risks:

- complete conversations may be large and sensitive;
- Git deletion does not erase history;
- ordinary runtime may be tempted to read too much.

### Option L3 — Local/private cloud archive only, with no repository yet

Advantages:

- low exposure and easy exact export retention.

Risks:

- target truth/current state may be less structured;
- no standard write/review workflow;
- pointer and backup discipline becomes critical.

### Option L4 — Provider-native chat history/library as the sole store

Advantages: minimal setup.

Risks:

- provider-dependent access, export, retention, search, context, and migration behavior;
- insufficient control as the only long-term truth/source store;
- product changes may break portability.

Not recommended as the sole durable source, though it may remain an auxiliary copy.

### Option L5 — Defer storage and continue only transient practice

No durable learner model is adopted yet. This may be acceptable for a few exploratory sessions but does not satisfy the intended persistent system.

## Required answer content

The Owner may decide:

- preferred option or combination for code;
- preferred option or combination for language learning;
- whether complete originals may enter any Git repository;
- who controls access;
- whether exact locations are decided now or only before first material ingestion;
- any employer, customer, legal, privacy, or device constraints.

## Deferral

Safe default:

- code target remains design-only/non-sensitive until an approved private repository exists;
- language target uses no public-Git personal material and plans for private structured truth plus a private cold archive;
- exact services/paths remain undecided.

## Escalation

Any actual private-material ingestion, visibility decision, external sharing, credentials, customer/work source, or provider data-use claim requires a separate current preflight and explicit authorization.

---

# OR-08 — Which system should enter bounded real use first?

## Background

The urgent plan aims to prove value quickly, test Meta-Agent's original purpose, and expose failures through real use. Starting everything simultaneously may create review overload; waiting for Meta-Agent to become complete may repeat the old slow path.

## Options

### OR-08-A — Meta-Agent design pilot first, then both targets

Meta-Agent receives a narrow, public/non-sensitive, design-only scope: frame the two needs and produce target package candidates.

Advantages:

- directly tests Meta-Agent's original value;
- may reduce duplicated design work;
- produces comparable packages for later next-tier execution.

Risks:

- Meta-Agent is currently inactive and has pending implementation-readiness work;
- activation/pilot preparation may delay actual user value;
- a failed Meta-Agent design run could become another abstract campaign.

### OR-08-B — Language teacher/practice Agent first

Begin low-risk text practice, evidence capture, user correction, and feedback after storage/authority baseline is set.

Advantages:

- existing learning activity provides immediate real tasks;
- lower code/customer-security risk;
- quickly tests long-term conversational memory and handoff.

Risks:

- private conversation handling must be resolved;
- voice/transcription and provider limitations may confound assessment;
- teaching quality requires longitudinal evidence.

### OR-08-C — Code-library system first

Begin with non-sensitive or approved representative code/business-function tasks.

Advantages:

- highly tangible artifacts and mechanical tests;
- strong fit for repository-backed memory and provenance;
- exposes reuse/compatibility and cross-repository issues.

Risks:

- real work source may be sensitive;
- target repository/toolchain may not be ready;
- risk of spending time on infrastructure before a safe task exists.

### OR-08-D — All three in parallel

Advantages:

- fastest breadth of evidence;
- compares meta-system and target behavior immediately.

Risks:

- high Owner review burden;
- unclear attribution of failures;
- shared catalogue/method changes may create conflicts;
- scarce frontier attention is divided.

### OR-08-E — Hybrid sequence **(planner recommendation)**

1. Prepare a narrowly bounded Meta-Agent **design-only** pilot for the two target packages, without private material or target writes.
2. In parallel or immediately afterward, begin a low-risk language-teacher pilot once private storage and correction rules are set.
3. Keep the code-library target in design/storage setup until a safe repository and representative non-sensitive/approved tasks are selected, then start without waiting for all other work to finish.

Advantages:

- tests Meta-Agent without making it the only gate to real use;
- produces immediate language-learning evidence;
- avoids unsafe code ingestion;
- permits later concurrency because targets have separate truth stores.

Risks:

- still requires coordination across two early tracks;
- Meta-Agent pilot activation and language privacy need frontier/human decisions;
- code value arrives later.

### OR-08-F — Another sequence

The Owner may define a custom order, a time-boxed trial, or one target only.

## Deferral

Safe default: prepare target packages but do not activate or ingest material. This preserves options but does not satisfy the urgent real-use objective for long.

## Escalation

Final Meta-Agent pilot activation, target repository creation, private storage, and allowed task actions return to frontier/human planning after the Owner chooses the sequence.

---

# OR-09 — Which product/provider questions should be decided now, and which should be deferred?

## Background

The Owner wants a persistent catalogue of available model abilities, subscriptions, settings, software surfaces, and Skills. However, these facts change quickly and were not verified during MNEMOSYNE-200. The present interview should not turn stale memory or model self-report into product truth.

## Candidate categories

### Decide now as Owner preferences

- which providers/subscriptions the Owner expects to use;
- cost/quota priorities;
- preference for web, desktop, mobile, CLI, or repository-based work;
- tolerance for manual export/upload;
- privacy and local-storage preferences;
- which target needs text, voice, code execution, repository write, or research.

### Verify later as current facts

- exact model names and availability;
- current plan prices, quota, context, file limits, and tool access;
- exact Claude Skills semantics;
- ChatGPT Project/Memory/App/connector behavior;
- Voice transcript/export and speech-recognition behavior;
- repository completeness and write actions;
- current privacy/data-use/retention settings.

## Options

### OR-09-A — Defer all product implementation choices until one target package is selected **(planner recommendation)**

Verify only the smallest facts needed for that target.

### OR-09-B — Build a small current comparison before choosing the first target surface

Useful if product capability materially changes launch order.

### OR-09-C — Populate a broad provider catalogue now

Not recommended: high time cost and rapid staleness before actual target decisions.

### OR-09-D — Other

The Owner may identify one urgent product fact that should be verified immediately.

## Required outcome

Record:

- Owner preferences;
- product facts that remain unknown;
- which first target decision will trigger verification;
- whether any question needs ordinary web verification, Deep Research, Fable, or a bounded behavior test.

## Deferral

Safe default: do not select a provider adapter yet; preserve portable target capabilities and verify current product facts just before packaging/launch.

## Escalation

The interviewer must stop rather than answer current product facts from memory. Research execution, quota, purchase, connector activation, and provider selection remain Owner actions.

---

# Final review confirmation

After OR-01 through OR-09, the interviewer should present:

1. confirmed decisions;
2. provisional decisions;
3. deferred items;
4. rejected premises/options;
5. corrected interpretations;
6. external fact checks required;
7. frontier adjudications required;
8. one proposed next safe action.

The interviewer must ask the Owner to confirm or correct this final summary.

Completion does **not** authorize repository write. If the Owner wants the result saved, the Owner should issue a separate message such as:

> 将刚刚确认的 MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-001 人工抉择结果按包内结果模板写入 Mnemosyne，新建一个任务级分支和 draft PR；不要修改执行源、Meta-Agent 或任何目标仓库。
