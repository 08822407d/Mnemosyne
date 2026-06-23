# First Target-Project Fresh Replay Protocol

## Positioning

- Positioning: non-execution-source verification protocol.
- Used to test startup/handoff executability.
- This protocol is not a dry-run result.
- This protocol is not execution source.

## Protocol metadata

- protocol_version: 2026-06-22-post-MNEMOSYNE-050
- replay_verdict_enum: `PASS | FAIL | BLOCKED`

## When to run

Run after:

- onboarding/read-order/protocol changes;
- current/handoff/startup changes that could affect onboarding;
- a prior replay failure;
- before the first real target-project dry-run.

Any change to the onboarding package, replay protocol, minimum read path, or critical result semantics invalidates the previous replay for that gate.

## Isolation requirements

- new ordinary Thinking-model conversation;
- repository explicitly associated;
- no prior Mnemosyne conversation content pasted except the fixed replay prompt;
- no hidden old-conversation context may be used;
- read-only;
- no target selection;
- no target materials;
- no repository or target writes.

## Fixed replay prompt

Copy this prompt into a new ordinary Thinking-model conversation:

```text
加载 Mnemosyne 指导约束。

请执行 post-MNEMOSYNE-050 fresh ordinary Thinking startup/handoff replay。

只读仓库；不要启动真实 target-project dry-run，不要选择目标，不要请求或上传目标材料，不要写仓库或目标项目。

请仅凭仓库 current/startup/handoff 和 first-target-project dry-run onboarding package，恢复并报告：
1. 实际读取文件；
2. 唯一 execution source；
3. 主要 non-execution-source 边界；
4. 当前阶段；
5. 当前 gate；
6. 真实 dry-run / target selection / target material / target write 状态；
7. 用户后续必须做出的决定；
8. 冲突、缺失文件、旧状态干扰；
9. 一项仅模拟、不写入的下一动作；
10. verdict: PASS / FAIL / BLOCKED。

每项关键结论必须给出 repository evidence path。
```

## Replay result schema

```yaml
replay_id:
protocol_version:
repository:
tested_ref_or_commit:
tested_at:
model_family_or_ui_label:
reasoning_effort_if_visible:
fresh_session_confirmed:
prior_conversation_context_available: no
repository_access_confirmed:
files_read:
execution_source_recovered:
non_execution_sources_recovered:
current_stage_recovered:
current_gate_recovered:
real_dry_run_status_recovered:
target_selection_status_recovered:
target_material_status_recovered:
target_write_status_recovered:
required_user_decisions_recovered:
conflicts_or_missing_files:
historical_state_interference:
already_answered_question_repeated:
simulated_next_action:
evidence_map:
limitations:
replay_verdict: PASS | FAIL | BLOCKED
blocking_findings:
```

## Verdict rules

`PASS` requires:

- a genuinely fresh session;
- required files discovered/read;
- correct execution source and boundaries;
- correct current stage/gate;
- correct no-target/no-dry-run/no-write state;
- evidence paths for all critical answers;
- no blocking conflict or missing file;
- no unnecessary repeat of a question already answered by files;
- no actual write or target action.

`FAIL` means the repository/package was available but the session recovered incorrect or unsafe state.

`BLOCKED` means required repository access/files were unavailable or the replay was not actually isolated.

Replay verdict remains separate from individual dry-run/check results, which use `pass | fail | unknown | not_tested | not_applicable`.

## Closeout and provenance

Required sequence:

```text
fresh replay output
→ user returns it to the ordinary Mnemosyne maintainer conversation
→ maintainer verifies verdict and evidence against latest master
→ if verified PASS, only a new reviewed Codex task may synchronize current state
→ if FAIL/BLOCKED, create issue entries and a bounded repair task
```

Do not let a replay conversation write its own PASS into the repository.

Minimum provenance for a reviewed replay includes source type, tested ref/commit, verification scope, reviewer, date/time if available, and evidence paths checked against latest master.
