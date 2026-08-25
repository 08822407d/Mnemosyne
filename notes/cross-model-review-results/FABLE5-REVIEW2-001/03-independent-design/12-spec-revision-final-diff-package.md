# 执行源修订 · 最终逐条对照包（供 Owner 逐条批准）

```yaml
track_id: FABLE5-REVIEW2-001
record_type: spec_revision_final_diff_package
design_id: R2-DESIGN-B-FINAL
created_by_task: FABLE5-REVIEW2-001
generated_by_actor: claude-fable-5
generated_on_surface: claude-code-vscode
date: 2026-08-25
evidence_class: JOINT_CONVERGED_CANDIDATE_TEXT
authority_level: non_execution_source_candidate_text
integration_rule: >
  按联合确认记录第四节（Owner 已批）：修订2 用 Fable 原文；修订1/7 用 Pro 逐字候选文本；
  修订5 用 Pro 精简替代文本；修订3/4/6 由 Fable 按 Pro 裁定方向改写；修订8 为 §18 泛化案文
  （Pro 议程B 十条要点，联合确认记录第二节已批方向）。
sources:
  fable_draft: 03-independent-design/02-design-B-spec-revision-draft.md
  pro_rulings: 07-pro-handover/received/MNE-FABLE5-REVIEW2-PRO-SELFREVIEW-001.md §7.2
  pro_agenda_b: 07-pro-handover/received/MNE-FABLE5-REVIEW2-JOINT-COOPERATION-ADJUDICATION-001.md 议程B
  target_spec: current/human-approved-spec.md（267 行，base master 72b225d）
adoption_gate: >
  本包是任务2（执行源修订）的输入件，非执行源。你逐条批（准/改/驳）后，
  由单独授权的实施任务把获批条目写入 current/human-approved-spec.md（走 §6 流程）。
mechanical_verification:
  - 修订2 引用路径 raw/research-reports/current/research-report-index.md 已核实存在
  - 全部【现行原文】逐字摘自 spec 当前版本（非记忆复述）
```

> **读法**：每条给【现行原文】【最终新文】【裁定来源】【连带影响】。你只需逐条给"准/改/驳"。
> 每条独立可批——驳掉任何一条不影响其他条目。

---

## 修订 1 — §7 会话入场规则（治死条款）

**批示：______**

【现行原文】（§7 标题 "handoff / active-context 原则"）

> - active-context 是当前工作集，不是执行源。
> - handoff-current 是跨会话交接卡，不是完整历史，也不是执行源。
> - 新会话应优先读取 human-approved-spec、active-context 和 handoff-current。
> - raw 和 research reports 按需回查，不默认全量读取。

【最终新文】（标题改为 "会话入场与读取原则"；正文为 Pro 候选文本逐字）

> - 新会话先读取 `current/human-approved-spec.md` 与仓库 AI onboarding 入口。
> - 只有在 Owner 明确选择交接、续接或某条路线时，才读取确切 handoff package、route status 或 task package。
> - `current/active-context.md`、`handoff/handoff-current.md`、TODO、status 与历史记录均不得自动选择任务；其是否为 current、frozen 或 deprecated，以各文件头及执行时 readback 为准。
> - raw 与完整历史按任务需要逐步读取，不默认全量加载。

【裁定来源】Fable 发现死条款（两个指定读物冻结于 2026-07-06）→ Pro MODIFY：不永久宣告 active-context 为历史废件，改按"文件头+readback 定状态"的会话模式化入口 → Fable 接受 Pro 文本。
【连带影响】与实施任务4（三处过期状态修复+冻结头）配套：两个冻结文件加状态头后，本条的"以各文件头为准"即闭环。标题改动是我方提议（原标题描述的正是被移除的机制），可单独驳回保留原标题。

---

## 修订 2 — §5 研究证据层去快照（治过期计数）

**批示：______**

【现行原文】（§5 第一条）

> - 7 份研究报告已经作为 `RC-2026Q2-initial` 轮次证据入库。

【最终新文】（替换该条；§5 其余五条逐字不动）

> - 研究证据按 research cycle 入库；当前有效轮次与报告清单以 `raw/research-reports/current/research-report-index.md` 为权威派生视图，执行源不维护轮次快照。

【裁定来源】Pro ACCEPT（原文方向正确，无修改）。
【连带影响】无；索引文件已核实在位。

---

## 修订 3 — §10 工具角色句产品无关化（治过期绑定）

**批示：______**

【现行原文】（§10 第二条）

> - Codex Cloud 当前主要作为远程 GitHub 文件写入和版本保存助手。

【最终新文】（替换该条；§10 其余边界清单逐字不动）

> - 仓库写入可经多种执行面（远程任务助手、对话内 GitHub app、本地 Agent 工具等）；各执行面的当前能力与限制以经登记的当前平台事实文件为准，执行源不绑定具体产品角色。

【裁定来源】Fable 原案 → Pro MODIFY：不把 `notes/platform-guides/` 具体路径写死进执行源（该入口尚未建成稳定），改指"经登记的当前平台事实索引" → 本文按此改写（去掉硬路径）。
【连带影响】"经登记"的落点由实施任务5（platform-guides 文件族）建成后自然补全；建成前该指引指向现有平台事实类 current 文件（如 claude-github-work-surface-facts.md）。

---

## 修订 4 — §14 平台前提降级（治过期前提）

**批示：______**

【现行原文】（§14 标题与第一条）

> ## 14. Manual import inbox / Codex Cloud non-image attachment boundary
> - Current Codex Cloud task conversations cannot be assumed to receive non-image file attachments directly.

【最终新文】（标题与第一条替换；§14 其余九条安全规则逐字不动）

> ## 14. Manual import inbox 与人工材料转移边界
> - 当材料无法经当前任务的执行面直接进入仓库时，用户可手动放入仓库；首选暂存位置是 `manual-import-inbox/`。

【裁定来源】Fable 原案在正文保留"历史动机注记"→ Pro MODIFY：历史产品动机移至设计/历史记录即可，不必留在执行源正文 → 本文按此删去注记（动机已由本轨道评审文件与 git 历史承载）。
【连带影响】**一处超出已裁定范围的连带微调，可单独打叉**：§14 末条结尾短语 "this rule may be revised if Codex Cloud attachment capability changes" 指向的正是被移除的平台前提，建议同步删去该短语（保留该条其余部分"可见性与平台行为是时效事实须复核"）。你若打叉，末条整条逐字保留。

---

## 修订 5 — 新增 §20 行为约束原则（治规范层无名分）

**批示：______**

【现行原文】无（新增节；spec 现止于 §19）

【最终新文】（Pro 精简替代文本逐字）

> ## 20. 行为约束原则
> - Owner 明确批准的行为 guard 与 process rule，在其声明的适用范围内约束 Mnemosyne 任务；它们仍不是独立执行源。
> - 约束力来自可追溯的 Owner 批准与 scope，不来自文件名、自称 guard 或导航注册状态。
> - guard 与执行源冲突时以执行源为准，并将冲突提交 Owner；不得由执行 Agent 静默重解释。
> - 新建、修订、合并、降级或退役 guard 需要当前任务的明确 Owner 授权，并保留历史与替代关系。
> - guard 的索引、加载分层和整编办法由非执行源指导文件维护；它们不得改变执行源或 Owner 已批准的实质约束。

【裁定来源】Fable 原案（§20 含"注册表在列才有强制力"）→ Pro REJECT_AS_WRITTEN：权力结构过重，注册表不得因"在列"创设强制力 → Fable 接受 Pro 精简文本（强制力只来自 Owner 批准；注册表降为纯导航索引）。
【连带影响】与实施任务3（guard 注册表[仅索引]+loader 分层 shadow pilot）配套；本条不依赖注册表建成即可生效。

---

## 修订 6 — §3 语言分层（治英文长文负担）

**批示：______**

【现行原文】（§3 全文两条，保留不动）

> - 当前阶段中文为主要工作语言。
> - 文件名、目录名、ID、状态值、YAML key、命令、Git/GitHub 术语、工具名和产品名可以使用英文。

【最终新文】（追加两条）

> - 需要用户阅读或决策的材料（决策包、评审报告、PR 说明、操作指引）以中文为主要语言。
> - 面向模型的规范与协议文件可用英文，但须在其登记索引中附中文一句话范围说明。

【裁定来源】Fable 原案另要求"新建规范文件须含中文摘要头"→ Pro MODIFY：逐文件摘要头是新增维护税，索引中的中文 scope 说明已覆盖需求 → 本文按此删去摘要头要求。
【连带影响】存量英文规范的中文 scope 说明随任务3 建注册表时一次性补齐，不专设任务。

---

## 修订 7 — §11 时效钩子（治"过期条款眼皮下无人登记"）

**批示：______**

【现行原文】无（§11 判断优先级列表后追加一条）

【最终新文】（Pro 候选文本逐字）

> - 当任务实际依赖某项平台、产品、订阅或工具事实，且发现执行源或现行行为规则中的相关陈述可能过期、冲突或证据不足时，必须在本任务结果中标注 `stale_or_uncertain`、列出证据与影响，并路由到 Owner 指定的 current issue/open-question/candidate 容器。无相关接触的任务不承担全库时效审计义务。

【裁定来源】Fable 原案（发现即登记为任务义务）→ Pro MODIFY：加 materiality 门槛（"实际依赖"才触发）与免责边界（无接触任务不担全库审计），且不绑定已冻结的 open-questions 文件 → Fable 接受 Pro 文本。
【连带影响】轻量；与 §4 冲突登记义务同构。

---

## 修订 8 — §18 泛化为表面无关原则（合作方案第二节已批方向）

**批示：______**

【现行原文】§18 全节（"ChatGPT GitHub App 写入能力与任务授权原则"，19 条，含 ChatGPT app 细节、Allow once 建议、三级风险分档等）——全文见 spec 237-256 行，此处不重抄。

【最终新文】（整节替换；Pro 议程 B 方向性案文逐字）

> ## 18. Repository action 能力与任务授权原则
> - 本原则适用于任何 AI Agent、自动化工具或人类辅助执行面，对 Mnemosyne、目标项目或验证仓库实施读取以外的 repository action。
> - `platform_capability` 仅说明当前表面技术上可执行某动作；`task_authority` 仅来自当前 Owner 指令、已批准 task package 或其明确引用。二者必须同时成立。
> - 产品、模型、连接器、CLI、IDE、审批卡和权限配置均为时效事实，执行时按对应 surface guide 与实际 action schema 重新核验；执行源不维护具体产品快照。
> - 首次使用或此前未充分验证的写入表面，先做 bounded capability preflight；不得在正式高价值任务中边失败边探索基础能力。
> - 写入默认使用一条 canonical branch、至多一个 canonical PR，并在首笔 mutation 后读回 default ref、intended ref 与实际路径。
> - 任务必须明确 repository、base ref、authorized paths、protected paths、side effects、验证、回滚和分支处置；执行方在边界内可采用适合该表面的工程过程。
> - 直接写默认分支、merge、branch deletion、权限/安全配置、批量外部动作等高影响操作需要动作前的明确 Owner 授权。
> - 重要写入记录 repository action actor、content producer、orchestrator、reviewer、operator selection、backend uncertainty、artifact identities、授权与限制。
> - Agent 不得自行修改其权限配置来扩大自己的能力；Owner 可以手动配置或明确授权由受控机械过程修改。
> - 本原则不授权自动化、自动写回、自动合并、目标项目激活、私有材料摄入或任何未明确批准的外部动作。

【裁定来源】联合确认记录第二节（你已批方向）：稳定内核表面无关化，surface 细节外置。"Agent 不得自行修改自身权限配置"系 C-02 两次实证入法。
【连带影响】被移出的现行 §18 内容**不丢失**，按去向分三类：(a) ChatGPT app 细节、Allow once 建议、三级风险分档示例 → 实施任务5 的 platform-guides 事实文件（时效层，改起来不动执行源）；(b) result record 字段要求 → 新文第八条+现行 run-context guard 已覆盖；(c) 过期声明检测义务 → 修订7 的 §11 钩子承接。替换前实施任务须逐条核对该三类映射无遗漏（已列入任务2 的验收项）。

---

## 汇总批示表

| 修订 | 节 | 一句话 | 文本来源 | 批示 |
|---|---|---|---|---|
| 1 | §7 | 死入口改为模式化入场 | Pro 候选逐字 | |
| 2 | §5 | 去"7 份报告"快照 | Fable 原文 | |
| 3 | §10 | 工具句产品无关化 | Fable 按 Pro 方向改写 | |
| 4 | §14 | 平台前提降为历史 | Fable 按 Pro 方向改写 | |
| 5 | §20 新增 | 行为约束层名分 | Pro 精简替代逐字 | |
| 6 | §3 | 中文优先分层 | Fable 按 Pro 方向改写 | |
| 7 | §11 | 时效发现即登记 | Pro 候选逐字 | |
| 8 | §18 | 泛化为表面无关 | Pro 议程B 案文逐字 | |

批准后的实施路径：获批条目 → 单独授权的主线实施任务（对应实施清单任务2）→ 单分支单 PR 修改 `current/human-approved-spec.md` → PR 说明含逐条映射与本包引用 → 你终审合并。

## 自我批判

1. 修订 3/4/6 的最终措辞是我按 Pro 方向的改写，未经 Pro 回看——三条均为收窄性修改（删硬路径/删注记/删摘要头），越改越少而非越多，风险判断为低 [MODEL_INFERENCE]；你若不放心可在任务7（GPT 侧对照）时顺带请 Pro 复核一眼。
2. 修订 8 的"内容三类去向映射"是我的分类，逐字级核对留给实施任务做验收——本包只承诺分类框架完整，不承诺此刻已逐字核对 19 条。
3. 修订 4 的连带微调（末条短语删除）超出已裁定范围，已单独标出可打叉——这是本包唯一一处我方新增的改动提议。
