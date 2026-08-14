# Target Agent Container, Evolution, and Dependency Responsibility Model — Candidate v0.2

> Owner-confirmed provisional architecture baseline prepared for bounded public/synthetic validation. This file is not Mnemosyne's execution source, target truth, implementation authorization, target adoption, or proof that the model works in practice.

```yaml
candidate_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-002
version: 0.2.0
task_id: MNEMOSYNE-209
status: owner_confirmed_provisional_baseline_prepared_for_validation
supersedes_for_candidate_scope: notes/target-agent-container-evolution-and-dependency-model-candidate-v0.1.md
owner_result_ref: notes/owner-decision-results/MNE-TARGET-LIFECYCLE-OWNER-REVIEW-RESULT-001.md
owner_review_package_ref: notes/owner-review-packages/target-agent-lifecycle-v0.1/README.md
frontier_adjudication_ref: notes/target-agent-container-evolution-and-dependency-frontier-adjudication-v0.1.md
validation_ref: notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.2.md
execution_source: false
target_adoption_authorized: false
validation_execution_authorized: false
automatic_cross_target_propagation: false
parent_side_substantive_downstream_content_default: prohibited_pending_future_evidence
```

## 1. Status and intended use

Candidate v0.2 converts the Owner-confirmed TLR-01 through TLR-05 result into a sufficiently frozen architecture contract for bounded validation.

It preserves explicit deferrals rather than pretending every mechanism is mature. In particular:

- TLR-04 remains deferred; no new substantive downstream content is placed in parent/meta repositories by default;
- TLR-03 does not adopt a complex universal change taxonomy or a mandatory fine-grained change-event schema;
- the exact concurrency proof, documentation schema, backup provider topology and validation execution surface remain unresolved implementation questions.

This candidate may be used only to design or run a separately authorized public/synthetic validation. It must not be adopted by a real target before validation review and a target-specific Owner decision.

## 2. Fixed architecture invariants

1. A concrete target Agent needs a formal target-owned repository/store before substantive target design or construction begins.
2. A parent/meta repository must not host a complete live target bootstrap intended for later migration.
3. One physical repository may contain one or several logical Agents.
4. Each logical Agent retains an unambiguous target root, current-truth boundary and authority owner.
5. A bounded task writer does not become a second authority owner merely because it is permitted to edit files.
6. Upstream/meta-system changes do not automatically propagate into downstream target truth.
7. Backups are required, non-authoritative and recover from an identified source version.
8. Target and product adoption remain target-owned decisions.
9. Validation preparation, validation execution, global architecture acceptance and per-target adoption are separate gates.

## 3. Authority unit, write policy and task contract

### 3.1 Authority unit

The authority unit is one logical target boundary, not the whole physical repository.

A target should identify at least:

```yaml
target_authority:
  target_id:
  physical_repository_or_store:
  target_root:
  authority_owner:
  canonical_truth_paths: []
  prohibited_writers: []
  shared_object_refs: []
  backup_refs: []
```

The exact file/schema representation is target-specific. The required meaning is:

- which logical target is being governed;
- where its authoritative truth lives;
- who decides what is current;
- which paths or objects are included;
- which actors or locations must not become competing writers.

### 3.2 Task writer versus authority owner

A task actor may receive permission to perform one bounded modification without acquiring ongoing authority over the target.

Every material repository-writing task should therefore have a task-local write contract that states, in a mechanically checkable form where possible:

```yaml
task_write_contract:
  task_id:
  primary_target:
  base_ref:
  primary_writer:
  exact_write_set: []
  read_or_dependency_set: []
  shared_or_repository_global_objects_touched: []
  conflicting_active_write_sets: []
  authorization_ref:
  decision: proceed | serialize | reconcile | blocked
  final_diff_verification_ref:
```

The exact schema may evolve, but the contract must preserve the task identity, authorized scope, conflict decision and final verification evidence.

## 4. Same-repository concurrency

### 4.1 Scope classes

For concurrency decisions, classify a task only as finely as is operationally useful:

1. **target-local and disjoint** — exact write set is confined to one target and mechanically disjoint from other active writes; no shared/global object changes;
2. **shared-object** — a declared shared object changes;
3. **repository-global** — repository governance, root tooling/configuration, generated global state, lockfiles or other repository-wide objects change;
4. **unknown** — exact scope or dependency cannot be established.

### 4.2 Conditional concurrency rule

Two distinct tasks may proceed concurrently in one physical repository only when all are true:

- each has a distinct task ID and canonical branch/PR lineage;
- exact write sets are declared;
- the write sets are mechanically disjoint;
- neither touches a shared object, repository-global object, the other target root or a common authority record;
- neither depends on the other's uncommitted result;
- the final path/diff check confirms no cross-target edit.

### 4.3 Serialize or reconcile

Serialize, reconcile explicitly or block when:

- write sets overlap;
- either task changes a shared or repository-global object;
- scope is unknown;
- an authority map or target-root migration changes;
- merge order creates a semantic dependency;
- a common capability/provider adapter version is changed for both targets.

Git text mergeability is not sufficient evidence of semantic non-interference.

### 4.4 One task, one canonical lineage

Conditional concurrency applies to **distinct tasks for distinct scopes**. It does not authorize parallel competing branches or PRs for one task. The repository's one-task/one-canonical-PR guard remains applicable per task.

## 5. Shared objects and dependency responsibility

### 5.1 Shared object boundary

An object is shared only when its shared status, canonical location, owner and change protocol are explicit. Being readable by multiple Agents does not by itself make an object shared.

A shared object should identify:

```yaml
shared_object_authority:
  object_id:
  canonical_path_or_store:
  authority_owner:
  allowed_task_writers: []
  contract_or_interface_ref:
  version_or_compatible_identity:
  change_protocol_ref:
```

No target may silently copy a shared object into its own root and evolve the copy as another current version.

### 5.2 Library/code-Agent responsibility

The library/code Agent owns accurate description of its own public or private contract, including as applicable:

- current interfaces and behavior;
- version or compatible identity;
- compatibility and material breaking changes;
- deprecations and removals;
- security-relevant change notices;
- migration actions and examples;
- tests for the published contract.

The library Agent does **not** by default own an exhaustive authoritative map of every consuming project and every use site.

### 5.3 Consuming-project responsibility

Each consuming project Agent owns:

- its dependency declaration and selected version/identity;
- discovery of actual project usage;
- the timing and scope of project rebuild/upgrade;
- project-local migration;
- project tests and acceptance.

The project Agent performs impact analysis when a rebuild, upgrade or other real trigger occurs. It reads the library's relevant version-to-version changes and combines them with the project's own code and dependency truth.

### 5.4 Human-facing and Agent-facing change documentation

The library should provide two semantically coordinated documentation roles.

#### Human-facing change explanation

Minimum contract:

- naturally and concisely explains important changes;
- supports human review and understanding;
- may include rationale, examples and richer material later;
- is not assumed to contain every detail needed for Agent-led project reconstruction.

#### Downstream-project-Agent change explanation

Semantic contract:

- identifies affected public symbols, interfaces, behavior, configuration or data forms where known;
- states the previous and new contract/behavior;
- states compatibility and affected version/use ranges where known;
- gives replacement or migration actions;
- includes before/after examples when they materially reduce ambiguity;
- gives downstream verification guidance;
- preserves source evidence or design/test references when useful.

This candidate does not require a particular file name, directory, serialization format or one-versus-two canonical fact-source implementation. It does require that the two forms do not silently contradict each other.

### 5.5 Documentation overview

The library project should expose one discoverable documentation overview for consuming Agents. It states:

- which non-code documents exist;
- what each document is for;
- where each document is located;
- when an Agent should read it;
- where the human-facing and Agent-facing change information lives and how their roles differ.

### 5.6 Impact views and registration exceptions

A repository/organization-level impact view may be generated as an optional convenience. It is not baseline truth and is not required for the Owner's on-demand rebuild model.

A manual consumer registration/notification mechanism is also not a baseline requirement. A later bounded exception may be justified for security, fixed coordinated migrations, contractual support or usage that cannot be rediscovered. Any such exception requires its own scope, owner, freshness/expiry rule and adoption decision.

## 6. Change routes and no automatic propagation

### 6.1 Practical route distinction

Change categories should exist only when they support real decisions, provenance or routing. Current useful routes include:

- upstream/meta-system method or capability change;
- target-local business requirement change;
- code-library requirement synthesized from business needs;
- material API/design change;
- provider/product-adapter or physical-container change when that distinction proves useful;
- `other_or_unknown` when a real case does not fit cleanly.

No mechanism should force every case into an artificial fine-grained taxonomy.

### 6.2 Upstream-initiated downstream work

An upstream/meta Agent may be the directional initiator and designer for a downstream change only through a bounded Owner-initiated task.

Required semantics:

- the Owner or target authority identifies the downstream target and purpose;
- the upstream system may research/design the change;
- any actual downstream write requires a separate target-writing authorization and exact scope;
- adoption remains a downstream/Owner decision;
- no standing cross-target writer authority is created;
- no automatic propagation is permitted.

### 6.3 Minimum durable change evidence

Before practice supports a richer schema, preserve at least:

- original requirement/source input or a safe exact reference;
- real entry route and affected target when material;
- requested change and authorization/adoption state;
- explicit material API changes;
- unresolved assumptions or unknowns;
- enough context for a capable later Agent to reconstruct why the change exists.

A universal mandatory `primary_axis + secondary_effect` record is not adopted. It may later be introduced only if real-use or synthetic evidence shows practical benefit.

### 6.4 Route interactions

Different routes may have real consequences for one another, but those consequences are not assumed.

Examples:

- a business requirement may create an API-design candidate;
- an upstream method change may create a downstream-Agent internal migration candidate;
- a provider-adapter failure may reveal a portable capability defect.

Each consequence needs explicit reasoning and the authority appropriate to the affected target/object.

## 7. Target destination and parent/meta boundary

### 7.1 Destination before substantive design/build

Required order:

1. preserve the initial requirement/source safely;
2. choose or create the formal target repository/store;
3. declare target identity, root and authority boundary;
4. create the smallest target-owned current/spec structure;
5. perform substantive design and construction inside the target boundary.

If a formal destination does not exist, substantive target construction blocks.

### 7.2 No parent bootstrap

Mnemosyne, Meta-Agent or another parent/meta repository must not contain a complete live target tree, target execution source, target current state, editable target memory, target business truth or a target handoff intended for later migration.

### 7.3 No new substantive parent-side downstream content

Candidate v0.1's proposed narrow parent-owned substantive design-brief exception is **not active** in v0.2.

Current safe default:

- do not create new substantive downstream-Agent content in a parent/meta repository merely because the parent designed the target;
- preserve the target's substantive material in the target-owned repository/store;
- use dedicated non-authoritative backups for recovery;
- do not treat the parent/meta repository as a recovery copy.

This does not silently delete already approved minimal meta-level indexes, target identity/provenance pointers or parent-owned method/history records. Their future retention and the exact boundary between a minimal pointer and downstream content remain deferred. They must not be expanded into a substantive target copy under this candidate.

### 7.4 Pre-destination receipt

When a destination is missing, a parent/meta system may record only the minimal blocking receipt and safe source pointer already necessary to explain:

- target identity;
- destination decision still required;
- source location/sensitivity status;
- why substantive construction is blocked.

This receipt must not contain enough target material to operate or reconstruct the target as a live system. Exact minimal content remains a validation question and does not authorize broader parent-side retention.

## 8. Backup model

### 8.1 Authority

Only the authoritative primary is current target truth. Backups are controlled copies from identified primary versions and must not evolve independently.

### 8.2 Candidate topology

```text
authoritative primary
  -> backup location A
  -> backup location B
```

A and B should be independent enough that one account, credential, provider failure or accidental deletion is unlikely to destroy both.

### 8.3 Snapshot identity

Each snapshot should identify at least:

```yaml
backup_snapshot:
  target_id:
  source_repository_or_store:
  source_version:
  created_by_controlled_sync:
  backup_location:
  content_scope:
  integrity_identity:
  independent_editing_allowed: false
  restore_test_ref:
```

### 8.4 Restore proof

A backup is not considered reliable until a bounded restore test can recover:

- target identity and authority;
- selected capability version;
- current state/handoff;
- irreplaceable requirements, rationale and history within the approved backup scope;
- integrity relation to the recorded source version.

Provider, account, privacy and automation choices remain later target/product decisions.

## 9. Adoption and validation gates

### 9.1 Provisional baseline

This v0.2 is the architecture selected for testing. It is not proof or target adoption.

### 9.2 Separate gates

1. **Candidate preparation** — completed by this file.
2. **Validation-package preparation** — may prepare frozen public/synthetic materials without executing them.
3. **Validation execution authorization** — Owner separately selects repository/surface, permissions and run scope.
4. **Validation execution** — frozen scenarios plus mechanical evidence.
5. **Pro/frontier adjudication** — semantic failures and candidate revision.
6. **Global Owner acceptance** — decide whether the architecture is acceptable for future target-specific consideration.
7. **Per-target adoption** — each target separately decides whether/how to adopt and migrate.

No gate implies the next one automatically.

## 10. Explicit deferrals and non-goals

Deferred or not fixed by v0.2:

- exact write-contract file/schema and non-interference algorithm;
- exhaustive concurrency automation;
- exact human/Agent change-document file names, paths, schema and synchronization;
- quantitative proof that the Agent-facing documentation supports reliable migration;
- universal impact views or consumer registries;
- detailed change taxonomy and mandatory primary/secondary-effect schema;
- a substantive parent-owned design brief or a final parent-side minimum-content rule;
- backup providers, account topology, synchronization automation and private-material controls;
- current provider/product implementation facts;
- real target adoption, migration and activation.

This candidate does not authorize GitHub Actions, auto-writeback, RAG, MCP, automatic multi-Agent coordination, target writes, private-material ingestion or external research runs.

## 11. Validation hypotheses and failure risks

Candidate v0.2 remains uncertain about:

- whether disjoint write sets can be established reliably enough to avoid both false locks and missed conflicts;
- whether shared/repository-global dependencies are discovered before concurrent work starts;
- whether the Agent-facing change documentation is sufficient for actual downstream reconstruction;
- whether on-demand project-side discovery misses important dynamic/indirect use;
- whether a simple route distinction preserves enough context without becoming ambiguous;
- whether the no-parent-content default loses useful design history;
- whether minimal pre-destination receipts stay minimal;
- whether backup independence and restore proofs work in practice.

The corresponding validation plan must treat these as falsifiable questions, preserve failures and prohibit silent architecture invention by the executor.
