# Mnemosyne F1 Validation-Disposition Handoff Package

```yaml
package_id: MNE-F1-VALIDATION-DISPOSITION-HANDOFF-001
package_tier: standard
package_status: non_execution_source_transfer_artifact
created_by_task: MNEMOSYNE-227
generated_at: 2026-08-15
repository: 08822407d/Mnemosyne
source_master_at_preparation: 5ca091e1c52bb1e7483b2d54e9259d3ec85b7b93
source_master_meaning: PR_294_merge_commit_and_latest_master_at_preparation
handoff_preparation_branch: mnemosyne-227-f1-validation-disposition-handoff
source_conversation_visible_selection_reported_by_Owner: Pro
source_conversation_backend_identity: unknown_or_not_attestable
intended_receiver: fresh_standard_ChatGPT_Pro_conversation_with_GitHub_read_access
intended_receiver_action: receive_mnemosyne_handoff
source_conversation_role_after_handoff: historical_fallback_and_post_merge_verification_only
new_conversation_role: F1_validation_disposition_coordinator
current_execution_source:
  path: current/human-approved-spec.md
  status: only_execution_source
  blob_at_preparation: 01f64a8223677829320c66dd46d3f172cc9155cc
receiving_operations_contract_ref: notes/object-templates-and-id-rules.md::Handoff_non_execution_source
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
  ordered_operations:
    - receive_authorized_handoff_package
    - emit_mnemosyne_handoff_receive_report
    - stop_after_receive_report
    - wait_for_separate_user_instruction
    - execute_Load_Mnemosyne_guidance_as_separate_operation
    - confirm_received_F1_task_preserved
    - continue_received_task_under_refreshed_constraints
receiving_operation_statuses:
  receive_handoff: pending
  receive_report: pending
  project_guidance_load: not_applicable
  mnemosyne_guidance_refresh: pending
  substantive_continuation: blocked_pending_prerequisites
```

## 1. Purpose and transfer scope

本包把当前对话中的 **F1「可复用 Agent 能力归属与生命周期」有界验证处置门槛**交给一段新的 Pro 对话。

交接只包含：

- 核验 F1 已接受的暂定架构基线；
- 核验有界验证设计和验证包已经准备完成但尚未选择执行；
- 用自然中文向 Owner 说明 A/B/C/D 四种处置的实际含义；
- 获取 Owner 的明确选择或修改；
- 在没有明确选择时保持 no-write / no-run。

本包不接管 F2/V2、Meta-Agent、真实目标、Target-Lifecycle、Fable、Work 或其他 Mnemosyne 路线。

## 2. Why the old conversation stops here

当前 F1 路线不存在还能在不改变 Owner 决策含义的情况下继续自动推进的 substantive 工作。

```yaml
current_phase: F1_bounded_validation_design_complete
current_gate: OWNER_VALIDATION_DISPOSITION
human_interaction_required: true
Owner_choice_recorded: false
execution_profile_selected: false
validation_execution_authorized: false
implementation_authorized: false
```

验证设计、精确执行方案、验证运行、fresh-Pro 裁决、实现和真实目标采用是分开的门槛。当前必须先由 Owner 决定是否继续准备合成验证的精确执行方案。

## 3. Authority and non-execution-source boundary

- `current/human-approved-spec.md` 是 Mnemosyne 唯一执行源。
- 本 handoff package、startup prompt、F1 current status、候选架构、Owner 决定、验证设计、验证包、结果记录和 PR metadata 都不是执行源。
- F1 架构 Owner 决定已经接受的是 **modified provisional baseline**，不是生产就绪或真实目标采用。
- 本包不包含新的架构接受、验证授权或仓库写入授权。
- GitHub app 的技术权限、当前连接状态或历史授权不构成本任务写入授权。
- consumer UI 中选择 `Pro` 只作为 Owner 报告的可见选择；隐藏 backend 仍为 `unknown_or_not_attestable`。

## 4. Immutable source identities

接收时优先验证这些精确对象，而不是要求 `master` 永远等于交接准备前的 SHA：

```yaml
source_identities:
  README:
    path: README.md
    blob: b6d99d254a01a30c930bc44e3f99c448589734da
  execution_source:
    path: current/human-approved-spec.md
    blob: 01f64a8223677829320c66dd46d3f172cc9155cc
  handoff_receive_command:
    path: commands/receive-mnemosyne-handoff.md
    blob: fa7fd7d31fdfd1663ea328db6c82e5c3a7b46cde
  guidance_load_command:
    path: commands/load-mnemosyne-guidance.md
    blob: 1124c2e058bba339688641c45ddf18a65f97e1ef
  F1_status_after_handoff_preparation:
    path: current/reusable-agent-capability-ownership-research-status.md
    blob: ac265b00278440e68d5c87137f2c9a45d962283f
  F1_architecture_candidate:
    path: notes/reusable-agent-capability-ownership-and-lifecycle-model-candidate-v0.1.md
    blob: accb13ccb57677d316f5f94ef58f7939ad69521b
  F1_architecture_Owner_decision:
    path: notes/owner-decision-results/MNE-REUSABLE-CAPABILITY-OWNERSHIP-OWNER-DECISION-001.md
    blob: e75fa69cbbaa206e480a889ff3eb1302a6780d80
  bounded_validation_design:
    path: notes/validation-designs/reusable-capability-ownership-and-lifecycle-bounded-validation-v0.1.md
    blob: 1a6103a357b70ed866e357ceef5b94522c50e49f
  bounded_validation_package_README:
    path: notes/reusable-capability-ownership-validation-package-v0.1/README.md
    blob: 64633a99eb2899255e9d24cecaa140128c7b729f
  validation_disposition_candidate:
    path: notes/owner-decision-candidates/MNE-REUSABLE-CAPABILITY-OWNERSHIP-VALIDATION-DISPOSITION-CANDIDATE-001.md
    blob: 8e416cf8347239afad4d6b16daa2472195612821
```

Publication of this handoff package will itself move `master`. Therefore receive validity is based on the package being present on current `master`, current `master` containing or descending from the package publication, and the load-bearing path/blob identities remaining exact. Do not require equality to the pre-publication SHA `5ca091e1...`.

## 5. Completed work

已完成：

1. 独立 Fable F1 研究；
2. fresh Pro 实质裁决 `ACCEPT_WITH_MATERIAL_CORRECTIONS`；
3. Pro 修正后的 F1 candidate v0.1；
4. Owner 选择架构 Option A，接受 modified provisional baseline；
5. 六场景公共合成有界验证设计；
6. 场景合同、机械检查、语义量表、结果模板和完整性清单；
7. 验证处置 A/B/C/D 候选；
8. PR #293 合并及只读 post-merge 核验；
9. “下一步仓库写入：是/否/待单独授权/待确认”回复约束进入 guidance load；
10. PR #294 已先于本交接合并，当前仓库在交接准备前没有开放 PR 或其他活动分支。

## 6. Current task transferred to the receiver

```yaml
current_task_from_package:
  task: obtain_explicit_Owner_disposition_for_F1_bounded_validation
  decision_candidate: MNE-REUSABLE-CAPABILITY-OWNERSHIP-VALIDATION-DISPOSITION-CANDIDATE-001
  permitted_dispositions:
    - A_ACCEPT_DESIGN_AND_AUTHORIZE_EXACT_EXECUTION_PROFILE_PREPARATION_ONLY
    - B_ACCEPT_DESIGN_BUT_DEFER_SYNTHETIC_EXECUTION_PREPARATION
    - C_REVISE_DESIGN
    - D_REJECT_BOUNDED_VALIDATION_AND_STOP_AT_PROVISIONAL_BASELINE
  recommendation: A
  recommendation_status: advisory_rejectable_not_defaulted
  safe_default_if_Owner_does_not_decide: no_repository_write_no_validation_action
```

新对话不得把“接收 handoff”“加载指导”“继续工作”或本包中的 recommendation 解释成 Owner 已选择 A。

## 7. Decision semantics

### A — 接受设计，只授权准备精确执行方案

接受六场景公共合成设计。下一阶段可另开任务冻结：

- 使用哪个公共合成仓库或 Git 表面；
- 精确 base / fixture / controller branch；
- 模型与产品表面；
- package blobs、输出路径和 no-write evidence；
- 并行路线复核；
- startup / return contract。

A **不授权运行验证**。精确方案准备完成后仍需第二次 Owner 执行授权。

### B — 接受设计，但暂不准备合成执行

保留设计，不选择执行仓库，不准备运行包。未来若 Meta-Agent 在独立授权下建设真实业务功能代码库 Agent，可把真实使用观察作为主要证据。B 不启动该建设。

### C — 修改设计

Owner 可修改场景、合成目标、关系字段、负担证据、接受标准、阶段分离或仓库约束。修改后需重新审查；不得猜测 Owner 未说明的改动。

### D — 拒绝有界验证

F1 暂定架构保持为未实现、未验证的设计候选；不再准备该验证，也不把它用于目标采用或生产就绪主张。

## 8. One safe next action

Startup receive 操作必须在 `mnemosyne_handoff_receive` 报告后停止。

用户下一条单独发送 `加载 Mnemosyne 指导约束` 后，receiver 应确认交接任务未被替换，然后：

> 用自然中文简要说明 A/B/C/D 的差别、推荐 A 的理由和每项不会自动授权什么，并请求 Owner 明确选择或修改。

在 Owner 作出选择以前，不创建 branch、commit、PR、execution profile、validation repository 或 cross-conversation task。

## 9. Forbidden automatic actions

Receiver 不得自动：

- 选择 A/B/C/D；
- 创建、修改或运行验证仓库；
- 准备精确执行方案；
- 运行任何 F1 cell；
- 修改 F1 candidate 或 Owner architecture decision；
- 实施 capability lifecycle schema；
- 建设业务功能代码库 Agent；
- 读取或修改真实业务仓库；
- 修改 Meta-Agent；
- 启动 target adoption、migration、activation 或 pilot；
- 修改 `current/human-approved-spec.md`；
- 进入、裁决或继续 F2/V2；
- 发出 V2-A G2A 或 A0 授权；
- 创建 `v2a-sentinel-001-controller`；
- 运行 Work、Deep Research、Fable 或消耗外部 quota；
- 导入 `current/active-context.md`、`handoff/handoff-current.md`、`current/todo.md` 或 `current/open-questions.md` 作为 action plan；
- 创建 branch、PR、comment、review、merge 或 auto-merge。

## 10. F2/V2 exclusion and current repository context

PR #294 / MNEMOSYNE-226 已合并为交接准备时的最新 `master@5ca091e1...`。它属于独立 F2/V2 路线，并不使 V2-A A0 成为本 handoff 的下一步。

F2/V2 文件可以作为仓库中存在的独立历史/当前证据，但 receiver 不应读取或处理它们，除非 Owner 以后显式改变路线。本 handoff 的 read order 不包含 F2/V2 status、package 003 或 G2A materials。

## 11. Minimum receive evidence and read order

第一轮接收只需：

1. `README.md`；
2. `current/human-approved-spec.md`；
3. `commands/receive-mnemosyne-handoff.md`；
4. 本 handoff package；
5. `current/reusable-agent-capability-ownership-research-status.md`；
6. `notes/owner-decision-candidates/MNE-REUSABLE-CAPABILITY-OWNERSHIP-VALIDATION-DISPOSITION-CANDIDATE-001.md`；
7. 必要时读取本包列出的精确 candidate / Owner decision / validation design / package README 以核验关键 claim。

第一轮不要加载 guidance；guidance 是 receive report 之后的独立操作。

第二轮 guidance refresh 应按 `commands/load-mnemosyne-guidance.md` 读取其 required files，并确认 received F1 task preserved。

## 12. Freshness, unknowns, and stale items

```yaml
preparation_time_repository_state:
  latest_master: 5ca091e1c52bb1e7483b2d54e9259d3ec85b7b93
  open_PRs: []
  visible_branches_before_handoff_branch_creation:
    - master
known_stale_item_repaired_by_MNEMOSYNE_227:
  - F1_status_safe_next_action_previously_said_publish_MNEMOSYNE_225_after_PR_293_had_merged
unknowns:
  - future_master_after_handoff_PR_merge
  - future_open_PR_or_branch_state
  - hidden_backend_identity
  - unsubmitted_intentions_in_other_conversations
```

Receiver must recheck current `master` and open repository state before any later write-producing task. Accessible GitHub state cannot prove that another conversation has no unsubmitted intent.

## 13. Evidence map

| Claim | Evidence path | Authority / role |
|---|---|---|
| Only execution source | `current/human-approved-spec.md` | execution source |
| Handoff receive protocol | `commands/receive-mnemosyne-handoff.md` | user-approved command, non-execution source |
| Guidance refresh protocol | `commands/load-mnemosyne-guidance.md` | user-approved command, non-execution source |
| F1 architecture accepted provisionally | `notes/owner-decision-results/MNE-REUSABLE-CAPABILITY-OWNERSHIP-OWNER-DECISION-001.md` | Owner decision record |
| F1 design and package prepared | `notes/validation-designs/reusable-capability-ownership-and-lifecycle-bounded-validation-v0.1.md`; `notes/reusable-capability-ownership-validation-package-v0.1/README.md` | prepared validation candidate |
| Owner validation disposition pending | `current/reusable-agent-capability-ownership-research-status.md`; decision candidate | current view + decision candidate |
| No validation authorization | same F1 status and package | explicit boundary |
| Real code-library Agent not started | same F1 status/design | explicit route boundary |

## 14. Explicitly excluded

- full old conversation export;
- raw Git diffs;
- complete Fable report reconstruction;
- F2/V2 package or execution route;
- Meta-Agent construction route;
- real target identity or private materials;
- speculative post-decision implementation;
- maintenance live-state files as receiver action plan;
- hidden platform memory as truth.

## 15. User transfer instruction

After the handoff PR is merged, create a fresh standard ChatGPT Pro conversation in the Mnemosyne project and:

1. enable/read the GitHub connection for `08822407d/Mnemosyne`;
2. send the paired prompt at `handoff/mnemosyne-f1-validation-disposition-startup-prompt.md`;
3. wait for the first-round `mnemosyne_handoff_receive` report;
4. send `加载 Mnemosyne 指导约束` as a separate next message;
5. after guidance refresh, let the new conversation explain A/B/C/D and request the Owner decision.

This package does not authorize GitHub writes in the receiving conversation.
