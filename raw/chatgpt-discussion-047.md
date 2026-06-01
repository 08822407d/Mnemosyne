# RAW-0047 — MNEMOSYNE-030D：研究课题 prompt 原文入库约定与 report-topic mapping

- raw_id: RAW-0047
- task_id: MNEMOSYNE-030D
- source_type: user_request
- status: captured
- created_by: Codex

## 用户输入要点

用户指出：除了 `RC-2026Q2-initial` 的研究动机，还需要明确哪些文件是这些研究对应的研究课题 / 输入 prompt。研究 prompt 是研究输入材料，用于说明研究问题从何而来；研究报告、summary、evidence map 则是研究结果或派生证据层。

用户会手动将 pro 深度研究课题文件放入约定路径：

- `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/AI_agent_external_persistent_memory_deep_research_prompt_pro.md`

当前只有 pro 深度研究报告对应的课题文件。6 个轻度研究的课题原文已经丢失。不得编造丢失的 6 个 prompt；只能根据报告文件名、report_id 和 summary 记录 topic title / inferred topic，并标记原始 prompt 缺失。

## 执行源声明

当前执行源仍是：

- `current/human-approved-spec.md`

以下内容不是执行源：

- `raw/`
- `raw/research-reports/`
- research prompts
- report-topic mapping
- report summaries
- PDF figure review index
- research motivation
- candidate / decision / active-context / handoff / task result records

如上述材料与 `current/human-approved-spec.md` 冲突，应以 `current/human-approved-spec.md` 为准，并登记 open question。

## 本任务边界

MNEMOSYNE-030D 建立 research prompts / topic mapping 层，不修改研究报告原件，不重命名用户手动放入的 pro prompt 文件，不补写或伪造丢失的 6 个轻度研究 prompt，不做 OCR，不声称 PDF 图表 / 图片 / 版式已复核，不选择真实目标项目，也不生成交付包。
