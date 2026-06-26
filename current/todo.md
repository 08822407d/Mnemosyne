# TODO

## Active now

- Run post-MNEMOSYNE-053 fresh ordinary Thinking replay using the updated protocol and maintainer scorecard.
- Do not treat any pre-053 replay PASS as closing the post-053 gate.
- Keep execution source unchanged unless separately approved.
- Maintain the MNEMOSYNE-043 manual-import safety gate when imports occur.

## Waiting for user decision

- Select target project after post-053 replay reviewed PASS and any required user acceptance of non-blocking warnings.
- Confirm owner/authority.
- Provide safe input manifest.
- Confirm no-target-write.
- Approve the run manifest before any real dry-run.
- Decide whether any D-01–D-07 candidate wording from the MNEMOSYNE-044 coverage map should be promoted into the execution source; separate approval only.

## Waiting for dry-run evidence

- No real target-project dry-run has occurred.
- Use onboarding package and review instruments when dry-run is later authorized.
- No target project has been selected.
- No target materials have been uploaded/ingested.
- No target-project repository has been written.

## Deferred / future

- PDF figure/table/image manual review.
- Candidate/idea cleanup beyond this current-state consolidation.
- Optional DR2 or additional research only if a future design question needs it.
- Platform/visibility reverification when importing files or when repository visibility materially affects the task. Do not add a recurring TODO to change repository visibility merely because it is public.

## Recently completed

- MNEMOSYNE-048 onboarding/review instruments.
- MNEMOSYNE-049 state synchronization after 048.
- MNEMOSYNE-050 protocol closure: manifest template, fresh replay protocol, result semantics, actor boundaries, and current gate update.
- MNEMOSYNE-051: DR2 handoff-strategy research ingested as supplemental evidence cycle `RC-2026Q2-handoff-strategy`; it is not execution source and does not close the post-050 replay gate.
- Batch A small fixes verified passed after post-047 and post-048 verification.
- MNEMOSYNE-052: post-051 compact current-state sync and manual-import helper/template review.
- MNEMOSYNE-053: DR2 handoff-correctness principle, handoff package strategy, replay scorecard, and post-053 replay protocol update.

## Historical detailed task list below

The material below is retained for history and may contain superseded pending/completed wording. Use the current view above for live status.

# TODO

> MNEMOSYNE-031 final checkpoint records are non-execution-source review/restatement records. Current execution source remains `current/human-approved-spec.md`.

## v0.1-final

- [x] 用户 review `notes/v0.1-final-review.md` 和关键接手文件；
- [x] 用户选择 v0.2 第一方向（self-improvement workflow）；
- [x] 创建 `startup-instructions`；
- [x] 做一次新 ChatGPT / 新 Codex 接手演练；
- [x] 为每份研究报告建立 summary；
- [x] MNEMOSYNE-030：研究报告 summary 与 PDF 图表复核准备；
- [ ] 人工复核 PDF 中的图表和图片；
- [ ] 根据人工复核结果更新 pdf-figure-review-index；
- [x] 用户通过 MNEMOSYNE-031 R3 接受 current-report-summaries 与 7 份 summaries 作为暂用文本证据入口（决策 B）；
- [ ] 必要时将 PDF 转换为 Markdown / TXT；
- [ ] 可选：执行一次新 ChatGPT 对话或第二个新 Codex 任务的只读回归验证（非阻断）。

## v0.2

- [x] MNEMOSYNE-043: public repository and manual-import safety gate added for current public/unverified visibility default; OP-08 remains open/partially addressed.

- [x] MNEMOSYNE-042: clarify that `操作内容` means user-required manual actions and use `无需用户操作` when no user action is needed.


### MNEMOSYNE-041 manual import inbox workflow

- [x] MNEMOSYNE-041: add manual import inbox workflow for non-image file transfer to Codex Cloud.
- [ ] Revisit manual-import-inbox workflow if Codex Cloud file attachment capability changes.

### MNEMOSYNE-039 Pro quota refresh plan

- [x] Run Deep Research: AI Agent external persistent memory system testing/debugging/evaluation/failure diagnosis.
- [x] MNEMOSYNE-040: normalize and ingest DR1 through the research workflow as non-execution-source evidence.
- [ ] Convert DR1 failure taxonomy into a minimal memory issue log / drift review checklist.
- [ ] Convert DR1 first-target-project dry-run implications into a minimal checklist before or during the first application test.
- [ ] Run ordinary ChatGPT-Pro Comprehensive Health Review.
- [ ] Use the comprehensive review to decide whether any pre-dry-run Codex small fixes are required.
- [ ] Proceed to first target-project design dry-run after must-fix issues are cleared or explicitly deferred.
- [ ] If quota/time permits, run current AI agent memory/context-engineering/coding-agent capability delta research.

- [x] MNEMOSYNE-038：recovered and indexed six light-research prompt originals for `PROMPT-2026Q2-0002` through `PROMPT-2026Q2-0007`; previous missing status superseded; prompts are research inputs, not execution source or research conclusions.
- [x] MNEMOSYNE-037：long-transfer file/chunking guidance and near-term target-project readiness priority.
- [x] MNEMOSYNE-035：operation/conclusion separation guidance.
- [x] MNEMOSYNE-034：objective neutral engineering stance and command registry.
- [x] `MNEMOSYNE-025：self-improvement workflow 设计`；
- [ ] 用户 review `notes/self-improvement-workflow.md`；
- [x] 清理 notes/self-improvement-workflow.md 的 Codex Task Result Record 路径，默认占位符路径为 notes/codex-task-results/TASK_ID-result.md；
- [ ] 清理 `notes/self-improvement-workflow.md` 的 Markdown 格式；
- [ ] 为每个后续 Codex 任务写入 task result record（默认路径：`notes/codex-task-results/TASK_ID-result.md`）；
- [ ] 后续阶段按 `notes/overall-target-and-roadmap-snapshot.md` 校验是否偏离长期路线；
- [x] `MNEMOSYNE-026：self-improvement workflow 模板设计`；
- [ ] 用户 review `notes/self-improvement-template-pack.md`；
- [ ] 根据 review 小修 self-improvement template pack；
- [x] 设计 Codex Task Result Record 固定模板；
- [x] 设计 Similarity / Conflict Report 最小格式；
- [x] 设计 User Decision Record 模板；
- [ ] 设计 Spec Update Proposal 模板；
- [x] `MNEMOSYNE-027：目标项目 intake / memory system design spec 模板设计`；
- [x] 目标项目 intake 模板；
- [x] memory system design spec 模板；
- [ ] 用户 review `notes/target-project-memory-system-template-pack.md`；
- [ ] 根据 review 小修目标项目模板包；
- [x] `MNEMOSYNE-028：delivery manifest / 目标项目交付包模板深化`；
- [x] delivery manifest 模板深化；
- [x] `MNEMOSYNE-029：三类模板包 review 清单与首个目标项目场景选择准备`；
- [x] MNEMOSYNE-030C：RC-2026Q2-initial 研究动机 raw 补充与索引；
- [x] 记录 RC-2026Q2-initial 的研究动机；
- [x] MNEMOSYNE-030D：研究课题 prompt 原文入库约定与 report-topic mapping；
- [x] 建立 research prompt index / report-topic map；
- [x] pro 深度研究 prompt 文件已放入约定路径；
- [x] MNEMOSYNE-030E：research motivation / research prompts 状态同步与索引补账；
- [x] MNEMOSYNE-030F：research prompt mapping 硬同步与 030E 结果纠偏；
- [x] MNEMOSYNE-031A：复核协议修正与用户设计构想重述准备
- [x] 记录“研究报告主要供元 Agent 使用，不要求用户通读掌握全部报告”的复核前提
- [x] 记录 MNEMOSYNE-031 增加用户设计构想重述流程
- [x] MNEMOSYNE-031 Round 1：research motivation review
- [x] MNEMOSYNE-031 Round 2：research prompts / report-topic mapping review
- [x] MNEMOSYNE-031 Round 3：current-report-summaries 与 7 份 summaries review
- [x] MNEMOSYNE-031 Round 4A：AI 整理用户设计构想待重述清单
- [x] MNEMOSYNE-031 Round 4B：用户按清单口语化重述 / user restatement records
- [x] MNEMOSYNE-031 Round 4C：AI 整理用户构想重述结果 / R4C synthesis
- [x] MNEMOSYNE-031 Round 5：D-01 to D-07 user decision review and checkpoint records

MNEMOSYNE-031 R1-R5 final checkpoint records are now persisted; do not regenerate R4B/R4C.
- [ ] 用户 review `raw/research-reports/cycles/2026Q2-initial/research-cycle-origin-and-motivation.md`；
- [ ] 用户 review `raw/research-reports/current/current-research-prompts.md`；
- [ ] 用户 review `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`；
- [x] MNEMOSYNE-038：已找回轻度研究 prompt 并更新 research-prompt-index / report-topic map / current-research-prompts；
- [x] 三类模板包 review 清单；
- [x] 首个目标项目场景候选矩阵；
- [ ] 用户 review `notes/template-pack-review-and-first-scenario-selection.md`；
- [ ] 用户 review `notes/delivery-manifest-template-pack.md`；
- [ ] 根据 review 小修 delivery manifest template pack；
- [ ] 用户选择第一个目标项目场景；
- [x] MNEMOSYNE-032 first dry-run intake and independent verification PASS；
- [ ] 根据 review 小修三类模板包；
- [ ] Idea Capture Buffer；
- [ ] 隐私分级；
- [ ] Evidence Item 模板；
- [ ] delta report 模板；
- [ ] PDF 图表 / 图片 / 版式人工复核（report summaries 已在 R3 以决策 B 接受为暂用文本证据入口）；
- [ ] `AGENTS.md` / `CLAUDE.md`；
- [ ] 自动化增强。

## future

- [ ] GitHub Actions 文档检查；
- [ ] 自动查重；
- [ ] similarity index；
- [ ] 自动索引；
- [ ] MCP / RAG；
- [ ] 多 Agent 自动协调；
- [ ] 自动 drift review；
- [ ] 自动模型迁移辅助。

## MNEMOSYNE-030C 状态同步

- [x] MNEMOSYNE-030C：RC-2026Q2-initial 研究动机 raw 补充与索引
- [x] 记录 RC-2026Q2-initial 的研究动机
- [x] 用户通过 MNEMOSYNE-031 R1 接受 research motivation（决策 B，保留 review notes）

## MNEMOSYNE-031 final checkpoint update

Completed:

- [x] MNEMOSYNE-031 R1 review
- [x] MNEMOSYNE-031 R2 review
- [x] MNEMOSYNE-031 R3 review
- [x] MNEMOSYNE-031 R4A prompt list
- [x] MNEMOSYNE-031 R4B user restatement records
- [x] MNEMOSYNE-031 R4B manifest
- [x] MNEMOSYNE-031 R4C synthesis
- [x] MNEMOSYNE-031 R5 user decision review
- [x] MNEMOSYNE-031 checkpoint records

Pending / next:

- [ ] decide next route after MNEMOSYNE-032 PASS: PDF figure review / Idea Capture Buffer / candidate cleanup / template review / memory-system testing-debugging feasibility research
- [ ] design future execution-source promotion workflow
- [ ] research memory-system testing/debugging feasibility

## MNEMOSYNE-032 dry-run independent verification

- [x] MNEMOSYNE-032 dry-run artifacts produced.
- [x] Independent verification detail report received and persisted.
- [x] Final independent verdict recorded as `PASS`.
- [x] Invalid-test condition checked: `false`.
- [x] Blocking issues checked: none.
- [ ] Next route remains user-selected: PDF figure/table/image manual review, Idea Capture Buffer / candidate cleanup, template review / small fixes, or memory-system testing/debugging feasibility research.

## MNEMOSYNE-033 Idea Capture Buffer / candidate cleanup

- [x] MNEMOSYNE-033：Idea Capture Buffer / candidate cleanup / 新对话接手稳固化
- [x] 创建 `notes/idea-capture-triage-rules.md`
- [x] 创建 `notes/idea-capture-buffer.md`
- [ ] 定期 triage idea-capture-buffer
- [ ] 生成 Pro Deep Research prompt：memory-system testing/debugging feasibility
- [ ] PDF figure/table/image/layout 局部复核
- [ ] template review / small fixes
- [ ] first real target-project scenario selection

## MNEMOSYNE-033A exported conversation insight buffer backfill

- [x] MNEMOSYNE-033A：exported conversation insight buffer backfill
- [ ] triage IDEA-2026-0009 之后的 exported-conversation-derived entries
- [ ] 决定完整对话导出是否需要清洗版摘要 / selected excerpts
- [ ] 明确 AI 回复在 raw/context evidence 中保存粒度
- [ ] 处理模型能力差异 / Codex 模型选择等 open questions
- [ ] 继续 Pro Deep Research prompt / PDF review / template review / onboarding rehearsal / first target selection 路线选择


## MNEMOSYNE-036 construction-stage understanding backfill

- [x] MNEMOSYNE-036：construction-stage understanding and artifact-boundary clarifications captured.


## MNEMOSYNE-040 follow-up

- [ ] Treat multi-model independent review only as an auxiliary second-opinion method; DR2 optional multi-model independent review research is not currently required unless future template/review-package design needs deeper evidence.

## MNEMOSYNE-044 execution-source coverage map

- [x] Create D-01 to D-07 execution-source coverage map: `notes/MNEMOSYNE-031-D01-D07-execution-source-coverage-map.md`.
- [ ] User review: decide whether to promote any candidate wording from the MNEMOSYNE-044 coverage map into `current/human-approved-spec.md`.
- [ ] If user approves promotion, run a separate spec-update task; do not use this coverage map as automatic approval.

Status boundary: final D-01 to D-07 decisions are authoritative checkpoint records, but only content already reflected in `current/human-approved-spec.md` is currently executable. Unreflected promotion candidates require separate user approval.

- MNEMOSYNE-051: DR2 handoff-strategy research ingested as supplemental evidence cycle `RC-2026Q2-handoff-strategy`.
- Review DR2 handoff-strategy implications before updating replay/handoff templates or starting first real target-project dry-run.
