# Open Questions

## answered

1. startup-instructions 应放在 `current/` 还是 `handoff/`？
   - 结论：当前放在 `handoff/startup-instructions.md`。
2. startup-instructions 是否应强制读取 `current-capability-boundaries`？
   - 结论：涉及能力边界、新机制设计、平台适配、目标项目设计时必须读取。
3. v0.1 是否已经足以支持新对话接手？
   - 结论：根据 `notes/startup-rehearsal-report.md`，当前结论为 pass，当前文件集足以支持新 ChatGPT / 新 Codex 任务仅依赖仓库文件接手。
4. startup-instructions 在新 ChatGPT / 新 Codex 接手演练中的可执行性是否足够？
   - 结论：根据 `notes/startup-rehearsal-report.md` 与 `notes/v0.1-independent-verification-report.md`，当前为可执行且足以支撑 v0.1 接手（PASS_WITH_WARNINGS）。
5. 用户是否接受 MNEMOSYNE-023 的 `PASS_WITH_WARNINGS` 结论，并允许进入 v0.2 第一方向选择？
   - 结论：用户接受 `PASS_WITH_WARNINGS`，其不阻断进入 v0.2。
6. v0.2 第一方向应选择哪个？
   - 结论：v0.2 第一方向选择 `self-improvement workflow`。
7. Codex Task Result Record 路径写法是否需要固定？
   - 结论：默认路径使用 `notes/codex-task-results/<TASK_ID>-result.md`。

## open

1. self-improvement workflow 的最小对象和模板是什么？
   - 当前已建立流程说明；
   - 是否需要进一步拆出模板仍为 open。
2. similarity/conflict 在 v0.2 中先人工执行还是由 Codex 辅助？
3. 用户反馈和 Codex 任务结果如何进入 raw？
4. Codex Task Result Record 是否需要固定模板？
5. 是否需要把重要 Codex 完成回复精简保存？
6. 研究报告 summary 是否先于目标项目模板？
7. PDF 图表人工复核何时做？
8. 是否需要隐私分级后再导入更多 raw？
9. 第一个目标项目记忆系统模板优先服务哪类场景？
10. 是否先设计 AGENTS.md / CLAUDE.md，还是先设计目标项目模板？
11. `raw/concept-origin-extract-001.md` 是否需要拆分成多个 raw record？
12. self-improvement workflow 是否需要单独模板文件？
13. 是否需要为 similarity/conflict report 设计最小格式？
14. 是否需要为 user decision 设计固定记录格式？
