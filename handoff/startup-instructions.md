# Startup Instructions / 启动说明

## 1. 文件定位

- 本文件用于新 ChatGPT 对话、新 Codex Cloud 任务或未来其他 Agent 接手 Mnemosyne。
- 本文件不是执行源。
- 当前执行源是 `current/human-approved-spec.md`。
- 如果本文件与 `human-approved-spec` 冲突，应以 `human-approved-spec` 为准，并登记 open question。

## 2. 启动前提

新任务必须假设：

- 旧对话上下文可能不可用；
- 旧 Codex 任务上下文不可用；
- GitHub 仓库文件是外部持久状态源；
- 不应依赖模型内部 memory；
- 不应默认读取全部 raw；
- 不应默认自动写回。

## 3. 标准读取顺序

1. `README.md`
2. `current/human-approved-spec.md`
3. `current/active-context.md`
4. `handoff/handoff-current.md`
5. `current/open-questions.md`
6. `current/todo.md`
7. `notes/codex-task-authoring-and-diff-verification-guidelines.md`
8. `notes/v0.1-scope-and-consistency-check.md`
9. `raw/research-reports/current/research-report-index.md`
10. `raw/research-reports/current/current-evidence-map.md`
11. `raw/research-reports/current/current-capability-boundaries.md`
12. `notes/core-object-model.md`
13. `notes/requirement-intake-workflow.md`
14. `notes/delivery-package-workflow.md`
15. `raw/concept-origin-extract-001.md` 按需回查

## 4. 执行源与非执行源

执行源：

- `current/human-approved-spec.md`

非执行源：

- `raw/`
- `raw/research-reports/`
- `notes/candidate-requirements.md`
- `notes/decision-log.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `handoff/startup-instructions.md`

说明：

- raw 和 research reports 是证据层；
- candidate 是候选需求；
- decision-log 是决策理由记录；
- active-context 是当前工作集；
- handoff 是交接卡；
- startup-instructions 是启动说明；
- 如果发生冲突，以 `current/human-approved-spec.md` 为准。

## 5. 研究证据读取规则

在以下任务前，必须读取研究证据 current 视图：

- 判断 ChatGPT / Claude / Codex / Claude Code / Cursor / GitHub / MCP / RAG 等工具能力边界；
- 设计新机制；
- 做平台适配；
- 设计目标项目记忆系统；
- 判断某项自动化是否现实可行；
- 修改 v0.1 / v0.2 能力承诺。

必须读取：

- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`

说明：

- 研究报告是高权重证据层，不是执行源；
- PDF 图表和图片仍需人工复核；
- 研究证据具有时效性，未来通过新 research cycle 和 delta report 更新。

## 5.1 Codex / ChatGPT task verification reminder

MNEMOSYNE-031 showed that natural-language Codex task descriptions may fail to produce all intended file edits. For future repository-editing tasks, read:

- `notes/codex-task-authoring-and-diff-verification-guidelines.md`

When generating or executing Codex tasks that modify files, require actual diff evidence: `git status --short`, `git diff HEAD --stat`, `git diff HEAD --name-only`, targeted `git diff HEAD -- <target files>`, protected-file checks, and task result records comparing intended files with actual changed files.

Detailed Codex task authoring and diff verification rule:

For any Codex task that modifies repository files:

- require exact target files;
- require protected-file list;
- prefer exact replacement blocks or a patch script for multi-file / high-risk / stale-text cleanup tasks;
- require `git status --short`;
- require `git diff HEAD --stat`;
- require `git diff HEAD --name-only`;
- require targeted `git diff HEAD -- <target files>` for important files;
- require grep/rg checks for expected additions/removals when applicable;
- require a task result record comparing intended files with actual changed files;
- do not accept Codex prose completion as sufficient evidence.

Detailed guideline:

- `notes/codex-task-authoring-and-diff-verification-guidelines.md`

## 6. 新 ChatGPT 对话启动提示

```text
你正在接手 GitHub 仓库 Mnemosyne。

这是一个“记忆系统元 Agent”工作仓库，用于设计、演化和交付 AI Agent 外部持久记忆系统。

请不要依赖旧对话上下文，只根据仓库文件接手。

请按以下顺序读取或要求用户提供以下文件内容：

1. README.md
2. current/human-approved-spec.md
3. current/active-context.md
4. handoff/handoff-current.md
5. current/open-questions.md
6. current/todo.md
7. notes/codex-task-authoring-and-diff-verification-guidelines.md
8. notes/v0.1-scope-and-consistency-check.md
9. raw/research-reports/current/research-report-index.md
10. raw/research-reports/current/current-evidence-map.md
11. raw/research-reports/current/current-capability-boundaries.md

接手后请先输出：
- 你理解的当前阶段；
- 当前执行源是什么；
- 哪些文件不是执行源；
- 当前已完成内容；
- 当前未完成内容；
- 下一步最合适的工作；
- 是否发现文件之间存在冲突。

注意：
current/human-approved-spec.md 是执行源。
raw、research reports、candidate、decision-log、active-context、handoff、startup-instructions 都不是执行源。
```

## 7. 新 Codex Cloud 任务启动提示

```text
你正在继续维护 GitHub 仓库 “Mnemosyne”。

这是一个新的 Codex Cloud 任务。不要依赖旧 Codex 任务上下文，只根据仓库文件接手。

请先读取：

- README.md
- current/human-approved-spec.md
- current/active-context.md
- handoff/handoff-current.md
- current/open-questions.md
- current/todo.md
- notes/codex-task-authoring-and-diff-verification-guidelines.md
- notes/v0.1-scope-and-consistency-check.md
- raw/research-reports/current/research-report-index.md
- raw/research-reports/current/current-evidence-map.md
- raw/research-reports/current/current-capability-boundaries.md
- notes/core-object-model.md
- notes/requirement-intake-workflow.md
- notes/delivery-package-workflow.md

接手规则：

- current/human-approved-spec.md 是执行源；
- raw 和 research reports 是证据层，不是执行源；
- candidate-requirements 是候选需求，不是执行源；
- decision-log 是决策理由记录，不是执行源；
- active-context 是当前工作集，不是执行源；
- handoff-current 是交接卡，不是执行源；
- startup-instructions 是启动说明，不是执行源；
- 如果文件之间冲突，以 human-approved-spec 为准，并登记 open question。

当前不要做：

- 不要创建 AGENTS.md；
- 不要创建 CLAUDE.md；
- 不要创建 GitHub Actions；
- 不要添加自动化脚本；
- 不要修改研究报告原件；
- 不要实现自动查重、自动索引、自动写回、MCP、RAG 或多 Agent 自动协调，除非用户明确要求进入对应阶段。

请先输出：
- 当前仓库状态摘要；
- 当前执行源；
- 当前未完成任务；
- 你建议的下一步；
- 本次计划修改哪些文件。
- 如果本次会修改文件，说明将如何用 `git status --short`、`git diff HEAD --stat`、`git diff HEAD --name-only` 和目标文件 diff 验证实际修改。
```

## 8. 常见任务入口

### A. 继续完善 Mnemosyne 自身

流程：

- 新构想或反馈先进入 raw；
- 抽取 candidate；
- 必要时查重和对比；
- 用户确认后才更新 human-approved-spec；
- 更新 active-context / handoff / todo。

### B. 为目标项目设计记忆系统

流程：

- 读取 human-approved-spec；
- 读取 delivery-package-workflow；
- 读取 current-evidence-map 和 current-capability-boundaries；
- 收集目标项目类型、工具环境、隐私约束、自动化期望；
- 生成 Memory System Design Spec 草案；
- 用户确认后再形成交付包。

### C. 上下文过长时交接

流程：

- 更新 active-context；
- 更新 handoff-current；
- 如有新需求，保存 raw 并抽取 candidate；
- 如有执行源变化，经用户确认后更新 human-approved-spec；
- 提交到 GitHub；
- 新对话 / 新任务按 startup-instructions 读取。

### D. 模型迁移

流程：

- 默认继承 Canonical Memory；
- 不默认全量读取 raw；
- 高风险内容按需回查 raw；
- 复审旧模型专用约束；
- 验证新模型能力后再启用新流程。

## 9. 当前不要默认做的事

- 不默认创建 AGENTS.md；
- 不默认创建 CLAUDE.md；
- 不默认创建 GitHub Actions；
- 不默认实现自动查重；
- 不默认实现自动索引；
- 不默认实现自动写回；
- 不默认全量读取 raw；
- 不默认修改研究报告原件；
- 不默认把 PDF 图表内容当作已验证证据；
- 不默认把新想法写入 human-approved-spec。

## 10. 启动后第一条回复格式

新会话 / 新任务接手后，第一条回复应包含：

- 当前阶段；
- 当前执行源；
- 非执行源清单；
- 已完成内容；
- 未完成内容；
- 下一步建议；
- 是否发现冲突；
- 是否需要用户确认。
