# V2-A A1 — Owner Gates and Surface Contract

```yaml
artifact_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-GATES-001
package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PACKAGE-001
status: frozen_plan_not_authorization
```

## 1. Current Owner authorization

Authorized by `MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-A1-PREPARATION-OWNER-DECISION-001`:

- prepare this exact A1 run package;
- write only the preparation artifacts to Mnemosyne;
- publish one Ready PR.

Not authorized:

- create or move any branch in the validation repository;
- execute controller or worker tasks;
- create a validation PR;
- run A1 or any later cell;
- modify Meta-Agent, a real target, account/app permissions or external quota.

## 2. Required future gate sequence

```text
package publication and post-merge verification
→ fresh Pro execution-time source/ref/branch/product check
→ Owner G2A authorization for this A1 run only
→ controller read-only preflight
→ controller creates the three initial branches
→ Owner launches two frozen worker messages
→ controller verifies workers and constructs two order branches
→ controller final bundle and stop
→ fresh Pro adjudication
→ Owner disposition
```

No step implies the next one.

## 3. Future product and model surface

Recommended candidate for controller, Alpha worker and Beta worker:

```text
gpt-5.6 sol extra high
```

This label is not frozen by package publication. Future G2A must preserve separately for each execution conversation:

```yaml
controller:
  Owner_authorized_visible_label:
  operator_selected_visible_label:
alpha_worker:
  Owner_authorized_visible_label:
  operator_selected_visible_label:
beta_worker:
  Owner_authorized_visible_label:
  operator_selected_visible_label:
```

Each pair requires exact raw-string equality. A value may come only from direct Owner authorization and current operator-observed/reported selection. It may not be inferred from memory, response style, speed, model self-identification or a repository recommendation.

Even after equality:

```yaml
backend_identity: unknown_or_not_attestable
```

## 4. Future G2A minimum fields

The single controller G2A/startup message must bind:

```yaml
run_decision_candidate_001_blob:
package_source_manifest_001_blob:
protected_Mnemosyne_master:
protected_Meta_Agent_master:
validation_master: e8e3296922185b4b70997c2351d6f39423f2cd4f
fixture_commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
A0_controller_head: d936cd2d4acd3f5b71f6f7f0d86ae6ffe93ab58c
controller_authorized_and_selected_label:
alpha_authorized_and_selected_label:
beta_authorized_and_selected_label:
branch_map:
output_manifest:
retention_and_cleanup:
retry_authorized: false
```

A mismatch, missing value or unknown required condition blocks before branch creation. The executor cannot refresh values, repair the package or ask the Owner to reinterpret a near match inside the execution conversation.

## 5. Exact future write authority

Only after G2A and controller preflight PASS:

### Controller

May:

- create `v2a-a1-001-controller` from validation `master@e8e329...`;
- create `v2a-a1-001-alpha` and `v2a-a1-001-beta` from fixture `81f18e...`;
- after both worker branches pass, create the two exact order branches from the verified worker heads;
- write only the frozen controller result files on the controller branch;
- create only controller-owned order commits that apply the peer's exact frozen blobs.

### Alpha worker

May move only `v2a-a1-001-alpha`, with exactly one commit from fixture base and exactly two target-local paths.

### Beta worker

May move only `v2a-a1-001-beta`, with exactly one commit from fixture base and exactly two target-local paths.

## 6. Exact prohibitions

```yaml
prohibited:
  - write_Mnemosyne_during_A1
  - write_Meta_Agent
  - access_or_write_unnamed_real_target
  - modify_validation_master
  - modify_fixture_or_any_tlr_v1_ref
  - modify_v2a-sentinel-001-controller
  - create_any_branch_not_in_frozen_five_branch_map
  - create_any_pull_request
  - change_worker_message_after_first_worker_result
  - expose_peer_final_head_or_output_to_the_other_worker_before_completion
  - add_generated_shared_or_global_effect
  - run_A2_to_A7
  - run_V2_B_or_V2_C
  - use_Web_Deep_Research_Fable_other_app_private_material_or_external_quota
  - automatic_retry
  - package_or_fixture_repair
  - architecture_change
  - reset_or_force_push
  - branch_cleanup
  - auto_merge
```

## 7. Stop and no-retry rule

Stop the affected run before further writes when:

- a source/package/ref/model/branch/output identity differs;
- an A1 branch already exists before G2A;
- the pre-run branch inventory contains an unexplained lineage;
- either worker writes an unexpected path or produces an unexpected tree;
- either worker needs peer output;
- an order branch cannot be built exactly from verified worker blobs;
- the two final order trees differ;
- a protected ref moves;
- the selected product surface cannot enforce the branch/path boundary.

A failed or blocked run is preserved and returned to fresh Pro. It is not retried in the same controller or worker conversations.

## 8. Retention

The A0 controller branch remains immutable. If A1 later runs, all five A1 branches remain retained until:

- the full raw bundle is complete or the run is explicitly abandoned;
- fresh Pro adjudication is complete;
- the Owner decides the result and any correction;
- durable result identities no longer depend on branch retention;
- cleanup receives a separate explicit authorization.
