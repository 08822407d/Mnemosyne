# Idea Capture Triage Rules / 想法捕获与分流规则

## 文件定位

- 本文件不是执行源。
- 当前执行源仍是 `current/human-approved-spec.md`。
- 本文件定义新想法如何进入缓冲区并经过 triage。
- 本文件不批准任何 candidate requirement。
- 本文件不把任何想法升级为 spec。

## 为什么需要 Idea Capture Buffer

- 新想法会出现在普通 ChatGPT、GPT-5.5 Pro、Pro Deep Research、Codex、verification、dry-run 中。
- 当前上下文巨大，新想法如果不入库会丢失。
- 新想法如果直接进入 spec 会污染执行源。
- buffer 层承接“还没被审查的新内容”。

## 分类

- `raw_idea`: 尚未整理的新想法或片段。
- `candidate_requirement`: 可能成为候选需求，但尚未获批。
- `open_question`: 需要用户、证据或后续任务回答的问题。
- `research_gated_item`: 需要外部最新实践、研究证据或能力边界支撑的项目。
- `possible_conflict`: 可能与执行源、既有候选、研究证据或边界冲突的内容。
- `weak_or_outdated_assumption`: 可能过时、过弱或未验证的前提。
- `speculative_long_term_direction`: 长期设想或远期方向，当前不应直接实施。
- `route_option`: 当前或后续路线选择。
- `tool_or_process_lesson`: 工具使用、流程、失败模式或操作经验。
- `do_not_upgrade_to_spec`: 明确不能升级为 spec 的内容或警戒项。
- `needs_user_decision`: 需要用户明确选择或批准。
- `needs_research_refresh`: 需要新研究周期或 delta report。
- `needs_pdf_figure_review`: 需要 PDF figure/table/image/layout 人工复核。
- `needs_codex_task`: 需要单独 Codex repo-editing 或验证任务。
- `needs_pro_review`: 需要 GPT Pro / 强模型复核、重述或方案评估。

## 升级规则

1. `raw_idea` 只能先进入 idea buffer。
2. `raw_idea` 经整理后可进入 candidate requirements，但不能直接进入 `human-approved-spec.md`。
3. 有冲突或不确定的内容进入 open questions。
4. 需要外部最新实践支撑的内容进入 research-gated item。
5. 只有用户明确批准后，才可以进入 decision log。
6. 只有通过明确 approved workflow，才可能更新 `current/human-approved-spec.md`。
7. 用户口语化构想不能直接成为执行源。
8. Deep Research 结果是 evidence，不是 spec。
9. Codex result record 是 audit trail，不是 spec。
10. Dry-run PASS 是 validation evidence，不是 final design。

## 新对话使用规则

新开 ChatGPT / Pro / Codex 对话遇到新想法时：

- 先记录 source；
- 标记 classification；
- 标记 confidence；
- 标记 evidence_needed；
- 标记 proposed_next_action；
- 不要直接更新 execution source；
- 若不确定，放入 open question。

## 禁止项

- 不得修改研究报告原件。
- 不得编造缺失 light prompts。
- 不得声称 PDF 图表已复核。
- 不得创建 AGENTS.md / CLAUDE.md / automation，除非明确授权。
- 不得把 buffer 中内容当作 user-approved design。
