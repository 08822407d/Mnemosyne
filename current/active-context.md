# Active Context

## 当前阶段

研究报告 summary 与 PDF 图表复核准备已建立，等待用户 review / 人工复核。

## 当前目标

当前目标是让 `RC-2026Q2-initial` 的 7 份研究报告具备可读 summary 入口，并明确 PDF 图表 / 图片 / 版式证据的人工复核状态，为后续目标项目 dry-run、能力边界判断、Evidence Item / delta report 模板设计提供更可靠的证据入口。

下一步不进入自动化实现，也不创建 AGENTS.md / CLAUDE.md，而是先由用户 review report summaries，并决定是否需要先人工复核与目标项目设计相关的 PDF 图表 / 图片，再进入首个目标项目 dry-run 或 Idea Capture Buffer。

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
- `notes/delivery-manifest-template-pack.md` 已创建；
- `notes/template-pack-review-and-first-scenario-selection.md` 已创建；
- 三类模板包 review 清单已创建；
- 首个场景候选矩阵已创建；
- trial run minimal input request 已创建；
- `raw/research-reports/cycles/2026Q2-initial/report-summaries/README.md` 已创建；
- 7 份研究报告 summary 文件已创建；
- `raw/research-reports/current/current-report-summaries.md` 已创建；
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md` 已创建；
- RPT-2026Q2-0002 ~ RPT-2026Q2-0007 的 PDF 图表 / 图片 / 版式已登记为 `pending_manual_review`；
- Codex Task Result Record 默认路径使用 `notes/codex-task-results/TASK_ID-result.md`；
- `notes/overall-target-and-roadmap-snapshot.md` 和 `notes/system-construction-baseline.md` 已作为规划 / 建设基线快照入库，且不是执行源。

## 当前未完成内容

- 用户 review `raw/research-reports/current/current-report-summaries.md`；
- 用户 review 7 份 report summaries；
- 人工复核 PDF 图表 / 图片 / 版式；
- 根据人工复核结果更新 `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`；
- 决定进入首个目标项目 dry-run 前是否需要复核全部 PDF 图表，还是只复核相关部分；
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
- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`
- `raw/research-reports/current/current-report-summaries.md`
- `raw/research-reports/cycles/2026Q2-initial/report-summaries/README.md`
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
- `notes/system-construction-baseline.md`
- `notes/overall-target-and-roadmap-snapshot.md`

## 下一步建议

1. 用户 review `raw/research-reports/current/current-report-summaries.md` 和 7 份 report summaries；
2. 对依赖设计判断的 PDF 图表 / 图片 / 版式进行人工复核，并更新 `pdf-figure-review-index.md`；
3. 决定进入首个目标项目 dry-run，还是先做 Idea Capture Buffer / 小修模板。
