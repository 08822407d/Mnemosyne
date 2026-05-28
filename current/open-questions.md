# Open Questions

## answered

1. startup-instructions 应放在 `current/` 还是 `handoff/`？
   - 结论：当前放在 `handoff/startup-instructions.md`。
2. startup-instructions 是否应强制读取 `current-capability-boundaries`？
   - 结论：涉及能力边界、新机制设计、平台适配、目标项目设计时必须读取。
3. v0.1 是否已经足以支持新对话接手？
   - 结论：根据 `notes/startup-rehearsal-report.md`，当前结论为 pass，当前文件集足以支持新 ChatGPT / 新 Codex 任务仅依赖仓库文件接手。

## open

1. 是否需要更严格的后续接手回归测试（如固定检查清单：执行源识别、非执行源识别、下一步建议一致性）？
2. 哪些 PDF 图表需要人工复核？
3. 是否需要把 PDF 转换为 Markdown / TXT？
4. 是否需要为每份研究报告建立单独 summary？
5. 是否需要把研究结论拆成 Evidence Item？
6. research evidence 与 `human-approved-spec` 冲突时是否需要固定模板？
7. 第一个目标项目记忆系统模板优先服务哪类场景？
8. 是否先设计 AGENTS.md / CLAUDE.md，还是先设计目标项目模板？
9. 是否需要隐私分级后再导入更多 raw？
10. `raw/concept-origin-extract-001.md` 是否需要拆分成多个 raw record？
