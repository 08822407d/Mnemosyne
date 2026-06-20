# 轻度研究子课题 3：Codex / Claude Code / Cursor 等本地开发 Agent 的文件式记忆能力

## 研究目标

请研究：Codex、Claude Code、Cursor、本地 IDE agent、CLI agent 等开发型 AI 工具，是否更适合实现“外部持久记忆系统”。重点验证它们是否能稳定读取、维护和更新仓库内的规则文件、项目状态、handoff 和 memory-ledger。

## 背景

相比 ChatGPT 网页端这类纯对话入口，本地 coding agent 通常可以直接访问项目文件系统、Git 仓库、测试命令和终端工具。因此它们可能更适合将长期记忆文件化、版本化、可审计化。

我希望查清：本地开发 Agent 能否把 AGENTS.md、CLAUDE.md、project-state.md、tasks/、ADR、memory-ledger、handoff-current 等当作长期记忆系统的一部分。

## 核心问题

1. Codex 是否支持 AGENTS.md、repo instructions 或类似仓库规则文件？
2. Codex 是否能读取和遵守仓库内规则文件？
3. Codex 是否能修改仓库内 memory files，并通过 diff、patch、commit 或 PR 呈现？
4. Claude Code 是否支持 CLAUDE.md、sessions、memory、hooks、permissions？
5. Claude Code 是否能读取、更新或维护 memory-ledger 一类文件？
6. Claude Code 的 sessions / resume / memory 能否用于跨任务接续？
7. Cursor Rules、project rules、agent 是否支持类似文件式规则和记忆？
8. 本地 agent 是否适合把 Git 作为记忆版本管理系统？
9. 如何避免 agent 误改长期记忆？
10. 是否应要求 agent 只生成 memory update patch，由用户 review 后再写入？

## 请优先查找的资料

- OpenAI / Codex 关于 AGENTS.md、repo instructions、coding workflow 的官方文档；
- Anthropic Claude Code 官方文档，尤其 CLAUDE.md、sessions、memory、hooks、permissions、subagents；
- Cursor Rules、Agent、project rules、cloud agent 官方文档；
- Git 与 coding agent 结合的官方或高质量案例；
- 开发者实际使用案例或官方最佳实践。

## 输出要求

请输出：

1. 总体结论：本地 coding agent 是否是外部持久记忆系统的最佳落地点之一。
2. Codex 能力边界：
   - 规则读取；
   - 文件修改；
   - diff / patch / commit；
   - 适合维护哪些记忆文件。
3. Claude Code 能力边界：
   - CLAUDE.md；
   - sessions；
   - memory；
   - hooks / permissions；
   - 文件更新和安全边界。
4. Cursor 能力边界。
5. 本地 coding agent 相比纯对话工具的优势。
6. 本地 coding agent 的风险：
   - 误改文件；
   - 规则冲突；
   - 本地记忆不跨设备；
   - 权限过大。
7. 推荐的高可信实践：
   - Git 管理记忆；
   - patch / diff 审查；
   - memory update 人工确认；
   - 受保护目录；
   - 规则文件版本化。

## 注意事项

不要设计完整系统。重点是验证工具能力和真实案例。若某项能力只有推测，没有官方文档或可靠案例，请明确标为不确定。
