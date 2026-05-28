# Open Questions

## answered

1. startup-instructions 应放在 `current/` 还是 `handoff/`？
   - 结论：当前放在 `handoff/startup-instructions.md`。
2. startup-instructions 是否应强制读取 `current-capability-boundaries`？
   - 结论：涉及能力边界、新机制设计、平台适配、目标项目设计时必须读取。
3. v0.1 是否已经足以支持新对话接手？
   - 结论：根据 `notes/startup-rehearsal-report.md`，当前结论为 pass，当前文件集足以支持新 ChatGPT / 新 Codex 任务仅依赖仓库文件接手。

4. startup-instructions 在新 ChatGPT / 新 Codex 接手演练中的可执行性是否足够？
   - 结论：根据 `notes/startup-rehearsal-report.md` 与 `notes/v0.1-independent-verification-report.md`，当前为可执行且足以支撑 v0.1 接手（PASS_WITH_WARNINGS），但仍建议用户做最终 review。
5. 接手演练是否需要固定检查清单？
   - 结论：当前已有 `notes/startup-rehearsal-report.md` 与 `notes/v0.1-independent-verification-report.md` 作为临时检查机制；标准模板可在 v0.2 / future 继续完善。

## open

1. 用户是否确认 v0.1 可作为可接手版本？
2. v0.2 第一方向应选择 self-improvement workflow、目标项目模板、研究 evidence、Idea Capture Buffer、AGENTS.md / CLAUDE.md，还是其他？
3. 是否需要更严格的后续接手回归测试（如固定检查清单：执行源识别、非执行源识别、下一步建议一致性）？
4. 哪些 PDF 图表需要人工复核？
5. 是否需要把 PDF 转换为 Markdown / TXT？
6. 是否需要为每份研究报告建立单独 summary？
7. 是否需要把研究结论拆成 Evidence Item？
8. research evidence 与 `human-approved-spec` 冲突时是否需要固定模板？
9. 第一个目标项目记忆系统模板优先服务哪类场景？
10. 是否先设计 AGENTS.md / CLAUDE.md，还是先设计目标项目模板？
11. 是否需要隐私分级后再导入更多 raw？
12. `raw/concept-origin-extract-001.md` 是否需要拆分成多个 raw record？

## 独立验证后续判断

- 问题：用户是否接受 MNEMOSYNE-023 的 PASS_WITH_WARNINGS 结论，并允许进入 v0.2 第一方向选择？
- 状态：open
- 说明：独立验证未发现阻断性问题，但仍保留研究报告 summary、PDF 图表人工复核、用户最终 review、可选只读回归验证等非阻断事项。
