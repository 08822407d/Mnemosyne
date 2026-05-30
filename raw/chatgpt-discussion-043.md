# Raw Record: RAW-0043

- raw_id: RAW-0043
- task_id: MNEMOSYNE-030
- task_name: 研究报告 summary 与 PDF 图表复核准备
- source_type: Codex task instruction
- status: captured

## 说明

本记录保存 MNEMOSYNE-030 的任务来源摘要。本任务不是完整原始对话，而是一次面向研究报告摘要层和 PDF 图表 / 图片人工复核索引的施工任务说明记录。

## 任务意图

用户选择先执行路线 D：研究报告 summary / PDF 图表复核。

当前研究轮次是：

- `RC-2026Q2-initial`

本任务用于为该轮次的 7 份研究报告建立 summary 层，并创建 PDF 图表 / 图片人工复核索引，支持后续目标项目 dry-run、能力边界判断、Evidence Item / delta report 模板设计。

## 边界

- 本任务不修改研究报告原件。
- 本任务不重命名或移动研究报告原件。
- 本任务不做 OCR。
- 本任务不把 PDF 图表 / 图片内容写成已复核事实。
- 本任务不选择真实目标项目。
- 本任务不生成真实目标项目交付包。
- 本任务不引入自动化。
- 本任务不创建 AGENTS.md、CLAUDE.md、GitHub Actions、RAG、MCP 或多 Agent 自动协调机制。

## 执行源边界

当前执行源仍是：

- `current/human-approved-spec.md`

report summaries / figure review index 不是执行源。若其内容与 `current/human-approved-spec.md` 冲突，应以 `current/human-approved-spec.md` 为执行准则，并登记 open question。
