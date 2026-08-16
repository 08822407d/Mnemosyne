# V2 Owner Gates and Stage Boundaries

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-GATES-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-PACKAGE-001
status: design_only_not_authorization
```

## 1. Current authorization

The Owner selected Option A on the F2 disposition candidate.

Authorized now:

- accept the Pro-corrected amendment as a modified provisional baseline;
- prepare this staged validation design and package.

Not authorized now:

- create validation repositories;
- execute any V2 stage;
- change account, app or connector permissions;
- consume external quota;
- use private or real-target material;
- modify an architecture candidate, execution source, Meta-Agent or real target.

## 2. Gate sequence

### G0 — package publication

Requires:

- this package exists on `master` after Owner merge;
- package paths and identities are verified;
- no execution side effect occurred.

Effect:

- design becomes durable;
- no run is selected.

### G1A — V2-A surface decision

Owner must select:

- temporary public/synthetic repository or isolated fixture surface;
- visibility and material classification;
- controller and worker product/model surfaces;
- exact write permissions and prohibited repositories;
- scenario subset: sentinel or selected full V2-A;
- quota and retention;
- result-storage and branch-cleanup plan.

### G2A — V2-A execution authorization

Requires a frozen run package with:

- exact repository and base SHA;
- exact scenario/cell task identities;
- exact branches and write sets;
- no-write baseline for protected repositories;
- evidence/result templates;
- stop and no-retry conditions.

G1A does not imply G2A.

### G3A — V2-A fresh Pro adjudication

Requires the complete raw result bundle and exact identities. Pro classifies executor, fixture, tool and candidate failures.

### G1B/G2B/G3B — V2-B

V2-B normally requires a reviewed V2-A result. The Owner may explicitly waive that dependency only with a recorded reason.

V2-B additionally requires:

- two separate public/synthetic target repositories plus a controller/evidence location;
- exact ordered-action authorization;
- exact recovery authorization;
- explicit prohibition on automatic destructive reset/force-push;
- preservation of partial-failure states.

### G1C — V2-C security/product design decision

Before a runnable V2-C package exists, the Owner must select:

- connector/app/integration identity;
- test account or installation;
- repository allowlist and explicit denied repositories;
- allowed read/write actions;
- whether any private fixture is permitted;
- retention and evidence visibility;
- account-level permission-change operations;
- quota and rollback.

### G2C — V2-C execution authorization

Separate from all earlier gates. V2-A or V2-B success does not authorize V2-C.

## 3. Stage independence

```yaml
V2_A_pass_implies_V2_B_authorization: false
V2_A_pass_implies_V2_C_authorization: false
V2_B_pass_implies_production_readiness: false
V2_C_pass_implies_real_target_adoption: false
any_stage_failure_automatically_modifies_candidate: false
```

## 4. Owner-only decisions

The Owner retains exclusive control over:

- repository creation and visibility;
- product/model/effort selection;
- connector and account permissions;
- external quota;
- execution and retry;
- architecture revision;
- global acceptance level;
- each real-target adoption or migration;
- branch/fixture retention after review.

## 5. No hidden continuation

An executor must stop after the selected stage or cell. It must not infer permission to:

- run another cell;
- retry a failed cell;
- repair a fixture;
- revise the architecture;
- write a result back to Mnemosyne;
- create a PR;
- start V2-B or V2-C.
