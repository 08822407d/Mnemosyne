# RC-2026Q2-initial Ingestion Notes

## 入库结果

- 已上传 7 份研究报告到 `raw/research-reports/cycles/2026Q2-initial/originals/`。
- 原始文件名未按 RPT 规范重命名，但已在 `current/research-report-index.md` 中建立稳定 report_id 映射。
- 本次不修改原件，不重命名原件。

## 文件类型与可读性

- Pro 综合报告 1 份：TXT（通常更容易被 Codex 直接读取）。
- 轻度研究 6 份：PDF（可能包含图表、图片与复杂版式）。
- 对 PDF：文本可能可读，但图表和图片结论需人工复核。

## 证据层边界

- 本次仅完成研究证据入库与派生映射更新。
- 本次不把研究报告写成执行源。
- 执行源仍为 `current/human-approved-spec.md`。

## 后续建议

- 为每份报告生成 summary。
- 将关键结论拆分为 Evidence Item（便于跨 cycle 复用与 delta 对照）。
