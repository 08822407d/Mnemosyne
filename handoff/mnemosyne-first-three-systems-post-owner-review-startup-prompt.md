# Startup Prompt — Mnemosyne First Three Systems Target-Lifecycle Continuation

> Use only after the MNEMOSYNE-206 PR is merged to `08822407d/Mnemosyne@master`. This prompt is for a later new Pro/frontier conversation. For a same-conversation next-tier Owner review, use the startup message inside `notes/owner-review-packages/target-agent-lifecycle-v0.1/` instead.

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
2. 返回 `mnemosyne_handoff_receive`，说明 package ID、实际 master commit、已核验/缺失证据、received task、禁止动作和一个安全下一步。
3. 不要在 receive 响应中开始实质设计、人工复核或仓库写入。

receive 通过后，作为第二个独立操作执行：

`加载 Mnemosyne 指导约束`

刷新时必须保留刚接收的本地任务，不得把 `current/active-context.md`、`handoff/handoff-current.md`、TODO、open questions、FCV/Fable 暂停路线或其他维护状态自动导入为行动计划。

指导刷新通过后，读取交接包列出的 core evidence 和：

`notes/owner-review-packages/target-agent-lifecycle-v0.1/README.md`

然后只推进“目标 Agent 承载、演化与依赖责任”这一条线。

- 如果 Owner 已在原对话完成并确认 TLR-01 至 TLR-05：读取已保存结果；不要重做访谈。
- 如果尚未完成：不要替 Owner 作答。提示 Owner优先返回原对话切换次一档模型，使用包内 `07-same-conversation-startup-message.md`；如果原对话不可用，再在当前新对话按同一 interviewer contract 进行。
- 不要从同一长对话的模型记忆重构 OR 或 TLR 决定；使用仓库结果，具体争议才请求完整导出。
- 不要修改或激活 Meta-Agent，不要创建/写入业务目标仓库，不要运行验证、Deep Research、Fable 或 quota-consuming work，除非 Owner 后续明确授权。
```

## Execution intent

```yaml
response_role: preparation_only
execution_disposition: RUN_AFTER_GATE_OPTIONAL
gate: MNEMOSYNE_206_PR_merged_and_Owner_selects_new_conversation_handoff
external_execution_or_quota_authorized: false
```
