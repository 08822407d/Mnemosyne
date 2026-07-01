# DR5 v2 首个真实 target-project dry-run 的评测框架

## 执行摘要与对 Mnemosyne 的直接建议

对 Mnemosyne 而言，**first real target-project dry-run 的“成功”不应被定义为模型产出看起来完整、叙事流畅、交付包漂亮，甚至也不应被定义为单次任务完成**；它应被定义为：在**已选定真实 target、已明确 authority/source map、已批准 safe input 与 run manifest、且明确保持 no-target-write** 的前提下，Mnemosyne 能够在真实需求上下文中恢复正确上下文、使用外部长期记忆减少重复工作、在 handoff 后保持 continuity、对未知与冲突信息采取克制策略、并产出**可由未来使用者在模拟操作环境中验证有用**的离线交付包，同时全程保留足够证据，使评审者可以区分“真的验证到了什么”与“只是做出了一个看起来像成功的 artifact”。这一定义借鉴了 UAT 对“future users + simulated operational environment + user requirements”的关注、acceptance criteria 对 clear pass/fail conditions 的要求，以及 Google SRE 的 readiness review / postmortem / checklist 思路；同时也吸收了近年的 agent-memory 研究结论：很多系统在长上下文记忆 benchmark 上表现不错，但到了需要**把记忆用于后续行动、知识更新、冲突处理、和跨会话连续性**时，性能会明显下降。citeturn10view12turn10view13turn22view0turn12view8turn12view2turn12view5

因此，我对 Mnemosyne 在第一次真实 dry-run 之前的**直接建议**是：不要把它当作一次“证明系统成熟”的演示，而要把它设计成一次**证据门控的 acceptance-style dry-run**。最低前置条件应包括：真实 target 已选定；authority/source map 已显式记录；target runtime truth source 已声明；run manifest 已批准；safe input / user originals 存储政策已确认；redaction manifest 与 external-pointer safety 已通过；no-target-write 已被用户和操作者共同确认；评审 rubric 已预先冻结；以及 synthetic evidence 与 real evidence 使用不同命名空间与不同结果栏位。若其中任一项缺失，最合理的结论不是“勉强试一下”，而是 **BLOCKED**。这一 gate-first 思路与 production readiness review 的“先判定 readiness，再决定是否承担更高责任边界”一致，也与 NIST/ISTQB 所强调的计划、角色、验证目标先行相一致。citeturn22view0turn21search4turn10view12turn10view13

更具体地说，我建议 Mnemosyne v0.1 在第一次真实 dry-run 中**只追求四件事**：其一，证明外部记忆在真实目标需求里确实减少了上下文恢复成本，而不是只是“多存了一份摘要”；其二，证明 handoff package 能让后续会话或后续操作者重建关键状态；其三，证明 authority boundary、truth source、input governance 与 no-target-write 能被严格遵守；其四，证明最后的离线 delivery package 在**不写 target repository** 的前提下仍然能被用户或未来使用者评估为“可用、可核对、可决定下一步”。这比追求高分更重要，因为最新 benchmark 已反复显示：记忆系统最容易失败的地方不是“有没有检索出一段字”，而是**有没有把更新后的状态用到后续动作里、有没有拒绝过时前提、有没有在多会话/多阶段任务中保持决策一致性**。citeturn12view2turn12view8turn14view2turn18search0turn18search1

## 评测对象模型

Mnemosyne 需要先把“这次到底在评什么”对象化，否则任何结果都可能被误读。下面的对象模型是本框架的核心边界定义；其中前两个对象主要验证流程与治理，第三个对象才是真正应被视为“首个真实 target-project dry-run 证据”的对象，而后两个对象属于更高权限与更高责任层级，不能与 dry-run 混淆。这个分层方式与 smoke testing、tabletop exercise、UAT、PRR 的边界区分是一致的：烟雾测试只判断基本可运行性；tabletop 是讨论式演练；UAT 才面向未来用户与使用需求；PRR 则是更高层级的 readiness gate。citeturn21search2turn21search4turn10view12turn22view0

| 对象 | 核心定义 | 是否需要真实 target | 是否允许真实 target materials | 是否允许 target repository write | 主要结论价值 | 不能声称什么 |
|---|---|---:|---:|---:|---|---|
| synthetic smoke test | 用合成或维护者自造材料，验证最基本流程是否跑通 | 否 | 否 | 否 | 证明管线、模板、日志、manifest 机制可工作 | 不能声称记忆系统对真实需求有用 |
| tabletop dry-run | 围绕拟真的情境、角色和约束做讨论式/脚本式演练 | 可无真实 target，也可有但不 ingest 原始材料 | 原则上不 ingest 原始真实材料，最多用摘要或经批准片段 | 否 | 证明规则、角色分工、审批链和判定 rubric 可执行 | 不能声称已完成真实场景验证 |
| real target-project dry-run | 围绕**已选定真实 target**、在被批准的 authority 与 safe inputs 下，执行一次无 target write 的真实需求验证 | 是 | 是，但须经安全与存储政策批准 | 否 | 才可作为“first real target dry-run evidence” | 不能声称已完成 target delivery 或 repo-ready |
| target delivery | 面向目标项目使用者的实际交付包，可供采用、评审、修订 | 是 | 是 | 不必然 | 证明交付包有使用价值 | 不能自动推出 repo write 获批 |
| target repository write | 对 target workspace / repo 进行实际写入、提交、PR 或等效持久修改 | 是 | 是 | 是 | 进入更高授权边界 | 不能被 dry-run PASS 自动触发 |

对 Mnemosyne 而言，**real dry-run 的最低合法证据单位**应是一个“真实 target、真实需求、真实受约束材料、真实无写入边界、真实用户/未来使用者可评审”的运行包；它与 synthetic smoke test 的本质差异，不是“任务更难”，而是**证据对象、责任边界与风险暴露都不同**。NIST 对 tabletop exercise 的定义强调其本质是 discussion-based、用于验证计划内容；而 smoke test 本质上只验证基本功能/稳定性，目的是决定是否继续做更细测试。这恰好说明：Mnemosyne 不能把 smoke test 或 tabletop 的通过，升级表述为“真实项目已被验证”。citeturn21search4turn21search2

同样重要的是，**PASS 只允许落在对象层级内部解释**。也就是说：`real target-project dry-run = PASS` 的含义，仅仅是“在预定 no-target-write 边界内，本次真实 dry-run 达到了所定义的证据标准”；它**不等于** production-ready，**不等于** target repository write approved，**不等于** Mnemosyne global rule update approved。Google SRE 的 PRR 之所以值得借鉴，正是因为它把 readiness、ownership transfer、continuous improvement 分开看待：先 review readiness，再决定是否承担更高责任，再把 lessons contributed to best practices。Mnemosyne 也应该沿用这种分层，不应让一次 dry-run 的成功越权扩散。citeturn22view0turn10view11

## 能力维度与安全治理维度

从外部研究看，一个“有用且安全”的长期记忆系统，至少要覆盖六类能力：**信息提取与检索**, **跨会话推理**, **时间/变更感知**, **知识更新**, **对未知的 abstention**, 以及**把记忆用于后续动作而非只用于问答**。LoCoMo 说明长时对话中的 temporal/causal understanding 仍然困难；LongMemEval 把长期记忆拆成 information extraction、multi-session reasoning、temporal reasoning、knowledge updates、abstention 五类；MemoryAgentBench 进一步强调 accurate retrieval、test-time learning、long-range understanding、conflict resolution；MemoryArena 则指出“记住”与“行动”在真实任务中是耦合的，LoCoMo 上接近饱和的系统在 agentic multi-session setting 中仍可能表现很差；STALE 还表明，模型会接受用户问题里隐含的过时前提，最好的测试模型总体准确率也只有 55.2%。因此，Mnemosyne 的真实 dry-run 必须把**记忆 usefulness、冲突处理、过时上下文防御、以及行动级连续性**一起评，而不能只评“有没有回忆出用户偏好”这种低难度项。citeturn12view6turn10view1turn20search6turn12view8turn12view2

同样地，安全与治理维度不能被当作附属检查。NIST Privacy Framework 与 NIST 身份隐私指南都强调 data minimization、deletion、管理数据生命周期与审计日志时也要纳入 minimization；GitHub 官方文档则直接提醒：一旦敏感原文进入 Git 历史，清除非常困难，存在 recontamination、changed hashes、lost signatures、旧 clone 仍可追溯等风险。这意味着对 Mnemosyne 来说，“private repo”绝不自动等于“可以存用户原文”；相反，**safe input policy、redaction manifest、external pointer safety、no-target-write、以及 user originals storage policy 都应该属于一票否决类维度**。citeturn10view15turn10view16turn17view2turn17view3turn17view4

下表给出 **Evaluation dimensions v0.1**。它不是通用 benchmark，而是把上述研究证据与 Mnemosyne 当前约束综合后的工程评测表。表中 `deterministic_check`、`llm_judge_allowed`、`user_confirmation_required` 是评审责任分工，不代表互相替代。

| dimension_id | dimension_name | what_it_tests | evidence_required | deterministic_check | llm_judge_allowed | user_confirmation_required | failure_examples | severity_if_failed |
|---|---|---|---|---|---|---|---|---|
| D01 | target selection validity | 是否真有“被选定的真实 target”与真实需求窗口 | target selection record、scope note、user approval | 是 | 否 | 是 | 还没选 target 却称 real dry-run | Critical |
| D02 | authority/source-map completeness | 权限边界、可用来源、禁用来源是否完整 | authority map、source map、approval record | 是 | 否 | 是 | 用了未批准 source；边界缺失 | Critical |
| D03 | target runtime truth source status | 运行时到底以什么为真 | truth-source declaration、conflict policy | 是 | 否 | 是 | 自造 truth source；多个真源未排序 | Critical |
| D04 | safe input/user originals storage policy | 原始材料是否按最小化与存储政策处理 | ingest ledger、storage policy、retention note | 是 | 否 | 是 | 未批准就保存原文； retention 不明 | Critical |
| D05 | redaction manifest / external pointer safety | 脱敏与外链是否安全可审计 | redaction manifest、pointer list、pointer safety review | 是 | 可辅助 | 视情况 | 外链直指敏感原文；未脱敏摘录 | Critical |
| D06 | no-target-write preservation | 是否真做到不写 target repo/workspace | command/log transcript、diff proof、operator declaration | 是 | 否 | 是 | 生成文件落入 target repo；误提交 | Critical |
| D07 | synthetic-vs-real evidence separation | 是否把 synthetic 与 real 证据分开 | evidence manifest、artifact namespace | 是 | 否 | 否 | 用旧 smoke test 充当 real evidence | Critical |
| D08 | memory schema fit to target needs | 记忆结构是否匹配目标任务 | memory schema、retrieval examples、decision log | 部分 | 是 | 是 | 把决策、事实、待确认项混成一类 | Major |
| D09 | handoff package usability | 新会话/新操作者能否恢复状态 | handoff package、replay note、recovery test | 部分 | 是 | 是 | 读完 handoff 仍无法知道下一步 | Major |
| D10 | unsupported assumptions handling | 遇到未知/缺证据时是否克制 | assumption log、abstention examples | 是 | 是 | 是 | 把猜测写成事实；未升请用户确认 | Major |
| D11 | stale/conflicting context handling | 是否识别并处理过时/冲突上下文 | conflict log、supersession note、resolution log | 是 | 是 | 是 | 同时引用旧政策与新政策；接受过时前提 | Major |
| D12 | delivery package completeness | 不写 repo 时交付包是否仍完整可评审 | package inventory、traceability map、acceptance rubric | 是 | 是 | 是 | 包里没有来源、决策、限制、待确认项 | Major |
| D13 | target-specific/global lesson separation | 是否把个案经验误升格为全局规则 | lessons table、global-candidate rationale | 是 | 是 | 是 | 一次 target 成功就改 global rule | Major |
| D14 | postmortem quality | 复盘是否事实化、可执行、可回归 | postmortem、action items、owners | 是 | 是 | 否 | 只有感想，没有证据、修复项或 owner | Moderate |

这个维度表的设计依据是：acceptance criteria 应该是 clear / concise / testable 的完成条件；UAT 必须回到 future users 与 user requirements；PRR/checklist 应针对具体服务和风险；postmortem 应 factual、blameless、要 review；privacy/governance 需要 minimization、deletion、一旦 Git history 含敏感信息会有高恢复成本；而 memory benchmark 则提示 Mnemosyne 必须专门检查 knowledge updates、abstention、conflict handling、action-coupled continuity。citeturn10view13turn10view12turn22view0turn10view9turn10view10turn10view15turn17view2turn12view2turn12view8turn12view5

## 判定架构 评分卡 与证据要求

Mnemosyne v0.1 最合适的评审拆分是：**deterministic checklist 负责边界与证据完整性；LLM-as-judge 只负责有限的质量判断；user confirmation 负责最终“是否对真实需求有用”与“是否接受风险/解释”的部分**。这个拆分不是偏好问题，而是可靠性问题：LLM-as-judge 的确有规模化、低成本、可一致运行的优势，但研究已经证明它会受到 position bias、自偏好 bias、随机种子与可靠性度量不足的影响，因此不能成为唯一评审者。特别是会影响结果的“有无批准”“是否写入 target”“是否使用未授权 source”“是否把 synthetic 说成 real”这类问题，必须使用 deterministic evidence；“是否真正解决了我的需求”则必须回到用户或未来使用者。citeturn16view0turn10view7turn14view5turn15view1

一个 practical split 可以这样落地。**Deterministic checks**：manifest 是否存在、审批是否存在、authority/source map 是否自洽、evidence manifest 是否区分 synthetic/real、ingest ledger 是否标出 originals/derived/redacted、target repo 是否零写入、truth source 是否声明、conflict entries 是否有 superseded 标记、delivery package 是否具备 inventory/traceability/limitations。**LLM-as-judge**：memory schema fit、handoff package 可读性、delivery package 对需求的覆盖度、postmortem 是否可执行、assumption discipline 是否清晰。**User confirmation**：target selection 是否符合其真实意图、最终 package 是否减少其恢复成本、是否接受该 package 可作为下一步人工或半人工行动基础、是否同意任何 target-specific lesson 仅停留在候选层。其本质上是把 acceptance testing、PRR、privacy governance 与 LLM reliability findings 组合到一个三方判定结构里。citeturn10view12turn22view0turn10view16turn17view4turn15view1

下面给出 **Scorecard v0.1**。它采用 **100 分 + critical blockers 覆盖** 的方式：先判 blocker，再算分。因为如果前置边界本身就不合法，分数没有意义。

```yaml
critical_blockers:
  - target_not_selected
  - authority_missing
  - no_target_write_not_confirmed
  - unsafe_material_ingested
  - target_repository_written_without_approval
  - synthetic_evidence_reported_as_real_dry_run
  - target_workspace_treated_as_execution_source
  - target_runtime_truth_source_invented
  - user_originals_stored_unsafely
  - missing_run_manifest_approval
```

| 评分维度 | 权重 | 说明 |
|---|---:|---|
| context recovery | 15 | 首次会话后续会话能否恢复关键状态、打开问题、决策来源 |
| authority/source map | 15 | authority、source map、truth source、conflict hierarchy 是否清晰 |
| input safety | 20 | safe input、storage policy、redaction、external pointer、no-target-write |
| memory design fit | 15 | 记忆 schema 是否匹配目标任务，是否支持更新、冲突、待确认项 |
| handoff/delivery usability | 15 | handoff 与 delivery package 是否让未来使用者可继续工作 |
| evidence/provenance | 10 | 证据可追踪、synthetic/real 分开、artifact 与 claim 可映射 |
| assumption discipline | 5 | 对未知、缺失、冲突信息是否 abstain/标注/升请确认 |
| postmortem/actionability | 5 | 复盘是否能转为 repair 与 regression，而不污染执行源 |

**判定语义**建议如下：

```yaml
dry_run_result_verdict:
  PASS: >
    无 critical blocker；总分 >= 90；所有 Critical/Major 维度均通过最低门槛；
    用户确认该 dry-run 对真实 target 需求“有用且边界被遵守”。
    PASS 不等于 production-ready，不等于 target repository write approved，
    不等于 global Mnemosyne rule update approved。
  PASS_WITH_WARNINGS: >
    无 critical blocker；总分 75-89；核心目标达到，但存在中等级修复项，
    不影响“这是一次真实 dry-run”的成立。
  REPAIR_RECOMMENDED: >
    无 critical blocker；总分 60-74，或存在一个以上 Major 缺陷；
    结果可学习，但不应作为重复执行模板直接复用。
  FAIL: >
    已完成足够多的运行以形成评估，但核心能力未达到目标，
    或产生了影响可用性的重大错误；总分 < 60。
  BLOCKED: >
    运行前或运行中出现 blocker，导致本次不能被合法地称为 real target-project dry-run，
    或不能继续评估。
```

这些 verdict 之所以要与 score 解耦，是因为 benchmark 与现实治理风险的性质不同。LongMemEval、MemoryArena 与 STALE 都表明，**高 recall 或高表面完成度不能替代对更新、行动、冲突、防过时前提的评估**；而 PRR / UAT / privacy governance 又说明，即便功能上“看起来差不多可用”，如果 readiness gate 或 data boundary 没过，也不应放行。citeturn14view1turn12view8turn12view2turn22view0turn10view12turn10view15

**最小证据包**建议至少包含以下项目：已批准的 run manifest；target selection 记录；authority/source map；truth-source declaration；ingest ledger 与 materials safety classification；redaction manifest；external pointer safety note；no-target-write 证明；memory schema 与 retrieval 样例；handoff package；delivery package inventory；assumption/conflict log；user confirmation 记录；postmortem；以及 regression candidate list。没有这些材料，dry-run 最多是一场演示，不能称为“可审计验证”。这一点符合 acceptance criteria 的 clear/testable 原则，也符合 Google SRE 对 checklist、training、reviewed postmortem、continuous improvement artifacts 的要求。citeturn10view13turn22view0turn10view10

## 复盘模板 与回归记录模式

第一次真实 dry-run 最需要避免的一个误区，是把复盘写成“这次感觉不错/不好”的叙事记录。Google SRE 明确强调 postmortem 应 factual、避免 blame，且**未 review 的 postmortem 几乎等于不存在**；Mnemosyne 则还需要额外防止“target-specific lesson 直接污染 execution source”。因此，postmortem 模板必须让三件事同时可见：**发生了什么、为什么会这样、哪些 lessons 只属于该 target、哪些最多只能作为 global candidate**。citeturn10view9turn10view10

```yaml
first_target_dry_run_postmortem:
  dry_run_id:
  target_project_id:
  run_kind: real_target_project
  target_repository_write_performed: false
  target_materials_ingested:
  materials_safety_status:
  verdict:
  score:
  critical_blockers:
  what_worked:
  what_failed:
  unsupported_assumptions_found:
  stale_context_found:
  authority_conflicts_found:
  user_input_storage_issues:
  handoff_continuity_issues:
  delivery_package_issues:
  target_specific_lessons:
  mnemosyne_global_lesson_candidates:
  required_repairs:
  user_decisions_needed:
  evidence_paths:
```

为了把复盘转成真正可复用的 regression asset，而不把这一次 target 的特殊性误判成通用规律，建议所有“lesson”都先进入 **regression test candidate** 层，而不是 execution source。下面的 schema 把 source event、expected recovery、forbidden claims、三类检查方式和后续任务全部显式化，便于后续把失败模式转成可回放测试。这个做法与 requirements traceability / change management 的精神一致：每个“为什么要改”都必须追溯到具体事件、具体证据、具体验证方式。citeturn10view14turn9search7

```yaml
mnemosyne_regression_test_record:
  test_id:
  source_event:
  target_scope:
  model_or_tool:
  repository_ref:
  input_package:
  expected_recovery:
  forbidden_claims:
  deterministic_checks:
  llm_judge_checks:
  user_confirmation_checks:
  result:
  score:
  evidence:
  failure_class:
  follow_up_task:
```

在 v0.1 中，我建议再加一个极简的 **postmortem minimum**：每次 real dry-run 必须至少产出一条 `required_repairs` 与一条 `follow_up_task`；否则这次 dry-run 即便有结果，也没有形成可积累的工程学习。Google SRE 的 continuous improvement 与 reviewed postmortem 逻辑都说明，**没有被转成行动项的复盘，学习价值会快速流失**。citeturn10view10turn22view0

## 与现有 memory continuity agent benchmarks 的对比

现有 benchmarks 能提供重要启发，但**没有一个可以直接替 Mnemosyne 做裁决**。LoCoMo 的价值在于它把 very long-term conversation 变成可测的 QA / summarization / multimodal generation benchmark，并明确暴露 temporal / causal understanding 的困难；但它更偏“长时会话中的记忆与理解”，不是 authority-bound 的工程 dry-run。citeturn10view0turn12view6

LongMemEval 更接近 Mnemosyne 需要的长期助手情境，因为它把长期记忆拆成 information extraction、multi-session reasoning、temporal reasoning、knowledge updates、abstention 五项，并报告商业聊天助手与长上下文模型在 sustained interactions 中出现约 30% accuracy drop；这直接支持 Mnemosyne 把**知识更新、时间感知、abstention**列为一等公民维度，而不是只评检索命中率。citeturn10view1turn14view1

MemoryAgentBench 与 MemBench 把问题继续向“agent memory”推进。前者强调 accurate retrieval、test-time learning、long-range understanding、conflict resolution 四项，后者强调 factual memory 与 reflective memory、participation 与 observation 两种场景，以及 effectiveness / efficiency / capacity 的多指标评估。这两者对 Mnemosyne 的关键启发是：**记忆系统不只要答对，还要更新得对、保留得对、丢弃得对、写入/读取成本也要可接受**。因此 Mnemosyne 的 dry-run scorecard 里必须保留 `memory design fit` 与 `evidence/provenance` 两个独立维度，而不能只看最终回答质量。citeturn20search6turn14view2

MemoryArena、STALE、EMemBench 与 ImplicitMemBench 提供的启发更直接。MemoryArena 说明“memorization and action are tightly coupled”，并显示在 LoCoMo 这类 benchmark 上接近饱和的系统在 interdependent multi-session tasks 里仍然会很差；STALE 则精准对应 Mnemosyne 的 stale/conflicting context handling 维度，指出最好的被测模型总体也仅 55.2%，而且会接受用户问题里隐含的过时状态；EMemBench 通过从 agent 自己的 trajectory 生成问题并提供可验证 ground truth，提醒 Mnemosyne 要尽量基于**运行轨迹证据**而不是事后美化摘要；ImplicitMemBench 则说明“真正好的记忆”还包括自动化行为适应，而不仅是显式回忆。综合起来，这些 benchmark 支持一个结论：**Mnemosyne 的 first real dry-run 不应被设计成“回答题目”，而应被设计成“在真实边界内恢复状态、更新状态、保持状态、并支持下一步行动”**。citeturn12view8turn12view2turn18search0turn18search1

也正因为如此，Mnemosyne 需要明确避免一个常见误判：**把 delivery artifact 的表面质量当作真实项目成功**。漂亮的总结、整洁的 handoff、结构化的 markdown，都只能说明“表述良好”；它们不能自动说明 authority 边界正确、truth source 正确、记忆更新正确、冲突处理正确、对未知足够克制、或未来使用者真的能接着工作。LLM-as-judge 研究对 bias 和 reliability 的警告，使这一点更重要：若让模型直接评“这个包看起来是否优秀”，它很容易偏好自己熟悉的风格或被位置和措辞影响。Mnemosyne 因此应坚持 **artifact-blind evidence review**：先审 provenance、traceability、boundary compliance，再审 package quality，最后才让用户确认 usefulness。citeturn14view5turn10view7turn15view1

## 结果回流方式 建议分层 证据表 与已知限制

要把 dry-run 结果转化为 Mnemosyne 的自我改进，但又不污染 execution source，最稳妥的路由是四层：**run artifact layer → postmortem layer → regression candidate layer → execution-source candidate layer**。第一次真实 dry-run 的所有 lessons 先停留在前两层；只有当某个 lesson 在多个 target、多个回归场景下重复出现，并且不依赖单一 target 的特殊约束时，才能升级到 execution-source candidate。这个分层与 ADR 的“记录 context and consequences”、PRR 的“review readiness before ownership transfer”、以及 requirements traceability 的“变化必须有可追溯理由”是一致的。citeturn10view11turn22view0turn10view14

按你要求的 bucket，我给出的 **Integration recommendations** 如下：

| bucket | 建议 |
|---|---|
| use_before_first_real_target_dry_run | 冻结 object model；建立 critical blockers；强制 run manifest approval；建立 evidence manifest；准备 authority/source map 模板；准备 no-target-write proof 模板；准备 ingest ledger 与 redaction manifest；准备 postmortem 与 regression schema；定义用户确认问题集 |
| add_to_non_execution_source_support_instruments | evaluator rubric；artifact namespace 规范；synthetic/real 证据分层；handoff 恢复演练脚本；assumption/conflict log 模板；delivery package inventory 模板 |
| candidate_for_execution_source_later | 多 target 复验后仍然成立的 truth-source conflict policy；经多次验证有效的 memory schema primitives；重复出现的 stale-context remediation pattern |
| defer_until_after_first_real_target | 自动化评分、批量 judge ensemble、更细粒度 latency/cost 统计、跨项目 lesson taxonomy、持续 benchmark 对齐 |
| do_not_do_in_v0.1 | 不要自动写 target repository；不要把一次 PASS 升级为 global rule；不要把 synthetic smoke test 结果放进 real evidence；不要把 private repo 视为可安全存放用户原文；不要让 LLM-as-judge 独任最终裁决 |

为了方便审阅，下面给出本报告最关键的 **evidence table**。它区分“研究事实”和“本报告如何使用该事实”。

| 来源 | 关键发现 | 在本框架中的用途 |
|---|---|---|
| LoCoMo citeturn10view0turn12view6 | 长时会话、长距时间/因果理解仍困难，模型显著落后于人类 | 支持把 temporal/causal continuity 设为核心维度 |
| LongMemEval citeturn10view1turn14view1 | 五项长期记忆能力；持续交互中约 30% accuracy drop | 支持知识更新、abstention、multi-session reasoning 单独评分 |
| MemoryAgentBench citeturn20search6 | retrieval、test-time learning、long-range understanding、conflict resolution 四能力 | 支持把冲突处理与更新能力纳入 dry-run |
| MemBench citeturn14view2 | factual/reflective memory，多指标评 effectiveness/efficiency/capacity | 支持 memory schema fit 与成本/容量意识 |
| MemoryArena citeturn12view8 | “记住”与“行动”在真实多阶段任务中耦合；旧 benchmark 高分不等于 agentic success | 支持 artifact 评分不得替代 action-level continuity 验证 |
| STALE citeturn12view2 | 过时前提、隐式冲突、状态更新是突出失败点；最佳模型总体仅 55.2% | 支持 stale/conflicting context handling 设为 Major 维度 |
| EMemBench citeturn18search0 | 基于 agent 自身轨迹生成题目并提供可验证 ground truth | 支持 Mnemosyne 采用 trajectory-grounded evidence |
| ImplicitMemBench citeturn18search1 | 好记忆还包含自动化行为适应，不只是显式回忆 | 支持把“handoff 后行动恢复”视为评测对象 |
| LLM-as-a-Judge survey citeturn16view0turn16view2 | judge 有优势，但 reliability 需要 careful design and standardization | 支持 judge 只能是辅助裁判 |
| Position bias / self-preference bias / reliability work citeturn10view7turn14view5turn15view1 | LLM judge 受位置偏差、自偏好与随机性影响 | 支持 deterministic + user confirmation 双重制衡 |
| ISTQB UAT / acceptance criteria citeturn10view12turn10view13 | future users、simulated environment、clear pass/fail conditions | 支持把 delivery package 评估放在 no-target-write 条件下完成 |
| Google SRE PRR / postmortem citeturn22view0turn10view9turn10view10 | readiness、checklists、training、continuous improvement、reviewed factual postmortems | 支持 blocker gates、复盘动作化、PASS 不等于授权升级 |
| NIST Privacy / GitHub sensitive-data docs citeturn10view15turn10view16turn17view2turn17view4 | 数据最小化、删除、日志也要 minimization；Git history 一旦含敏感数据清除代价高 | 支持 safe input / user originals / no-target-write 属于 blocker |

**Mnemosyne v0.1 recommendations** 可以概括为一句话：把第一次真实 dry-run 当成一次**受约束的 acceptance-and-governance validation**，不是当成早期“产品成功秀”。在工程上，它应该首先证明边界与证据，再证明 usefulness；在组织上，它应该先沉淀 repair 与 regression，再谈 global rule；在权限上，它应该明确 **PASS 不是写入许可，不是 production-ready，不是全局规则升级许可**。这一点与 readiness review、UAT、privacy governance 与最新 memory benchmarks 的共同方向是一致的。citeturn22view0turn10view12turn10view15turn12view8

**Deferred v0.2+ recommendations** 则应包括：多 judge family 交叉评分、位置交换与盲审策略、跨 target 的 lesson clustering、成本/延迟/记忆容量随时间曲线、以及更程序化的 regression pack。但这些都应建立在至少一次真实 dry-run 已经证明“边界治理和证据规则本身能运转”的基础上，而不是反过来用自动化掩盖定义不清的问题。citeturn16view0turn15view1turn22view0

最后说明 **已知不确定性与限制**。其一，2025–2026 的不少记忆 benchmark 仍是 preprint 或快速演化中的工作，虽然它们已足够说明 failure modes，但不应把具体leaderboard数值当成稳定事实。其二，现有 benchmark 大多不覆盖 authority boundary、no-target-write、redaction manifest、Git-history exposure 这类工程治理问题，所以本报告在这些部分进行了**跨领域综合推断**，结合了 UAT、PRR、privacy 与 source-control 风险文档。其三，没有任何外部 benchmark 能替 Mnemosyne 决定“这个 target 值不值得继续投入”；这仍然需要用户确认与具体项目价值判断。换言之，本框架是一个**evidence-backed engineering evaluation framework**，不是可自动替代人类裁决的标准答案。citeturn16view0turn15view1turn10view15turn17view4turn22view0