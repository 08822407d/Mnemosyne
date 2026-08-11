# Minimum Real-Use Launch Baseline — Candidate v0.1

> Non-execution-source launch-preparation baseline for Meta-Agent and the first two real target needs. It defines what should exist before bounded use and what should deliberately remain deferred. It does not activate Meta-Agent, create target repositories, ingest private material, start a pilot, or authorize repository writes.

```yaml
baseline_id: MNEMOSYNE-MINIMUM-REAL-USE-LAUNCH-BASELINE-001
task_id: MNEMOSYNE-200
version: 0.1.0
status: candidate_for_owner_review_and_target_intake
systems:
  - Meta_Agent
  - work_business_function_code_library
  - long_term_language_teacher_and_practice_Agent
execution_source_modified: false
operational_activation_authorized: false
pilot_authorized: false
```

## 1. Launch philosophy

The first useful version should begin real work before the system is complete, provided that it:

- preserves irreplaceable source information;
- has one explicit target truth source and owner;
- separates current truth, evidence, raw source, candidates and navigation;
- can resume in a fresh conversation;
- records important decisions and failures;
- can be revised, migrated or rolled back;
- does not expose private material or perform unauthorized writes.

The baseline optimizes for **recoverability, reversibility and visible value**, not maximum design coverage.

## 2. Common hard floor

Every first target should have or explicitly decide these items before bounded real use:

1. **Owner and scope** — target purpose, owner, initial non-goals and exact pilot boundary.
2. **Target-local truth** — one file or declared store that controls current target behavior.
3. **Source policy** — where complete requirements, conversations, reports, code and private material are preserved; what is exact, normalized or pointer-only.
4. **Authority map** — who may change target truth, memory, code, provider configuration and external systems.
5. **Selected capability record** — catalogue version plus required, adapted, experimental, deferred and rejected capabilities.
6. **Current state and handoff** — completed, in progress, blocked, unknown and one safe next action.
7. **Decision and change history** — important rationale, supersession and version effect.
8. **Feedback/issue record** — failures, friction, user corrections, missing memory and rework.
9. **Evaluation and stop criteria** — what counts as useful, unsafe, misleading or too burdensome.
10. **Upgrade/rollback reference** — previous state, compatibility and recovery route.

For a low-volume first version these may be compact files or sections; they do not require a database or service.

## 3. Not required before first use

Do not block initial use on:

- complete automation or automatic writeback;
- RAG, embeddings or a vector database;
- a universal Agent ontology or compiler;
- complete provider/model/setting research;
- automatic cross-target methodology propagation;
- full historical capability backfill;
- perfect teaching or coding evaluation metrics;
- multi-Agent runtime coordination;
- provider-neutral Skill implementation;
- proof that every future migration will be inexpensive.

These become candidates only when real use supplies a concrete need.

## 4. Meta-Agent bounded-use candidate

### 4.1 Purpose of the first real use

Use Meta-Agent to produce and review target-Agent design packages for the two real needs:

1. work/business-function code-library system;
2. long-term language teacher/practice Agent.

This directly tests Meta-Agent’s original value proposition rather than an unrelated synthetic benchmark.

### 4.2 Minimum preconditions

Before any bounded operational pilot:

- current Meta-Agent target truth remains the sole authority;
- the Owner explicitly authorizes an exact pilot scope;
- applicable health-review P0/P1-equivalent findings are checked, fixed or explicitly deferred with residual risk;
- no private source, customer material or complete personal learning history is required;
- exact outputs, acceptance criteria, stop conditions and repository write boundaries are frozen;
- initial memory-system foundation is adopted only to the minimum needed for fresh-session recovery and case/feedback records;
- Meta-Agent-owned behavior guidance is reviewed separately rather than importing all Mnemosyne maintenance guidance.

### 4.3 First candidate tasks

- frame each real need and separate confirmed requirements, unknowns and assumptions;
- select a minimum Agent capability package from the catalogue;
- decide one Agent versus a workflow/team arrangement;
- draft target-local memory, authority, handoff and evaluation files;
- identify provider-specific packaging questions without pretending they are already resolved;
- return design rationale, target-specific risks and questions requiring Owner decisions.

### 4.4 What the first pilot can establish

- whether Meta-Agent reduces repeated design work;
- whether it identifies omitted Agent capabilities the user would not recall unaided;
- whether target-specific facts remain separated from general methodology;
- whether its outputs are usable by a next-tier implementation model;
- whether review burden is lower than designing directly from a blank prompt.

It cannot establish production readiness or universal Agent-design optimization.

## 5. Work/business-function code-library launch candidate

### 5.1 Initial purpose

Capture real development needs, business rules, design decisions, reusable implementation and verification evidence so repeated work can accumulate into a governed business-function/code asset library.

### 5.2 Minimum target package

Candidate compact layout:

```text
current/approved-spec.md
current/active-context.md
authority/source-and-owner-map.md
requirements-and-decisions.md
function-and-code-catalog.md
evaluation-and-issue-log.md
handoff/handoff-current.md
history/version-migration-log.md
```

The exact layout is an Owner/target decision. The point is to preserve roles, not require these exact filenames.

### 5.3 First real task set

Choose a small group of non-sensitive representative tasks, for example:

- one new bounded business function;
- one correction to an existing function or business rule;
- one candidate reuse of a function in another context;
- one case where reuse should be rejected because assumptions differ;
- one change requiring version/compatibility handling.

For each task record:

- original requirement/source;
- project-local versus reusable scope;
- design decision and assumptions;
- implementation and tests;
- review result and user usefulness;
- discovered missing capability or excessive process burden.

### 5.4 Stop conditions

Stop or narrow the pilot if:

- private/customer/source material would enter an unapproved repository;
- the Agent invents business rules or authorization;
- reusable code is promoted without compatibility evidence;
- target and consuming-project truth become confused;
- verification/rework costs exceed the value of the produced asset;
- concurrent repository work cannot preserve exact write order and ownership.

## 6. Long-term language teacher/practice launch candidate

### 6.1 Initial purpose

Provide sustained language teaching and practice that records detailed evidence of performance and progress, adapts teaching plans, and avoids turning sparse interaction into fixed learner labels.

### 6.2 Minimum target package

Candidate logical roles:

```text
current target teaching/behavior spec
current learning goals and plan
learner evidence ledger
error/hypothesis/correction ledger
session activity and assignment record
feedback/evaluation log
handoff/current state
version/change history
private cold conversation archive or safe pointer
```

Complete personal conversations and sensitive learning records default to approved private cold storage, not public Git.

### 6.3 First real task set

Start with ordinary low-risk learning activities rather than a high-stakes assessment:

- short language conversation/practice;
- one focused explanation or correction task;
- one production task such as speaking or writing;
- one delayed reuse/review task;
- one explicit user feedback/reflection turn.

Record evidence separately for vocabulary, grammar, comprehension, spoken/written production, coherence, pragmatics and task completion only where the activity actually provides evidence.

### 6.4 Stop conditions

Stop or revise if:

- the Agent invents stable proficiency, personality or learning-style claims from weak evidence;
- speech-recognition or tool errors are mistaken for language ability;
- the user cannot correct or delete an interpretation;
- the system stores private conversations in an unapproved location;
- adaptation becomes opaque, patronizing or unhelpfully burdensome;
- the system cannot distinguish immediate fluent repetition from independent retention/transfer.

## 7. Shared test–feedback–improvement loop

For each target task:

1. record the exact task and source inputs;
2. record selected capabilities/provider adapter version;
3. perform the bounded task;
4. collect mechanical evidence where possible;
5. collect concise user feedback on usefulness, burden and mistakes;
6. classify failures: source loss, retrieval miss, authority error, handoff error, business/teaching error, provider/tool error, excessive process or other;
7. decide whether the fix belongs only to the target, the reusable capability catalogue, Meta-Agent methodology or current provider adapter;
8. create a candidate change with validation and rollback;
9. preserve negative evidence and do not auto-promote it to a global rule.

Review after enough representative tasks to reveal patterns; do not fix a universal numeric cadence before use.

## 8. Evidence package for later full-history review

Normal runtime should use compact current state. A later frontier review may use:

- complete pre-pilot requirements/design conversation;
- exact task inputs and outputs;
- current handoff and target state at each transition;
- complete representative execution conversations;
- user corrections and result records;
- target changes and migration records;
- review rubrics fixed before inspecting preferred outcomes where practical.

These full archives remain cold/on-demand and are not evidence that the runtime loaded them.

## 9. Model and tool split

### Frontier/open-ended reasoning

- reconstruct target purpose and ambiguous requirements;
- decide authority, privacy, product architecture and target truth;
- select or change general capabilities/methodology;
- adjudicate severe failures or migration impact;
- perform longitudinal full-conversation review.

### Validated next-tier candidate

- execute frozen target tasks;
- maintain bounded current state, handoff and ledgers;
- apply approved templates and low-risk updates;
- produce draft capability-selection and migration mappings;
- stop and escalate on semantic/authority conflict.

### Mechanical support

- path, ID, version and hash checks;
- changed-file allowlists and diffs;
- source-ref existence;
- test/build results;
- required-field and forbidden-material checks.

### Human-only decisions

- purpose and target acceptance;
- sensitive material/storage approval;
- target truth/authority changes;
- operational activation;
- methodology promotion;
- subscription/quota and provider selection.

## 10. Success signals

The first phase is valuable when it:

- begins real work without losing source or authority;
- reduces repeated explanation/design effort;
- recovers accurately in a fresh conversation;
- produces visible useful code assets or language-learning progress;
- exposes design defects early;
- permits low-cost correction and rollback;
- keeps maintenance/review burden acceptable;
- identifies which common capabilities are genuinely reusable.

It is not necessary to prove that the system is complete or permanently optimal.

## 11. Owner decisions required for launch

Before any actual pilot, the user must separately decide:

- which target starts first or whether the two proceed in parallel;
- exact target repository/store and visibility;
- storage route for private source/conversation originals;
- exact initial real tasks and allowed materials;
- Meta-Agent pilot activation scope and health-review disposition;
- allowed repository/tool actions;
- provider/product surfaces and quota;
- acceptance, stop and rollback criteria.

## 12. Design rationale

The baseline deliberately guarantees source preservation, target authority, fresh-session continuity and reversible feedback while deferring advanced automation. These properties remain valuable even as models improve; most other complexity can be added when real failures demonstrate its need.
