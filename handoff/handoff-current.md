# Handoff Current

## 仓库

Mnemosyne

## 定位

Mnemosyne 是记忆系统元 Agent 工作仓库，用于设计、演化和交付 AI Agent 外部持久记忆系统。

## 当前阶段

v0.1 接手层已完成强制覆盖修复，等待用户 review、`startup-instructions` 和接手演练。

## 当前执行源

`current/human-approved-spec.md`

以下文件不是执行源：

- `raw/`
- `raw/research-reports/`
- `notes/candidate-requirements.md`
- `notes/decision-log.md`
- `current/active-context.md`
- `handoff/handoff-current.md`

如果其他文件与 `human-approved-spec` 冲突，以 `human-approved-spec` 为准，并登记 open question。

## 研究证据层状态

7 份研究报告已作为 `RC-2026Q2-initial` 入库。

当前研究证据入口：

- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`

研究报告是高权重证据层，不是执行源。PDF 图表和图片仍需人工复核。

## 新会话推荐读取顺序

1. `README.md`
2. `current/human-approved-spec.md`
3. `current/active-context.md`
4. `handoff/handoff-current.md`
5. `current/open-questions.md`
6. `current/todo.md`
7. `notes/v0.1-scope-and-consistency-check.md`
8. `raw/research-reports/current/research-report-index.md`
9. `raw/research-reports/current/current-evidence-map.md`
10. `raw/research-reports/current/current-capability-boundaries.md`
11. `notes/core-object-model.md`
12. `notes/requirement-intake-workflow.md`
13. `notes/delivery-package-workflow.md`
14. `raw/concept-origin-extract-001.md` 按需回查

## 当前不要做

- 不要创建 `AGENTS.md`；
- 不要创建 `CLAUDE.md`；
- 不要创建 GitHub Actions；
- 不要实现自动查重；
- 不要实现自动索引；
- 不要实现自动写回；
- 不要把 research reports 当执行源；
- 不要把 candidate / decision / active-context / handoff 当执行源。

## 下一步建议

1. 用户 review `human-approved-spec`、`active-context`、`handoff-current`；
2. 创建 `startup-instructions`；
3. 做一次新 ChatGPT / 新 Codex 接手演练；
4. 再选择 v0.2 方向。
