# FABLE5-GREENFIELD-001 Final-Phase Handoff Package

```yaml
package_id: MNEMOSYNE-FABLE5-GREENFIELD-FINAL-PHASE-HANDOFF-001
created_by_task: MNEMOSYNE-134
package_status: non_execution_source_transfer_artifact
intended_receiver_action: receive_mnemosyne_handoff
repository: 08822407d/Mnemosyne
repository_visibility_at_preparation: public
prepared_at: 2026-07-17
current_execution_source: current/human-approved-spec.md
source_conversation_status_after_merge: historical_frozen_no_longer_primary_receiver
receiving_conversation_role: FABLE5_GREENFIELD_final_phase_result_receiver_and_storage_finisher
recommended_surface: ordinary_ChatGPT_chat
ChatGPT_Work_required: false
substantive_Pro_adjudication_in_scope: false
```

## 1. Purpose

当前长对话已经非常庞大，并发生过上下文压缩后仓库状态误判。为降低 GF-STEP-4、GF-STEP-5 和最终收尾发生路径偏差的风险，本包把 `FABLE5-GREENFIELD-001` 的**最终阶段结果接收、精确保存和状态同步职责**交给一段全新的普通 ChatGPT 对话。

本包不转移 Mnemosyne 的其他维护主线，不恢复 paused post-handoff route，也不授权接收方读取现有 GPT/Mnemosyne 设计。

## 2. Execution source and authority boundary

- `current/human-approved-spec.md` 是 Mnemosyne 唯一执行源。
- 本 handoff、Fable 输出、manifest、result record、current status 和 review records 都不是执行源。
- 当前接收方在 Thinking 模型上下文中只负责：
  - 核验文件身份和结构；
  - 原文保存；
  - 必要索引与状态同步；
  - 创建一个 ready PR；
  - 给出下一步 Fable 工作入口。
- 不得在 Thinking 上：
  - 实质接纳、否决或修补 Fable 设计；
  - 修改 `current/human-approved-spec.md`；
  - 依据 Fable 结果完善 Mnemosyne；
  - 开始现有设计比较。
- GPT Pro 的实质裁决和 Mnemosyne 改进属于以后单独的高判断工作流。

## 3. Receiver guidance load

```yaml
receiver_guidance_load:
  project_guidance: not_applicable
  mnemosyne_guidance: required
  ordered_operations:
    - receive_authorized_handoff_package
    - output_the_required_handoff_receive_report_and_stop
    - user_sends_Load_Mnemosyne_guidance_as_a_separate_message
    - execute_Load_Mnemosyne_guidance_as_separate_operation
    - confirm_received_task_preserved
    - continue_received_task_under_refreshed_constraints
```

接收交接与加载约束必须是两个不同操作。接收方不得因为加载 guidance 而用无关的 maintenance live route 替换本包任务。

## 4. Verified repository state at preparation

```yaml
default_branch: master
verified_master_sha: 984eb7697b17fd953c6145d5596755f00159d4b3
latest_merged_storage_PR:
  number: 184
  task_id: MNEMOSYNE-133
  title: MNEMOSYNE-133 preserve Fable GF-STEP-3B result
  merged: true
  merge_commit: 984eb7697b17fd953c6145d5596755f00159d4b3
repository_visibility: public
```

PR #184 已保存 GF-STEP-3B。PR #183 只保存 GF-STEP-3A；其历史 metadata 已修正，不得再声称 STEP3B 包含在 PR #183 中。

## 5. Fable greenfield current phase

```yaml
track_id: FABLE5-GREENFIELD-001
GF_STEP_1:
  Fable_status: complete_with_explicit_open_questions
  substantive_maintainer_acceptance: not_performed
GF_STEP_2:
  Fable_status: complete_with_dated_fact_and_text_only_visual_caveats
  substantive_maintainer_acceptance: not_performed
GF_STEP_3:
  Fable_status: complete_with_explicit_parameter_and_amendment_gates
  advisory_components:
    - GF-STEP-3A
    - GF-STEP-3B
  substantive_maintainer_acceptance: not_performed
  premature_candidate:
    status: preserved_unaccepted
    used_by_canonical_3A_or_3B: false
GF_STEP_4:
  task_prepared: true
  executed: false
GF_STEP_5:
  started: false
comparison_firewall:
  existing_GPT_design_read_authorized: false
```

## 6. Completed work relevant to this handoff

- GF-STEP-1A through 1E：需求模型重建；
- GF-STEP-2A through 2D：能力边界证据和核验；
- GF-STEP-3A：信息架构与权限模型；
- GF-STEP-3B：生命周期与操作架构；
- INC-003：STEP2D 被误解为 STEP3 的事件已通过 fresh-conversation 重跑解决；
- GF-STEP-3-EARLY：保留但未接受，canonical 3A/3B 未使用它；
- PR #184 / MNEMOSYNE-133 已合并。

## 7. Immediate transferred task

接收方的第一项实际工作不是重新分析历史，而是：

1. 完成交接接收和 guidance refresh；
2. 确认 GF-STEP-4 尚未执行；
3. 等待用户提供 Fable 的 GF-STEP-4：
   - 聊天摘要；
   - 可下载 Markdown 文件；
4. 在 Thinking 模型上下文中仅执行 storage-only 处理；
5. 使用当前 `master` 新任务号和单活跃 PR 谱系创建 ready PR；
6. 合并前只向用户给出一个 merge target；
7. 保存后根据 Fable 自己声明的 continuation，仅区分：
   - `GF-STEP-3R` repair gate；或
   - ready to request user authorization for `GF-STEP-5`；
8. 不自行打开 comparison firewall。

## 8. GF-STEP-4 prepared execution kit

Canonical prepared task copy after this handoff PR merges:

- `handoff/fable5-greenfield-final-phase-step4-task.md`
- `handoff/fable5-greenfield-final-phase-step4-input-manifest.json`

Local/downloadable identities:

```yaml
GF_STEP_4_task:
  filename: FABLE5-GREENFIELD-001-GF-STEP-4-task.md
  size_bytes: 27489
  sha256: a0afeb6f13e62346f789be05e958b1365e8a90ced0e94379d34ab6230facd973
GF_STEP_4_input_package:
  filename: FABLE5-GREENFIELD-001-GF-STEP-4-complete-input-package.zip
  size_bytes: 85839
  sha256: ced674a2da30035176dfc5a9f2760dbe95c234dadb9ef9d0b7464e4d59730726
```

The task uses exactly:

- STEP1E: 32,577 bytes, SHA-256 `60fd4ca8aba48236b947d3852f0666a2eb93c1c624e0833ba6e520b91eb7a3b0`;
- STEP2D: 68,834 bytes, SHA-256 `ebb994bd3d8f4998cbdc7aead17dcc609958a53798f6c8e9d6dd03d8de5893ac`;
- STEP3A: 47,324 bytes, SHA-256 `3d82a3728ee7ff628be8495469e3e7039a273e28ad9262af4dea88351d8896b1`;
- STEP3B: 68,033 bytes, SHA-256 `af4dd4c2d9658319462a28cc13c469f24823be06cc003f33858b348a68fb6685`.

The earlier incorrect STEP3B identity (`66,747` bytes / `403515…`) is superseded and must not be reused.

## 9. Evidence paths

Minimum paths for receive verification:

- `README.md`
- `current/human-approved-spec.md`
- `commands/receive-mnemosyne-handoff.md`
- `commands/load-mnemosyne-guidance.md`
- `current/artifact-delivery-and-direct-generation-guard.md`
- `current/github-single-active-pr-lineage-guard.md`
- `current/fable-greenfield-execution-deviation-status.md`
- `notes/cross-model-review-results/FABLE5-GREENFIELD-001/00-task-charter.md`
- `notes/cross-model-review-results/FABLE5-GREENFIELD-001/steps/GF-STEP-3A/manifest.yaml`
- `notes/cross-model-review-results/FABLE5-GREENFIELD-001/steps/GF-STEP-3B/manifest.yaml`
- `notes/codex-task-results/MNEMOSYNE-133-result.md`
- PR #184 metadata

Task-local files:

- `handoff/fable5-greenfield-final-phase-step4-task.md`
- `handoff/fable5-greenfield-final-phase-step4-input-manifest.json`

## 10. Repository-write authority carried into the new conversation

When the user invokes the paired startup prompt, that new user message authorizes the receiving conversation to:

- preserve forthcoming Fable greenfield result files in this repository;
- create/update the necessary manifest, result record, current wayfinding and index files;
- create one ready PR without re-asking;
- use a new task ID resolved from current `master`.

It does not authorize:

- merge or auto-merge;
- direct default-branch writes;
- execution-source changes;
- target project actions;
- comparison against current GPT design;
- substantive Fable conclusion acceptance;
- parallel PRs;
- task-number reuse.

The receiver must apply `current/github-single-active-pr-lineage-guard.md`.

## 11. Forbidden actions

The receiving conversation must not automatically:

- read or compare the current GPT/Mnemosyne design;
- execute or generate GF-STEP-5 without explicit user authorization;
- modify `current/human-approved-spec.md`;
- accept the early GF-STEP-3 candidate;
- treat Fable outputs as execution source;
- run Pro-level adjudication while operating under Thinking;
- improve Mnemosyne based on STEP1–4;
- resume or close the paused post-handoff Meta-Agent route;
- create target workspace or ingest target material;
- formalize regression;
- start build or target write;
- merge PRs or enable auto-merge.

## 12. Safe next action

```yaml
safe_next_action:
  actor: user_then_receiving_conversation
  sequence:
    - merge_the_handoff_PR
    - open_a_new_ordinary_ChatGPT_conversation
    - send_the_paired_startup_prompt
    - wait_for_receive_report
    - send_Load_Mnemosyne_guidance_as_a_second_message
    - wait_for_guidance_refresh_confirmation
    - execute_GF_STEP_4_in_a_fresh_Fable_5_conversation_or_bring_existing_result
    - provide_STEP4_summary_and_downloadable_file_to_the_new_ChatGPT_conversation
```

## 13. Freshness, unknowns, and non-assumptions

- The model/tier used by the future receiving conversation is unknown until the user states or the product exposes it.
- Fable quota state is not repository-verifiable.
- GF-STEP-4 has not yet been executed at package preparation.
- GF-STEP-4 may produce either a repair gate, a user-decision gate, or readiness for STEP5.
- STEP5 is a large comparison phase and requires a separate explicit user authorization because it opens the existing-design read firewall.
- The exact next Mnemosyne task ID must be resolved fresh from current `master`; do not assume it from this package.
- Repository visibility is public; no private user material, secrets, credentials, or sensitive originals may be placed into this repository.

## 14. Handoff completion condition

This handoff is complete when:

1. the new conversation reports successful package receipt;
2. the user separately invokes `加载 MNEMOSYNE 约束指导`;
3. the receiver confirms the transferred local task is preserved;
4. the receiver states the one safe next action: await/receive GF-STEP-4.

After those conditions, this old conversation is historical only and should not receive further Fable results.
