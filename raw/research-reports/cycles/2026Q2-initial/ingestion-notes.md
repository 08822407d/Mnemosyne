# RC-2026Q2-initial Ingestion Notes

## 入库结果

- 7 份研究报告已上传至 `raw/research-reports/cycles/2026Q2-initial/originals/`。
- 原文件名未重命名，但已通过 report_id 建立稳定引用。
- 本次未修改任何研究报告原件。

## 文件类型与可读性

- Pro 综合报告 1 份：TXT，通常可读性更好。
- 轻度研究 6 份：PDF，可能包含图表、图片或复杂版式。
- PDF 文本可能可读，但图表和图片需要人工复核。

## 执行源边界

- 研究报告属于高权重证据层，不是执行源。
- 当前执行源仍为 `current/human-approved-spec.md`。

## 后续工作建议

- 为每份研究报告生成 summary。
- 必要时将 PDF 转换为 Markdown / TXT，提升后续检索与对照效率。
- 将关键证据拆分为 Evidence Item，支持跨 cycle 复用与 delta 对照。
