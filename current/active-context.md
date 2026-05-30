# Active Context

## 当前阶段

研究报告 summary 与 PDF 图表复核准备已建立，等待用户 review / 人工复核。

## 当前目标

当前目标是为 `RC-2026Q2-initial` 的 7 份研究报告建立 summary 层，并创建 PDF 图表 / 图片人工复核索引。

本阶段用于提高研究证据可读性，支持后续目标项目 dry-run、能力边界判断、Evidence Item / delta report 模板设计。下一步不进入自动化实现，也不创建 AGENTS.md / CLAUDE.md；PDF 图表 / 图片仍需人工复核，未复核内容不得作为已验证设计证据。

## 当前执行源

`current/human-approved-spec.md` 是当前执行源。

以下内容不是执行源：

- `raw/`
- `raw/research-reports/`
- `raw/research-reports/cycles/2026Q2-initial/report-summaries/`
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
- `raw/research-reports/current/current-report-summaries.md`
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

如发生冲突，以 `current/human-approved-spec.md` 为准，并登记 open question。

## 已完成内容

- v0.1 已被接受为可接手版本；
- v0.2 第一方向 self-improvement workflow 已完成流程说明和模板包；
- `notes/self-improvement-workflow.md` 已创建；
- `notes/self-improvement-template-pack.md` 已创建；
- `notes/target-project-memory-system-template-pack.md` 已创建；
- 目标项目 intake 模板已创建；
- memory system design spec 模板已创建；
- target project type classifier 已创建；
- target project memory file layout template 已创建；
- target project execution source rule template 已创建；
- target project workflow template 已创建；
- delivery package draft template 已创建；
- target project handoff template 已创建；
- unsupported assumptions template 已创建；
- drift review template 已创建；
- minimal target project design runbook 已创建；
- `notes/delivery-manifest-template-pack.md` 已创建；
- delivery manifest 模板已创建；
- files to create / update checklist 已创建；
- target project runtime truth source checklist 已创建；
- manual setup steps template 已创建；
- unsupported assumptions linkage template 已创建；
- delivery review checklist 已创建；
- handoff package template 已创建；
- rollback / revision plan template 已创建；
- delivery result record template 已创建；
- minimal delivery runbook 已创建；
- delivery completion criteria 已创建；
- `notes/template-pack-review-and-first-scenario-selection.md` 已创建；
- MNEMOSYNE-029A 已用于补账 / 修复 MNEMOSYNE-029 后 review / scenario selection 文件缺失问题；
- 三类模板包 review 清单已创建；
- 首个场景候选矩阵已创建；
- trial run minimal input request 已创建；
- `raw/research-reports/cycles/2026Q2-initial/report-summaries/README.md` 已创建；
- 7 份研究报告 summary 文件已创建；
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md` 已创建；
- `raw/research-reports/current/current-report-summaries.md` 已创建；
- Codex Task Result Record 默认路径使用 `notes/codex-task-results/TASK_ID-result.md`；
- `notes/overall-target-and-roadmap-snapshot.md` 和 `notes/system-construction-baseline.md` 已作为规划 / 建设基线快照入库，且不是执行源。

## 当前未完成内容

- 用户 review `notes/delivery-manifest-template-pack.md`；
- 用户 review `notes/target-project-memory-system-template-pack.md`；
- 用户 review `notes/self-improvement-template-pack.md`；
- 用户 review `notes/template-pack-review-and-first-scenario-selection.md`；
- 根据 review 小修 self-improvement template pack；
- 根据 review 小修目标项目模板包；
- 根据 review 小修 delivery manifest template pack；
- 选择第一个目标项目场景；
- 第一轮 dry-run intake；
- Idea Capture Buffer；
- 用户 review 7 份 report summaries；
- 用户 review `raw/research-reports/current/current-report-summaries.md`；
- 人工复核 PDF 图表 / 图片；
- 根据复核结果更新 `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`；
- `AGENTS.md` / `CLAUDE.md`；
- 自动化增强（自动查重、自动写回、自动索引等）。

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
- `notes/system-construction-baseline.md`
- `notes/overall-target-and-roadmap-snapshot.md`
- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`
- `raw/research-reports/current/current-report-summaries.md`
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`

## 下一步建议

1. 用户 review `raw/research-reports/current/current-report-summaries.md`；
2. 对依赖设计判断的 PDF 图表 / 图片进行人工复核；
3. 决定进入首个目标项目 dry-run，还是先做 Idea Capture Buffer / 小修模板。
