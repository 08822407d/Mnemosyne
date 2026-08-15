# Target-Lifecycle V1 证据保存路线 — Owner 决策候选 001

> 本文件把 `MNEMOSYNE-218` 的设计结果整理成可由 Owner 直接选择的决定。它不是 Owner 决定，不授权向验证仓库写入，也不授权删除任何分支。

```yaml
decision_candidate_id: MNE-TARGET-LIFECYCLE-V1-EVIDENCE-PRESERVATION-DISPOSITION-CANDIDATE-001
task_id: MNEMOSYNE-218
status: READY_FOR_OWNER_DECISION
source_candidate: notes/evidence-preservation-designs/target-lifecycle-v1-evidence-preservation-and-cleanup-candidate-v0.1.md
source_validation: notes/validation-designs/target-lifecycle-v1-evidence-preservation-and-cleanup-validation-v0.1.md
source_manifest: notes/evidence-manifests/MNE-TARGET-LIFECYCLE-V1-BRANCH-EVIDENCE-MANIFEST-CANDIDATE-001.md
source_rationale: notes/design-rationales/target-lifecycle-v1-evidence-preservation-and-cleanup-v0.1.md
validation_repository: 08822407d/mnemosyne-target-lifecycle-validation-002
current_retained_branch_count: 16
current_cleanup_authorized: false
```

## 1. 需要决定什么

V1 的 16 条证据分支目前都保留完好。仓库体积很小，也没有清理紧迫性；但 Owner 早先已要求，未来若清理，必须先建立并验证可靠保存机制。

本次决定只回答：

> 是否接受现在准备好的保存/清理设计，以及是否现在就进入“只建立锚点、不删除分支”的下一阶段。

它不决定任何真实目标采用，也不重新裁决 V1。

## 2. 已经确认的事实

- 验证仓库当前为 public；
- 默认分支仍是 `master@e8e3296922185b4b70997c2351d6f39423f2cd4f`；
- controller 仍是 `tlr-v1-controller@e892749fc9e242b24908f89b6a78f1c0f0bed75e`；
- controller bundle blob 仍是 `8a5f3644707ae518182ed352174e58d1ca419067`；
- 16 条 `tlr-v1-*` 分支的当前 head 已与 controller evidence 相互核对；
- 仅保存 SHA 的文档不能单独保证删除全部 ref 后对象仍永久可达；
- 当前仓库约 95 KiB，没有存储紧急性；
- 本次任务没有写验证仓库，也没有删除任何分支。

## 3. 选项

### A — 接受保存设计，但当前继续保留全部分支（推荐）

决定内容：

- 接受精确 manifest、分阶段保存/清理候选和验证设计，作为未来清理的准备方案；
- 当前不创建 `tlr-v1-evidence-anchor-001`；
- 当前不删除任何分支；
- 只有出现真实清理需求或 Owner 以后明确选择 P1，才启动锚点创建与验证；
- 锚点通过后仍必须再次由 Owner 决定是否删除哪些分支。

优点：不制造当前不必要的 Git 操作，同时使未来路线不再从零设计。

代价：16 条分支继续保留，分支列表暂时不变。

### B — 接受设计，并在设计文件合并后另行授权 P1 锚点阶段

决定内容：

- 接受本次设计；
- 下一阶段准备一份精确 P1 运行授权；
- 只创建并验证 `tlr-v1-evidence-anchor-001`；
- P1 中删除数量必须为 0；
- P1 结束后返回 Owner，再决定是否清理。

优点：提前建立可达性保存机制，未来清理时更快。

代价：当前没有实际清理压力，却要增加一个非常规多父提交和一个长期 anchor ref；还需要一次独立写入运行与复核。

### C — 只保留现状，不接受本设计为未来路线

决定内容：

- 继续永久或无限期保留全部 16 条分支；
- 本次 manifest 可作为只读观察记录，但 anchor/cleanup 候选不作为以后默认设计；
- 若未来要清理，重新设计。

优点：最简单，没有新机制。

代价：未来仍需重新解决“删除 ref 后如何保证完整历史可达”的问题。

### D — 在任何 GitHub 内部锚点之前，先设计外部精确归档

决定内容：

- 暂不采用单一 anchor 作为主要保存机制；
- 先设计 `git bundle` 或其他平台外精确归档、存储位置、权限、哈希和恢复测试；
- 外部归档通过后再讨论分支清理。

优点：提供更强的平台独立恢复能力。

代价：当前公开合成仓库很小，这一方案成本明显更高，也需要新的存储与权限决定。

### E — 其他 / 拒绝问题前提 / 自由修改

Owner 可以：

- 指定另一种保存机制；
- 改变拟保留或拟删除的分支集合；
- 要求补充证据；
- 暂缓；
- 拒绝“需要清理分支”这一前提。

## 4. 推荐

推荐 **A**。

理由：当前没有存储、性能或导航方面的真实紧急问题；保留全部分支已经满足安全要求。现在最有价值的工作是把精确身份和未来可验证路线固定下来，而不是为了完成流程而立即制造锚点和后续清理任务。

## 5. 各选项都不授权的事项

无论选择哪一项，本决定都不会自动授权：

- 删除或改写任何验证分支；
- 移动验证仓库 `master`；
- 运行 runtime supplement、S10、V2 或新验证；
- 将 raw V1 结果写入 Mnemosyne；
- 真实目标采用、迁移或激活；
- 修改 Meta-Agent、真实目标或 `current/human-approved-spec.md`；
- Work、Deep Research、Fable、Scheduled Task 或外部 quota。

选择 B 也只表示下一步可以准备 P1 的精确授权，不等于本文件本身已经授权写验证仓库。

## 6. 简洁确认格式

接受推荐项时，可确认：

```text
确认 MNE-TARGET-LIFECYCLE-V1-EVIDENCE-PRESERVATION-DISPOSITION-CANDIDATE-001，选择 A。
接受保存设计候选，但当前继续保留全部 16 条证据分支；不创建锚点，不授权清理。
```

也可直接说明选择 B、C、D，或自由修改。
