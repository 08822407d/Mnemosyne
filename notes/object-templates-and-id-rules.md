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

### 0) 共享硬约束块（非执行源）

以下结构只把 `current/human-approved-spec.md` 已批准的 S1、S2、S4 约束转换为可复用的下游模板。它们不创建新的执行源、对象 ID 类型、隐私分类、自动校验器或平台能力承诺。

#### Repository capture 安全预检

```yaml
repository_capture_safety_preflight:
  preflight_id:
  source_contract_refs:
    - current/human-approved-spec.md §14
    - current/human-approved-spec.md §16
  checked_at:
  checked_by:
  repository_visibility_evidence_ref:
  current_repository_visibility: public | private | unknown
  source_or_material_ref:
  material_sensitivity_evidence_refs: []
  material_sensitivity_assessed: true | false
  contains_credentials_or_secrets: true | false | unknown
  contains_personal_private_customer_or_confidential_data: true | false | unknown
  intended_repository_path:
  storage_route: repository_original | repository_redacted_excerpt | repository_safe_pointer | outside_git
  redaction_or_pointer_safety_checked: true | false | not_applicable
  git_history_persistence_acknowledged: true | false | not_applicable
  residual_risk:
  result: pass | blocked | incomplete
```

规则：

- `current_repository_visibility` 表示在 `checked_at` 依据 `repository_visibility_evidence_ref` 验证或观察到的状态；`public` 或 `unknown` 一律采用 public-risk treatment；
- `source_or_material_ref` 与 `material_sensitivity_evidence_refs` 必须足以界定本次被检查的材料；安全关键证据缺失、未知或相互矛盾时必须 fail closed，结果只能是 `blocked` 或 `incomplete`；
- credentials、secrets、access tokens 或等价认证材料始终产生 `result: blocked`；
- `repository_original` 仅在完整预检为 `pass` 时可用；`repository_redacted_excerpt` 和 `repository_safe_pointer` 仅允许保存已经单独筛查的对应内容；unsafe original 必须使用 `outside_git`；
- `git_history_persistence_acknowledged: not_applicable` 仅在 `storage_route: outside_git` 且没有任何 repository storage route 时可用；
- 后续移动或删除文件不能消除既有 Git 历史暴露。

#### 机械 no-write 证据

```yaml
no_write_evidence:
  evidence_id:
  source_contract_refs:
    - current/human-approved-spec.md §19
  checked_at:
  proof_actor_or_process:
  claim_surfaces:
    - surface: target_repository | target_runtime_store | mnemosyne_repository | local_sandbox | other
      repository_or_target:
      prohibited_write_scope:
      allowed_nonpersistent_outputs: []
      pinned_pre_ref:
      pinned_post_ref:
      mechanical_method:
      mechanical_evidence_refs: []
      mechanical_commands_or_api_results: []
      changed_paths: []
      scope_match: exact | partial | mismatch | unknown
      result: pass | pass_with_approved_exception | blocked | incomplete | contradicted
      approved_exception_ref:
      limitations: []
  overall_result: pass | pass_with_approved_exception | blocked | incomplete | contradicted
```

```yaml
no_write_evidence_exception:
  exception_id:
  approval_ref:
  approved_at:
  approver:
  exact_run:
  exact_scope:
  default_proof_unavailable_reason:
  substitute_evidence_refs: []
  confidence:
  user_independently_verified: true | false | unknown
  not_future_precedent: true
```

规则：

- 每项 no-write 主张必须列出一个或多个明确 `claim_surfaces`；不得用 `repository_and_target_no_write` 一类 blanket scope 代替 surface-specific claim；
- `mechanical_method` 的文字说明本身不是机械证明；`pass` 需要与 pinned refs、exact scope 和 `mechanical_evidence_refs` 或 `mechanical_commands_or_api_results` 绑定；
- `scope_match: mismatch`、`unknown`，或只验证了部分 scope 而未明确降级时，必须 fail closed；
- `pass_with_approved_exception` 只有在 `approved_exception_ref` 指向字段完整、已批准且 exact run / exact scope 匹配的 exception 时才成立；默认机械证明不可用但完整 exception 已获批准时，不得仅因默认方法不可用而判定为 blocked；
- exception 缺失、未批准、字段不完整或 scope 不匹配时，结果保持 `blocked` 或 `incomplete`；exception 只适用于所列 run，不构成未来先例；
- `overall_result` 必须采用不夸大证据的保守汇总；synthetic smoke test、tabletop exercise、real no-write run、delivery 与 target write 仍是不同对象或阶段。

#### Repository action context

```yaml
repository_action_context:
  action_context_id:
  source_contract_refs:
    - current/human-approved-spec.md §18
    - current/run-context-and-pr-provenance-guard.md
  action_surface: mnemosyne_repository | target_repository | target_runtime_store | local_artifact_surface | other
  repository_or_target:
  branch_or_ref:
  paths: []
  protected_paths: []
  target_workspace_material_write_boundary:
  action_type:
  platform_permission:
    status: sufficient | insufficient | unknown | not_applicable
    evidence_refs: []
  mnemosyne_task_authority:
    status: authorized | not_authorized | unknown | not_applicable
    decision_ref:
    authorized_actions: []
    excluded_actions: []
    evidence_refs: []
    expires_with_task: true
    not_future_precedent: true
  action_risk: read_only | low_scope_write | high_scope_or_sensitive_write
  result_record_required: true | false
  related_action_context_refs: []
```

规则：

- 一个 `repository_action_context` 只描述一个 surface 上的一项有边界 action；target read-only、单独获批的 Mnemosyne evidence write 与 local artifact generation 必须分别记录，不得捆绑成一个权限结论；
- app connection、action availability、approval card 或 persistent permission 只能作为 `platform_permission` 证据，不能建立当前 task-local authority；
- 任何 external write 都要求充分的平台权限与当前任务授权同时成立，并预先记录 repository/target、branch/ref、paths、protected paths、target workspace/material/write boundary 与 action type；
- persistent permission 不是未来任务授权；branch / PR 工作还必须遵守 `current/github-single-active-pr-lineage-guard.md`；
- 下游模板通常只保存 canonical instance 的引用和本地必需字段；若保留本地 summary，必须标明 canonical source，并要求 summary 与被引用实例一致；
- 计划、workspace、connector、UI 与 approval mechanics 等时效性事实保持 research-gated，不得固化为永久能力。

### 1) Raw Record（非执行源）

Raw Record 可以保存安全原文、经筛查的脱敏摘录、安全 pointer 或 outside-Git reference，但不得把“raw-first”解释为无条件把原始内容写入 Git。

```yaml
id: RAW-0000
title: <原文记录标题>
status: preserved
source_refs: []
recorded_at: YYYY-MM-DD
summary: <该原文记录的简短说明>
repository_capture_safety_preflight_ref:
repository_capture_safety_preflight_result_summary: pass | blocked | incomplete
content_storage:
  mode: repository_original | repository_redacted_excerpt | repository_safe_pointer | outside_git
  original_text_or_file_ref:
  redacted_excerpt_ref:
  safe_external_pointer_ref:
  outside_git_reference:
notes: <补充说明，未定可写 TODO>
execution_source: false
```

规则：

- `content_storage.mode` 必须且只能选择一个 route；只有所选 route 对应的内容字段可以非空，其他内容字段必须为空或省略；
- `repository_original` 只允许在被引用 preflight 为 `pass` 时保存 original bytes/text；
- `repository_redacted_excerpt` 只允许保存 preflight 已筛查的 redacted content/reference；`repository_safe_pointer` 只允许保存 preflight 已筛查的 pointer；
- `outside_git` 不得在本记录中包含 original repository content，只能保存经过安全检查、不会泄露受限信息的 outside-Git reference 与必要 summary；
- `repository_capture_safety_preflight_result_summary` 只是本地摘要，canonical source 是 `repository_capture_safety_preflight_ref`；两者不一致时必须 fail closed；
- 无论 storage mode 如何，Raw Record 都保持 non-execution-source。

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
receiver_guidance_load:
  project_guidance: required | not_applicable | unknown_requires_owner_decision
  mnemosyne_guidance: required | yes | no | unknown_requires_user_decision | not_applicable
receiving_operations:
  receive_handoff:
    required: true
    status: pending | completed | blocked
    command_ref: commands/receive-mnemosyne-handoff.md
  receive_report:
    required: true
    status: pending | completed | blocked
    report_ref:
  project_guidance_load:
    required: true | false | unknown_requires_owner_decision
    status: pending | completed | blocked | not_applicable
    guidance_or_owner_rule_ref:
  mnemosyne_guidance_refresh:
    requirement: required | yes | no | unknown_requires_user_decision | not_applicable
    status: pending | completed | blocked | not_applicable
    command_ref: commands/load-mnemosyne-guidance.md | null
  substantive_continuation:
    status: blocked_pending_prerequisites | ready | started
notes: <下一步建议，不复制完整历史>
execution_source: false
```

规则：

- `source_refs` 继续保存 task-relevant evidence；其中的 `current/active-context.md`、handoff 或其他 live-state 文件不会仅因被引用而成为接收方 action plan；
- receiving 顺序固定为：`receive_handoff` → `emit_receive_report` → 加载 required project guidance / owner rule → 仅在 task-local 值要求时单独刷新 Mnemosyne guidance → substantive continuation；
- handoff package 创建时不得预先声称上述 operation 已完成，初始状态应为 `pending` 或明确的 `not_applicable`；
- 当 `mnemosyne_guidance` 为 `no` 或 `not_applicable` 时，refresh `command_ref` 必须为空或省略，status 必须为 `not_applicable`；
- Mnemosyne-owned handoff 的 project guidance 是 `current/human-approved-spec.md`，且 receive report 后仍需单独 guidance refresh；target-project business handoff 必须先加载目标项目自己的 confirmed guidance / owner rule，并保留 task-local open question。

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
