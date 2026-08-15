# Target-Lifecycle V1 证据保存与清理设计理由 v0.1

> 本文件记录 `MNEMOSYNE-218` 的外显工程理由。它不是执行源，不授权向验证仓库写入，也不授权删除任何证据分支。

```yaml
design_rationale_id: MNE-TARGET-LIFECYCLE-V1-EVIDENCE-PRESERVATION-RATIONALE-001
task_id: MNEMOSYNE-218
status: CANDIDATE_RATIONALE_NOT_OWNER_DECISION
design_ref: notes/evidence-preservation-designs/target-lifecycle-v1-evidence-preservation-and-cleanup-candidate-v0.1.md
validation_ref: notes/validation-designs/target-lifecycle-v1-evidence-preservation-and-cleanup-validation-v0.1.md
manifest_ref: notes/evidence-manifests/MNE-TARGET-LIFECYCLE-V1-BRANCH-EVIDENCE-MANIFEST-CANDIDATE-001.md
owner_source_ref: notes/owner-decision-results/MNE-TARGET-LIFECYCLE-V1-OWNER-ARCHITECTURE-DECISION-001.md
execution_source_modified: false
```

## 1. 要解决的问题

V1 已经完成并获得 Owner 接受，但 16 条 `tlr-v1-*` 分支包含各场景独有的提交历史。Owner 明确要求：在存在可靠保存机制、确认独有证据已经保存、并再次明确授权之前，不得清理这些分支。

当前 controller bundle 已记录每条分支、提交、结果文件和 blob 身份。不过，仅把提交 SHA 写进文档，并不能保证当所有指向该提交的 Git ref 都被删除后，GitHub 会永久保留该对象。

另一方面，验证仓库目前是公开合成仓库，体积约 95 KiB，分支数量也只有 16 条，没有存储紧急性。因此本任务不应为了“看起来整洁”而制造删除压力。

## 2. 固定约束

- 现阶段不删除、不改写、不强制更新任何证据分支；
- 不移动验证仓库 `master`；
- 不把互斥场景内容普通合并到 `master`；
- 不把原始 V1 结果复制进 Mnemosyne 作为替代证据；
- 创建保存机制与执行删除必须是两个独立授权阶段；
- 并发对话造成任何 ref 漂移时必须停止，不得静默刷新输入；
- 当前标准 GitHub 连接器没有 branch-ref 删除动作，未来删除必须换到具备精确删除能力且可审计的独立表面；
- 不触碰 Meta-Agent、真实目标或执行源。

## 3. 备选方案

### 方案 A：永久保留全部 16 条分支

优点：机制最简单、当前已经有效、分支名可直接导航、无需额外写入。

缺点：长期占据分支列表；没有一个紧凑的“路线已封存”锚点；仍依赖所有分支持续存在。

结论：**作为当前默认状态继续采用。**

### 方案 B：每条分支建立一个 tag

优点：原生 Git ref，能够维持提交可达性，语义也较直接。

缺点：仍需 16 个新 ref，几乎没有减少 ref 数量；还要新增 tag 命名与不可变性规则；当前连接器没有已验证的 tag 创建动作。

结论：不作为首选。

### 方案 C：一个多父提交的“可达性锚点”

建立 `tlr-v1-evidence-anchor-001`。锚点提交以 controller head 为第一父提交，其余 15 条证据分支 head 为附加父提交；提交树只在 controller tree 上增加一份自描述 archive manifest。

优点：

- 一个 ref 可以让全部 16 个 head 及其历史保持可达；
- 原分支名与 head 的映射保存在 manifest；
- 不移动 `master`，不改写原证据分支；
- 可以机械验证父提交集合、树差异和所有关键 blob；
- 当前 GitHub 写入表面具备构造 blob、tree、commit、ref 所需的低层动作。

缺点：

- 多父提交不常见，容易被误解成场景语义合并；
- 锚点自身也必须长期保留；
- 单一 GitHub ref 仍不是外部灾难恢复副本；
- 在当前分支负担很低时，立即创建它并无迫切收益。

结论：**作为未来真正要清理分支时的首选保存机制，但现在不执行。**

### 方案 D：外部 `git bundle` 或等价精确归档

优点：可移植、可离线恢复、对 GitHub 平台依赖更低。

缺点：需要具备完整 Git/二进制文件保存能力的表面；还要决定存储位置、权限、保留周期和指针验证；对于当前 95 KiB 的公开合成仓库成本偏高。

结论：作为可选增强层保留，不是当前必需条件。

### 方案 E：只保存文件快照，或普通合并所有场景分支

文件快照会丢失提交图和过程证据；普通合并会把彼此互斥的合成场景错误地表现成一个统一状态，并改变仓库导航语义。

结论：拒绝作为主保存机制。

## 4. 选择

采用分阶段方案：

1. **现在**：继续保留全部 16 条分支，并发布精确分支清单、保存候选与验证设计；
2. **以后有实际清理需求时**：单独授权创建并验证一个可达性锚点；
3. **锚点验证通过以后**：由 Owner 再决定是否删除任何场景分支，并选择具备精确 branch-ref 删除能力的 Codex/Git/人工 GitHub 表面；
4. **任何删除以后**：必须证明原 head、提交历史和关键 blob 仍能通过锚点取得。

决定性理由是：这一方案既不制造当前不必要的操作，又预先冻结了一条可机械验证、不会把“归档成功”误写成“允许删除”的路径。

## 5. 风险与控制

### 风险：把锚点提交误解为场景语义合并

控制：提交信息、manifest 和结果记录必须反复说明其作用只是维持 Git 可达性；验证 `master` 未移动，且不允许从锚点推断统一场景状态。

### 风险：并发对话移动某条证据分支

控制：在分支创建、commit 创建、ref 发布和未来删除前分别重新枚举并比较全部 refs；任何漂移直接停止。

### 风险：锚点建立后过早删除

控制：P1 只允许建立和验证锚点，A12 明确要求删除数量为 0；删除必须使用新的任务号和 Owner 明确列出的分支清单。

### 风险：使用不具备删除能力的连接器，却声称清理完成

控制：P3 启动前必须核验具体表面存在 branch-ref 删除动作；当前标准 GitHub 连接器明确标记为不可执行 P3。文件删除、PR 关闭、移动分支或自然语言声明都不能冒充 ref 删除。

### 风险：只剩一个 GitHub ref，平台级灾难恢复仍不足

控制：不把锚点描述为外部备份；如未来需要平台独立恢复，再单独设计 `git bundle` 或其他精确外部存储。

### 风险：为了低价值整理长期占用强模型或人工操作

控制：当前默认继续保留全部分支；只有真实清理需求出现时才运行 P1。设计和机械执行可分层，避免浪费 Pro 额度。

## 6. 可证伪条件

出现以下任一事实，应重新评估本设计：

- GitHub 或当前连接器无法可靠创建/读取多父提交；
- 当前验证仓库开始承担新活动工作，证据分支不再是冻结历史；
- Owner 要求外部平台独立灾难恢复，而不是仅减少 GitHub 分支数量；
- 实际仓库体积、ref 数量或组织政策使永久保留分支成本显著变化；
- 可达性锚点在测试中不能保证删除后仍可按 SHA 获取所有对象；
- 另一种机制能以更低复杂度同时满足精确历史保存和可恢复性。

## 7. 影响范围

本设计只影响 V1 合成证据的未来保存/清理路径。它不改变：

- candidate v0.2 的架构语义；
- V1 的 Owner 裁决；
- TLR-03、TLR-04 延期；
- 真实目标采用门槛；
- Meta-Agent 或任何目标的真相源；
- `current/human-approved-spec.md`。

## 8. 当前结论

推荐 Owner 接受“保存设计候选已准备，但当前继续保留全部 16 条分支，不运行锚点、不授权删除”的状态。

Deep Research：不需要。独立 Fable 复核：当前不需要。若未来计划在没有外部归档的情况下删除不可替代证据，才建议重新评估是否需要额外异构复核。
