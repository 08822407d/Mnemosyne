# 设计稿A — 规范层治理设计（guard 层地位、加载分层、整编机制、语言分层）

```yaml
track_id: FABLE5-REVIEW2-001
record_type: independent_design_draft
design_id: R2-DESIGN-A
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: DESIGN_RECOMMENDATION
authority_level: non_execution_source_advisory_draft
owner_preleaning: Q5a_spec_defines_guard_layer (门3 批示)
incorporates: [R2-CONF-005, R2-COST-001, R2-COST-006, R2-CONF-007(Q7a), 束3机制(R2-FRESH-006), MNEMOSYNE-199方案]
adoption_gate: >
  本稿不生效。按门3 总约束：先经 ChatGPT Pro 自我检讨与异构复核、
  合作方案确认后，再由 Owner 批准并以单独授权任务实施。
```

## 1. 问题重述（一段话）

13 份用户批准的行为规范（guard）实际统治仓库的全部写入行为，但执行源只定义了"执行源/非执行源"二元权威，规范层没有名分、没有清单、没有修订与退役流程；行为刷新要求必读全部规范（约 3800 行），仓库自己的评审（MNEMOSYNE-199）确诊过度加载并开出分层方案后，必读清单反而继续增长。根因是**规则层只有加法机制**。

## 2. 设计目标与硬约束

目标：给规范层名分、给加载分层、给增长配上整编对冲、给语言定分层规则——四件事一次设计、可分步实施。

硬约束：
1. `current/human-approved-spec.md` 保持唯一执行源（不因式分解——Q5a 预倾向）；
2. 不引入自动化（v0.1 §10 边界）：一切清单、触发、整编靠人工纪律与 checklist；
3. 不作废任何现有 guard 的实质内容（保护既有投资与事故教训）；
4. 兼容多写入方（GPT 族/Claude 族/未来族均可执行同一套规则）。

## 3. 核心设计

### 3.1 权威四层模型（写入执行源的定义，案文见设计稿B §7）

| 层 | 内容 | 强制力 | 修订流程 |
|---|---|---|---|
| L1 执行源 | current/human-approved-spec.md | 最高，冲突时胜出 | §6 全流程（candidate→确认→修订） |
| L2 行为规范层 | 注册表在列的 guard 文件 | 在各自声明的 scope 内强制 | Owner 批准的任务即可修订；新建/退役须更新注册表 |
| L3 指导与导航层 | onboarding、loader、README、commands | 建议与入口，不独立施加义务 | 普通维护任务 |
| L4 证据层 | 其余一切（notes/raw/handoff/status/研究/评审） | 仅证据 | 按各自惯例 |

关键语义：L2 的强制力**来源**是"Owner 批准 + 注册表在列"双条件——不在注册表的文件即使自称 guard 也不具强制力。这一条把"哪些规则算数"从全库搜索题变成查表题。

### 3.2 规范注册表（新文件 `current/guard-registry.yaml`）

每份 guard 一条登记：

```yaml
- guard_id: MNEMOSYNE-GITHUB-SINGLE-ACTIVE-PR-LINEAGE-001
  file: current/github-single-active-pr-lineage-guard.md
  scope_zh: 每任务一条写入谱系、至多一个打开的 PR   # 中文一句话（Q7a 义务）
  load_class: conditional            # core | conditional
  triggers: [branch_creation, pr_creation]
  status: active                     # active | merged_into:<id> | retired
  created_by_task: MNEMOSYNE-118
  last_amended_by_task: MNEMOSYNE-210
  last_confirmed_current: MNEMOSYNE-XXX   # 整编时刷新（束3 失效纪律在注册表上的落点）
```

注册表本身属 L3（导航），但"在列"是 L2 强制力的必要条件；它是唯一需要随 guard 增删同步维护的文件——把状态维护面从 13 处收敛到 1 处。

### 3.3 加载分层（采纳 MNEMOSYNE-199 方案的修订版）

- **core（每次行为刷新必读）**：执行源 + loader（改造为调度表）+ user-operation guard（最宽适用面）。3 份，约 1100 行，较现状降 ~70%。
- **conditional（触发才读）**：其余全部 guard，触发条件在注册表 `triggers` 字段；loader 只保留"触发→读哪份"的调度表与每份的一行中文 scope。
- **新 guard 默认进 conditional**；进 core 需要 Owner 在批准该 guard 时显式说明理由——堵住"创建任务顺手加必读"的增长通道（R2-COST-001 的机制性根因）。
- 不确定是否触发时：先读再动（现行 199 建议保留）。

### 3.4 整编机制（对冲只加不减）

- 触发条件（先到先触发）：注册表新增满 3 份 guard；或距上次整编满 8 周；或 Owner 点名。
- 整编任务产出：合并提案（同域 guard 归并）、降级提案（L2→L3）、退役提案（标 retired 不删文件，历史保全）、注册表 `last_confirmed_current` 全量刷新。
- 整编产出仍走 Owner 批准；无自动生效。
- 首次整编的现成候选 [MODEL_INFERENCE]：artifact-delivery 与 deep-research-correction 两份同域可考虑归并；frontier-clarification 系两份使用频率待查证。

### 3.5 语言分层（Q7a 落地）

- 人读材料（决策包、报告、PR 说明、Owner 批示对象）：中文优先——写入 spec（案文见设计稿B）。
- 模型规则文件：可英文；义务两条——注册表内一行中文 scope（新旧都补）+ guard 文件头部中文摘要块（新 guard 强制，存量随整编分批补齐，不专门立任务）。

### 3.6 与束3（状态失效纪律）的合并落点

"live 文件强制 `last_updated_by_task` + 失效声明"不再另立机制，直接由两处承载：注册表的 `last_confirmed_current` 字段（覆盖 guard 层）+ loader checklist 增加一行"完成任务前检查你改变了哪些领域的状态、对应 live 文件是否更新"（覆盖 status 层）。

## 4. 迁移步骤（全部待授权，供 Pro 复核后排期）

1. **任务一**：建注册表（13 份存量登记）+ loader 改造为"core 3 份+调度表"；无 guard 内容改动，风险低。
2. **任务二**：spec 修订（采纳设计稿B 案文，含 3.1 定义与语言规则）——L2 强制力的合法性来源就位。
3. **任务三起**：按 3.4 节奏运转整编；中文摘要随整编补齐。

顺序理由：任务一先行也安全（注册表在 spec 承认前仅是导航），但强制力语义在任务二后才完整；两任务合并为一次亦可。

## 5. 备选方案与否决理由

- **方案 b（少数吸收入 spec、其余降级）**：优点是层级简单；否决因为"哪些算少数"本身是高争议裁定，且 spec 会因吸收而膨胀、修订门槛使未来规则迭代变慢——与实用化阶段的敏捷需要相反。
- **方案 c（spec 因式分解）**：第一轮悬置的大改。当前证据（guard 增长、加载税）其实部分支持它，但迁移成本大、且要求全体写入方同步换认知模型；在 Meta-Agent 实测优先（门3 Q2 理由）的资源分配下不划算。**保留为远期选项**：若整编机制运转两个周期后 guard 仍失控增长，c 案自动回到议程。
- **不动方案（维持现状）**：已被 40 天实证否决（199 确诊后清单继续增长）。

## 6. 代价与风险

- 实施：任务一 M（半天级）、任务二并入设计稿B 的修订任务；持续成本：注册表随 guard 增删同步（每次一行）、整编每 8 周一次 M 任务。
- 风险1：注册表成为新的单点过期文件——对冲即 3.6 的 `last_confirmed_current` 与整编强制刷新；
- 风险2：整编触发靠人记——对冲：触发条件写入注册表头部，loader 调度表含"检查整编是否到期"一行；
- 风险3：conditional 加载导致漏读——对冲：触发表覆盖式枚举 + "不确定先读"规则；此风险现状同样存在（3800 行里漏看比 13 行触发表漏查更易发生 [MODEL_INFERENCE]）。

## 7. 自我批判（按轨道惯例）

1. **利益相关**：本设计者是将受该规则体系约束的写入方之一，且分层方案直接降低我自己的加载负担——存在把"对模型省事"包装成"对项目有利"的动机风险。对冲：全部量化主张可独立复核；Pro 异构复核是显式门。
2. **单模型设计**：与 199（GPT 侧）结论高度一致既可解读为跨族收敛验证，也可能是我读过 199 后的锚定效应——诚实标注：本设计不是独立重推导，是在 199 基础上的增量设计（增量部分：注册表、强制力双条件、整编触发、语言分层、束3 合并落点）。
3. **注册表是新增维护面**：声称"收敛到 1 处"的前提是人真的维护这 1 处；若失守，注册表比无注册表更误导（虚假权威清单）。这是本设计最脆弱的假设。
4. **触发词表的完备性未经验证**：conditional 的 triggers 枚举来自 199 的分析加我的补充，没有经过真实任务流的覆盖测试——建议作为跨模型实验之一（见 05 文件 EXP-3）先小规模验证再全量切换。
5. **整编机制无先例**：8 周/3 份的参数是拍的，无证据支撑；首个周期应视为参数校准运行。
