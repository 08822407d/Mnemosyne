# Open Questions

## answered

1. startup-instructions 应放在 `current/` 还是 `handoff/`？
   - 答案：当前放在 `handoff/startup-instructions.md`。

2. startup-instructions 是否应强制读取 `current-capability-boundaries`？
   - 答案：当任务涉及能力边界判断、新机制设计、平台适配、目标项目记忆系统设计、自动化可行性判断或 v0.1/v0.2 能力承诺时，必须读取：
     - `raw/research-reports/current/research-report-index.md`
     - `raw/research-reports/current/current-evidence-map.md`
     - `raw/research-reports/current/current-capability-boundaries.md`

3. startup-instructions 在新 ChatGPT / 新 Codex 接手演练中的可执行性是否足够？
   - 结论：初步演练结果为 pass，足以支持接手；仍需用户 review。

4. 接手演练是否需要固定检查清单？
   - 结论：需要，startup-rehearsal-report 已采用执行源识别、非执行源识别、已完成内容、未完成内容、冲突检查和结论作为检查项。

## pending

1. 哪些 PDF 报告中的图表和图片需要优先人工复核？
2. 是否需要将 6 份 PDF 转换为 Markdown / TXT？
3. 是否需要为每份报告建立单独 summary？
4. 是否需要将研究结论拆分为可复用的 Evidence Item？
5. current-evidence-map 是否足以支撑下一阶段设计，还是需要更细颗粒度证据索引？
6. 当 research report 与 human-approved-spec 冲突时，是否需要标准处理模板？
7. 下一次 research refresh 的触发机制是固定按 2026-08-27，还是允许提前 ad-hoc 触发？
