# Handoff Current

## 仓库

Mnemosyne

## 定位

Mnemosyne 是记忆系统元 Agent 工作仓库，用于设计、演化和交付 AI Agent 外部持久记忆系统。

## 当前阶段

v0.2 第一方向 self-improvement workflow 已建立，下一步是模板设计。

## 当前执行源

`current/human-approved-spec.md`

以下文件不是执行源：

- `raw/`
- `raw/research-reports/`
- `notes/candidate-requirements.md`
- `notes/decision-log.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `handoff/startup-instructions.md`

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
5. `handoff/startup-instructions.md`
6. `current/open-questions.md`
7. `current/todo.md`
8. `notes/v0.1-scope-and-consistency-check.md`
9. `notes/v0.1-final-review.md`
10. `notes/requirement-intake-workflow.md`
11. `notes/self-improvement-workflow.md`
12. `raw/research-reports/current/research-report-index.md`
13. `raw/research-reports/current/current-evidence-map.md`
14. `raw/research-reports/current/current-capability-boundaries.md`
15. `raw/concept-origin-extract-001.md` 按需回查

## 当前不要做

- 不要创建 `AGENTS.md`；
- 不要创建 `CLAUDE.md`；
- 不要创建 GitHub Actions；
- 不要添加自动化脚本；
- 不要把 research reports 当执行源；
- 不要把 candidate / decision / active-context / handoff / startup-instructions 当执行源。

## 下一步建议

1. 用户 review `notes/self-improvement-workflow.md`；
2. 进入 MNEMOSYNE-026：self-improvement workflow 模板设计；
3. 暂不创建 AGENTS.md / CLAUDE.md / GitHub Actions。
