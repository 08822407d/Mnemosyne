# Handoff Current

## 仓库

Mnemosyne

## 定位

Mnemosyne 是记忆系统元 Agent 工作仓库，用于设计、演化和交付 AI Agent 外部持久记忆系统。

## 当前阶段

research motivation / research prompts / report summaries / PDF figure review index 已建立，等待 review / 人工复核 / dry-run 决策。

## 当前执行源

`current/human-approved-spec.md`

以下文件不是执行源：

- `raw/`
- `raw/research-reports/`
- research prompts / topic mapping
- `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
- `raw/research-reports/current/current-research-prompts.md`
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

如果其他文件与 `human-approved-spec` 冲突，以 `human-approved-spec` 为准，并登记 open question。

## 研究证据层状态

7 份研究报告已作为 `RC-2026Q2-initial` 入库；MNEMOSYNE-030C 已补充该轮研究的 origin / motivation 文件；MNEMOSYNE-030D 已建立 research prompt / topic mapping 层；MNEMOSYNE-030E 已完成 current 索引与状态同步补账。

当前研究证据入口：

- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`
- `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`
- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
- `raw/research-reports/current/current-research-prompts.md`
- `raw/research-reports/current/current-report-summaries.md`
- `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`

研究报告是高权重证据层，不是执行源。PDF 图表和图片仍需人工复核。

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
16. `notes/overall-target-and-roadmap-snapshot.md`（可选：当需要理解长期目标、路线图或后续计划时按需读取；不是执行源）
17. `notes/system-construction-baseline.md`（可选：当需要理解系统建设基线时按需读取；不是执行源）
18. `raw/research-reports/current/research-report-index.md`
19. `raw/research-reports/current/current-evidence-map.md`
20. `raw/research-reports/current/current-capability-boundaries.md`
21. `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`
22. `raw/research-reports/current/current-research-prompts.md`
23. `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
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
- 不要把 research reports 当执行源；
- 不要把 motivation / prompt / topic mapping 当执行源；
- 不要编造缺失 prompt；
- 不要把 candidate / decision / active-context / handoff / startup-instructions / template packs / review selection 文件当执行源；
- 不要为真实目标项目生成交付包，除非用户明确选择目标项目场景并确认进入交付试用阶段。

## 下一步建议

1. 用户 review research motivation / prompts / summaries；
2. 决定是否先人工复核与目标项目设计相关的 PDF 图表；
3. 决定进入首个目标项目 dry-run，还是先做 Idea Capture Buffer / 小修模板。
