# 阶段1 复合评审 — 总摘要与发现索引

```yaml
track_id: FABLE5-REVIEW2-001
record_type: composite_review_phase_summary
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: summary_of_labeled_findings_see_theme_files
authority_level: non_execution_source_advisory_evidence
phase: phase_1_composite_review
next_gate: gate_2_owner_review_of_composite_findings
theme_files:
  - 01-spec-core-needs-coverage.md
  - 02-spec-section-conformance.md
  - 03-freshness-and-staleness.md
  - 04-acceptance-debt-register.md
  - 05-cost-and-process-weight.md
  - 06-single-point-risks.md
  - 07-scalability-and-multi-target.md
  - 08-first-round-deferred-items-recheck.md
finding_counts:
  BLOCKING: 0
  REPAIR_RECOMMENDED: 9
  NON_BLOCKING: 8
  OBSERVATION: 15
  QUESTION: 3
  acceptance_debt_items: 17 (2 HIGH / 6 MEDIUM / 9 LOW)
```

## 一段话总评

仓库的**纪律与保全**是强项（挂账诚实、逐任务落盘、事故必复盘），**质量债很少**；主要问题集中在三个结构层面：(1) 执行源与现实脱节——§7 指定的启动文件已死、三处平台快照过期、实际统治日常行为的 13 份 guard 层在执行源中没有地位；(2) 状态层只有创建纪律没有失效纪律——live 文件靠人记得更新，三处关键路标停在 6~7 周前；(3) 流程只加不减——指导必读清单在自家评审建议收缩后反而扩到 13 份文件，约 23% 的任务是纯记账。此外，Owner 已宣布的实用化转向（真实需求 A/B）在仓库中尚无落地痕迹，而它依赖的并发安全验证（F2）与多项决策正排队等 Owner。无任何 BLOCKING 级发现。

## 九条 REPAIR_RECOMMENDED 发现（全部索引）

| ID | 主题 | 一句话 | 所在文件 |
|---|---|---|---|
| R2-CORE-002 | 方向 | 自我治理产出远大于目标项目产出；Owner 已定的转向未落地 | 01 |
| R2-CONF-001 | 执行源 | §7 是死条款：指定的启动文件两个冻结一个弃用，冲突未登记 | 02 |
| R2-CONF-002 | 执行源 | §5 研究证据层描述停在"7 份报告"时代（现 13 个轮次） | 02 |
| R2-CONF-005 | 执行源 | guard 层实际统治行为但在执行源中无地位定义（规则治理双轨） | 02 |
| R2-FRESH-001 | 状态 | 启动三件套全部过期/弃用，是指向已拆桥梁的活路标 | 03 |
| R2-FRESH-002 | 状态 | 自称 live 的评审总览含大段过期内容（greenfield 节停在 7 月中） | 03 |
| R2-COST-001 | 流程 | 指导加载负担已确诊已开方未服药，且必读清单继续加重 | 05 |
| R2-COST-006 | 流程 | 规则层只有加法机制没有整合机制（结构性根因） | 05 |
| R2-SCALE-002 | 扩展 | F2 并发门与真实需求 A/B 立项存在未决的先后依赖 | 07 |

## 跨主题合流：建议进入阶段2 分诊的六个"修复束"

多条发现指向同一根因，分诊时建议按束处理而非逐条：

1. **执行源时效性修订束**：R2-CONF-001 + 002 + 003 + 004 + GF5-TRIAGE-008 升级 + overfitting refresh-gate 失效（专题08）。一次 Owner 批准的 spec 修订任务可全部解决。
2. **规则层治理设计束**：R2-CONF-005 + R2-COST-001 + R2-COST-006 + 199 load-profile 搁浅。这是门3 最重的候选设计题（guard 层地位、加载分层、整编周期三合一）。
3. **状态失效纪律束**：R2-FRESH-001/002/003/006 + GF5-ENH-CUR-004 升级 + R2-SCALE-006。最低成本版本已具体化（live 文件强制 last_updated + 失效声明）。
4. **Owner 决策打包束**：D-01（F2 G2A）+ D-02（#265 结算与 A/B 立项）+ D-04（HO-GUIDANCE-001）+ D-16 + D-17（署名方案）+ 连续性销账（专题08 的 009 拆分）。这不是设计题，是一份待批清单——门3 时呈交。
5. **历史收尾束**：D-03/D-05（已毕业对象的 BLOCKED 门作废或收尾）+ D-06/D-07（证据保全设计）+ GF5-TRIAGE-001 改判 + ENH-CUR-003 销账。
6. **多写入方常态化束**：署名方案确认（既定日程）+ R2-CONF-006（§18 泛化）+ R2-SCALE-004（任务号命名空间追认）+ R2-CORE-004 缺口。大部分搭署名方案确认的车。

三条 QUESTION（R2-CORE-005 学习系统立项、R2-CONF-007 语言分层、R2-SPOF-001 连续性销账语句）已并入上述束 4/2/4。

## 同族证据限制声明

本轮全部发现由 claude-fable-5 单一模型产出（§19 同族限制）。其中对**第一轮 Fable 工作**的复检（专题08）不构成独立复核；对 **GPT 侧两个月工作**的评审具备跨族视角但仍是单模型意见。按既定日程，ChatGPT Pro 恢复后的联合确认可同时充当本轮发现的异构复核机会。

## 返回契约（阶段1）

```yaml
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
branch: fable5-review2-001-workspace
phase_1_deliverables: 9_files_under_01-composite-review/
changed_paths_this_phase:
  - notes/cross-model-review-results/FABLE5-REVIEW2-001/01-composite-review/00-phase1-summary.md
  - notes/cross-model-review-results/FABLE5-REVIEW2-001/01-composite-review/01..08 (八个专题文件)
protected_paths_untouched: current/**, 既有 notes/**, handoff/**, raw/**, target-projects/**, commands/**, README.md, 两个保留分支
validation_method:
  - 全部 VERIFIED 主张附仓库证据路径；日期类主张以 git log 核验
  - 量化主张（guard 行数、记账占比、任务计数）来自可重放的 shell 计数命令
  - 无外部研究、无付费调用；GitHub 只读 API 与 gh CLI 仅用于 issue/PR 元数据
known_limitations:
  - 单模型同族评审（见上节声明）
  - notes/ 深层（owner-review-working、validation-designs 全文等）为抽样读取，未逐文件全读
  - WORK-ULTRA Stage A/B 归档 tar 未解包（其结论经 README/receipt/decision-matrix 层核验）
  - 会话侧未入库信息不可见，默认以仓库为准
next_gate: 门2 — Owner 审阅本阶段发现；批示后进入阶段2 分诊（优先级矩阵+修复建议+代价评估）
```
