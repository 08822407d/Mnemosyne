# Target Agent Container, Evolution, and Dependency Responsibility Model — Candidate v0.1

> Frontier-designed candidate that consolidates the Owner-confirmed OR-06/OR-07 architecture and advances three unresolved issues: multiple logical Agents in one repository, upstream meta-system changes versus business/API changes, and library-versus-consumer dependency responsibility. It is not execution source, target truth, or implementation authorization.

```yaml
candidate_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-001
version: 0.1.0
task_id: MNEMOSYNE-205
status: frontier_candidate_pending_owner_review_and_bounded_validation
owner_result_ref: notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002.md
selection_ref: notes/first-three-system-capability-selection-v0.3.md
execution_source_modified: false
target_repository_write_authorized: false
automatic_propagation: false
```

## 1. Problem and selected scope

The prior planner model equated safe concurrency too closely with separate physical repositories and did not clearly separate:

1. changes to an Agent's own operating system;
2. changes to the business requirements it serves;
3. changes to a managed library/API and consumer adaptation.

The Owner also rejected parent-repository bootstrap and questioned an exhaustive library-side consumer reverse index.

This candidate designs one logical model around those decisions.

## 2. Owner-confirmed invariants

1. A concrete business Agent must have a formal destination repository/store **before** substantive design/build starts.
2. Mnemosyne, Meta-Agent, or another parent Agent repository must not host a complete live bootstrap target intended for later migration.
3. A physical repository may contain one or several logical Agents.
4. Each logical Agent must retain an unambiguous authority, writer, and target-truth boundary.
5. Parent/meta-systems may keep bounded design, provenance, feedback, and impact pointers, but not a competing editable target truth.
6. Backups are required and remain non-authoritative.
7. Upstream changes create target-specific review/adoption candidates; they do not propagate automatically.

## 3. Logical objects

### 3.1 Physical repository/store

A storage and Git/other-versioning container. It is not itself the target authority boundary when several Agents share it.

### 3.2 Target Agent root

A declared logical root for one Agent, for example:

```text
targets/<target-id>/
```

The exact path is target-specific. Required meaning:

- the target's approved behavior/specification;
- selected capability record;
- current state and handoff;
- target-specific memory/data rules;
- target-owned implementation and evaluation records;
- target-local authority map.

### 3.3 Target authority map

Minimum candidate fields:

```yaml
target_authority:
  target_id:
  physical_repository_or_store:
  target_root:
  current_truth_paths: []
  active_writer:
  allowed_secondary_writers: []
  shared_object_refs: []
  parent_meta_refs: []
  backup_refs: []
  prohibited_writers: []
```

The map must resolve conflicts without relying on the newest timestamp alone.

### 3.4 Shared object

An object intentionally used by several co-located Agents, such as shared code, a common schema, or a common provider adapter.

Every shared object needs:

```yaml
shared_object_authority:
  object_id:
  canonical_path:
  owner:
  allowed_writers: []
  allowed_readers: []
  version:
  change_protocol:
  dependent_target_refs: []
  reconciliation_required: true | false
```

A path is not shared merely because several Agents can read it. Shared status must be explicit.

## 4. No-parent-bootstrap workflow

Required order:

1. preserve the initial user requirement and sensitivity at a safe source location;
2. choose or create the formal target repository/store;
3. declare target root and authority map;
4. create the smallest target-owned spec/current-state structure;
5. record capability selection/adaptations;
6. design and build only inside the formal target boundary;
7. keep parent/meta outputs as bounded design packages or pointers;
8. test fresh-session recovery from target-owned sources.

Temporary complete target construction inside a parent repository is prohibited by default.

A small design brief in the parent repository is allowed when it is clearly a parent-owned design artifact and not a live target truth.

## 5. Co-located multiple-Agent repository model

### 5.1 Default layout candidate

```text
targets/<agent-a>/...
targets/<agent-b>/...
shared/<shared-object-id>/...
repository-governance/...
```

This is an example, not a mandatory directory naming standard.

### 5.2 Concurrent work

Two tasks may proceed concurrently in the same physical repository when:

- each task has a different primary target root;
- neither changes a shared object or repository-wide governance;
- branch/PR scopes and paths are explicit;
- neither depends on the other's uncommitted result;
- final mechanical diff checks confirm no cross-target edits.

Serialize or explicitly reconcile when:

- both tasks change the same target root;
- either task changes `shared/` or repository governance;
- a target-root migration or authority change occurs;
- a shared schema/provider adapter version affects both;
- one task changes a parent capability selection used by the other.

### 5.3 PR lineage

The repository may host multiple open PRs for different target tasks when their task IDs, branches, target roots, and reconciliation rules are distinct.

The current Mnemosyne one-task/one-canonical-PR safety rule still applies **per task**. This candidate does not approve parallel variants for one task.

A merge instruction must identify the target and exact changed-path scope.

### 5.4 Cross-target shared objects

A target may depend on a shared object without owning it. Changes are governed by the shared object's owner and change protocol.

No Agent may silently copy a shared object into its target root and independently evolve it as another current version.

## 6. Four separate evolution axes

### Axis A — Meta-system/capability change

Examples:

- Mnemosyne changes memory architecture;
- Meta-Agent changes multi-Agent coordination;
- a common capability or packaging method changes.

Primary impact target:

- the target Agent's own specification;
- memory schema and storage organization;
- instructions and behavior;
- handoff/current-state method;
- authority, evaluation, and collaboration protocols.

Process:

1. identify targets whose capability-selection records use the changed version;
2. classify impact: none, future-only, review, adapt, rebuild, migrate, re-evaluate, or reapprove;
3. create a target-specific candidate;
4. target authority/Owner decides adoption;
5. implement and validate inside the target boundary;
6. update parent impact records without becoming the target writer.

A meta-system change does not imply a business/API change.

### Axis B — Business requirement change

Primary impact target:

- business rules;
- design decisions;
- implementation;
- tests and acceptance;
- possibly business data.

It uses requirement intake, conflict review, approval, and traceability.

It does not automatically rewrite the Agent's operating system.

### Axis C — Managed library/API change

Primary impact target:

- public/private API contract;
- semantic version or compatible identity;
- tests;
- change log;
- migration guidance.

It does not automatically change the Agent's memory/behavior architecture.

### Axis D — Provider/product adapter change

Examples:

- Skill/module semantics;
- context/file limits;
- repository connector behavior.

Primary impact target:

- provider-specific packaging or adapter;
- capability implementation details;
- current-product evidence records.

It should not redefine the portable capability unless repeated evidence shows the capability itself is wrong.

## 7. Library-versus-consumer dependency responsibility candidate

### 7.1 Default recommendation

The library/code Agent should own:

- current API and compatibility contract;
- version identity;
- breaking-change classification;
- release/change notes;
- migration instructions and examples;
- deprecation and security notices;
- tests for the published contract.

Each consuming project Agent should own:

- its dependency declaration and selected version;
- its own API usage analysis;
- upgrade decision and timing;
- project-local migration;
- project tests and acceptance.

An exhaustive library-maintained reverse index of every consumer/API use is **not required by default**.

### 7.2 Why this matches the Owner direction

- avoids a central registry that becomes stale;
- preserves target-local ownership;
- follows a familiar library-publication/consumer-upgrade division;
- lets an Agent rediscover project-local usage from its own code and dependency metadata.

### 7.3 Optional registration exceptions

A bounded consumer registry may be justified only when a separately reviewed case shows material value, such as:

- a controlled organization explicitly registers all consumers;
- a security emergency needs proactive notification;
- a coordinated breaking migration has a fixed participant set;
- consumer-side usage cannot be reliably rediscovered;
- contractual support requires impact tracking;
- the Owner accepts the maintenance burden.

The registry must then state scope, freshness, owner, and removal/reconciliation rules.

### 7.4 Current status

This recommendation remains a frontier candidate because the Owner requested later engineering/research support before final adoption.

## 8. Backup model

### 8.1 Topology candidate

```text
authoritative primary
  -> backup repository A
  -> backup repository B
```

A and B should be operationally independent enough that one failure is unlikely to remove both.

### 8.2 Authority

- only the primary is current truth;
- backup writes are one-way synchronization from an identified primary version;
- no independent edits;
- every snapshot records source commit/version;
- restore creates or repairs a primary; it does not make the backup a concurrent writer.

### 8.3 Scope by irreconstructability

- Mnemosyne/Meta-Agent: complete backup preferred;
- code target: requirements, designs, decisions, feedback, and history fully backed up; code scope may reflect reconstructability;
- language target: structured learner truth and required-period conversation archive backed up according to retention/privacy policy;
- target-specific exceptions require explicit rationale.

### 8.4 Restore proof

A backup is not considered reliable until a bounded restore test can recover:

- target identity and authority;
- selected capability version;
- current state/handoff;
- irreplaceable rationale/history;
- integrity relation to the recorded source version.

## 9. Design rationale

The selected model treats the logical target boundary as the unit of authority and the physical repository as a container. This preserves the Owner's permission for multiple Agents to share a repository without returning to parent-repository bootstrap or dual writers.

It separates Agent-internal evolution from business and API evolution so that improvements to Mnemosyne/Meta-Agent can reach target Agents without falsely implying that their business outputs or public APIs must change.

It adopts consumer-owned dependency analysis as the default candidate because an exhaustive library-side registry creates recurring maintenance and staleness cost. Explicit high-value exceptions remain possible.

## 10. Assumptions and risks

Assumptions:

- target roots and changed paths can be made mechanically visible;
- consuming Agents can normally rediscover their own dependency usage;
- shared objects are a minority and can be explicitly governed;
- backup repositories can be made non-editable in practice.

Risks:

- same-repository tasks may still conflict through repository-wide files;
- a supposedly target-local change may affect shared objects;
- target selection records may become stale;
- consumer-side discovery may miss dynamic or indirect API use;
- backups may drift or fail restore;
- too many always-active capability rules may burden current models.

## 11. Adoption and validation gate

This candidate should not be adopted by a target until the bounded validation plan passes the relevant scenarios and the Owner reviews:

- same-repository target isolation;
- shared-object conflict/reconciliation;
- meta-capability impact without business/API conflation;
- consumer-owned migration adequacy and exception triggers;
- backup restore and non-authority.
