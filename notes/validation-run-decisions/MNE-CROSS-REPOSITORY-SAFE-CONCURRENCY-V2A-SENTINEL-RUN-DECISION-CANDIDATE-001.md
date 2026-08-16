# Cross-Repository Safe Concurrency V2-A Sentinel — Pro-Recommended Owner Run Decision Candidate 001

> Exact G1A surface and run-profile recommendation for the Owner-selected V2-A sentinel route. This file is not execution authorization, validation execution, repository creation, connector-permission authority, external-quota authority, architecture promotion or target adoption.

```yaml
decision_candidate_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-001
task_id: MNEMOSYNE-223
source_master: 2308c1e55fbbfb753ec527691809dd8f91f6f462
source_owner_decision: notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md
source_validation_design: notes/validation-designs/cross-repository-safe-concurrency-v2-staged-validation-v0.1.md
source_package: notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/README.md
proposed_run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
status: PRO_RECOMMENDATION_READY_NOT_OWNER_AUTHORIZED
selected_stage_candidate: V2_A
selected_cells_candidate:
  - A0
sentinel_only: true
validation_execution_authorized: false
synthetic_repository_creation_authorized: false
validation_repository_write_authorized: false
external_quota_authorized: false
connector_or_app_change_authorized: false
real_target_adoption_authorized: false
```

## 1. Recommendation

Prepare one **A0-only V2-A sentinel** in the existing public synthetic validation repository:

```text
08822407d/mnemosyne-target-lifecycle-validation-002
```

The sentinel should verify only:

- exact package and source identities;
- repository, branch and fixture identities;
- current product/model/tool receipts;
- public/synthetic material classification;
- exact allowed-write and prohibited-write boundaries;
- protected-repository and protected-ref before/after evidence;
- absence of worker branches, scenario PRs and hidden continuation.

It must stop before A1–A7. It must not construct or modify a V2-A substantive fixture, create a worker branch, create a PR, repair a package, or infer authorization for a full V2-A run.

This is useful because it tests the actual GitHub surface and evidence contract at low cost while preserving the Owner's separate G2A execution gate for substantive cells.

## 2. Exact source package identities

The sentinel package is bound to Mnemosyne:

```yaml
Mnemosyne_source:
  repository: 08822407d/Mnemosyne
  branch: master
  commit: 2308c1e55fbbfb753ec527691809dd8f91f6f462
  required_blobs:
    current/human-approved-spec.md: 01f64a8223677829320c66dd46d3f172cc9155cc
    current/github-single-active-pr-lineage-guard.md: 042efe9e353097a17eea38d0bcb0ff1da7c4385e
    current/run-context-and-pr-provenance-guard.md: 0e588b3f6789d0d941221d33c3eaba1561f6e2a3
    current/user-operation-next-step-capability-and-intent-guard.md: 265d61aad34c9e55006647c9e12d77c4214310ea
    current/fable5-cross-repository-safe-concurrency-research-status.md: 4c83d65e054f1be9022d6c1cf08da014a567b5fe
    notes/owner-decision-results/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-OWNER-DECISION-001.md: 4d59e6edefb5f166261dca353f4552e9346d0f8a
    notes/research-adjudications/MNE-DR-005-CROSS-REPOSITORY-SAFE-CONCURRENCY-PRO-ADJUDICATION-001.md: 27d607257bb1700d9ff9c73f0048a6a7b7847746
    notes/cross-repository-safe-concurrency-and-ordered-work-amendment-candidate-v0.1.md: 46fd66dc23d6615ea167e0950de970cc316c056b
    notes/validation-designs/cross-repository-safe-concurrency-v2-staged-validation-v0.1.md: f66678c0ebdc28a9407553b918838256e6e633a4
    notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/README.md: 3429f981f9b7dc0900dff4d356f9a001c280f1e6
    notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/00-owner-gates-and-stage-boundaries.md: fd56c6710ba4aa76e2e962693e3f97bb35ffb175
    notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/01-synthetic-fixture-and-scenario-contracts.md: 19235ec7110f6ad4f529a09400f00a7b00240934
    notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/02-v2-a-core-concurrency-taskbook.md: c36ac4604dea9ebe1bef00d30bea684db775f687
    notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/03-v2-b-ordered-cross-repository-taskbook.md: 836afd993d19d444a22d75704977c0de8f3383a4
    notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/04-v2-c-connector-security-design-only.md: f99c761245c4c3a5d2229d084fb0fb400b9e7360
    notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/05-mechanical-checks-and-evidence-rubric.md: 59082fb32c1e38d48878bc5f4b4f4faa561e44cb
    notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/06-run-manifest-and-result-template.md: 17494c9bf86a8782f5a3a91c6a33dd14aa27e5a8
    notes/cross-repository-safe-concurrency-v2-validation-package-v0.1/07-package-integrity-and-non-execution-checklist.md: c7ee1083a9b84d7d070dfec7a9bd65655750b4a9
```

Any mismatch before execution invalidates this candidate and requires Pro refresh. The controller must not silently substitute current files.

## 3. D1 — Repository and fixture surface

```yaml
repository_surface_decision:
  disposition: RUN_CANDIDATE
  repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  visibility: public
  repository_exists: true
  default_branch: master
  pinned_controller_base_sha: e8e3296922185b4b70997c2351d6f39423f2cd4f
  read_only_fixture_ref: tlr-v1-fixture-base
  read_only_fixture_commit: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  read_only_fixture_tree: f1e221ce8aef404579b96adb3ab01319016889db
  fixture_material_class: public_synthetic_only
  fixture_modification_authorized: false
  new_repository_creation_authorized: false
```

Why reuse this repository:

- it is already public and synthetic-only;
- it preserves V0→V1 evidence lineage;
- it exposes real branch/ref/write behavior without touching Mnemosyne or Meta-Agent;
- an A0 sentinel does not need a new V2-specific substantive fixture;
- using the existing V1 fixture as a read-only identity surface avoids premature fixture construction.

The future full V2-A run may require a separately prepared V2-A fixture base. A0 success does not pre-authorize or validate that later fixture.

## 4. D2 — Product/model and conversation topology

```yaml
execution_surface_decision:
  controller_surface: standard_ChatGPT_conversation_with_GitHub_connector
  controller_conversation_count: 1
  controller_role: A0_receive_identity_material_permission_and_no_write_controller
  worker_surfaces: []
  worker_branches: []
  scenario_PRs: prohibited
  recommended_controller_visible_selection_if_available: gpt-5.6 sol extra high
  required_visible_selection_verbatim_at_launch: true
  substitution_without_new_Owner_or_Pro_decision: prohibited
  exact_backend_identity: unknown_or_not_attestable
  post_run_review_surface: fresh_ChatGPT_Pro_conversation_with_GitHub_read_access
```

If `gpt-5.6 sol extra high` is not available at launch, or the GitHub tool surface cannot establish exact refs and branch writes, stop and return to Pro. Do not silently substitute another model or product surface.

A0 is frozen, bounded and primarily mechanical; next-tier execution is an appropriate candidate. Fresh Pro remains required for semantic/provenance adjudication before any full V2-A preparation or run.

## 5. D3 — Exact run and branch topology

```yaml
run_topology:
  validation_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-STAGED-VALIDATION-001
  package_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2-PACKAGE-001
  run_id: MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001
  selected_stage: V2_A
  selected_cells:
    - A0
  sentinel_only: true
  controller_branch: v2a-sentinel-001-controller
  controller_branch_base: e8e3296922185b4b70997c2351d6f39423f2cd4f
  controller_PR: null
  fixture_ref_read_only: tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
  worker_branches: []
  worker_PRs: []
  stop_after_A0_bundle: true
```

The controller branch does not yet exist and must not be created until G2A authorization.

## 6. D4 — Exact allowed and prohibited writes

Future A0 allowed write scope, only on `v2a-sentinel-001-controller`:

```text
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/00-controller-receive.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/01-product-and-permission-receipt.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/02-package-and-material-receipt.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/03-repository-and-ref-baseline.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/04-mechanical-checks.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/05-sentinel-result-bundle.yaml
runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/incidents/incident-ledger.yaml
```

```yaml
write_boundary:
  allowed_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  allowed_branch: v2a-sentinel-001-controller
  allowed_paths: exact_list_above
  branch_creation_allowed_after_G2A: v2a-sentinel-001-controller_only
  PR_creation: prohibited
  fixture_write: prohibited
  validation_repository_master_write: prohibited
  existing_tlr_v1_branch_write: prohibited
  Mnemosyne_write: prohibited
  Meta_Agent_write: prohibited
  real_target_read_or_write: prohibited
  unlisted_repository_read_or_write: prohibited
```

No A1–A7 task contract, worker branch, merge-order simulation or substantive fixture change is allowed in A0.

## 7. D5 — Protected repositories and refs

The sentinel must capture before and after refs for:

```yaml
protected_repositories:
  - repository: 08822407d/Mnemosyne
    refs:
      master: 2308c1e55fbbfb753ec527691809dd8f91f6f462
  - repository: 08822407d/Meta-Agent
    refs:
      master: 1fdbd7af9437f72f7c8106714ad1e64908983fb7
  - repository: 08822407d/mnemosyne-target-lifecycle-validation-002
    refs:
      master: e8e3296922185b4b70997c2351d6f39423f2cd4f
      tlr-v1-controller: e892749fc9e242b24908f89b6a78f1c0f0bed75e
      tlr-v1-fixture-base: 81f18eb5dcc6a6e68e496f67ae8f8eae782226e6
      tlr-v1-s1-destination-block: d20f1239784f88072399a3c874800f6c94c0ad2c
      tlr-v1-s2-bounded-writer: b0923aedf551262f0b24409611824c526252982f
      tlr-v1-s3-alpha: 1a8496893260f35b0b06d32d6b2128a192489ae7
      tlr-v1-s3-beta: 9a77045e77856a25336a664840aeaa984cdb8886
      tlr-v1-s4-alpha-dependent: 4861cc27e8960353f29af9ca5cfa0927430b89ad
      tlr-v1-s4-shared-schema: 2aa6c0a8a7ac39ab1d3e06a64006e83aff20b5aa
      tlr-v1-s4-unknown-global: c77f20f0320313d1ccb2b4d1272dfa0daba8ef77
      tlr-v1-s5-upstream-proposal: 8bfd56e5800566b048702d8b8a89e3bd05f9e6e9
      tlr-v1-s6-beta-requirement: e90fcc6633bae50236aa96f9c499ba6c7379f53f
      tlr-v1-s7-alpha-migration: be627df6a1e633e8c93f25c056b643b603f1aea8
      tlr-v1-s7-commonlib-v2: 9cfae2953fa8d7b2ff4ab2e14abab263891932de
      tlr-v1-s8-insufficient-docs: d9c4c88aa17d6edf73955054833bd2738709aec9
      tlr-v1-s9-imperfect-route: b16a458339497425387d71c843388ef30aa2eb46
      tlr-v1-s11-backup-restore: 47262b6bf8f89c9ac13d7f488595f8adff250299
```

At launch, every value must be re-read. A mismatch blocks the run; it does not authorize a refresh or retry. After A0 writes, all listed protected refs must remain unchanged. The only new ref allowed is the named controller branch.

No-write claims remain limited to these named refs, the observed time window and the accessible GitHub action surface.

## 8. D6 — Tool, network and quota boundary

```yaml
tool_boundary:
  GitHub_read_on_Mnemosyne: exact_listed_source_and_before_after_refs_only
  GitHub_write_on_Mnemosyne: prohibited
  GitHub_read_on_Meta_Agent: master_before_after_ref_only
  GitHub_write_on_Meta_Agent: prohibited
  GitHub_read_on_validation_repository: allowed_for_named_refs_and_public_synthetic_material
  GitHub_write_on_validation_repository: exact_controller_branch_and_paths_only_after_G2A
  local_or_mechanical_tools: allowed_for_hash_ref_path_schema_and_count_checks
  web_access: prohibited_not_needed
  Deep_Research: prohibited
  Fable_or_Research: prohibited
  other_connected_apps: prohibited
  private_files_or_conversations: prohibited

quota_decision:
  separate_paid_or_external_quota_authorized: false
  ordinary_plan_use_only: true
```

## 9. D7 — Result storage, retention and cleanup

```yaml
result_storage:
  raw_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
  raw_branch: v2a-sentinel-001-controller
  raw_root: runs/MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-001/
  raw_result_write_to_Mnemosyne: false
  Mnemosyne_ingestion_authorized: false
  required_return:
    - all_seven_output_files
    - controller_branch_head
    - every_output_blob_and_creation_commit
    - protected_before_after_ref_comparisons
    - visible_product_model_and_reasoning_labels
    - incidents_and_unresolved_inputs

retention:
  retain_controller_branch_until:
    - complete_A0_bundle_reviewed_by_fresh_Pro
    - every_required_commit_tree_and_blob_identity_preserved
    - Owner_decides_full_V2_A_or_repair_or_defer
  branch_cleanup: separately_released_after_review
  validation_repository_archive_or_delete: not_authorized
```

## 10. A0 acceptance and stop conditions

A provisional A0 executor PASS requires:

- exact Mnemosyne source commit and listed blobs match;
- validation repository, controller base and read-only fixture identities match;
- material remains public/synthetic;
- selected cells equal `[A0]`;
- controller branch and exact write set are unambiguous;
- no worker branch or PR exists or is created;
- all protected refs are captured before and after and remain unchanged;
- the controller records the actual visible model/reasoning and tool surface;
- all seven output files and exact identities exist;
- no hidden continuation, retry, package repair or architecture modification occurs.

Stop and return `BLOCKED` if any of these is false or unknown. Do not repair or retry.

A0 PASS proves only the bounded repository/material/surface/identity/no-write gate. It does not validate A1–A7, production readiness, connector denial, target adoption or candidate correctness.

## 11. Remaining Owner action

This candidate and its execution package may be merged without authorizing the run.

A later sufficient G2A instruction is:

```text
确认 MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-V2A-SENTINEL-RUN-DECISION-CANDIDATE-001；
授权仅运行 A0 sentinel。

在 08822407d/mnemosyne-target-lifecycle-validation-002 中，
从 master@e8e3296922185b4b70997c2351d6f39423f2cd4f 创建
v2a-sentinel-001-controller，仅读取
 tlr-v1-fixture-base@81f18eb5dcc6a6e68e496f67ae8f8eae782226e6，
只写 run decision 中列出的七个结果路径；不创建 worker branch 或 PR。

使用 ChatGPT GitHub connector；我会选择界面显示的 gpt-5.6 sol extra high，
并记录模型/推理标签原文。若该选项或所需 GitHub 能力不可用，停止返回。
不得写 Mnemosyne、Meta-Agent、现有 V1 refs 或任何真实目标；
不得运行 A1–A7，不得使用 Web、Deep Research、Fable、其他 app 或外部 quota；
失败后不重试。完成后停止并交给全新 Pro 对话裁决。
```

The Owner may correct any repository, model, scope, retention or output decision before G2A.

## 12. Capability and research assessment

```yaml
model_capability_estimate:
  A0_execution:
    capability_class: NEXT_TIER_SUFFICIENT_CANDIDATE
    Pro_required: false
    bounded_components:
      - exact_package_and_ref_receipts
      - material_classification
      - exact_branch_and_path_scope
      - before_after_no_write_comparisons
      - result_template_population
    escalation_triggers:
      - source_or_ref_mismatch
      - authority_or_scope_ambiguity
      - tool_surface_missing_required_branch_or_ref_controls
      - any_need_to_change_package_semantics
      - private_or_real_material_discovered
  A0_fresh_review:
    capability_class: FRONTIER_REQUIRED
  Owner_full_V2_A_decision:
    capability_class: HUMAN_REQUIRED
  exact_backend_identity: unknown_or_not_attestable

deep_research_assessment:
  status: NOT_NEEDED
  reason: the open gap is controlled product/repository execution evidence, not external literature

parallel_frontier_research_assessment:
  status: NOT_NEEDED_BEFORE_A0
  reason: independent research would duplicate an already frozen sentinel contract
```

## 13. Current boundary

```yaml
current_state:
  G1A_surface_decision_prepared: true
  G2A_execution_authorization: false
  controller_branch_created: false
  validation_repository_written: false
  A0_executed: false
  A1_to_A7_authorized: false
  V2_B_authorized: false
  V2_C_authorized: false
  external_quota_authorized: false
  target_adoption_authorized: false
```
