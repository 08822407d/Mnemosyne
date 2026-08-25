# MNEMOSYNE · 多写入方合作方案联合裁定（议程 A～D）

```yaml
report_id: MNE-FABLE5-REVIEW2-JOINT-COOPERATION-ADJUDICATION-001
track_id: FABLE5-REVIEW2-001
report_role: advisory_joint_confirmation_input
repository: 08822407d/Mnemosyne
reviewed_master: 72b225d6a2faf42639cdc61c8b536439ccfdddce
reviewed_track_branch: fable5-review2-001-workspace
reviewed_track_head: 7483708a80b11c98e050ac37d6c19de36e6a1f17
PR: 306
prepared_in_surface: operator_reported_ChatGPT_with_GitHub_app
operator_selection: operator_reported_GPT_Pro
exact_backend_identity: unknown_or_not_attestable
repository_write_performed: false
external_research_performed: false
authority_level: non_execution_source_advisory_evidence
depends_on: MNE-FABLE5-REVIEW2-PRO-SELFREVIEW-001
```

## 总裁定

```yaml
agenda_A_attribution_scheme: MODIFY
agenda_B_generalize_spec_18: ACCEPT_WITH_MODIFICATION
agenda_C_task_namespace: ACCEPT_WITH_MODIFICATION
agenda_D_cross_family_minimum_practices: MODIFY
joint_confirmation_ready: true_with_explicit_open_disputes
Owner_final_decision_required: true
```

最重要的修改：

1. 一个 `Actor` 字段不足以同时表达“谁生成内容、谁编排、谁实际调用 GitHub 写入”。委派实验证明主会话模板可能覆盖子任务真实模型，因此必须拆角色。
2. 无尾注不能解释为“人类提交”；只能解释为 legacy/unattributed/unknown。
3. ChatGPT GitHub app 在部分低层写入动作中可控制 commit message，但本只读任务没有执行多行 trailer 实验，不能承诺所有 action/surface 都稳定支持。
4. 草案自称有 8 个待确认问题，实际正文只列 6 个。第 7、8 项不能由本报告代写。
5. §18 应泛化为表面无关的仓库动作原则；ChatGPT approval card、Claude permissions、CLI/SSH 等细节移到时效性 surface guide。
6. “终态合同 + 执行方自主”是默认候选，不是无条件原则；授权、隐私、不可逆外部动作、身份和验证隔离仍需要过程约束。
7. 异族抽检按风险触发，不要求每个普通改动都双族复核。

---

## 议程 A · 署名与作者溯源方案

```yaml
agenda: A
verdict: MODIFY
```

### A.1 对三层方案的裁定

| 层 | 原方案 | 裁定 | 修改 |
|---|---|---|---|
| commit trailer | `Actor` + `Task` | MODIFY | 拆分 repository action actor、content producer、orchestrator；仅记录证据允许的身份层级。 |
| 文件头 | created/generated/surface/date + last_updated | MODIFY | 文档类重要文件采用；脚本/数据/分片不强制。保留 created，更新 last_updated；中间历史由 Git 承担。 |
| PR 来源区块 | 固定 Actor/Task/base/path | ACCEPT_WITH_MODIFICATION | 重要写入强制；纯机械低风险任务可用精简自然语言，但仍需 task、action source、授权和 verification。 |

### A.2 建议替代的角色模型

原草案要求“Actor 必须取实际执行模型而非主会话模型”。该方向指出了真实问题，但一个字段仍不足以表达实际链路。建议：

```yaml
attribution_roles:
  repository_action_actor:
    meaning: 实际调用 Git/GitHub mutation、组装并提交 commit 的 actor
  substantive_content_producer:
    meaning: 实际生成或实质修改内容的模型/人/子任务；可多值
  orchestrator:
    meaning: 拆分任务、选择子模型、验收并决定提交内容的主 actor
  semantic_reviewer:
    meaning: 进行了语义审查的 actor；不得与 producer 自动视为独立
  mechanical_verifier:
    meaning: 执行 hash/ref/schema/diff 等机械核验的 actor/process
  Owner_authorizer:
    meaning: 授权任务与高影响动作的人类 Owner
```

委派场景示例：

```yaml
repository_action_actor: claude-fable-5@claude-code-vscode
substantive_content_producer:
  - claude-opus-5@claude-code-subtask
orchestrator: claude-fable-5@claude-code-vscode
semantic_reviewer: same_orchestrator_not_independent
backend_identity: unknown_or_not_attestable_beyond_available_platform_metadata
```

若一个 commit 混合多个子任务，commit trailer 不列长清单，改为 `multiple_see_run_context_ref`。

### A.3 commit trailer 候选文本

```text
Agent-Action-Actor: <repository mutation actor>@<surface>
Agent-Task: <canonical task id>
Agent-Run-Context: <result/run-context ref>
Agent-Content-Producer: <actor | multiple-see-run-context | unknown>
```

约束：

- 值必须与 run-context 证据等级一致。
- Consumer Chat 的 picker 标签不得写成后端证明。
- 无法确认 producer 时写 `unknown`，不继承主会话模型名。
- 机械脚本可写 `mechanical-process@local`，并在 run-context 记录操作者。
- trailer 是索引，不替代完整 provenance record。

### A.4 文件头候选文本

重要新文档：

```yaml
created_by_task:
generated_by_actor:
generated_on_surface:
orchestrated_by_actor:
evidence_for_actor_identity:
```

重要修改：

```yaml
last_updated_by_task:
last_updated_by_actor:
last_updated_on_surface:
```

不要求每个文件写 `date`，Git 已保存提交时间；只有文档语义需要生效/观察日期时才写。对于多 producer 或复杂委派，文件头用 `provenance_ref` 指向 run-context，而不是无限增长字段。

### A.5 PR 来源区块候选文本

```yaml
provenance:
  task_id:
  repository_action_actor:
  substantive_content_producer:
  orchestrator:
  product_surface:
  operator_selection:
  backend:
    status: unknown_or_not_attestable
  base_sha:
  head_sha:
  changed_paths:
  authorization_ref:
  result_or_run_context_ref:
  semantic_review:
  mechanical_verification:
  limitations:
```

与现行 run-context guard 合并使用，不另建一套冲突 schema。

### A.6 草案待确认问题逐项裁定

#### 问题 1：Actor/Task 字段名与取值表

```yaml
verdict: MODIFY
```

- `Actor` 太含混，改为 `Agent-Action-Actor`、`Agent-Content-Producer` 和可选 `Agent-Orchestrator`。
- `Task` 改为 `Agent-Task`，避免与普通正文 trailer 冲突。
- Actor 值应先写 actor/surface，再在 run-context 分开 operator selection、provider metadata 和 backend。
- `gpt-<model>@chatgpt-web` 只有在 `<model>` 是 operator-reported selection 且明确标注时可用；更稳妥的 action actor 是 `ChatGPT@chatgpt-github-app`。

#### 问题 2：文件头最小字段集

```yaml
verdict: MODIFY
```

接受文档类文件头，但最小集应是 task、actor、surface、provenance ref；`date` 与 model 名不是所有文件必需。生成者和编排者必须可区分。

#### 问题 3：PR 来源区块

```yaml
verdict: ACCEPT_WITH_MODIFICATION
```

重要 repository-writing PR 强制；字段增加 authorization、review、mechanical verification 和 limitations。低风险机械改动可压缩，但不能省掉 task/action source。

#### 问题 4：无尾注是否默认为人类；Owner 是否也标

```yaml
verdict: REJECT
```

无尾注只能表示：

```text
legacy_or_unattributed_or_unknown
```

不能证明人类。Owner 手工普通提交不必增加负担；高影响手工动作可在 PR/result 写 `human_owner_manual`。Git author 与 Owner 账号是辅助证据，不等于“无尾注即人类”。

#### 问题 5：历史 Claude 独立文件夹不迁移

```yaml
verdict: ACCEPT
```

历史不改写。新规则生效后按内容组织文件，不按厂商隔离；cross-model-review-results 仍可作为评审内容的自然归档位置。

#### 问题 6：ChatGPT GitHub app 能否稳定携带 trailer

```yaml
verdict: MODIFY_UNKNOWN_SCOPE
```

当前证据：

- 本项目过去通过 ChatGPT GitHub app 的低层 `create_commit`/更新动作生成过调用方指定的 commit message，说明**部分 action path**具备 message 控制。
- 本只读任务没有执行多行 trailer canary。
- 不同 connector action 可能由平台生成默认 commit；不同 ChatGPT surface/rollout 也可能不同。

因此只能裁定：

> ChatGPT 侧可在明确支持 caller-supplied commit message 的 action path 上使用 trailer；写前需读取 action schema，并在第一次提交后 readback。若 action 不支持或 trailer 丢失，PR 来源区块与 run-context 是强制 fallback，不能阻断所有低风险工作。

#### 问题 7、8

```yaml
verdict: REJECT_INPUT_INCOMPLETE
reason: >-
  草案标题和转交包声称有 8 个待确认问题，但文件正文实际只列出 1～6。
  本报告不替起草方猜测或补写第 7、8 项。请 Fable 侧确认是计数错误还是内容遗漏。
```

### A.7 对模型委派实验的显式处理

实验中 Opus 子任务继承了主 Fable 会话的提交署名模板，并错误推断两者是同一模型。这证明：

1. 模板继承不能作为 producer identity。
2. `model self-report` 不是充分证据。
3. Claude Code JSONL 的逐回复 `model` 字段可作为平台记录证据，但仍不是权重级密码学证明。
4. 一个 commit 可能由 orchestrator 提交、subtask 生成内容；两者都必须记录。
5. 子任务固定约 19k token 开销，委派只适合有实质工作量的任务，不应把署名流程本身拆成子任务。

---

## 议程 B · 将 §18 泛化为任意 Agent 写入面

```yaml
agenda: B
verdict: ACCEPT_WITH_MODIFICATION
```

同意泛化方向。现行 §18 的稳定内核已经适用于 ChatGPT、Codex、Claude Code 和未来表面：

- platform capability 不等于 task authority；
- 写入前必须核对 repository、branch、path、protected boundaries；
- 默认 feature branch + PR；
- 高影响动作需要动作前明确 Owner 授权；
- 产品能力是时效事实；
- 重要写入要有 result/run-context；
- 不授权自动写回、自动合并、MCP/RAG 或目标项目写入。

不应继续写在执行源中的 surface-specific 内容：

- ChatGPT approval card / `Allow once`；
- Claude Code permission file、settings、CLI/VSCode 差异；
- Codex attachment 与凭据细节；
- 某个 connector 的参数名；
- 当前订阅/模型/计划能力。

### B.1 建议方向性案文

> ## Repository action capability 与任务授权原则  
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

### B.2 修改原因

- 保留稳定规则，移出时效产品事实，可解决 §10/§14/§18 的重复漂移。
- 现行 run-context guard 已明确适用于 future Agent writes，不应再建平行 provenance 体系。
- “任意 Agent”仍不能等价为“所有表面能力相同”；每个 surface 需要独立 preflight。
- Owner 对 Claude 用户设置的建议授权，不等于 Agent 可以自行修改自身权限；C-02 已证明该边界需要写清。

---

## 议程 C · 任务号命名空间

```yaml
agenda: C
verdict: ACCEPT_WITH_MODIFICATION
```

接受现状追认：

```yaml
task_namespace_policy:
  MNEMOSYNE_NNN:
    role: canonical_mainline_Mnemosyne_maintenance_and_repository_change_tasks
    historical_ids_renamed: false
  long_review_or_research_tracks:
    role: own_stable_prefix_and_sequence
    examples:
      - FABLE5-REVIEW2-001
      - FABLE5-GREENFIELD-001
      - WORK-ULTRA-FABLE-GF5-STAGE-A-001
  target_projects:
    role: target_owned_namespace_in_target_repository_or_workspace
  validation_runs:
    role: run_or_scenario_specific_IDs_under_parent_task
```

附加约束：

1. 每个 repository-writing task 在建分支前搜索 exact task ID、head branch 和 equivalent scope。
2. 轨道 ID 不自动获得 Mnemosyne 主线写入权限；每次动作仍需当前授权。
3. 一个轨道可含多个 run/attempt ID，不应为每个机械重试消耗新的 `MNEMOSYNE-NNN`。
4. 当轨道需要改变 master 的正式现行内容时，建立一个明确的主线实施 task ID 或在 Owner 指令中声明该轨道即 canonical write task。
5. 不建立需要全局锁服务的复杂 task-ID allocator；用轻量 registry/搜索与单 PR preflight 足够，出现真实碰撞后再升级。

---

## 议程 D · 跨族最小惯例

```yaml
agenda: D
verdict: MODIFY
principle: risk_adaptive_minimum_not_universal_maximal_process
```

### D.1 强制惯例

| ID | 惯例文本 | 级别 | 对 ChatGPT 工作方式成本 |
|---|---|---|---|
| D-01 | 重要任务必须冻结终态合同：目标、权限、路径、禁止项、验收证据和停止条件；过程命令只在安全/可逆性需要时规定。 | 强制 | 低；减少过程误解。 |
| D-02 | ref/hash/blob/branch/PR/权限/输入清单/no-write 等可机械核验事项使用 expected/observed/evidence/result；取不到即 BLOCKED/unknown。 | 强制（仅机械事实域） | 中；高风险任务合理，普通文本不使用。 |
| D-03 | 所有 blocking requirement 均有 clean-failure 状态；不得用相近产物、局部完成或流畅解释替代。 | 强制 | 低。 |
| D-04 | 重要写入区分 repository action actor、content producer、orchestrator、reviewer；委派时记录真实 worker 或 unknown，不继承主会话模板。 | 强制 | 中；需 run-context，但提高归因。 |
| D-05 | 新/不熟悉的产品表面在正式工作前做 bounded capability preflight；首笔 mutation 后读回 default/intended refs。 | 强制（首次或变化后） | 低到中；显著减少平台事故。 |
| D-06 | 任务改变 route/status/handoff 时，必须列出被替代指针和执行负向 stale 检查；无编辑授权时至少报告。 | 强制（状态改变任务） | 中；针对最常复发故障。 |

### D.2 默认但有边界的惯例

| ID | 惯例文本 | 级别 | 成本 |
|---|---|---|---|
| D-07 | “终态合同 + 执行方自主”作为有明确权限、可观察终态、可回滚的实现任务默认；身份、隐私、不可逆动作、外部付费、验证隔离和 handoff 仍可规定过程门。 | 默认规则 | 低；防止 brittle transcript，同时保留必要门。 |
| D-08 | 重要架构、执行源、权限、验证结论或跨仓写入由异族抽检；普通 typo/格式/固定机械动作不要求异族复核。 | 风险触发建议/高影响强制候选 | 中到高；控制为抽检而非全检。 |
| D-09 | 指导加载采用 core + conditional；不确定先读。首轮保留抽样 full-read shadow review，记录漏载与成本。 | 试点默认 | 低；EXP-3 支持方向但非跨族定论。 |
| D-10 | 每次新增 guard/流程义务同时给出 overlap、replacement、retirement 与 load-budget 影响；不允许无解释纯加法。 | 默认规则 | 中；直接抑制规则复利。 |

### D.3 “终态合同优先”证据的限定

档案显示 8/20 同时发生：

- 从不可靠传输/对话表面切换到本地 deterministic git；
- 从逐步骤过程合同切换到终态合同 + 执行自主；
- 次日发布成功。

因此只能得出：

```yaml
VERIFIED:
  - both_surface_and_contract_form_changed
  - subsequent_run_succeeded
INFERENCE:
  - terminal_state_contract_likely_reduced_brittleness
NOT_ESTABLISHED:
  - contract_form_alone_caused_success
  - process_contracts_are_generally_inferior
```

### D.4 异族抽检的最低范围

以下任一成立时，应至少一次异族抽检或显式记录为何不做：

- execution source / active global guard 变更；
- authority、privacy、target truth、activation；
- 重大验证 PASS / gate close；
- 新产品表面首次成为正式写入面；
- 多仓库并发或迁移/cutover；
- 先前 actor 发生来源失实或 fabricated evidence；
- 大规模规则整编。

抽检必须记录输入重叠和 reviewer relation；同样读过相同设计稿不等于完全独立。

---

## 明确分歧与交给 Fable/Owner 的问题

```yaml
open_joint_items:
  - id: A-Q7-Q8-MISSING
    GPT_position: 草案实际只有六项，不能裁定不存在的两项
    requested_Fable_response: 确认计数错误或补交原始第7/8项
  - id: A-ROLE-SPLIT
    GPT_position: 一个Actor字段不足，必须拆action actor/content producer/orchestrator
    requested_Fable_response: 接受、修改或说明为何单字段足够
  - id: A-NO-FOOTER
    GPT_position: absence_means_unknown_not_human
    requested_Fable_response: 确认
  - id: A-CHATGPT-TRAILER
    GPT_position: 部分action可控，但未证明跨action稳定；run-context/PR为fallback
    requested_Fable_response: 不应把footer作为解除Claude隔离的单点门
  - id: B-GENERALIZATION
    GPT_position: 接受surface-neutral原则，surface细节外置
    requested_Fable_response: 建议具体guide/registry落点但不得创设第二执行源
  - id: D-FAMILY-PROFILES
    GPT_position: 风险画像可用于抽检，不可写成稳定族性
    requested_Fable_response: 修改两族缺陷表标题与适用范围
```

---

## 最终建议

```yaml
joint_recommendation:
  attribution_scheme: adopt_after_MODIFY_and_Fable_response
  spec_18_generalization: direction_accept_candidate_text_requires_Owner_review
  task_namespace: adopt_as_lightweight_convention
  cross_family_practices: adopt_risk_adaptive_subset
  existing_Draft_PR_306_merge: not_decided_by_this_report
  repository_changes: require_separate_Owner_authorization
```

本报告不解除 Draft PR #306 的门，不批准执行源/guard 修订，不授权 Claude/GPT 在常规路径写入，也不替 Owner 作最终联合确认。
