# Open Questions

## answered

1. startup-instructions 应放在 `current/` 还是 `handoff/`？
   - 答案：当前放在 `handoff/startup-instructions.md`。

2. startup-instructions 是否应强制读取 `current-capability-boundaries`？
   - 答案：当任务涉及能力边界判断、新机制设计、平台适配、目标项目记忆系统设计、自动化可行性判断或 v0.1/v0.2 能力承诺时，必须读取：
     - `raw/research-reports/current/research-report-index.md`
     - `raw/research-reports/current/current-evidence-map.md`
     - `raw/research-reports/current/current-capability-boundaries.md`

## pending

1. 接手演练是否需要固定检查清单（执行源识别、非执行源识别、已完成/未完成识别、研究证据读取规则识别、下一步任务识别）？
2. 是否需要为每份研究报告建立单独 summary（含固定模板）？
3. 哪些 PDF 图表需要人工复核？是否按决策影响度排序？
4. 是否需要把 PDF 转换为 Markdown / TXT，以便后续自动比对与检索？
5. 是否需要把研究结论拆成 Evidence Item？
6. research evidence 与 `current/human-approved-spec.md` 冲突时是否需要固定模板？
7. 第一个目标项目记忆系统模板优先服务哪类场景？
8. 是否先设计 `AGENTS.md` / `CLAUDE.md`，还是先设计目标项目模板？
9. 是否需要隐私分级后再导入更多 raw？
10. `raw/concept-origin-extract-001.md` 是否需要拆分成多个 raw record？
11. v0.1 是否已经足以支持新对话接手？
