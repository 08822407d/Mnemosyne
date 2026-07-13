# Mnemosyne Post-113 Maintenance Options Handoff Package

```yaml
package_id: MNEMOSYNE-POST-113-MAINTENANCE-OPTIONS-HANDOFF
created_by_task: MNEMOSYNE-114
package_status: non_execution_source_transfer_artifact
intended_receiver_action: receive_mnemosyne_handoff
repository: 08822407d/Mnemosyne
prepared_at: 2026-07-13
current_execution_source: current/human-approved-spec.md
source_conversation_role_after_handoff: FABLE5_GREENFIELD_result_receiver_and_storage_finisher
new_conversation_role: Mnemosyne_maintenance_route_selection_and_execution
```

## 1. Purpose

当前维护对话已经很长并影响浏览器性能。本包把 **MNEMOSYNE-113 之后的 Mnemosyne 维护主线**交给一段新的 ChatGPT 对话。

旧对话不关闭，而是保留为：

- `FABLE5-GREENFIELD-001` 后续结果的接收者；
- Fable 下载文件的结构检查、保存和 ready PR 收尾者；
- Fable weekly quota 恢复后继续 GF-STEP-2B5 及后续步骤的原上下文。

新对话不得把 Fable greenfield 轨道自动接走，也不得把暂停的 post-handoff Meta-Agent 路线自动恢复。

## 2. Execution-source and authority boundary

- `current/human-approved-spec.md` 是 Mnemosyne 唯一执行源。
- 本 handoff package、review records、current status、handoff files、research reports 和 task result records 都不是执行源。
- PR #160 / MNEMOSYNE-113 已合并；merge commit：`7a88cf299f5dd538d1bae8696da8247c8979b362`。
- MNEMOSYNE-113 已完成第一波 Fable review 的 GPT Pro 实质裁决和支持充分的修补。
- 任何新仓库写入仍须满足当前用户授权、platform permission 和 repository preflight。

## 3. Completed work

### 3.1 Fable first-wave review adjudication

已完成：

- `FABLE5-REVIEW-001`；
- `FABLE5-REVIEW-002`；
- `FABLE5-REVIEW-003`；
- `FABLE5-TRIAGE-001`；
- MNEMOSYNE-097 evidence audit；
- MNEMOSYNE-099 higher-model decision package；
- MNEMOSYNE-113 GPT Pro adjudication and accepted repairs。

主要结论：

- Q2-2 采用 layered canonicalization，不选择一份扁平 warning list；
- frozen MNEMOSYNE-082/083 artifacts 不修改；
- W4 为 validation-only、completion uncertain/interrupted、no real-project acceptance；
- maintainer review provenance 记录为 GPT maintenance conversation generated/performed；
- DRY-RUN-001 equivalent no-write evidence 是历史 run-scoped exception，不是 future precedent；
- R3-F-001..004 已关闭或修复；
- regression candidates 仅形成未来 formalization-decision agenda，尚未 formalize。

### 3.2 Execution-source improvement

`current/human-approved-spec.md` §19 已加入：

- no-write claim 默认需要 `git diff` 类或 pinned before/after repository-state proof；
- exception 需要新的明确 user approval、run scope 和 non-precedent metadata；
- reviewer/actor 和 human verification scope 必须记录；
- execution-source modification result record 必须记录 `user_decision_recorded`；
- same-family review 的 independence limitation 必须标记。

### 3.3 Current wayfinding

- live review status：`current/review-and-validation-status.md`
- Pro decision record：`notes/cross-model-review-results/FABLE5-TRIAGE-001/02-gpt-pro-substantive-adjudication-and-repair-decisions.md`
- live warning interpretation：`notes/first-target-project-intake-records/meta-agent/controlled-dry-run-results/META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001-live-interpretation.md`
- result record：`notes/codex-task-results/MNEMOSYNE-113-result.md`

## 4. Fable greenfield track status

```yaml
track_id: FABLE5-GREENFIELD-001
status: paused_operationally
reason: user_reported_Fable_weekly_quota_exhausted
latest_completed_substep: GF-STEP-2B4B
next_planned_substep: GF-STEP-2B5
failure_classification: not_a_task_failure
substantive_maintainer_acceptance: incomplete_and_not_performed_for_track_as_a_whole
owner_conversation_after_handoff: current_long_conversation
```

Relevant paths：

- `current/review-and-validation-status.md`
- `notes/cross-model-review-results/FABLE5-GREENFIELD-001/manifest.yaml`
- `notes/cross-model-review-results/FABLE5-GREENFIELD-001/incidents/INC-002-weekly-quota-exhaustion.md`

新维护对话不得代替 Fable 补写 GF-STEP-2B5，也不得把现有 greenfield outputs 当成已接受设计。

## 5. ChatGPT Work assessment

Candidate assessment：

- `notes/chatgpt-work-mode-assessment-2026-07.md`

当前结论：

- **handoff receive 和路线选择：使用普通 Chat，GPT-5.6 Sol + Pro；不需要 Work。**
- **大型 read-only comprehensive health review：可以考虑 Work。**
- **软件开发、测试、命令、repository implementation：优先 Codex。**
- Work 相关行为规则暂不写入执行源；先做 read-only pilot 和 delta verification。

重要平台限制：

- Chat、Work、Codex 是不同体验；
- cloud Work 与 desktop Work 在发布时不是同一 thread/history 空间；
- desktop Work 的本地 files/threads 留在该电脑；
- 跨 surface 续接必须依靠显式 handoff artifact，不能假定自动共享完整上下文。

## 6. New-conversation route options

新对话先做 read-only receive/verification，然后由用户选择一条路线。

### Route A — Post-MNEMOSYNE-113 merge verification and closeout

```yaml
route_id: A
recommended_surface: Chat_GPT_5_6_Sol_Pro
priority: recommended_first
mode: read_only_first_then_low_scope_PR_only_if_needed
```

目标：

- 核实 PR #160 的 master 最终状态；
- 对照 MNEMOSYNE-113 intended repair set 检查 execution source、live status、review manifests、live interpretation 和 retained transfer markers；
- 检查是否有 post-merge residue、路径错误、相互矛盾或遗漏；
- 若全部正确，形成 closeout record；
- 若发现 residue，再创建最小修复 PR。

主要证据：

- `notes/codex-task-results/MNEMOSYNE-113-result.md`
- `current/human-approved-spec.md`
- `current/review-and-validation-status.md`
- `notes/cross-model-review-results/FABLE5-TRIAGE-001/02-gpt-pro-substantive-adjudication-and-repair-decisions.md`
- live warning interpretation file
- PR #160 metadata/diff

### Route B — Ordinary Pro comprehensive Mnemosyne health review

```yaml
route_id: B
recommended_surface: ChatGPT_Work_candidate
fallback_surface: Chat_GPT_5_6_Sol_Pro
mode: read_only_review
```

目标：

- 执行 TODO 中长期待办的 ordinary ChatGPT-Pro Comprehensive Health Review；
- 审查 execution source、current views、handoff consistency、review state、research evidence usage、task/result hygiene 和 backlog priorities；
- 产出 source manifest、findings、severity、recommended repair bundle 和 explicit non-actions；
- 不在 Work 内直接更新 execution source 或仓库；先把结果交回普通维护 Chat 复核。

选择 Work 前应先读 `notes/chatgpt-work-mode-assessment-2026-07.md`，并明确 cloud/web 或 desktop/local surface、连接 apps、read-only 边界和最终 handoff 格式。

### Route C — Resume the paused post-handoff Meta-Agent route

```yaml
route_id: C
recommended_surface: Chat_GPT_5_6_Sol_Pro
mode: explicit_user_selected_route_only
status: paused_not_closed
```

目标：

- 根据官方 MNEMOSYNE-083 package 和 post-084/085 live guards 恢复 Meta-Agent 后续路线；
- 先确认用户要选择哪一条 post-handoff path；
- 不重做 MNEMOSYNE-084/085；
- 不自动创建 workspace、ingest materials、formalize regression、build 或 target write。

主要证据：

- `handoff/meta-agent-post-079-phase-closure-handoff-package.md`
- `handoff/meta-agent-next-conversation-startup-prompt.md`
- `handoff/handoff-current.md`
- `current/active-context.md`
- `current/open-questions.md`

该路线只有在用户明确选择 Route C 后才能成为新对话主线。

### Route D — ChatGPT Work bounded pilot and policy research

```yaml
route_id: D
recommended_surface: ChatGPT_Work
mode: read_only_platform_pilot
execution_source_update: prohibited_in_pilot
```

目标：

- 在 Work 中运行一个受限、read-only 的 Mnemosyne review task；
- 实测 GitHub/plugin access、Plan mode、artifact generation、progress steering、context persistence 和跨 surface handoff；
- 形成 Work behavior observation report；
- 回到普通维护 Chat 决定是否将 surface-selection guidance 提升为 execution-source rule。

Pilot 不允许 repository write、execution-source update、target action、regression formalization 或 paused-route resumption。

### Route E — Maintenance backlog reprioritization

```yaml
route_id: E
recommended_surface: Chat_GPT_5_6_Sol_Pro
mode: planning_and_small_repairs
```

目标：

- 读取 `current/todo.md` 的 live 与 historical sections；
- 结合 post-113 状态，区分真正仍待办、历史陈旧条目、user-review items 和 research-gated items；
- 形成下一阶段 1–3 个高价值任务；
- 不在第一轮自动执行全部 backlog。

## 7. Recommended first action

新对话的安全第一步：

1. receive this handoff；
2. 读取 execution source、receive command、本 package 和 `current/review-and-validation-status.md`；
3. 核实 PR #160 merged；
4. 向用户以 A–E 的形式呈现路线；
5. 等用户选择；
6. 路线选择前不写仓库。

推荐默认顺序：

1. Route A；
2. Route B 或 D；
3. Route C 仅在用户准备恢复 paused route 时；
4. Route E 可替代 B 作为轻量维护路线。

## 8. Forbidden automatic actions

新对话不得自动：

- 接管或继续 `FABLE5-GREENFIELD-001`；
- 恢复或关闭 paused post-handoff route；
- 修改 frozen MNEMOSYNE-082/083 artifacts；
- formalize regression candidates；
- 创建 target workspace；
- ingest target materials；
- write target repository；
- start operational build；
- 将 Work candidate guidance 直接写入 execution source；
- 把本 handoff 当作 execution source。

## 9. Freshness and unknowns

- ChatGPT Work 于 2026-07-09 发布并仍在 rollout；功能、surface synchronization、usage 和 plugin behavior 可能快速变化。
- Work 的 GitHub read/write 行为尚未在 Mnemosyne 上完成受限 pilot。
- 旧对话中 Fable weekly quota 的下一次恢复时间不属于仓库可验证事实。
- 本 package 不保证所有历史 backlog 条目仍然有效；Route E 需要重新核验。

## 10. User transfer instruction

在新对话中提供或授权读取：

- `handoff/mnemosyne-post-113-maintenance-options-handoff-package.md`

并明确说：

- `Receive Mnemosyne handoff.`

推荐直接使用配套 startup prompt：

- `handoff/mnemosyne-post-113-maintenance-next-conversation-startup-prompt.md`
