# Meta-Agent Mapping Resume — Pro Startup Prompt v0.2

> Use only in the dedicated Meta-Agent construction conversation after the MNEMOSYNE-194 PR containing this version has merged. This prompt consumes the already merged E0 inventory; it does not rerun E0 and does not write the destination repository.

```text
@GitHub 请读取并严格执行：

1. handoff/meta-agent-dedicated-repository-mapping-resume-source-contract-v0.2.yaml
2. handoff/meta-agent-dedicated-repository-mapping-resume-taskbook.md

执行任务：
META-AGENT-DEDICATED-REPOSITORY-MAPPING-RESUME-001

当前对话唯一主线保持为 META_AGENT_PRODUCT_BUILD，并使用 GPT Pro/frontier 级推理。

本轮使用双平面源合同：

A. 迁移 payload 基线：
- repository: 08822407d/Mnemosyne
- commit: 8ef1c43b18b8686a30ffef544ca8b32fce1ca6cb
- root: target-projects/meta-agent/
- root subtree: 4c1cd341777d46b3d6794abc62682e9c915ec46a
- blob count: 226

B. E0 control evidence：
- PR #258
- merge commit: a443940a2ff2425ebb8fc67e084fce5b7b49de58
- target-projects/meta-agent/migration/source-inventory/ 下的 generator 和 manifests
- 对应 Mnemosyne result records

E0 control evidence 默认保留在 Mnemosyne 并使用 immutable pointer；不得因为这些文件物理上位于 bootstrap root 就把它们递归加入 226-blob payload。

开始前必须：

1. 核验最新 Mnemosyne master 已包含 PR #258 和 MNEMOSYNE-194；
2. 核验 PR #259 已关闭未合并、其 branch 不存在，且不使用其内容；
3. 核验 E0 closure 和四项 manifest identity；
4. 比较 8ef1c43b... 到执行时最新 master：
   - target root 内只允许出现 PR #258 的 exact source-inventory control paths；
   - 若出现其他 target-root 变化，返回 BLOCKED_SOURCE_TREE_CHANGED_AFTER_E0；
5. 核验 08822407d/Meta-Agent 仍为空、无 commit/branch/PR；
6. 核验唯一 target truth 仍为 target-projects/meta-agent/current/approved-spec.md 且未启用 operational use。

E0 有效时，严格禁止：
- 重跑完整 recursive git ls-tree；
- 重复工具能力探索；
- 重复 receive-only 测试；
- 把当前整个 target root 当作 E0 payload tree；
- 把 PR #258 inventory outputs 加入 226-blob base payload。

在 08822407d/Mnemosyne 中完成：

- PR #255 post-merge closeout、E0 remote-transfer closeout 与 live navigation 修复；
- 226/226 base blob 的最终 authority / memory / material / migration 语义记录；
- PR #258 control-evidence exclusion ledger；
- E1 自身 added/modified/deleted paths 的 bounded overlay manifest；
- base snapshot + E1 overlay 的 composite migration candidate；
- 两套完整 destination mapping；
- history strategy 比较；
- Meta-Agent-owned behavior guidance candidate、loader candidate 与 adoption matrix；
- 初始 memory-system alignment；
- Owner initialization decision package；
- 一个任务分支和至多一个 PR；
- 不使用 Pro 的 post-merge overlay verification 指令。

严格禁止：

- 写入或初始化 08822407d/Meta-Agent；
- 修改 approved-spec、authority map、accepted methodology、case ledger 或 migration log；
- 自动采用 behavior guidance 或 memory design；
- shadow copy、cutover、private material、prototype、pilot、RAG、MCP、automation 或 activation；
- 导入 PR #259 的内容。

如果 E0 identity 有效，不得因为 PR #258 的 exact control paths 而返回 source-tree-changed blocker。

完成一个 Mnemosyne PR 后停止，等待 Owner 审查。
```
