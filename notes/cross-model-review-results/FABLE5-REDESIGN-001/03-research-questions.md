# FABLE5-REDESIGN-001 · 研究需求清单（v1，随门 0 提前交付）

```yaml
record_type: research_questions_register
track_id: FABLE5-REDESIGN-001
version: v1
date: 2026-08-31
trigger: 门 0 批示（09-continuation/03）——Owner 要求在整理期即识别 Deep Research 课题并出任务书文件，优先消耗 ChatGPT Pro 周额度
principle: 决策拉动——只列"影响某个具体决定"的问题；每题登记其影响的决定、期望证据与到期处置（对冲反模式清单 #7"研究由额度调度、无闭环"）
allocation_note: MNE-DR-007/008 为候选显示名（注册表 next_unallocated_sequence: 007，核对于 2026-08-31，含 PR #316 增量；本轨道无注册表写权限，正式登记待维护线任务补记；启动运行前若怀疑并发占号，重读注册表确认）
```

## 1. 课题清单

| ID | 课题 | 状态 | 影响的决定 | 期望证据 | 到期处置 |
|---|---|---|---|---|---|
| RQ1 | 平台能力刷新（2026-08/09 现状）——任务书 `project-knowledge/FABLE5-REDESIGN-001/MNE-DR-007-platform-capability-refresh-taskbook.md` | **READY，可立即执行** | 阶段 2 记忆载体与交接机制能依赖哪些当前平台功能；旧平台结论（RC-2026Q2 子课题2/3/4、DR6）的时效替换；模型自识别调查项（A3b 遗留） | 逐条带"截至日期"的产品事实＋旧结论核对表 | 报告返回后由本轨道 7 日内消化登记；若阶段 2 开始时仍未执行，阶段 2 平台依赖全部标 UNKNOWN 处理 |
| RQ2 | 跨会话连续性实践与评测（2025-2026）——任务书 `project-knowledge/FABLE5-REDESIGN-001/MNE-DR-008-continuity-practice-taskbook.md` | **READY，可立即执行** | 阶段 2 交接方案的机制选型与舍弃理由；"像同一个对话"的机械验收指标选定（登记表 §4.1）；RPT-2026Q2-0001/DR1/DR2 的时效刷新 | 机制盘点＋基准指标＋失败模式＋与现行方案的三向对照 | 同上 |
| RQ3 | 需求生命周期管理方法（需求工程×LLM agent：捕获/查重/矛盾/时效重评/反馈闭环的业界方法） | DEFER——待登记表经 Owner 确认、阶段 1 冻结问题面后出题，避免课题被上游裁决作废 | 阶段 2 需求生命周期状态机的设计依据 | 方法与工具盘点 | 阶段 1 结束时重评是否出题 |
| RQ4 | 学习者建模/个人画像的证据现状（知识技能图谱、思维模式分析的可靠性边界） | DEFER——属 Alaya/目标项目线，非本轨道决定所需；且 #244/#265 pilot 决策未开 | 学习类 agent 目标设计（N-08/O-21） | 学界实证与伦理边界 | 目标项目立项时移交该线出题 |
| RQ5 | ChatGPT/Codex 对话内模型自识别复查 | 并入 RQ1 的 Q6（单独立题过小） | 署名惯例 §6 可信度分级的 ChatGPT/Codex 行更新 | 官方口径 | 随 RQ1 |

## 2. 既往深度研究的时效评估（Owner 要求：不跳过旧课题）

| 旧轮次（完成时点） | 内容 | 时效判定 | 去向 |
|---|---|---|---|
| RC-2026Q2-initial 综合＋轻度1~6（2026-05~06） | 外部记忆总论；对话/开发 agent/云端写回各表面能力；理论依据；跨场景迁移 | **平台能力部分已过期高风险**；理论与工程依据部分耐久 | 平台部分→RQ1；实践格局→RQ2；理论部分不重做 |
| RC-2026Q2-memory-testing DR1（2026-06） | 记忆系统测试/调试/评估/失败诊断 | 方法论耐久；基准与工具格局可能已变 | 基准部分→RQ2 Q2/Q3 |
| RC-2026Q2-handoff-strategy DR2（2026-06） | 交接策略与量化评估（曾直接改写执行源 §15） | 方法论耐久；产品功能引用过期风险 | 产品部分→RQ1 Q5；指标对照→RQ2 Q7 |
| RC-2026Q2-user-input-governance DR4（2026-06） | 用户原文/脱敏/可见性治理 | 治理原则耐久，暂无刷新必要 | 不重做；阶段 2 引用时标注采集时点 |
| RC-2026Q2-first-target-dry-run DR5（2026-06） | 首个真实目标试运行评估框架 | 框架耐久 | 不重做 |
| RC-2026Q3-platform-context-apps-delta DR6（2026-07） | Project memory/apps/GitHub/DR/no-write delta | **自我声明时效敏感**，已满 1 月＋ | 整体由 RQ1 刷新（RQ1 Q8 核对表即其关键结论） |
| RC-2026Q3-frontier-planning-clarification（2026-07~08） | 澄清路由架构 | 路线被 Owner 无限期暂停 | 不刷新；若路线恢复再评 |
| MNE-DR-004 能力归属 / MNE-DR-005 跨仓库并发 / MNE-DR-006 交接加固（2026-08 上中旬） | Fable 侧研究/审计 | 尚新（≤1 月）；且为仓库内证据非外部时效事实 | 不刷新 |

## 3. 执行意图声明（本文件与两份任务书）

```yaml
execution_intent:
  response_role: ANALYSIS_AND_PREPARATION
  execution_disposition: RUN_NOW_OPTIONAL（Owner 已声明将亲自发给 ChatGPT 并消耗 Pro 额度；何时/是否发送由 Owner 决定）
  external_execution_or_quota_authorized: false（任务书就绪≠额度已花；执行动作是 Owner 亲手发送）
  per_run_requirements: 每个课题单独新对话；deep research 模式；智能程度选 Pro；对话命名建议用显示名
```

## 4. Deep Research 模式现状摘要（任务设计依据，时效事实，核对日 2026-08-31，来源：网络检索，运行时以产品 UI 为准）

- 2026-02 起 Deep Research 底层由 o3 换代（报道称 GPT-5.2 系），可连接 MCP/连接器、可限定信源、可中途插入补充；2026-03 起模型选择器改为 Instant/Thinking/Pro 三档；2026-03-26 legacy deep research 模式移除。运行时长通常 5~30 分钟，综合数十至数百来源。
- 与仓库既有 DR6（2026-07）结论兼容：DR 期间对连接 app 只读；有计划配额；报告可导出。
- 上述均为 operator 侧待核验事实——任务书已按"运行时以 UI 为准"编写，不依赖具体数字。
