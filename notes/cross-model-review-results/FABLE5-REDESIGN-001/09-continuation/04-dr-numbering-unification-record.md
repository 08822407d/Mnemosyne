# FABLE5-REDESIGN-001 · DR 编号统一方案与执行记录（2026-08-31）

```yaml
record_type: numbering_unification_plan_and_execution_record
track_id: FABLE5-REDESIGN-001
date: 2026-08-31
owner_decision_verbatim: "既然是完全不同的研究内容，那我认为应该把它们都统一到新版的三位数编号系统中。你设计统一方案后执行，然后把前因后果通知给另一个参与mnemosyne建设的claude code本地任务。"
prior_records: 03-research-questions.md §5（编号核对更正——旧序列实至 13，注册表未回填）
generated_by_actor: claude-fable-5
generated_on_surface: claude-code-vscode
```

## 1. 统一方案（七条）

1. **单一序列**：Mnemosyne 线深度研究/前沿研究/一次性评审统一用 `MNE-DR-NNN`（三位数），注册表为唯一分配器。
2. **旧 07~13 原号回填**：这七个数字在新表从未签发，按原数字登记为 legacy 行（身份不变：旧 DR-07 即 MNE-DR-007）。
3. **旧 01~06 同号双档**：数字已被 2026-07-30 后的新任务占用，且六对均为不同内容——历史事实不改名；注册表以 era 字段（legacy_2026H1 / current）双档登记，今后引用 001~013 号须带年代或主题消歧。
4. **未编号旧研究**：登记为 unnumbered_legacy 附录，不追编号、不占数字。
5. **新分配自 014 起严格唯一**：本轨道两课题 = 014、015；`next_unallocated_sequence: 016`。
6. **旧 3 号缺档**：仓库与 Alaya 均未见 3 号实物，登记 `legacy_003: not_found`（不断言不存在，Owner 可补）。
7. 历史文件、对话导出、报告一律**不改名**（对照表消歧，符合命名规范 §7.6"历史不批量改名"与"序号永不复用"铁律）。

## 2. 旧序列证据映射表（回填数据源）

| 统一号 | 旧称 | 主题 | 日期 | 证据（Alaya 对话导出 / 仓库轮次） | 映射置信 |
|---|---|---|---|---|---|
| 001(legacy) | DR1 | 记忆系统测试/调试/评估证据综述 | 2026-06 | RC-2026Q2-memory-testing（DR1_*report）；对话导出未定位（疑 `ChatGPT-DR - AI Agent 持久记忆研究-20260622.md`） | 报告 VERIFIED / 对话 INFERENCE |
| 002(legacy) | DR2 | 交接策略与量化评估 | 2026-06 | RC-2026Q2-handoff-strategy（DR2_*report）；对话导出未定位 | 报告 VERIFIED / 对话 UNKNOWN |
| 003(legacy) | DR3 | — | — | **not_found**（仓库与 Alaya 均无 3 号实物） | — |
| 004(legacy) | DR4 | 用户原文/需求脱敏治理 | 2026-06-29 | RC-2026Q2-user-input-governance；Alaya `ChatGPT-DR - Mnemosyne 04 - user-originals-…-20260629.md` | VERIFIED |
| 005(legacy) | DR5 | 首个真实目标试运行评估框架（v2） | 2026-06-30 | RC-2026Q2-first-target-dry-run-evaluation（DR5_v2 prompt/report）；Alaya `ChatGPT-DR5 v2评测框架-20260630.md` | VERIFIED |
| 006(legacy) | DR6 | 平台/Project memory/apps 能力 delta | 2026-07-15 | RC-2026Q3-platform-context-apps-delta（DR6_*report）；Alaya `ChatGPT-DR - Mnemosyne 06 - platform context apps-20260715.md` | VERIFIED |
| **007** | DR-07 | 多模型裁定与溯源研究（pro/thinking 双运行） | 2026-07-21 | RC-2026Q3-multi-model-adjudication-provenance（run-context guard research_basis）；Alaya `ChatGPT-DR-07_多模型裁定研究(pro)(thinking)-20260721.md` ×2 | VERIFIED |
| **008** | DR-08 | HO-GUIDANCE-001（目标项目对话加载指导研究） | 2026-07-28 | Alaya `ChatGPT-DR-08_HO-GUIDANCE-001-20260728.md` | VERIFIED |
| **009** | DR-09 | LEARNER-COGNITIVE-COACHING-001 | 2026-07-28 | Alaya `ChatGPT-DR-09_…-20260728.md` | VERIFIED |
| **010** | DR-10 | CROSS-AGENT-SHARED-MEMORY-001 | 2026-07-28 | Alaya `ChatGPT-DR-10_…-20260728.md` | VERIFIED |
| **011** | DR-11 | TARGET-MEMORY-MIGRATION-001 | 2026-07-28 | Alaya `ChatGPT-DR-11_…-20260728.md` | VERIFIED |
| **012** | DR12 | PRO-DR-ADAPTIVE-EXPLANATION-STAGE-A-001（自适应讲解与前置诊断） | 2026-07-28 | Alaya `ChatGPT-DR12-20260728.md`（首条消息含 research_id，本轮已核） | VERIFIED |
| **013** | DR13 | PRO-DR-FRONTIER-PLANNING-CLARIFICATION-HANDOFF-001（澄清包与触发策略） | 2026-07-29 | Alaya `ChatGPT-DR13-20260729.md`（同上） | VERIFIED |
| 附录 | 无号 | AI Agent 持久记忆研究（6/22）；review batch-B（6/22）；并行工作主线治理（7/24）；2026Q2-initial 整轮（综合＋轻度1~6，编号系统建立前） | — | Alaya 同名导出；RC-2026Q2-initial | unnumbered_legacy |

## 3. 注册表补丁（交维护线落地；本轨道无 notes/registries/ 写权限，且该文件在 open PR #316 变更路径内）

对 `notes/registries/project-research-display-name-registry-v0.1.md`：

1. §1 `next_unallocated_sequence: 007` → `016`；
2. §2 追加两行 issued：
   - `MNE-DR-014 平台能力刷新`，canonical `FABLE5-REDESIGN-001-RQ1`，status issued_ready_not_executed，allocation_task FABLE5-REDESIGN-001，taskbook `project-knowledge/FABLE5-REDESIGN-001/MNE-DR-014-platform-capability-refresh-taskbook.md`；
   - `MNE-DR-015 交接实践现状`，canonical `FABLE5-REDESIGN-001-RQ2`，同上，taskbook `…/MNE-DR-015-continuity-practice-taskbook.md`；
3. 新增小节"legacy 2026H1 回填段"：§2 表按本记录 §2 落 007~013 七行（era: legacy）＋001~006 双档说明＋unnumbered_legacy 附录＋`legacy_003: not_found`；
4. 新增规则行：`≥014 严格唯一；001~013 为历史混用区，引用须带年代或主题`；
5. 建议同批：风险登记簿视情记一条（注册表建立时未回填旧序列→本次撞号预警靠 Owner 记忆拦截；执行方未反查存档为次因）。

## 4. 本轨道已执行

- 任务书改名与内文改号：`MNE-DR-014-platform-capability-refresh-taskbook.md`、`MNE-DR-015-continuity-practice-taskbook.md`（原 007/008 号候选作废，两号仍空闲——将由 legacy DR-07/DR-08 回填占用）；
- `03-research-questions.md` §1/allocation_note 同步，§6 执行记录；
- 跨会话通知维护线（mnemosyne-2e）：前因后果＋本补丁指针（Owner 指令中的"通知另一个 claude code 本地任务"即此）。

## 5. 方案 v2 · 终案（2026-08-31 Owner 二次裁定，取代 §1 第 2/3/5 条与 §3 补丁）

Owner 裁定原话："按照你给出的新思路"新研究001~006编号仍单独做说明以对应已存档里使用的编号，但同时给他们续编到013后面供从今天开始的所有对话/工作使用"，然后你把最新两个研究课题中的编号续到它们后面（应该是020和021了）"。

### 5.1 统一号表（自 2026-08-31 起对所有新对话/工作生效）

| 统一号 | 任务 | 说明 |
|---|---|---|
| 001~006 | 旧序列 DR1~DR6（记忆测试 / 交接策略 / not_found / 用户原文治理 / 试运行评估 / 平台 delta） | 证据映射见 §2；003 缺档待补 |
| 007~013 | 旧序列 DR-07~DR13（多模型裁定 / HO-GUIDANCE / 学习教练 / 共享记忆 / 记忆迁移 / 自适应讲解 StageA / 澄清交接） | 原号回填，见 §2 |
| **014** | 验证包审计（曾用号 MNE-DR-001） | 八月新研究续编段。曾用号只作读档案对照别名，**冻结材料一律不改名**；活文件"碰到才改"（lazy migration，由维护线掌握节奏） |
| **015** | 表面威胁（曾用号 MNE-DR-002） | 同上 |
| **016** | 生命周期验证（曾用号 MNE-DR-003） | 同上 |
| **017** | 能力归属（曾用号 MNE-DR-004） | 同上 |
| **018** | 跨仓库并发（曾用号 MNE-DR-005） | 同上 |
| **019** | 交接加固（曾用号 MNE-DR-006） | 同上 |
| **020** | 平台能力刷新（本轨道 RQ1） | taskbook `project-knowledge/FABLE5-REDESIGN-001/MNE-DR-020-platform-capability-refresh-taskbook.md` |
| **021** | 交接实践现状（本轨道 RQ2） | taskbook `…/MNE-DR-021-continuity-practice-taskbook.md` |
| next | **022** | |

### 5.2 消歧备注

- 数字 014/015 曾在本分支 commit fe40814（2026-08-31，存续约一小时、未合并）短暂标注本轨道两课题，随本终案改判归属验证包审计/表面威胁——考古时以本记录为准。
- 自今日起新对话/工作引用八月六项研究一律用 014~019；读 8 月冻结档案（Alaya 导出、raw/validation-reviews、received 件等）遇 MNE-DR-001~006 按"曾用号"列解读。

### 5.3 注册表补丁 v2（取代 §3，交维护线）

1. `next_unallocated_sequence` → **022**；
2. §2 六行既有 issued 记录改号 014~019，各加 `former_number: MNE-DR-00X`、`former_number_scope: frozen_materials_and_pre_2026-08-31_references`；
3. 回填 legacy 001~013 行（数据源本记录 §2；`legacy_003: not_found`）；
4. 追加 020/021 两行（canonical FABLE5-REDESIGN-001-RQ1/RQ2，issued_ready_not_executed）；
5. 规则行：全序列严格唯一；曾用号仅为读档别名不再签发；活文件旧号引用 lazy migration；
6. 风险登记簿记录建议同 §3 第 5 条。
