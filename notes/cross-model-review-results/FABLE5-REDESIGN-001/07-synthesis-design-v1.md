# Mnemosyne 合成设计 SYN-2

```yaml
record_type: synthesis_design
track_id: FABLE5-REDESIGN-001
version: SYN-2_PRE-FREEZE（SYN-1 经 MNE-DR-032 复核 ADOPT_WITH_CHANGES 后的修订版；BLOCKER-01~09 逐项闭合，对照见 08 附件 ANNEX-F 与本文件 §13）
date: 2026-09-01
normative_unit: 本文件＋08-syn-annexes-normative.md 于同一 commit 构成唯一规范根（版本锚=commit SHA）；**04 与 MNE-DR-029 自本版起降为 evidence/reference，全部规范权由本单元承接**（closing BLOCKER-01/D-07）
citation: 逐项追踪见 ANNEX-F；[INF]=INFERENCE 待校准，汇总见 §12
status_gates: **Owner 已采纳（2026-09-01 批示"采纳"）**；预冻结测试（ANNEX-D）与迁移 T0 为后续独立门，未自动开始
```

## 0. 最小可用子集

五件即可运行：规范根＋manifest；当前视图＋变更集；检查点＋Quick Card 交接（ANNEX-C）；加载表＋minimal 收据（ANNEX-B）；双闸门。其余层须经目的核查证明"购买了已测出的失败面"方可启用。

## 1. 公理、架构与权威

公理：记录≠加载≠呈现（N-19）；原文≠资产、裁决是资产（N-14）；耐久核心/可再生层（N-15）；节奏声明制（N-18）；规范库集中＋整体迁移＋唯一权威源（N-17）。

**架构七层（A 系，closing D-06）**：A0 Owner 目的与授权 → A1 耐久核心（原始证据/裁决/当前规范/测试真值）→ A2 可再生投影 → A3 任务工作态与检查点 → A4 上下文编译器 → A5 概率模型适配层 → A6 确定性工具与权限闸门。三面（写全/读省/呈人话）纵贯 A 系。

- 五个禁止依赖的假保证（入迷你章程）：模型确定性；上下文可寻址；指令/数据天然隔离；规则文本自动强制；交接=完整进程快照。
- 权威语义六分表（029 §1.3 采纳为正文语义）：Owner 要求什么→A1 目标与裁决；发生过什么→原始证据与不可覆盖变更记录；现在执行什么→当前有效规范；任务进展→检查点；本模型怎么读→A2 模型投影；动作是否允许→A6 闸门。每域唯一 canonical，派生只引用。
- 轻量语义账本：语义变更=原子变更集（change record＋当前文档＋trace＋校验同 commit）。**裁决快车道**（closing D-14）：紧急时允许 current 先行变更，但必须携带 `provisional=true`＋Owner 一字引用，48h 内补全变更集并通过 reconciliation 校验；逾期未补=integrity stop，provisional 变更回滚。
- 投影四不变量与"耐久≠常驻"判定：见 ANNEX-B；单向写：A2/派生层禁改实质内容，变更一律经 A1 裁决再编译。

## 2. 字段制度

三档（核心/条件/可选）逐字段矩阵见 **ANNEX-E**（含次档模型 fallback 规则与触发词机械判据）。"audit 档任务"的机械定义：写耐久核心 / 跨族交接 / 迁移步 / 测试运行 / 规范变更 / Owner 明示，六者其一即是。

## 3. 规范库（norms-library）

条目字段（全文，closing F-02）：`norm_id / statement / scope / status(active|superseded|retired|candidate) / supersedes / origin(L1 裁决引用＋日期) / verification(违反判定方式) / compiled_check(none|script|hook|清单) / enforcement(advisory|hard) / portability(mnemosyne_only|generic_candidate|generic_adopted) / built_for_model_generation`。

- **hard 规则必须有模型外强制层**；无强制层不得标 hard。现役 hard 实例：写前预检（scripts/preflight-write.sh）、worktree 分离。**双频道暂标 advisory＋Owner 抽查**，强制层（回复结构检查 hook）落地后升 hard（closing D-08/BLOCKER-07）。
- 复杂度预算：常驻核心 ≤200 行 [INF]；整编触发与减法同权；review 四类结果（merge/replace/archive/delete），只增不减=目的漂移信号。
- 晋升五条件（重复故障或 Owner 原则；作用域可界定；无更低成本表达；有退出条件；过新上下文负测）；晋升序：反馈证据→可复现 case→eval/test/hook→必要时才是规则。
- N-17 工程化：唯一写权目录；rule_id 引用；migration-manifest；迁移后旧址仅重定向。散文 guard 原件转 A1 历史，逐条映射机械校验。

## 4. 三态循环与捕获

S0 原始（有毒，完整捕获不信任）→S1 经检查构想（只供裁决）→S2 执行层；单向晋升＋新事件回环；禁止覆盖改写。

- 捕获时限统一 **48h**（closing D-09；"当日"表述废除）；随手输入发给任一在场 agent 即入 S0 inbox，由该 agent 在 48h 内转录。
- 反馈 bundle 核心档八字段（id/时间/原话或 capture_mode/触发输入/观察/期望/影响/复现）；全集条件档（audit 任务）。
- S1 最低八问与 S1→S2 晋升门（029 §3.4-3.5 采纳为正文义务）：目标与授权明确；无未决同权威冲突；状态允许；验收与停止条件写明；高风险有机械检查或 proof-gap；目的核查过；touch 预算内；变更集三同步；模型产物不得自批。

## 5. 需求生命周期

**ANNEX-A 为规范正文**：18 态、转换表、defer_reason/revisit_trigger、MODEL-EVENT、quarantine 例外、人话出口。

## 6. 加载/投影

**ANNEX-B 为规范正文**：六级装载类（L0~L5）＋data_only 机器边界、八步算法、两档收据、指标数据映射、not_measurable 纪律、检索升级阶梯（冻结 eval 触发）、投影四不变量。任务型加载表与应载/实载/漏载/误载四单照 SYN-1 保留；污染指标阈值在预冻结测试校准 [INF]。

## 7. 目的核查（与 fail-closed 同级）

双闸门（Integrity=STOP_INTEGRITY / Purpose=STOP_PURPOSE 同权）；九触发点与十条自动停止规则见 ANNEX-B 末节（正文）。逐轮 purpose_delta 一行；周期目的账单（收尾记账 15% [INF]；分母=该周期全部任务记录条目数，治理类=收据/登记/归档/收尾四类标签 [INF]）；连续 2 个声明周期零 G 推进→STOP [INF]，周期取自 operating-profile，安全/事故处置豁免。目的账单入异族抽检与 Owner 抽查。

## 8. Owner 负担双账（closing D-12/BLOCKER-06）

- **agent_touch 账**（029 口径）：计入=不可合并的决定/批准/补件/搬运/纠错（failure_touch、manual_transfer 单列）；不计入=发起、交付、Owner 自愿补充。预算 routine=0/standard=1/high-consequence=2/owner-defined [INF]。
- **owner_manual_actions 账**（登记表口径）：发起、上传、复制、核对、纠错全计。**交接验收 ≤2 步以本账判定**。
- 超支五步阶梯＋三件套内嵌：合并提问；每问带（a）人话意思（b）答后果＋推荐默认＋各选项后果（c）不答/晚答后果；缩 scope；defer 非关键；仍超才一次 ESCALATE_OWNER。
- 两账＋owner_time 估计分别可重算（预冻结证据条件 6）。

## 9. 呈现面制度

双频道（对话人话/技术进文件；advisory＋Owner 抽查，hard 化路径见 §3）；状态机人话出口（ANNEX-A）；三件套（§8）；N-11 套用成本度量（新 agent 从零到记忆系统就位的 owner_manual_actions 与耗时入账，目标逐代下降）；人类投影页为 A2 标配。

## 10. 迁移（T0~T5）

照 SYN-1 六步保留，修订两处：T2 的规范映射抽检**不预设比率**——由 T0 盘点产出的规则数量/风险/重复分布决定分层抽样方案（含最小样本与停止条件），随 T0 退出条件一并冻结（closing BLOCKER-09）；每步一 PR、影子并行、只切新会话、revert、不重写历史。

## 11. 反模式自检与测试

16 条自检索引照 05b §2；运行级负测（#9/#12/#14/#16）由 **ANNEX-D 协议**承担；PRE-FREEZE 状态维持至十条通过门全过。

## 12. [INF] 与 UNKNOWN 登记

[INF] 全表：≤200 行；15% 及其分母/分类定义；2 周期 STOP；touch 默认 0/1/2；返场 2 周期；12-case 配额与六臂；Owner 参与 ≥2、盲抽 1；provisional 48h 补录窗；audit 档触发六项之界定。UNKNOWN：继承 029 §12.4 全部 14 条，另加：used_source_refs 测量办法；双频道强制层形态；**恢复登记**（closing F-13）：条目化压缩失义风险、purpose_delta 自报美化风险——均保持开放，不因"已有对冲"关闭。

## 13. BLOCKER 闭合对照（MNE-DR-032 §4.2 → 本版）

| BLOCKER | 闭合处 |
|---|---|
| 01 唯一权威 | 头部 normative_unit 声明＋ANNEX-A/B/C/D 正文化＋04/029 降级 |
| 02 三档矩阵/层号 | ANNEX-E 逐字段＋A/L/S 三系正交命名＋触发词机械判据 |
| 03 收据支撑指标 | ANNEX-B 两档＋指标数据映射＋not_measurable 纪律 |
| 04 交接字段/分层 | ANNEX-C：hidden_dependencies 条件核心（none 显式）＋风险×能力类矩阵＋登记制能力类＋升档规则 |
| 05 测试协议 | ANNEX-D：十条门＋11 问题列出＋条件 F 全档审计＋cosmetic 定义＋残留控制＋冻结纪律 |
| 06 双账/双层归因 | §8 双账＋ANNEX-D 四轴×工程子因矩阵 |
| 07 hard 一致性/快车道 | §3 双频道降 advisory＋§1 provisional 机制 |
| 08 时间/阈值/标签 | §4 统一 48h＋ANNEX-C 去 7 天上限＋ANNEX-F 一对一追踪＋§12 [INF] 全表与风险恢复 |
| 09 抽检率 | §10 T0 后冻结抽样方案 |

## 14. 自我批判（承 SYN-1 §14 全部有效，另加）

8. 本轮修订仍由 Fable 执笔且未再经异族复核——对冲：BLOCKER 闭合对照表逐项机械可查（§13＋ANNEX-F），Owner 可要求 MNE-DR-033 二次复核或径行采纳（成本取舍在 Owner）；
9. 正文化使规范单元体量上升（07＋08 约 400 行）——仍在常驻 ≤200 行预算之外（规范单元属 A1 耐久核心，非常驻装载集；常驻的是由它编译出的迷你章程与任务加载表）。
