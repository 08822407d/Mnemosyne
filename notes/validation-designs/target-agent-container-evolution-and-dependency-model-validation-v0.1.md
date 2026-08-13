# Target Agent Container, Evolution, and Dependency Model — Bounded Validation Plan v0.1

> Public/synthetic, no-private-material validation plan for `MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-001`. This file prepares tests only. It does not create a target repository, run an external Agent, use quota, adopt the candidate, or authorize writes outside a separately approved validation task.

```yaml
validation_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-VALIDATION-001
task_id: MNEMOSYNE-205
candidate_ref: notes/target-agent-container-evolution-and-dependency-model-candidate-v0.1.md
status: prepared_not_selected_not_executed
material_class: public_synthetic_only
execution_source_modified: false
```

## 1. Validation objective

Establish whether the candidate can support:

- destination-before-build;
- multiple logical Agents in one repository;
- target-local authority and no competing writer;
- separate Agent-internal, business, API, and provider evolution;
- library-published migration information with consumer-owned adaptation;
- non-authoritative multi-repository backup and restore.

The validation tests the design contract, not a specific provider's current product features.

## 2. Capability split

- Frontier/Pro: adjudicate semantic failures, authority conflicts, and candidate revision.
- Next-tier candidate: execute frozen synthetic scenarios and produce ledgers.
- Mechanical: path allowlists, commit/diff checks, schema fields, source/version identities, restore comparison.
- Human Owner: accept/revise/reject architecture and any future real target adoption.

No named-model adequacy is assumed without observed results.

## 3. Synthetic fixture

A future validation task may create one temporary public/synthetic repository with:

```text
targets/agent-alpha/
targets/agent-beta/
shared/common-schema/
repository-governance/
backups-fixture/
```

All data must be synthetic. No real work code, learner records, credentials, private conversations, or target truth may be used.

## 4. Scenarios

### V1 — Destination-before-build

Attempt to begin Agent Gamma design without a formal target root/store.

Expected:

- substantive target construction blocks;
- only a bounded parent-owned design brief is allowed;
- the result identifies the exact destination decision needed.

Failure:

- complete live target files appear in a parent/meta repository.

### V2 — Two Agents, one repository, disjoint changes

Agent Alpha and Agent Beta receive separate frozen tasks affecting only their own roots.

Expected:

- independent task IDs and branches;
- exact path scopes;
- no cross-root modifications;
- both PRs can coexist when no shared object changes;
- final diff checks pass.

Failure:

- global serialization is imposed without shared-object need;
- one task edits the other's root or repository governance.

### V3 — Shared-object change

Both Agents depend on `shared/common-schema/`; one task changes it.

Expected:

- shared-object owner and change protocol are read;
- affected targets are identified;
- concurrent target-local work either pauses or reconciles;
- no silent copy/fork occurs.

Failure:

- shared object changes without impact handling;
- two current versions appear.

### V4 — Meta-capability update

A synthetic Mnemosyne capability changes target memory layout.

Expected:

- Agent Alpha receives an Agent-internal change candidate;
- business requirements and library API remain unchanged unless separately justified;
- adoption requires target authority;
- parent system remains non-writer.

Failure:

- change automatically propagates;
- business/API changes are assumed merely because Agent internals changed.

### V5 — Business requirement update

A synthetic business rule changes.

Expected:

- requirement/decision/implementation/test trace updates;
- Agent operating system remains unchanged unless an explicit secondary effect is justified.

Failure:

- capability/memory architecture is changed without reason.

### V6 — Library API breaking change

The synthetic library publishes a new version, breaking-change note, and migration guide.

Expected:

- no exhaustive library-side consumer registry is required;
- each synthetic consumer Agent discovers its own usage and prepares migration;
- migration success is tested;
- library records the contract and guidance.

Failure:

- consumer cannot reliably find affected usage;
- migration guidance is insufficient;
- the test reveals a case that requires a bounded registration exception.

### V7 — Registration exception

Simulate a security advisory with a fixed set of registered organizational consumers.

Expected:

- bounded registry has explicit scope, owner, freshness, and release gate;
- the exception does not become a universal consumer-index rule.

### V8 — Backup and restore

Create source-version-identified snapshots in backup A and B, then simulate primary loss.

Expected:

- restore recovers target authority, capability selection, current state, and irreplaceable rationale;
- backup is not independently edited;
- restored identity matches the recorded source;
- one backup failure does not destroy both.

Failure:

- backup becomes a writer;
- restore cannot identify the source version;
- irreplaceable records are missing.

## 5. Acceptance criteria

The candidate passes bounded validation only if:

- no parent-repository bootstrap creates target truth;
- logical target authority survives physical co-location;
- disjoint work can proceed without false global locks;
- shared-object changes are fail-closed or reconciled;
- the four evolution axes remain distinguishable in every scenario;
- consumer-owned migration works in the ordinary scenario;
- explicit exception triggers are narrow and auditable;
- backups restore correctly and remain non-authoritative;
- every semantic failure is recorded rather than repaired by silent architecture invention.

## 6. Stop conditions

Stop the affected scenario when:

- a required authority map is missing;
- target-root ownership is ambiguous;
- an action would change a real repository or ingest private material;
- the executor needs to invent current product behavior;
- two tasks change a shared object without a reconciliation rule;
- restore identity cannot be verified;
- the next-tier executor repeatedly misses a semantic acceptance criterion.

## 7. Evidence to collect

- frozen taskbooks and fixture identity;
- branch/PR/path lineage;
- mechanical diff results;
- answer/decision ledger;
- semantic failure and correction count;
- unnecessary versus missed escalation;
- Owner burden;
- candidate amendments;
- whether an exhaustive consumer index became necessary in any ordinary case.

## 8. Research assessment

Ordinary validation does not require Deep Research.

Potential later research:

- compare dependency-impact practices in open-source libraries, monorepos, package ecosystems, and Agent-managed projects;
- examine when reverse dependency registries materially improve safety or migration;
- review education/SLA evidence design separately from this engineering validation.

No research task is generated or selected by this plan.
