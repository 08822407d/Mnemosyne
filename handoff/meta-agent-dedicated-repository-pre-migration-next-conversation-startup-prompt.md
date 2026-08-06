# Meta-Agent Dedicated-Repository Pre-Migration — Startup Prompt

@GitHub 请读取并严格执行：

```text
handoff/meta-agent-dedicated-repository-pre-migration-test-package.md
```

第一轮只做 receive-only pre-migration test intake：

1. 核验 `08822407d/Mnemosyne` 最新 `master`，并确认 PR #253 已合并；
2. 核验新的 `08822407d/Meta-Agent` 仓库是否可访问、是否仍为空、是否无 branch/commit/open PR；
3. 按 handoff 的 required reading order 读取 Mnemosyne 迁移设计、验证设计、Meta-Agent target truth、authority、active context、compatibility guard、history 和 handoff；
4. 明确区分：
   - connector/platform permission；
   - 当前任务授权；
   - shadow copy；
   - target-truth cutover；
5. 返回 handoff 中规定的 `pre_migration_test_receive`；
6. 不创建或修改任何仓库、branch、file、issue、comment、label 或 PR；
7. 不初始化 `08822407d/Meta-Agent`，不复制文件，不修改 target truth，不开始 prototype/pilot/private material/RAG/MCP/automation/activation；
8. 返回 receive report 后停止，等待我的下一条命令。

本提示只用于 Meta-Agent 专用建设对话。它不会把当前 Mnemosyne maintenance 路线变成 Meta-Agent 产品路线。
