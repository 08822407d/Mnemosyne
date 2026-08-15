# Target-Lifecycle V1 证据保存路线 — Owner 决定 001

> 本文件记录 Owner 对 `MNE-TARGET-LIFECYCLE-V1-EVIDENCE-PRESERVATION-DISPOSITION-CANDIDATE-001` 的正式选择。它接受证据保存与未来清理设计候选，但当前继续保留全部 V1 证据分支；不创建锚点，不授权任何清理。

```yaml
decision_id: MNE-TARGET-LIFECYCLE-V1-EVIDENCE-PRESERVATION-OWNER-DECISION-001
task_id: MNEMOSYNE-218
decision_status: OWNER_CONFIRMED_OPTION_A
source_branch: mnemosyne-218-v1-evidence-preservation-design
confirmed_source_head: bc2f6850bad8e83a7cba13cd6fac92ea30b1c3a3
source_decision_candidate: notes/owner-decision-candidates/MNE-TARGET-LIFECYCLE-V1-EVIDENCE-PRESERVATION-DISPOSITION-CANDIDATE-001.md
confirmed_decision_candidate_blob: f34d0b74da4d6285356c7e7466a0a676cb62a573
selected_option: A
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
accepted_design_candidate: true
retain_all_16_tlr_v1_branches: true
create_anchor_now: false
cleanup_authorized: false
validation_repository_write_authorized: false
execution_source_modified: false
Meta_Agent_or_real_target_modified: false
```

## 1. Owner 决定

Owner 明确确认：

- 接受本次 V1 证据保存与未来清理设计候选；
- 当前继续保留全部 16 条 `tlr-v1-*` 证据分支；
- 当前不创建 `tlr-v1-evidence-anchor-001`；
- 当前不授权删除、移动、改写或 force-update 任何验证分支；
- 当前不授权向验证仓库写入任何 archive/anchor/result；
- 只有以后出现真实清理需求，或 Owner 另行明确选择 P1 时，才重新评估并授权锚点创建与验证；
- 即使未来 P1 锚点验证通过，也不能推导出 P3 清理授权，删除仍需新的 Owner 决定和精确分支清单。

## 2. 接受的设计含义

Owner 接受的是一条**未来可用的保存/清理设计路线**，不是立即执行计划。

当前默认状态保持最简单、最安全的做法：所有 16 条 V1 evidence branches 原样保留。设计候选中的 reachability-anchor 机制仅作为以后真正需要减少 branch refs 时的首选候选；它尚未执行，也没有获得验证结果。

接受设计不改变已经完成的 Target-Lifecycle V1 架构裁决，也不重新打开 V1、S8、S11、S10 或 V2。

## 3. 当前仍保留的证据集合

精确 branch/head 映射以：

```text
notes/evidence-manifests/MNE-TARGET-LIFECYCLE-V1-BRANCH-EVIDENCE-MANIFEST-CANDIDATE-001.md
```

为本次设计的观察基线。

当前保留义务仍覆盖全部 16 条 `tlr-v1-*` refs。任何未来 cleanup task 都必须在执行时重新枚举并验证 live refs，不得仅凭本决定中的历史快照删除。

## 4. 未来 P1 门槛

如果以后 Owner 明确选择 P1，则必须使用新的精确授权，并至少重新绑定：

- 执行时最新 Mnemosyne 相关设计/授权身份；
- 验证仓库当前 public/material boundary；
- validation `master`；
- 全部 16 条原始 evidence branch 的名称与 exact head；
- controller bundle 和 branch/output identity blobs；
- `tlr-v1-evidence-anchor-001` 必须在 P0A 时不存在；
- concurrent write / active related lineage 必须不存在。

P1 只能创建并验证 reachability anchor，删除数量必须为 0。

## 5. 未来 P3 门槛

P3 不被本决定授权。

如果未来确需 cleanup：

1. P1 必须已通过；
2. Owner 必须重新做 cleanup 决定；
3. 必须冻结 exact deletion list；
4. 必须使用具备真实 branch-ref 删除能力的表面；
5. 删除后必须执行 reachability/recovery proof；
6. 任一 partial failure、ref drift 或 identity mismatch 都必须停止并保留证据。

当前标准 GitHub 连接器没有 branch-ref 删除动作，因此不得用删除文件、关闭 PR、移动分支或自然语言声明替代真实 ref 删除。

## 6. 明确未授权事项

本决定不授权：

- P1 锚点阶段；
- P3 清理；
- 删除、移动、改写或 force-update 任一 V1 evidence branch；
- validation `master` 变化；
- runtime supplement、S10、V2 或新 validation；
- raw V1 result ingestion into Mnemosyne；
- Work、Deep Research、Fable、Scheduled Task 或其他外部 quota；
- Meta-Agent、真实目标或 `current/human-approved-spec.md` 修改；
- target adoption、migration 或 activation；
- auto-merge。

## 7. Publication authority

Owner 同时授权：

- 在同一 `mnemosyne-218-v1-evidence-preservation-design` lineage 保存本决定；
- 在完成最终 semantic/mechanical preflight 后，从该分支创建一个 Ready PR 到 `master`；
- `draft: false`；
- 不启用 auto-merge；
- 不由 Agent 自动合并。

Owner merge remains the publication/acceptance gate and does not imply comprehensive line-by-line human review.

## 8. Decision provenance

本决定由 Owner 在当前 GitHub-enabled Mnemosyne conversation 中直接给出，并显式绑定：

```text
branch: mnemosyne-218-v1-evidence-preservation-design
head: bc2f6850bad8e83a7cba13cd6fac92ea30b1c3a3
decision candidate blob: f34d0b74da4d6285356c7e7466a0a676cb62a573
```

后续用于发布本决定而新增的 task-local commits 不改变上述被 Owner 审定的候选内容身份。
