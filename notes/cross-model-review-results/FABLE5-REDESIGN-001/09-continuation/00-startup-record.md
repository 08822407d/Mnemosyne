# FABLE5-REDESIGN-001 · 启动仪式记录（门 0 前）

```yaml
record_type: track_startup_record_and_run_context
track_id: FABLE5-REDESIGN-001
created_by_task: FABLE5-REDESIGN-001
generated_by_actor: claude-fable-5
generated_on_surface: claude-code-vscode
date: 2026-08-30
work_order: notes/cross-model-review-results/FABLE5-REDESIGN-001/00-work-order.md
execution_source: current/human-approved-spec.md
authority_level: non_execution_source_track_record
```

## 1. 写前预检（工作令 §0.1）

- `scripts/preflight-write.sh` 第一次运行（在 `mnemosyne-258-recover-orphaned-exp7-addendum` 上）：`STOP`（该分支 PR #322 已合并）——按谱系防护 §4.3 不在已合并分支续写，切至最新 master 新建分支。
- 本地 `master` 由 `9b05672` fast-forward 至 `origin/master`；第二次运行（在新分支上）：`preflight_ok`。
- `gh auth status`：已登录 `08822407d`（scopes: gist, read:org, repo；协议 ssh）。
- **钉住 master**：`ccd42434b2f946fda78138ba2f5bf66f1f432be1`（`ccd4243`，Merge PR #322，2026-08-30 08:11 -0700）。工作令起草时钉 `82b1093`；之间新增 PR #321（MNEMOSYNE-257 Owner 裁定）与 #322（MNEMOSYNE-258 含本工作令），工作令正文与 origin/master 逐字一致。

## 2. 谱系预检（lineage guard §3 / §3.1 / §5）

```yaml
github_write_lineage_preflight:
  task_id: FABLE5-REDESIGN-001
  intended_scope_summary: 需求综合分析与独立重新设计（四门）；只新建文件于两个授权目录
  default_branch: master
  pinned_default_branch_sha: ccd42434b2f946fda78138ba2f5bf66f1f432be1
  intended_branch: fable5-redesign-001-workspace
  open_pr_enumeration:
    method: gh pr list --state open --limit 100 (1 open) + gh pr diff 316 --name-only
    pagination_complete: true
    all_accessible_open_prs_checked: true
  matches:
    by_exact_task_id: ["#322 MERGED（含本工作令，非本轨道谱系）"]
    by_intended_head_branch: []
    by_equivalent_scope: []
    open_pr_changed_paths_vs_authorized_paths: empty   # #316 改 current/review-and-validation-status.md、notes/cross-family-cooperation/MNEMOSYNE-253-*.md、notes/registries/project-research-display-name-registry-v0.1.md；与本轨道两目录无交集
    existing_result_records_or_task_artifacts: ["notes/cross-model-review-results/FABLE5-REDESIGN-001/00-work-order.md"]
  decision: create_new_lineage
authorized_paths:
  - notes/cross-model-review-results/FABLE5-REDESIGN-001/
  - project-knowledge/FABLE5-REDESIGN-001/
protected_paths_not_to_touch: [current/, commands/, handoff/, notes/registries/, scripts/, README.md]
```

```yaml
PR_readiness_preflight:
  substantive_scope_complete: false
  required_Agent_semantic_review_complete: not_yet
  required_mechanical_checks_complete: not_yet
  blocking_Owner_decisions: [门0, 门1, 门2, 门3]
  further_substantive_commits_expected: true
  explicit_Owner_Draft_request: true   # 工作令 §0.4 明示建 Draft PR
  decision: DRAFT_WITH_RECORDED_EXCEPTION
  reason: 多阶段门控、内容随每门批示变化、后续实质提交必然发生、Owner 明示；不是"大 diff / 一般谨慎"类理由
```

```yaml
owner_review_branch_ledger:
  package_id: FABLE5-REDESIGN-001
  task_id: FABLE5-REDESIGN-001
  repository: 08822407d/Mnemosyne
  base_branch: master
  base_sha: ccd42434b2f946fda78138ba2f5bf66f1f432be1
  working_branch: fable5-redesign-001-workspace
  working_root: notes/cross-model-review-results/FABLE5-REDESIGN-001/
  current_head: (见 git log；本记录提交即首个 head)
  current_question: 门 0——是否进入阶段 0（目标登记表）
  writes_limited_to_review_evidence: true
  execution_source_modified: false
  target_modified_or_activated: false
```

## 3. 指导加载（loader 分层调度）

核心集已读：`README.md`、`current/human-approved-spec.md`（§1–§20）、`current/user-operation-next-step-capability-and-intent-guard.md`、`commands/load-mnemosyne-guidance.md`；另读 `current/guard-registry.yaml`（导航）。

条件件已读（触发理由）：

| guard | 触发 |
|---|---|
| github-single-active-pr-lineage | 建分支/建 PR |
| run-context-and-pr-provenance | 重要写入（设计记录将引导后续 agent） |
| artifact-delivery-and-direct-generation | 阶段 1/3 起草任务书；§3A 完整回复转移文件条款 |
| cross-conversation-execution-intent-and-operator-flow | 阶段 1/3 跨对话任务设计 |
| source-artifact-preservation-and-design-rationale | 材料摄入（A8 私档只读引用）＋重大设计选择 |
| agent-product-ready-pr-and-frontier-efficiency | Draft 例外裁定（§2.2） |
| next-step-repository-write-visibility | 每次回复的下一步含写入 |
| owner-review-branch-ledger | 本轨道即分支承载的多步 Owner 评审 |

未读（当前无触发；到期再读）：external-research-display-name（阶段 1 若出 Deep Research 任务书则读）、deep-research-report-delivery-correction（同上）、frontier-planning-clarification-handoff-adjudication、pr-merge-branch-disposition（转 Ready 请合并时读）。

整编触发检查：注册表基线 MNEMOSYNE-245 后无新增 guard、未满 8 周；影子试点已记一次漏载（C-20）。**本轮无整编到期。**

## 4. 材料完整性核对（工作令 §2）

| 项 | 状态 | 备注 |
|---|---|---|
| A1 owner-goals verbatim | OK（51 行） | |
| A2 REVIEW2 工作令原文 / 08-22 补充指示 | OK（66 / 41 行） | |
| A3 门3 决定记录 / Owner 终审记录 | OK（55 / 42 行） | |
| A4 数字分身愿景记录 | OK（43 行） | |
| A5 Issue #265 | OK | OPEN；正文（TODO 1–4）＋6 条 Owner 评论（TODO 5、三条临时构想补充等）均可经 `gh` 读取 |
| A6 concept-origin-extract-001 / chatgpt-discussion-057 | OK（909 / 91 行） | |
| A7 Alaya 命名决定 | OK（36 行） | |
| A8 Alaya 私档 | OK（只读） | `~/projs/Alaya` @ `7c8b71c`（2026-08-28）；genealogy-origin 31 行；GeodataMaster 1 件；MNE 57 件；MA 26 件；索引 4 份 yaml。读取范围将逐条记入阶段 0 读取清单；引用 ≤200 字/处、不含隐私 |
| B1 执行源 / 注册表 / loader | OK（271 / 150 / 203 行） | |
| B2 MNEMOSYNE-254 复盘对照 ＋ received/ 两份 | OK（72 行 ＋ 2 件） | |
| B3 反模式清单 v1 | OK（34 行） | |
| **B4 MNEMOSYNE-253 审核分工设计稿** | **不在 master** | 仅存在于未合并 PR #316 头分支 `origin/mnemosyne-253-review-assignment-design`（78 行，R2-DESIGN-H，自标 `non_execution_source_advisory_draft`，落点待 Owner 选）。可读，已读；按"未采纳草稿"引用，标 `UNMERGED_DRAFT_NOT_ON_MASTER`。不算 BLOCKED，不替代 |
| B5 风险分布登记簿 / 署名惯例 | OK（448 / 104 行） | |
| B6 FABLE5-REVIEW2-001 全轨道 | OK（54 件） | |
| B7 cross-family-experiments | OK（9 件：EXP-7 七件 ＋ 251/252） | |
| B8 platform-guides | OK（6 件） | |
| C 冻结状态文件 | 存在 | 只作历史，不作路线来源 |
| `project-knowledge/` | 不存在 | 阶段 1 需 Deep Research 材料副本时新建 `project-knowledge/FABLE5-REDESIGN-001/` |

BLOCKED：无。

## 5. run-context（v0.2 紧凑记录）

```yaml
run_context:
  schema_and_task:
    record_version: v0.2
    task_id: FABLE5-REDESIGN-001
    record_id: FABLE5-REDESIGN-001-RUN-001
  date_or_window:
    started_at: 2026-08-30
    completed_or_recorded_at: 2026-08-30（启动仪式；轨道进行中）
  action:
    actor: claude-fable-5
    actor_kind: model
    source: Owner 在新开 Claude Code（VSCode）会话中的启动提示，指向工作令
    switch_history:
      status: confirmed_none
      evidence:
        - class: provider_returned_request_metadata
          ref: Claude Code 会话注入的模型标识（claude-fable-5）与表面上下文；本会话未使用委派子任务
          observed_or_accessed_at: 2026-08-30
          claim_scope: 单一会话、单一模型标识、无子任务
          detail: 平台记录级证据，非密码学证明（署名惯例 §6：Claude Code 表面"较可靠"）
  product_surface:
    value: claude-code-vscode
    evidence:
      - class: provider_returned_request_metadata
        ref: 会话注入的 VSCode 扩展环境块
        observed_or_accessed_at: 2026-08-30
        claim_scope: 执行表面
  operator_selection:
    verbatim: "Fable 5"（Owner 启动提示原话："你是新开的 Claude Code 会话（Fable 5）"）
    evidence:
      - class: direct_user_instruction
        ref: 本会话首条 Owner 消息
        observed_or_accessed_at: 2026-08-30
        claim_scope: Owner 报告的模型选择
  backend:
    status: unknown_or_not_attestable
    reason: 消费者/本地 Agent 表面无 provider 级逐请求后端证明
  artifacts:
    status: recorded
    refs:
      - ref: notes/cross-model-review-results/FABLE5-REDESIGN-001/09-continuation/00-startup-record.md
        relation: created
        immutable_identity: {status: not_available_before_merge, type: git_commit_sha, value: null}
  user_authorization:
    status: authorized
    actor: Owner
    decision_ref: 00-work-order.md（经 Owner 合并 PR #322 生效）＋ 2026-08-30 本会话启动提示
    authorized_actions: [建分支 fable5-redesign-001-workspace, 建 Draft PR, 在两个授权目录新建文件, commit+push, 只读 Alaya/Meta-Agent]
    excluded_actions: [改执行源/guard/loader/状态文件/注册表, 执行 Deep Research, 建立自动化, 写 Alaya/Meta-Agent, 读 Pro 对照设计, 未批示进入下一阶段]
    evidence:
      - class: direct_user_instruction
        ref: 本会话首条 Owner 消息
        observed_or_accessed_at: 2026-08-30
        claim_scope: 授权执行启动仪式并等门 0
    expires_with_task: true
    not_future_precedent: true
  human_adjudication:
    status: pending
    actor: Owner
    decision: 门 0 批示待收
    evidence: []
    limitations: []
  limitations:
    - 同族局限：工作令由 Claude 族起草，本轨道由 Claude 族执行；异构对照留待阶段 3（GPT-Pro）
    - 后端身份不可证明
  omissions:
    - field: [provider_normalization, operator_reasoning_setting, segments, review_events, assessment_refs, recovery_refs, lineage, heterogeneous_review_exception]
      reason: not_applicable
      detail: 启动阶段无切换、无复核事件、无评估、无恢复、无谱系关系、非执行源变更
```

## 6. 阶段计划（工作令 §3，每门等 Owner 一字批示）

| 阶段 | 交付 | 模型要求 | 仓库写入 |
|---|---|---|---|
| 0 目标登记表 | `01-goals-register.md` | 前沿（多源综合、矛盾并列不调和） | 是（本分支） |
| 1 自洽与可行性 | `02-consistency-and-feasibility.md`、`03-research-questions.md`（＋可选 DR 任务书与 `project-knowledge/` 材料副本） | 前沿 | 是 |
| 2 独立重新设计 | `04-redesign-fable.md`（＋附件） | 前沿 | 是 |
| 3 跨族对照准备 | `05-pro-counterpart-package.md` | 前沿（任务书设计）；执行在 GPT-Pro 侧、由 Owner 触发 | 是 |
| 收口 | Draft→Ready、合并建议、`09-continuation/` 检查点 | 次档可 | 是 |
