---
raw_id: RAW-0015
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: public_repo_but_personal_design_content
language: zh-CN
---

# RAW-0015：v0.1 接手能力最终修复与当前状态同步

这不是完整原始对话，而是从当前 ChatGPT 对仓库的核对结果中整理出的交接记录。

## 1. 当前目标

用户希望 Mnemosyne 达到以下状态：

新开 ChatGPT 对话或 Codex 任务后，可以正确读取仓库中的执行源、active-context、handoff、研究证据 current 视图和必要 notes 文件，从而继续当前工作。

接手后的新对话或任务应能够：

- 按当前需求为其他项目设计外部持久记忆系统；
- 根据用户新构想和使用反馈继续增强 Mnemosyne 自身；
- 正确区分执行源、证据层、候选需求、决策记录、handoff、TODO 和开放问题；
- 尊重 7 份研究报告给出的能力边界；
- 不把 raw、research reports、candidate、decision-log、handoff 或 active-context 当成当前实施要求；
- 不把 future / v0.2 功能误写成 v0.1 已完成；
- 在上下文过长时继续通过 handoff 和 active-context 交接。

## 2. 当前仓库核对结论

研究证据层已经初步完成：

- 7 份研究报告已上传到 `raw/research-reports/cycles/2026Q2-initial/originals/`；
- 当前 research cycle 是 `RC-2026Q2-initial`；
- `research-report-index.md` 已经建立 report_id 到实际文件路径的映射；
- `current-evidence-map.md` 已经建立当前证据派生视图；
- `current-capability-boundaries.md` 已经建立当前能力边界派生视图；
- PDF 报告中的图表和图片仍需人工复核。

但接手层仍未完全完成：

- `current/human-approved-spec.md` 仍偏早期，未覆盖 v0.1 已确认的完整执行原则；
- `current/active-context.md` 仍提示下一步要做 v0.1 接手能力修复；
- `handoff/handoff-current.md` 仍提示下一步要做 v0.1 接手能力修复；
- `current/todo.md` 需要按 v0.1-final / v0.2 / future 整理；
- `notes/candidate-requirements.md` 和 `notes/decision-log.md` 需要补齐接手能力相关条目；
- 本次涉及的 Markdown 文件需要修复为正常段落和列表格式。

## 3. 本阶段目标

本阶段只做 v0.1 接手能力最终修复，不引入新机制。

需要完成：

1. 修复本次涉及文件的 Markdown 换行格式；
2. 更新 `current/human-approved-spec.md`，使其成为 v0.1 当前执行源；
3. 更新 `current/active-context.md`，使其反映真实当前阶段；
4. 更新 `handoff/handoff-current.md`，使新 ChatGPT / Codex 任务能接手；
5. 整理 `current/open-questions.md`；
6. 整理 `current/todo.md`；
7. 补齐 `notes/candidate-requirements.md` 中的关键候选需求；
8. 补齐 `notes/decision-log.md` 中的关键设计决策；
9. 更新 `notes/v0.1-scope-and-consistency-check.md` 的检查状态。

## 4. 当前阶段仍不做的事项

本阶段不做：

- 为每份研究报告生成 summary；
- 人工复核 PDF 图表；
- 创建 startup-instructions；
- 建立 AGENTS.md；
- 建立 CLAUDE.md；
- 建立 GitHub Actions；
- 自动查重；
- 自动索引；
- 自动写回；
- 自动模型迁移；
- 自动交付；
- 目标项目真实交付试验。

这些作为 v0.1-final 后续或 v0.2 处理。

## 5. 完成标准

本阶段完成后，未来新会话应能通过读取以下文件接手：

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
11. 必要时读取 `notes/core-object-model.md`、`notes/requirement-intake-workflow.md`、`notes/delivery-package-workflow.md`
12. 需要早期动机时按需读取 `raw/concept-origin-extract-001.md`

如果这些文件之间发生冲突，应以 `current/human-approved-spec.md` 为准，并把冲突登记为 open question。
