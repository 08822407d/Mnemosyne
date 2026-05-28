# Self-Improvement Workflow / 自我改进工作流

## 1. 文件定位

本文件定义 Mnemosyne 如何根据用户新构想、使用反馈、Codex / ChatGPT 任务结果、研究更新和目标项目反馈持续改进自身。

本文件是工作流说明，不是执行源。

当前执行源仍是：

- `current/human-approved-spec.md`

如果本文件与 `current/human-approved-spec.md` 冲突，应以 `human-approved-spec` 为准，并登记 open question。

## 2. 输入来源

Mnemosyne 的自我改进输入至少包括：

1. 用户新构想；
2. 用户对 Mnemosyne 使用体验的反馈；
3. Codex Cloud 任务结果；
4. ChatGPT 对话阶段总结；
5. 新研究报告或 research refresh；
6. 目标项目使用反馈；
7. 失败案例或冲突案例；
8. 模型迁移或工具切换时的反馈；
9. 临时点子速记。

说明：

- 不同输入来源都不能直接修改执行源；
- 必须进入自我改进流程；
- 临时点子速记当前仍属于 Idea Capture Buffer 的未来方向。

## 3. 总体流程

推荐流程：

Input
→ Raw / Task Result Record
→ Candidate Requirement
→ Similarity / Conflict Check
→ User Decision
→ Apply to Spec / TODO / Open Question / Decision Log
→ Refresh Active Context / Handoff

## 4. Step 1：Capture / 保存输入

用户原文、新构想、反馈、任务结果或研究更新应先保存为 raw 或 task result record。

应尽量保留：

- 来源；
- 时间；
- 上下文；
- 相关 PR；
- commit；
- 文件路径；
- 用户原始表述；
- Codex / ChatGPT 的重要限制或不确定项。

本步骤不得直接更新 `current/human-approved-spec.md`。

## 5. Step 2：Extract / 抽取候选需求

从 raw 或 task result 中抽取 Candidate Requirement。

要求：

- 记录 source_refs；
- 标记状态；
- 说明是否已反映到 spec / todo / open question / handoff；
- Candidate Requirement 不是执行源。

候选状态可以包括：

- pending；
- reflected；
- rejected；
- deferred；
- merged；
- superseded。

## 6. Step 3：Compare / 查重和冲突检查

将新候选与已有内容比较：

- `current/human-approved-spec.md`
- `notes/candidate-requirements.md`
- `notes/decision-log.md`
- `current/open-questions.md`
- `current/todo.md`
- research evidence current 视图
- relevant raw records

比较关系可以包括：

- duplicate；
- similar；
- conflicts_with；
- refines；
- supersedes；
- merged_into。

当前只做人工或 Codex 辅助检查，不做自动语义查重。

## 7. Step 4：Present / 向用户呈现决策选项

向用户呈现至少以下选项：

- accept：接受并进入实施；
- refine：要求改写后再确认；
- merge：合并到已有规则；
- replace：替换旧规则；
- keep_parallel：并列保留；
- keep_candidate：继续作为候选；
- defer：延期；
- reject：拒绝但保留证据；
- needs_research：需要更多研究证据；
- needs_human_review：需要人工复核。

模型可以建议，但不得替用户静默决定。

## 8. Step 5：Apply / 应用用户确认结果

只有用户确认后，才可更新：

- `current/human-approved-spec.md`

如果只是未来工作，更新：

- `current/todo.md`

如果仍未决定，更新：

- `current/open-questions.md`

如果形成设计取舍，更新：

- `notes/decision-log.md`

如果影响当前工作状态，更新：

- `current/active-context.md`

如果影响新会话接手，更新：

- `handoff/handoff-current.md`
- `handoff/startup-instructions.md`

## 9. Step 6：Refresh / 刷新接手材料

以下情况后应检查是否刷新 active-context / handoff：

- human-approved-spec 发生变化；
- 当前阶段发生变化；
- v0.2 方向变化；
- 接手流程变化；
- 研究证据影响能力边界；
- 目标项目交付状态变化；
- 模型迁移或工具切换；
- Codex 任务结果显示实际文件状态与任务总结不一致。

## 10. Codex Task Result Record 规则

Codex 任务完成后，除了对话界面总结外，重要任务还应把任务结果写入仓库。

结果记录不是执行源，只是审计材料。最终判断仍以 Git diff、仓库文件、用户 review 和必要验证为准。

每个后续 Codex 任务原则上都应写入对应 `<TASK_ID>-result.md`。

默认路径为：`notes/codex-task-results/<TASK_ID>-result.md`。

如果任务已有专门验证报告或演练报告，可以在该报告中写入结果，但仍需在任务总结中说明。

如果没有专门报告文件，则写入：

- `notes/codex-task-results/<TASK_ID>-result.md`

结果记录应至少包含：

- task_id；
- task_name；
- files_created；
- files_modified；
- files_not_modified；
- codex_summary；
- known_gaps；
- manual_review_required；
- follow_up_tasks；
- whether_any_limits_or_uncertainties。

## 11. 什么时候必须回查研究证据

在以下场景必须读取 research current 视图：

- 判断工具能力边界；
- 设计平台适配；
- 设计自动化能力；
- 设计目标项目记忆系统；
- 修改 v0.1 / v0.2 能力承诺；
- 判断某个机制是否现实可行；
- 讨论 ChatGPT / Claude / Codex / Claude Code / Cursor / GitHub / MCP / RAG 等能力。

必须读取：

- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`

## 12. 什么时候必须更新 human-approved-spec

只有在以下条件同时满足时，才更新 `current/human-approved-spec.md`：

- 用户明确确认；
- 已检查是否与现有 spec 冲突；
- 已记录 source_refs；
- 必要时已记录 decision-log；
- 不属于纯 TODO、open question 或未来构想；
- 不只是 Codex / ChatGPT 的建议。

## 13. 什么时候只更新 TODO / Open Questions

只更新 TODO 的情况：

- 用户认可该事项未来要做，但当前不做；
- 该事项属于 v0.2 / future；
- 还没有足够设计细节进入 spec。

只更新 Open Questions 的情况：

- 用户尚未决定；
- 研究证据不足；
- 文件之间存在冲突；
- 需要人工复核；
- 需要比较多个方案。

## 14. 什么时候更新 decision-log

当出现以下情况时更新 decision-log：

- 选择一个方向并拒绝其他方向；
- 接受 PASS_WITH_WARNINGS；
- 决定某项机制延期；
- 决定某项能力不在 v0.1 / v0.2 承诺中；
- 决定采用某个目录结构、模板、流程或约束；
- 决定从某个 research cycle 继承证据视图；
- 决定将某个异常或修复结果纳入长期维护规则。

## 15. 失败与偏差处理

如果 Codex 声称完成但文件未修改，应：

- 以仓库文件和 diff 为准；
- 不以 Codex 总结为准；
- 创建修复任务；
- 在 codex task result 或 decision-log 中记录偏差；
- 必要时缩小任务范围或改为手工修改。

如果 startup-instructions、handoff、active-context 和 human-approved-spec 冲突，应：

- 以 human-approved-spec 为准；
- 将冲突登记为 open question；
- 通过自我改进流程修复。

## 16. 当前不自动化的边界

当前不做：

- 自动抓取对话；
- 自动写 raw；
- 自动查重；
- 自动更新 human-approved-spec；
- 自动合并 PR；
- 自动判断用户真实意图；
- 自动解析 PDF 图表；
- 自动 RAG / MCP；
- 自动跨工具同步。

## 17. 最小操作清单

每次处理新构想、反馈或任务结果时，至少检查：

1. 这是不是新构想 / 反馈 / 任务结果？
2. 是否需要保存 raw 或 task result？
3. 是否抽取 candidate？
4. 是否需要查重 / 冲突检查？
5. 是否需要读取 research evidence？
6. 是否需要用户确认？
7. 更新 spec、todo、open question、decision-log 中的哪一个？
8. 是否需要更新 active-context / handoff？
9. 是否需要记录 Codex task result？
10. 是否产生下一步 TODO？

## 18. 与现有文件关系

- `current/human-approved-spec.md`：执行源；
- `notes/requirement-intake-workflow.md`：通用需求进入流程；
- `notes/self-improvement-workflow.md`：Mnemosyne 自身演化流程；
- `notes/decision-log.md`：设计取舍理由；
- `notes/candidate-requirements.md`：候选需求池；
- `current/open-questions.md`：未决问题；
- `current/todo.md`：待办；
- `current/active-context.md`：当前工作集；
- `handoff/handoff-current.md`：新会话接手卡；
- `notes/codex-task-results/`：Codex 任务结果审计材料。
