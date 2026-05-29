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
   - 结论：当前由 `notes/self-improvement-workflow.md` 和 `notes/self-improvement-template-pack.md` 提供基础流程与模板包。
   - 状态：已由 template pack 初步覆盖；是否拆分或小修见 open 区域。

8. 用户反馈和 Codex 任务结果如何进入 raw？
   - 结论：当前由 `notes/self-improvement-workflow.md` 定义基本流程，并由 `notes/self-improvement-template-pack.md` 提供 Raw Input 与 Codex Task Result Record 模板。
   - 状态：partially_answered；实际效果仍待用户 review。

9. Codex Task Result Record 是否需要固定模板？
   - 结论：当前由 `notes/self-improvement-template-pack.md` 中的 Codex Task Result Record Template 覆盖。
   - 状态：answered；是否小修见 open 区域。

10. 是否需要把重要 Codex 完成回复精简保存？
    - 结论：重要任务、异常任务、验证任务应保存精简结果记录；普通任务可不保存完整回复。
    - 状态：模板已由 `notes/self-improvement-template-pack.md` 初步覆盖；是否小修见 open 区域。

11. 是否需要为 similarity/conflict report 设计最小格式？
    - 结论：当前由 `notes/self-improvement-template-pack.md` 中的 Similarity / Conflict Check Template 覆盖。
    - 状态：answered；是否小修见 open 区域。

12. 是否需要为 user decision 设计固定记录格式？
    - 结论：当前由 `notes/self-improvement-template-pack.md` 中的 User Decision Record Template 覆盖。
    - 状态：answered；是否小修见 open 区域。

13. 是否先设计 AGENTS.md / CLAUDE.md，还是先设计目标项目模板？
    - 结论：当前先进入目标项目 intake / memory system design spec 模板设计；AGENTS.md / CLAUDE.md 留作后续。

14. 目标项目 intake 和 memory system design spec 应先做哪个，还是一起做？
    - 结论：MNEMOSYNE-027 选择一起创建基础模板包。


15. 是否先深化 delivery manifest，还是先选择第一个目标项目场景试用模板？
    - 结论：MNEMOSYNE-028 先深化 delivery manifest。

## open

1. 用户是否接受当前 `notes/delivery-manifest-template-pack.md`，是否需要小修？
   - 说明：`notes/delivery-manifest-template-pack.md` 已创建，但尚未经过用户 review。

2. 用户是否接受当前 `notes/self-improvement-template-pack.md`，是否需要小修？
   - 说明：template pack 已创建，但尚未经过用户最终 review。

3. self-improvement template pack 是否需要拆成多个独立模板文件？
   - 说明：当前先采用单文件模板包；是否拆分仍待用户 review 后决定。

4. 用户是否接受当前 `notes/target-project-memory-system-template-pack.md`，是否需要小修？
   - 说明：`notes/target-project-memory-system-template-pack.md` 已创建，但尚未经过用户 review。

5. 是否选择第一个目标项目场景作为模板试用？
   - 说明：候选场景包括长期研究、学习系统、源码学习、软件开发项目、AI Agent 项目、个人长期对话或多 Agent 团队，尚未由用户确认。

6. 是否需要先做 Idea Capture Buffer？
   - 说明：Idea Capture Buffer 可能改善临时想法进入流程，但是否优先于目标项目模板 review / delivery manifest 仍待决定。

7. 是否需要更正式的隐私分级字段？
   - 说明：目标项目 intake 已包含 `privacy_level` 和 `sensitive_content_types`，但是否扩展为正式隐私分级体系仍待决定。

8. 研究报告 summary 是否先于真实目标项目交付？
   - 说明：研究报告 summary 可增强证据可读性；是否作为真实目标项目交付前置条件仍待决定。

9. PDF 图表人工复核何时做？
   - 说明：PDF 图表和图片仍需人工复核；若真实目标项目设计依赖图表证据，应先复核。

10. `raw/concept-origin-extract-001.md` 是否需要拆分成多个 raw record？
    - 说明：当前可按需回查；是否拆分仍待决定。

11. 第一个目标项目模板优先服务哪类场景？
    - 说明：若决定选择第一个目标项目场景试用模板，仍需确认优先服务长期研究、学习系统、源码学习、软件开发项目、AI Agent 项目、个人长期对话或多 Agent 团队中的哪一类。
