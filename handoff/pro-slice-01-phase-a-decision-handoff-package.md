# PRO-SLICE-01 Phase A Decision Handoff Package

```yaml
package_id: MNEMOSYNE-PRO-SLICE-01-PHASE-A-DECISION-HANDOFF-001
created_by_task: MNEMOSYNE-156
package_status: non_execution_source_transfer_artifact
intended_receiver_action: receive_mnemosyne_handoff
repository: 08822407d/Mnemosyne
prepared_at: 2026-07-26
current_execution_source: current/human-approved-spec.md
trusted_default_branch: master
trusted_default_branch_sha: accaa83324418068ed5b1c32390139eb9ffe0d48
verified_merge:
  PR: 206
  merge_commit: accaa83324418068ed5b1c32390139eb9ffe0d48
  merged_at: 2026-07-26T02:42:24Z
  master_identical_to_merge_commit: true
source_conversation_role_after_handoff: historical_fallback_and_post_handoff_storage_only
new_conversation_role: PRO_SLICE_01_phase_A_disposition_and_task_generation_coordinator
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
  ordered_operations:
    - receive_authorized_handoff_package
    - emit_mnemosyne_handoff_receive_report
    - stop_after_receive_report
    - wait_for_separate_user_instruction
    - execute_Load_Mnemosyne_guidance_as_separate_operation
    - confirm_received_task_preserved
    - continue_received_task_under_refreshed_constraints
```

## 1. Purpose

本包把 `PRO-SLICE-01` 的下一决策门从当前超长维护对话交给一段新的 Mnemosyne 项目内普通 Pro 对话。

交接范围仅限：

- 核验 PR #206 后的可信仓库基线；
- 接收并保持 `PRO-SLICE-01` 的 v2 patch specification 结论；
- 向用户呈现 Phase A 的明确处置选项；
- 只有用户明确接受 Phase A 后，才可生成一个新的、尚不执行的 repository-write implementation task；
- Phase A 实际写入、PR 创建和合并仍需新的任务级授权。

本包不接管其他 Mnemosyne 工作主线。

## 2. Authority boundary

- `current/human-approved-spec.md` 是 Mnemosyne 唯一执行源。
- 本 package、startup prompt、current status、v1/v2 patch specification、maintainer receipt、task result 和 PR metadata 都不是执行源。
- PR #206 的合并只激活 complete-response transfer-file 行为规则并保存 v1/v2 证据；它没有批准 Phase A 或 Phase B patch。
- GitHub 技术权限、approval card、app connection 或 persistent permission 不是当前写入授权。
- consumer Chat 中选择 `Pro` 只能作为 operator-visible / operator-reported selection；特定响应后台身份仍为 `UNKNOWN_OR_NOT_ATTESTABLE`。

## 3. Verified post-merge baseline

```yaml
post_merge_verification:
  PR_206:
    state: closed
    merged: true
    merge_commit: accaa83324418068ed5b1c32390139eb9ffe0d48
  default_branch:
    branch: master
    sha: accaa83324418068ed5b1c32390139eb9ffe0d48
    relation_to_merge_commit: identical
  execution_source_modified_by_PR_206: false
  complete_response_rule_active_on_master: true
  phase_A_started: false
  phase_B_started: false
```

Phase A 五个目标文件仍保持 v2 分析时的 exact blob：

```yaml
phase_A_source_identity:
  notes/object-templates-and-id-rules.md: 5dcb779314ca53a44f5c8ccdb26b65ac5fa8c8d7
  notes/self-improvement-template-pack.md: 1b35d5cada11a4448d9e5c2dcb5722be4890a408
  notes/first-target-project-dry-run-manifest-template.md: 1525333e61494133674db44ee8b88856d4427221
  notes/first-real-target-dry-run-evaluation-framework-v0.1.md: a366d29c4ac7fe615e52f4813f0fe98f62e70ab0
  notes/first-real-target-dry-run-scorecard-v0.1.md: 553306bf04fe436a5ed8535a331fd88cc8c4e152
  v2_anchor_compatibility_at_handoff_preparation: pass
```

任何实施任务仍必须在自己的 pinned latest master 上重新核验 blob、literal anchor、SHA-256、open-work overlap 和 single-active-PR lineage。

## 4. Completed work

已完成并入库：

1. Fable Greenfield 独立设计、self-critique、bounded repair、reverification 与 GF-STEP-5 comparison；
2. Work Ultra Stage A pre-reveal assessment；
3. Work Ultra Stage B reveal/crosswalk/triage；
4. 当前标称 Pro 的实质维护者裁决；
5. `PRO-SLICE-01-PATCH-SPEC-001` v1；
6. v1 的维护者 `ACCEPT_WITH_REQUIRED_REVISION`；
7. `PRO-SLICE-01-PATCH-SPEC-002` v2；
8. v2 对 R1–R10 的十项修复；
9. v1/v2 13 个 transfer originals 的 exact archive；
10. complete-response transfer-file behavior rule；
11. PR #206 合并与 post-merge verification。

```yaml
v2_disposition:
  artifact_integrity: pass
  revision_items:
    repaired: 10
    partial: 0
    rejected: 0
    blocked: 0
  patch_records: 29
  proposed_changed_files: 9
  atomicity: TWO_SEQUENTIAL_NONPARALLEL_IMPLEMENTATION_TASKS
  ready_for_user_patch_scope_approval: true
  implementation_authorized: false
```

## 5. Transferred task and current gate

```yaml
current_task_from_package:
  task: obtain_explicit_user_disposition_for_PRO_SLICE_01_PHASE_A
  permitted_dispositions:
    - ACCEPT_AS_SPECIFIED
    - ACCEPT_WITH_MODIFICATIONS
    - DEFER
    - REJECT
  safe_default_if_user_does_not_decide: no_repository_write
  implementation_task_generation_before_acceptance: prohibited
  repository_write_before_new_task_local_authorization: prohibited
```

新对话应向用户清楚呈现 Phase A 的范围和这四个选项。不得把“继续工作”“接收 handoff”或“加载 guidance”解释成 Phase A 接受。

## 6. Phase A candidate scope

```yaml
phase_A:
  id: PHASE_A_FOUNDATION
  purpose:
    - evidence_bearing_repository_capture_safety_preflight
    - one_of_storage_routes
    - surface_specific_mechanical_no_write_evidence
    - coherent_run_scoped_exception_semantics
    - repository_action_context
    - handoff_operation_state
  paths:
    - notes/object-templates-and-id-rules.md
    - notes/self-improvement-template-pack.md
    - notes/first-target-project-dry-run-manifest-template.md
    - notes/first-real-target-dry-run-evaluation-framework-v0.1.md
    - notes/first-real-target-dry-run-scorecard-v0.1.md
  patch_ids:
    - P01-A
    - P01-B
    - P01-C
    - P02-A
    - P02-B
    - P02-C
    - P03-A
    - P03-B
    - P04-A
    - P04-B
    - P05-A
  patch_count: 11
  execution_source_change: false
  historical_record_rewrite: false
  target_project_action: false
  external_research_required: false
```

Phase A 不采用完整 Greenfield 架构；它只把当前 execution source 已批准的硬合同传播到五个 foundational non-execution-source files。

## 7. Decision semantics

- `ACCEPT_AS_SPECIFIED`：接受五文件、11 patch exact v2 scope。下一步只可生成新的 read-only implementation taskbook；实际写入仍需新授权。
- `ACCEPT_WITH_MODIFICATIONS`：用户必须明确修改哪些 path / patch ID；不得由新对话猜测。受影响 literal anchors 需要重新生成和复核。
- `DEFER`：仓库不变，v2 保持 advisory candidate。
- `REJECT`：记录拒绝范围和理由；不自动切换到 Phase B、research 或其他路线。

## 8. Phase B stop gate

```yaml
phase_B:
  id: PHASE_B_PROPAGATION
  paths:
    - notes/handoff-package-strategy-v0.1.md
    - notes/delivery-package-workflow.md
    - notes/delivery-manifest-template-pack.md
    - notes/target-project-memory-system-template-pack.md
  patch_count: 18
  status: blocked
  prerequisites:
    - Phase_A_single_canonical_PR_merged
    - Phase_A_literal_replacements_verified
    - R1_through_R5_semantics_consistent
    - protected_paths_and_historical_records_unchanged
    - fresh_master_and_open_work_overlap_recheck
    - fresh_user_authorization_for_Phase_B
```

不得提前创建 Phase B branch 或 PR。

## 9. Evidence paths

Minimum receive evidence:

- `README.md`
- `current/human-approved-spec.md`
- `commands/receive-mnemosyne-handoff.md`
- this package
- `current/pro-slice-01-patch-specification-status.md`
- `notes/complete-response-transfer-file-behavior-adoption-record.md`

Guidance refresh evidence after receive:

- `commands/load-mnemosyne-guidance.md`
- `current/artifact-delivery-and-direct-generation-guard.md`
- `current/run-context-and-pr-provenance-guard.md` when later taskbook/write work is in scope
- `current/github-single-active-pr-lineage-guard.md` when later branch/PR work is in scope

Patch-specification evidence:

- `notes/cross-model-review-results/PRO-SLICE-01-PATCH-SPEC/README.md`
- `notes/cross-model-review-results/PRO-SLICE-01-PATCH-SPEC/manifest.yaml`
- `notes/cross-model-review-results/PRO-SLICE-01-PATCH-SPEC/maintainer-receipt.md`
- exact archive parts under `notes/cross-model-review-results/PRO-SLICE-01-PATCH-SPEC/archive-parts/`

Useful direct transfer originals after user acceptance:

```yaml
v2_direct_transfer_originals:
  - filename: PRO-SLICE-01-PATCH-SPEC-002-file-and-contract-matrix.yaml
    bytes: 108937
    sha256: 88f8ae0b80d909af7165402c4f75b8afd33b474f4397cd073b2a5bcbb708adad
  - filename: PRO-SLICE-01-PATCH-SPEC-002-validation-plan.md
    bytes: 10210
    sha256: bf13527195b9f0763ffe1510c630247856251bfc01973a1b4bc5dfe4e7afd3b2
  - filename: PRO-SLICE-01-PATCH-SPEC-002-source-and-overlap-ledger.yaml
    bytes: 11503
    sha256: ba179ffbc477821f7a990411c34cd683889be220501ad732f4442c977942251a
```

The receive report does not require reconstruction of the full archive.

## 10. Forbidden automatic actions

The receiver must not automatically:

- modify `current/human-approved-spec.md`;
- execute or authorize Phase A;
- execute, generate, or authorize Phase B before the stop gate;
- create a branch, PR, issue, comment, review, merge, or auto-merge;
- access target-project materials or perform target work;
- resume another project or maintenance workstream;
- reopen Fable Stage A/B or GF-STEP-5;
- start FABLE5-GOV deferred-governance or platform/model-routing research;
- adopt universal event journal or numeric validation instruments;
- infer backend model identity;
- use maintenance live-state files as the action plan.

## 11. Safe next action

The startup operation stops after the receive report.

After the user separately sends `加载 MNEMOSYNE 约束指导` and the receiver confirms the handoff task was preserved, the safe next action is to present the exact Phase A scope and ask the user to choose `ACCEPT_AS_SPECIFIED`, `ACCEPT_WITH_MODIFICATIONS`, `DEFER`, or `REJECT`.

## 12. Freshness and unknowns

- Verified baseline: `master@accaa83324418068ed5b1c32390139eb9ffe0d48` at package preparation.
- The receiver must recheck current `master` before relying on exact anchors or generating any implementation task.
- No Phase A user disposition is recorded.
- No Phase A or Phase B implementation has started.
- No backend model identity is attested.
- Accessible GitHub state cannot establish unpushed local branches or inaccessible external systems.
- This package transfers only this local route; it is not a global Mnemosyne maintenance handoff.

## 13. User transfer instruction

In a new standard ChatGPT Pro conversation inside the existing Mnemosyne project:

1. add the GitHub app/plugin and use read-only access for receive;
2. provide or authorize this package path;
3. send the paired startup prompt;
4. wait for `mnemosyne_handoff_receive`;
5. in the next message separately send `加载 MNEMOSYNE 约束指导`;
6. only after the guidance refresh, discuss Phase A disposition.

This package does not authorize GitHub writes.