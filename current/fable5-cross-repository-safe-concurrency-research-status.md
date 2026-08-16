# Fable F2 Cross-Repository Safe Concurrency Research — Current Status

```yaml
status_id: MNE-FABLE5-CROSS-REPOSITORY-CONCURRENCY-STATUS-001
created_by_task: MNEMOSYNE-214
last_updated_by_task: MNEMOSYNE-223
canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
display_name: MNE-DR-005 跨仓库并发
roadmap_priority: F2
status: V2A_A0_SENTINEL_EXACT_PLAN_PREPARED_EXECUTION_NOT_AUTHORIZED
Fable_report_received: true
return_identity_verified: true
fresh_Pro_adjudication_completed: true
Owner_F2_disposition:
  selected: A
  decision_ref: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
modified_provisional_amendment_accepted: true
V2_staged_validation_design_prepared: true
V2_validation_package_prepared: true
Owner_stage_selection:
  selected_route: A_prepare_minimal_V2_A_sentinel
  exact_run_decision_candidate: notes/validation-run-decisions/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-001.md
  exact_execution_package: notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-001/README.md
V2_A_A0_plan_prepared: true
V2_A_A0_execution_selected: false
V2_A_A0_execution_authorized: false
V2_A_A1_to_A7_execution_authorized: false
V2_B_execution_authorized: false
V2_C_execution_authorized: false
controller_branch_created: false
validation_repository_written_by_MNEMOSYNE_223: false
connector_permission_change_authorized: false
external_execution_or_quota_authorized: false
automatic_retry: false
repository_write_by_Fable: false
real_target_adoption_authorized: false
```

## 1. Preserved Fable result and fresh Pro adjudication

Exact Fable result cycle:

```text
raw/research-reports/cycles/2026Q3-cross-repository-safe-concurrency/
```

Fresh Pro adjudication:

```text
notes/research-adjudications/
MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md
```

Controlling F2 disposition:

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

## 2. Owner-accepted provisional amendment

The Owner accepted the Pro-corrected amendment for bounded validation design:

- task-local contracts remain the default;
- non-interference evidence extends beyond write-set intersection;
- read/version freshness, generated/derived effects and semantic contracts are explicit;
- shared/global/authority-changing/unknown scope fails closed;
- cross-repository work uses ordered committed-identity checkpoints;
- stop plus forward repair or explicit revert is the normal recovery;
- future leases require destination-enforced fencing;
- project-native evidence-strength labels are used;
- V2-A, V2-B and V2-C are separate validation surfaces.

The Owner did not authorize execution or a real target.

## 3. Prepared staged V2 design

```text
notes/validation-designs/
cross-repository-safe-concurrency-v2-staged-validation-v0.1.md

notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/
```

- V2-A: public/synthetic core concurrency and stale-state design;
- V2-B: public/synthetic ordered multi-repository failure/recovery design;
- V2-C: connector/app permission and privacy design only.

## 4. Selected V2-A sentinel plan

The Owner selected preparation of a minimal V2-A sentinel, not execution.

```yaml
sentinel_plan:
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
  selected_stage: V2_A
  selected_cells:
    - A0
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  controller_base: master@e8e3296922185b4b70997c2351d6f39423f2cd4f
  read_only_fixture: tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
  future_controller_branch: v2a-sentinel-001-controller
  worker_branches: []
  PR_creation: prohibited
  exact_output_file_count: 7
  recommended_controller_visible_selection_if_available: gpt-5.6 sol extra high
  fresh_review: separate_ChatGPT_Pro_conversation
```

A0 will test only package, identity, material, surface, permission and no-write evidence. It will not run A1–A7 or create a substantive V2-A fixture.

## 5. Current gate

```yaml
current_gate: MERGE_MNEMOSYNE_223_THEN_FRESH_IDENTITY_RECHECK_THEN_OWNER_G2A_DECISION
G1A_surface_and_run_profile_prepared: true
G2A_execution_authorized: false
next_Owner_decision:
  - authorize_exact_A0_sentinel
  - revise_the_plan
  - defer
```

After package publication, the responsible Pro route must recheck all source blobs, validation refs, branch absence and model/tool availability before asking for G2A authorization.

## 6. Explicit boundaries

No current artifact authorizes:

- creation of `v2a-sentinel-001-controller`;
- any validation-repository write;
- A0 execution;
- A1–A7 execution;
- V2-B or V2-C;
- connector/app/account permission changes;
- web, Deep Research, Fable or external quota;
- private or real-target material;
- modification of Target Lifecycle candidate v0.2, the execution source, Meta-Agent or a real target;
- a lock/lease/orchestrator service;
- automatic compensation, reset or force-push;
- target adoption or production-readiness claims.
