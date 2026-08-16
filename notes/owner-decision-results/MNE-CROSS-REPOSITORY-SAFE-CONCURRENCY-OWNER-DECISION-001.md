# Cross-Repository Safe Concurrency — Owner Decision 001

> Durable record of the Owner's Option A disposition on `MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-DISPOSITION-CANDIDATE-001`. This accepts the Pro-corrected F2 amendment as a modified provisional baseline and authorizes preparation of a bounded staged V2 design/package only. It does not authorize validation execution, connector-permission testing, real-target work, a lock service, automatic compensation or modification of the Target Lifecycle candidate v0.2.

```yaml
decision_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001
task_id: MNEMOSYNE-222
decision_status: OWNER_CONFIRMED_OPTION_A
selected_option: A_ACCEPT_MODIFIED_PROVISIONAL_AMENDMENT_AND_AUTHORIZE_V2_DESIGN_ONLY
execution_time_base_master: c01918b2a1ad0b0e25b9b62cbc90fb923836f36d
source_adjudication:
  path: notes/research-adjudications/MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md
  blob: 27d607257bb1700d9ff9c73f0048a6a7b7847746
source_corrected_amendment:
  path: notes/cross-repository-safe-concurrency-and-ordered-work-amendment-candidate-v0.1.md
  blob: 46fd66dc23d6615ea167e0950de970cc316c056b
source_decision_candidate:
  path: notes/owner-decision-candidates/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-DISPOSITION-CANDIDATE-001.md
  blob: 7a56489c235dcd79a15f3fc351afcc1a69a335c7
amendment_status_after_decision: OWNER_ACCEPTED_MODIFIED_PROVISIONAL_AMENDMENT_FOR_BOUNDED_V2_DESIGN
validation_design_authorized: true
validation_package_preparation_authorized: true
validation_execution_authorized: false
V2_A_execution_authorized: false
V2_B_execution_authorized: false
V2_C_execution_authorized: false
connector_permission_change_or_test_authorized: false
external_quota_authorized: false
synthetic_repository_creation_authorized: false
real_target_write_or_adoption_authorized: false
Target_Lifecycle_candidate_v0_2_modification_authorized: false
execution_source_modified_or_authorized: false
Meta_Agent_modified_or_authorized: false
lock_or_lease_service_authorized: false
automatic_compensation_authorized: false
```

## 1. Accepted provisional amendment

The Owner accepts the following F2 direction for validation design:

1. Task-local contracts remain the default coordination mechanism.
2. Safe-concurrency evidence must cover more than write-set intersection; it must include material read/version identities, generated or derived effects, semantic contracts, authority/cutover effects, merge-order dependence, base freshness and side effects on the selected tool surface.
3. Shared, repository-global, authority-changing or unknown scope fails closed to serialization, explicit reconciliation or a human/Owner gate.
4. Cross-repository work is an ordered sequence of separately authoritative steps with committed identity handoff and revalidation; it is not assumed to be an ACID transaction.
5. Normal failure handling is stop, preserve evidence and choose forward repair or an explicit revert. Automatic compensation is not a default and requires a separately declared, authorized, idempotent and validated inverse operation.
6. Any future lease/lock proposal must include a named protected object, monotonic fencing/epoch identity and destination-side stale-token rejection. TTL alone is insufficient.
7. Evidence claims use Mnemosyne-native strength states rather than applying SLSA levels to ordinary self-attestations.
8. Validation design is staged into V2-A, V2-B and V2-C because repository concurrency, ordered cross-repository failure and provider permission/privacy are different risk surfaces.

## 2. Relationship to existing architecture

This decision does not replace or directly edit:

```text
notes/target-agent-container-evolution-and-dependency-model-candidate-v0.2.md
```

The accepted amendment is a bounded provisional extension for validation design. The controlling architecture still preserves the Owner-confirmed target-local authority, bounded writer, no automatic propagation, backup and adoption gates already present in candidate v0.2.

The Fable report is not accepted as an implementation specification. The controlling F2 delta is the Pro-corrected amendment identified above.

## 3. Authorized design scope

The current task may prepare:

- one staged validation design;
- a frozen public/synthetic fixture and scenario contract for V2-A;
- a frozen public/synthetic multi-repository scenario contract for V2-B;
- a design-only threat and permission contract for V2-C;
- mechanical checks, evidence-level rules, run/result templates and package-integrity checks;
- future Owner run-selection gates.

The package must make every stage separately selectable and must not imply that package preparation authorizes execution.

## 4. Stage boundaries

### V2-A — core repository concurrency and stale state

Design may cover:

- true disjoint positive concurrency;
- generated/derived-object collision;
- stale read/base identities;
- merge-order dependence;
- duplicate canonical PR lineage;
- shared/global/unknown fail-closed behavior;
- mechanically clean but semantically invalid work.

### V2-B — ordered cross-repository failure and recovery

Design may cover:

- successful ordered identity handoff;
- later-step failure after an earlier commit;
- separately authorized recovery success;
- recovery failure and human escalation;
- stale former-writer behavior after cutover;
- backup-to-authority misuse.

### V2-C — connector and privacy boundary

Only design is authorized. Any run requires a separate product/security decision specifying:

- connector/app identity;
- repository allowlist and denied repositories;
- read versus write scopes;
- visibility and sensitivity class;
- provider-visible denial evidence;
- account/permission changes;
- quota and retention terms.

## 5. Explicitly not authorized

This decision does not authorize:

- creation of any synthetic or real repository;
- execution of V2-A, V2-B or V2-C;
- modification of connector/app permissions;
- access to private or real-target material;
- a lock, lease, transaction-log or central-orchestrator service;
- GitHub Actions or merge-queue configuration;
- automatic compensation, reset or force-push;
- modification of Target Lifecycle candidate v0.2;
- modification of `current/human-approved-spec.md`;
- modification of Meta-Agent or any real target;
- target adoption, migration or activation;
- external Research/Fable/Deep Research/Work quota;
- Agent merge or auto-merge.

## 6. Next gates

After the design/package is published, the next possible gates are separate Owner decisions:

1. accept, revise, defer or reject the V2 design;
2. select a V2-A sentinel or full V2-A run;
3. only after reviewing V2-A, decide whether V2-B should run;
4. authorize V2-C only under a separate connector/security contract;
5. review results through a fresh Pro/frontier adjudication;
6. separately decide any architecture revision or real-target adoption.

No gate implies the next one automatically.
