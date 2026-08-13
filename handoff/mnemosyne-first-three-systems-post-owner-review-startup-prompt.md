# Startup Prompt — Mnemosyne First Three Systems Target-Lifecycle Handoff Continuation

> Use only after the MNEMOSYNE-208 handoff-closeout PR is merged to `08822407d/Mnemosyne@master`. Start a new Pro/frontier conversation with this prompt. Handoff receive and guidance refresh are separate operations.

```yaml
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
  ordered_operations:
    - receive_authorized_handoff_package
    - execute_Load_Mnemosyne_guidance_as_separate_operation
    - continue_received_task_under_refreshed_constraints
```

```text
@GitHub 请接收并继续以下 Mnemosyne 交接包：

`handoff/mnemosyne-first-three-systems-post-owner-review-handoff-package.md`

不要从旧聊天记忆推断仓库状态，也不要导入其他维护路线。

第一步只做 handoff receive：

1. 从执行时最新的 `08822407d/Mnemosyne@master` 读取：
   - `current/human-approved-spec.md`
   - `commands/receive-mnemosyne-handoff.md`
   - `handoff/mnemosyne-first-three-systems-post-owner-review-handoff-package.md`
2. 核验 package ID 为 `MNE-FIRST-THREE-SYSTEMS-POST-REVIEW-HANDOFF-001`，task ID 为 `MNEMOSYNE-208`，并确认对应 handoff-closeout PR 已合并。
3. 返回简短的 `mnemosyne_handoff_receive`，说明：
   - package ID；
   - 实际 master commit；
   - handoff-closeout merge 核验；
   - 已读取和缺失的必读文件；
   - received task；
   - 当前执行源；
   - 禁止动作；
   - 一个安全下一步。
4. 不要在 receive 响应中开始 TLR 人工复核、创建分支、做实质设计或写仓库。

如果必读文件缺失、package identity 不一致、handoff-closeout 尚未合并或 package 因后续 master 变化而重大过期，只返回：

`MNEMOSYNE_HANDOFF_RECEIVE_BLOCKED — <具体原因>`

receive 通过后，作为第二个独立操作执行：

`加载 Mnemosyne 指导约束`

刷新时必须保留刚接收的本地任务，不得把 `current/active-context.md`、`handoff/handoff-current.md`、TODO、open questions、FCV/Fable 暂停路线或其他维护状态自动导入为行动计划。

指导刷新通过后，只读取交接包列出的 core evidence。重点核验：

- transcript audit 没有发现实质 Owner 决策遗漏；
- ACAP-037 只有决策路径归类纠正，三个目标的采用结果不变；
- TLR-01 至 TLR-05 尚未开始；
- 分支式中间记录只允许使用 `mnemosyne-tlr-owner-review-001-ledger` 和指定 working root；
- candidate v0.2、验证和目标采用仍未授权。

随后返回简短的 `target_lifecycle_handoff_ready`，列出：

- 当前主线；
- 当前未决问题范围 TLR-01 至 TLR-05；
- 计划使用的 review branch 和 working root；
- 没有启动 review、验证、研究或目标修改；
- 下一步是等待 Owner 将当前新对话切换到次一档模型，并发送：
  `notes/owner-review-packages/target-agent-lifecycle-v0.1/09-branch-backed-startup-message.md`

返回 ready receipt 后停止。不要自动开始 TLR，也不要提前创建 review branch。

当 Owner 切换到次一档模型并显式启动 `09-branch-backed-startup-message.md` 后，才按该文件创建或继续唯一 review branch、逐题处理 TLR-01 至 TLR-05 并写中间 ledger。全部问题完成且 Owner 确认后，再切换回 Pro/frontier，并在同一个 review branch 上进行综合、纠正和清理；不要创建第二个分支。

不要修改或激活 Meta-Agent，不要写业务目标仓库，不要运行验证、Deep Research、Fable 或 quota-consuming work，除非 Owner 后续另行明确授权。
```

## Execution intent

```yaml
response_role: preparation_only
execution_disposition: RUN_AFTER_GATE_SELECTED
gate: MNEMOSYNE_208_PR_merged_and_Owner_starts_new_conversation
external_execution_or_quota_authorized: false
```
