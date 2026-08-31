# MNE-DR-022 / FABLE5-REDESIGN-001-RQ3 · 需求生命周期与状态演化管理

研究截止日：**2026-08-31（America/Los_Angeles）**。本报告仅使用公开网络材料，未访问任何私有仓库或连接器。证据按【论文实证】【机构/厂商文档】【厂商案例】【社区经验】区分；其中厂商案例和社区经验只作为实践信号，不等同于独立因果证据。对公开资料中未找到可靠先例或数据的项目明确标记为 **UNKNOWN**。

**结论先行。** 到 2026 年，AI 辅助软件开发已经形成相当清晰的“意图/需求 → spec → plan/design → tasks → implementation → verification/convergence”工件链；GitHub Spec Kit、Kiro、OpenSpec 都把 Markdown 规格变成 agent 的工作上下文，而不再只把规格当交付前文档。与此同时，传统需求工程中的 baseline、change control、双向 traceability、决策理由、supersession 等机制仍比多数新一代 agent SDD 工具更成熟。最值得本任务关注的三个公开先例是：**OpenSpec 的“current source of truth + change delta + archive”**、**Kiro/Spec Kit 的“机器发现矛盾但不替用户决定”**、以及 **LLM eval 工具链的“模型/架构变化触发 regression/backtest”**。反过来，公开资料中尚未发现成熟通用工具把“新模型出现 → 自动找回因能力不足而 deferred 的旧需求 → 重评 → owner 再批准”做成完整的一等生命周期，故这一点为 **UNKNOWN**。citeturn16view0turn16view5turn20view2turn19view1

## 规格驱动开发现状

**对应 Q1。**

2025–2026 的 spec-driven development 已从“先写规格再提示模型”演化成**多工件、可检查、可循环的 agent orchestration**。GitHub Spec Kit 当前核心流程是 `Spec → Plan → Tasks → Implement`，同时加入 `clarify`、跨工件 `analyze`、requirements checklist，以及实施后将代码库重新与 spec/plan/tasks 对齐的 `converge`；官方说明各阶段产生 Markdown 工件供下一阶段作为结构化上下文。当前文档还列出 38 个 agent 集成和 157 个社区扩展。citeturn16view0turn16view2

| 实践 | 工件化方式 | spec 与代码/agent 同步机制 | 公开采用信号 | 证据判断 |
|---|---|---|---|---|
| **GitHub Spec Kit** | constitution → spec → plan → tasks → implementation；另有 clarify/analyze/checklist | `converge` 检查实现相对 spec/plan/tasks 的剩余差距并追加任务；`analyze` 在实现前做跨工件一致性与覆盖分析 | 官方文档截至 2026-08-21 显示 38 integrations、157 extensions；GitHub 项目公开规模约 130K+ stars、270+ contributors | 【厂商文档·2026】强实践证据；**真实企业部署率 UNKNOWN** citeturn16view0turn16view1turn1view1 |
| **Kiro** | `requirements.md → design.md → tasks.md → implementation`；requirements 使用 user story + EARS acceptance criteria | 用户改 requirements 后可让 Kiro 更新 design/tasks；官方还明确称开发者可让 Kiro 根据代码更新 spec，或修改 spec 后刷新 tasks | AWS/Kiro 有大量公开教程与案例，但未发现可信的活跃项目/组织部署总数 | 【厂商文档·2025–2026】；采用率 **UNKNOWN** citeturn17view1turn17view2 |
| **OpenSpec** | proposal → delta specs → design → tasks → implement | 主 `specs/` 是当前 source of truth；变更在独立目录；完成时把 ADDED/MODIFIED/REMOVED delta 合并进 current specs 并归档完整上下文 | GitHub 项目公开约 66.7K stars，属于关注度代理而非部署统计 | 【开源项目文档·2026】强 current-state/change-set 先例 citeturn16view5turn16view6turn16view7turn12view0 |

Spec Kit 的跨工件检查尤其值得区分于普通“让 agent 再读一遍”：其 `analyze` 被定义为**严格只读**，检查 spec、plan、tasks 中的 inconsistency、duplication、ambiguity、underspecification，并规定任何后续修改都要用户显式批准。这意味着 spec 与执行工件的一致性已经开始被当作独立质量门，而不是隐含在一次生成中。citeturn16view3

Kiro 的同步策略更接近双向维护：2025 年官方介绍明确说，开发者既可写代码后要求 Kiro 更新 specs，也可直接修改 specs 并刷新 tasks；2026 年 Requirements-First 文档则规定，修改 `requirements.md` 后可以重新 refine `design.md`，再同步 tasks。也就是说，公开产品实践已经不再假设“spec 一旦生成就冻结”。citeturn17view1turn17view2

另一方面，**审批门并不是行业统一强制**。Kiro 的标准 Requirements-First 流程要求人在 requirements 和 design 阶段 review/confirm，但 2026-08-04 更新的 Quick Spec 可以在一轮澄清后连续生成 requirements/design/tasks，刻意跳过中间 approval gates；Kiro 自己建议高风险、陌生或质量敏感工作仍使用显式 gate。这个先例说明，“owner approval”有明确价值，但“每类需求都必须同样重的审批流程”并非现成行业共识。citeturn17view2turn17view3

公开成功经验里，AWS 2026-02 的药物发现 agent 案例报告称其团队在三周项目中使用 requirements/design/tasks，且架构师在执行前审阅并纠正 Kiro 对 prompt 的解释；其价值主张正是把 planning 与 execution 分离，在 agent 真正改代码前暴露误解。但这是**厂商案例**，不能据此推断普遍生产率提升。citeturn17view4

公开失败经验同样存在。Spec Kit 的 2025 年 GitHub Discussion 中，有实际使用者报告为复杂任务花大量时间纠正 AI 生成的规格，并认为过多文本反而造成上下文噪声；同一讨论中也有人表示经过模板和流程调优后效果明显改善。因此目前更可靠的结论不是“SDD 必然有效”或“必然无效”，而是其收益高度依赖任务复杂度、规格质量、上下文预算和流程调校。这些都是**社区经验**，没有控制实验效力。citeturn16view4turn14view3

学术层面的证据也要求保守。2025 年一项 LLM-for-Requirements-Engineering 系统综述覆盖 74 项 2023–2024 的 primary studies，发现研究大量集中在需求获取、验证和规格处理，但通常仍在受控环境评估，在真实工业流程和复杂 workflow 中的整合有限。2026-08-21 的跨任务实证预印本进一步报告，不同模型在需求分类、specification generation、traceability identification/explanation 上表现明显依任务而异，没有单一模型稳定占优。它们支持“LLM 可参与 RE”，却还不能证明当前某一 SDD 框架具有普遍因果优势。citeturn20view1turn13academia11turn20view0

因此，对 Q1 的证据分级结论是：

**工件链做法：已成熟到可实施。**  
**公开关注度：高且快速增长。**  
**真实组织采用率：UNKNOWN。**  
**独立、可泛化的成功率/生产率提升：UNKNOWN。**  
**已公开失败模式：规格膨胀、LLM 对需求细节误解、工件间漂移、过度流程化。** citeturn16view0turn16view4turn20view1

## 需求演化与当前态管理

**对应 Q2。**

这里最重要的发现是：**“历史怎么保存”与“当前哪些需求有效”是两个不同问题。** 公开成熟方法通常不会要求消费方每次扫描版本控制历史来推断 current state，而是同时维护一个明确 baseline/current view，再把变化保存在 change set、delta、archive 或 supersession graph 中。NASA 的 requirements management 明确要求管理已建立的 requirement baselines、在整个生命周期管理其变更、保持双向 traceability，并记录正式的 change initiation、assessment、review、approval 和 disposition。citeturn15view4

OpenSpec 是当前 agent-SDD 领域最清楚的公开实现之一。它明确把：

`openspec/specs/` = **系统当前行为的 source of truth**

与

`openspec/changes/` = **尚未进入当前态的 proposed modifications**

分开。一个 change 可以包含 proposal、design、tasks 和 delta specs；归档时，delta 才真正进入 current specs，同时原 change 文件夹完整移入带日期的 archive。citeturn16view5turn16view7

其 delta 还把需求演化分类为 `ADDED`、`MODIFIED`、`REMOVED`。修改项可以直接注明旧值；删除项从 current spec 中移除，但原变化原因仍存在于 archive。这实际上形成了“**materialized current state + appendable/auditable change history**”的组合，而不是把历史版本本身当成当前状态表示。citeturn16view6

显式 supersession 方面，需求工具之外已有非常成熟的先例。Martin Fowler 2026 年总结的 ADR 模式使用 `proposed → accepted → superseded` 状态；被接受的 ADR 不应原地改写，而是在新决定出现时被新 ADR supersede，并链接到替代它的记录，从而保存“什么决定在什么时间有效”。IETF RFC 系列更严格：已发布 RFC 原则上保持不可变，新 RFC 可显式 `updates` 或 `obsoletes` 一个或多个旧 RFC；Historic 状态还用于标记已被更近期规范取代的规格。citeturn15view7turn20view4

这些先例可以对应到本课题关心的状态语义：

| 所需语义 | 找到的公开先例 | 判断 |
|---|---|---|
| **valid/current** | NASA requirement baseline；OpenSpec current `specs/`；ADR `accepted` | 已有成熟先例 citeturn15view4turn16view5turn15view7 |
| **superseded** | ADR `superseded` + superseding ADR link；RFC `updates/obsoletes` | 已有强先例，而且强调“保留旧记录，不原地抹去” citeturn15view7turn20view4 |
| **deleted/withdrawn from current** | OpenSpec `REMOVED`：从 current spec 移除，同时 archive 保留变更上下文 | 已有“逻辑退出当前态”的先例；不等价于不可恢复硬删除 citeturn16view6turn16view7 |
| **deferred** | 通用 issue/backlog 系统存在 not-planned/reopen 类生命周期，但在本次调查的主要 requirement/spec 工具里未发现统一的 requirement-level `deferred` 标准 | **UNKNOWN：无行业统一枚举** |
| **冲突中/待裁决** | Kiro conflict finding；Spec Kit read-only analyze report | 有“临时非可执行状态”的流程先例，但未发现统一状态名 citeturn20view2turn16view3 |

NASA 还明确要求 stakeholder expectations、technical requirements、derived requirements 和 verification/validation 之间的双向 traceability，并要求 baseline 包含 decision rationale、assumptions 等上下文；配置管理则要求标识配置项及其 revisions/versions，并维护 change action 的 disposition。换言之，传统 RE 并不仅保存“版本”，还保存**语义关系与处置结果**。citeturn15view4

因此，公开证据并不支持把 Git commit history 本身视为完整的 requirement lifecycle model。Git 很适合做不可抵赖历史和人工 review，但 current-validity、supersession、deferred reason、requirement-to-test trace 等语义若只存在于 commit diff 中，消费 agent 必须重新推理这些事实。OpenSpec、NASA、ADR、RFC 的共同方向恰好相反：**历史保留，同时把 current state 和 supersession 关系显式化。**这是基于上述资料的综合推论。citeturn16view5turn15view4turn15view7turn20view4

本次检索未找到一个被广泛接受、跨工具统一使用的 `valid / superseded / deleted / deferred` 四值 requirement 状态标准，因此这一精确枚举的行业标准性为 **UNKNOWN**。

## 重评触发机制

**对应 Q3。**

“模型升级或环境变化 → 触发重审”在 **evaluation / regression testing** 层已有非常明确的公开先例；在“deferred requirement 自动复活”层则没有找到同样成熟的产品化先例。

OpenAI 当前 evaluation best-practices 文档要求把 evaluation 作为持续过程，并明确建议 **continuous evaluation 在 every change 上运行**，同时从生产数据和用户反馈中不断扩充 eval set。OpenAI 2024 的 Evals cookbook 更直接把 continuous model upgrades 列为使用 eval 的理由：用一套针对自己 use case 的标准化测试理解新模型是否更适合，并把 eval 纳入 CI/CD。citeturn14view6turn14view7

LangSmith 现在把这件事写得更具体：regression tests 用于比较应用版本，通常在预计会影响用户体验的变更发生时运行，文档明确举了“**model or architecture changes**”；backtesting 则建议当新模型发布时，把新模型跑在近期真实生产 traces 上，与实际生产结果比较。citeturn19view1

Anthropic 的当前 model-selection 文档也规定，在升级或更换模型前应创建特定于 use case 的 benchmark、使用真实 prompts/data 测试、比较 accuracy、quality 和 edge cases，再权衡性能与成本。因此“model upgrade 不是直接替换，而应先重新验证既有行为假设”已经是主要模型厂商公开倡导的工程做法。citeturn19view0

可以把现有公开实践抽象成：

**模型/架构/环境发生变化 → 自动或半自动运行已有 eval/backtest → 识别 regression 与 improvement → 人工判断是否采用新版本。** citeturn14view6turn19view1turn19view2

但是本任务要求的下一步更特殊：

**新模型出现 → 找出过去因“模型能力不够”而 deferred 的需求 → 自动/半自动重新评估它们能否实现。**

在本次公开检索中，未发现 GitHub Spec Kit、Kiro、OpenSpec、OpenAI Evals、LangSmith 或传统 RE 公开文档把这一过程做成一套现成的一等工作流。因此：

> **“模型升级自动复活 deferred requirements”的成熟公开先例：UNKNOWN。**

最接近的公开构件是两套机制的组合：一套是带原因和历史的 backlog/change lifecycle，另一套是 model-change regression/backtesting。因而一个**证据支持的研究推导**是：deferred 项不应因新模型上线直接变成 valid，而是先进入 `review-needed` 类重审队列；触发结果需要由此前失败的 acceptance/eval 在新环境中重新执行，然后再由 owner 决定是否恢复执行资格。这里的“队列”和状态名是本研究推导，不是声称某一现有产品已经这样实现。支撑这一推导的公开机制是 model-change eval、baseline comparison 和 human review。citeturn19view1turn19view2turn14view6

若要使“挂起需求”可被可靠唤醒，至少必须能区分**为什么挂起**。例如“当前模型能力不足”与“owner 暂时不想要”在模型升级后应得到不同处理；否则单纯扫描所有 deferred 项会制造大量无意义 review。公开工具没有给出通用字段标准，因此具体 `defer_reason / revisit_trigger` schema 属于 Q7 的候选补法，而非已存在行业标准。

## 从模糊意图到验收标准

**对应 Q4。**

这方面公开方法已经相当成熟，且 2025–2026 的 agent 工具正把传统 requirements engineering 技法直接嵌入生成流程。

NASA 的系统工程过程是较经典的分层先例：先 elicitate stakeholder expectations，将 agreed-to expectations 建立 baseline；随后 technical requirements definition 把这些基线化期望转成**唯一、定量、可测量**的 technical requirements。要求本身要清晰、可实现、尽量只有一个解释，并要求整个集合无冲突；产品 verification/acceptance 又需要能回链到相关需求。citeturn15view4turn15view5

Kiro 把这一传统逻辑压缩成了 agent workflow。一个诸如“增加产品评论系统”的普通 prompt，会被展开成 user stories，并为每个 story 生成 EARS 格式 acceptance criteria，覆盖正常和 edge cases；随后用户 review、迭代、补场景，确认 requirements 后才进入 design。citeturn17view1turn17view2

Kiro 2026 年的 requirement analysis 又展示了更强的“模糊 → 可验收”转换：它明确认为第一版需求通常过于抽象，先 refinement 成能够指出 event、input、state、output 的 testable、solution-free criteria，再进行形式化和 consistency/completeness 分析。例如“authenticate users”本身不可直接验收，而应落到输入条件及可观察结果。citeturn17view0turn20view2

OpenSpec 同样把 requirement 与 scenario 绑定。其 current spec 示例使用 `SHALL/MUST` 描述行为，并用 `GIVEN / WHEN / THEN` 场景定义有效凭证、错误凭证、超时等可测试情况。这说明在 agent SDD 生态里，“requirement 不是一段散文，而应伴随 observable scenarios”正在成为共同模式。citeturn16view5

由这些资料可以得到一个较稳固的公开实践链：

**人的不完整意图 → 澄清/elicitation → 结构化 requirement → observable acceptance scenario → 人确认 baseline → design/tasks → test/eval。** citeturn15view4turn17view2turn16view5

但本课题特别要求的 **“原话 vs 解释 vs owner 批准版”三层严格分离**需要进一步区分。

NASA 明确分离 stakeholder expectations 与 baselined technical requirements；Kiro 明确分离初始 prompt 与生成的 requirements，并要求用户确认后再进入 design；OpenSpec 又分离 proposal/change 与 current spec。这些都支持“不应把第一次机器解释直接当执行真相”。citeturn15view4turn17view2turn16view5

不过，在本次调查的主流公开 agent-SDD 工具中，未找到明确承诺：

> “原始用户 utterance 逐字、不可变地保留为一级 requirement provenance；所有机器解释均独立成新实体；owner-approved requirement 又是第三个独立实体，并保持逐项 lineage。”

所以，**这一精确三层模型的主流产品先例为 UNKNOWN**。这并不构成对委托方 raw 层设计的否定；只是外部证据最多支持“分离 elicited intent 与 approved specification”，不能把它夸大成“业界已经采用同样的 verbatim 三层架构”。

近期 LLM-for-RE 实证又提供了一个重要限制条件。2026-08-21 的跨任务研究同时考察 feedback-driven requirements classification、specification generation 和真实项目 traceability，报告模型能力明显 task-dependent，且不存在一个模型在所有任务上持续最优。因此，把 AI 生成的 interpretation 作为候选、而不是未经 owner/eval 检查就升级为权威 requirement，与目前有限但最新的实证结果是一致的。citeturn13academia11turn20view0

## 矛盾呈现与人裁决

**对应 Q5。**

这个问题有非常明确的肯定答案：**已经有工具把“机器发现矛盾，但不替人决定真正意图”做成一等流程。**

Kiro 2026-05 的 deep spec analysis 是目前最直接的公开先例。其文档明确指出，形式化/神经符号分析可以发现一个 requirement 存在多个合理解释，却**不能决定哪一个符合用户原始意图**；系统应把这种语义分歧转化成少量具体问题让用户选择。citeturn20view2

它会产生至少五类 finding，其中 conflict 的定义是“两个规则在同一情形下同时触发，却要求不兼容结果”；工具随后要求用户决定哪一条胜出，或缩小其中一条的适用条件。文档给出的实际例子是：一条 acceptance criterion 要“remove the record”，另一条却要求 soft deletion 保留记录，两条单独看似合理，放在一起却互相冲突。系统把 hard delete 与 retained-but-hidden 两种含义并列，让用户决定。citeturn20view2

Spec Kit 的处理方式更接近“只呈报、不擅改”。其 `analyze` command 明确标为 **STRICTLY READ-ONLY**，负责列出 inconsistencies、duplications、ambiguities 和 underspecified items；如需修改，必须另行提出 remediation plan，并取得用户明确批准后才执行编辑。citeturn16view3

这两者共同证明：

**“发现冲突 ≠ 自动调和冲突”已经是公开的一等 agent workflow。** citeturn20view2turn16view3

至于“裁决记录”和“可撤销性”，ADR 模式提供了很好但非 requirements-specific 的先例。Fowler 建议记录 serious alternatives 及其 pros/cons，同时 accepted ADR 不原地重写；后来反悔时，以新 ADR `supersede` 旧 ADR，从而保留过去为什么那样决定、何时生效、又何时被新决定替代。这里的“撤销”不是抹去历史，而是**新决策取代旧决策**。citeturn15view7

OpenSpec 的 delta/archiving 则为 review-friendly diff 提供了另一种实现：change 只显示 ADDED/MODIFIED/REMOVED 的差异，reviewer 不需要在完整新旧 spec 中人工寻找变化；archive 后旧 change 的 proposal、design、tasks、delta 仍然存在。citeturn16view6turn16view7

所以各子能力的公开成熟度是：

| 能力 | 结论 |
|---|---|
| 自动发现 requirement contradiction | **有**：Kiro、Spec Kit citeturn20view2turn16view3 |
| 不自动消解、交人裁 | **有，而且是一等流程**：Kiro A/B clarification；Spec Kit read-only report citeturn20view2turn16view3 |
| 并列展示候选解释 | **有**：Kiro concrete alternatives citeturn20view2 |
| review-oriented delta/diff | **有**：OpenSpec delta；LLM 实验领域也普遍有 side-by-side diff citeturn16view6turn19view2 |
| 裁决理由与 alternatives 长期保留 | **有成熟邻域先例**：ADR citeturn15view7 |
| 旧裁决被新裁决显式 supersede | **有成熟邻域先例**：ADR、RFC citeturn15view7turn20view4 |
| 单一现成 requirements 工具同时提供“原文不可变 + 冲突并列 + owner verdict + supersession + 一键撤销” | **UNKNOWN** |

因此，委托方“矛盾并列不调和、交 owner 裁”的方向并不是异端设计；它反而与 2026 年 Kiro 和 Spec Kit 的公开冲突处理原则高度一致。区别只在于委托方还要求长期 provenance 与历史裁决可追踪，这部分更接近 ADR/RFC 式 supersession。

## 反馈回流闭环

**对应 Q6。**

公开实践中已经可以观察到一条完整的反馈闭环，只是它通常跨越 observability、issue tracking、requirements management 和 eval 工具，而不是由单一 SDD 产品全部包办。

在 agent/LLM 系统一侧，LangSmith 当前文档把闭环写成：

**production interaction → online evaluation/monitoring → failing production trace → 加入 evaluation dataset → 创建针对性 evaluator → 离线验证修复 → redeploy。** citeturn17view5turn19view1

这非常贴近本任务“反馈连同材料完整记录”的要求，因为反馈不是只留下“用户不满意”这一句话，而是保留导致问题的 production trace，并把它转成以后所有版本都要面对的 regression case。LangSmith 的 backtesting 还让新模型重新运行历史生产数据，从而使旧反馈具有跨模型的持续验证价值。citeturn19view1

Sentry 提供了更直接的“**反馈 + 触发上下文**”先例。其 User Feedback / Session Replay 文档说明，feedback 可以与相关 event/replay 关联；Replay Details 还说明，在用户提交反馈时，可在 replay timeline 中看到反馈点，并捕获提交前最多约 60 秒的活动。这意味着“反馈本身”与“发生反馈之前用户经历了什么”可以作为同一调查材料。citeturn18search1turn18search12turn18search16

GitHub Issue Forms 展示了较轻量的结构化 intake：表单可强制填写 what happened、产品版本、相关日志等字段，提交后字段内容被保存为普通 Markdown issue body，继续接受评论、标签和后续开发工作关联。这是 bug/摩擦/新想法进入长期项目记录的一种低门槛公开做法。citeturn17view7

传统 requirements management 则负责把这些反馈真正变成 controlled requirement change。NASA 的 requirement-management process 明确把 requirement change requests、technical assessment、verification results 和 validation results作为输入；变化需要经过 formal initiation、assessment、review、approval、disposition，并回写 requirement baseline 和 compliance/traceability 状态。citeturn15view4

Spec Kit 目前也开始补上“问题 → 证据 → 修复验证”的小闭环：其 bundled bug extension 采用 `assess → fix → test`，强调 agent 不应从 bug report 直接跳到 patch，而要保存从 root cause 到 verification 的过程。citeturn16view1

把这些公开机制组合起来，可以得到一条已有充分先例支撑的 lifecycle：

**用户反馈/bug/摩擦/新想法**  
→ 保存原反馈与 trace/replay/log/context  
→ triage 成 issue/change candidate  
→ 必要时形成 requirement change  
→ owner/reviewer 审批  
→ 更新 current requirement  
→ 生成或更新 acceptance test/eval  
→ implementation  
→ regression/eval  
→ production monitoring  
→ 新反馈再次进入闭环。citeturn18search12turn17view7turn15view4turn17view5

本次未找到一个主流 agent-SDD 产品能够开箱即用地把“production feedback + raw context → requirement entity → supersession → owner approval → code → eval → deployment trace”全部串成一个统一对象图。因此，**单产品端到端实现：UNKNOWN**；但各段公开成熟构件均已存在。

## 对照分析

**对应 Q7。**

委托方公开给出的四个现行要点是：①需求原文逐字保存 raw 层；②分析/候选与 owner 批准执行层分离；③变化走 Git 历史＋人审合并；④矛盾并列、不由机器强行调和，交 owner 裁。

**业界已有、而现行公开描述中未明确出现的机制如下。**“未明确”不等于内部一定不存在，只表示本任务书给出的公开要点没有覆盖。

| 业界机制 | 为什么与现行四点不同 | 外部证据 |
|---|---|---|
| **稳定 requirement identity + 显式 supersession edge** | Git 可以保存 diff，但“R17 被 R42 取代”如果没有结构化关系，agent 仍须从历史推断 | ADR 使用 `superseded` + superseding ADR；RFC 显式 updates/obsoletes citeturn15view7turn20view4 |
| **直接可消费的 current-state view** | 历史记录与当前有效集分离；agent 不必每次重放 Git history | OpenSpec `specs/` 是 current source of truth，changes/archive 保存变化 citeturn16view5turn16view7 |
| **双向 requirement traceability** | 不只 source→requirement，还包含 requirement→design/task/test/verification，便于 impact 和 satisfaction 分析 | NASA 要求 bidirectional traceability、compliance matrix；实证研究发现部分 traceability completeness 与较低 defect rate 显著相关 citeturn15view4turn21search3 |
| **deferred 的显式原因与 revisit trigger** | 仅知道“挂起”不足以判断模型升级是否相关 | model-change regression/backtest 已成熟，但 requirement resurrection schema **UNKNOWN** citeturn19view1turn14view7 |
| **production feedback 的 evidence bundle** | feedback 不只是文字，还要能跟 trace/replay/log 一起再现 | LangSmith failing traces→dataset；Sentry feedback→replay；GitHub Issue Forms 可收日志 citeturn17view5turn18search12turn17view7 |
| **裁决 rationale / alternatives / superseding decision** | “owner 选了 A”之外还保存为何选、另有哪些选择、何时被新决定取代 | ADR 是直接先例 citeturn15view7 |
| **机器可算的 lifecycle health invariants/coverage** | Git review 可发现单次 diff 问题，但不自动回答“有多少 current requirements 没有验收/trace/owner decision” | Spec Kit analyze 已做 cross-artifact coverage；NASA 保持 traceability/compliance 状态 citeturn16view3turn15view4 |

**外部证据对现行方案的支持与质疑可以分开看。**

| 现行环节 | 证据判断 | 原因 |
|---|---|---|
| **raw 与解释层分离** | **部分支持** | NASA 明确区分 stakeholder expectations 与后续 measurable technical requirements；Kiro 也区分初始 prompt 与待确认 requirements。但“逐字 raw 永不被解释层替代”的精确主流先例，本课题未找到，故不能用本报告声称已被行业直接验证。citeturn15view4turn17view2 |
| **候选层与 owner-approved 执行层分离** | **强支持** | NASA baseline/change control、Kiro Requirements-First、OpenSpec changes→current 都把 proposed 与 approved/current 分开。citeturn15view4turn17view2turn16view5 |
| **所有变化走 Git＋人审** | **方向支持，但 Git 单独不足** | OpenSpec 使用 repo/history 很合适，但仍另建 current spec、delta、archive；NASA 又要求显式 traceability、change disposition。证据因此支持“Git 做审计底座”，质疑“只靠 Git 历史承载全部生命周期语义”。citeturn16view7turn15view4 |
| **矛盾并列、不自动调和** | **强支持** | Kiro 明确称机器无法知道哪个合理解释符合真实意图；Spec Kit analyze 规定只读、修改需人批准。citeturn20view2turn16view3 |
| **owner gate 应用于所有工作** | **有保留** | Kiro 同时提供标准 review-gated spec 与 Quick Spec，后者对低风险、熟悉任务跳过阶段审批；说明 gate 的价值有证据，但“任何变化都同样重审批”不是统一实践。citeturn17view3 |
| **挂起需求等待以后人工想起来重看** | **证据质疑** | AI 工具已把 model/architecture change 作为 regression/backtest trigger；长期项目若完全依赖人工记忆，会错过能力变化带来的可行性变化。citeturn19view1turn14view6 |

**最小补法候选如下；它们是候选清单，不构成设计裁决或架构选择。**

第一类候选是在现有 requirement 记录上增加非常少的生命周期元数据，例如稳定 `req_id`、`status`、`supersedes/superseded_by`，而不改变 raw 层本身。这样可以把 ADR/RFC 已证明实用的 supersession 语义带入 requirement 层。citeturn15view7turn20view4

第二类候选是在 Git 历史之上生成一个**明确的 current-valid requirement view**，使执行 agent 默认只消费这个视图，同时仍可回链到 raw、候选和历史版本。这对应 OpenSpec 的 current specs/change/archive 分离；它不要求放弃 Git。citeturn16view5turn16view7

第三类候选是给 deferred item 附最小 `defer_reason` 与 `revisit_trigger`，并记录最近一次评估所用 model/environment/eval。新模型或关键环境变化只触发“待重评”，而不自动把需求恢复为有效。该机制是基于 continuous regression/backtesting 的推导；**现成 requirement-resurrection 产品先例仍为 UNKNOWN**。citeturn19view1turn14view7

第四类候选是为 owner-approved requirement 增加至少一条 downstream trace：acceptance criterion/test/eval/task/implementation 中至少一个可验证对象，并允许反向查询。NASA 和 traceability 实证为这一机制提供的外部证据明显强于单纯版本历史。citeturn15view4turn21search3

第五类候选是把冲突裁决保存成独立 decision record：冲突双方引用、owner verdict、rationale、时间、以及后续 superseding decision。这样不会要求修改原始 raw，也不会让 AI 默默“解决掉”矛盾；Kiro 提供 human conflict resolution 先例，ADR 提供长期决策历史先例。citeturn20view2turn15view7

第六类候选是对来自实际使用的 change candidate 保存 `feedback_ref + evidence_ref`，后者可以指向 trace/replay/log/eval case，而不是把所有上下文压成一段摘要。LangSmith、Sentry 和 GitHub Issue Forms 均已有相应构件。citeturn17view5turn18search12turn17view7

综合而言，现行方案的核心方向没有被外部证据推翻；最明显的风险不是 raw/owner/human-review 这些原则，而是**如果 current state、supersession、traceability、deferred trigger 和 feedback evidence 仍只隐含在 Git 文本历史中，agent 消费时会承担本可提前结构化消除的推理负担。**这是本研究基于多类公开先例得到的主要差距判断。citeturn16view5turn15view4turn15view7turn19view1

## 度量候选

**对应 Q8。**

以下给出 8 个生命周期健康度指标。需要特别说明：除“traceability completeness”已有直接学术度量与实证外，其余多数是**依据公开机制推导出的 operational metrics**，而不是声称存在统一行业公式。公开资料也不足以给出跨项目通用的红线阈值，因此统一阈值均为 **UNKNOWN**，应由项目历史基线和风险等级校准。

| 指标候选 | 可操作定义 | 指标解释 | 证据来源 |
|---|---|---|---|
| **双向需求可追溯完整率** | `同时具有上游来源链接和至少一个下游验收/验证/实现链接的 current requirements ÷ current requirements 总数` | 越高越好；可分别拆分 source trace、acceptance trace、implementation trace | NASA 要求双向 traceability；Rempel & Mäder 对 24 个中大型开源项目研究发现，用于多类工程活动的 traceability completeness 与较低 defect rate 有显著关系。【论文实证·2017】 citeturn15view4turn21search3 |
| **过期需求误用率** | `观察期内引用 superseded/removed/non-current requirement 的执行任务、agent run 或变更数 ÷ 所有有 requirement reference 的执行数` | 越低越好，理想方向为 0；直接测“agent 把旧需求当现行需求”的核心故障 | OpenSpec 把 current spec 与 archived/removed change 分开；ADR/RFC 显式 supersession/obsoletion。【工具/标准先例】 citeturn16view5turn16view6turn15view7turn20view4 |
| **矛盾发现时延** | `median(t_detected − t_second_conflicting_requirement_entered)`；也可看 P90/P95 | 越短越好；与“矛盾数量”相比，更能评价流程能否在实现前发现问题 | NASA 明确强调 derived requirement conflicts 应尽早发现；Kiro/Spec Kit 已自动化 consistency/conflict analysis。【机构/厂商文档】 citeturn15view4turn20view2turn16view3 |
| **挂起需求复评及时率** | `触发事件发生后，在规定 review SLA 内完成重评的 deferred requirements ÷ 本期触发重评条件的 deferred requirements` | 越高越好；需要先把“哪些变化构成 trigger”结构化 | OpenAI CE 要求变化后持续评估；LangSmith 明确把 model/architecture changes 与新模型 release 作为 regression/backtest 场景。【厂商文档】 citeturn14view6turn19view1 |
| **验收可执行覆盖率** | `具有至少一个 testable acceptance scenario 且链接到 test/eval 的 current requirements ÷ current requirements 总数` | 越高越好；可先只要求 testable criterion，再逐步要求 executable test | NASA 要求 requirements 可验证；Kiro 用 EARS acceptance criteria；OpenSpec requirement 绑定 Given/When/Then scenarios。【机构/厂商文档】 citeturn15view4turn17view2turn16view5 |
| **需求变更闭环完整率** | `同时具备变更原因/来源、owner/reviewer disposition、current-state 更新、下游验证结果与历史留档的已批准 change ÷ 已批准 changes` | 越高越好；用于发现“批准了但 current 没改”“改了但没验证”“验证了但无 provenance” | NASA formal initiation/assessment/review/approval/disposition；OpenSpec merge+archive preserves context。【机构/工具文档】 citeturn15view4turn16view7 |
| **反馈证据绑定率** | `附带 trace/replay/log/source context 中至少一种可复查材料的 actionable feedback ÷ actionable feedback 总数` | 越高越好；比“反馈都有文字描述”更接近可复现性 | Sentry 把反馈和 replay/event 关联；LangSmith 将 failing trace 留入 dataset；GitHub Issue Forms 支持结构化日志字段。【厂商文档】 citeturn18search12turn17view5turn17view7 |
| **需求变更负荷 / volatility** | 每周期可定义为 `(ADDED + MODIFIED + REMOVED requirement events) ÷ 周期开始时 current requirements 数量`；同时分开报告三类更稳妥 | **不是越低越好**；用于发现需求高速变化区、估计 review/trace 维护负担，并解释其他健康指标恶化 | OpenSpec 已把需求变化正式分类为 ADDED/MODIFIED/REMOVED，因此这些事件可直接计数。【工具文档；公式为本研究 operationalization】 citeturn16view6 |

其中，**双向需求可追溯完整率**具有本报告中最强的独立实证基础。Rempel 与 Mäder 的研究分析 24 个中大型开源项目，并针对 high-/low-level impact analysis、requirements satisfaction 等活动定义 traceability completeness；结果显示其中多类完整度与缺陷率存在显著关系。因此，对于本项目，“需求是否能从来源追到执行/验证，并从执行/验证反追到需求”不只是审计便利，而有实际软件质量证据支持。citeturn21search1turn21search3

相反，**过期需求误用率、挂起需求复评及时率、反馈证据绑定率**目前没有找到被广泛采用的标准公式；它们之所以值得采纳为候选，是因为它们直接测量本项目特有的失败模式，而不是因为行业已有统一 benchmark。对应的标准阈值因此为 **UNKNOWN**。

对指标使用还应避免一个常见误区：需求 volatility 本身并不等于不健康。真实用户完全可能合理反复改变想法；更有意义的是观察“高 volatility 是否同时造成冲突发现延迟、过期需求误用、traceability 降低或 deferred review 积压”。因此建议把 volatility 作为解释变量，而不是简单 KPI 惩罚变化。这一判断是本研究的度量解释，不是某厂商给出的统一阈值。

**来源表（访问日期统一为 2026-08-31）**

| 编号 | 标题 | URL | 访问日期 |
|---|---|---|---|
| S01 | GitHub Spec Kit Documentation【厂商/开源项目文档】 citeturn16view0 | https://github.github.com/spec-kit/ | 2026-08-31 |
| S02 | github/spec-kit Repository【厂商/开源项目文档】 citeturn16view1turn16view2 | https://github.com/github/spec-kit | 2026-08-31 |
| S03 | Spec Kit `analyze` command implementation / PR #1451【开源项目文档】 citeturn16view3 | https://github.com/github/spec-kit/pull/1451/files | 2026-08-31 |
| S04 | “SpecKit creates the illusion of work, generating a bunch of text” Discussion #1784【社区经验·2025-09】 citeturn16view4 | https://github.com/github/spec-kit/discussions/1784 | 2026-08-31 |
| S05 | Introducing Kiro【厂商文档·2025-07】 citeturn17view1 | https://kiro.dev/blog/introducing-kiro/ | 2026-08-31 |
| S06 | Kiro Requirements-First【厂商文档·页面更新 2026-08-04】 citeturn17view2 | https://kiro.dev/docs/specs/feature-specs/requirements-first/ | 2026-08-31 |
| S07 | Requirements analysis: catching requirement bugs before they become code【厂商文档·2026】 citeturn20view2 | https://kiro.dev/blog/deep-spec-analysis/ | 2026-08-31 |
| S08 | Kiro Quick Spec【厂商文档·页面更新 2026-08-04】 citeturn17view3 | https://kiro.dev/docs/specs/quick-spec/ | 2026-08-31 |
| S09 | From spec to production: a three-week drug discovery agent using Kiro【厂商案例·2026-02】 citeturn17view4 | https://aws.amazon.com/blogs/industries/from-spec-to-production-a-three-week-drug-discovery-agent-using-kiro/ | 2026-08-31 |
| S10 | OpenSpec Concepts【开源项目文档】 citeturn16view5turn16view6turn16view7 | https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md | 2026-08-31 |
| S11 | Fission-AI/OpenSpec Repository【开源项目文档】 citeturn12view0 | https://github.com/Fission-AI/OpenSpec | 2026-08-31 |
| S12 | NASA NPR 7123.1B Appendix C — Systems Engineering Processes【机构规范】 citeturn15view4 | https://nodis3.gsfc.nasa.gov/displayCA.cfm?Internal_ID=N_PR_7123_001B_&page_name=AppendixC | 2026-08-31 |
| S13 | NASA Technical Requirements Definition【机构规范】 citeturn15view5 | https://www.nasa.gov/reference/4-2-technical-requirements-definition/ | 2026-08-31 |
| S14 | NASA Software Engineering Handbook — Requirements【机构规范】 citeturn15view6 | https://swehb.nasa.gov/plugins/viewsource/viewpagesrc.action?pageId=32604503 | 2026-08-31 |
| S15 | Martin Fowler, Architecture Decision Record【业界方法·2026】 citeturn15view7 | https://martinfowler.com/bliki/ArchitectureDecisionRecord.html | 2026-08-31 |
| S16 | IETF — About RFCs: Statuses, Obsoleting and Updating【标准组织文档】 citeturn20view4 | https://www.ietf.org/process/rfcs/ | 2026-08-31 |
| S17 | OpenAI Evaluation Best Practices【厂商文档】 citeturn14view6 | https://developers.openai.com/api/docs/guides/evaluation-best-practices | 2026-08-31 |
| S18 | Getting Started with OpenAI Evals【厂商文档·2024-03-21，现已归档】 citeturn14view7 | https://developers.openai.com/cookbook/examples/evaluation/getting_started_with_openai_evals | 2026-08-31 |
| S19 | Anthropic — Choosing the right model【厂商文档】 citeturn19view0 | https://platform.claude.com/docs/en/about-claude/models/choosing-a-model | 2026-08-31 |
| S20 | LangSmith Evaluation Types【厂商文档】 citeturn19view1 | https://docs.langchain.com/langsmith/evaluation-types | 2026-08-31 |
| S21 | LangSmith Evaluation【厂商文档】 citeturn17view5 | https://docs.langchain.com/langsmith/evaluation | 2026-08-31 |
| S22 | LangSmith — How to compare experiment results【厂商文档】 citeturn19view2 | https://docs.langchain.com/langsmith/compare-experiment-results | 2026-08-31 |
| S23 | GitHub Docs — Syntax for issue forms【厂商文档】 citeturn17view7 | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms | 2026-08-31 |
| S24 | Sentry User Feedback【厂商文档】 citeturn18search1 | https://docs.sentry.io/product/user-feedback/ | 2026-08-31 |
| S25 | Sentry Replay Details【厂商文档】 citeturn18search12 | https://docs.sentry.io/product/session-replay/replay-details/ | 2026-08-31 |
| S26 | Zadenoori et al., *Large Language Models (LLMs) for Requirements Engineering (RE): A Systematic Literature Review*【论文综述预印本·2025-09-14】 citeturn20view1 | https://arxiv.org/abs/2509.11446 | 2026-08-31 |
| S27 | Dąbrowski et al., *Large Language Models for Requirements Engineering: A Cross-Task Empirical Evaluation*【论文实证预印本·2026-08-21】 citeturn13academia11turn20view0 | https://arxiv.org/abs/2608.21531 | 2026-08-31 |
| S28 | Rempel & Mäder, *Preventing Defects: The Impact of Requirements Traceability Completeness on Software Quality*, IEEE TSE 43(8), 2017【论文实证】 citeturn21search3 | https://dl.acm.org/doi/10.1109/TSE.2016.2622264 | 2026-08-31 |