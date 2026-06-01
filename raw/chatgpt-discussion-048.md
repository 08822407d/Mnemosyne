# RAW-0048 — MNEMOSYNE-030E：research motivation / research prompts 状态同步与索引补账

- raw_id: RAW-0048
- task_id: MNEMOSYNE-030E
- source_type: user_request
- status: captured
- created_by: Codex

## 用户输入要点

本任务用于修复 MNEMOSYNE-030C / MNEMOSYNE-030D 后状态文件和 current 索引未完全同步的问题。用户确认主体文件已经存在，但 active-context、handoff、todo、open-questions、current research index、current report summaries、candidate / decision / roadmap / baseline 和 030C / 030D result 记录仍需要状态同步与补账。

已确认状态：

- research motivation 已创建：`raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`；
- research prompts / report-topic mapping 已创建；
- pro prompt 原文已放入约定路径，并被标记为 `available_original_prompt`；
- 6 个轻度研究 prompt 原文缺失，并已标记为 `missing_original_prompt`。

## 执行源声明

当前执行源仍是：

- `current/human-approved-spec.md`

以下内容不是执行源：

- `raw/`
- research reports
- research motivation
- research prompts
- report-topic mapping
- report summaries
- PDF figure review index
- candidate / decision / active-context / handoff / task result records

如上述材料与 `current/human-approved-spec.md` 冲突，应以 `current/human-approved-spec.md` 为准，并登记 open question。

## 本任务边界

MNEMOSYNE-030E 只做状态同步、索引补账和结果记录纠偏。本任务不修改研究报告原件，不修改、重命名或移动 pro prompt 原文，不为 6 个轻度研究编造 prompt 原文，不把 inferred topic 写成 user original prompt，不做 OCR，不声称 PDF 图表 / 图片已复核，不创建 AGENTS.md / CLAUDE.md / GitHub Actions，不添加脚本、依赖、测试或构建文件，不修改 `current/human-approved-spec.md`，不选择真实目标项目，也不生成交付包。
