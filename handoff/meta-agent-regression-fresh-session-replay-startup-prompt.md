# Meta-Agent Regression Fresh-Session Replay — Startup Status

> Non-execution-source startup artifact. `current/human-approved-spec.md` remains Mnemosyne's only execution source.

```yaml
status: paused_after_Replay_004
latest_reviewed_by_task: MNEMOSYNE-121
automatic_Replay_005_authorized: false
current_decision_record: current/meta-agent-replay-mechanical-proof-decision.md
```

## 当前状态

不要再使用本文件、Replay v4 package 或 v4 bootstrap 启动新的普通 Chat replay。

已完成的 fresh-session 证据是：

- Replay 002：五项行为 5/5 PASS，整体因机械覆盖不完整而 `BLOCKED`；
- Replay 003：五项行为 5/5 PASS，整体因机械覆盖不完整而 `BLOCKED`；
- Replay 004：literal bootstrap 成功进入用户消息，但 public endpoint 返回不完整且与已合并 PR 状态不一致的数据，因此在五项测试开始前正确 `BLOCKED`。

Replay 004 证明，继续修改 URL、page 参数或 prompt 措辞不足以解决当前 ordinary Chat surface 的机械观测限制。

## 下一步

读取：

- `current/meta-agent-replay-mechanical-proof-decision.md`

在用户选择后，才能决定：

1. 接受两次独立 5/5 行为恢复作为当前测试结果，同时保留机械 no-write gate 为 blocked；或
2. 设计一个由外部 observer / local Git 环境提供 before/after 证据的最终运行。

## 禁止事项

在用户做出该选择前：

- 不生成或执行 Replay 005；
- 不把 Replay 002/003 的 case PASS 提升为 package-level PASS；
- 不把 Replay 004 解释为行为 FAIL；
- 不批准 no-write exception；
- 不修改执行源；
- 不启动 Meta-Agent 产品构建、target workspace、材料摄入、target write 或 operational installation。
