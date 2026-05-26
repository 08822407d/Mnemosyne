# Object Templates and ID Rules / 对象模板与 ID 规则

这是 Mnemosyne 当前阶段的对象模板和 ID / 状态规则草案，用于支持手工维护、Codex 小步写入和未来自动化扩展。

> 说明：本文件是草案，不是最终不可变规范。

## 全局规则

- 正文以中文为主。
- 文件名、ID、状态值、YAML key 可使用英文。
- 所有派生对象尽量保留 `source_refs`。
- 模板用于统一写法与审阅，不代表自动化系统已实现。
- 当前不实现自动化校验。

## ID 前缀表（草案）

| 前缀 | 对象 | 示例 | 当前阶段是否启用 | 备注 |
|---|---|---|---|---|
| IDEA | Idea Capture Item | IDEA-0001 | 否 | 未来对象 |
| RAW | Raw Record | RAW-0005 | 是 | 原文证据层 |
| CAND | Candidate Requirement | CAND-0027 | 是 | 候选层 |
| SIM | Similarity / Conflict Report | SIM-0001 | 部分 | 仅定义模板与规则 |
| SPEC | Human-Approved Spec Entry | SPEC-0001 | 部分 | 概念启用，模板草案 |
| DEC | Decision Record | DEC-0020 | 是 | 决策解释层 |
| OQ | Open Question | OQ-0001 | 部分 | 当前以列表方式维护 |
| TODO | TODO Item | TODO-0001 | 部分 | 当前以列表方式维护 |
| HOFF | Handoff | HOFF-0001 | 部分 | 当前以 handoff-current 形式维护 |
| DIGEST | Model-Specific Digest | DIGEST-0001 | 否 | 未来对象 |
| DELIV | Delivery Manifest | DELIV-0001 | 否 | 未来对象 |

## 状态值表（草案）

- Raw Record：`preserved`、`archived`、`superseded`、`sensitive`
- Candidate Requirement：`pending`、`reflected`、`rejected`、`deferred`、`merged`、`superseded`
- Similarity / Conflict Report：`draft`、`reviewed`、`resolved`、`deferred`
- Human-Approved Spec Entry：`active`、`deprecated`、`replaced`、`review_on_model_upgrade`
- Decision Record：`accepted`、`deferred`、`rejected`、`superseded`
- Open Question：`open`、`answered`、`deferred`、`blocked`
- TODO Item：`todo`、`in_progress`、`blocked`、`done`、`deferred`
- Handoff：`current`、`archived`、`superseded`

## 对象模板草案

### 1) Raw Record（非执行源）

```yaml
id: RAW-0000
title: <原文记录标题>
status: preserved
source_refs: []
recorded_at: YYYY-MM-DD
summary: <该原文记录的简短说明>
notes: <补充说明，未定可写 TODO>
execution_source: false
```

### 2) Candidate Requirement（非执行源）

```yaml
id: CAND-0000
title: <候选需求标题>
status: pending
source_refs:
  - RAW-0000
created_at: YYYY-MM-DD
summary: <候选需求摘要>
notes: <补充说明>
execution_source: false
```

### 3) Similarity / Conflict Report（非执行源）

```yaml
id: SIM-0000
title: <查重与冲突报告标题>
status: draft
source_refs:
  - RAW-0000
  - CAND-0000
created_at: YYYY-MM-DD
statement: <本次比对结论摘要>
notes: <相同点/差异点/冲突点/合并建议>
execution_source: false
```

### 4) Human-Approved Spec Entry（执行源）

```yaml
id: SPEC-0000
title: <实施版条目标题>
status: active
source_refs:
  - CAND-0000
  - RAW-0000
approved_at: YYYY-MM-DD
statement: <当前执行规则>
notes: <变更说明与边界>
execution_source: true
```

### 5) Decision Record（非执行源）

```yaml
id: DEC-0000
title: <决策标题>
status: accepted
source_refs:
  - RAW-0000
  - CAND-0000
recorded_at: YYYY-MM-DD
summary: <决策与理由摘要>
notes: <接受/拒绝/延期原因>
execution_source: false
```

### 6) Open Question（非执行源）

```yaml
id: OQ-0000
title: <开放问题标题>
status: open
source_refs:
  - CAND-0000
created_at: YYYY-MM-DD
statement: <问题描述>
notes: <阻塞点/待确认人>
execution_source: false
```

### 7) TODO Item（非执行源）

```yaml
id: TODO-0000
title: <延期任务标题>
status: todo
source_refs:
  - DEC-0000
created_at: YYYY-MM-DD
summary: <任务摘要>
notes: <阶段边界与完成条件>
execution_source: false
```

### 8) Handoff（非执行源）

```yaml
id: HOFF-0000
title: <交接标题>
status: current
source_refs:
  - current/active-context.md
  - current/human-approved-spec.md
recorded_at: YYYY-MM-DD
summary: <当前阶段概览>
notes: <下一步建议，不复制完整历史>
execution_source: false
```

## 未来对象占位

- Idea Capture Item：仅占位，当前阶段不实现。
- Model-Specific Digest：仅占位，当前阶段不实现。
- Delivery Manifest：仅占位，当前阶段不实现。

## 执行源说明

- 只有 Human-Approved Spec Entry 是执行源。
- Raw Record、Candidate Requirement、Similarity Report、Decision Record、Open Question、TODO、Handoff 都不是执行源。


## 与需求进入流程相关的字段建议（草案）

> 说明：以下字段为建议项，当前不要求自动校验。

### Candidate Requirement 可补充字段
- `intake_step`
- `proposed_action`
- `needs_similarity_check`
- `user_decision`

### Similarity / Conflict Report 可补充字段
- `new_item_ref`
- `compared_items`
- `relation_type`
- `difference_summary`
- `proposed_action`
- `user_decision`

### Human-Approved Spec Entry 可补充字段
- `approved_from`
- `approval_decision`
- `approved_at`
- `supersedes`
- `replaces`
- `merged_from`


## Handoff 与 Active Context 字段建议（草案）

### Handoff 建议字段
- `handoff_id`
- `status`
- `created_at`
- `current_stage`
- `current_goal`
- `accepted_principles`
- `execution_source_refs`
- `important_context_refs`
- `deferred_items`
- `next_step`
- `cautions`

### Active Context 建议字段
- `current_stage`
- `current_goal`
- `current_focus`
- `recently_completed`
- `current_constraints`
- `next_step`
- `relevant_files`
- `last_updated`

说明：
- Active Context 可以不作为正式对象编号管理，也可以未来再决定。
- 当前不实现自动更新。


## 模型迁移与约束相关 ID/字段建议（草案）

- `CONSTRAINT-0001` 或 `CST-0001`：约束条目（未来对象，当前未正式启用）。
- `MIG-0001`：模型迁移记录（未来对象，当前未正式启用）。
- `DIGEST-0001`：模型专用摘要（未来对象，当前未正式启用）。

说明：以上 ID 前缀当前只是候选，未来在模板阶段再确认。

Constraint 条目可选字段：
- `constraint_id`
- `status`
- `applies_to`
- `review_trigger`
- `source_refs`
- `rationale`
- `replaced_by`


## Delivery Manifest 相关候选字段（草案）

- `delivery_id`
- `target_project`
- `target_project_type`
- `delivery_version`
- `source_design_refs`
- `generated_at`
- `target_paths`
- `included_files`
- `excluded_items`
- `unsupported_assumptions`
- `manual_steps_required`
- `review_required`
- `post_delivery_notes`

## 交付与漂移相关候选 ID（草案）

- `DELIV-0001`：Delivery Manifest（未来对象）。
- `MSD-0001`：Memory System Design Spec（未来对象）。
- `DRIFT-0001`：Drift Review 记录（未来对象）。

说明：以上 ID 当前仅为候选，未来模板阶段再确认。
