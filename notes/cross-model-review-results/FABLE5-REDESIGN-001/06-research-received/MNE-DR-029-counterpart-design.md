# MNE-DR-029 · GPT-5.6 Pro 对照总体方案

**任务 ID：** `FABLE5-REDESIGN-001-CP1 / MNE-DR-029`  
**执行表面：** ChatGPT 官方普通对话，模型选择器为 Pro；本报告按 GPT-5.6 Pro 对照设计身份作答。模型标签属于本次表面观察，不等同于可独立验证的运行时遥测。  
**日期：** 2026-08-31  
**设计状态：** `DESIGN-COMPLETE / PRE-FREEZE`——方案已完整形成，但在 §8 的冻结前效果测试通过之前，不宣称生产冻结。  
**边界：** 仅使用任务书及任务书 §2B 所列 12 份附件；没有搜索其他仓库路径或外部资料；没有修改 GitHub 仓库。

## 执行结论

本方案不把“模型像 CPU、context 像 RAM、Git 像硬盘”继续当作规范性总模型，而把它降为一个**可推翻的教学类比**。规范性架构改为：

> **Owner 目的与授权 → 耐久核心 → 可再生投影 → 任务工作态/检查点 → 上下文编译器 → 可替换的概率模型后端 → 确定性工具闸门。**

耐久核心仍以 Git 中人类可读、可审查、可整体迁移的文件为唯一规范根；但“发生过什么”“现在有效什么”“这次任务要加载什么”不再由同一类文件、同一摘要或同一超长对话承担。系统采用**轻量语义账本 + 当前有效文档 + 可重建派生层**，而不是一次性引入完整数据库或纯事件溯源平台。

### 证据标记

- **[OWNER]**：Owner 在目标登记表或裁决包中的直接要求。
- **[EVIDENCE]**：12 份附件中的研究、实测或工程结论。
- **[INFERENCE]**：本方案基于材料做出的设计合成，尚未由本项目实测。
- **[UNKNOWN]**：材料不足或尚未通过本项目实验验证，禁止伪装成事实。

## 材料完整性核验

12 份附件均从任务书给出的对应直链抓取，按 UTF-8 完整读取并核验尾部；合计 **434,921 字节**。未发现缺件、截断或主题替换。

| # | 文件 | UTF-8 字节数 | 首行 | 状态 |
|---:|---|---:|---|---|
| 1 | `01-goals-register.md` | 28,670 | `# FABLE5-REDESIGN-001 · 目标登记表（门 0 交付 · v1）` | 完整 |
| 2 | `02a-contradiction-clarification-package.md` | 14,041 | `# 矛盾点澄清包 · 第一轮（阶段 1 开工件）` | 完整 |
| 3 | `foundational-agent-antipattern-checklist-v1.md` | 4,693 | `# 基础 Agent 反模式清单 v1（Meta-Agent 与项目 agent 立项前置检查）` | 完整 |
| 4 | `MNE-DR-020-report.md` | 42,042 | `# MNE-DR-020 / FABLE5-REDESIGN-001-RQ1 · 平台能力刷新` | 完整 |
| 5 | `MNE-DR-021-report.md` | 50,638 | `# MNE-DR-021 / FABLE5-REDESIGN-001-RQ2 · 跨会话连续性实践与评测` | 完整 |
| 6 | `MNE-DR-022-report.md` | 43,904 | `# MNE-DR-022 / FABLE5-REDESIGN-001-RQ3 · 需求生命周期与状态演化管理` | 完整 |
| 7 | `MNE-DR-023-report.md` | 49,489 | `# MNE-DR-023 / FABLE5-REDESIGN-001-RQ6 · 文件/Git 真相源上的检索与按需加载` | 完整 |
| 8 | `MNE-DR-024-report.md` | 47,826 | `MNE-DR-024 / FABLE5-REDESIGN-001-RQ7 · 交接效果评测工具与小样本测试方法` | 完整 |
| 9 | `MNE-DR-025-report.md` | 42,582 | `# MNE-DR-025 / FABLE5-REDESIGN-001-RQ8 · 学习者建模与教学计划生成的证据现状` | 完整 |
| 10 | `MNE-DR-026-report.md` | 40,770 | `# MNE-DR-026 / FABLE5-REDESIGN-001-RQ9 · 开发知识资产与自用代码库实践` | 完整 |
| 11 | `MNE-DR-027-result.md` | 2,520 | `## MNE-DR-027 实测结果` | 完整 |
| 12 | `MNE-DR-028-report.md` | 67,746 | `# MNE-DR-028 / FABLE5-REDESIGN-001-RQ13 · 总体架构抽象模型复核` | 完整 |

> 字节数按抓取到的完整 UTF-8 字节流计算；首行按原文件保留。此表只证明本次输入材料完整，不证明附件中引用的所有外部研究已被本次执行独立复核。



# 1. 架构总览

## 1.1 设计名称与定位

本方案称为 **“可重建权威—投影—工作集架构”**（Reconstructible Authority–Projection–Working-set Architecture，简称 **RAPW**）。

RAPW 不是一个独立于具体 agent 的终端产品；它是 Mnemosyne 用来为具体 agent 设计、维护和验证持久记忆系统的参考架构。[OWNER：`01-goals-register.md` N-16]

它吸收但不照搬三类公开先例：

1. Git/文档中心的人类可读、可审查、可迁移接口；
2. 事件/账本的 provenance、supersession 与状态演化语义；
3. working state、checkpoint、context compiler 与确定性治理的分层。

它刻意不采用“所有事件都进入一个高频事件存储”的纯事件溯源，也不采用“把所有文件变成一个大向量库”的纯检索中心。两者都超出当前证据和个人维护预算。[EVIDENCE：`MNE-DR-023-report.md` Q3/Q7；`MNE-DR-028-report.md` Q4/Q5]

## 1.2 七层结构

```text
┌──────────────────────────────────────────────────────────┐
│ L0 Owner Purpose & Authority                             │
│ 目标、授权、审批边界、目的核查、Owner-touch 预算          │
└──────────────────────────────┬───────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────┐
│ L1 Durable Core                                            │
│ 原始证据、裁决、当前有效规范、规则单元、需求状态、测试真值 │
└──────────────────────────────┬───────────────────────────┘
                               │ 受控变更 / 同一变更集
┌──────────────────────────────▼───────────────────────────┐
│ L2 Regenerable Projections                                 │
│ 人类视图、任务包、索引、摘要、模型专用提示/适配器          │
└──────────────────────────────┬───────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────┐
│ L3 Task Working State & Portable Checkpoint                │
│ 当前目标、已完成、未决、下一动作、环境/工件状态             │
└──────────────────────────────┬───────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────┐
│ L4 Context Compiler / Loader                               │
│ 适用性硬过滤、按需读取、token 预算、装载回执                │
└──────────────────────────────┬───────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────┐
│ L5 Probabilistic Model Adapter                             │
│ GPT / Claude / Gemini / 开源模型；可替换、需重新验证        │
└──────────────────────────────┬───────────────────────────┘
                               │
┌──────────────────────────────▼───────────────────────────┐
│ L6 Deterministic Tool & Policy Gates                       │
│ 权限、schema、测试、hook、lint、审批、写入前预检            │
└──────────────────────────────────────────────────────────┘
```

横贯七层的两个独立停止闸门是：

- **完整性闸门（fail-closed）**：材料缺失、版本冲突、权限/表面能力不明、校验失败时，禁止猜测性继续。
- **目的闸门（purpose-closed）**：即使材料完整，若动作不再服务 Owner 目标、只是增加形式或维护负担，也必须缩减或停止。

## 1.3 权威语义

RAPW 坚持“一个规范根”，但不把不同问题强塞给同一个文件：

| 问题 | 唯一权威位置 | 说明 |
|---|---|---|
| Owner 到底要求什么 | 耐久核心中的目标、裁决和当前需求记录 | 模型记忆、对话摘要无权覆盖 |
| 当时发生了什么 | 原始证据包和不可覆盖的变更/决定记录 | 后续可追加纠正，不静默改写历史 |
| 现在应执行什么 | Owner 批准的当前有效规范/需求/规则 | 历史记录不得凭“更新”或相似度重获执行权 |
| 这次工作到哪里 | 当前任务检查点 | 任务局部，不升级为全局事实 |
| 本模型怎样最好读取 | 可再生模型专用投影 | 可删、可重建、不可反写规范层 |
| 某动作是否允许 | 模型外权限、测试、hook、审批闸门 | 自然语言规则不是强授权边界 |

“历史权威”与“当前权威”不是两份互相竞争的真相：前者回答“发生过什么”，后者回答“现在有效什么”。每个 authority domain 只有一个 canonical 文件或目录；派生视图只能引用它。[INFERENCE，依据：`MNE-DR-022-report.md` Q1–Q4；`MNE-DR-028-report.md` Q4]

## 1.4 轻量语义账本，而非全量事件溯源

每一次**语义性变更**——目标变化、需求接受/推迟、规则新增/撤销、决策 supersede、验证结果改变——形成一个原子“变更集”：

1. 新增不可覆盖的 `change record`；
2. 更新对应的当前有效文档；
3. 更新 trace links；
4. 运行机械校验；
5. 在同一 Git commit/PR 中提交。

普通聊天 token、每次文件读取和每个中间推理不进入语义账本；只有对长期状态有重建价值的事件进入。这样保留 provenance，又避免把个人项目变成运维一个完整 event platform。[INFERENCE]

若 change record 与当前文档不一致，状态为 `BLOCKED_INTEGRITY`：不由模型选择“更像真的”一边，而是回到源证据和 Owner 裁决修复。

## 1.5 原“类冯诺依曼”模型的保留边界

[OWNER：`02a-contradiction-clarification-package.md` X-1] 要求该类比只能作为可被更强证据推翻的默认。RAPW 的处理是：

| 旧类比 | 可保留的教学意义 | 不得作为的系统保证 |
|---|---|---|
| 模型≈CPU | 可替换计算后端 | 确定执行、稳定 ISA、同 prompt 同结果 |
| context≈RAM | 有限运行期工作集 | 随机可寻址、装入即可靠使用 |
| Git 文件≈硬盘 | 耐久、人读、可迁移 | Git 自动赋予 authority、并发和一致性语义 |
| 规则≈程序 | 组织和审查接口 | 模型看到文本就等于强制执行 |
| handoff≈快照 | 可移植应用检查点 | 捕获模型内部全部隐藏状态 |

因此，类比可以保留在说明文档中，不能作为 schema、权限、恢复或测试的依据。[EVIDENCE：`MNE-DR-028-report.md` Q2]


## 1.6 现行机制的去留与抛弃理由

任务书允许抛弃 H 类机制猜想，但要求逐项说明。RAPW 的处理如下：

| 现行/既有机制 | 裁决 | 理由 |
|---|---|---|
| “模型=CPU、context=RAM、Git=硬盘”作为**规范性总体模型** | **抛弃** | 模型非确定、context 非随机可寻址、规则/数据无天然隔离、handoff 非完整进程快照；继续字面化会制造错误保证。[EVIDENCE：MNE-DR-028 Q2] |
| 同一类 Markdown 同时承担原始历史、当前状态、执行说明 | **抛弃** | 容易让 stale/superseded 内容重新获得执行权，也无法明确“发生过什么”与“现在有效什么”。[EVIDENCE：MNE-DR-022；MNE-DR-028 Q4] |
| Git/人类可读文件作为长期规范接口 | **保留并收窄** | 它最符合 Owner 可读、审计和跨模型迁移；但 authority、状态机和写入规则需显式补上，Git 本身不自动提供。 |
| 模型/产品原生 memory、会话摘要作为长期真相 | **抛弃为权威源；仅作缓存** | 表面、账户和模型依赖强，非逐字、不可保证完整，也不适合跨供应商迁移。[EVIDENCE：MNE-DR-020、021] |
| 超长主线对话承担路由、发布、验收与交接 | **抛弃** | 依赖隐含上下文、难冷启动、污染大、Owner 成为消息总线；改为 task-bound checkpoint/handoff。 |
| 全量历史/所有规则默认加载 | **抛弃** | 违反 N-19；额外上下文可能降低正确性、增加成本和 stale 使用。[OWNER：N-19；EVIDENCE：MNE-DR-023、026] |
| 既有 quick card + full package 两层交接思想 | **保留并强化** | 增加可移植 checkpoint、机械 receipt 与预冻结配对评测，使其从文档习惯变成可验证机制。[OWNER：O-05；EVIDENCE：MNE-DR-021、024] |
| “一次事故→加一条全局规则” | **抛弃** | 容易规则膨胀和错作用域；改为 evidence→reproducer→test/eval→必要时规则。 |
| 直接引入完整 event sourcing/database/vector stack | **暂不采用** | 材料支持其局部价值，也明确指出复杂度、迁移和维护风险；只有真实故障和 eval 触发才升级。[INFERENCE] |



# 2. “耐久核心 / 可再生层”文件组织

## 2.1 建议目录

以下是逻辑目录，不要求现有仓库一次性重排；迁移步骤见 §9。

```text
mnemosyne/
├─ durable/
│  ├─ 00-governance/
│  │  ├─ goals/                         # Owner 目标与成功标准
│  │  ├─ adjudications/                 # Owner 裁决
│  │  ├─ purpose-policy/                # 目的核查规则
│  │  └─ behavior-rules/                # N-17 可整体迁移的唯一规则单元
│  │     ├─ RULESET-INDEX.yaml
│  │     ├─ rules/R-*.md
│  │     ├─ checks/
│  │     └─ migration-manifest.yaml
│  ├─ 10-evidence/
│  │  ├─ raw-input/                     # 原话、原文件、完整反馈材料
│  │  ├─ research-originals/            # 研究原件/报告，非默认加载
│  │  ├─ feedback-bundles/
│  │  └─ evidence-manifests/
│  ├─ 20-analysis/
│  │  ├─ claims/                        # 经检查的事实/推断
│  │  ├─ proposals/                     # 待裁决构想
│  │  ├─ conflicts/
│  │  └─ rejected-deferred/
│  ├─ 30-current/
│  │  ├─ requirements/
│  │  ├─ decisions/
│  │  ├─ specifications/
│  │  ├─ operating-profiles/            # 每任务/项目节奏与预算
│  │  └─ agent-designs/
│  ├─ 40-ledger/
│  │  ├─ changes/YYYY/MM/CHG-*.yaml
│  │  ├─ supersession/
│  │  └─ reconciliation/
│  ├─ 50-work/
│  │  └─ <task-id>/
│  │     ├─ checkpoint.yaml
│  │     ├─ handoff/
│  │     ├─ load-receipts/
│  │     └─ outputs/
│  ├─ 60-verification/
│  │  ├─ frozen-cases/
│  │  ├─ oracles-private-or-referenced/
│  │  ├─ regression/
│  │  ├─ result-ledger/
│  │  └─ calibration/
│  └─ 70-assets/
│     ├─ reusable-code/
│     ├─ skills/
│     ├─ environment-contracts/
│     └─ templates/
├─ regenerable/
│  └─ <generation-id>/
│     ├─ PROJECTION-MANIFEST.yaml
│     ├─ human-views/
│     ├─ current-state-snapshots/
│     ├─ task-context-packs/
│     ├─ indexes/lexical/
│     ├─ indexes/vector/
│     ├─ summaries/
│     └─ model-adapters/
└─ runtime/
   └─ <session-id>/                      # 临时 scratch；默认不作长期真相
```

## 2.2 “耐久”不等于“常驻加载”

耐久核心的判定标准是：**删除后是否会丢失不可安全重建的事实、Owner 意图、权威状态或验证真值**。它与 prompt 是否常驻无关。原始资料可以很耐久，却因毒性和噪声只在审计时加载；模型专用短摘要可以每次常驻，却仍是可删的派生物。[OWNER：N-15、N-19]

耐久核心包括：

- Owner 原始目标、裁决、授权与关键原话；
- 原始证据、完整反馈包及其完整性说明；
- 经 Owner/流程接受的当前需求、规范和规则；
- 决策、supersession、defer/reject 记录；
- 任务检查点和已冻结 handoff/eval 真值；
- 可执行测试、环境 contract、回归资产；
- 所有派生层的生成规范和 source binding。

可再生层包括：

- 摘要、目录、当前状态展示页；
- FTS/BM25、embedding、图索引；
- task context pack；
- 模型专用 prompt/instruction projection；
- 针对某个表面生成的工具调用说明；
- 聚合报表和可视化。

## 2.3 每一代模型的可再生层必须显式标注

`generation-id` 不使用含糊的“latest”，建议构成为：

`<provider>__<model-label>__<surface>__<valid-as-of>__proj-v<schema>`

例如本次表面可写成：

`openai__gpt-5.6-pro__chatgpt-web-ordinary__2026-08-31__proj-v1`

这只是标签，不主张已知内部运行时 model revision。每个 `PROJECTION-MANIFEST.yaml` 必须包含下列完整字段：

| 字段 | 必需 | 含义 |
|---|---:|---|
| `generation_id` | 是 | 派生代唯一 ID |
| `built_for_provider` | 是 | 供应商 |
| `built_for_model_label` | 是 | 界面/配置中可见模型标签 |
| `model_identity_evidence` | 是 | `official_doc / surface_observed / owner_declared / self_report_only / unknown` |
| `built_for_surface` | 是 | 普通对话、deep research、API、CLI 等 |
| `valid_as_of` | 是 | 平台事实有效日期 |
| `source_root` | 是 | 唯一规范根 |
| `source_revision` | 是 | Git commit/ref 或冻结清单 |
| `source_hash_manifest` | 是 | 输入源及 hash |
| `projection_schema_version` | 是 | 派生结构版本 |
| `generator_id` | 是 | 生成器/流程 ID |
| `generator_version` | 是 | 生成逻辑版本 |
| `generated_at` | 是 | 生成时间 |
| `scope_included` | 是 | 纳入的 authority/task scope |
| `scope_omitted` | 是 | 明确排除的 scope |
| `toxicity_policy_version` | 是 | 装载分类规则版本 |
| `determinism_class` | 是 | `deterministic / model-assisted-reviewed / model-assisted-unreviewed` |
| `integrity_status` | 是 | `valid / stale / conflicted / rebuild_required` |
| `rebuild_triggers` | 是 | 源变更、模型变更、schema 变更等 |
| `expires_at_or_review_trigger` | 是 | 到期或复核条件；不得永久无期限 |
| `known_limitations` | 是 | 已知遗漏/不兼容 |
| `supersedes_generation` | 是 | 可为空；被替代代 |
| `superseded_by_generation` | 是 | 可为空；后继代 |

任何字段缺失都不能由模型猜补；状态改为 `rebuild_required` 或 `blocked_unknown`。

## 2.4 N-17 行为规范单元

[OWNER：`02a-contradiction-clarification-package.md` X-2 / N-17] 当前所有行为规范继续共同存放在 Mnemosyne，但必须从一开始就是**可整体迁移的独立单元**：

- 只有 `durable/00-governance/behavior-rules/` 有规范写权；
- 其他 agent、项目和派生 prompt 只引用稳定 `rule_id`；
- 每条规则记录 `scope`、`source_owner_decision`、`evidence`、`enforcement_mode`、`last_verified`、`sunset/review trigger`、`supersedes`；
- 可执行的规则优先编译为 test/hook/lint/schema；自然语言文本只负责解释和模型提示；
- 迁移到 Meta-Agent 时移动整个单元并改一份 canonical root manifest；旧位置只留重定向，不保留第二份可编辑副本。

规则不得因“更通用”而自动晋升。至少满足：重复故障或明确 Owner 原则、作用域可界定、现有机制不能更低成本表达、存在退出条件、通过新上下文负测；否则留在任务局部。[EVIDENCE：反模式 #4、#7、#15；`MNE-DR-026-report.md` Q4/Q6]

## 2.5 通用耐久记录头

所有耐久记录使用同一最小头部；不同类型可追加字段，但不能删除下列字段：

| 字段 | 含义 |
|---|---|
| `artifact_id` | 稳定唯一 ID |
| `artifact_type` | `goal / owner_adjudication / evidence / claim / proposal / requirement / decision / rule / checkpoint / handoff / feedback / test / asset / change` |
| `schema_version` | 记录 schema 版本 |
| `canonical_status` | `canonical / reference / derived / archive` |
| `authority_domain` | 本记录在哪个问题域有权威 |
| `lifecycle_state` | 该类型的完整状态枚举之一 |
| `scope` | agent / project / task / path / time / surface |
| `created_at` | 创建时间 |
| `created_by` | Owner、模型、脚本或 agent ID |
| `source_refs` | 原始证据指针 |
| `source_hashes` | 可用时保存 hash |
| `valid_from` | 生效起点 |
| `valid_to` | 失效点，可为空但必须有 review trigger |
| `last_verified_at` | 最近验证 |
| `verified_by` | 人/机械 oracle/模型及证据级别 |
| `supersedes` | 被替代记录 ID 列表 |
| `superseded_by` | 后继记录 ID 列表 |
| `sensitivity` | `public / private / restricted / secret-reference-only` |
| `toxicity_class` | §5 定义的装载等级 |
| `model_binding` | `model-neutral` 或具体代 |
| `surface_binding` | `surface-neutral` 或具体表面 |
| `change_id` | 产生本版本的变更集 |
| `integrity_status` | `valid / stale / conflicted / incomplete / quarantined` |
| `notes_on_unknowns` | 明确 UNKNOWN，不以空白代替 |



# 3. “原始资料 → 经检查构想 → 实现层”三态循环

## 3.1 三态定义

RAPW 把长期知识分成三种权限完全不同的状态：

| 状态 | 主要内容 | 能否直接驱动执行 | 默认装载 |
|---|---|---:|---:|
| **S0 原始资料（RAW EVIDENCE）** | Owner 原话、完整任务书、反馈、研究原件、工具输出、历史 trace | 否 | 否 |
| **S1 经检查构想（CHECKED CANDIDATE）** | 带证据的 claim、设计候选、冲突分析、风险、INFERENCE/UNKNOWN | 否；只能供裁决 | 条件加载 |
| **S2 实现层（APPROVED EXECUTION）** | 当前有效需求、裁决、规范、规则、实现、测试、环境 contract | 是，按 scope | 是，按任务直接相关性 |

这对应目标登记表 O-13 的“历史真相 / 分析真相 / 执行真相”，但本方案把“真相”一词收窄为不同 authority domain，避免候选分析被误当执行命令。[OWNER：`01-goals-register.md` O-13；N-14]

## 3.2 状态转换

```text
外部输入 / Owner 反馈 / 实现结果
               │
               ▼
         S0 RAW CAPTURED
               │  完整性检查、来源绑定、隐私处理
               ▼
        S1 CHECKED CANDIDATE
        ├─ conflict ───────► 冲突记录 / Owner 裁决
        ├─ defer ──────────► deferred queue
        ├─ reject ─────────► rejected archive
        └─ accept
               │  决策、验收条件、scope、测试
               ▼
        S2 APPROVED EXECUTION
               │
               ├─ 实现/运行产生新证据
               ├─ 用户纠正产生反馈包
               └─ 新模型/新平台/新需求触发重评
                          │
                          └──────────────► 新的 S0
```

转换是**单向晋升 + 新事件回环**，不是覆盖式改写：

- S0 不会因分析完成而删除；若原文含错误，追加纠正记录。
- S1 被接受后仍保留当时替代方案和证据，但失去执行权。
- S2 被替代时产生新的 S2 和 supersession 关系；旧 S2 转入历史，不被静默修改成“当初就这样想”。
- 实现失败不回写原需求为“从未接受”；新增 `failed_validation` 证据并回到分析。

## 3.3 S0：完整捕获，但不信任

[OWNER：N-02、N-06] 原始捕获的目标是防止意义丢失，而不是把所有输入升级为指令。最小规则：

1. 对 Owner 关键表述保存逐字文本或原文件；若只能摘要，必须同时保留可回溯原件指针。
2. 工具输出、研究原件、其他 agent 内容保留 producer、时间、表面、参数和权限上下文。
3. 任何自动 redaction 都产生一份 redaction manifest；原始敏感材料可保存到受限位置或只留 hash/外部安全引用。
4. 无法合法或安全保存的部分标记 `capture_gap` 与原因，不得以“已完整记录”掩盖。
5. S0 标签默认是 `TOXIC_RAW` 或 `SEMI_TOXIC_RESEARCH`，不会被 context compiler 当作指令。

这直接回应裁决包中 Owner 对非逐字 AI 记录遗失意义的实际经历。[OWNER：`02a-contradiction-clarification-package.md` 后续回填]

## 3.4 S1：检查构想的最低要求

任何 S1 构想必须回答：

- 它试图服务哪个 Owner goal / requirement？
- 哪些句子是直接证据，哪些是推断？
- 是否存在相反证据或旧裁决？
- 适用 scope、valid_at、模型/表面条件是什么？
- 如果采用，如何验证；如果失败，如何回滚？
- 是否会新增全局规则、Owner-touch 或长期维护成本？
- 是否有更小、更局部的方案？
- 何时应 defer、reject 或重新研究？

缺任一关键项时不自动补齐，而是状态 `blocked_unknown` 或保持 `analysis_pending`。

## 3.5 S1 → S2 的晋升门

只有同时满足以下条件才可进入实现层：

1. 有明确的目标和 Owner authority；
2. 没有未解决的同权威冲突；
3. 需求/规则状态允许执行；
4. 写明接受标准、负约束和停止条件；
5. 高风险变更有机械检查或 proof-gap 记录；
6. 目的核查通过；
7. Owner-touch 预算未被突破；
8. 变更集同时更新 provenance、当前态和测试；
9. 模型生成内容不能自行给自己最终批准，除非已有 Owner 预授权与机械 oracle。

## 3.6 实现层的反馈回流

实现层不是终点。每次以下事件都生成新的 S0 evidence bundle：

- Owner 明确纠正或表达不满；
- 机械测试失败；
- 模型做出不必要动作或违反负约束；
- 环境/表面能力与记录不一致；
- 交接后出现 rediscovery、stale-value 使用或误拒；
- 新模型表现改变；
- 资产复用造成错作用域/错误移植。

重复故障的晋升顺序是：

`反馈证据 → 可复现 case → eval/test/hook/lint → 必要时才是简短行为规则`

而不是：

`一次事故 → 全局 prompt 再加一条`。

[EVIDENCE：`MNE-DR-026-report.md` Q4/Q6；反模式 #4、#7]



# 4. 需求生命周期状态机

## 4.1 完整状态枚举

每条需求只能处于下列一个主状态；禁止自由文本状态：

| 状态 | 可执行性 | 说明 |
|---|---:|---|
| `captured` | 否 | 已逐字/原件捕获，未分流 |
| `triage_pending` | 否 | 待分类目标、scope、风险、来源 |
| `analysis_pending` | 否 | 正在澄清、研究或拆解 |
| `conflict_pending` | 否 | 与现有需求/裁决冲突，等待解析 |
| `blocked_unknown` | 否 | 缺关键材料、能力或权限；必须干净停止 |
| `owner_decision_pending` | 否 | 已形成可裁决选项，等待 Owner |
| `accepted` | 是（设计/计划） | Owner 或预授权流程已接受，尚未规划实现 |
| `planned` | 是 | 已有实现/验证计划 |
| `implementing` | 是 | 正在实现 |
| `verification_pending` | 否（不得宣称完成） | 实现已产出，等待机械/人工验证 |
| `verified_current` | 是 | 验证通过且当前有效 |
| `failed_validation` | 否 | 未通过验收；保留失败证据 |
| `deferred` | 否 | 暂缓，必须有原因和重启触发器 |
| `reassessment_pending` | 否（旧 current 可按规则暂时维持） | 新模型、平台、反馈、依赖或风险触发重评 |
| `rejected` | 否 | 经裁决不采用 |
| `withdrawn` | 否 | Owner 撤回或需求源取消 |
| `superseded` | 否 | 被明确后继需求替代 |
| `retired` | 否 | 曾有效，但因生命周期结束退役 |

`reassessment_pending` 的特殊规则：若来源是 `verified_current`，旧版本在没有安全/完整性风险时可以保持当前执行权，直至重评完成；若触发原因标记 `quarantine_required=true`，则立即停止执行。新模型出现本身不会自动激活 deferred 需求，也不会自动废止旧实现。[OWNER：N-03、N-05；EVIDENCE：`MNE-DR-022-report.md` Q2/Q3]

## 4.2 允许的主要转换

| From | To | 必要条件 |
|---|---|---|
| `captured` | `triage_pending` | 原始证据可定位；敏感性已标 |
| `triage_pending` | `analysis_pending` | scope/goal 初步确定 |
| `triage_pending` | `blocked_unknown` | 缺关键原件、权限或上下文 |
| `analysis_pending` | `conflict_pending` | 发现同权威冲突 |
| `analysis_pending` | `owner_decision_pending` | 选项、证据、风险齐全 |
| `analysis_pending` | `deferred` | 当前不可行但有重启条件 |
| `analysis_pending` | `rejected` | 已有充分反证或不服务目标 |
| `conflict_pending` | `owner_decision_pending` | 冲突已整理成可裁决包 |
| `owner_decision_pending` | `accepted / deferred / rejected / withdrawn` | 明确裁决或 Owner 行为 |
| `accepted` | `planned` | 计划、验收标准、Owner-touch 预算齐全 |
| `planned` | `implementing` | 执行闸门通过 |
| `implementing` | `verification_pending` | 实现产物固定 |
| `verification_pending` | `verified_current` | 验收通过 |
| `verification_pending` | `failed_validation` | 任一主 oracle 失败 |
| `failed_validation` | `analysis_pending / deferred / rejected` | 记录失败并选择后续 |
| `deferred` | `reassessment_pending` | 命中已登记 trigger |
| `verified_current` | `reassessment_pending` | 模型/平台/反馈/依赖/定期测试触发 |
| `reassessment_pending` | `analysis_pending / owner_decision_pending / verified_current / deferred / superseded` | 重评结果 |
| `accepted / planned / implementing / verified_current` | `superseded` | 新记录明确替代；不得原地改写 |
| 非终态 | `withdrawn` | Owner 撤回 |
| `verified_current` | `retired` | 作用域或产品生命周期结束 |

所有非法转换由 schema/lint 拒绝；若业务需要新状态，必须先升级 schema，而不是写一个临时字符串。

## 4.3 需求记录完整字段

每条 `REQ-*` 除 §2.5 通用头外，必须含：

| 字段 | 说明 |
|---|---|
| `requirement_text_verbatim` | Owner 原话或逐字摘录 |
| `normalized_intent` | 经检查的规范表达 |
| `goal_refs` | 对应 N/O/X 目标或上层目标 |
| `source_evidence_refs` | 原材料 |
| `request_class` | `goal / constraint / option / hypothesis / preference`（对应 N-12） |
| `state` | §4.1 完整枚举之一 |
| `scope` | agent/project/task/path/surface/time |
| `priority` | Owner 指定或 `unknown` |
| `risk_class` | `low / medium / high / critical / unknown` |
| `acceptance_oracles` | 机械、闭池或人工 rubric |
| `must_include` | 正约束 |
| `must_not_include` | 负约束 |
| `dependencies` | 前置需求/能力 |
| `conflicts_with` | 冲突 ID |
| `decision_refs` | Owner/流程裁决 |
| `implementation_refs` | 设计、代码、配置、工件 |
| `verification_refs` | 测试与结果 |
| `defer_reason` | `model_capability / platform_capability / evidence_gap / owner_priority / resource / dependency / risk / other / not_applicable` |
| `revisit_triggers` | 模型事件、日期、依赖、反馈、阈值 |
| `quarantine_required_on_trigger` | 布尔值 |
| `current_effect` | `none / design_authority / execution_authority` |
| `owner_touch_budget_ref` | 对应运行配置 |
| `unknowns` | 不确定项及获取办法 |
| `next_required_action` | 唯一下一状态动作 |
| `closure_reason` | 终态原因 |

## 4.4 新前沿模型触发重评

“新前沿模型”没有可自动可靠识别的通用定义，故采用显式 `MODEL-EVENT`：

1. 捕获表面可见模型标签、供应商、入口、日期和证据级别；
2. 不把模型自报当运行时遥测；
3. 将事件与上一已验证模型代绑定；
4. 查询 `defer_reason in {model_capability, platform_capability}` 且 `revisit_triggers` 匹配的需求；
5. 将这些需求转为 `reassessment_pending`；
6. 同时运行冻结回归集，检查既有 `verified_current` 是否退化；
7. 形成差异报告，只有有意义的能力变化才进入 Owner 裁决；
8. 通过 Owner/预授权门后，才重新进入 `accepted` 或 `planned`。

这满足“新模型触发复核”而不把“新”误作“更好”。[OWNER：N-03、N-05；EVIDENCE：`MNE-DR-020-report.md` 平台/模型身份边界；`MNE-DR-022-report.md` Q3]

`MODEL-EVENT` 必须记录：

- `event_id`
- `provider`
- `model_label`
- `surface`
- `observed_at`
- `identity_evidence`
- `previous_generation`
- `capability_claims`
- `claims_evidence`
- `affected_requirement_query`
- `regression_suite`
- `owner_review_needed`
- `unknowns`
- `valid_as_of`

## 4.5 反馈全材料捕获

每次会改变需求、规则、测试或实现的反馈，形成一个 `FEEDBACK-BUNDLE`，完整字段如下：

| 字段 | 说明 |
|---|---|
| `feedback_id` | 唯一 ID |
| `received_at` | 时间 |
| `source_actor` | Owner/用户/测试/agent/tool |
| `verbatim_feedback` | 原话；不能保存时说明 |
| `capture_mode` | `verbatim / redacted_with_hash / secure_reference_only / incomplete` |
| `conversation_or_task_ref` | 所属任务 |
| `affected_goal_requirement_rule_refs` | 影响对象 |
| `triggering_input` | 导致输出的输入或指针 |
| `model_output_or_action` | 被反馈对象 |
| `model_surface_and_label` | 表面与标签 |
| `loaded_source_receipt` | 当次实际装载集合 |
| `tool_actions_and_results` | 工具调用 |
| `environment_manifest` | 环境与版本 |
| `expected_behavior` | 期望 |
| `observed_behavior` | 实际 |
| `impact_and_severity` | 影响 |
| `reproduction_steps` | 可复现步骤 |
| `artifacts` | 文件、截图、日志、安全引用 |
| `privacy_and_retention` | 敏感性、保留策略 |
| `initial_analysis` | S1 分析，标证据/推断 |
| `candidate_fix` | 候选修复 |
| `regression_case_ref` | 转化后的测试 |
| `resolution_state` | `captured / analyzed / test_added / fixed / verified / deferred / rejected / blocked_unknown` |
| `closure_evidence` | 关闭依据 |

“完整”是相对于明确的隐私/安全保留政策；不能保存的材料必须有 gap 记录，禁止默默省略。

## 4.6 定期测试与触发测试

[OWNER：N-06、N-18] 不设全局统一节奏。每个 agent/project 的 `operating-profile` 必须声明：

- 主线性质；
- 交互节奏；
- review cadence；
- handoff test cadence；
- model-change trigger；
- feedback-to-regression SLA 或事件条件；
- Owner-touch 预算；
- 暂停/冻结窗口。

测试分两类：

**事件触发：** 模型代、平台入口、GitHub 连接、schema、规则单元、projection generator、重大需求或权限发生变化时立即运行。

**声明节奏：** 按任务/项目自己的 cadence 运行固定 anchor；例如每 N 次真实 handoff、每个阶段门、或迁移前后，而不是“所有项目每周一次”。

测试结果只追加到 result ledger；聚合报告从原始结果重算，不人工改总分。[EVIDENCE：`MNE-DR-024-report.md` Q6]



# 5. 加载 / 投影机制：记录 ≠ 加载 ≠ 呈现

## 5.1 N-19 的机械化实现

[OWNER：`02a-contradiction-clarification-package.md` X-3 / N-19] 规定：

- 默认装载：执行源 + 当前任务直接材料；
- 任务包只在接收任务的上下文加载；
- 已完成主线只在复核时懒加载；
- 原始想法有“毒性”，未经检查不得进入执行上下文；
- 研究原件“半毒性”，默认不加载；
- 边界必须被弱模型按清单执行，而不是依赖哲学理解。

RAPW 将其变成六级装载类：

| 类别 | 标签 | 默认行为 | 典型内容 |
|---|---|---|---|
| L0 | `EXECUTION_CORE` | 必装，但仅装与任务直接相关部分 | 当前目标、当前需求、当前规则、权限 |
| L1 | `TASK_DIRECT` | 必装 | 当前 checkpoint、handoff、直接输入、验收 |
| L2 | `VALIDATED_REFERENCE` | 条件触发 | 已检查研究结论、稳定设计说明、环境 contract |
| L3 | `HISTORY_LAZY` | 默认不装 | 已完成主线、旧决定、旧实现、事故历史 |
| L4 | `SEMI_TOXIC_RESEARCH` | 只有显式研究/审计任务才装 | 研究原件、长报告、来源摘录 |
| L5 | `TOXIC_RAW` | 隔离装载，不得作为指令 | 原始想法、未审 agent 输出、外部不可信文本 |

L4/L5 被装载时，context compiler 必须加一个机器可见边界：`data_only=true`、`instruction_authority=false`，并在可能时使用工具/权限隔离。自然语言标签不能单独构成安全边界；关键工具仍由 L6 闸门控制。[EVIDENCE：`MNE-DR-028-report.md` Q2 的 instruction/data 边界]

## 5.2 装载算法

每次任务按以下固定顺序执行：

1. **绑定任务**：确定 `task_id`、goal、pace、checkpoint、model/surface。
2. **硬适用性过滤**：
   - canonical status；
   - authority domain；
   - scope/path/task；
   - lifecycle state；
   - `valid_from ≤ as_of < valid_to` 或 review trigger；
   - model/surface binding；
   - sensitivity/permission；
   - source hash 与 projection integrity。
3. **装入 L0/L1**：只取直接适用的当前执行源和任务直接材料。
4. **检查覆盖缺口**：所需目标、约束、下一动作、验收、环境是否齐全。
5. **检索候选**：
   - 先目录/manifest/path/ID；
   - 再 `rg`/关键词；
   - 需要排名时用 FTS/BM25；
   - 只有项目检索集证实存在持续 lexical miss，才启用 dense；
   - 只有 sparse 与 dense 各自存在独立 critical miss，才启用 hybrid。
6. **按毒性与 token 预算裁剪**：优先短、权威、当前、直接证据；预算未用完不是继续装材料的理由。
7. **生成 load receipt**。
8. **模型作答后记录真正引用的 source spans**；未使用的上下文计入污染指标。

适用性、版本和 authority 必须先 hard gate，再做相关性排序；不能用高 cosine score 决定哪个版本当前有效。[EVIDENCE：`MNE-DR-023-report.md` Q4/Q6]

## 5.3 Load Receipt 完整字段

每次模型调用或任务阶段至少保存：

| 字段 | 说明 |
|---|---|
| `receipt_id` | 唯一 ID |
| `task_id` | 任务 |
| `checkpoint_id` | 工作态版本 |
| `model_generation_id` | 模型/表面 |
| `compiled_at` | 时间 |
| `as_of` | 事实时间 |
| `loader_policy_version` | 装载规则 |
| `token_budget` | 输入预算 |
| `mandatory_sources` | L0/L1 清单及 hash |
| `retrieved_sources` | L2–L5 清单及 hash |
| `source_spans` | 实际片段 |
| `load_reason_per_source` | 目标、规则或查询触发原因 |
| `toxicity_class_per_source` | 装载等级 |
| `authority_per_source` | 权威域 |
| `hard_filters_applied` | scope/state/time/model/privacy |
| `omitted_candidates` | 因预算、失效、冲突、权限而省略 |
| `integrity_checks` | hash/schema/validity |
| `conflicts_detected` | 冲突 |
| `unknowns` | 缺口 |
| `estimated_input_tokens` | 估算 |
| `actual_input_tokens_if_available` | 表面可得时记录；否则 UNKNOWN |
| `used_source_refs` | 输出实际依赖 |
| `pollution_labels` | irrelevant/wrong-scope/wrong-version/unused |
| `status` | `valid / incomplete / conflicted / blocked_unknown` |

## 5.4 可再生投影

投影分两类：

**人类投影：** 当前状态页、决策索引、需求看板、可读 handoff。目标是 Owner 可浏览、可纠正，不要求模型专用。

**模型投影：** 某一模型/表面适配的最短规则包、任务上下文包、tool contract 摘要、索引。它必须标注“为哪一代模型而建”，并在模型/表面变化时重新验证。

任何投影遵守四个 invariant：

1. 可以删除并从耐久核心重建；
2. 每一条都能回到 source path + revision/hash + span；
3. stale 时最多降低检索/性能，不能改变 authority；
4. 模型生成投影不能自动反写 current 规范。

## 5.5 检索升级触发器

不按仓库 MB、文件数或上下文窗口宣传值升级。升级依据是冻结 query/eval 集：

| 当前层 | 进入下一层的证据 |
|---|---|
| manifest + path + `rg` | 多次需要反复 grep，或排名成本明显 |
| FTS/BM25 | 代表性 paraphrase/概念查询持续漏掉关键源 |
| dense sidecar | sparse 与 dense 各自有互补 critical recall |
| hybrid | version/current-state 问题成为真实故障 |
| version-aware/rerank | 仅在明确版本、历史时点、近似文本冲突中获益 |

每次升级都必须同时测 task success、critical recall、stale/wrong-scope rate、loaded tokens、tool calls 与维护成本；不能只测“搜到了更多”。[EVIDENCE：`MNE-DR-023-report.md` Q1/Q7]

## 5.6 污染与失效指标

建议记录但不预设普遍阈值：

- `Token Pollution Rate`：无关 + 错 scope + 错版本 token / 全部装载 token；
- `Stale Context Rate`：superseded source token / 全部规则/来源 token；
- `Rule Scope Error Rate`：错误作用域规则 / 全部已装规则；
- `Unused Mandatory Rate`：被强制装入但输出完全未使用的 L0/L1；
- `Projection Drift Count`：source hash 不匹配数量；
- `Critical Miss Count`：未装入 oracle 必需源的次数。

阈值在预冻结测试中校准。[UNKNOWN：没有附件支持通用阈值]



# 6. 目的核查机制：与 fail-closed 同级的停止条件

## 6.1 双闸门

RAPW 不允许“材料齐全，所以就应该做”。每个阶段同时过两道闸：

| 闸门 | 核心问题 | 失败状态 |
|---|---|---|
| **Integrity Gate** | 我们是否有足够、正确、当前且有权限的材料去做？ | `STOP_INTEGRITY` |
| **Purpose Gate** | 即使做得到，这个动作是否仍服务 Owner 的真实目的，且是足够小的办法？ | `STOP_PURPOSE` |

任一失败都禁止继续。`STOP_PURPOSE` 不是软建议，其权限与 fail-closed 相同。[EVIDENCE：反模式 #1、#10、#11、#16]

## 6.2 目的核查触发点

必须在以下时点运行：

1. 接受一个新主线前；
2. 将任务局部教训提升为全局规则前；
3. 引入数据库、向量、图、自动化服务等新组件前；
4. 生成长期维护工件前；
5. Owner-touch 预算预计超支前；
6. 冻结设计/测试结论前；
7. 迁移规则单元或 authority root 前；
8. 连续两个周期只有格式、索引、摘要变化而无 Owner 可观察收益时；
9. 计划把 UNKNOWN 通过复杂结构“包装掉”时。

## 6.3 目的核查完整记录

`PURPOSE-CHECK` 必须有：

| 字段 | 说明 |
|---|---|
| `check_id` | 唯一 ID |
| `task_or_change_id` | 被检查对象 |
| `trigger_point` | 触发时点 |
| `goal_refs` | 直接服务的 Owner goals |
| `owner_problem_statement` | Owner 的实际问题，不是系统自造需求 |
| `expected_owner_outcome` | 可观察结果 |
| `non_goals` | 明确不做 |
| `candidate_action` | 拟执行动作 |
| `smallest_sufficient_action` | 更小方案 |
| `existing_mechanism_reuse` | 能否复用现有 |
| `evidence_for_need` | 真实故障/需求证据 |
| `evidence_class` | `[OWNER] / [EVIDENCE] / [INFERENCE] / [UNKNOWN]` |
| `maintenance_cost` | 预期长期成本 |
| `owner_touch_cost` | 需要 Owner 交互 |
| `context_cost` | 装载/推理负担 |
| `reversibility` | 回滚方式 |
| `sunset_or_review_trigger` | 退出条件 |
| `scope_locality` | 为什么是 task/project/global |
| `alternatives_rejected` | 其他方案及理由 |
| `verdict` | `PROCEED / PROCEED_NARROW / DEFER / ESCALATE_OWNER / STOP_PURPOSE` |
| `verdict_reason` | 结论 |
| `approved_by_or_policy` | Owner 或预授权规则 |
| `unknowns` | 未知项 |

## 6.4 自动停止规则

满足任一项即默认 `STOP_PURPOSE` 或 `PROCEED_NARROW`：

- 无法指向一个 Owner goal；
- 产物只有格式合规，没有结果层验收；
- 新规则只源于一次局部事故，且没有 locality/promotion 分析；
- 新组件没有购买一个已测出的失败面；
- 维护/Owner-touch/上下文成本未受预算约束；
- 已有更简单机制可满足同一结果；
- 方案只能让系统“看起来更完备”，不能改善 handoff、状态正确性、Owner 负担或具体 agent 效果；
- 研究结论没有 adoption、expiry、reject/defer 或 test closure；
- 需要把平台当前限制提升为永久核心规则；
- 为避免承认 UNKNOWN 而继续建模。

`ESCALATE_OWNER` 只在真正的价值取舍、授权或不可逆风险上使用；不把 Owner 当消息总线。[EVIDENCE：反模式 #7–#10、#15–#16]

## 6.5 “删除也是设计动作”

每个 review 周期必须允许四类结果：

- merge；
- replace；
- archive/retire；
- delete derived artifact and rebuild later。

只有新增、没有退休，是 purpose drift 的信号。耐久原始证据通常不删除，但可降低装载等级、迁移到受限存储或通过 retention policy 处理；可再生层应积极删除陈旧代。



# 7. Owner-touch 预算

## 7.1 计数口径

`Owner touch` 指 agent 主动要求 Owner 做一次不可合并的决定、批准、补件、转运或纠错。以下不计入：

- Owner 最初发起任务；
- 最终交付本身；
- Owner 自愿追加信息而非 agent 索取。

以下必须计入：

- 单独审批；
- 要 Owner 在工具间搬文件/复制状态；
- 本可批量却拆成多轮的问题；
- 因 agent 遗漏而要求 Owner 重述；
- Owner 为修复 agent 错误所做的纠正（另标 `failure_touch=true`）。

## 7.2 每任务声明，而非全局节奏

[OWNER：N-18] 每个任务在 `operating-profile` 中声明预算。建议的**预冻结默认**如下，属于 [INFERENCE]，须由实测校准：

| 任务类 | agent 主动 touch 上限 | 适用情况 |
|---|---:|---|
| `routine` | 0 | 权限、目标、验收均已存在，可机械执行 |
| `standard` | 1 | 允许一次打包后的价值/冲突裁决 |
| `high-consequence` | 2 | 不可逆、高影响、多个等价价值选项 |
| `owner-defined` | 显式值 | Owner 指定节奏；不得默认为无限 |

若预计超支，agent 必须依次：

1. 合并问题；
2. 给出推荐默认和各选项后果；
3. 缩小 scope；
4. defer 非关键项；
5. 仍无法在预算内完成时，以一个 `ESCALATE_OWNER` 触点说明原因。

不得用“我需要确认一下”作为无成本动作。

## 7.3 Owner-touch 记录

每个 task 记录：

- `budget_class`
- `max_agent_initiated_touches`
- `touches_used`
- `failure_touches`
- `manual_transfer_touches`
- `batched_decision_id`
- `budget_exceeded`
- `exceed_reason`
- `owner_override`
- `owner_time_estimate_if_known`
- `outcome_delivered`

核心指标不是“消息数少”，而是：

- Owner 是否需要重复背景；
- 是否被迫充当路由/消息总线；
- 是否只在真正价值裁决上被打断；
- 交付失败是否把隐性维护成本转嫁给 Owner。

## 7.4 预算与 fail-closed 的关系

fail-closed 不等于“不断问 Owner”。缺材料时先检查耐久核心、当前任务包和可用工具；只有关键缺口无法恢复且影响正确性时才占用一个 touch。若是低风险、可逆、已有默认授权，则按默认继续并记录假设。若是 UNKNOWN 且会改变核心结论，干净停止并把所有缺口合并成一次请求。



# 8. 交接方案及预冻结效果测试

## 8.1 交接目标

[OWNER：N-01] 核心目标不是“摘要写得好”，而是：新上下文/新模型在不依赖原对话隐含状态的情况下，能够像同一连续工作流一样恢复**当前目标、当前有效状态、负约束、下一动作和验证办法**，同时显著减少 rediscovery 与 Owner 重述。

交接采用四件分离的工件：

1. **Portable checkpoint**：机器/任务工作态；
2. **Quick Card**：接手者必须先读的最小当前信息；
3. **Full Handoff Package**：可重建的完整选择性包；
4. **Receiver Receipt**：接手者对完整性、冲突和首个动作的签收。

Quick Card 不是 Full Package 的替代；Full Package 也不是把整个历史 trace 全塞进去。[EVIDENCE：`MNE-DR-021-report.md`；`MNE-DR-024-report.md`]

## 8.2 Portable Checkpoint 完整字段

| 字段 | 说明 |
|---|---|
| `checkpoint_id` | 不可变 ID |
| `task_id` | 任务 |
| `source_revision` | Git commit/ref/工件 hash |
| `created_at` | 时间 |
| `created_by` | 创建者 |
| `purpose_and_goal_refs` | 目的与目标 |
| `pace_profile_ref` | N-18 节奏 |
| `current_phase` | 阶段 |
| `completed_work` | 已完成及证据 |
| `current_working_state` | 当前状态 |
| `next_atomic_action` | 接手后的第一个可验证动作 |
| `active_requirements` | 当前需求 ID |
| `active_decisions` | 当前决定 ID |
| `negative_constraints` | 禁止事项 |
| `open_questions` | 未决问题 |
| `blocked_unknowns` | UNKNOWN |
| `workspace_manifest` | 文件/分支/工件/dirty state |
| `environment_manifest` | 环境、依赖、版本 |
| `tool_and_permission_state` | 工具、连接、权限、valid_as_of |
| `loaded_context_receipt` | 原 agent 实际装载 |
| `tests_and_oracles` | 当前测试与结果 |
| `known_failures` | 已失败尝试 |
| `rollback_point` | 回滚 |
| `sensitivity` | 权限 |
| `valid_until_or_invalidation_trigger` | 失效条件 |
| `integrity_hash` | hash |
| `schema_version` | 版本 |

## 8.3 Quick Card 完整字段

Quick Card 必须能独立回答：

- `package_id / checkpoint_id / task_id`
- `why_this_task_exists`
- `current_goal`
- `pace`
- `current_status`
- `current_authoritative_decisions`
- `next_atomic_action`
- `must_not_do`
- `blocking_unknowns`
- `acceptance_oracle`
- `critical_source_refs`
- `workspace_and_environment_pointer`
- `validity/invalidation`
- `package_hash`

没有 `next_atomic_action`、当前决定、负约束或 oracle 的卡片不合格。

## 8.4 Full Handoff Package 完整字段

在 Quick Card 基础上增加：

| 分区 | 必需内容 |
|---|---|
| `scope` | sender、receiver、task、允许的子任务、明确排除范围 |
| `state` | checkpoint 全量字段 |
| `intent` | Owner 原始意图与规范化目标 |
| `requirements` | 当前、deferred、conflict、superseded 摘要及原记录指针 |
| `decisions` | 当前决策、替代方案、理由、supersession |
| `evidence` | 关键证据 spans；原件按毒性懒加载 |
| `work_product` | 已产物、diff、未提交变更、hash |
| `execution_history` | 仅保留对接手有诊断价值的尝试/失败，不默认全 trace |
| `environment` | 可重放环境 contract 和 proof gaps |
| `tools_permissions` | 当前表面能力、审批语义、valid_as_of |
| `load_plan` | 接手默认 L0/L1、可选 L2–L5 |
| `tests_oracles` | 机械检查、闭池答案、must/must-not、拒收条件 |
| `risks` | stale、scope、security、privacy、model-binding |
| `owner_touch` | 已用预算、剩余预算、何时才能打断 Owner |
| `rollback` | 恢复点和撤销方式 |
| `provenance` | 来源、版本、hash、生成器 |
| `expiry` | 失效时间/触发器 |
| `package_integrity` | manifest/hash/schema |
| `known_unknowns` | UNKNOWN 清单 |
| `sender_claim` | `complete / complete_with_gaps / incomplete` |

## 8.5 Receiver Receipt

接手者先验证、再继续。回执字段：

- `receipt_id`
- `package_id`
- `receiver_model_generation`
- `received_at`
- `integrity_check`
- `scope_match`
- `checkpoint_match`
- `current_state_consistency`
- `missing_required_fields`
- `stale_or_superseded_refs`
- `conflicts`
- `permission_gaps`
- `unknowns`
- `acceptance_decision`: `ACCEPT / ACCEPT_WITH_WARNINGS / REJECT_FATAL / BLOCKED_UNKNOWN`
- `fatal_reasons`
- `warnings`
- `sources_to_lazy_load`
- `first_intended_action`
- `expected_oracle`
- `owner_touch_needed`
- `receipt_hash`

### Fatal 与非 fatal

**Fatal：** task/checkpoint mismatch、hash/schema 破坏、没有 current goal/next action/关键 oracle、当前决定无法判定、关键 secret/evidence 缺失、权限不足却要求写入。

**Warning：** 可选 rationale 缺失、背景较旧但 current marker 清楚、冗余历史、非关键主观说明不完整。

“看到冲突就一律拒绝”也不合格：若 B 明确 supersedes A，应接受并使用 B；若 A/B 无 provenance 才拒绝。[EVIDENCE：`MNE-DR-024-report.md` Q5]

## 8.6 预冻结实验设计

### 冻结原则

- 先冻结 case、checkpoint、oracle、scorer、条件和分析计划，再看结果；
- 同一个真实 checkpoint 只改变 handoff 条件；
- successor 模型、工具权限、时间/step/token 预算保持一致；
- 主结论由机械/闭池 oracle 决定；
- 原始输出与总分分离，总分可重算；
- development fold 可新增 trap，confirmation fold 一旦开始只读。

### 建议的 12-case pilot [INFERENCE]

- 6 个真实历史 checkpoint，覆盖至少三种主线；
- 2 个不可重推隐藏事实 case；
- 2 个 current/superseded + must-not case；
- 1 个缺关键字段、应拒收 case；
- 1 个 anti-trap：只缺 optional 字段或包含明确 supersession，应接受。

12 是工程起点，不是统计学通用最优样本量。[EVIDENCE：`MNE-DR-024-report.md` Q4/Q7]

### 实验条件

| 条件 | 用途 |
|---|---|
| A. Same-session oracle | 近似连续上限；不作为可部署方案 |
| B. Cold current-files only | 当前 Git/文件基线 |
| C. Quick Card only | 最小交接 |
| D. Quick + Full Package + Receipt | 候选方案 |
| E. Deliberately degraded package | 检查拒收和 oracle 灵敏度 |

主比较是 B vs D；A 提供上限，C 诊断最小信息价值，E 验证系统不会被流畅但错误的包骗过。

### 接手者

至少包含：

1. 同模型、fresh context；
2. 一个较弱模型或受限设置；
3. 条件允许时一个不同模型家族。

同家族可以参与开发，不得独占最终自证。主 pass/fail 不依赖 LLM judge。[EVIDENCE：反模式 #14；`MNE-DR-024-report.md` Q3]

### Oracle 组合

每 case 至少一个：

- executable check；
- closed pool `current / superseded / other`；
- `must_include / must_not_include`；
- `expected_action=ACCEPT/REJECT`；
- hidden non-inferable fact；
- purpose-drift check；
- Owner-touch count。

### 指标

**主指标：**

- task/oracle pass；
- critical constraint retention；
- stale/superseded misuse；
- fatal package true rejection；
- good package false rejection。

**成本指标：**

- rediscovery tool calls；
- tokens/steps/time；
- 首次有效动作前的无效操作；
- Owner touches；
- loaded token pollution；
- package authoring/maintenance cost。

**诊断指标：**

- provenance use；
- abstention correctness；
- wrong-scope loading；
- current-state correctness；
- receiver receipt accuracy。

### 统计

- 二元配对结果报告完整 2×2 discordant counts，并可用 exact McNemar；
- 连续 debt 报告逐 case paired delta、中位数/均值和 exact/sign-flip sensitivity；
- n 很小时不把“p 未小于 .05”写成“无效果”；
- 不因中途看到好结果提前停；如分批，事前声明 N；
- 原始 counts 优先于漂亮 aggregate。

[EVIDENCE：`MNE-DR-024-report.md` Q4]

## 8.7 预冻结通过门

以下是本方案建议的**项目级 provisional gate**，标记为 [INFERENCE]，必须在运行前冻结，不能看结果后修改：

1. D 相对 B 不得新增任何 critical stale-state 或 must-not 违规；
2. D 在主 pass/fail 上不得出现未解释的 candidate-worse pair；
3. D 必须在至少一个结果轴上产生可观察收益：更多通过，或在不降通过率下减少 rediscovery/Owner-touch；
4. adversarial fold 必须同时报告 TRR 与 FRR，不能靠“一律拒绝”通过；
5. 所有 fatal integrity defect 必须触发拒收或 clean stop；
6. package 维护成本与 Owner-touch 未超任务预算；
7. 同一结果可由冻结 raw logs 重算；
8. 若不同模型结论分裂，状态保持 `PRE-FREEZE`，不以同家族多数票冻结。

若只改善可读性或格式而没有结果层收益，目的闸门判 `STOP_PURPOSE`。

## 8.8 交接不是全量历史复制

Full Package 应提供完整**重建路径**，而非完整历史文本。历史、研究原件和原始想法通过指针和按需触发存在。接手者必须先使用 current state 与 oracle，再为具体缺口懒加载。这样同时满足 N-01 的连续性和 N-19 的“记录≠加载”。[EVIDENCE：`MNE-DR-021-report.md`；`MNE-DR-023-report.md`]



# 9. 自现状迁移计划

迁移采用“先标注、后分层、影子运行、通过测试再切换”，不做大爆炸重写。

## 阶段 0：冻结迁移边界

- 宣布本轮只改变信息语义和加载机制，不顺带重构所有项目内容；
- 暂停无 locality gate 的全局规则新增；
- 记录当前 branch/commit、文件数、关键入口、writer topology；
- 建立回滚点；
- GitHub 写能力每次单独 preflight，不以 MNE-DR-027 一次成功当永久保证。

**退出条件：** 可回滚、scope 清楚、Owner-touch 预算已声明。

## 阶段 1：只读盘点与分类

对现有文件建立 inventory，不移动：

- authority domain；
- RAW / CANDIDATE / EXECUTION；
- current / superseded / archive；
- toxicity class；
- model/surface binding；
- source/provenance；
- 是否存在重复 canonical；
- 是否可再生。

**退出条件：** 所有规范性文件都有唯一 owner/authority；UNKNOWN 显式列出。

## 阶段 2：建立稳定 ID 与 canonical manifest

- 为 goals、requirements、decisions、rules、handoff、tests 建稳定 ID；
- 建立唯一 canonical root；
- 旧链接通过 reference map 解析；
- 禁止复制内容作为“兼容”，只保留引用。

**退出条件：** 任一 ID 可从 manifest 找到唯一当前记录与历史。

## 阶段 3：切出三态

不改变语义，先把现有材料映射到：

- S0 evidence；
- S1 checked candidate；
- S2 approved execution。

对混在同一文件中的内容，可先用 section-level manifest 标注，后续再拆文件。避免为目录美观破坏历史。

**退出条件：** context compiler 能排除 S0/S1 的指令权。

## 阶段 4：建立当前有效视图与变更集

- 为当前需求、决策、规则建立 materialized current documents；
- 新变更开始使用 `change record + current update + validation`；
- 旧历史不强制追溯重建成事件；只对高价值决策补最小 provenance。

**退出条件：** current 与 change ledger 一致性校验通过。

## 阶段 5：整理 N-17 规则单元

- 汇总行为规范到唯一目录；
- 每条规则补 scope、source、enforcement、expiry；
- 删除/合并重复规则；
- 可执行项转 test/hook/lint/check；
- 建 migration manifest，为未来整体迁往 Meta-Agent 做准备。

**退出条件：** 其他位置无可编辑副本；规则可整体移动。

## 阶段 6：需求与反馈闭环

- 对活跃需求启用 §4 状态机；
- deferred 项补 `defer_reason + revisit_trigger`；
- 新反馈使用完整 bundle；
- 选取历史高价值反馈转成首批 regression cases。

**退出条件：** 至少一条真实需求走完整捕获→实现→验证→反馈回环。

## 阶段 7：最小加载器

先实现：

1. canonical manifest；
2. task/scope/state/time hard filter；
3. `rg`/ID/path 检索；
4. load receipt；
5. toxicity boundary。

不先建 embedding。只有冻结 query set 显示 critical lexical miss 才升级。

**退出条件：** 新上下文可说明“装了什么、为什么装、漏了什么”。

## 阶段 8：交接影子运行

- 现有 handoff 继续作为基线；
- 同时生成 RAPW Quick + Full + Receipt；
- 不影响当前主线；
- 记录包制作成本与接手效果。

**退出条件：** 12-case pilot 数据完整、可重算。

## 阶段 9：预冻结评测与裁决

按 §8 冻结并执行。若失败：

- 不粉饰；
- 定位是源证据、投影、loader、package、receiver 还是模型能力；
- 只修改 development fold；
- confirmation fold 版本递增。

**退出条件：** provisional gate 通过，或明确 defer/stop。

## 阶段 10：有限切换

优先选择一个低风险、真实主线：

- RAPW current 视图成为该主线执行入口；
- 旧入口只读并显示迁移指针；
- 监控 stale、Owner-touch、pollution、handoff debt；
- 保留一键回到旧入口的 rollback manifest。

通过后逐项目迁移，不全仓一次切换。

## 阶段 11：N-17 整体迁往 Meta-Agent

只有在以下条件满足时：

- 规则单元在多个 concrete agents 中稳定复用；
- scope/冲突/retirement 机制通过负测；
- Meta-Agent 的 authority/ownership 已明确；
- 迁移后只有一个 canonical root；
- 回滚和引用重定向已测试。

“何时算成熟”的定量阈值目前为 **[UNKNOWN]**；不能因目录已经独立就自动迁移。

## 回滚原则

- 任何 migration phase 都有 source revision、migration manifest 和 inverse steps；
- 派生层直接删除重建；
- 当前规范切换失败时恢复上一 current revision，但保留失败 change record；
- 不通过重写 Git 历史掩盖迁移失败；
- 无法验证写入表面时输出本地工件，停止远端修改。



# 10. 反模式清单 16 条逐项自检

| # | 反模式 | RAPW 的防线 | 残余风险 / 验证 | 自检 |
|---:|---|---|---|---|
| 1 | **没有产品/Owner 拉力** | 每个 change 必须有 goal refs 和 Purpose Check；无实际问题则 `STOP_PURPOSE` | 模型可能事后编造“收益”；需 Owner 原话和真实 failure evidence | 通过设计，待实测 |
| 2 | **用格式验收替代结果验收** | handoff、需求、规则均有机械 oracle、负约束和任务结果；可读性只作次级指标 | 某些目标难机械化；主观项需独立 judge/human | 通过设计 |
| 3 | **只增不减** | rules/projections 有 supersede、retire、sunset、expiry；review 必须允许 merge/replace/delete | 原始证据仍增长；需 retention 与受限存储 | 通过设计，保留 UNKNOWN |
| 4 | **一次事故直接变全局规则** | `scope_locality + promotion gate`；先 reproducer/test，再考虑规则 | 重复模式判定可能主观 | 通过设计，需负测 |
| 5 | **没有全局冻结窗口/任意时点改规则** | 每任务/阶段声明 freeze；confirmation fold 只读；重大变更走 change set | N-18 禁止全局统一节奏，故冻结也必须 task-local | 通过设计 |
| 6 | **live state 无有效期/复核** | `valid_from/to`、`last_verified`、review trigger、model/surface binding | 某些长期目标无自然到期；至少要求触发器 | 通过设计 |
| 7 | **研究无 adoption、expiry、closure** | S1 必须进入 accept/defer/reject/blocked；研究原件默认半毒性，不因存在而执行 | 长期 deferred queue 可能堆积 | 通过设计，需队列健康指标 |
| 8 | **Owner 成为消息总线** | task-bound package、直接 source pointer、Owner-touch 预算、禁止手工搬运 | 工具连接不可用时仍可能需一次转运 | 通过设计；表面 preflight |
| 9 | **bookkeeping 成本无上限** | 只记录语义变更；按任务声明维护预算；purpose gate 比较最小方案 | 尚无经验证成本阈值 | 通过设计，[UNKNOWN] 阈值 |
| 10 | **lead agent 不质疑目的** | Purpose Gate 与 Integrity Gate 同级；可 `STOP_PURPOSE` | lead agent 仍可能为了完成任务而形式化通过 | 通过设计，需 purpose trap |
| 11 | **只敏感于 authority，不敏感于 purpose drift** | 每次晋升/全局化/迁移都重新绑定 goal 与 outcome | Owner goal 本身会变化，需新裁决 | 通过设计 |
| 12 | **在未验证表面上写字节级流程契约** | 平台事实带 `valid_as_of/surface/evidence`；关键写操作先 preflight；语义 contract 与 UI 细节分离 | 厂商表面可无预告变化 | 通过设计 |
| 13 | **超长主线兼任路由、发布、验收和交接总线** | 每任务 checkpoint/handoff；fresh context；completed mainline 懒加载 | Owner 仍可能偏好长对话；需要工具化入口 | 通过设计 |
| 14 | **同家族自我认证** | 机械 oracle 为主；fresh context、较弱模型和不同家族参与；主观 judge 独立 | 跨家族成本/可用性可能受限 | 通过设计，能力待定 |
| 15 | **把当前平台限制写成永久核心规则** | 平台事实进入 model/surface adapter 或 evidence，不进入模型中立 core；变化触发重评 | 某些限制可能被误分类为原则 | 通过设计 |
| 16 | **把 UNKNOWN 当成待补字段，继续猜测** | `blocked_unknown / STOP_INTEGRITY` 是合法终态；缺关键材料必须干净停止 | 模型可能把 UNKNOWN 美化成 inference | 通过设计，需 adversarial case |

## 10.1 保留的优良原则

清单中值得保留并已纳入 RAPW 的部分：

- 执行源、证据、候选、历史分层；
- fail-closed、expected/observed、禁止捏造；
- task-bound handoff 和 locality；
- fresh-context negative tests；
- archive reconstruction；
- incident preservation、rollback、不静默修复；
- debt 和 proof-gap 诚实披露。

## 10.2 自检结论

16 项在**设计层**均有对应机制，但这不是运行证明。#9、#12、#14、#16 尤其需要冻结测试；未跑测试前，本报告状态仍为 `PRE-FREEZE`，不能把“表格全打勾”当成验收完成。



# 11. 自我批判与盲区

## 11.1 可能过度设计

RAPW 虽然刻意避免完整事件平台，仍引入 authority、ledger、current view、projection、checkpoint、receipt 等多个概念。对单 owner、低并发、少量文件的项目，收益可能小于维护成本。[EVIDENCE：`MNE-DR-028-report.md` Q4 对混合架构复杂度的警告]

**缓解：** 分阶段迁移；允许只启用 manifest + current + handoff 的最小子集；Purpose Gate 可停止后续层。

## 11.2 “账本 + 当前文档”仍可能漂移

同一变更集和校验可以降低漂移，不能保证永远没有部分提交、冲突 merge 或人工绕过。Git 也不是事务数据库。

**缓解：** schema/lint、commit-level validation、reconciliation report；高并发 writer 出现前不声称支持强一致。  
**[UNKNOWN]：** 当前 writer topology、并发率和冲突率未由本任务实测。

## 11.3 原始完整捕获与隐私存在张力

N-02/N-06 要求高保真保存，长期 Git 又可能不适合 secret、敏感学习画像或受限附件。hash/reference 方案保留可验证性，却可能降低可恢复性。

**缓解：** sensitivity、secure reference、redaction manifest、retention policy。  
**[UNKNOWN]：** 项目实际隐私法域、公开/私有仓库策略和加密存储未提供。

## 11.4 “毒性”标签可能造成过度隔离

原始材料确实会污染执行上下文，但过于保守会漏掉关键例外、Owner 原话或研究证据。

**缓解：** 毒性只控制默认装载，不控制保存和检索；审计/冲突任务可以显式解封；每次 critical miss 进入检索评测。  
**[UNKNOWN]：** 最佳分类粒度和 token 边界需实测。

## 11.5 需求状态机可能僵化

18 个主状态能机械执行，但复杂项目可能需要组合状态，例如“部分验证、部分 deferred”。若强行把多维现实压成单状态，会制造假精确。

**缓解：** 大需求拆成子需求；主状态只表达权威生命周期，进度细节放 implementation/test records；新增状态必须 schema migration。  
**残余风险：** 拆分本身增加 bookkeeping。

## 11.6 “新前沿模型”仍依赖人为或表面信号

平台可能静默更新同一标签，模型自报不可靠，官方文档也不总给精确 revision。

**缓解：** MODEL-EVENT 接受多证据级别；固定 anchor regression 可在标签不变时发现行为漂移。  
**[UNKNOWN]：** 无公开统一方法证明检测到所有静默更新。[依据：`MNE-DR-020-report.md`]

## 11.7 Handoff 测试可能过拟合

12-case pilot 很小，hidden fact 和 current/superseded trap 不能覆盖所有真实主线。候选方案可能学会测试格式而非真正连续性。

**缓解：** real + synthetic 双 cohort；冻结 confirmation fold；真实 handoff 连续监控；每版新 trap 进入下一折。  
**[UNKNOWN]：** 需要多少 case 才覆盖跨年项目，没有材料给出通用数字。

## 11.8 机械 oracle 不等于完整质量

可执行检查擅长“做没做对”，不一定测到解释、可维护性和 Owner 信任。LLM judge 又有位置、长度和自偏好。

**缓解：** 机械 oracle 决定主 pass/fail；主观维度独立评分并保存分歧；不让主观分掩盖任务失败。[依据：`MNE-DR-024-report.md` Q3]

## 11.9 可再生层可能代际爆炸

每个模型/表面一代投影会产生大量目录和维护噪声，尤其同一供应商频繁更新时。

**缓解：** 只有验证到行为差异才新建代；旧代自动 stale/retire；manifest 可重建；不保留无使用者的投影。  
**[UNKNOWN]：** 最佳代际粒度未验证。

## 11.10 Owner-touch 预算是工程假设

routine=0、standard=1、high-consequence=2 是为了落实 Owner 成本目标的 provisional default，不是附件中的普遍实证阈值。

**缓解：** 每任务声明；报告实际 touch 与结果；冻结前校准。  
**[INFERENCE]：** 不能把低消息数自动等同高满意度。

## 11.11 规则单元迁移成熟度未定义

N-17 明确最终整体迁往 Meta-Agent，但材料没有给出“成熟”量化条件。

**缓解：** 先要求多 agent 复用、负测、唯一 canonical、回滚；最终阈值由后续证据/Owner 裁决。  
**[UNKNOWN]**

## 11.12 GitHub 写能力是局部事实

MNE-DR-027 证明本账户、本连接、2026-08-31 普通 Pro 对话可直接 create branch/file/PR，且无额外审批卡；MNE-DR-020 的公开平台文档又曾表现为 read-only 描述。两者不能被压成一个永久结论。

**设计后果：** 每次远端变更先发现 action 和 preflight；无法写入时输出本地工件并停止，不绕过授权。  
本次 MNE-DR-029 没有修改仓库。

## 11.13 本报告没有做的事

- 没有执行迁移；
- 没有运行 12-case handoff pilot；
- 没有与 Claude 方案互看或比较；
- 没有独立复核 8 份研究报告引用的外部论文；
- 没有测真实 repo 的检索 recall、token pollution、Owner-touch 或多 writer 冲突；
- 没有证明 RAPW 优于沿用现状。

因此“完整设计”不等于“效果已证实”。



# 12. 证据引用与结论追踪

## 12.1 主要设计决策追踪

| 设计结论 | 类型 | 依据附件与章节 |
|---|---|---|
| 原 CPU/RAM/Git 类比降为可推翻教学默认 | **[OWNER]** | `02a-contradiction-clarification-package.md` X-1；`01-goals-register.md` §7 |
| 规范架构采用概率模型 + 确定性控制 + 显式耐久状态 | **[EVIDENCE]+[INFERENCE]** | `MNE-DR-028-report.md` Q2–Q5 |
| Git 中存在一个模型无关、可迁移的规范根 | **[OWNER]** | `01-goals-register.md` N-11、N-15；`02a...` N-17 |
| 行为规范目前共同存于 Mnemosyne，未来整体迁往 Meta-Agent | **[OWNER]** | `02a...` X-2 / N-17 |
| 不采用全量纯事件溯源，而使用轻量 change ledger + current docs | **[INFERENCE]** | `MNE-DR-028-report.md` Q4 的收益/复杂度；现状兼容要求 |
| 原始资料、候选分析、执行源三态分离 | **[OWNER]+[EVIDENCE]** | `01-goals-register.md` O-13、N-14；`MNE-DR-022-report.md` Q1/Q4 |
| 原始资料高保真保存但不默认加载 | **[OWNER]** | N-02、N-19；裁决包后续回填 |
| 研究原件半毒性、已完成主线懒加载 | **[OWNER]** | `02a...` X-3 / N-19 |
| 先 hard-filter applicability，再 relevance rank | **[EVIDENCE]** | `MNE-DR-023-report.md` Q4/Q6 |
| manifest/path/rg → FTS → dense → hybrid 渐进升级 | **[EVIDENCE]** | `MNE-DR-023-report.md` Q1/Q7 |
| 派生索引必须可删、可重建、回源 | **[EVIDENCE]** | `MNE-DR-023-report.md` Q5/Q7 |
| 需求需 current + change + archive，显式 supersession/defer | **[EVIDENCE]** | `MNE-DR-022-report.md` Q1/Q2 |
| 新模型只触发重评，不自动激活 deferred 或推翻 current | **[OWNER]+[EVIDENCE]** | N-03、N-05；`MNE-DR-022-report.md` Q3 |
| 反馈必须保存原话、上下文、工件、expected/observed，并转 regression | **[OWNER]+[EVIDENCE]** | N-06；`MNE-DR-026-report.md` Q4 |
| 可执行经验优先晋升为 test/hook/lint/eval | **[EVIDENCE]** | `MNE-DR-026-report.md` Q4/Q7 |
| 学习画像/模型解释必须可推翻，避免稳定人格化 | **[EVIDENCE]** | `MNE-DR-025-report.md` Q3/Q5/Q6 |
| handoff 目标是任务结果与 rediscovery debt，而非摘要美感 | **[EVIDENCE]** | `MNE-DR-021-report.md`；`MNE-DR-024-report.md` Q2/Q4 |
| 同一 checkpoint、只变 handoff view 的配对测试 | **[EVIDENCE]** | `MNE-DR-021-report.md`；`MNE-DR-024-report.md` Q4/Q7 |
| 主 pass/fail 用机械/闭池 oracle，LLM judge 只做次级主观诊断 | **[EVIDENCE]** | `MNE-DR-024-report.md` Q2/Q3 |
| adversarial fold 同时测真拒收和误拒 | **[EVIDENCE]** | `MNE-DR-024-report.md` Q5 |
| 同家族不能独占自我认证 | **[EVIDENCE]** | 反模式 #14；`MNE-DR-024-report.md` Q3 |
| task/conversation 自己声明 pace，无全局统一节奏 | **[OWNER]** | `02a...` X-4 / N-18 |
| Purpose Gate 与 fail-closed 同级 | **[INFERENCE]，由反模式强制导出** | 反模式 #1、#10、#11、#16 |
| Owner-touch 按任务预算，避免 Owner 成为消息总线 | **[OWNER]+[INFERENCE]** | `01-goals-register.md` §4 候选标准；反模式 #8/#9；N-18 |
| 平台事实带表面、账户、日期；每次写入重新 preflight | **[EVIDENCE]** | `MNE-DR-020-report.md`；`MNE-DR-027-result.md` |
| 迁移采用影子运行和可回滚渐进切换 | **[INFERENCE]** | `MNE-DR-028-report.md` Q4/Q5；反模式清单 |
| Mnemosyne 是为具体 agent 设计持久记忆系统的 meta-level 工程 | **[OWNER]** | `01-goals-register.md` N-16 |

## 12.2 Owner 目标覆盖矩阵

| 目标 | 本方案机制 |
|---|---|
| N-01 完美交接 | §8 四工件交接 + paired pre-freeze test |
| N-02 原始捕获 | §3 S0 + feedback bundle + secure reference |
| N-03 新模型触发复核 | §4 MODEL-EVENT + regression |
| N-04 需求生命周期 | §4 完整状态机 |
| N-05 deferred 重评 | `defer_reason/revisit_triggers/reassessment_pending` |
| N-06 反馈全材料与定期测试 | §4.5–§4.6 |
| N-07 开发知识资产 | §2 `70-assets`；test/hook/lint/eval 晋升 |
| N-08 学习 agent 低置信 | 解释与画像留在 S1、可推翻、带证据/不确定性 |
| N-09 人类可读 | Git/Markdown current views + human projections |
| N-10 真实平台能力 | model/surface/valid_as_of + preflight |
| N-11 可用记录/可转移方法 | 规范根、manifest、schema、迁移计划 |
| N-12 Owner 输入分类 | requirement `request_class` |
| N-13 独立重设计 | 本报告未读取或猜测 Claude 方案 |
| N-14 原始证据不神圣 | S0 保真但无执行权；必须进入 S1 检查 |
| N-15 耐久核心/可再生层 | §2 |
| N-16 Meta-Agent 定位 | §1.1 |
| N-17 规则整体迁移 | §2.4、§9 阶段 5/11 |
| N-18 任务级节奏 | §4.6、§7 |
| N-19 记录≠加载≠呈现 | §5 |

## 12.3 明确 INFERENCE

以下不是附件中已有的直接结论，而是本方案的设计选择：

1. “RAPW”名称及七层具体组合；
2. 轻量 change ledger 与 current docs 同 commit 的事务约定；
3. 六级 toxicity/load class；
4. 18 状态主 FSM 的具体枚举；
5. Quick Card、Full Package、Receipt 的字段集合；
6. 12-case pilot 的具体配额；
7. provisional freeze gate；
8. routine/standard/high-consequence 的 touch 默认；
9. 当前目录树、编号和文件名；
10. Purpose Check 记录格式。

这些都必须通过迁移影子运行、schema lint 和 §8 测试验证。

## 12.4 明确 UNKNOWN

1. RAPW 相对现状的真实任务成功率、handoff debt、Owner-touch 与维护成本；
2. 最佳 event/change 粒度；
3. 现有仓库中实际重复 canonical、stale rate、multi-writer 冲突率；
4. 检索何时需要 FTS、dense 或 hybrid；
5. toxicity 分类的最佳阈值；
6. 新模型静默更新的完整检测办法；
7. 规则单元何时足够成熟可迁往 Meta-Agent；
8. 12-case pilot 的外部效度；
9. Owner-touch 的最优数字；
10. 多年跨供应商迁移保真率；
11. 隐私/秘密材料的最终存储与 retention policy；
12. 高并发 runtime 是否需要数据库/事务层；
13. 本次表面 GitHub 写 action 的未来稳定性；
14. Claude 对照方案内容及两方案比较结果——本任务禁止访问和猜测。

## 12.5 最终设计裁决

**建议进入影子实现与预冻结实验：** 保留 Git/文件作为 Owner-facing 唯一规范根；加入轻量语义账本、当前有效状态、任务检查点、模型专用可再生投影、机械 loader 和双停止闸门。

**不建议立即做：**

- 全仓事件溯源重写；
- 默认 embedding/知识图；
- 将所有历史/研究/原始想法常驻加载；
- 把自然语言规则当强制权限；
- 用同一家族模型和主观 judge 自证；
- 在未跑交接实验前宣布冻结；
- 因一次 GitHub 写能力成功而把远端写入当永久平台契约。

**冻结条件：** §8 的预冻结测试通过，Owner-touch 与维护成本可接受，16 条反模式的运行级负测完成，且 UNKNOWN 没有被模型用猜测掩盖。

---

**报告状态：** `COMPLETE / PRE-FREEZE`  
**仓库修改：** 无  
**外部检索：** 无（任务书和 12 份附件之外）  
**建议交付文件名：** `MNE-DR-029-counterpart-design.md`
