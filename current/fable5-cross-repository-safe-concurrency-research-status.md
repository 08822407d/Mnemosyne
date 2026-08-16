# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
last_updated_by_task: MNEMOSYNE-222
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: OWNER_OPTION_A_ACCEPTED_MODIFIED_PROVISIONAL_AMENDMENT_V2_DESIGN_PREPARED_EXECUTION_NOT_AUTHORIZED
Fable_report_received: true
return_identity_verified: true
fresh_Pro_adjudication_completed: true
Owner_disposition:
  selected: A
  decision_ref: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
modified_provisional_amendment_accepted: true
validation_design_prepared: true
validation_package_prepared: true
validation_execution_selected: false
validation_execution_authorized: false
V2_A_execution_authorized: false
V2_B_execution_authorized: false
V2_C_execution_authorized: false
connector_permission_change_authorized: false
external_execution_or_quota_authorized: false
automatic_retry: false
repository_write_by_Fable: false
real_target_adoption_authorized: false
```

## Preserved result and adjudication

Exact Fable result cycle:

```text
raw/research-reports/cycles/2026Q3-cross-repository-safe-concurrency/
```

Fresh Pro adjudication:

```text
notes/research-adjudications/
MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md
```

The controlling F2 result remains:

```yaml
return_identity: PASS_EXACT
run_validity: ACCEPT_WITH_LIMITATIONS
input_verification: PASS_WITH_BOUNDED_IDENTITY_DEFECT
task_contract_compliance: PASS_WITH_LIMITATIONS
citation_portability: FAIL
architecture_direction: ACCEPT_AS_CORROBORATED_MODIFIED_PROVISIONAL_DIRECTION
technical_details: ACCEPT_WITH_MATERIAL_CORRECTIONS
implementation_readiness: REJECT
```

## Owner Option A decision

The Owner accepted the Pro-corrected amendment as a modified provisional baseline for validation design.

Accepted direction:

- task-local contracts remain the default;
- non-interference evidence extends beyond write-set intersection;
- read/version freshness, generated/derived effects and semantic contracts are explicit;
- shared/global/authority-changing/unknown scope fails closed;
- cross-repository work uses ordered committed-identity checkpoints;
- stop plus forward repair or explicit revert is the normal recovery;
- future leases require destination-enforced fencing;
- project-native evidence-strength labels replace inappropriate SLSA-level analogies;
- V2-A, V2-B and V2-C are separate validation surfaces.

The Owner did not authorize execution or a real target.

## Prepared V2 design

Design:

```text
notes/validation-designs/
cross-repository-safe-concurrency-v2-staged-validation-v0.1.md
```

Package:

```text
notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/
```

### V2-A

Public/synthetic core repository concurrency and stale-state design:

- positive independent work;
- generated/derived collision;
- stale read/base identity;
- merge-order dependence;
- duplicate canonical lineage;
- shared/global/unknown fail-closed behavior;
- mechanically clean but semantically invalid work.

### V2-B

Public/synthetic ordered multi-repository design:

- ordered identity handoff;
- later-step failure after an earlier commit;
- separately authorized recovery;
- recovery failure and human gate;
- cutover stale-writer evidence by enforcement layer;
- backup non-authority.

### V2-C

Design-only connector/app permission and privacy boundary. It is not runnable until a separate product/security/account authorization exists.

## Current gate

```yaml
current_gate: FUTURE_OWNER_STAGE_AND_SURFACE_SELECTION
recommended_next_sequence:
  - review_or_merge_MNEMOSYNE_222_design_PR
  - separately_select_V2_A_sentinel_or_defer
  - prepare_exact_repository_and_run_authorization_if_selected
  - fresh_Pro_adjudication_after_any_run
V2_execution_authorized_now: false
```

No package merge, branch creation or status update implies execution authorization, connector permission change, external quota use, architecture promotion or real-target adoption.
