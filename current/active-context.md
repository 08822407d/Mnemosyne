# Active Context

## 当前阶段

研究动机、研究课题 prompt mapping、report summaries 与 PDF 图表复核准备已建立，等待用户 review / 用户构想重述 / 人工复核 / dry-run 决策。

## MNEMOSYNE-031 current status

当前目标是收口 MNEMOSYNE-030C / 030D / 030E / 030F 后的研究证据层状态，并按 MNEMOSYNE-031A 修正复核协议：

- MNEMOSYNE-031 review 将通过普通 ChatGPT 对话执行；
- review 不假定用户已通读研究报告；研究报告主要作为元 Agent 的高权重证据层；
- 元 Agent 应基于报告进行可行性评价、能力边界确认、当前实践对照和现代化优化建议；
- MNEMOSYNE-031 增加用户设计构想重述流程：先由 AI 整理待重述清单，再由用户口语化重述；
- 重述结果不是原始需求、不是最终设计、不是执行源；

后续材料复核包括：

- MNEMOSYNE-031 R1-R3 研究材料复核；
- MNEMOSYNE-031 R4A-R4C 用户设计构想重述；
- 用户 review `raw/research-reports/current/current-research-prompts.md`；
- 用户 review `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`；
- 用户 review `raw/research-reports/current/current-report-summaries.md` 与 7 份 report summaries；
- 对依赖设计判断的 PDF 图表 / 图片 / 版式进行人工复核；
- 根据复核结果更新 `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`；
- 如果未来找回轻度研究 prompt，更新 research-prompt-index；
- 再决定进入首个目标项目 dry-run，还是先做 Idea Capture Buffer / 小修模板。

## 当前执行源

`current/human-approved-spec.md` 是当前执行源。

以下内容不是执行源：

- `raw/`
- `raw/research-reports/`
- `raw/research-reports/current/current-research-prompts.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`
- `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
- `raw/research-reports/cycles/2026Q2-initial/report-summaries/`
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
- `raw/research-reports/current/current-report-summaries.md`
- future MNEMOSYNE-031 review record
- future user design restatement record
- `notes/candidate-requirements.md`
- `notes/decision-log.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `handoff/startup-instructions.md`
- `notes/system-construction-baseline.md`
- `notes/overall-target-and-roadmap-snapshot.md`
- `notes/self-improvement-template-pack.md`
- `notes/target-project-memory-system-template-pack.md`
- `notes/delivery-manifest-template-pack.md`
- `notes/template-pack-review-and-first-scenario-selection.md`
- `notes/research-review-and-user-intent-restatement-workflow.md`

如发生冲突，以 `current/human-approved-spec.md` 为准，并登记 open question。

## 已完成内容

- v0.1 已被接受为可接手版本；
- v0.2 第一方向 self-improvement workflow 已完成流程说明和模板包；
- `notes/self-improvement-workflow.md` 已创建；
- `notes/self-improvement-template-pack.md` 已创建；
- `notes/target-project-memory-system-template-pack.md` 已创建；
- `notes/delivery-manifest-template-pack.md` 已创建；
- `notes/template-pack-review-and-first-scenario-selection.md` 已创建；
- 三类模板包 review 清单已创建；
- 首个场景候选矩阵已创建；
- trial run minimal input request 已创建；
- `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md` 已创建，研究动机入库；
- report-summaries README 已创建；
- 7 份研究报告 summary 文件已创建；
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md` 已创建；
- `raw/research-reports/current/current-report-summaries.md` 已创建；
- Codex Task Result Record 默认路径使用 `notes/codex-task-results/TASK_ID-result.md`；
- `notes/overall-target-and-roadmap-snapshot.md` 和 `notes/system-construction-baseline.md` 已作为规划 / 建设基线快照入库，且不是执行源。
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/README.md` 已创建；
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md` 已创建；
- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md` 已创建；
- `raw/research-reports/current/current-research-prompts.md` 已创建；
- pro 深度研究 prompt 原文路径约定已建立，且文件存在；
- RPT-2026Q2-0002 ~ RPT-2026Q2-0007 的轻度研究 prompt 原文缺失状态已记录为 `missing_original_prompt`；
- MNEMOSYNE-031A 已建立研究复核与用户构想重述协议，但尚未执行 review 或生成 review / restatement record；

## 当前未完成内容

- MNEMOSYNE-031 R4B 用户口语化重述；
- MNEMOSYNE-031 R4C 用户构想重述结果；
- MNEMOSYNE-031 R5 最终 combined writeback package；
- 人工复核 PDF 图表 / 图片；
- 根据复核结果更新 figure review index；
- 用户 review `notes/delivery-manifest-template-pack.md`；
- 用户 review `notes/target-project-memory-system-template-pack.md`；
- 用户 review `notes/self-improvement-template-pack.md`；
- 用户 review `notes/template-pack-review-and-first-scenario-selection.md`；
- 根据 review 小修三类 template packs；
- 选择第一个目标项目场景；
- 第一轮 dry-run intake；
- Idea Capture Buffer；
- `AGENTS.md` / `CLAUDE.md`；
- 自动化增强（自动查重、自动写回、自动索引等）。
- 如果未来找回轻度研究 prompt，更新 `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`；

## 当前最重要文件

- `current/human-approved-spec.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `current/open-questions.md`
- `current/todo.md`
- `handoff/startup-instructions.md`
- `notes/self-improvement-workflow.md`
- `notes/self-improvement-template-pack.md`
- `notes/target-project-memory-system-template-pack.md`
- `notes/delivery-manifest-template-pack.md`
- `notes/template-pack-review-and-first-scenario-selection.md`
- `notes/research-review-and-user-intent-restatement-workflow.md`
- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`
- `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
- `raw/research-reports/current/current-report-summaries.md`
- `raw/research-reports/cycles/2026Q2-initial/report-summaries/README.md`
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
- `notes/system-construction-baseline.md`
- `notes/overall-target-and-roadmap-snapshot.md`
- `raw/research-reports/current/current-research-prompts.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`

## Next step / 下一步

1. 普通 ChatGPT 执行 MNEMOSYNE-031 R1-R3 研究材料复核；
2. 执行 R4A-R4C 用户设计构想重述；
3. 将 R1-R4 结果交给 Codex 或手工写入 review record / restatement record；
4. 再决定 PDF 图表复核 / 首个 dry-run / Idea Capture Buffer。
