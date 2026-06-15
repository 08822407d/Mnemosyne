# Handoff Current

## 仓库

Mnemosyne

## 定位

Mnemosyne 是记忆系统元 Agent 工作仓库，用于设计、演化和交付 AI Agent 外部持久记忆系统。

## 当前阶段

MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。当前等待用户选择下一路线：PDF 图表复核、首次 dry-run 或 Idea Capture Buffer / candidate cleanup。

## 当前执行源

`current/human-approved-spec.md`

以下文件不是执行源：

- `raw/`
- `raw/research-reports/`
- `raw/research-reports/current/current-research-prompts.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`
- `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
- `raw/research-reports/cycles/2026Q2-initial/report-summaries/`
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
- `raw/research-reports/current/current-report-summaries.md`
- `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md`
- `raw/user-design-restatements/MNEMOSYNE-031-user-design-intent-restatement.md`
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

如果其他文件与 `human-approved-spec` 冲突，以 `human-approved-spec` 为准，并登记 open question。

## 研究证据层状态

7 份研究报告已作为 `RC-2026Q2-initial` 入库；MNEMOSYNE-030C 已补充该轮研究的 origin / motivation 文件。

当前研究证据入口：

- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`
- `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
- `raw/research-reports/current/current-report-summaries.md`
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
- `raw/research-reports/current/current-research-prompts.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`

研究报告主要供元 Agent 使用，是高权重证据层，不是执行源；不要求或假定用户已经通读、掌握全部报告。元 Agent 应据此进行可行性评价、能力边界确认、当前实践对照和现代化优化建议。PDF 图表和图片仍需人工复核。

MNEMOSYNE-031 增加用户构想重述：先由 AI 整理待重述清单，再由用户口语化重述。重述结果不是原始需求、不是最终设计、不是执行源。

## MNEMOSYNE-031 continuation point

MNEMOSYNE-031 has reached the final writeback checkpoint.

Completed:
- R1 Research Motivation Review.
- R2 Research Prompts and Topic Mapping Review.
- R3 Report Summaries Review.
- R4A User Design Intent Restatement Prompt List.
- R4B user oral restatement: 9 main records + 1 addendum.
- R4B manifest/index.
- R4C user design intent synthesis / candidate requirements draft.
- R5 final D-01 to D-07 user decision review.
- Final checkpoint records.

Current continuation:
- Do not resume from R4B.
- Do not regenerate R4B, R4C, or R5.
- Use final D-01 to D-07 decisions from `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md`, not the unsuperseded R5 draft alone.
- Next route should be selected by the user: PDF figure review / first dry-run / Idea Capture Buffer / candidate cleanup.

Historical note:
- Earlier MNEMOSYNE-031 checkpoint/status-sync files that say R4B/R4C/R5 are pending are historical records from before the final checkpoint.
- They are superseded for current continuation purposes by the final checkpoint record and this handoff section.

## 新会话推荐读取顺序

1. `README.md`
2. `current/human-approved-spec.md`
3. `current/active-context.md`
4. `handoff/handoff-current.md`
5. `handoff/startup-instructions.md`
6. `current/open-questions.md`
7. `current/todo.md`
8. `notes/v0.1-scope-and-consistency-check.md`
9. `notes/v0.1-final-review.md`
10. `notes/requirement-intake-workflow.md`
11. `notes/self-improvement-workflow.md`
12. `notes/self-improvement-template-pack.md`
13. `notes/target-project-memory-system-template-pack.md`
14. `notes/delivery-manifest-template-pack.md`
15. `notes/template-pack-review-and-first-scenario-selection.md`
16. `notes/research-review-and-user-intent-restatement-workflow.md`
17. `notes/overall-target-and-roadmap-snapshot.md`（可选：当需要理解长期目标、路线图或后续计划时按需读取；不是执行源）
18. `notes/system-construction-baseline.md`（可选：当需要理解系统建设基线时按需读取；不是执行源）
19. `raw/research-reports/current/research-report-index.md`
20. `raw/research-reports/current/current-evidence-map.md`
21. `raw/research-reports/current/current-capability-boundaries.md`
22. `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
23. `raw/research-reports/current/current-research-prompts.md`
24. `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`
25. `raw/research-reports/current/current-report-summaries.md`
26. `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
27. `raw/concept-origin-extract-001.md` 按需回查

## 当前不要做

- 不要创建 `AGENTS.md`；
- 不要创建 `CLAUDE.md`；
- 不要创建 GitHub Actions；
- 不要添加自动化脚本；
- 不要实现自动查重、自动索引、自动写回、MCP、RAG 或多 Agent 自动协调；
- 不要假定用户已通读全部研究报告；
- 不要把 research reports 当执行源；
- 不要把 motivation / prompt / topic mapping 当执行源；
- 不要把用户设计构想重述当原始需求、最终设计或执行源；
- 不要把 review 结果写回仓库，除非用户明确确认；
- 不要编造缺失 prompt；
- 不要把 candidate / decision / active-context / handoff / startup-instructions / template packs / review selection 文件当执行源；
- 不要为真实目标项目生成交付包，除非用户明确选择目标项目场景并确认进入交付试用阶段。

## 下一步建议

1. 不要重生成 MNEMOSYNE-031 R4B/R4C/R5；使用 final D-01 to D-07 决策继续后续路线。
2. 下一路线由用户选择：PDF 图表复核 / first dry-run / Idea Capture Buffer / candidate cleanup。
3. 如果执行 dry-run，应显式记住：MNEMOSYNE-031 review/restatement materials 不是执行源；`current/human-approved-spec.md` 仍是当前执行源。

## MNEMOSYNE-031 final checkpoint handoff

Current handoff:

- MNEMOSYNE-031 review and restatement phase has reached final writeback checkpoint.
- Do not regenerate R4B or R4C.
- Use final D-01 to D-07 decisions from `raw/research-reports/cycles/2026Q2-initial/review-records/MNEMOSYNE-031-research-review-record.md`, not the unsuperseded R5 draft alone.
- Next route should be selected by user: PDF figure review / first dry-run / Idea Capture Buffer / small fixes.

Handoff concept clarification:

- Handoff is task-local continuation context.
- It is not global project law.
- It may carry explicit local recovery constraints or temporary exceptions.
- Such local exceptions must not silently become global execution-source changes.
