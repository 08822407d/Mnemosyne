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
