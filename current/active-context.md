# Active Context

## 当前阶段

v0.2 第一方向 self-improvement workflow 已建立，正在清理格式和记录一致性。

## 当前目标

本阶段目标是设计 Mnemosyne 的自我改进工作流，使用户新构想、使用反馈、Codex/ChatGPT 结果和其他上游反馈能够稳定进入：

raw → candidate → similarity/conflict → user decision → human-approved-spec / todo / open question / decision-log → active-context / handoff。

## 当前执行源

`current/human-approved-spec.md` 是当前执行源。

以下内容不是执行源：

- `raw/`
- `raw/research-reports/`
- `notes/candidate-requirements.md`
- `notes/decision-log.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `handoff/startup-instructions.md`

如发生冲突，以 `current/human-approved-spec.md` 为准，并登记 open question。

## 已完成内容

- v0.1 已被接受为可接手版本；
- v0.2 第一方向已选择为 self-improvement workflow；
- `raw/chatgpt-discussion-025.md` 已创建；
- `notes/self-improvement-workflow.md` 已创建；
- `current/human-approved-spec.md` 已补充 self-improvement workflow 高层原则。

## 当前未完成内容

- self-improvement workflow 用户 review；
- self-improvement workflow 模板设计；
- 目标项目设计模板；
- 研究报告 summary；
- PDF 图表人工复核；
- Idea Capture Buffer；
- `AGENTS.md`；
- `CLAUDE.md`；
- 自动化项（自动查重、自动写回、自动索引等）。

## 下一步建议

1. 用户 review self-improvement workflow；
2. 执行 MNEMOSYNE-026：self-improvement workflow 模板设计；
3. 再考虑目标项目 memory system design spec 模板或 AGENTS.md / CLAUDE.md。
