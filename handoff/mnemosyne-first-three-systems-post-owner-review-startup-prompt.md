# Startup Prompt — Mnemosyne First Three Systems Post-Owner-Review Continuation

> Use only after the MNEMOSYNE-205 PR is merged to `08822407d/Mnemosyne@master`.

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
   - `README.md`
   - `current/human-approved-spec.md`
   - `commands/receive-mnemosyne-handoff.md`
   - `handoff/mnemosyne-first-three-systems-post-owner-review-handoff-package.md`
2. 返回 `mnemosyne_handoff_receive`，说明 package ID、实际 master commit、已核验/缺失证据、received task、禁止动作和一个安全下一步。
3. 不要在 receive 响应中开始实质设计或仓库写入。

receive 通过后，作为第二个独立操作执行：

`加载 Mnemosyne 指导约束`

刷新时必须保留刚接收的本地任务，不得把 `current/active-context.md`、`handoff/handoff-current.md`、TODO、open questions、FCV/Fable 暂停路线或其他维护状态自动导入为行动计划。

指导刷新通过后，再读取：

- `notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002.md`
- `notes/first-three-system-capability-selection-v0.3.md`
- `notes/target-agent-container-evolution-and-dependency-model-candidate-v0.1.md`
- `notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.1.md`
- `current/first-three-systems-owner-review-status.md`

然后只推进这一条线：

审查“目标 Agent 容器、演化轴与依赖责任”候选是否准确落实 Owner 已确认决定；发现问题时在一个新任务 ID、一个 canonical branch、至多一个 Draft PR 中修订。没有发现结构性问题时，准备公共/合成、无私有材料的 bounded validation task，但不要运行，除非用户另行授权。

不要重新开展 OR-01 至 OR-09 全量人工审阅。不要修改或激活 Meta-Agent，不要创建/写入业务目标仓库，不要启动 Deep Research、Fable 或 quota-consuming run。
```

## Execution intent

```yaml
response_role: preparation_only
execution_disposition: RUN_AFTER_GATE_OPTIONAL
gate: MNEMOSYNE_205_PR_merged_and_user_selects_new_conversation_handoff
external_execution_or_quota_authorized: false
```
