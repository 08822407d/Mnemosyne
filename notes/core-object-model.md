# Core Object Model / 核心对象模型

这是 Mnemosyne 当前阶段的核心对象模型草案，用于统一后续文件、模板、handoff、查重和交付设计。

> 说明：本文件是阶段性草案，不代表最终稳定规范。

## 1) Idea Capture Item
- 用途：记录临时粗糙点子，避免想法丢失。
- 是否是执行源：否。
- 是否需要用户确认：通常不需要，升级前需要。
- 典型字段：`idea_id`、`title`、`content`、`created_at`、`source_refs`、`status`。
- 典型状态：`todo`、`deferred`。
- 与其他对象关系：可转化为 `Candidate Requirement`，可被 `Similarity / Conflict Report` 引用。
- 当前阶段是否实现：否（未来 TODO）。

## 2) Raw Record
- 用途：保存原始输入、反馈、交接和讨论材料。
- 是否是执行源：否（证据源）。
- 是否需要用户确认：不需要逐条确认，但写入应可追溯。
- 典型字段：`raw_id`、`source_type`、`status`、`sensitivity`、`language`、`created_at`、`source_refs`。
- 典型状态：`preserved`、`superseded`、`sensitive`、`archived`。
- 与其他对象关系：一个 `Raw Record` 可产生多个 `Candidate Requirement`；可被 `Decision Record`、`Human-Approved Spec Entry` 引用。
- 当前阶段是否实现：是（已以 raw 文档形式使用）。

## 3) Candidate Requirement
- 用途：从 raw 或其他证据整理出的候选需求。
- 是否是执行源：否（候选层）。
- 是否需要用户确认：需要，确认后才可能进入实施版。
- 典型字段：`candidate_id`、`title`、`description`、`source_refs`、`status`、`related_items`、`conflicts_with`、`supersedes`。
- 典型状态：`pending`、`reflected`、`rejected`、`deferred`、`merged`、`superseded`。
- 与其他对象关系：引用 `Raw Record`；可被 `Similarity / Conflict Report` 比较；可进入 `Human-Approved Spec Entry`。
- 当前阶段是否实现：是（已在 notes 中维护）。

## 4) Similarity / Conflict Report
- 用途：输出新输入与历史对象的相似/冲突分析。
- 是否是执行源：否。
- 是否需要用户确认：需要用户审阅其建议。
- 典型字段：`report_id`、`input_item`、`related_items`、`similar_points`、`differences`、`conflicts_with`、`merge_suggestions`、`status`。
- 典型状态：`pending`、`deferred`（状态体系待定）。
- 与其他对象关系：输入常来自 `Raw Record`/`Candidate Requirement`；比对对象包括 `Candidate Requirement`、`Human-Approved Spec Entry`、`Decision Record`、`Open Question`、`TODO Item`。
- 当前阶段是否实现：否（仅原则定义）。

## 5) Human-Approved Spec Entry
- 用途：记录当前真正执行的需求、原则、约束或规则。
- 是否是执行源：是。
- 是否需要用户确认：是（必须）。
- 典型字段：`spec_entry_id`、`statement`、`source_refs`、`candidate_refs`、`status`、`approved_at`、`supersedes`。
- 典型状态：`active`、`deprecated`、`replaced`、`review_on_model_upgrade`。
- 与其他对象关系：由 `Candidate Requirement` + `Raw Record` 追溯而来；可被 `Decision Record` 解释。
- 当前阶段是否实现：是（以 `current/human-approved-spec.md` 形式存在）。

## 6) Decision Record
- 用途：解释为什么接受/拒绝/延期某方案。
- 是否是执行源：否（解释层）。
- 是否需要用户确认：建议需要。
- 典型字段：`decision_id`、`decision`、`rationale`、`status`、`source_refs`、`related_items`。
- 典型状态：`accepted`、`deferred`、`rejected`、`superseded`。
- 与其他对象关系：解释 `Human-Approved Spec Entry`、`TODO Item`、`rejected alternatives`。
- 当前阶段是否实现：是（已在 notes 中维护）。

## 7) Open Question
- 用途：记录未决问题与待确认事项。
- 是否是执行源：否。
- 是否需要用户确认：通常需要。
- 典型字段：`question_id`、`question`、`status`、`owner`、`related_items`。
- 典型状态：`open`、`answered`、`deferred`、`blocked`。
- 与其他对象关系：可触发 `TODO Item` 或新 `Candidate Requirement`。
- 当前阶段是否实现：是（`current/open-questions.md`）。

## 8) TODO Item
- 用途：记录明确延期但未来要做的事项。
- 是否是执行源：否。
- 是否需要用户确认：建议需要。
- 典型字段：`todo_id`、`task`、`status`、`priority`、`related_items`。
- 典型状态：`todo`、`in_progress`、`blocked`、`done`、`deferred`。
- 与其他对象关系：可由 `Candidate Requirement`、`Decision Record`、`Open Question` 派生。
- 当前阶段是否实现：是（`current/todo.md`）。

## 9) Handoff
- 用途：给未来 AI 会话快速恢复状态的短上下文。
- 是否是执行源：否。
- 是否需要用户确认：建议需要。
- 典型字段：`handoff_id`、`current_goal`、`confirmed_principles`、`next_steps`、`source_refs`。
- 典型状态：`active`、`superseded`（状态体系待定）。
- 与其他对象关系：引用 `Active Context`、`Human-Approved Spec Entry`、主要 `Open Question`；不复制完整历史。
- 当前阶段是否实现：是（`handoff/handoff-current.md`）。

## 10) Model-Specific Digest
- 用途：面向不同模型/工具生成压缩视图与迁移辅助摘要。
- 是否是执行源：否。
- 是否需要用户确认：需要（高风险信息压缩）。
- 典型字段：`digest_id`、`target_model`、`source_refs`、`summary`、`status`。
- 典型状态：`todo`、`deferred`。
- 与其他对象关系：可引用 `Raw Record`、`Candidate Requirement`、`Decision Record`、`Human-Approved Spec Entry`。
- 当前阶段是否实现：否（未来对象）。

## 11) Delivery Manifest
- 用途：记录面向具体目标项目的交付版本、目标路径与限制条件。
- 是否是执行源：否（交付追踪层）。
- 是否需要用户确认：需要。
- 典型字段：`delivery_id`、`target_project`、`version`、`source_refs`、`status`、`assumptions`、`unsupported_items`。
- 典型状态：`todo`、`deferred`。
- 与其他对象关系：未来应引用 `Human-Approved Spec Entry`、设计文档与目标项目路径。
- 当前阶段是否实现：否（未来对象）。


## 模型与模板规则的关系（阶段说明）

- `notes/core-object-model.md` 负责定义对象含义与关系边界。
- `notes/object-templates-and-id-rules.md` 负责定义对象填写模板、ID 规则、状态值与 `source_refs` 草案。
- 当前模板与规则均为草案，后续可根据实践反馈调整。


## 对象、模板与流程文档分工（阶段说明）

- `notes/core-object-model.md`：定义对象含义与关系边界。
- `notes/object-templates-and-id-rules.md`：定义对象模板、ID、状态值与 source_refs 草案。
- `notes/requirement-intake-workflow.md`：定义对象如何从输入进入候选需求，并在用户确认后进入实施版。


## 对象、模板、流程与交接回顾文档分工（阶段说明）

- `notes/core-object-model.md`：定义对象。
- `notes/object-templates-and-id-rules.md`：定义模板、ID 和状态。
- `notes/requirement-intake-workflow.md`：定义新需求进入流程。
- `notes/handoff-active-context-review.md`：定义未来会话如何接手和阶段性回顾机制。


## 模型迁移与约束生命周期补充（阶段说明）

- Model-Specific Digest 当前仍是未来对象。
- Constraint 可作为未来独立对象，或作为 Decision / Spec 的附属对象管理。
- 模型迁移机制记录在 `notes/model-migration-and-constraint-lifecycle.md`。
- 模型迁移不会改变“Human-Approved Spec Entry 是执行源”的原则。


## 面向目标项目交付补充（阶段说明）

- Delivery Manifest 当前仍属于未来正式对象，但第九阶段已开始定义其用途。
- Target Project Memory Package 可作为未来交付对象。
- Memory System Design Spec 是 Mnemosyne 面向具体项目输出的核心设计文档。
- 交付后目标项目运行文件是该目标项目的运行真相源。
- 相关流程记录在 `notes/delivery-package-workflow.md`。
