# Cross-Repository Safe Concurrency V2-A Sentinel — Pro-Recommended Owner Run Decision Candidate 002

> Repaired G1A/G2A recommendation for A0. This supersedes candidate 001 only for package/source binding and execution-window protected-ref semantics. It is not Owner authorization and does not execute validation.

```yaml
decision_candidate_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-002
task_id: MNEMOSYNE-224
source_protocol_defect: V2A-SENTINEL-PROTOCOL-DEFECT-001
supersedes_for_scope:
  decision_candidate: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-001
  exact_scope:
    - pre_run_Mnemosyne_source_binding
    - protected_external_ref_baseline_timing
source_package_publication_commit: 9157c476e8bf785f6440af4aaefbc44532d47c14
source_owner_decision: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
source_validation_design: notes/validation-designs/cross-repository-safe-concurrency-v2-staged-validation-v0.1.md
source_package: notes/cross-repository-safe-concurrency-v2a-sentinel-execution-package-002/README.md
proposed_run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
status: PRO_REPAIR_RECOMMENDATION_READY_NOT_OWNER_AUTHORIZED
selected_stage_candidate: V2_A
selected_cells_candidate: [A0]
sentinel_only: true
validation_execution_authorized: false
validation_repository_write_authorized: false
external_quota_authorized: false
connector_or_app_change_authorized: false
real_target_adoption_authorized: false
```

## 1. Protocol repair

Candidate 001 required Mnemosyne `master` to remain at its pre-publication SHA. PR #291 necessarily changed `master` when the candidate/package were merged, so a correctly published package became invalid before it could ever be authorized.

Candidate 002 fixes this without weakening fail-closed behavior:

```yaml
source_integrity:
  mechanism: exact_load_bearing_path_blob_pairs
  package_identity:
    decision_candidate_blob: supplied_by_future_G2A
    source_manifest_blob: supplied_by_future_G2A

execution_window_no_write:
  Mnemosyne_master: supplied_by_future_G2A_after_package_merge
  Meta_Agent_master: supplied_by_future_G2A_after_package_merge
  must_match_before_first_validation_write: true
  must_match_after_A0: true
  controller_may_refresh_expected_value: false
```

No new Mnemosyne PR is created after the Owner freezes those execution-window refs. The Owner's natural-language G2A instruction is the authorization authority and is preserved verbatim in the A0 output.

## 2. Recommended A0 run

```yaml
run_decision:
  disposition: RUN_CANDIDATE
  validation_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-STAGED-VALIDATION-001
  package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-PACKAGE-002
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
  selected_stage: V2_A
  selected_cells: [A0]
  sentinel_only: true
  stop_after_A0_bundle: true
```

A0 proves only bounded repository/material/surface/identity/no-write behavior. It does not validate A1–A7 or architecture correctness.

## 3. Repository and fixture

```yaml
repository_surface:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  repository_exists: true
  default_branch: master
  pinned_controller_base_sha: e8e3296922185b4b70997c2351d6f39423f2cd4f
  read_only_fixture_ref: tlr-v1-fixture-base
  read_only_fixture_commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  read_only_fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
  fixture_modification_authorized: false
  new_repository_creation_authorized: false
```

The full historical V1 ref inventory is hard-pinned in source manifest 002.

## 4. Product/model topology

```yaml
execution_surface:
  controller_surface: standard_ChatGPT_conversation_with_GitHub_connector
  controller_conversation_count: 1
  worker_surfaces: []
  worker_branches: []
  scenario_PRs: prohibited
  recommended_visible_selection_if_available: gpt-5.6 sol extra high
  exact_visible_selection: Owner_G2A_must_name_verbatim
  substitution_without_new_Pro_Owner_decision: prohibited
  exact_backend_identity: unknown_or_not_attestable
  post_run_review: fresh_ChatGPT_Pro_conversation
```

A0 is bounded/mechanical enough for a next-tier execution candidate. If the intended visible option is absent or GitHub controls differ, stop before write.

## 5. Exact controller branch and write set

```yaml
controller_branch:
  name: v2a-sentinel-001-controller
  base: e8e3296922185b4b70997c2351d6f39423f2cd4f
  must_be_absent_before_run: true
  force_update: prohibited
  PR_creation: prohibited
```

Allowed paths, only on that branch:

```text
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/00-controller-receive.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/01-product-and-permission-receipt.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/02-package-and-material-receipt.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/03-repository-and-ref-baseline.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/04-mechanical-checks.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/05-sentinel-result-bundle.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/incidents/incident-ledger.yaml
```

All other writes are prohibited.

## 6. Tool/network/quota boundary

```yaml
tool_boundary:
  GitHub_read_on_Mnemosyne: exact_manifest_sources_and_master_before_after_only
  GitHub_write_on_Mnemosyne: prohibited
  GitHub_read_on_Meta_Agent: master_before_after_only
  GitHub_write_on_Meta_Agent: prohibited
  GitHub_read_on_validation_repository: named_refs_and_public_synthetic_fixture_only
  GitHub_write_on_validation_repository: exact_controller_branch_and_seven_paths_only
  web_access: prohibited_not_needed
  Deep_Research: prohibited
  Fable_or_Research: prohibited
  other_connected_apps: prohibited
  private_files_or_conversations: prohibited
  unlisted_real_targets: prohibited_read_and_write

quota:
  separate_paid_or_external_quota_authorized: false
  ordinary_plan_use_only: true
```

## 7. Execution-window protected refs

Candidate 002 intentionally does **not** hardcode the post-publication values. Fresh Pro re-reads them after package 002 merges and inserts them into the Owner G2A instruction:

```yaml
G2A_required_dynamic_fields:
  protected_Mnemosyne_master:
  protected_Meta_Agent_master:
  decision_candidate_002_blob:
  source_manifest_002_blob:
  authorized_visible_model_label:
```

Once the Owner issues G2A, no Mnemosyne write is permitted before or during A0. If either protected ref moves, controller blocks before branch creation.

## 8. Retention and result storage

```yaml
result_storage:
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  branch: v2a-sentinel-001-controller
  root: runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/
  raw_result_write_to_Mnemosyne: false
  Mnemosyne_ingestion_authorized: false

retention:
  retain_controller_branch_until:
    - complete_A0_bundle_reviewed_by_fresh_Pro
    - required_commit_tree_blob_identities_preserved
    - Owner_decides_full_V2_A_or_repair_or_defer
  cleanup: separately_released_after_review
```

## 9. A0 PASS and stop conditions

Provisional executor PASS requires:

- exact candidate/manifest and all load-bearing blobs match;
- protected external refs equal G2A baseline before and after;
- validation master/fixture/V1 inventory match;
- selected cells exactly `[A0]`;
- controller branch/write set exact;
- no worker branch or PR;
- all seven outputs and identities exist;
- visible model/reasoning/tool receipt recorded;
- no hidden continuation/retry/repair/architecture modification.

Any required false/unknown condition is `BLOCKED` or `FAIL`, never repaired in-run.

## 10. Sufficient future G2A authorization

After package 002 is merged and fresh Pro fills the five dynamic fields, the Owner may authorize with one message of this form:

```text
确认 MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-002，
其 merged blob 为 <DECISION_CANDIDATE_002_BLOB>；
确认 package 002 source-manifest merged blob 为 <SOURCE_MANIFEST_002_BLOB>；
授权仅运行 A0 sentinel。

本次运行窗口保护：
- Mnemosyne master = <PROTECTED_MNEMOSYNE_MASTER>
- Meta-Agent master = <PROTECTED_META_AGENT_MASTER>

使用一段全新的 ChatGPT + GitHub connector 对话；我将选择界面显示的
<AUTHORIZED_VISIBLE_MODEL_LABEL>，并记录模型/推理标签原文。若该选项或必需 GitHub 能力不可用，停止返回，不得替换。

仅允许在 08822407d/mnemosyne-target-lifecycle-validation-002 中，
从 master@e8e3296922185b4b70997c2351d6f39423f2cd4f 创建
v2a-sentinel-001-controller；仅读取
 tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6，
只写 package 002 冻结的七个结果路径；不创建 worker branch 或 PR。

不得写 Mnemosyne、Meta-Agent、validation master、任何 tlr-v1-* ref 或真实目标；
不得运行 A1–A7/V2-B/V2-C，不得使用 Web、Deep Research、Fable、其他 app 或 external quota；
失败后不重试、不 repair。完成后停止，并交给一段全新的 Pro 对话裁决。
```

No repository publication follows this G2A message before A0.

## 11. Capability/research assessment

```yaml
A0_execution:
  capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
  Pro_required: false
A0_fresh_review:
  capability_class: FRONTIER_REQUIRED
Owner_full_V2_A_decision:
  capability_class: HUMAN_REQUIRED
Deep_Research: NOT_NEEDED
parallel_frontier_research: NOT_NEEDED_BEFORE_A0
```

## 12. Current boundary

```yaml
G1A_repaired_package_prepared: true
G2A_execution_authorization: false
controller_branch_created: false
validation_repository_written: false
A0_executed: false
A1_to_A7_authorized: false
V2_B_authorized: false
V2_C_authorized: false
external_quota_authorized: false
real_target_adoption_authorized: false
```
