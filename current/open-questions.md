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
7. self-improvement workflow 的最小对象和模板是什么？
   - 结论：当前由 `notes/self-improvement-template-pack.md` 提供基础模板包。
   - 来源：RAW-0033；MNEMOSYNE-026B
8. 用户反馈和 Codex 任务结果如何进入 raw？
   - 结论：当前由 `notes/self-improvement-workflow.md` 与 `notes/self-improvement-template-pack.md` 定义基础流程和模板。
   - 状态：partially_answered；具体使用效果仍待用户 review。
   - 来源：RAW-0033；MNEMOSYNE-026B
9. Codex Task Result Record 是否需要固定模板？
   - 结论：当前由 `notes/self-improvement-template-pack.md` 中的 Codex Task Result Record Template 覆盖。
   - 来源：RAW-0033；MNEMOSYNE-026B
10. 是否需要为 similarity/conflict report 设计最小格式？
    - 结论：当前由 `notes/self-improvement-template-pack.md` 中的 Similarity / Conflict Check Template 覆盖。
    - 来源：RAW-0033；MNEMOSYNE-026B
11. 是否需要为 user decision 设计固定记录格式？
    - 结论：当前由 `notes/self-improvement-template-pack.md` 中的 User Decision Record Template 覆盖。
    - 来源：RAW-0033；MNEMOSYNE-026B
12. self-improvement workflow 是否需要单独模板文件？
    - 结论：当前先采用 `notes/self-improvement-template-pack.md` 单文件模板包；是否拆成多个独立模板文件仍作为 open question 保留。
    - 来源：RAW-0033；MNEMOSYNE-026B

## open

1. similarity/conflict 在 v0.2 中先人工执行还是由 Codex 辅助？
2. 是否需要把重要 Codex 完成回复精简保存？
   - 结论：重要任务、异常任务、验证任务应保存精简结果记录；
   - 普通任务可不保存完整回复；
   - `notes/self-improvement-template-pack.md` 已提供 task result 记录模板，但完成回复保存粒度仍待用户 review。
3. 研究报告 summary 是否先于目标项目模板？
4. PDF 图表人工复核何时做？
5. 是否需要隐私分级后再导入更多 raw？
6. 第一个目标项目记忆系统模板优先服务哪类场景？
   - 来源：RAW-0031；RAW-0033；
   - 说明：目标项目类型尚未由用户确认。
7. 是否先设计 AGENTS.md / CLAUDE.md，还是先设计目标项目模板？
8. `raw/concept-origin-extract-001.md` 是否需要拆分成多个 raw record？
9. self-improvement template pack 是否需要拆成多个独立模板文件？
   - 来源：RAW-0031；RAW-0033；
   - 说明：当前先采用单文件模板包；是否拆分仍待用户 review 后决定。
10. 目标项目 intake 和 memory system design spec 应先做哪个？
    - 来源：RAW-0031；RAW-0033；
    - 说明：两者相关但先后顺序尚未确认。
11. 是否需要先做 Idea Capture Buffer？
    - 来源：RAW-0031；RAW-0033；
    - 说明：Idea Capture Buffer 可能改善临时想法进入流程，但是否优先于目标项目模板仍待决定。
12. 是否需要在模板中加入更正式的隐私分级字段？
    - 来源：RAW-0031；RAW-0033；
    - 说明：Raw Input Entry Template 已包含 `sensitivity`，但是否扩展为正式隐私分级体系仍待决定。
13. 是否需要先小修 self-improvement template pack 再进入目标项目模板？
    - 来源：RAW-0032；RAW-0033；
    - 说明：当前建议先由用户 review template pack；若问题较小，可小修后再进入目标项目 intake / memory system design spec 模板设计。
