# Target Project Memory System Template Pack / 目标项目记忆系统模板包

## 文件定位

本文件用于 Mnemosyne 为目标项目设计外部持久记忆系统。

本文件不是执行源。当前执行源仍是：

- `current/human-approved-spec.md`

本文件是模板包，不是某个真实项目的最终交付物。使用本模板生成真实目标项目设计前，必须先收集目标项目约束，并经用户或目标项目 owner 确认。

涉及平台能力、自动化承诺、目标项目交付方式时，必须参考研究证据 current 视图：

- `raw/research-reports/current/research-report-index.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`

如果本文件与 `current/human-approved-spec.md` 冲突，以 `current/human-approved-spec.md` 为准，并登记 open question。

## 使用边界

- 本模板包只提供设计骨架和检查点。
- 本模板包不自动创建目标项目文件。
- 本模板包不默认目标项目有 GitHub、MCP、RAG、GitHub Actions 或自动触发能力。
- 本模板包不默认普通对话窗口能写回外部持久层。
- 本模板包不要求全量读取 raw；高风险、高价值、低置信度内容按需回查。
- PDF 图表、图片和版式相关证据仍需人工复核后才能作为强证据使用。

---

## 1. Target Project Intake Template

用于收集目标项目基本信息。

说明：

- Intake 不是执行源。
- Intake 只用于收集约束、目标、风险和待确认问题。
- 如果用户目标不清，应先补 intake，而不是直接设计记忆系统。
- Intake 中的假设必须在 Memory System Design Spec 中显式标为 `assumptions` 或 `unsupported_assumptions`。

```yaml
intake_id:
target_project_name:
target_project_type:
owner_or_user:
primary_language:
working_language:
project_stage:
repository_or_storage_location:
existing_files_or_artifacts:
current_tools:
expected_ai_tools:
expected_human_users:
target_project_goal:
memory_system_goal:
expected_lifespan:
expected_update_frequency:
collaboration_pattern:
privacy_level:
sensitive_content_types:
automation_expectation:
review_requirement:
handoff_requirement:
migration_requirement:
research_evidence_required:
constraints:
assumptions:
open_questions:
status:
```

字段提示：

- `target_project_type` 可先使用第 2 节分类器中的类型，未知时写 `hybrid_or_unknown`。
- `privacy_level` 可先使用 `public`、`internal`、`private`、`confidential`、`unknown`，后续是否正式化仍待决策。
- `automation_expectation` 应区分“用户希望自动化”和“当前工具已验证可自动化”。
- `research_evidence_required` 可标记是否需要回查 research current 视图或更细报告。
- `status` 可使用 `draft`、`needs_user_review`、`confirmed`、`superseded`。

---

## 2. Target Project Type Classifier

用于初步分类目标项目。分类只服务于设计取向，不替代用户确认。

| type | 典型输入 | 典型记忆对象 | 推荐文件结构倾向 | 风险 | 是否适合高自动化 | 是否需要更强隐私分级 | 是否需要研究证据回查 |
|---|---|---|---|---|---|---|---|
| `long_term_research` 长期研究 | 论文、报告、访谈、实验记录、阅读笔记 | 研究问题、证据、假设、结论、反例、待复核材料 | `raw/` 与 `notes/` 较重，保留 evidence map / decision log | 证据过期、引用漂移、PDF 图表误读 | 通常不宜高自动化，适合半自动整理与人工 review | 视研究主题而定，可能需要 | 是，尤其涉及工具能力或外部事实时 |
| `learning_system` 学习系统 | 课程、教材、练习、错题、学习日志 | 学习目标、知识点、弱项、复习计划、反馈 | `current/` 与 `notes/` 平衡，强调 todo / review | 把短期状态误写成长期真相；隐私学习记录泄露 | 中等；计划生成可辅助，确认仍需人工 | 通常需要个人隐私分级 | 按需，尤其涉及工具能力和学习方法承诺 |
| `source_code_learning` 源码学习 | 代码仓库、阅读笔记、调试记录、架构图 | 模块理解、调用链、疑问、实验结论 | 可放仓库根目录或 `.memory/`，强调 code refs 与 task-results | 代码版本漂移、理解过时、误读生成代码 | 中等；依赖开发工具读写能力 | 如含私有代码则需要 | 是，涉及开发 Agent 能力时 |
| `software_development_project` 软件开发项目 | issue、PR、代码、设计文档、测试结果 | 产品决策、架构约束、任务状态、变更记录 | 适合仓库内 `memory/` 或 `.memory/`，强调 handoff / task-results | 执行源与代码规范冲突、自动化越权、过期 TODO | 可在已验证工具链中逐步提高，但不默认 | 私有仓库通常需要 | 是，涉及 GitHub / Codex / CI 能力时 |
| `ai_agent_project` AI Agent 项目 | prompt、工具说明、评测、运行日志 | agent 目标、工具边界、失败案例、评测结论 | 强调 capability boundaries、unsupported assumptions、eval notes | 过度承诺模型能力、工具权限不清 | 谨慎；需先验证工具与权限 | 常需要，可能含密钥或用户数据 | 是，必须回查能力边界 |
| `multi_agent_team` 多 Agent 团队 | 角色定义、任务拆分、交接记录、冲突记录 | agent 责任边界、协调规则、共享记忆、决策记录 | 强调 handoff、conflict log、owner / review 规则 | 协调幻觉、重复劳动、自动写回冲突 | 当前不默认高自动化；需额外治理 | 常需要 | 是，涉及多 Agent 自动协调边界时 |
| `personal_long_conversation` 个人长期对话 / 知识管理 | 对话摘要、偏好、生活 / 工作笔记、长期目标 | 个人偏好、长期计划、重要决定、背景知识 | 可用独立资料库目录，强调隐私、摘要和手工确认 | 隐私泄露、未经确认的个人结论固化 | 不宜高自动化；普通对话窗口默认半自动 | 强烈需要 | 是，尤其涉及普通对话外部记忆能力 |
| `hybrid_or_unknown` 混合或未知场景 | 混合材料、不完整描述、未定目标 | 暂存目标、约束、疑问、候选分类 | 先最小 intake + open questions，不急于完整结构 | 过早设计、错误分类、遗漏约束 | 不适合高自动化 | 先按 unknown 处理，必要时更强保护 | 按需；若涉及能力承诺则需要 |

---

## 3. Memory System Design Spec Template

用于为目标项目生成记忆系统设计说明。

说明：

- Memory System Design Spec 草案不是执行源。
- 只有目标项目用户确认并落入目标项目仓库 / 目录后，才成为该目标项目的运行依据。
- Mnemosyne 仓库保存设计档案，目标项目仓库或目录保存运行真相源。
- 不要把 Mnemosyne 的 `current/human-approved-spec.md` 直接当成目标项目执行源。

```yaml
design_spec_id:
target_project_ref:
design_status:
design_version:
created_from_intake:
design_owner:
target_project_type:
memory_system_purpose:
execution_source_for_target_project:
non_execution_sources:
evidence_sources:
canonical_memory_files:
raw_input_policy:
candidate_requirement_policy:
decision_record_policy:
active_context_policy:
handoff_policy:
todo_policy:
open_question_policy:
codex_task_result_policy:
research_evidence_policy:
model_migration_policy:
privacy_policy:
automation_boundary:
review_workflow:
drift_review_policy:
file_layout:
update_workflow:
conflict_resolution_policy:
unsupported_assumptions:
open_questions:
acceptance_criteria:
```

字段提示：

- `design_status` 可使用 `draft`、`needs_user_review`、`confirmed`、`delivered_to_target_project`、`superseded`。
- `execution_source_for_target_project` 必须指向目标项目自己的执行源，而不是 Mnemosyne 执行源。
- `automation_boundary` 必须写明哪些更新需要人工确认，哪些工具能力尚未验证。
- `evidence_sources` 应列明实际参考过的研究 current 视图、目标项目资料和用户确认记录。

---

## 4. Target Project Memory File Layout Template

用于生成目标项目记忆系统文件结构。

通用推荐结构：

```text
memory/
  current/
    human-approved-spec.md
    active-context.md
    todo.md
    open-questions.md
  handoff/
    handoff-current.md
    startup-instructions.md
  notes/
    decision-log.md
    candidate-requirements.md
    task-results/
  raw/
    raw-index.md
```

说明：

- 这是通用模板，不是强制结构。
- 开发项目可以放在仓库根目录或 `.memory/`。
- 非开发项目可以放在独立资料库目录。
- 隐私敏感项目需要额外分级，例如将敏感 raw 与可共享 summary 分开。
- 目标项目可根据工具能力裁剪文件。
- 如果目标项目工具不能稳定读写文件，应把“写回”改为人工复制 / 人工提交步骤。

---

## 5. Target Project Execution Source Rule Template

用于定义目标项目中的执行源。

```yaml
execution_source_file:
non_execution_sources:
conflict_rule:
user_confirmation_rule:
update_permission:
review_requirement:
versioning_rule:
```

必须说明：

- 每个目标项目都应明确自己的执行源。
- raw、candidate、decision-log、handoff、active-context 默认不是执行源。
- 如果目标项目有自己的 `AGENTS.md` / `CLAUDE.md`，其执行边界必须单独定义。
- 不要把 Mnemosyne 的 `human-approved-spec` 直接当成目标项目执行源。
- 若目标项目存在多类规范文件，应定义冲突优先级和用户确认规则。

示例规则骨架：

```yaml
execution_source_file: memory/current/human-approved-spec.md
non_execution_sources:
  - memory/raw/
  - memory/notes/candidate-requirements.md
  - memory/notes/decision-log.md
  - memory/current/active-context.md
  - memory/handoff/handoff-current.md
conflict_rule: 若非执行源与 execution_source_file 冲突，以 execution_source_file 为准，并登记 open question。
user_confirmation_rule: 更新 execution_source_file 前必须经 owner 确认。
update_permission: 半自动草案；人工 review 后提交。
review_requirement: 高风险、隐私、自动化和交付边界变更必须 review。
versioning_rule: 使用 Git commit 或带日期版本记录；无 Git 时保留变更日志。
```

---

## 6. Target Project Workflow Template

用于描述目标项目日常运行流程。

当前 v0.2 仍是半自动流程：

- 不默认自动写回。
- 不默认自动查重。
- 不默认全量读取 raw。
- 不默认自动触发。

最小流程：

1. Capture：捕获输入，例如用户反馈、项目资料、任务结果、研究证据或运行日志。
2. Extract：抽取候选需求 / 记忆项，写入 candidate 或草案。
3. Compare：查重和冲突检查，对比执行源、open questions、decision log 和必要 evidence。
4. Decide：用户或项目 owner 确认接受、修改、延期或拒绝。
5. Apply：更新目标项目执行源或当前上下文；若不能自动写文件，则输出人工操作步骤。
6. Handoff：更新交接文件，说明当前阶段、已完成、阻塞和下一步。
7. Review：周期性检查漂移，尤其检查执行源、活跃上下文和实际项目状态是否一致。
8. Archive：归档旧 raw / 旧状态，保留可追溯性，避免把过期状态当作当前事实。

---

## 7. Delivery Package Draft Template

用于未来把 Mnemosyne 设计输出给目标项目。

```yaml
delivery_package_id:
target_project_ref:
memory_system_design_spec_ref:
generated_files:
files_to_copy_to_target_project:
files_to_keep_in_mnemosyne:
unsupported_assumptions:
manual_setup_steps:
review_required_before_use:
drift_review_todo:
rollback_or_revision_plan:
```

说明：

- 本模板是 Delivery Package Draft 的草案入口。
- delivery manifest 深化入口为 `notes/delivery-manifest-template-pack.md`。
- 完整交付清单、复制清单、落地检查、handoff package、rollback / revision plan 和 delivery result record 应参考 `notes/delivery-manifest-template-pack.md`。
- delivery manifest template pack 不是执行源。
- 交付包不是自动生效，真正交付目标项目之前必须经用户确认和目标项目落地。
- 目标项目运行真相源应位于目标项目仓库 / 目录，而不是 Mnemosyne 草案文件。
- `files_to_copy_to_target_project` 与 `files_to_keep_in_mnemosyne` 必须分开，避免把设计档案误当运行真相源。

---

## 8. Target Project Handoff Template

用于目标项目跨对话 / 跨任务交接。

```yaml
target_project_name:
current_stage:
execution_source:
recommended_read_order:
completed_items:
current_blockers:
next_recommended_step:
files_changed_recently:
review_required:
warnings:
unsupported_assumptions:
```

说明：

- Handoff 是交接卡，不是完整历史，也默认不是执行源。
- `recommended_read_order` 应优先列执行源、active context、handoff 和 open questions。
- `warnings` 应明确能力边界、隐私边界和未验证假设。

---

## 9. Unsupported Assumptions Template

用于明确哪些能力或前提尚未验证。

```yaml
assumption_id:
assumption:
source:
affected_design_part:
risk_level:
verification_needed:
fallback_plan:
status:
```

字段提示：

- `risk_level` 可使用 `low`、`medium`、`high`、`unknown`。
- `status` 可使用 `unverified`、`partially_verified`、`verified`、`rejected`、`replaced_by_fallback`。

常见风险清单：

- 目标工具是否能写文件。
- 目标工具是否能访问 GitHub。
- 目标工具是否能稳定读取 PDF / 图片 / 图表。
- 目标工具或平台是否能自动触发。
- 目标项目是否允许外部工具或自动化。
- 隐私 / 权限是否允许存储原文。
- 目标项目是否允许把 raw、日志或用户材料保存到仓库。
- 目标项目是否有 review owner 和提交权限。

---

## 10. Target Project Drift Review Template

用于定期检查目标项目记忆系统是否偏离原设计。

```yaml
drift_review_id:
target_project_ref:
review_date:
reviewed_files:
expected_state:
actual_state:
drift_found:
severity:
proposed_fix:
user_decision_required:
follow_up_tasks:
```

说明：

- Drift review 不应默认自动修改文件。
- 高风险漂移包括：执行源失效、handoff 过期、自动化越权、隐私材料误入公开仓库、目标项目实际流程与设计 spec 不一致。
- 若发现漂移，应先提出修复方案和用户决策点，再更新目标项目运行文件。

---

## 11. Minimal Target Project Design Runbook

最小操作流程：

1. 读取 Mnemosyne 执行源：`current/human-approved-spec.md`。
2. 读取 target project template pack：本文件。
3. 读取 research evidence current 视图：research report index、current evidence map、current capability boundaries。
4. 填写 Target Project Intake。
5. 分类目标项目类型。
6. 生成 Memory System Design Spec 草案。
7. 标记 unsupported assumptions。
8. 向用户展示设计选项。
9. 用户确认。
10. 生成交付包草案。
11. 用户 review。
12. 复制 / 落地到目标项目仓库或目录。
13. 创建 handoff。
14. 记录 delivery result。
15. 后续 drift review。

---

## 12. Completion Criteria

使用本模板包设计目标项目记忆系统时，至少应满足：

- 目标项目类型已明确或标为 `hybrid_or_unknown`。
- 执行源已明确。
- 非执行源已明确。
- 文件结构已草拟。
- 更新流程已草拟。
- handoff 流程已草拟。
- unsupported assumptions 已列出。
- 用户 review 点已明确。
- 自动化边界已明确。
- 研究证据已按需参考。
- 目标项目尚未确认前，不得声称已交付完成。
