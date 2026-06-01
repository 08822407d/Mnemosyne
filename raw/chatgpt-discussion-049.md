# RAW-0049 — MNEMOSYNE-030F：research prompt mapping 硬同步与 030E 结果纠偏

- raw_id: RAW-0049
- task_id: MNEMOSYNE-030F
- source_type: user_request
- status: captured
- created_by: Codex

## 记录说明

本文件不是完整原始对话，只记录 MNEMOSYNE-030F 的任务输入、边界和状态纠偏要求。

## 用户输入要点

本任务用于修复 MNEMOSYNE-030E 后 research prompt mapping 仍未稳定同步进 current 索引和接手状态文件的问题。用户要求进行“硬同步”，确保 current research index、current report summaries、active-context、handoff、todo、open-questions、candidate / decision、roadmap / baseline 和 030E task result 都明确反映 research motivation / research prompts / report-topic mapping 的状态。

已确认状态：

- research motivation 已创建：`raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`；
- `raw/research-reports/current/current-research-prompts.md` 已创建；
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md` 已创建；
- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md` 已创建；
- pro prompt 原文已放入约定路径，并标记为 `available_original_prompt`；
- 6 个轻度研究 prompt 原文缺失，并已标记为 `missing_original_prompt`。

## 执行源声明

当前执行源仍是：

- `current/human-approved-spec.md`

以下内容不是执行源：

- `raw/`
- `raw/research-reports/`
- research reports
- research motivation
- research prompts
- report-topic mapping
- report summaries
- PDF figure review index
- `notes/candidate-requirements.md`
- `notes/decision-log.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- task result records

如果其他文件与 `current/human-approved-spec.md` 冲突，应以执行源为准，并登记 open question。

## 本任务边界

MNEMOSYNE-030F 只做 research prompt mapping 硬同步与 030E 结果纠偏。本任务不修改研究报告原件，不修改、重命名或移动 pro prompt 原文，不编造缺失 prompt，不把 inferred topic 写成 user original prompt，不做 OCR，不声称 PDF 图表 / 图片已复核，不创建 AGENTS.md / CLAUDE.md / GitHub Actions，不添加脚本、依赖、测试或构建文件，不修改 `current/human-approved-spec.md`，不选择真实目标项目，也不生成交付包。
