# Open Questions

## answered

1. startup-instructions 应放在 `current/` 还是 `handoff/`？
   - 答案：当前放在 `handoff/startup-instructions.md`。

2. startup-instructions 是否应强制读取 `current-capability-boundaries`？
   - 答案：当任务涉及能力边界判断、新机制设计、平台适配、目标项目记忆系统设计、自动化可行性判断或 v0.1/v0.2 能力承诺时，必须读取：
     - `raw/research-reports/current/research-report-index.md`
     - `raw/research-reports/current/current-evidence-map.md`
     - `raw/research-reports/current/current-capability-boundaries.md`

3. 接手演练是否足以证明 Mnemosyne v0.1 可以从仓库状态接手？
   - 答案：本次 REH-2026Q2-0001 结果为 pass，说明在当前文件状态下可以接手；仍需用户 review 后进入下一阶段。

## pending

1. 如果后续接手演练发现问题，哪些问题必须在 v0.2 前修复？
2. 进入 v0.2 的第一方向应选择哪个？
3. 是否先做研究报告 summary / PDF 图表复核，还是先做目标项目模板？
4. 是否需要将 startup rehearsal 固化成模板？
5. 是否需要为每份研究报告建立单独 summary（含固定模板）？
6. 哪些 PDF 图表需要人工复核？是否按决策影响度排序？
7. 是否需要把 PDF 转换为 Markdown / TXT，以便后续自动比对与检索？
8. 是否需要把研究结论拆成 Evidence Item？
9. research evidence 与 `current/human-approved-spec.md` 冲突时是否需要固定模板？
10. 第一个目标项目记忆系统模板优先服务哪类场景？
11. 是否先设计 `AGENTS.md` / `CLAUDE.md`，还是先设计目标项目模板？
12. 是否需要隐私分级后再导入更多 raw？
13. `raw/concept-origin-extract-001.md` 是否需要拆分成多个 raw record？
