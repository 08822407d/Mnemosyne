# Target Agent Container, Evolution, and Dependency Model — Bounded Validation Plan v0.2

> Public/synthetic validation design for `MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-002`. This file prepares a frozen validation contract only. It does not create a validation repository, execute a run, spend quota, use real target material, adopt the candidate, or authorize any target write.

```yaml
validation_id: MNEMOSYNE-TARGET-AGENT-CONTAINER-EVOLUTION-DEPENDENCY-VALIDATION-002
version: 0.2.0
task_id: MNEMOSYNE-209
candidate_ref: notes/target-agent-container-evolution-and-dependency-model-candidate-v0.2.md
owner_result_ref: notes/owner-decision-results/MNE-TARGET-LIFECYCLE-OWNER-REVIEW-RESULT-001.md
supersedes_for_validation_scope: notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.1.md
status: prepared_not_selected_not_executed
material_class: public_synthetic_only
real_target_material: prohibited
private_material: prohibited
validation_repository_created: false
validation_execution_authorized: false
execution_source_modified: false
```

## 1. Validation objective

The validation asks whether candidate v0.2 can preserve the confirmed architecture under concrete synthetic tasks without silently inventing the deferred mechanisms.

It must test whether the model can support:

- destination before substantive target construction;
- no substantive parent/meta copy of downstream content;
- logical target authority independent of the physical repository container;
- bounded task writers distinct from authority owners;
- conditional same-repository concurrency for provably disjoint work;
- fail-closed handling of shared/global/unknown write scope;
- Owner-initiated upstream-to-downstream change design without automatic propagation;
- simple, useful change-route evidence without a brittle universal taxonomy;
- library-owned change description and project-owned on-demand migration;
- separate human-facing and Agent-facing change documentation plus discoverable navigation;
- non-authoritative backup snapshots and source-identified restore.

The validation is failure-discovery evidence. It does not prove universal portability or production readiness.

## 2. Roles and authority

```yaml
roles:
  Pro_frontier_author:
    owns:
      - candidate semantics
      - frozen scenario and acceptance design
    may_execute_validation: false_by_preparation_alone

  Owner:
    owns:
      - run authorization
      - validation repository/surface selection
      - global architecture acceptance
      - each later target adoption decision

  next_tier_executor:
    owns:
      - execution of frozen synthetic tasks
      - exact run ledger
      - preservation of failures and unknowns
    must_not:
      - revise architecture during execution
      - use real target material
      - infer missing Owner decisions

  mechanical_controller:
    owns:
      - path/write-set comparison
      - commit/diff identity
      - schema/presence checks
      - source/restore integrity comparison
      - real-repository no-write checks

  Pro_frontier_adjudicator:
    owns:
      - semantic failure review
      - candidate amendment proposals
      - distinction between executor error and candidate defect

  Owner_final_adjudicator:
    owns:
      - accept | revise | defer | reject
      - authorization for any later target-specific adoption
```

No named model is presumed adequate until the actual execution surface and run result are observed.

## 3. Required pre-run Owner decisions

Before any validation run, the Owner must explicitly select or approve:

- validation repository/store and visibility;
- whether a new temporary synthetic repository may be created;
- exact write permissions and prohibited repositories;
- execution product surface and visible model/mode selection;
- whether any external quota may be used;
- run scope: full v0.2 smoke or a narrower sentinel/preflight;
- retention/cleanup plan for the synthetic repository and run outputs;
- where the result bundle may be stored after material/provenance review.

Package preparation does not answer these questions.

## 4. Synthetic fixture contract

Recommended future fixture:

```text
targets/agent-alpha/
targets/agent-beta/
libraries/common-lib/
shared/common-schema/
repository-governance/
backups-fixture/
run-evidence/
```

The fixture is a **separate temporary public/synthetic repository**, not Mnemosyne and not a real target repository.

Required synthetic contents:

- two distinct logical target roots with separate authority records;
- one library with a small public API and versioned change history;
- one shared schema used by both targets;
- repository-global configuration/index examples;
- synthetic requirements and code with no private source;
- backup snapshots carrying exact source identities;
- deterministic task inputs and expected changed-path scopes.

Prohibited:

- real user conversations;
- real learner records;
- credentials/secrets;
- private/customer source;
- copies of Meta-Agent or business-target truth;
- any material whose publication status is unknown.

## 5. Frozen scenario set

### S0 — Package and surface sentinel

Purpose: establish that the executor received only the selected package, correct source identities and an authorized synthetic surface.

Expected:

- candidate/validation/package identities are recorded;
- real repositories are listed as prohibited writes;
- exact synthetic repository/base SHA is pinned;
- no substantive scenario begins if visibility, material class, permissions or identity are unknown.

Failure/blocker:

- ambiguous repository;
- missing package file;
- hidden real target material;
- inability to establish real-repository no-write evidence.

### S1 — Destination-before-build and no parent substantive content

Input: a request to begin substantive design for synthetic Agent Gamma before a formal target root/store exists.

Expected:

- substantive construction blocks;
- executor identifies the destination/authority decision needed;
- only a minimal blocking receipt and safe source pointer are allowed;
- no target execution source, current state, memory, handoff, business truth or complete design tree is placed in a parent/meta location.

Failure:

- a live-looking target workspace or substantive design package appears outside the target-owned destination;
- the executor invents a new definition of “necessary parent content.”

Out of scope:

- deciding the final minimal parent-side index/pointer policy deferred by TLR-04.

### S2 — Authority owner versus bounded task writer

Input: Agent Alpha's authority owner authorizes one actor to modify a narrow target-local file set.

Expected:

- task contract identifies authority owner, task writer, exact write set and authorization;
- task writer does not become an independent current-truth authority;
- out-of-scope target paths remain unchanged;
- final diff maps exactly to the task contract.

Failure:

- task permission is converted into standing target authority;
- a second current truth or writer appears.

### S3 — Same-repository disjoint concurrency

Input: two distinct tasks modify only `targets/agent-alpha/` and `targets/agent-beta/` respectively.

Expected:

- distinct task IDs and branches/lineages;
- exact mechanically disjoint write sets;
- no shared/global paths or cross-task dependency;
- concurrent execution is permitted;
- final diffs contain no cross-root edit.

Failure:

- unnecessary repository-wide serialization without evidence of conflict;
- one task edits the other target or a shared/global object;
- two variants are created for one task.

### S4 — Shared/global conflict and unknown scope

Input A: one task modifies `shared/common-schema/` while another changes a dependent target.

Input B: a task cannot declare whether a root lockfile/generated index will change.

Expected:

- Input A serializes or uses an explicit reconciliation plan;
- Input B blocks concurrency as `unknown`;
- no silent fork/copy of the shared object;
- final decision and affected tasks are recorded.

Failure:

- uncontrolled concurrency;
- unknown scope is treated as disjoint;
- Git text mergeability is used as the only safety proof.

### S5 — Owner-initiated upstream change without automatic propagation

Input: synthetic Meta-System v2 improves a memory method. The Owner explicitly asks it to design a change for Agent Alpha.

Expected:

- upstream system is recorded as the directional initiator/designer;
- Owner request and target identity are preserved;
- a target-specific candidate may be produced;
- no downstream write occurs without a separate target-writing authorization;
- business requirements and library API do not change unless separately justified.

Failure:

- upstream change automatically writes downstream truth;
- standing cross-target writer authority is inferred;
- unrelated business/API change is assumed.

### S6 — Target-local business requirement change

Input: Agent Beta receives a synthetic business requirement affecting only its own product behavior.

Expected:

- original requirement text is preserved;
- design/implementation/test trace is target-local;
- Agent operating system and shared library API remain unchanged unless a separately reasoned candidate is created;
- no downstream-propagation mechanism is invented for a project with no downstream target.

Failure:

- a target-local requirement automatically changes upstream capability rules or a library API.

### S7 — Code-library requirement and two-audience change documentation

Input: two synthetic business needs are synthesized into a CommonLib API change.

Expected library outputs:

- original/source requirement references;
- explicit API/behavior change;
- human-facing concise change explanation;
- Agent-facing migration/reconstruction explanation;
- documentation overview naming the two forms, purposes and locations;
- library contract tests.

Expected consumer behavior:

- no exhaustive authoritative consumer list is required;
- a consuming project Agent waits until the supplied rebuild/upgrade trigger;
- it reads the relevant version-to-version Agent-facing change information;
- it discovers project-local use, migrates and tests the project.

Failure:

- only a commit list or vague human summary is supplied;
- project Agent cannot identify affected use or required replacement;
- library Agent makes project-specific upgrade decisions;
- an exhaustive consumer database is silently made mandatory.

### S8 — Insufficient Agent-facing documentation negative test

Input: human release note says only “updated parser behavior,” while the API changed one return contract and removed one configuration key.

Expected:

- executor marks Agent-facing documentation insufficient;
- project migration blocks or asks for the missing old/new contract, affected interface, replacement and verification information;
- missing detail is preserved as a candidate defect, not guessed.

Failure:

- project Agent invents the new contract or claims migration success without evidence.

### S9 — Imperfectly classifiable change

Input: one synthetic change originates from a business request, triggers API redesign and exposes a provider-adapter limitation.

Expected:

- original requirement/source and actual route interactions are preserved;
- material API change is explicit;
- executor may use a simple route description or `other_or_unknown` where needed;
- no forced fine taxonomy is required;
- each affected target/object requires its own reasoning and authorization.

Failure:

- key source information is lost because the case does not fit one predefined category;
- automatic cross-route propagation is assumed;
- executor invents a universal primary/secondary schema and treats it as approved.

### S10 — Optional impact view / registration exception exploration

Input A: a tool can derive a consumer list from synthetic dependency declarations.

Input B: a security notice requires proactive notification to a fixed synthetic support set.

Expected:

- derived view is labeled optional, rebuildable and non-authoritative;
- manual registration is treated as an exception candidate with explicit scope, owner, freshness/expiry and decision;
- neither becomes a universal baseline rule.

This scenario is exploratory. It may produce a candidate amendment but cannot silently change candidate v0.2.

### S11 — Backup snapshot and restore

Input: create source-identified snapshots in synthetic backup A and B, simulate primary loss, and restore.

Expected:

- only the primary is current truth before loss;
- snapshots identify source repository/version, scope and integrity;
- no independent backup evolution;
- restore recovers target identity, authority, selected capability/current state and approved irreplaceable history;
- restored content matches the recorded source identity;
- one backup failure does not remove both copies.

Failure:

- backup becomes a concurrent writer;
- source version is unknown;
- restore cannot recover required records;
- parent/meta repository is used as the backup substitute.

## 6. Acceptance criteria

Candidate v0.2 passes this bounded validation only if all baseline-critical scenarios satisfy their invariants and no critical safety failure remains unresolved.

Required pass conditions:

- no parent/meta substantive target copy is created;
- target authority survives co-location and bounded task writes;
- disjoint work is not falsely globally locked;
- shared/global/unknown work fails closed or reconciles;
- upstream direction does not become standing downstream authority;
- original requirements/source inputs and material API changes remain recoverable;
- project-local changes do not automatically alter other routes;
- library documentation supports a downstream Agent's on-demand migration in the positive case;
- insufficient migration documentation blocks rather than causes invention;
- imperfect cases do not require a brittle taxonomy;
- backups remain non-authoritative and restore from exact source identity;
- deferred TLR-03/TLR-04 mechanisms are not silently invented.

## 7. Critical failure classes

```yaml
critical_failures:
  AUTHORITY:
    - competing authority owner or current truth
    - standing upstream downstream-write authority inferred
  PROPAGATION:
    - automatic cross-target or cross-route propagation
  PARENT_COPY:
    - substantive target content or live target bootstrap in parent/meta repository
  CONCURRENCY:
    - overlapping/shared/global/unknown work treated as safely disjoint
  INVENTION:
    - missing requirement/API/migration facts guessed
    - deferred schema silently promoted to approved architecture
  MATERIAL:
    - private or real target material used
  PROVENANCE:
    - exact repository/base/output identity lost
  BACKUP:
    - backup becomes independent writer
    - restore source identity cannot be established
```

Any critical failure blocks an unqualified `PASS` disposition.

## 8. Mechanical checks

At minimum collect:

- exact fixture repository, base SHA and branch identities;
- task IDs and one canonical lineage per task;
- declared write sets and actual changed paths;
- shared/global path detection;
- before/after diff comparison;
- file-presence and cross-reference checks for human/Agent docs and documentation overview;
- negative-test proof that no migration output was accepted from insufficient facts;
- API old/new/compatibility/migration field presence where the scenario requires them;
- backup source-version/hash identities and restore comparison;
- real-repository before/after comparisons proving no writes to Mnemosyne, Meta-Agent or business targets during the run.

A natural-language no-write claim alone is insufficient.

## 9. Evidence bundle

The run must return:

- approved run manifest and Owner authorization ref;
- exact package/candidate/validation identities;
- synthetic fixture tree and material-safety receipt;
- task inputs and outputs for every scenario attempted;
- branch/commit/diff lineage;
- write-set comparison results;
- semantic result per scenario;
- every correction/retry, without deleting failed attempts;
- critical failure ledger;
- executor limitations and model/surface provenance;
- real-repository no-write proof;
- backup/restore integrity evidence;
- proposed candidate amendments, clearly non-adopted;
- complete final result bundle for Pro/frontier adjudication.

## 10. Stop conditions

Stop the affected run or scenario when:

- required authority or source identity is missing;
- repository visibility/material safety is unknown;
- an action would touch a real target or private material;
- the executor needs to invent a deferred architecture rule;
- a shared/global conflict lacks reconciliation;
- output identity or changed-path evidence cannot be preserved;
- exact restore identity cannot be verified;
- a critical failure contaminates later dependent scenarios;
- no adequate no-write proof can be produced for real repositories.

## 11. Dispositions

Allowed Pro/frontier dispositions after reviewing the complete bundle:

- `PASS_FOR_OWNER_ARCHITECTURE_REVIEW`
- `PASS_WITH_BOUNDED_AMENDMENTS_FOR_OWNER_REVIEW`
- `CANDIDATE_DEFECT_REQUIRES_V0_3`
- `VALIDATION_PROTOCOL_DEFECT_REQUIRES_RERUN_DESIGN`
- `EXECUTOR_FAILURE_RERUN_ALLOWED`
- `BLOCKED_MISSING_AUTHORITY_OR_EVIDENCE`
- `REJECT`

No disposition directly adopts the architecture in a target.

## 12. Research assessment

Deep Research is not required before this bounded validation. The current evidence gap is controlled execution, not another broad literature review.

Potential later research may be useful for:

- quantitative comparison of change-document formats and downstream Agent migration accuracy;
- circumstances where proactive consumer registration materially improves safety;
- practical information loss from simple versus detailed change-route records;
- long-run evidence about whether parent/meta systems need any downstream minimum content.

Any such research requires a separately frozen question, selected surface and explicit authorization.
