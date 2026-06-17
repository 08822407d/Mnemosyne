# Idea Capture Buffer / 想法捕获缓冲区

## 文件定位

- 本文件是非执行源。
- 当前执行源仍是 `current/human-approved-spec.md`。
- 本文件保存待 triage 的想法、候选需求、弱假设、研究触发点、路线选项。
- 本文件中的内容不是 approved requirements。
- 本文件中的内容不能直接覆盖 spec。
- 本文件应定期整理到 candidate requirements / open questions / decision log / research plan。

## 使用字段

每条 idea 应包含：

- idea_id
- source
- source_type
- captured_at
- short_title
- raw_note
- classification
- confidence
- evidence_needed
- conflicts_or_risks
- proposed_next_action
- target_followup_file
- status
- promotion_condition

## 初始 seed entries

### IDEA-2026-0001

- source: RAW-0054 / MNEMOSYNE-033 user request
- source_type: user_request
- captured_at: 2026-06-16
- short_title: 任意新开对话也能继续 Mnemosyne 建设
- raw_note: 用户希望任意新 ChatGPT / Pro / Codex 对话都能通过仓库继续系统建设，减少上下文丢失。
- classification: `candidate_requirement`
- confidence: high
- evidence_needed: startup / handoff / active-context consistency check
- conflicts_or_risks: 不能把接手便利性扩展为自动写回或执行源变更。
- proposed_next_action: 加强 startup instructions / handoff / idea buffer / continuation checklist。
- target_followup_file: `handoff/startup-instructions.md`; `handoff/handoff-current.md`; `current/active-context.md`
- status: seeded_from_current_route_selection
- promotion_condition: 用户通过 approved workflow 明确批准后，才可进入执行源或更正式流程。

### IDEA-2026-0002

- source: RAW-0054 / MNEMOSYNE-033 user request
- source_type: user_request
- captured_at: 2026-06-16
- short_title: 一个月 Pro 会员高强度建设路线
- raw_note: 用户希望一个月内用 Pro 模型、Pro Deep Research、Codex 尽可能稳固 Mnemosyne 根基。
- classification: `route_option`
- confidence: high
- evidence_needed: 用户优先级、Pro / Deep Research 可用额度、候选路线排序。
- conflicts_or_risks: 不能因为路线紧迫而跳过用户确认或污染执行源。
- proposed_next_action: 建立 1-month roadmap，不直接改执行源。
- target_followup_file: `notes/overall-target-and-roadmap-snapshot.md`; future roadmap task
- status: seeded_from_current_route_selection
- promotion_condition: 用户明确选择路线和节奏。

### IDEA-2026-0003

- source: RAW-0054 / MNEMOSYNE-033 user request
- source_type: user_request
- captured_at: 2026-06-16
- short_title: Pro Deep Research 用于 memory-system testing/debugging feasibility
- raw_note: 当前 Pro 对话余额不足，但可使用 Pro Deep Research；memory-system testing/debugging feasibility 是研究门控候选项。
- classification: `research_gated_item`
- confidence: medium
- evidence_needed: Deep Research prompt、外部最新实践、能力边界复核。
- conflicts_or_risks: Deep Research 结果是 evidence，不是 spec。
- proposed_next_action: 生成 Deep Research prompt / research plan。
- target_followup_file: future research prompt / research plan
- status: captured_pending_triage
- promotion_condition: 研究结果入库、用户 review，并经 approved workflow 处理。

### IDEA-2026-0004

- source: MNEMOSYNE-031 / MNEMOSYNE-032 current route state
- source_type: route_state
- captured_at: 2026-06-16
- short_title: PDF figure/table/image/layout 局部复核
- raw_note: PDF 图表复核仍 pending，不应声称完成。
- classification: `needs_pdf_figure_review`
- confidence: high
- evidence_needed: 人工复核目标、相关报告页面、复核记录。
- conflicts_or_risks: 不得 OCR；不得声称已复核。
- proposed_next_action: 后续按目标项目相关性局部复核。
- target_followup_file: `raw/research-reports/cycles/2026Q2-initial/pdf-figure-review-index.md`
- status: captured_pending_triage
- promotion_condition: 人工复核完成并登记。

### IDEA-2026-0005

- source: MNEMOSYNE-032 PASS route options
- source_type: route_state
- captured_at: 2026-06-16
- short_title: Template review / small fixes
- raw_note: 032 dry-run PASS 后，可复核 self-improvement、target-project memory-system、delivery-manifest、first-scenario selection 模板。
- classification: `route_option`
- confidence: medium
- evidence_needed: 用户选择的 template review scope。
- conflicts_or_risks: 不应把模板 review 当成 spec approval。
- proposed_next_action: 后续 template review task。
- target_followup_file: template pack files / future task record
- status: captured_pending_triage
- promotion_condition: 用户选择模板 review 路线。

### IDEA-2026-0006

- source: MNEMOSYNE-032 PASS route options
- source_type: route_state
- captured_at: 2026-06-16
- short_title: First real target-project scenario selection
- raw_note: 只有用户明确选择目标项目并确认进入试用 / 交付阶段后才能开始。
- classification: `route_option`
- confidence: high
- evidence_needed: 用户选择目标项目、范围、隐私边界和交付位置。
- conflicts_or_risks: 不得提前选择真实外部目标项目或生成交付包。
- proposed_next_action: 暂不执行，等待用户选择。
- target_followup_file: `notes/template-pack-review-and-first-scenario-selection.md`
- status: captured_pending_triage
- promotion_condition: 用户明确确认进入试用 / 交付阶段。

### IDEA-2026-0007

- source: MNEMOSYNE-032 cleanup chain / task authoring guideline
- source_type: tool_process_lesson
- captured_at: 2026-06-16
- short_title: Codex stale-branch / Accept Incoming rollback 作为硬性操作规则
- raw_note: 后续 repo-editing 任务必须新开或刷新到最新 master；冲突 PR 不要 unconditional Accept Incoming。
- classification: `tool_or_process_lesson`
- confidence: high
- evidence_needed: startup / task authoring guideline consistency.
- conflicts_or_risks: 忽略该规则会导致状态文件回滚。
- proposed_next_action: 确保 startup / task authoring guidelines 已记录；本条仅做 buffer 索引。
- target_followup_file: `notes/codex-task-authoring-and-diff-verification-guidelines.md`; `handoff/startup-instructions.md`
- status: seeded_from_current_route_selection
- promotion_condition: 已作为操作经验记录，不直接升级为 spec。

### IDEA-2026-0008

- source: MNEMOSYNE-032 cleanup observations
- source_type: cleanup_observation
- captured_at: 2026-06-16
- short_title: Markdown 长行可读性 cleanup
- raw_note: 部分状态文件可能存在超长行，不阻断语义接手，但影响人工 diff。
- classification: `route_option`
- confidence: medium
- evidence_needed: 后续人工 readability review。
- conflicts_or_risks: 单独 cleanup 可能制造无意义 diff。
- proposed_next_action: 后续 template/status readability cleanup 时处理，不单独开任务。
- target_followup_file: future readability cleanup task
- status: captured_pending_triage
- promotion_condition: 用户选择可读性 cleanup 或相关文件正好进入小修。

## Buffer review cadence

- 每个重要对话或 Codex 任务后，可追加 entries。
- 每隔若干任务做一次 triage。
- triage 后可以移动到 candidate requirements / open questions / decision log。
- 已处理条目不要删除，改状态并保留 trace。

## MNEMOSYNE-033A exported conversation derived insight backfill

All entries in this section are `historical_conversation_derived_insight`. They are not execution source, not final design, and not approved spec. They require triage through idea buffer / candidate requirements / open questions / approved workflow before any execution-source change.

### IDEA-2026-0009

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: 用户不是 Agent 架构专家，需要 Mnemosyne 主动辅助设计
- raw_note: 用户需要系统帮助持续整理、查重、比较和升级设计，而不只是提供静态模板。
- classification: `candidate_requirement`
- confidence: medium
- evidence_needed: 后续 candidate cleanup 与用户确认。
- conflicts_or_risks: 不能直接升级为 spec。
- proposed_next_action: 进入 candidate cleanup；后续模板和 onboarding 中强调 active assistance。
- target_followup_file: `notes/candidate-requirements.md`
- status: captured_pending_triage
- promotion_condition: 用户确认后进入 approved workflow。

### IDEA-2026-0010

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: 用户记忆力不强是系统设计约束
- raw_note: 用户记忆力不强解释了 handoff、idea capture、口语化重述、待重述清单、阶段编号、路线图、任务状态落盘等机制。
- classification: `candidate_requirement`
- confidence: medium
- evidence_needed: 后续 candidate rationale / onboarding rationale。
- conflicts_or_risks: 需要避免过度个人化或未经用户确认的执行源表述。
- proposed_next_action: 进入 candidate rationale / onboarding rationale。
- target_followup_file: `notes/candidate-requirements.md`
- status: captured_pending_triage
- promotion_condition: 用户确认 wording 和适用范围。

### IDEA-2026-0011

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: 系统应持续整理、查重、比较、升级用户断续提出的想法
- raw_note: 用户会断断续续提出需求、反馈和想法，系统应持续管理其演化。
- classification: `candidate_requirement`
- confidence: high
- evidence_needed: 与 idea buffer triage / candidate cleanup / decision workflow 对齐。
- conflicts_or_risks: 不应绕过用户确认直接更新执行源。
- proposed_next_action: 与 idea buffer triage / candidate cleanup / decision workflow 对齐。
- target_followup_file: `notes/candidate-requirements.md`
- status: captured_pending_triage
- promotion_condition: 与既有 self-improvement workflow 查重后由用户确认。

### IDEA-2026-0012

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: 中文优先策略的长期回顾理由
- raw_note: 中文优先不仅是语言偏好，也是为了长期回顾、避免翻译误差、减少双语膨胀；英文保留路径、ID、命令、Git/GitHub、工具名、产品名。
- classification: `candidate_requirement`
- confidence: high
- evidence_needed: 语言策略 candidate cleanup。
- conflicts_or_risks: 与当前 spec 的语言策略基本一致，但理由和边界仍需候选化。
- proposed_next_action: 进入语言策略 candidate cleanup。
- target_followup_file: `notes/candidate-requirements.md`
- status: captured_pending_triage
- promotion_condition: 用户确认是否补充到 approved spec rationale。

### IDEA-2026-0013

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: AI 关键回应也可能需要保存为 raw/context evidence
- raw_note: 用户希望保存的不只是用户原话，也包括影响后续构想演化的 AI 关键分析和建议。
- classification: `raw_idea`
- confidence: medium
- evidence_needed: raw 保存粒度、隐私和冗余控制规则。
- conflicts_or_risks: 可能带来体积、隐私、重复和过时上下文污染风险。
- proposed_next_action: 研究 raw 保存粒度与隐私 / 冗余控制。
- target_followup_file: `current/open-questions.md`; `notes/candidate-requirements.md`
- status: captured_pending_triage
- promotion_condition: 用户确认保存粒度策略。

### IDEA-2026-0014

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: 三周压缩版 Pro 根基加固路线
- raw_note: 普通 Pro 对话和 Pro Deep Research 额度共享，实际剩余时间从一月路线压缩为三周。
- classification: `route_option`
- confidence: medium
- evidence_needed: 用户当前 Pro / Deep Research 额度和优先级。
- conflicts_or_risks: 额度和 UI 会变化，不能写成长期事实或执行源。
- proposed_next_action: 更新 route planning view；不直接改 spec。
- target_followup_file: `notes/overall-target-and-roadmap-snapshot.md`
- status: captured_pending_triage
- promotion_condition: 用户确认路线优先级。

### IDEA-2026-0015

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: 普通 ChatGPT + GitHub 新对话作为 onboarding rehearsal
- raw_note: 关联仓库的普通 ChatGPT 新对话可作为只读接手、路线复核、任务分流和接手能力验证入口。
- classification: `route_option`
- confidence: medium
- evidence_needed: 后续 fresh conversation onboarding rehearsal 结果。
- conflicts_or_risks: 不应替代 repo diff 验证或执行源。
- proposed_next_action: 后续 fresh conversation onboarding rehearsal 可使用该模式。
- target_followup_file: `handoff/handoff-current.md`; `notes/overall-target-and-roadmap-snapshot.md`
- status: captured_pending_triage
- promotion_condition: 用户选择演练路线并确认边界。

### IDEA-2026-0016

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: Codex 任务内容文件化交付标准化
- raw_note: 长任务、复杂任务、含 code fence 的任务应优先文件化或使用精确替换块，避免复制截断。
- classification: `tool_or_process_lesson`
- confidence: high
- evidence_needed: Codex task authoring guideline cleanup。
- conflicts_or_risks: 需决定是全局硬规则还是高风险任务规则。
- proposed_next_action: 进入 Codex task authoring guideline candidate cleanup。
- target_followup_file: `current/open-questions.md`; `notes/candidate-requirements.md`
- status: captured_pending_triage
- promotion_condition: 用户确认适用范围。

### IDEA-2026-0017

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: 每个阶段任务开头编号
- raw_note: 用户会中途切换事务，任务开头编号可降低忘记当前任务状态的风险。
- classification: `tool_or_process_lesson`
- confidence: medium
- evidence_needed: task authoring convention review。
- conflicts_or_risks: 编号应辅助记忆，不应替代仓库状态。
- proposed_next_action: 进入 task authoring convention。
- target_followup_file: `notes/candidate-requirements.md`
- status: captured_pending_triage
- promotion_condition: 与现有任务编号规则查重后确认。

### IDEA-2026-0018

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: Codex Cloud 文件上传失败时的 text-paste fallback
- raw_note: 文件上传失败时需有可复制粘贴的 fallback，避免任务中断。
- classification: `tool_or_process_lesson`
- confidence: medium
- evidence_needed: Codex operational fallback candidate。
- conflicts_or_risks: text-paste fallback 仍需避免 code fence 截断。
- proposed_next_action: 进入 Codex operational fallback candidate。
- target_followup_file: `notes/candidate-requirements.md`
- status: captured_pending_triage
- promotion_condition: 用户确认操作约定。

### IDEA-2026-0019

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: 模型能力差异与工作分工需要动态核实
- raw_note: Custom GPT、普通对话、Pro 强度、Codex Cloud 模型选择等 UI 和能力会变化，应实时核实。
- classification: `open_question`
- confidence: high
- evidence_needed: 当前官方产品状态和用户实际 UI。
- conflicts_or_risks: 不要写成长期固定事实。
- proposed_next_action: 进入 open questions；不要写成长期固定事实。
- target_followup_file: `current/open-questions.md`
- status: captured_pending_triage
- promotion_condition: 作为动态事实按需核实。

### IDEA-2026-0020

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: 完整对话导出只作本地背景，是否入库需另行决策
- raw_note: 完整导出记录有历史价值，但存在隐私、体积、重复污染、可检索性和过时任务风险。
- classification: `open_question`
- confidence: high
- evidence_needed: 用户隐私边界、选摘策略和仓库体积策略。
- conflicts_or_risks: 默认不完整入库，避免污染与隐私风险。
- proposed_next_action: 进入 open questions；默认不完整入库。
- target_followup_file: `current/open-questions.md`
- status: captured_pending_triage
- promotion_condition: 用户明确确认入库范围。

### IDEA-2026-0021

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: 研究报告主要供元 Agent 使用，用户不必通读
- raw_note: 研究报告作为高权重证据层，用于让元 Agent 评价用户构想是否可行、过时或有更现代方案。
- classification: `candidate_requirement`
- confidence: high
- evidence_needed: research evidence usage cleanup。
- conflicts_or_risks: 不得声称用户已通读报告或 PDF 图表已复核。
- proposed_next_action: 进入 research evidence usage / template candidate cleanup。
- target_followup_file: `notes/candidate-requirements.md`
- status: captured_pending_triage
- promotion_condition: 用户确认是否进入 approved rationale。

### IDEA-2026-0022

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: 用户口语化重述前应由 AI 生成待重述清单
- raw_note: 031 已完成一次该流程，但可成为未来目标项目 intake 的通用机制候选。
- classification: `candidate_requirement`
- confidence: medium
- evidence_needed: target-project intake template review。
- conflicts_or_risks: 031 流程成功不等于所有场景通用。
- proposed_next_action: 进入 target-project intake template review。
- target_followup_file: `notes/candidate-requirements.md`
- status: captured_pending_triage
- promotion_condition: template review 后由用户确认。

### IDEA-2026-0023

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: 原文—候选—查重—人类确认—实施版链路
- raw_note: 新想法不一定比旧想法更好，必须查重后由用户决定实施版写法。
- classification: `candidate_requirement`
- confidence: high
- evidence_needed: candidate lifecycle / approved workflow cleanup。
- conflicts_or_risks: 与现有 self-improvement workflow 需查重合并。
- proposed_next_action: 进入 candidate lifecycle / approved workflow cleanup。
- target_followup_file: `notes/candidate-requirements.md`
- status: captured_pending_triage
- promotion_condition: 与现有 workflow 对齐后确认。

### IDEA-2026-0024

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: dry-run / independent verification 机制模板化
- raw_note: 032 PASS 证明一次流程可行，但是否将验证性 dry-run 设计为未来通用模板仍需整理。
- classification: `candidate_requirement`
- confidence: medium
- evidence_needed: template review / verification workflow candidate。
- conflicts_or_risks: 单次 PASS 不是通用机制批准。
- proposed_next_action: 进入 template review / verification workflow candidate。
- target_followup_file: `notes/candidate-requirements.md`
- status: captured_pending_triage
- promotion_condition: 用户确认是否模板化。

### IDEA-2026-0025

- source: RAW-0055 / MNEMOSYNE-033A
- source_type: historical_conversation_derived_insight
- captured_at: 2026-06-16
- short_title: 任务结果记录保存范围
- raw_note: 是否只保存有警告、限制、失败、未完成、人工复核需求的精简记录，而不是保存所有 Codex 完成回复。
- classification: `open_question`
- confidence: medium
- evidence_needed: result-record policy cleanup。
- conflicts_or_risks: 保存过多会污染，保存过少会丢失审计线索。
- proposed_next_action: 进入 open questions / result-record policy cleanup。
- target_followup_file: `current/open-questions.md`; `notes/candidate-requirements.md`
- status: captured_pending_triage
- promotion_condition: 用户确认任务结果记录策略。

### IDEA-2026-0026

- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
- source_type: user_supplemental_explanation
- captured_at: 2026-06-17
- short_title: Prototype-stage Mnemosyne construction understanding
- raw_note: Mnemosyne is currently a prototype-stage exploratory system aiming to establish a usable external persistent memory framework; maturity should come through real target-project use, observed failures, and feedback rather than premature perfect architecture.
- classification: `candidate_requirement` / `design_rationale`
- confidence: high
- evidence_needed: target-project dry-runs and observed memory-system failure records.
- conflicts_or_risks: Could be misread as permission for careless execution; must remain bounded by `current/human-approved-spec.md`.
- proposed_next_action: Deduplicate against existing construction rationale and decide whether any wording belongs in future approved rationale.
- target_followup_file: `notes/candidate-requirements.md`; `current/open-questions.md`
- status: captured_pending_triage
- promotion_condition: User confirms the formulation after deduplication and conflict review.

### IDEA-2026-0027

- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
- source_type: user_supplemental_explanation
- captured_at: 2026-06-17
- short_title: Ordinary ChatGPT to Codex repository writeback loop
- raw_note: Ordinary ChatGPT discussions are read-only for repositories but may generate strict Codex tasks; Codex performs reviewed repository writes through PRs, followed by user review/merge and possible read-only verification.
- classification: `tool_or_process_lesson` / `candidate_requirement`
- confidence: high
- evidence_needed: Review against current Codex task authoring guidance and repository workflow notes.
- conflicts_or_risks: "Do not write the repository in this conversation" could be overgeneralized to block Codex task generation.
- proposed_next_action: Consider adding a workflow clarification to future process guidance if approved.
- target_followup_file: `notes/candidate-requirements.md`; `handoff/handoff-current.md`
- status: captured_pending_triage
- promotion_condition: User confirms this should become stable workflow guidance.

### IDEA-2026-0028

- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
- source_type: user_supplemental_explanation
- captured_at: 2026-06-17
- short_title: Evidence-guided self-improvement
- raw_note: Mnemosyne should improve through self-use and project feedback plus periodic deep research and current best practices; agents should map research findings to open questions, failure modes, target-project feedback, template gaps, capability boundaries, and outdated assumptions.
- classification: `candidate_requirement` / `research_gated_item`
- confidence: high
- evidence_needed: Research-to-improvement cadence and mapping template validation.
- conflicts_or_risks: Research evidence must not be promoted directly into execution source or override human-approved spec.
- proposed_next_action: Triage into research evidence usage and self-improvement workflow cleanup.
- target_followup_file: `notes/candidate-requirements.md`; `current/open-questions.md`
- status: captured_pending_triage
- promotion_condition: User approves the research-to-improvement loop and its safeguards.

### IDEA-2026-0029

- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
- source_type: user_supplemental_explanation
- captured_at: 2026-06-17
- short_title: Human-readable basis materials vs agent-operational artifacts
- raw_note: Mnemosyne should distinguish human-readable basis materials that preserve intent and reviewability from agent-operational artifacts designed for later agents to load, follow, transform, or verify reproducibly.
- classification: `candidate_requirement` / `design_rationale`
- confidence: high
- evidence_needed: Artifact inventory review and verification criteria for agent-operational files.
- conflicts_or_risks: Operational artifacts may be mistaken for deterministic machine code or silently reinterpreted by later agents.
- proposed_next_action: Add to candidate cleanup and open questions about artifact verification.
- target_followup_file: `notes/candidate-requirements.md`; `current/open-questions.md`
- status: captured_pending_triage
- promotion_condition: User confirms the boundary and lifecycle implications.

### IDEA-2026-0030

- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
- source_type: user_supplemental_explanation
- captured_at: 2026-06-17
- short_title: HADB terminology
- raw_note: Human-Approved Design Basis (HADB), Chinese 人类确认设计依据稿, names a settled human-readable design-basis text formed after discussion, contradiction resolution, feasibility analysis, research-evidence checking, and user confirmation; it is not raw record and not automatically execution source.
- classification: `candidate_requirement`
- confidence: high
- evidence_needed: Lifecycle review against raw records, candidate requirements, and execution-source promotion rules.
- conflicts_or_risks: HADB could be confused with approved spec unless its non-execution-source boundary is explicit.
- proposed_next_action: Triage HADB terminology and lifecycle into candidate cleanup.
- target_followup_file: `notes/candidate-requirements.md`; `current/open-questions.md`
- status: captured_pending_triage
- promotion_condition: User confirms terminology, Chinese label, and lifecycle rules.

### IDEA-2026-0031

- source: current ChatGPT conversation / MNEMOSYNE-036 preparation
- source_type: user_supplemental_explanation
- captured_at: 2026-06-17
- short_title: Indexing as research-gated performance optimization
- raw_note: The user's index idea comes from PC hardware / operating-system / file-system analogies and has not been verified for AI agent external memory; it should be treated as a research-gated retrieval acceleration candidate, not a core Mnemosyne requirement.
- classification: `research_gated_item` / `performance_optimization_candidate` / `weak_or_outdated_assumption`
- confidence: high
- evidence_needed: Evidence that indexing improves agent retrieval without stale or misleading authority risks.
- conflicts_or_risks: Stale indexes, misleading indexes, and agents treating indexes as authority rather than retrieval aids.
- proposed_next_action: Keep as research-gated candidate until memory scale and retrieval failure evidence justify evaluation.
- target_followup_file: `notes/candidate-requirements.md`; `current/open-questions.md`
- status: captured_pending_triage
- promotion_condition: Research evidence and user confirmation support a specific indexing mechanism.
