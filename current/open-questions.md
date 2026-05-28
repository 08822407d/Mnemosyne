# Open Questions

## answered

1. startup-instructions 应放在 `current/` 还是 `handoff/`？
   - 结论：当前放在 `handoff/startup-instructions.md`。

2. startup-instructions 是否应强制读取 `current-capability-boundaries`？
   - 结论：涉及能力边界、新机制设计、平台适配、目标项目设计时必须读取。

3. startup-instructions 在新 ChatGPT / 新 Codex 接手演练中的可执行性是否足够？
   - 结论：`notes/startup-rehearsal-report.md` 已记录演练结果，状态为 pass。

## pending

1. 是否需要为每份研究报告建立单独 summary（含固定模板）？
2. 哪些 PDF 报告中的图表和图片需要优先人工复核？是否按决策影响度排序？
3. 是否需要将 6 份 PDF 转换为 Markdown / TXT，以便后续自动比对与检索？
4. 是否需要将研究结论拆分为可复用的 Evidence Item？
5. 当前 `current-evidence-map.md` 是否足以支撑下一阶段设计，还是需要更细颗粒度证据索引？
6. 当 research report 与 `current/human-approved-spec.md` 冲突时，是否需要标准处理模板？
7. 下一次 research refresh 的触发机制是固定按 2026-08-27，还是允许提前 ad-hoc 触发？
8. v0.2 第一方向应优先选择哪一个？
   - 目标项目 memory system design spec 模板；
   - self-improvement workflow；
   - 研究报告 summary / Evidence Item；
   - 隐私分级；
   - AGENTS.md / CLAUDE.md。
