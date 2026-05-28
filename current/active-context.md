# Active Context

## 当前阶段

v0.1 接手演练已通过，等待用户 review 和 v0.2 方向选择。

## 当前目标

让新 ChatGPT 对话或新 Codex 任务可以正确接手 Mnemosyne，并继续：

- 为其他项目设计外部持久记忆系统；
- 根据用户新构想和使用反馈完善 Mnemosyne 自身；
- 正确区分执行源、证据层、候选需求、决策记录、handoff、TODO 和开放问题；
- 尊重 7 份研究报告给出的能力边界。

## 当前执行源

`current/human-approved-spec.md` 是当前执行源。

以下内容不是执行源：

- `raw/`
- `raw/research-reports/`
- `notes/candidate-requirements.md`
- `notes/decision-log.md`
- `current/active-context.md`
- `handoff/handoff-current.md`

如发生冲突，以 `current/human-approved-spec.md` 为准，并登记 open question。

## 已完成内容

- 最小仓库结构；
- 当前操作约定；
- 核心业务需求；
- 核心对象模型；
- 对象模板与 ID / 状态规则；
- 需求进入流程；
- handoff / active-context / 阶段性回顾机制；
- 模型迁移与约束生命周期；
- 交付包结构；
- v0.1 范围说明；
- 近原文核心构想摘录入库；
- 7 份研究报告作为 `RC-2026Q2-initial` 证据层入库；
- `current-evidence-map` 与 `current-capability-boundaries` 建立；
- `human-approved-spec` 已同步为 v0.1 当前执行源；
- `handoff-current` 已更新为新会话接手卡；
- `startup-instructions` 已创建；
- 新 ChatGPT / 新 Codex 接手演练已通过；
- `notes/startup-rehearsal-report.md` 已创建。

## 当前未完成内容

- 用户 review 接手演练结果；
- 为每份研究报告生成 summary；
- PDF 图表人工复核；
- 目标项目设计模板；
- `AGENTS.md`；
- `CLAUDE.md`；
- GitHub Actions；
- 自动查重和索引；
- 隐私分级；
- Idea Capture Buffer。

## 当前最重要文件

- `current/human-approved-spec.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `current/open-questions.md`
- `current/todo.md`
- `notes/v0.1-scope-and-consistency-check.md`
- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`
- `raw/concept-origin-extract-001.md`

## 下一步建议

1. 用户 review `human-approved-spec`、`startup-instructions` 和 `startup-rehearsal-report`；
2. 根据 review 结果修正少量状态文件；
3. 选择 v0.2 第一方向；
4. 不建议在 review 前直接开始 AGENTS.md、CLAUDE.md 或自动化。
