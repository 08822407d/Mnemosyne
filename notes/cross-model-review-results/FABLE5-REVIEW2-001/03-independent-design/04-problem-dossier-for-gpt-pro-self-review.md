# 问题详录 — 供 ChatGPT Pro 自我检讨与教训总结用

```yaml
track_id: FABLE5-REVIEW2-001
record_type: problem_dossier_for_heterogeneous_self_review
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: VERIFIED_REPOSITORY_FACT_unless_labeled
authority_level: non_execution_source_advisory_evidence
audience: ChatGPT_Pro_self_review_session (Owner 转交)
companion_file: 05-cross-model-failure-analysis-and-experiments.md（Claude 侧自我记录与两族对照在彼处）
fairness_note: >
  本详录记录的问题发生于 GPT 族（ChatGPT 对话/Work + Codex Cloud）作为唯一
  建设执行族的时期，但"发生在谁值班时"不等于"由谁的缺陷造成"。每个问题
  均给出多重成因假设（模型行为/流程设计/Owner 输入/平台故障），供自我检讨
  时逐一判别，而非预设结论。Claude 族自身的缺陷记录见配套文件 05。
usage_note_for_pro: >
  建议逐问题回答文末的"自检问题"，区分：(1) 我会重犯吗；(2) 根因归类；
  (3) 什么机制能挡住它；(4) 该机制对我的工作方式的成本。产出教训清单
  供合作方案与后续修复排期使用。
```

## P-01 · 启动文件冻结 47 天且冲突未登记

**现象**：`current/active-context.md` 与 `current/open-questions.md` 自 2026-07-06（MNEMOSYNE-085）后零实质更新；期间约 158 个任务号的工作照常进行。执行源 §7 仍要求新会话优先读它们；§4 要求"与 spec 冲突应登记 open question"——冲突实际存在数周，无一个会话登记。
**证据**：git log -- current/active-context.md（末次 d8a9182 2026-07-06）；同 open-questions.md；spec §4/§7 原文。
**时间线细节**：07-06 后至少有 6 个任务专门做"current-state sync/residue repair"（139、151、154、156 等），都修了别的状态文件，无一触碰这两份。08-11 的 MNEMOSYNE-199 评审注意到它们（归类为"不默认读"），但也未触发修复或冲突登记。
**成因假设**：(a) 模型行为——任务范围纪律极强的副作用：不在任务书里的文件绝不动，哪怕明知过期；(b) 流程设计——"发现问题→必须开新授权任务"的门槛让顺手登记一条 open question 都显得越权；(c) 结构——open-questions.md 本身冻结，登记冲突的指定容器就是冻结文件之一（自指死锁）；(d) Owner 输入——无人指派过"检查启动文件新鲜度"的任务。
**自检问题**：任务范围纪律与全局状态责任的边界在哪？看到"章程要求读的文件明显过期"时，你当时的会话为什么没有说出来？如果说了，流程允许你做什么？

## P-02 · 自称 live 的总览文件半新半旧

**现象**：`current/review-and-validation-status.md`（113 创建，自称 live wayfinding）的 greenfield 段停在 GF-STEP-2C；其后 130~143 十余个存档任务逐步推进到 GF-STEP-5，每个任务都更新了 manifest 与各自 status，无一个回头更新这份总览；其余段落却是新的——半新半旧比全旧更难识别。
**证据**：该文件 greenfield_track 段 vs FABLE5-GREENFIELD-001 manifest 的 step_records。
**成因假设**：(a) 创建者与更新者分离——113 建文件，后续任务的任务书没写"更新它"；(b) 冗余登记面太多——同一事实要写 manifest、专线 status、总览三处，模型优先完成任务书点名的那处；(c) 无失效声明——文件没说"谁负责保鲜"。
**自检问题**：当一个事实有多个登记点时，你如何决定更新哪些？"任务书没点名"是否应该成为不更新的充分理由？

## P-03 · 加载清单在自家评审确诊后继续增长

**现象**：08-11 MNEMOSYNE-199（GPT 侧执行）确诊 loader 必读 11 文件过度、建议收缩到 3+条件加载；其后 08-14 MNEMOSYNE-210、08-15 MNEMOSYNE-225 创建新 guard 时把自己加进必读清单——13 份必读，与自家评审方向相反。收缩方案停在 candidate。
**证据**：notes/runtime-guidance-utilization-review-2026-08.md F1/§6；git log -- commands/load-mnemosyne-guidance.md；load-profile-candidate 文件状态。
**成因假设**：(a) 模型行为——每个任务局部正确（新 guard 当然要被加载），无会话持有"清单总量"的全局视图；(b) 流程——candidate 的采纳需要 Owner 专门批准，而往清单加一行不需要，阻力不对称；(c) 时序——210/225 的任务书可能写于 199 结论传播之前 [MODEL_INFERENCE]。
**自检问题**：你在 210/225 会话中是否读过 199 的结论？若读过，为何仍加必读？"遵守任务书"与"引用仓库内已有的相反结论"冲突时你的优先序是什么？

## P-04 · 发布事故链：五个任务同一目标连续失败

**现象**：MNEMOSYNE-235~239（08-18~20）为同一次 91 文件发布连续失败五次，全部 BLOCKED_CLOSED_NO_RETRY；两次 Pro 法证裁定归因含执行面故障（dual-failure、execution-surface）；最终 240 换架构（本地确定性 git）+241 成功。
**证据**：F2 status publication_closeout 段；两个 Pro 裁定 ID。
**成因假设**：(a) 平台故障为主（法证裁定已认定部分）；(b) 重试策略——第 2 次失败后是否就该切换通道而不是再试 3 次？(c) 任务粒度——每次重试烧一个任务号，事故记账反而增加恢复摩擦。
**自检问题**：连续失败几次后应停止同通道重试？当时的会话有没有备选通道意识？"换通道"的决策为什么要等到第五次失败与两次法证之后？（注：235–239 每个任务的关闭都合规且记录完善——问题不在纪律在策略。）

## P-05 · 记账任务占比约 23%

**现象**：第一轮时点后 146 个合并 PR 中约 34 个是 closeout/post-merge/sync/finalize 类；典型链：实质任务→PR 收尾任务→合并后闭环任务→状态同步任务。
**证据**：git log --merges 计数（可重放）；例：157→159、160→161→162、241→242。
**成因假设**：(a) 断续会话模式的理性适应——每个任务都可能是该会话最后一个，所以状态必须即时结清；(b) 惯例自增强——早期几次"residue repair"事故后，收尾任务成了默认动作而不再评估必要性；(c) 工具面限制——ChatGPT 会话无法像常驻会话那样在一个任务内多次提交推送。
**自检问题**：哪些收尾任务在"常驻会话+即时推送"工具面下可以合并回主任务？你能否给出"什么时候确实需要独立收尾任务"的判别标准？

## P-06 · 执行源中的时代快照句（三处）

**现象**：§5"7 份报告"、§10"Codex Cloud 主要作为远程写入助手"、§14"Codex Cloud 不能收非图附件"——起草时正确，随现实漂移变错；第一轮评审（GF5-TRIAGE-008）已警告此模式并裁定"易变事实外置"，两个月后三处仍在。§18 自带的时效核验义务与 overfitting 处置的 refresh gate 都声明了、没执行过。
**证据**：spec 对应节原文；Pro decision-matrix GF5-TRIAGE-008 条；阶段1 专题02。
**成因假设**：(a) 起草习惯——把当下事实写成规则背景；(b) 机制缺失——"发现过期→登记"无任务义务承载（修订案文的修订7 即为此设）；(c) 裁定后无实施任务跟进——GF5-TRIAGE-008 的路由是原则（keep stable principles）而没变成活修复任务。
**自检问题**：裁定"方向正确"之后由谁把它变成任务？你的裁定输出格式里是否缺一个"实施钩子"字段？

## P-07 · Owner 高优先级事项单过窗未结算

**现象**：Issue #265（08-10，四个 workstream，窗口 08-11~15）过窗一周无完成度标注仍 OPEN；其中 TODO 2 的真实需求 A/B 零落地、TODO 4 未执行。窗口内确实做了大量工作（owner review、TLR、F2），但没人回头对账。
**证据**：gh issue view 265；阶段1 专题03 R2-FRESH-005。
**成因假设**：(a) Issue 不在任何会话的任务书里——与 P-01 同构的范围纪律副作用；(b) 事项单粒度是"方向"而任务是"动作"，对账需要判断力没人被授权行使；(c) Owner 侧未指派结算。
**自检问题**：Owner 的意图文档（issue/评论）在你的工作流里处于什么地位？谁应该负责对账——每个任务？定期专项？还是 Owner 自己？

## P-08 · Q6 四笔账的记录说明（按门3 批示：不销账，详录备查）

按 Owner 批示，以下四项**不关闭**，此处做详细记录说明供检讨与后续裁定：

1. **机械 no-write 门 BLOCKED + W4 open_uncertain**：源自 Meta-Agent replay 时代（07 月中）；行为验证 5/5 PASS 而机械证明始终缺失，按 §19 如实挂 BLOCKED。对象（Meta-Agent 的 Mnemosyne 侧路线）已于 08-05 迁出退役。挂账本身合规且诚实；问题是"对象消亡后挂账何去何从"无先例规则。关闭它需要：Owner 一句作废声明或一次 observer-assisted 补证。**留给检讨的点**：验收债应否随对象退役自动转历史？
2. **GF5-TRIAGE-001（FR-01/03 平台表面研究）DEFER 未执行**：裁定于 07-23；此后 §18 修正、DR6、claude-github-work-surface-facts（08-15）与两次真实表面事件（发布事故、Claude 通道打通）已实质覆盖原研究动机。**留给检讨的点**：DEFER 类裁定是否需要自带"失效条件"（什么情况出现即自动销账/重定范围），避免永久漂浮？
3. **GF5-ENH-CUR-003（no-re-ask 约定）未采纳**：当时判 medium 未采纳；两个月后其目标被 onboarding+per-route status+署名方案组合部分覆盖。**留给检讨的点**：同上——增强建议的"被其他机制覆盖"判定由谁、何时做？
4. **Owner 连续性无方案**：GF4-F08 与 GF5-OMIT-CUR-002 两轮点名，P3 watch 至今。单人瓶颈的吞吐维度已显性化（2 项 HIGH 决策债排队）。**留给检讨的点**：watch 类条目的复查节律；以及"接受风险"是否也该是一种显式可记录的合法结局（而不是默认无限挂起）。

## P-09 · 正面记录（检讨的对照面，避免失衡）

以下 GPT 族执行期的强项应在教训总结中显式保留，防止"检讨"演变为推翻有效纪律：
- **挂账诚实**：抽样所见零粉饰（BLOCKED 从不写成 PASS）；
- **事故→规范反射**：116 双 PR→118 guard、#170/171→artifact guard、277 Draft 误用→210 修订，每次事故都沉淀了可复用规则；
- **保全文化**：发布事故中先建 capsule 再恢复；评审归档哈希级精确；
- **验收升级**：8 月起 OR/TLR 系列建立了真实 Owner 验收，修复了第一轮指出的同族自证短板。

## 给 Pro 的总自检框架（建议输出格式）

对 P-01~P-08 逐项输出：

```yaml
problem_id: P-0X
recur_risk_for_me: high | medium | low   # 我会重犯吗
root_cause_class: model_behavior | process_design | owner_input | platform | mixed
my_analysis: <两三句>
blocking_mechanism: <什么机制能挡住it>
mechanism_cost: <该机制对我的工作方式的代价>
disagreement_with_dossier: <若认为本详录的记录或假设有误，指出并给证据>
```

外加一节自由式教训总结（面向合作方案：两族协作时如何互补对方的盲区）。本详录作者的盲区与缺陷记录在 05 文件——**建议 Pro 检讨时同时批判 05 中 Claude 的自我记录是否避重就轻**。
