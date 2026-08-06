# Meta-Agent Dedicated Repository Migration Preparation — Startup Prompt

> Use only in the dedicated Meta-Agent construction conversation after the MNEMOSYNE-191 PR containing this file has merged.

```text
@GitHub 请读取并严格执行：

handoff/meta-agent-dedicated-repository-migration-preparation-taskbook.md

执行任务：

META-AGENT-DEDICATED-REPOSITORY-MIGRATION-PREPARATION-001

当前对话唯一主线必须保持为 META_AGENT_PRODUCT_BUILD。

本任务应使用 frontier/Pro 级推理，允许在 08822407d/Mnemosyne 中创建一个任务分支和至多一个 PR，但严格禁止写入、初始化或修改 08822407d/Meta-Agent。

必须从执行时最新 Mnemosyne master 开始，并确认 PR #255 merge commit
9e60fef75c524fc2e8acf227e84eaa820f08bc59
已包含在最新 master 中。

完成：
- receive 结果正式绑定与 PR #255 post-merge closeout；
- 活动 active-context / handoff 的陈旧状态修复；
- target-projects/meta-agent/ 完整递归 Git tree/blob manifest；
- artifact role、authority、material、migration disposition 分类；
- 候选 destination mapping；
- Meta-Agent-owned behavior guidance adoption matrix；
- 初始 memory-system candidate alignment；
- Owner initialization decision package；
- 单一 Mnemosyne PR。

如果无法机械证明完整递归 tree 和每个 blob identity，必须返回：

BLOCKED_INCOMPLETE_REPOSITORY_ENUMERATION

不得以搜索结果、抽样文件或模型记忆伪装完整清单。

不要初始化目标仓库，不要复制文件，不要进行 shadow PR、cutover、prototype、pilot、private material、RAG、MCP、automation 或 activation。

完成后停止，等待 Owner 审查。
```
