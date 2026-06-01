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
    - 结论：MNEMOSYNE-028 先深化 delivery manifest，已创建 `notes/delivery-manifest-template-pack.md`。

16. 是否先直接选择第一个目标项目场景，还是先建立 review / selection 准备文件？
    - 结论：MNEMOSYNE-029 先建立三类模板包 review 清单与首个场景选择矩阵。

17. 是否先做研究报告 summary / PDF 图表复核？
   - 结论：用户选择先做一次 D；MNEMOSYNE-030 建立 report summaries，MNEMOSYNE-030A 补齐 PDF figure review index 和状态同步。


18. 是否需要把 7 份研究报告的研究动机入库？
   - 结论：需要。MNEMOSYNE-030C 创建 `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`，用于解释 7 份报告为什么存在、服务什么设计问题、如何约束 Mnemosyne，以及为什么研究报告和 motivation 都不是执行源。
   - 状态：answered；仍需用户 review motivation 文件。

## open


0. 用户是否接受 `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`？
   - 说明：MNEMOSYNE-030C 已创建 research motivation 文件，但需要用户 review，确认其是否准确保留研究动机、边界和后续读取顺序。


1. 用户是否接受 `notes/template-pack-review-and-first-scenario-selection.md`？
   - 说明：该文件已创建，用于 review 三类模板包并准备首个场景选择，但尚未经过用户 review。

2. 用户是否接受当前 `notes/delivery-manifest-template-pack.md`，是否需要小修？
   - 说明：`notes/delivery-manifest-template-pack.md` 已创建，但尚未经过用户 review。

3. 用户是否接受当前 `notes/target-project-memory-system-template-pack.md`，是否需要小修？
   - 说明：`notes/target-project-memory-system-template-pack.md` 已创建，但尚未经过用户 review。

4. 用户是否接受当前 `notes/self-improvement-template-pack.md`，是否需要小修？
   - 说明：template pack 已创建，但尚未经过用户最终 review。

5. self-improvement template pack 是否需要拆成多个独立模板文件？
   - 说明：当前先采用单文件模板包；是否拆分仍待用户 review 后决定。

6. 用户是否接受当前 7 份 report summaries？
   - 说明：7 份 report summaries 与 current-report-summaries 已建立，但仍需用户 review。

7. 哪些 PDF 图表 / 图片需要优先人工复核？
   - 说明：RPT-2026Q2-0002 ~ RPT-2026Q2-0007 均为 pending_manual_review。

8. 人工复核结果是否会影响目标项目模板或 capability boundaries？
   - 说明：若复核发现关键差异，可能需要登记后续修正任务。

9. 是否在进入首个目标项目 dry-run 前完成全部 PDF 图表复核，还是只复核相关部分？
   - 说明：可先复核与首个目标项目设计直接相关的图表 / 图片。

10. 是否选择第一个目标项目场景作为模板试用？
   - 说明：整套 self-improvement / target project / delivery manifest 模板已经建立基础版本，下一步可选择一个真实、半真实或玩具目标项目场景试用。

11. 第一个目标项目模板优先服务哪类场景？
   - 说明：候选场景包括长期研究、学习系统、源码学习、软件开发项目、AI Agent 项目、个人长期对话 / 知识管理、多 Agent 团队或混合未知场景，尚未由用户确认。

12. 是否先小修某个 template pack？
   - 说明：用户可能选择先小修 delivery manifest、target project 或 self-improvement template pack，而不是直接进入场景试用。

13. 是否先做 Idea Capture Buffer？
   - 说明：Idea Capture Buffer 可能改善临时想法进入流程，但是否优先于模板 review / 场景试用仍待决定。

14. 是否需要更正式的隐私分级字段？
   - 说明：目标项目 intake 已包含 `privacy_level` 和 `sensitive_content_types`，但是否扩展为正式隐私分级体系仍待决定。

15. `raw/concept-origin-extract-001.md` 是否需要拆分成多个 raw record？
   - 说明：当前可按需回查；是否拆分仍待决定。
