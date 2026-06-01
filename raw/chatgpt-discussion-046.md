# RAW-0046 — MNEMOSYNE-030C：RC-2026Q2-initial 研究动机 raw 补充与索引

- raw_id: RAW-0046
- task_id: MNEMOSYNE-030C
- source_type: user_request
- status: captured
- created_by: Codex

## 用户输入要点

用户指出：当前仓库已经保存了 `RC-2026Q2-initial` 的 7 份研究报告、report summaries、current evidence map、capability boundaries 和 PDF figure review index，但没有显式保存“为什么要做这轮研究”的动机材料。

用户要求将研究动机与报告结果一起保存，帮助后续 ChatGPT / Codex / Claude / Claude Code 理解：

- 这些报告为什么存在；
- 每份报告服务什么设计问题；
- 这些报告如何约束 Mnemosyne 的设计方向、能力边界和风险判断；
- 为什么这些报告是高权重证据层；
- 为什么这些报告和本次创建的 research motivation 都不是执行源。

## 本任务边界

MNEMOSYNE-030C 只补充 `RC-2026Q2-initial` 的研究动机 raw 与索引，不重新摘要研究报告，不修改、移动或重命名 7 份研究报告原件，不做 OCR，不声称 PDF 图表 / 图片 / 版式已经人工复核，也不进入真实目标项目 dry-run。

## 执行源声明

当前执行源仍是：

- `current/human-approved-spec.md`

以下内容不是执行源：

- `raw/`
- `raw/research-reports/`
- 研究报告原件
- report summaries
- figure review index
- 本任务创建的 research motivation 文件
- candidate / decision / active-context / handoff / task result records

如上述材料与 `current/human-approved-spec.md` 冲突，应以 `current/human-approved-spec.md` 为准，并登记 open question。

## 本 raw 的用途

本 raw 记录用户对 MNEMOSYNE-030C 的明确要求：需要把研究动机入库，使后续模型不仅能看到研究结论，还能理解这轮研究为什么被发起、为什么对 Mnemosyne 的外部持久记忆架构重要，以及应该如何把研究结果作为证据层而不是执行源使用。
