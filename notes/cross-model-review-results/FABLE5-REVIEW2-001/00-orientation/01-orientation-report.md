# FABLE5-REVIEW2-001 — 入场定向报告（阶段0）

```yaml
track_id: FABLE5-REVIEW2-001
record_type: orientation_report
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: mixed_per_claim_labels_below
authority_level: non_execution_source_advisory_evidence
execution_source: current/human-approved-spec.md
phase: phase_0_orientation
next_gate: gate_1_owner_review_of_orientation
session_note: >
  首次会话在任何写动作之前因 Owner 误关 VSCode 中断；本报告由续接会话
  重新完成全部入场读取后生成。无上一会话对话记忆被依赖。
```

## 0. 写前 preflight 记录

```yaml
github_write_lineage_preflight:
  task_id: FABLE5-REVIEW2-001
  intended_scope_summary: second_round_composite_review_and_independent_design_new_files_only_under_track_directory
  repository: 08822407d/Mnemosyne
  repository_visibility: public          # VERIFIED via GitHub REST API 2026-08-22
  default_branch: master
  pinned_default_branch_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce   # git fetch --prune 后 origin/master
  intended_branch: fable5-review2-001-workspace
  branch_enumeration:
    method: git_fetch_prune_then_git_branch_a
    remote_branches:
      - master
      - mnemosyne-240-preservation-capsule          # 工作令列为禁触分支，保留不动
      - mnemosyne-242-post-pr303-closeout-and-handoff  # 工作令列为禁触分支，保留不动
    complete: true
  open_pr_enumeration:
    method: GitHub_REST_API_pulls_state_open_per_page_100
    open_pr_count: 0
    pagination_complete: true
    all_accessible_open_prs_checked: true
  matches:
    by_exact_task_id: []
    by_intended_head_branch: []
    by_equivalent_scope: []
    existing_result_records_or_task_artifacts: []   # track 目录此前不存在
  single_active_pr_guard_conflict: none
  decision: create_new_lineage
  working_tree_before_branch: clean
  notes:
    - gh_CLI_not_installed_on_this_machine_open_PR_enumeration_used_read_only_REST_API
    - git_ls_remote_over_SSH_timed_out_once_but_git_fetch_prune_succeeded_enumeration_based_on_fresh_fetch
first_write_action_completed:
  file: 00-orientation/00-owner-work-order-verbatim.md
  commit: 489cbfa
```

## (a) 重建的项目现状全貌

以下每条标注主张等级。VERIFIED_REPOSITORY_FACT 简写 VRF；MODEL_INFERENCE 简写 MI。

### a.1 项目定位与执行源

- [VRF] Mnemosyne 是"记忆系统元 Agent"设计仓库，为其他 AI Agent 项目设计外部持久记忆系统；核心原则"模型负责计算，文件负责记忆"（`current/human-approved-spec.md` §1–2；`README.md`）。
- [VRF] 执行源 v0.1 共 19 节，自 2026-07-13 以来未再修改（`git log -- current/human-approved-spec.md`：最后两次改动为 1d2799a "MNEMOSYNE-113 add no-write proof and review provenance principle" 与 20f83f2 "MNEMOSYNE-116 require guidance refresh in Mnemosyne handoffs"，均 2026-07-13）。
- [VRF] 仓库 public；master 为默认分支；本地与 origin/master 一致于 72b225d6（2026-08-21，PR #305 合并 MNEMOSYNE-243 AI onboarding）。
- [VRF] 仓库共 2360 个提交（2026-05-26 首提交至 2026-08-21），任务号已推进到 MNEMOSYNE-243。

### a.2 治理与行为层（第一轮后大幅增厚）

- [VRF] `current/` 下现有约 15 个用户批准的行为 guard（第一轮时点主要只有 meta-agent 对齐 guard 与 handoff 命令），新增包括：single-active-PR lineage guard（MNEMOSYNE-118）、artifact-delivery guard（125/127）、run-context/PR provenance guard（147/149）、cross-conversation execution-intent 与 operator-flow guard（185/187）、PR branch-disposition guard（196/197）、source-artifact preservation guard（198）、owner-review branch ledger guard（207）、next-step write-visibility guard、user-operation/capability/intent guard、external-research display-name guard、deep-research delivery correction guard 等（`ls current/`，各文件头部 created_by_task）。
- [VRF] 2026-08-21 新增仓库原生 AI onboarding 包（MNEMOSYNE-243，PR #305）：`notes/ai-onboarding/` 下的 AUTHORITY-AND-EVIDENCE、REPOSITORY-MAP、CLAUDE-CODE-LOCAL-START、TAKEOVER-CHECKLIST 等——即本轨道入场所用文件。
- [MI] 治理层的增厚几乎全部由真实事故驱动（116 双 PR 事故→118；#170/#171 交付失败→125/127；PR 277 Draft 误用→210 修订；235–239 发布事故→240 恢复架构），呈"事故→guard"的自愈模式。

### a.3 当前活动路线状态（截至 base_master_sha）

- [VRF] **无活跃选定主线**。live wayfinding（`current/post-interruption-live-wayfinding-status.md`，MNEMOSYNE-197 更新）声明 `route: no_active_selected_mainline_after_FCV_indefinite_pause`。
- [VRF] **Fable 前沿澄清验证路线（FCV，MNE-DR-001/002）被 Owner 无限期暂停**（MNEMOSYNE-196，2026-08-06；`current/fable5-research-delivery-status.md`）：A1 曾一次输入完整性失败（操作者报告成本约 $8）与一次 Project-knowledge 探针（约 $7，低成本门 FAIL），无有效实质报告；恢复需在独立专用对话中显式批准。**本轨道 FABLE5-REVIEW2-001 是 Owner 新授权的独立轨道，不恢复、不关闭该暂停路线。**
- [VRF] **F2 跨仓库安全并发路线（MNE-DR-005）是最新的实质工作线**（`current/fable5-cross-repository-safe-concurrency-research-status.md`，MNEMOSYNE-242 更新）：V2-A A0 sentinel 已执行并被 Owner 接受为 PASS_WITH_BOUNDED_EVIDENCE_DEFECTS；A1 packages 001–004 已封存；修正后的 G2A 外层模板经 PR #303 发布；当前门 = 运行机械校验器后由 Owner 单独决定是否签发 A1 controller G2A。`G2A_issued: false`、`A1_execution_authorized: false`。
- [VRF] **Meta-Agent 已完成专属仓库迁移**：target truth 现位于 `08822407d/Meta-Agent@master:current/approved-spec.md`（cutover merge eb71ed35），Mnemosyne 侧旧入口经 PR #261 退役；`target-projects/meta-agent/` 仅为历史 bootstrap 与 rollback source（`README.md`；`current/meta-agent-dedicated-repository-pre-migration-status.md`）。本轨道对 Meta-Agent 仓库零操作（工作令禁令）。
- [VRF] 发布事故链：MNEMOSYNE-235~239 五个任务先后 BLOCKED_CLOSED_NO_RETRY，240 形成恢复架构与持久暂存 capsule（分支 mnemosyne-240-preservation-capsule 保留），241 作为发布载体成功（PR #303），242 closeout（分支 mnemosyne-242-post-pr303-closeout-and-handoff 保留）。两个保留分支即本轨道的禁触分支。
- [VRF] 其他路线（Adaptive Explanation Stage B0、HO-GUIDANCE-001、Model-capability planning、GPT live learning 等）均 selected_here: false，处于等待显式选择状态（live wayfinding §5）。

### a.4 验证与验收状态

- [VRF] Meta-Agent 测试路线：五个 REG-META-DRYRUN 规格已形式化，cleanroom 行为 replay 5/5 PASS，但机械 no-write 子门与组合包门保持 BLOCKED（`current/review-and-validation-status.md`）。
- [VRF] artifact-delivery 验证 Cases 001–004 PASS，Case 005 NOT_RUN（条件未自然触发）；Issues #170/#171 closed。
- [VRF] W4（用户验收警告）保持 open_uncertain，未发生真实项目验收（同上文件 Pro adjudication outcomes 节）。
- [MI] 整体验收模式：行为层验证较充分，机械证明层与"真实使用"层始终未闭合——这是贯穿两轮的结构性验收债（详见 (c) 与 (d)）。

## (b) 与第一轮时点的关键变化（git log 证据）

### b.0 第一轮时点校准

- [VRF] 工作令称第一轮"约 MNEMOSYNE-113，2026-06 末"。git 证据：FABLE5 评审件 canonical 入库为 2026-07-07~08（PR #135~#141，MNEMOSYNE-088~094），MNEMOSYNE-113 Pro 裁定合并于 **2026-07-13**（PR #160），GREENFIELD 轨道收尾存档至 **2026-07-21**（PR #194，MNEMOSYNE-143 存 GF-STEP-5）。评审对话本身可能发生于 6 月末~7 月初，但仓库时间线上第一轮闭环在 7 月中下旬。本报告以 2026-07-13（MNEMOSYNE-113 合并）为第一轮基准时点。
- [VRF] 自该时点至 base_master_sha：约 130 个任务号（113→243）、约 145 个已合并 PR（#160→#305）、40 天。

### b.1 变化时间线（按 PR 合并日期，均 VRF）

| 时段 | 任务/PR | 内容 |
|---|---|---|
| 07-13 | 113–114 (#160–161) | 第一轮 findings Pro 裁定闭环；post-113 维护交接 |
| 07-13~15 | 115–122 (#162–172) | 五个 REG-META-DRYRUN 规格形式化；**116 双 PR 事故**（#163/#164）→117 调解→**118 single-active-PR lineage guard**；replay 系列评审与 cleanroom replay |
| 07-15~20 | 123–125, 127, 137–139 (#173–176, 178, 188–190) | DR6 平台 delta 研究入库；artifact-delivery guard 与验证闭环（Issues #170/#171 关闭） |
| 07-16~21 | 126, 128–136, 141–143 (#177–187, 192–194) | Fable 配额恢复后 GREENFIELD 轨道续跑并存档：GF-STEP-2B5→2C→2D→3A→3B→4→3R→3RV→**GF-STEP-5 对比报告** |
| 07-21~23 | 144–151 (#195–202) | 模型质量重启检查点；DR-07 对比与 Fable5 治理研究入库；run-context/PR provenance guard v0.2 |
| 07-23~26 | **152–162 (#203–213)** | **GF-STEP-5 后续闭环**：Stage A 独立评估→Stage B reveal 与交叉裁定→Pro maintainer 裁定（10 条 GF5-TRIAGE 全部处置）→PRO-SLICE-01 patch spec→Phase A 11 patch + Phase B 18 patch 实施→路线 COMPLETE |
| 07-26~28 | 163–172 (#214–224) | 模型能力感知工作规划；四题研究入库；升级契约试点；**Meta-Agent M0-M1 启动与 v0.1 七文件构建**（作为目标项目） |
| 07-28~30 | 173–187 (#225–241) | Adaptive Explanation Stage A/B0；前沿澄清研究与验证包；Fable 交付重设计（184）；operator-flow / execution-intent guards |
| 07-31~08-05 | 188–195 + meta-agent-* (#242–262) | Fable research Project-knowledge surface；研究显示名 guard；**Meta-Agent 专属仓库迁移与 Mnemosyne 侧退役（PR #261）**；FCV 恢复准备 |
| 08-06 | **196–197 (#263–264)** | **Fable 路线无限期暂停**（含未来恢复 handoff 包）；分支保留通知制度化 |
| 08-10~13 | 198–208 (#266–276) | source-artifact preservation guard；runtime guidance 利用率评审；**Owner review 系列（OR01 起）**；target lifecycle baseline；owner-review branch ledger |
| 08-14~18 | 209–234 (#277–302) | TLR owner-review ledger；v0/v1/v2 裁定；F2 能力归属裁定；**MNE-DR-005 跨仓库并发 V2-A**：A0 sentinel 执行并获 Owner 接受、A1 packages 001–004、handoff-003 行为演练、readiness PASS、G2A 组合闭合被阻→Pro 修正模板 |
| 08-18~21 | 235–243 (#303–305) | **发布事故链 235–239 全部 BLOCKED_CLOSED_NO_RETRY**→240 恢复 capsule→241 发布成功（PR #303）→242 closeout→**243 AI onboarding 包**（本轨道入场文件） |

### b.2 结构性变化归纳

1. [VRF] **执行源冻结而治理层膨胀**：spec 40 天零修改，同期新增 10+ 个 guard、多个 registry/adjudication/validation 目录。规则增量全部进入非执行源层。
2. [VRF] **工作重心从"设计文档"转向"验证运行"**：F1/F2 路线引入 sentinel run、G2A 授权门、机械校验器脚本（`notes/validation-tools/validate_and_fill_mne_v2a_a1_controller_g2a.py`）、独立验证仓库（08822407d/mnemosyne-target-lifecycle-validation-002）。
3. [VRF] **第一个目标项目完成完整生命周期**：Meta-Agent 从 bootstrap workspace → v0.1 构建 → 专属仓库迁移 → Mnemosyne 侧 writer 退役。
4. [VRF] **Owner review 成为显式机制**：OR01–OR09 包、owner-review branch ledger、owner-decision-candidates/results 目录。
5. [VRF] **Fable 参与方式变化**：第一轮 Fable 是评审/对比设计主力；此后 Fable 承担 Stage A/B、治理研究、F2 报告，但 FCV 研究路线因成本与表面问题于 08-06 无限期暂停；本轨道是暂停后 Fable 的首次新任务授权（依据：工作令；[MI] 关于"首次"—仓库中未见 08-06 后其他 Fable 新轨道记录，若 Owner 另有未入库 Fable 工作则此判断失效）。

## (c) 第一轮 findings 与设计建议落实情况逐条核对

### c.1 FABLE5-REVIEW-001（6 条，全部闭环）

| Finding | 第一轮裁定 | 当前核验 | 主张 |
|---|---|---|---|
| F-001 frozen startup prompt 过期状态 | MNEMOSYNE-088 修复 | findings.yaml 记 accepted_repaired；088 于 #135 合并 | VRF |
| F-002 同族自证据模式 | 接受为观察，限定独立性 | spec §19 已含同族证据限制标注规则（§19 第 7 条） | VRF |
| F-003 todo 遗漏 080 | 088 修复 | findings.yaml 记 accepted_repaired | VRF |
| F-004 maintainer review provenance | 用户答复后关闭 | §19 要求记录实际 reviewer/actor；113 记录 GPT 维护对话执行、用户未逐步核验 | VRF |
| F-005 equivalent no-write 证据范围 | 关闭：历史单次例外 | spec §19 明文 not_future_precedent 规则 | VRF |
| F-006 评审件仓库归宿 | notes/cross-model-review-results/ 为 canonical | 该树现存 9 个轨道目录且持续使用（含本轨道） | VRF |

### c.2 FABLE5-REVIEW-002（4 条，全部闭环）

| Finding | 裁定 | 当前核验 | 主张 |
|---|---|---|---|
| R2-F-001 W4 范围模糊 | live interpretation 层记 W4 open/uncertain | live-interpretation 文件在位（e4c3ec2, 2026-07-13）；review-and-validation-status.md 记 W4 remains open_uncertain | VRF |
| R2-F-002 warning 列表漂移 | 分层 canonical 化（Q2-2 决定） | 113 决定记录完整；冻结件未改写 | VRF |
| R2-F-003 regression 候选仅指针 | live status 文件 + root 指针 | `current/review-and-validation-status.md` 在位且 README 指向之 | VRF |
| R2-F-004 warning 无 per-item 状态 | live 层加稳定 ID/状态/归属 | live-interpretation 承载该角色 | VRF |
| （Q2-3 附带）regression 议程 | 113 仅立议程不形式化 | **后续 115 已把 REG-META-DRYRUN-001/002/004/005/007 形式化**，定义级静态 replay PASS；但机械 no-write 门至今 BLOCKED | VRF |

### c.3 FABLE5-REVIEW-003（4 条，全部闭环）

R3-F-001（历史残留不修）、R3-F-002（089 批准补注）、R3-F-003（inbox README 标 superseded，文件在位 3344 字节）、R3-F-004（live 指针补齐）——均按 113 裁定落实并可在仓库核验。[VRF]

### c.4 FABLE5-GREENFIELD-001 与 GF-STEP-5 十条 triage 的落实

- [VRF] 轨道走完 GF-STEP-1~5 全部步骤并逐步存档（manifest + manifest-supplements MNEMOSYNE-130~143）。
- [VRF] GF-STEP-5 之后的落实链：Stage A（独立评估，152/#203）→ Stage B（reveal 与交叉裁定，153/#204；52 项 GF5 清单核对：31 corroborated / 17 partial / 4 Fable-only）→ **PRO-FABLE-GF5-MAINTAINER-ADJUDICATION-001**（decision-matrix.yaml 对 10 条 GF5-TRIAGE 全部给出 verdict/route；Stage B integrity ACCEPT、methodology ACCEPT_WITH_MODIFICATION、implementation readiness **REJECT**）→ **PRO-SLICE-01**（existing_hard_contract_propagation）v2 patch spec 全量实施：Phase A 11 patch（157/#208）+ Phase B 18 patch（160/#211），路线 2026-07-26 COMPLETE（`current/pro-slice-01-patch-specification-status.md`，verified_master 11df4679）。
- 十条 triage 逐条现状：

| GF5-TRIAGE | Pro 裁定路由 | 当前落实核验 | 主张 |
|---|---|---|---|
| 001 FR-01/03 表面 delta 研究 | DEFER_RESEARCH | 未见专项 FR-01/03 refresh 记录；后续平台事实经 DR6(07-15)与 claude-github-work-surface-facts(08-15)部分更新，但非该研究本身 | UNKNOWN_REQUIRES_EVIDENCE（是否另有入库） |
| 002 单 spec vs 因式分解 | 拆分：P1 current 修 + 用户决定延后 | C-01 ACCEPT_BOUNDED_CURRENT_REPAIR + defer execution_source_factoring；spec 未因式分解（40 天未改） | VRF |
| 003 DP02/03/04/07/14 参数确认 | ACCEPT_CANCELLATION（不做整轮参数确认） | 无整轮参数确认记录，与裁定一致 | VRF |
| 004 constraint-refresh 操作 | P1 硬契约传播 | 纳入 PRO-SLICE-01 scope（receive_report_then_separate_guidance_refresh），已实施 | VRF |
| 005 no-write 例外结构 | P1 硬契约传播 | 纳入 PRO-SLICE-01 scope（mechanical_no_write_evidence_and_fail_closed_status），已实施 | VRF |
| 006 write-lineage 失败类 | 降为 P3 可移植性候选 | 未实施；CUR-04 系 guard 继续演进（196/197 分支处置） | VRF |
| 007 no-re-ask 约定 | NO_ACTION | 无动作，一致 | VRF |
| 008 spec 中过时机制迁出 | RESEARCH_VOLATILE_FACTS_KEEP_STABLE_PRINCIPLES | spec 未改；平台事实类文件另立（claude-github-work-surface-facts 等）；是否算落实待阶段1 评估 | MI |
| 009 owner-continuity | P3 watch | 无新记录 | VRF（无动作，符合 watch） |
| 010 overfitting 处置/自动化时机/语言政策 | 捆绑拆分处置 | 语言政策未变（§3）；自动化 fence 未变（§10）；无专项记录 | VRF（无动作） |

- [VRF] **验收边界保持诚实**：greenfield 架构整体从未被采纳（implementation readiness REJECT）；被实施的只有硬契约传播切片。第一轮所有 `substantive_maintainer_acceptance: not_performed` 标记中，GF-STEP-5 一件经 Stage B + Pro 裁定获得了实质维护者处置；GF-STEP-1~4 各步产出仍保持 advisory、未逐步实质验收（其价值已通过 Stage A/B 汇总消化——[MI]）。

### c.5 未落实/仍开放项汇总

1. [VRF] 机械 no-write 组合门（Meta-Agent replay）BLOCKED 未闭合。
2. [VRF] W4 真实项目验收 open_uncertain。
3. [VRF] artifact-delivery Case 005 NOT_RUN。
4. [VRF] HO-GUIDANCE-001（目标项目交接是否加载 Mnemosyne 指导）仍 unresolved（`current/handoff-guidance-open-question.md`）。
5. [UNKNOWN_REQUIRES_EVIDENCE] GF5-TRIAGE-001 的 FR-01/03 表面研究是否以其他形式完成。
6. [VRF] F2 路线停在 Owner G2A 决定门前。

## (d) 本轮评审计划与信息缺口

### d.1 阶段1 复合评审拟按主题分件（提议，待门1 批示）

| 文件 | 主题 | 对照 |
|---|---|---|
| 01-spec-core-needs-coverage.md | 执行源 §1–2 核心需求在当前仓库的实现覆盖与偏差 | §1–2 |
| 02-spec-section-conformance.md | §3–19 逐节符合性（含 spec 冻结 40 天下的规则漂移检查：guard 层是否出现实质上该进 spec 的新全局规则） | §3–19 |
| 03-freshness-and-staleness.md | 新鲜度：研究证据老化（RC-2026Q2 主体已 3 个月）、平台事实时效（§10/§14/§18）、**live 状态文件相互过期**（已见：review-and-validation-status greenfield 节停在 GF-STEP-2C；post-interruption-live-wayfinding 停在 197，未反映 198–243） | §5/§11/§18 隐含 |
| 04-acceptance-debt-register.md | 验收债台账：全部 BLOCKED/NOT_RUN/open_uncertain/not_performed/DEFER 清点与风险分级 | §19 隐含 |
| 05-cost-and-process-weight.md | 成本与流程重量：每任务仪式开销、发布事故链 235–241 的成本教训、guard 数量与 onboarding 负担、Fable 路线成本记录（$8+$7 失败探针） | 隐含非功能 |
| 06-single-point-risks.md | 单点风险：单维护者/owner-continuity、单一 GPT 维护族依赖、Fable 暂停后异构评审空窗、public 可见性纪律 | 隐含非功能 |
| 07-scalability-and-multi-target.md | 可扩展性：多目标项目并发（F2 设计的对象）、Meta-Agent 迁移经验的可复用性、validation 仓库模式 | §9/§16 |
| 08-first-round-deferred-items-recheck.md | 第一轮 DEFER/WATCH 项在两个月后的复检（GF5-TRIAGE-001/006/008/009/010 等） | — |

### d.2 已确认的信息缺口（阶段1 需补读）

1. `current/open-questions.md`（43KB）、`current/todo.md`、`current/active-context.md` 全量——本阶段仅读结构。
2. Owner review 系列实体（`notes/owner-review-packages/`、`owner-decision-results/`、OR01–OR09）。
3. F2 验证设计与 HVAL（`notes/validation-designs/`、`notes/validation-run-decisions/`、A1 packages 001–004）。
4. `handoff/` 目录清单与 Fable 恢复包内容（仅在需要证据时定点读，保持冷源纪律）。
5. `raw/research-reports/` 索引与新研究周期（DR-07、四题研究、2026Q3 delta）的清单。
6. GitHub Issues 状态（open issues 未枚举；可用只读 REST API 补）。
7. WORK-ULTRA-FABLE-GF5-STAGE-A/B 归档 tar 的正文（如阶段1 需要 Stage B triage-ledger 细节则解包核验）。
8. [UNKNOWN_REQUIRES_EVIDENCE] 是否存在未入库的会话侧决定影响上述任何状态——仓库无法自证，默认以仓库为准。

### d.3 与第一轮方法的衔接

- 本轮沿用第一轮的主张标签纪律与"证据路径逐条附注"格式（工作令要求，且与 `MNEMOSYNE-AUTHORITY-AND-EVIDENCE.md` 标签集对齐）。
- 同族证据限制照 §19 声明：本轨道作者（claude-fable-5）与第一轮评审/greenfield 作者同为 Fable 家族，且本会话已完整读过第一轮结论——本轮对第一轮工作的复检不构成异构独立评审；对**第一轮之后 GPT 侧工作**的评审则具备跨族视角。[MI]

## 返回契约（本会话）

```yaml
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
branch: fable5-review2-001-workspace
head_after_this_commit: to_be_recorded_in_commit   # 本文件与其提交即 head
changed_paths:
  - notes/cross-model-review-results/FABLE5-REVIEW2-001/00-orientation/00-owner-work-order-verbatim.md
  - notes/cross-model-review-results/FABLE5-REVIEW2-001/00-orientation/01-orientation-report.md
protected_paths_untouched:
  - current/** (含 human-approved-spec.md 与全部 guard/status)
  - 既有 notes/**、handoff/**、raw/**、target-projects/**、commands/**、README.md
  - 分支 mnemosyne-240-preservation-capsule、mnemosyne-242-post-pr303-closeout-and-handoff
  - 未创建根 CLAUDE.md / AGENTS.md
validation_method:
  - 入场读取按工作令顺序完成（spec、onboarding 三件、第一轮全部正典结论件）
  - GF-STEP-5 正文自 base64+gzip 分片重建并 SHA-256 校验通过（82a5c8ee…f48bfe）
  - 时间线以 git log --merges --first-parent 重建；关键状态以 current/ 状态文件交叉核验
  - 写前 preflight 完整记录于本报告 §0
evidence_class_summary: VERIFIED_REPOSITORY_FACT_for_all_repository_claims_MI_and_UNKNOWN_labeled_inline
known_limitations:
  - gh CLI 缺失，open-PR 枚举依赖只读 REST API（结果 0 个 open PR）
  - PR 创建（Draft 绑定）尚未执行：本机无 gh 亦无已配置的 API 写凭据；见"下一个门"操作项
  - open-questions/todo/active-context 未全量读（列入阶段1 缺口）
  - 本会话未执行任何外部验证运行
next_gate: 门1 — Owner 审阅本定向报告并批示是否进入阶段1（及 d.1 分件方案是否调整）
```
