# Meta-Agent Regression Fresh-Session Replay — Startup Status

> Non-execution-source startup artifact. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
status: archived_after_cleanroom_replay_review
latest_reviewed_by_task: MNEMOSYNE-122
automatic_additional_ordinary_Chat_replay_authorized: false
current_decision_record: current/meta-agent-replay-mechanical-proof-decision.md
current_cleanroom_replay: META-AGENT-CONSOLIDATED-CLEANROOM-REPLAY-001-v2
```

## 当前状态

不要再使用本文件、Replay v2/v3/v4 packages 或旧 bootstrap 启动新的普通 Chat replay。

Replays 002–004 已重新分类为历史诊断记录，因为用户后来确认：

- 它们在现有 Default-memory Mnemosyne Project 中执行；
- 没有显式通过 `+` 选择 GitHub。

当前接受的行为测试证据来自 consolidated cleanroom replay：

```yaml
replay_id: META-AGENT-CONSOLIDATED-CLEANROOM-REPLAY-001-v2
tested_ref: 714c54ffdb7e5899ef3cac20084bcd82d4db022c
environment_qualification: PASS
behavioral_cases: PASS_5_of_5
mechanical_no_write_subgate: BLOCKED
combined_package_gate: BLOCKED
```

## 解释

Cleanroom replay 使用了用户声明的：

- 新建 Project-only Project；
- 零 prior chats；
- 未加入旧 Mnemosyne chats/files；
- 全局 GitHub repository access；
- 当前 Chat 中通过 `+` 选择 GitHub；
- GitHub chip 可见。

它成功读取固定 commit 上的仓库证据并完成五项正式行为测试。

完整 branch/ref 与 repository-wide PR 覆盖仍不可用，因此 mechanical no-write 和 combined package gate 保持 `BLOCKED`。不得把这项限制改写成行为失败，也不得把行为 PASS 改写成 package-level PASS。

## 模型 provenance 限制

执行提示词中的可见模型和推理标签占位符没有被替换。因此 exact visible labels 记录为 unknown；不得推断隐藏模型等价关系，也不要求仅为补齐该字段而重复整个 replay。

## 后续

当前 test-only 行为目标已经完成，不需要自动运行新的 ordinary-Chat replay。

只有在用户以后明确要求高保证 combined gate 时，才能新建 observer-assisted proof task，由可靠 external/local Git 环境提供完整 before/after mechanical evidence。

## 禁止事项

- 不自动生成或执行 Replay 005 或其他 ordinary-Chat 变体；
- 不批准 no-write exception；
- 不修改执行源；
- 不启动 Meta-Agent 产品构建；
- 不创建 target workspace；
- 不摄入 target materials；
- 不访问或写 target repository；
- 不启动 operational installation；
- 不恢复或接管 FABLE5-GREENFIELD-001。
