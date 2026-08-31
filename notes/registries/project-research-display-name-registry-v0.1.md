# Project Research Display-Name Registry v0.1

> Non-execution-source registry for compact UI aliases used by Deep Research, Fable-class research, and equivalent one-run external work. Canonical task IDs and project truth remain elsewhere.

```yaml
registry_id: MNEMOSYNE-PROJECT-RESEARCH-DISPLAY-NAME-REGISTRY-001
created_by_task: MNEMOSYNE-189
version: 0.3.0
last_updated_by_task: MNEMOSYNE-259（DR 编号统一终案 v2 落地：旧序列回填 001~013、八月六项改号 014~019、新签发至 027、next→028）
status: active_after_MNEMOSYNE_189_merge
source_guard: current/external-research-display-name-guard.md
execution_source: false
owner: user
scope_extension_by_MNEMOSYNE_246: 对话命名规范（§7）——研究运行显示名之外，UI 对话名也由本表登记主线码与类型码
```

## 1. Project abbreviations

```yaml
projects:
  Mnemosyne:
    project_id: mnemosyne
    abbreviation: MNE
    sequence_width: 3
    allocation_owner: Mnemosyne_owner_or_authorized_Mnemosyne_task
    next_unallocated_sequence: 028
  Meta_Agent:
    project_id: meta-agent
    abbreviation: MA
    sequence_width: established_two_digit_canonical_convention
    allocation_owner: Meta_Agent_owner_route
    highest_observed_canonical_research_sequence: 15
    next_sequence: must_be_allocated_by_Meta_Agent_target_route
```

## 2. Issued Mnemosyne display aliases

```yaml
issued_aliases:
  - display_name: MNE-DR-014 验证包审计
    sequence: 014
    former_number: MNE-DR-001
    former_number_scope: frozen_materials_and_pre_2026-08-31_references
    canonical_task_id: FABLE5-FCV-PACKAGE-ADVERSARIAL-AUDIT-001
    project: Mnemosyne
    status: issued_paused_not_completed
    notes: [alias_only_no_canonical_rename, R0_and_R1_use_phase_suffixes]
  - display_name: MNE-DR-015 表面威胁
    sequence: 015
    former_number: MNE-DR-002
    former_number_scope: frozen_materials_and_pre_2026-08-31_references
    canonical_task_id: FABLE5-FCV-MANUAL-SURFACE-THREAT-MODEL-001
    project: Mnemosyne
    status: issued_deferred_not_executed
    notes: [alias_only_no_canonical_rename]
  - display_name: MNE-DR-016 生命周期验证
    sequence: 016
    former_number: MNE-DR-003
    former_number_scope: frozen_materials_and_pre_2026-08-31_references
    canonical_task_id: MNE-TARGET-LIFECYCLE-V1-001
    project: Mnemosyne
    status: issued_owner_authorized_execution_complete_pending_fresh_Pro
    allocation_task: MNEMOSYNE-212
    execution_package: notes/target-agent-lifecycle-v1-execution-package-001/README.md
    notes: [alias_only_no_canonical_rename, one_V1_run_with_logical_multicell_execution, three_conversation_operator_flow, use_suffixes_Execute_S8_Review, no_Deep_Research_or_Fable_execution_implied]
  - display_name: MNE-DR-017 能力归属
    sequence: 017
    former_number: MNE-DR-004
    former_number_scope: frozen_materials_and_pre_2026-08-31_references
    canonical_task_id: FABLE5-MNE-REUSABLE-CAPABILITY-OWNERSHIP-001
    project: Mnemosyne
    status: completed_pending_Owner_disposition
    allocation_task: MNEMOSYNE-213
    report_cycle: raw/research-reports/cycles/2026Q3-reusable-agent-capability-ownership/
    notes: [Fable_run_used_historical_UI_name_MNE_DR_003_能力归属, stored_alias_changed_only_for_navigation_after_parallel_sequence_collision, canonical_task_id_and_original_report_unchanged]
  - display_name: MNE-DR-018 跨仓库并发
    sequence: 018
    former_number: MNE-DR-005
    former_number_scope: frozen_materials_and_pre_2026-08-31_references
    canonical_task_id: FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001
    project: Mnemosyne
    status: A1_readiness_pass_corrected_G2A_template_publication_complete_pending_separate_Owner_G2A_decision
    allocation_task: MNEMOSYNE-214
    execution_package: handoff/fable5-ready/FABLE5-MNE-CROSS-REPOSITORY-SAFE-CONCURRENCY-001/
    notes: [roadmap_F2, A0_complete, A1_not_authorized, G2A_not_issued, corrected_G2A_template_published_via_PR_303_merge_3ea2b97c369837d27d0e4a65c38c252e755954b5, separate_Owner_G2A_decision_still_required]
  - display_name: MNE-DR-019 交接加固
    sequence: 019
    former_number: MNE-DR-006
    former_number_scope: frozen_materials_and_pre_2026-08-31_references
    canonical_task_id: FABLE5-MNE-HANDOFF-PROTOCOL-REPOSITORY-AUDIT-001
    project: Mnemosyne
    status: repository_audit_and_HVAL_design_audit_complete_Pro_adjudicated
    allocation_task: MNEMOSYNE-240_durable_registration_after_235_236_237_238_239_blocked
    report_source_roots:
      - raw/validation-reviews/MNE-DR-006-handoff-protocol-repository-audit-001/
      - raw/validation-reviews/MNE-DR-006-HVAL001-preexecution-design-audit-001/
    notes:
      - Fable_5_Work_Ultra_Research_OFF
      - repository_only_public_evidence_audit
      - HVAL_design_002_accepted_for_separate_Owner_authorization
      - audit_evidence_and_HVAL_design_002_published_via_PR_303
      - registration_complete_at_repository_audit_and_HVAL_design_stage
      - HVAL_fixture_publication_and_scenario_execution_remain_separately_gated
      - cross_route_god_view_claims_remain_blocked
  - display_name: MNE-DR-020 平台能力刷新
    sequence: 020
    canonical_task_id: FABLE5-REDESIGN-001-RQ1
    project: Mnemosyne
    status: executed_report_recovered_archived_alaya_research_MNE
    allocation_task: FABLE5-REDESIGN-001
    taskbook: project-knowledge/FABLE5-REDESIGN-001/MNE-DR-020-platform-capability-refresh-taskbook.md
  - display_name: MNE-DR-021 交接实践现状
    sequence: 021
    canonical_task_id: FABLE5-REDESIGN-001-RQ2
    project: Mnemosyne
    status: executed_report_recovered_archived_alaya_research_MNE
    allocation_task: FABLE5-REDESIGN-001
    taskbook: project-knowledge/FABLE5-REDESIGN-001/MNE-DR-021-continuity-practice-taskbook.md
  - display_name: MNE-DR-022 需求生命周期
    sequence: 022
    canonical_task_id: FABLE5-REDESIGN-001-RQ3
    project: Mnemosyne
    status: issued_ready_not_executed
    allocation_task: FABLE5-REDESIGN-001
    taskbook: project-knowledge/FABLE5-REDESIGN-001/MNE-DR-022-requirements-lifecycle-taskbook.md
  - display_name: MNE-DR-023 检索与按需加载
    sequence: 023
    canonical_task_id: FABLE5-REDESIGN-001-RQ6
    project: Mnemosyne
    status: issued_ready_not_executed
    allocation_task: FABLE5-REDESIGN-001
    taskbook: project-knowledge/FABLE5-REDESIGN-001/MNE-DR-023-retrieval-and-loading-taskbook.md
  - display_name: MNE-DR-024 交接评测工具
    sequence: 024
    canonical_task_id: FABLE5-REDESIGN-001-RQ7
    project: Mnemosyne
    status: issued_ready_not_executed
    allocation_task: FABLE5-REDESIGN-001
    taskbook: project-knowledge/FABLE5-REDESIGN-001/MNE-DR-024-handoff-eval-instruments-taskbook.md
  - display_name: MNE-DR-025 学习者建模证据
    sequence: 025
    canonical_task_id: FABLE5-REDESIGN-001-RQ8
    project: Mnemosyne
    status: issued_ready_not_executed
    allocation_task: FABLE5-REDESIGN-001
    taskbook: project-knowledge/FABLE5-REDESIGN-001/MNE-DR-025-learner-modeling-evidence-taskbook.md
  - display_name: MNE-DR-026 开发知识资产
    sequence: 026
    canonical_task_id: FABLE5-REDESIGN-001-RQ9
    project: Mnemosyne
    status: issued_ready_not_executed
    allocation_task: FABLE5-REDESIGN-001
    taskbook: project-knowledge/FABLE5-REDESIGN-001/MNE-DR-026-dev-knowledge-assets-taskbook.md
  - display_name: MNE-DR-027 GitHub写能力实测
    sequence: 027
    canonical_task_id: FABLE5-REDESIGN-001-RQ12
    project: Mnemosyne
    status: issued_ready_not_executed
    allocation_task: FABLE5-REDESIGN-001
    taskbook: project-knowledge/FABLE5-REDESIGN-001/MNE-DR-027-github-write-capability-taskbook.md
```

## 2A. Legacy 2026H1 回填段（MNEMOSYNE-259，按 FABLE5-REDESIGN-001 编号统一终案 v2）

旧 UI 序列 DR1~DR13（2026-06-22~07-29）按**原号**回填占用 001~013；证据映射与逐件实物见
`notes/cross-model-review-results/FABLE5-REDESIGN-001/09-continuation/04-dr-numbering-unification-record.md` §2（该轨道 PR 合并后为准）。

```yaml
legacy_2026H1:
  entries:
    - {seq: "001", topic: 记忆系统测试/调试/评估证据综述, date: 2026-06, evidence: RC-2026Q2-memory-testing}
    - {seq: "002", topic: 交接策略与量化评估, date: 2026-06, evidence: RC-2026Q2-handoff-strategy}
    - {seq: "003", topic: not_found, note: 仓库与 Alaya 均无 3 号实物；不断言不存在，Owner 可补}
    - {seq: "004", topic: 用户原文/需求脱敏治理, date: 2026-06-29, evidence: RC-2026Q2-user-input-governance}
    - {seq: "005", topic: 首个真实目标试运行评估框架 v2, date: 2026-06-30, evidence: RC-2026Q2-first-target-dry-run-evaluation}
    - {seq: "006", topic: 平台/Project memory/apps 能力 delta, date: 2026-07-15, evidence: RC-2026Q3-platform-context-apps-delta}
    - {seq: "007", topic: 多模型裁定与溯源（pro/thinking 双运行）, date: 2026-07-21, evidence: RC-2026Q3-multi-model-adjudication-provenance}
    - {seq: "008", topic: HO-GUIDANCE-001 目标项目对话加载指导, date: 2026-07-28, evidence: Alaya 对话导出}
    - {seq: "009", topic: LEARNER-COGNITIVE-COACHING-001, date: 2026-07-28, evidence: Alaya 对话导出}
    - {seq: "010", topic: CROSS-AGENT-SHARED-MEMORY-001, date: 2026-07-28, evidence: Alaya 对话导出}
    - {seq: "011", topic: TARGET-MEMORY-MIGRATION-001, date: 2026-07-28, evidence: Alaya 对话导出}
    - {seq: "012", topic: PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001, date: 2026-07-28, evidence: Alaya 对话导出}
    - {seq: "013", topic: PRO-DR-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001, date: 2026-07-29, evidence: Alaya 对话导出}
  unnumbered_legacy: [AI Agent 持久记忆研究(0622), review batch-B(0622), 并行工作主线治理(0724), RC-2026Q2-initial 整轮]
```

**序列规则（终案 v2）**：全序列严格唯一、永不复用；曾用号（八月六项的旧 001~006 指代）仅为读档别名、不再签发；
读 2026-08-31 前冻结档案遇 MNE-DR-001~006 按"曾用号"解读；活文件中的旧号引用采 lazy migration（碰到才改，维护线掌节奏）。

## 3. Historical Meta-Agent compatibility

Meta-Agent canonical IDs such as `MA-DR-08` through `MA-DR-15` remain unchanged. Mnemosyne does not allocate a Meta-Agent sequence.

## 4. Allocation procedure

```yaml
allocation:
  required_inputs: [project_identity, canonical_task_id, short_topic, latest_project_registry]
  checks: [abbreviation_exists, canonical_task_not_already_mapped, sequence_not_previously_issued, short_topic_is_compact]
  result: [update_registry_in_authorized_project_route, expose_display_name_in_operator_flow]
```

Prepared but unregistered aliases remain vulnerable to cross-conversation races. Issue/PR numbers are never DR sequences.

## 5. Migration rule

On repository migration: copy the full issued history, verify collisions, designate one allocator, mark the old registry historical, and prohibit simultaneous allocation.

## 6. Boundaries

- This registry does not authorize external runs or quota.
- Aliases are not canonical task IDs.
- It does not modify Meta-Agent target truth.
- It does not guarantee UI character support.

## 7. 对话命名规范（MNEMOSYNE-246 并入；设计源：FABLE5-REVIEW2-001 设计稿G，Owner 终审批准）

### 7.1 命名格式

```text
[项目]-[主线]-[类型][序号] 简短主题
```

示例：`MNE-M-C16 状态修复批次`（Mnemosyne · 维护主线 · 普通对话第 16 代）、`MNE-FR2-K01 第二轮评审`、`MA-B-W03 产品构建`。

### 7.2 主线码登记表

```yaml
mainline_codes:
  MNE:
    M:
      full_name: Mnemosyne 维护主线
      status: active
    FR2:
      full_name: FABLE5-REVIEW2-001 第二轮评审轨道
      status: active
  MA:
    B:
      full_name: Meta-Agent 构建主线
      status: active_allocation_by_meta_agent_route
# 新主线码：起名前在本表登记一行（读-占-写同批：与首个使用它的变更同 PR 落表）。
```

### 7.3 类型码表

| 码 | 类型 | 说明 |
|---|---|---|
| C | ChatGPT 普通对话 | |
| DR | 深度研究 | 沿用现行 MNE-DR-NNN 序列（本表 §2）时可省主线段（历史兼容） |
| W | ChatGPT Work | |
| X | Codex 任务 | |
| K | Claude 网页对话 | C 已被占用；取 K 蕴意 Klaude |
| CC | Claude Code 会话 | 通常无需手动命名（见 §7.5） |

### 7.4 三条铁律

1. **序号 = 主线内交接代数**：只在同主线交接时 +1；插队/派生对话用父名加后缀（如 `MNE-M-C16a`），不占代数。
2. **名字是导航元数据，不是权威**：canonical 任务号/轨道号以仓库记录为准；名字标错可随时改，不需留痕仪式。
3. **不用状态词命名**（Depre/Finish/Failed 一律不用）：对话死活成败写在归档索引里；日期不进名字（导出件自带创建时间）。

（三条铁律分别针对档案盘点实证的命名陷阱：系列号撞名、改名残留前缀、"Finish 却在链条中段"误读。）

### 7.5 Claude 侧并入方式

- Claude 网页对话：创建时按 §7.1 起名（K 类型），与 ChatGPT 对话同一套登记。
- Claude Code 会话：身份已由三层自动承载（任务号入 commit 尾注、会话记录含逐响应模型标识、转录归档带会话 ID），不强制手动命名；需要 UI 辨识时用会话重命名打同格式标签即可。
- 归档衔接：导出文件名 = 对话名 + 创建日期（现行惯例保留）；族谱索引以任务号区间校验名字。

### 7.6 迁移与容错

- **历史对话不批量改名**（既有导出的真实谱系由归档索引承载）；本规范自生效起用于新对话。
- 忘记起名/起错名无惩罚，归档索引兜底；每次归档盘点时核对序号连续性（对冲 Owner 错记上一代序号的风险）。
- **历史对话导出标记法**（MNEMOSYNE-253 追认，2026-08-28 MA 批次首用）：为便于在 ChatGPT 侧栏辨识待导出的历史对话，可加**项目码单段前缀**（如 `MA-原名`）——不补主线码、不追编序号、不加状态词；改名只作导航标记，谱系真相由归档索引承载。
