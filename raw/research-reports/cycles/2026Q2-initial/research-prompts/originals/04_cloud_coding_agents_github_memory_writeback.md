# 轻度研究子课题 4：云端 Coding Agent 与 GitHub 工作流下的记忆写回和审计

## 研究目标

请研究：云端 coding agent、GitHub Actions、PR 工作流、CODEOWNERS、branch protection 等是否适合实现“外部持久记忆系统”的写回、审计、版本控制和人工批准。

## 背景

我的外部持久记忆系统希望将长期记忆保存到 GitHub 仓库或类似版本化存储中。对于本地 agent，可以直接修改文件；但对于云端 agent，必须考虑权限、分支隔离、PR、审计日志、失败恢复和敏感数据隔离。

本研究不要求设计完整实施方案，只验证这些机制是否现实可行。

## 核心问题

1. GitHub Copilot coding agent / cloud agent 是否能在云端读取仓库、修改文件、运行测试、提交 PR？
2. 云端 agent 是否适合修改记忆文件，例如 memory-ledger、handoff-current、project-state？
3. 记忆和代码同仓是否比独立记忆仓库更容易被云端 agent 访问？
4. 如果记忆仓库独立，云端 agent 如何授权读取和写入？
5. 写回长期记忆是否应强制走 PR？
6. GitHub Actions 是否可以作为记忆写回自动化工具？
7. CODEOWNERS、branch protection、PR review 是否能用于保护记忆文件？
8. 云端任务失败时，是否能保存 checkpoint、日志、handoff 或 artifact？
9. 哪些敏感记忆不应暴露给云端 agent？
10. GitHub 工作流是否能作为“记忆更新审计链”？

## 请优先查找的资料

- GitHub Copilot coding agent / cloud agent 官方文档；
- GitHub Actions 官方文档；
- GitHub Pull Request workflow；
- CODEOWNERS；
- branch protection；
- GitHub security scanning / secret scanning；
- Claude Code GitHub Actions 或相关云端执行资料；
- Codex cloud / remote execution 相关官方资料；
- MCP 和云端 agent 权限安全资料。

## 输出要求

请输出：

1. 总体结论：云端 agent + GitHub 工作流是否适合做记忆写回和审计。
2. 云端 agent 能做什么：
   - 读仓库；
   - 改文件；
   - 跑测试；
   - 提 PR；
   - 留日志。
3. 哪些记忆文件适合云端 agent 写回。
4. 哪些记忆文件不适合云端 agent 访问。
5. 同仓记忆 vs 独立记忆仓库的优缺点。
6. PR / CODEOWNERS / branch protection 如何支持人工审批。
7. GitHub Actions 在自动化评估、格式检查、归档、写回中的作用。
8. 当前无法确认或不建议自动化的环节。

## 注意事项

请重点依据官方文档和真实工作流。不要假定云端 agent 有无限权限。若写回外部仓库需要复杂授权，请明确说明。
