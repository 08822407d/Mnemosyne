# Delivery Manifest Template Pack / 交付清单模板包

## 文件定位

本文件用于 Mnemosyne 将记忆系统设计交付到目标项目时生成交付清单。

本文件不是执行源。当前执行源仍是：

- `current/human-approved-spec.md`

本文件是模板包，不是任何真实项目的交付包。真实目标项目交付前必须由用户确认。

涉及工具能力、自动化承诺、目标项目写入方式时，必须参考研究证据 current 视图：

- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`

如果本文件与 `current/human-approved-spec.md` 冲突，以 `current/human-approved-spec.md` 为准，并登记 open question。

## 使用边界

- 本模板包只定义交付清单、检查项和记录格式，不自动执行交付。
- app connection、action availability、approval card 或 persistent permission 只能作为 `platform_permission` evidence，不能构成当前任务授权。
- 每个 repository / target / runtime-store action 都必须引用独立 canonical `repository_action_context`；不同 action surface 不得捆绑成一个权限结论。
- 计划、角色、workspace、connector、授权 UI 和 approval mechanics 是时效性事实；需要时通过 research gate 核验，不得写成稳定模板的永久能力。
- 不默认 GitHub Actions、RAG、MCP、自动查重、自动写回或自动 drift review 已经可用。
- 目标项目仓库 / 目录中的运行文件才是目标项目运行真相源；Mnemosyne 仓库保留设计档案和交付档案。
- PDF 图表、图片和版式相关证据仍需人工复核后才能作为强证据使用。

---

## 1. Delivery Manifest Template

用于记录一次目标项目记忆系统交付的总清单。

```yaml
delivery_manifest_id:
target_project_ref:
target_project_name:
target_project_type:
source_design_spec_ref:
source_intake_ref:
delivery_status:
delivery_version:
created_at:
created_by:
reviewed_by:
target_repository_or_storage:
repository_capture_safety_preflight_refs: []
repository_action_context_refs: []
target_memory_root:
files_to_create:
files_to_update:
files_to_copy_from_mnemosyne:
files_to_keep_only_in_mnemosyne:
files_not_to_copy:
required_manual_steps:
required_user_confirmations:
unsupported_assumptions_refs:
privacy_review_required:
automation_boundary:
rollback_plan_ref:
drift_review_plan_ref:
handoff_package_ref:
acceptance_criteria:
open_questions:
notes:
```

说明：

- Delivery Manifest 不是自动执行脚本。
- Delivery Manifest 记录交付意图、复制清单和人工确认点。
- 只有用户确认并实际落地到目标项目后，目标项目仓库 / 目录中的文件才成为目标项目运行真相源。
- `delivery_status` 可使用 `draft`、`needs_user_review`、`approved`、`delivered`、`partially_delivered`、`blocked`、`superseded`。
- `automation_boundary` 必须区分“希望自动化”与“当前工具和权限已验证可自动化”。

---

## 2. Files To Create / Update Checklist

用于明确目标项目需要创建或更新哪些文件。

```yaml
file_path:
action_type:
source_template_ref:
source_material_safety_preflight_ref:
repository_action_context_ref:
target_purpose:
is_execution_source:
requires_user_review:
contains_sensitive_content:
copy_mode:
overwrite_policy:
merge_policy:
validation_needed:
owner:
notes:
```

`action_type` 可包括：

- `create`
- `update`
- `copy`
- `merge`
- `skip`
- `manual_review_only`

`copy_mode` 可包括：

- `copy_from_mnemosyne_template`
- `generated_from_design_spec`
- `manually_written`
- `target_project_existing_file`
- `do_not_copy`

`overwrite_policy` 可包括：

- `never_overwrite_without_user_confirmation`
- `append_only`
- `replace_after_review`
- `manual_merge_required`

说明：

- 每个目标路径都应明确是否为执行源。
- 对已有目标项目文件，默认使用 `manual_merge_required` 或 `never_overwrite_without_user_confirmation`。
- 含敏感内容的文件必须先完成隐私 / 权限 review。

---

## 3. Target Project Runtime Truth Source Checklist

用于确认交付后哪些文件是目标项目运行真相源。

```yaml
target_execution_source_file:
target_non_execution_sources:
target_active_context_file:
target_handoff_file:
target_todo_file:
target_open_questions_file:
target_decision_log_file:
target_raw_policy:
conflict_resolution_rule:
user_confirmation_required:
relation_to_mnemosyne_archive:
```

必须说明：

- Mnemosyne 仓库是设计工厂和设计档案。
- 目标项目仓库 / 目录才是目标项目运行真相源。
- 不要让目标项目长期依赖 Mnemosyne 仓库中的草案文件运行。
- 如果目标项目已有 `AGENTS.md` / `CLAUDE.md` / `README` / `docs`，需要单独定义它们与目标项目执行源的关系。
- 若目标项目执行源与 Mnemosyne 交付档案冲突，以目标项目执行源为准，并把差异反馈到 Mnemosyne 的 self-improvement workflow 或 drift review。

---

## 4. Manual Setup Steps Template

用于记录用户或 AI 工具需要手工完成的落地步骤。

```yaml
step_id:
step_title:
actor:
repository_action_context_ref:
preconditions:
action:
target_file_or_location:
expected_result:
verification_method:
rollback_step:
risk:
notes:
```

`actor` 可包括：

- `user`
- `ChatGPT`
- `Codex`
- `Claude Code`
- `target_project_agent`
- `other_tool`

必须说明：

- 当前不默认自动执行。
- 普通对话窗口不能默认写回目标项目仓库。
- Codex / Claude Code 等是否能写入目标项目，取决于权限、仓库关联和任务环境。
- 每个高风险步骤应包含 `verification_method` 和 `rollback_step`。

---

## 5. Unsupported Assumptions Linkage Template

用于把目标项目模板中的 unsupported assumptions 连接到交付清单。

```yaml
assumption_ref:
delivery_impact:
must_resolve_before_delivery:
fallback_if_unresolved:
user_confirmation_required:
evidence_needed:
status:
```

必须覆盖：

- 工具是否能访问目标项目仓库。
- 工具是否能写文件。
- 用户是否允许保存原文。
- 是否存在隐私 / 权限限制。
- 是否需要离线存储。
- 是否需要多设备同步。
- 是否需要自动触发。
- 是否需要读取 PDF / 图片 / 图表。
- 是否依赖未验证的 MCP / RAG / GitHub Actions。

说明：

- `must_resolve_before_delivery` 为 `true` 时，交付前必须解决或由用户明确接受 fallback。
- `evidence_needed` 应列出需要回查的用户确认、目标项目资料或 research current 视图。

---

## 6. Delivery Review Checklist

用于交付前 review。

检查项至少包括：

- 目标项目类型是否明确。
- intake 是否完整。
- memory system design spec 是否完成。
- execution source 是否明确。
- non-execution sources 是否明确。
- 文件结构是否明确。
- 需要复制 / 生成 / 手写的文件是否明确。
- 隐私分级是否完成。
- unsupported assumptions 是否列出。
- 自动化边界是否明确。
- 用户确认点是否明确。
- rollback plan 是否存在。
- handoff package 是否存在。
- drift review TODO 是否存在。
- 是否存在未解决的阻断 open question。

建议记录格式：

```yaml
review_item_id:
check_item:
status:
evidence_ref:
blocking:
required_fix:
owner:
notes:
```

---

## 7. Handoff Package Template

用于目标项目交付后的接手包。

```yaml
handoff_package_id:
target_project_ref:
delivery_manifest_ref:
current_stage:
execution_source:
recommended_read_order:
receiver_guidance_load:
  project_guidance: required
  mnemosyne_guidance: yes | no | unknown_requires_user_decision
receiving_operations_contract_ref: notes/object-templates-and-id-rules.md::### 8) Handoff（非执行源）
receiving_operations:
  receive_handoff: pending | completed | blocked
  receive_report: pending | completed | blocked
  project_guidance_load: pending | completed | blocked
  mnemosyne_guidance_refresh: pending | completed | blocked | not_applicable
  substantive_continuation: blocked_pending_prerequisites | ready | started
receiving_operation_status_record_ref:
completed_setup_steps:
pending_setup_steps:
known_risks:
unsupported_assumptions:
next_recommended_step:
review_required:
drift_review_due:
notes:
```

说明：

- Handoff Package 是交接材料，默认不是执行源；package 创建时不得预先把 receiving operations 标为 completed。
- `recommended_read_order` 是 evidence/navigation，不能替代 artifact-mediated receive，也不会自动把 active context、handoff、open questions 或 todo 变成 action plan。
- 接收顺序固定为 receive → receive report → load target-project guidance / owner rule → 仅在 task-local 值为 `yes` 时单独刷新 Mnemosyne guidance → substantive continuation。
- `mnemosyne_guidance` 不得静默推断，也不构成全局先例；值为 `no` 时 refresh status 必须为 `not_applicable`，不得暗示执行 `commands/load-mnemosyne-guidance.md`。
- 未完成 setup steps、pending operation 与 known risks 必须保留到目标项目后续 review。

---

## 8. Rollback / Revision Plan Template

用于记录交付失败或需要回滚时的方案。

```yaml
rollback_plan_id:
delivery_manifest_ref:
affected_files:
rollback_trigger:
previous_state_refs:
rollback_steps:
manual_confirmation_required:
data_loss_risk:
fallback_plan:
notes:
```

说明：

- 如果目标项目已有文件，必须记录 `previous_state_refs` 或人工备份位置。
- 涉及删除、覆盖、迁移或隐私材料移动时，`manual_confirmation_required` 应为 `true`。
- 无法安全回滚时，应明确 `data_loss_risk` 和 fallback。

---

## 9. Delivery Result Record Template

用于记录一次实际交付结果。

```yaml
delivery_result_id:
delivery_manifest_ref:
target_project_ref:
delivery_date:
delivered_by:
repository_action_context_refs: []
repository_write_result_record_ref:
files_created:
files_modified:
files_skipped:
files_requiring_manual_merge:
user_confirmations_received:
unresolved_assumptions:
post_delivery_handoff_ref:
drift_review_todo:
actual_gaps:
follow_up_tasks:
notes:
```

说明：

- Delivery Result Record 不是执行源。
- 目标项目运行状态以后应以目标项目仓库 / 目录中的运行文件为准。
- Mnemosyne 中保留交付档案和后续 drift review 线索。
- 若交付结果与 manifest 草案不一致，应记录差异和 follow-up，而不是静默修改历史。

---

## 10. Minimal Delivery Runbook

最小交付流程：

1. 读取目标项目 intake。
2. 读取 memory system design spec。
3. 读取 target project template pack。
4. 读取 delivery manifest template pack。
5. 回查 research evidence current 视图。
6. 生成 delivery manifest 草案。
7. 列出 files to create / update。
8. 标记 unsupported assumptions。
9. 明确 execution source 和 non-execution sources。
10. 向用户展示交付选项。
11. 用户确认。
12. 复制 / 生成目标项目文件。
13. 创建目标项目 handoff package。
14. 创建 delivery result record。
15. 安排 drift review。
16. 更新 Mnemosyne active-context / todo / decision-log。
17. 提交并 review。

说明：

- 第 12 步不意味着自动写回；如果当前工具没有写入权限，应输出人工复制步骤。
- 任何真实交付都必须先完成用户确认和目标项目路径确认。

---

## 11. Delivery Completion Criteria

一次目标项目交付至少满足：

- Delivery Manifest 已创建。
- 用户已确认交付范围。
- 目标项目执行源已明确。
- 目标项目非执行源已明确。
- `files_to_create` / `files_to_update` 已明确。
- manual setup steps 已明确。
- unsupported assumptions 已列出。
- 隐私 / 权限风险已标注。
- rollback 或 revision plan 已存在。
- handoff package 已存在。
- drift review TODO 已存在。
- 未解决阻断问题已标注。
- 未确认前不得声称交付完成。
