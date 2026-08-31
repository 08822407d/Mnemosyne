# MNE-DR-021 / FABLE5-REDESIGN-001-RQ2 · 跨会话连续性实践与评测

**研究范围：**公开网络资料；重点覆盖 2025 年下半年至 2026-08-31 可公开检索的论文、官方产品文档与公开基准；较早工作仅作为基线。  
**证据标记：**“**论文实证**”表示有公开实验或 benchmark 数据；“**系统作者实证**”表示实验由被评系统的作者/厂商团队发表，不能视为独立复现；“**厂商文档**”仅证明功能/设计已公开部署或支持，不等于效果已经独立验证；“**UNKNOWN**”表示在本次公开检索中没有找到足够直接的公开证据。

## Q1 · 机制与系统盘点

截至 2026 年 8 月，公开实践已经相当明确地从“给模型一个越来越大的聊天记录”转向**多层持久化**：工作线程有 checkpoint/session state，长期信息进入文件、键值/向量库或图结构，必要信息在每次会话重新装入；长上下文本身更多被当成有限的工作区，而不是唯一长期记忆。LangGraph 已把这种区分直接产品化为 thread-scoped checkpointer 与 cross-thread store；Letta 则把“始终在上下文中的 memory blocks”和可检索的长期记忆分层。citeturn17view1turn17view0

| 机制 | 2025–2026 代表做法 | 成熟度 | 已公开效果与限制 |
|---|---|---|---|
| **上下文压缩、裁剪、摘要** | Claude/Codex 等 coding-agent 工作流都把压缩视为越过 context limit 的常规手段；LangGraph 支持 thread 状态持续化，再配合上下文管理。 | **生产级、极普遍**；但它是工作上下文管理，不应自动等同于无损长期记忆。 | 2026 年受控实验显示，摘要/抽取的主要风险是**写入时不可逆的信息损失**。在同一 retrieval/rerank/reasoning pipeline 中，verbatim chunks 在 LoCoMo 为 43.9% vs extracted artifacts 28.0%，LongMemEval-S 为 67.4% vs 45.4%；一个专门测试精确约束的 probe 中，摘要 exact match 14.0%，逐字检索 91.0%。citeturn14view0 |
| **外部文件/文档型记忆** | Claude Code 的 `CLAUDE.md`、`.claude/rules/`、auto-memory `MEMORY.md`；仓库中的 instructions/specs；文件本身作为可版本控制的持久事实载体。 | **coding-agent 场景生产级**。 | Claude Code 明确规定每个 session 都从 fresh context 开始，`CLAUDE.md` 与 auto memory 跨 session 加载；子目录规则可按需加载，官方还建议保持规则短小，过长会降低 adherence。`MEMORY.md` 只预载前 200 行或 25KB，其余 topic files 按需读取。citeturn19view3 论文层面，逐字 source-preserving 表示显著优于用抽取产物替换原文；但**“Git 仓库作为唯一长期真相源”本身的独立对照 benchmark：UNKNOWN**。citeturn14view0 |
| **向量检索 / RAG 型记忆** | Mem0、LangGraph Store、Letta archival/searchable memory，以及大量 embedding + reranker 架构。 | **技术和部署成熟度高；性能高度依任务而变**。 | Mem0 作者论文报告 LoCoMo 上相对 OpenAI baseline 的 LLM-judge 提升 26%，p95 latency 降 91%、token cost 省逾 90%；这是**系统作者实证**，不是独立复现。citeturn18view0 2026 AgentMemBench 的统一 harness 则发现 external key-value/dense retrieval 在其三套数据上整体最强，macro Recall@5 0.792；LoCoMo Recall@5 为 0.573，而其测试的窗口、图和摘要策略均 ≤0.005，但付出了约 5,100-token footprint 对约 300-token 窗口基线的代价。该结果说明“简单、可追溯的 dense retrieval”仍是非常强的基线，并不存在“越复杂越好”的一致排序。citeturn16view0 |
| **结构化/图型记忆** | Zep/Graphiti temporal KG、Mem0 graph、Letta structured memory blocks；新研究还使用显式 supersession、dependency、causality graph。 | **框架层成熟，效果证据混合**。 | Zep 作者论文报告 DMR 94.8% vs MemGPT 93.4%，LongMemEval 相对其 baseline 最高 +18.5% accuracy、约 -90% latency；同样属于**系统作者实证**。citeturn18view1 更关键的新证据来自 AMA-Bench：现有 memory system 的问题之一是 similarity retrieval 丢失 causal/objective information；其 causality graph + tool-augmented retrieval 的 AMA-Agent 达到 57.22%，比最强 baseline 高 11.16 个百分点。citeturn18view2 StateMemBench 又显示显式记录“哪个状态 supersede 哪个旧状态”可显著提高 current-state accuracy。citeturn18view3 |
| **checkpoint / execution-state 持久化** | LangGraph checkpointer；Claude Code/Codex session resume；coding agents 保存 working tree + trajectory/session。 | **生产级，且与“记忆”概念开始分离**。 | LangGraph 明确把 checkpoint 用于 conversation continuity、interruption resume、failure recovery、time travel、human-in-the-loop，而 Store 才承担 cross-thread facts/preferences。citeturn17view1 这一区分很重要：长期项目连续性不只是“知道以前发生过什么”，还包括“恢复到哪个执行状态”。 |
| **平台原生记忆** | ChatGPT Memory、Claude Memory、Gemini past-chat memory。 | **面向终端用户的大规模产品级功能**；内部算法通常不透明。 | ChatGPT 当前 Memory 会自动综合 chats/files/apps，并提供可编辑 memory summary 和 response memory sources；官方也承认旧系统会 stale、出现互相矛盾的 memories，新系统改成自动维护。citeturn19view1 Claude 在 2026-07 把旧的 daily summary 换成 conversation 中可读写的分类 individual entries。citeturn19view0 Gemini 可利用 past chats 做 project-next-step 等个性化，并明确提示“might not always get it right”。citeturn19view2 **三者之间公开、独立、可复现实验比较跨会话工作连续性准确率：UNKNOWN。** |

### 当前格局的几个重要变化

第一，**“长期记忆”已经不再等价于“摘要”**。LongMemEval 在 500 个人工构造问题上把能力拆为 information extraction、multi-session reasoning、temporal reasoning、knowledge updates 与 abstention；当 interaction history 拉长时，当时的 commercial assistants 和 long-context LLMs 出现约 30% accuracy drop。citeturn21view0 2025–2026 的工作进一步把“选择性遗忘”“状态突变”“因果轨迹”“agent 执行”从一般 recall 中拆出来。MemoryAgentBench 明确包含 retrieval、test-time learning、long-range understanding、selective forgetting 四种能力；没有一种现有方法在四类上全面解决。citeturn21view2

第二，**原文保存重新变得重要**。2026 的 controlled ablation 并不是证明“结构化记忆无用”，而是更精确地证明：当结构化 artifact **替代** source text 时，会发生无法在读时恢复的 write-time loss；其结论是结构应该补充 source，而不是切断回 source 的路径。研究中 69.0% 可诊断的“chunks 对、artifact 错”案例，是 extractor 根本没有把相关事实写进 artifact。citeturn14view0 这与 Zep 一类保留 episode/source provenance 的设计、以及 DreamBench-SWE 中 verbatim event memory 仍然很强的结果相呼应。citeturn15view3turn18view1

第三，**“状态恢复”和“事实记忆”正被分成两个问题**。例如 LangGraph 用 checkpoint 恢复 thread execution state，用 Store 维护 durable knowledge；Claude Code/Codex 直接提供 session resume；新 handoff benchmark 则开始同时保存 repository working state 和 predecessor trajectory，而不是只问“上一轮说了什么”。citeturn17view1turn20view1turn20view2turn15view0

因此，2026 年最有依据的整体判断不是“某一种 memory architecture 获胜”，而是：**多层组合已成主流；无损 source/provenance、检索、状态版本、checkpoint 各解决不同故障面；复杂 memory extraction/graph 的价值必须通过任务级 benchmark 验证，不能仅凭架构复杂度推断。** AgentMemBench、AMA-Bench、StateMemBench、DreamBench-SWE 都出现了“简单 baseline 很难击败”或“专门结构只在特定故障面显著获益”的结果。citeturn16view0turn18view2turn18view3turn15view3

## Q2 · 评测指标与基准

2024 年的 LoCoMo/LongMemEval 仍是基础设施，但 2025H2–2026 的明显变化，是 benchmark 从**“过去说过什么？”**转向**“经过多 session 的修改、执行和冲突后，现在到底该怎么继续？”**。citeturn21view1turn21view0

| Benchmark / 日期 | 测什么 | 主要打分方式 | 与“换会话后继续工作”的距离 |
|---|---|---|---|
| **LoCoMo**，2024 | 平均约 300 turns、9K tokens、最长 35 sessions 的长期 dialogue；QA、event summarization、multimodal dialogue generation。 | 任务级 QA/生成/摘要评价；重点是跨 session 长距离记忆。 | **中等。** 是长期对话经典基线，但仍主要问历史内容，而非接手未完成的工作。citeturn21view1 |
| **LongMemEval**，ICLR 2025 | information extraction、multi-session reasoning、temporal reasoning、knowledge update、abstention；500 个精编问题。 | 主要看最终 QA accuracy，并可拆 retrieval 与 reading。 | **中等偏高。** 已包含 update/abstention，但仍以问答为核心。citeturn21view0 |
| **MemoryAgentBench**，2025-07，2026-06 更新 | accurate retrieval、test-time learning、long-range understanding、selective forgetting。 | 各 competency 的任务正确率；通过 incremental multi-turn ingestion 测 memory agent。 | **中等偏高。** 特别适合测“记住旧规则、学习新规则、忘掉旧状态”。citeturn21view2 |
| **MemoryArena**，2026-02 | multi-session Memory–Agent–Environment loop；web navigation、规划、搜索、形式推理，后续 subtask 依赖前一 session 的行动/反馈。 | 最终 agentic task success。 | **高。** 后续任务必须把早期 experience 用于行动；作者发现即使在 LoCoMo 接近饱和的 agent，也会在这里表现明显变差。citeturn21view3 |
| **AMA-Bench**，2026-02/05 | 长 agent–environment trajectory 中的 states/actions/observations/tool outputs；含真实轨迹和可任意扩长的 synthetic trajectory。 | expert-curated 或 rule-based QA **accuracy**。 | **高。** 测的是 agent 执行轨迹中的 causal/objective memory，而非纯聊天事实。citeturn18view2 |
| **Memora + FAMA**，2026-04 | weeks→months 的 personalized memory，Remembering、Reasoning、Recommending；大量 add/update/delete。 | **Forgetting-Aware Memory Accuracy**：正确使用当前有效 memory 得分，依赖 obsolete/deleted memory 受罚。 | **高，针对状态演化。** Quarterly 条件平均要整合 28.4 个历史 memory elements、经历 14.8 次 mutation，最大分别 309/94。citeturn16view1 |
| **AgentMemBench**，2026-06/08 | 同一 harness 比较 context window、external KV、graph episodic、summary compression、web-augmented 等 memory strategy。 | **Recall@k、MRR、nDCG@k、Answer F1、LLM-judge Faithfulness、Memory Footprint、Latency**，491 个 annotated question turns。 | **很适合作为组件级指标库**，但不是 handoff end-to-end benchmark。citeturn16view0 |
| **Handoff Debt**，2026-06 | coding agent 在一个 predecessor 已做一半的 SWE-bench task 上接手；比较 repository-only、raw trace、summary notes、structured notes。 | 官方 SWE-bench **resolution**；另计 cumulative prompt tokens、agent events。75 个 source tasks → 181 handoff points → 2,172 runs。 | **非常高；目前最直接的 handoff benchmark 之一。**citeturn15view0 |
| **StateMemBench**，2026-08 | 234 个 multi-session scenarios；故意多次修改 facts、constraints、user/agent decisions。 | closed-pool classifier 将回答判为 **current state / superseded state / other failure**，核心是 current-state accuracy。 | **非常高，针对“接着做时不要使用旧状态”。**citeturn18view3 |
| **DreamBench-SWE**，2026-08 | 后续 software session 依赖早期 session 中**无法从当前 repo 单独推断**的信息，包括 stale architecture、reviewer preference、generated-file trap、scope、exact token 等。 | executable hidden oracle pass/fail；附 UsefulMemoryPrecision、stale/overscope/repeated-error 等 hygiene diagnostics。 | **极高；直接测试跨 session successor 是否真正保住前序证据。**citeturn13view1turn15view3 |
| **Handoff Tax**，2026-08 | 一个模型中途接手另一个模型 trajectory；比较 full raw trajectory、sender-summary、receiver-summary、trajectory-drop，同时保持 working tree。 | SWE-bench pass rate、cost、steps，并计算质量优势/成本优势 retention。主实验 58,000 runs、36B processed tokens。 | **极高。** 直接证明 handoff interface 本身会改变后续质量/成本。citeturn15view1turn15view2 |

**是否已经有“会话切换后能否正确继续工作”的专门评测？——有，而且 2026 年明显成熟。**

最接近委托方目标的并不是传统 LoCoMo，而是三类新 benchmark：

**Handoff Debt**直接冻结 predecessor 的 repository state，再让 successor 在四种不同“交接视图”下继续。repository-only 虽然拥有相同代码状态，却因为看不到“做过什么、测过什么、失败过什么”，产生大量 rediscovery。带 context 的 handoff 相比 repository-only，raw trace 的 median agent events 少 57–59%，summary/structured notes 少 20–46%，prompt tokens 少 42–63%；raw trace 的最终 solved-rate 也分别提高 +6.1、+6.6、+14.9 个百分点。citeturn15view0

**DreamBench-SWE**更接近“新 session 必须继承之前不可重新推断的信息”。其 successor audit 中，无 external memory 仅 21/180 = 11.67% 通过；deterministic verbatim event memory 为 82/180 = 45.56%，typed-plus-raw reference probe 为 83/180 = 46.11%，一个冻结配置的 hosted Mem0 literal-storage 条件为 97/180 = 53.89%。作者明确警告这不是对产品总体性能的排名，但它证明 benchmark 能区分“有可用跨 session 证据”和“无证据”的行为。citeturn13view1

**StateMemBench/Memora**补上了另一个关键维度：不是“能否找到旧东西”，而是“旧东西已经过期时，能否不再按照它做”。StateMemBench 的 strongest same-backbone baseline 在 DeepSeek-V4-Flash 上 current-state accuracy 0.205，显式 state/supersession 方法到 0.363；在 Qwen-3.5-9B 上相对 strongest memory system 从 0.149 到 0.233。其 wrapper 在六种 memory/retrieval backend 上能提高 +32 至 +67 个百分点，其中 cost/length matched control 仍有 +15 至 +32 点可归因于 state structure。citeturn18view3

因此，“像同一个对话”不能只用 recall accuracy 验收。至少必须同时测：**接手后的任务成功、rediscovery cost、当前状态正确性、过期状态误用、约束保持、来源忠实度、拒答/拒收能力和成本。**

## Q3 · 已发表的失败模式

**摘要偏差与不可逆压缩。** 最典型的失败不是摘要完全错，而是把一个仍然“语义大致正确”的陈述压缩得失去约束力。例如 “use type hints everywhere” 被概括成一般的 type-hint preference 后，关键词还在，但量词 `everywhere` 已丢失。受控实验的 exact constraint probe 为摘要 14.0% 对逐字 retrieval 91.0%；自然 benchmark 上，verbatim chunks 对 extracted artifacts 的优势达 15.9–22.0 个百分点。citeturn14view0 **已知对策**不是禁止摘要，而是保留 lossless source/provenance，让摘要、artifact、graph 成为索引或 annotation，不能成为唯一不可回溯的替代物。该论文的 union store（chunks + artifacts）与 chunks 基线相当，也支持这种“结构叠加在原文上”的思路。citeturn14view0

**过期状态污染 / state drift。** Memora 表明现有系统常把“曾经正确”误当成“现在仍正确”；其 manual error analysis 中，最佳 memory agent 的 recommendation 错误样本里 16/25（64%）归因于没有忘掉 outdated memory，7/25（28%）涉及 preference 的 partial retrieval。普通 memory-presence accuracy 因为不惩罚 obsolete memory，会系统性高估性能。citeturn16view1 StateMemBench进一步将这一故障隔离出来：即便 relevant new fact 已出现在 assembled context，agent 仍可能按照 superseded/incomplete state 行动。citeturn18view3 **已知对策**包括显式 `valid/current/superseded/deleted` 状态、版本/时间关系、dependency propagation，以及将 current-state correctness 单独计分，而不是简单“最新向量结果优先”。

**相似度检索有相关性却没有因果性。** AMA-Bench 的核心发现是，真实 agent trajectory 中需要的不只是“和 query 文义最像”的 observation，还包括造成当前结果的 action、失败原因、客观 environment state 和工具输出；现有 memory systems 因 causal/objective information 捕获不足以及 lossy similarity retrieval 而表现较差。其 causality graph + tool-augmented retrieval 达到 57.22%，高出最强 baseline 11.16 点。citeturn18view2 **对策**是把 action→observation→decision→outcome 或 dependency 链作为一等数据，而不把向量 similarity 当成唯一 routing signal。

**抽取器造成“记忆错误”与遗漏。** 结构化 memory 常在 write time 让 LLM 判定“什么值得记”。这意味着遗漏一旦发生，后续再强的 reranker 也无法找回。Verbatim Chunks 的 error analysis 发现，在可诊断的 chunk-pass/artifact-fail case 中 69.0% 属于 extractor 根本没把事实写成 artifact；另有 temporal markers、implicit attributes、情感偏好等类别容易被漏掉。citeturn14view0 **对策**是 immutable/raw trace + derived index；抽取结果应有 source pointer、置信度和可重建性，不能单独承担 authoritative record。

**上下文腐化不等于“上下文越少越好”。** Handoff Tax 给出了非常重要的反例：完整 raw trajectory 对接手者的价值取决于**接手方向**。从低能力模型升级到高能力模型时，继承低能力 trajectory 可能成为负担；Claude 条件下 raw escalation 甚至被“放弃原尝试、让高能力模型 fresh restart”在成本和准确率上同时支配。相反，从高能力模型下放给低能力模型时，删除 trajectory 明显损害质量；例如 Claude HC→LC raw handoff 将 pass rate 从 LC-only 的 54.6% 提至 65.6%，而保留大部分成本优势。citeturn15view1turn15view2 因此**对策是 selective handoff，而不是 dogmatic full-history 或 dogmatic summary**：持久工作产品、source-of-truth、关键 evidence、失败结论和 unresolved state 应与低价值探索轨迹分开处理。

**handoff rediscovery。** 只有当前 repository/work product 并不意味着 successor 知道 predecessor 的意图和实验史。Handoff Debt 中 repository-only 与其他条件拿到完全相同的 checkpointed files，但 predecessor context 可以减少 20–59% 的 agent events；raw trace 虽首 prompt 很大，反而可能因为减少后续重复探索而降低总 prompt tokens。citeturn15view0turn14view3 **对策**是把“当前结果”与“为什么到这里”同时移交，尤其包括验证结果、已排除路径、剩余任务、当前 hypothesis 和 known failure。

**persistent memory poisoning。** Microsoft 2026 Zero Trust catalog 将 AI memory/context poisoning 单列为 durable attack surface：攻击内容可通过用户输入、poisoned documents/RAG、grounding data 或 adversarial agent interactions 进入长期 store，并跨 session 影响未来 reasoning/action；共享 memory 中一个 compromised agent 也可向其他 agent 种入隐藏 directive。citeturn20view3 **对策方向**包括把 provenance/trust level 与内容一起保存、隔离自动生成 memory、限制谁可写 shared/authoritative memory、危险操作在执行时重新做权限检查。Letta 已支持 read-only memory block；Claude Code 也明确说明 CLAUDE.md 只是 context，而不是 enforced configuration，对于必须阻断的动作应使用 PreToolUse hook。citeturn17view0turn19view3 这说明“记忆里的规则”与“权限/安全执行机制”不应混为一层。

**身份/授权跨 session 或跨 agent 混淆。** 公开安全资料已经明确指出 shared persistent context 会扩大 poisoning 与权限边界风险，但本次检索没有找到一个已经成为主流、专门量化“旧 session 的用户/agent 身份或授权被错误继承”的长期连续性 benchmark。因此其作为独立 benchmark 类别目前记为 **UNKNOWN**；现有可操作证据更偏向 architecture/security principle，而非成熟准确率数字。citeturn20view3

总的说，2026 年研究正在把长期 memory 的失败从一个笼统的“忘记”拆成至少五个不同错误：**没保存、没找回、找回旧版本、错误解释、以及把不该可信/不该授权的内容永久化**。只优化 retrieval recall 无法覆盖后四类。citeturn16view1turn18view2turn18view3turn20view3

## Q4 · 交接（handoff）专门实践

公开实践中已经可以区分三种完全不同、但经常都叫“handoff”的机制。

**其一是 agent-to-agent delegation。** OpenAI Agents SDK 把 handoff 本身建模成一个 tool；例如 `transfer_to_<agent>`，可以定义目标 agent、structured `input_type`、handoff callback 和 input filters。也就是说，交接不是一句自由文本“你继续吧”，而可以有结构化 payload 与明确路由。citeturn20view0 这类机制解决的是“谁接手、交什么上下文”，但不自动解决几个月后长期 source-of-truth 的一致性。

**其二是 checkpoint/resume。** LangGraph 将每个 thread 的 graph state checkpoint 化，用于中断后恢复、failure recovery、time travel 和 human-in-the-loop；跨 thread 的 durable facts 放 Store。citeturn17view1 Claude Code 会在本地保存每次 conversation，`claude --continue` 可继续当前目录最近 session，`--resume`/`/resume` 可选择历史 session；官方明确把用途写成“task spans multiple sittings”。citeturn20view1 Codex 的 `codex resume` 已标为 Stable，可以按 session ID 或最近会话恢复，`codex fork` 则从历史 session 分叉为新 chat。citeturn20view2

这类 resume 的优势是**真正恢复原 trajectory/session**，而不需要通过一个新模型重新解释一份人工摘要；但它不等价于“跨任意新会话迁移”。它还可能继承大量已经无关或错误的 trajectory，因此与新 session handoff 是不同的问题。Handoff Tax 正好说明，完整继承 trajectory 有时帮助、有时会形成 handoff tax。citeturn15view1turn15view2

**其三是显式 takeover package。** Handoff Debt 是目前公开证据最直接的一项：作者比较了四个 takeover interface——只给 repository、给 raw trace、给 summary notes、给 structured notes。所有 successor 均从同一 frozen repository state 开始，因此差异可以较干净地归因于交接信息。结果表明，交接 context 对**降低重新发现成本**的影响比对最终 solved-rate 更稳定：raw trace 事件数 -57% 到 -59%，summary/structured notes -20% 到 -46%，token -42% 到 -63%；solved-rate 的提升则依模型和格式不同。citeturn15view0

这一结果支持一种很具体的实践判断：**交接质量不能只检查“文件状态有没有保存”，还必须检查 successor 是否得到足够的 intent、evidence、validation history 和 unresolved work。**

与此同时，Handoff Tax 对“交接包越全越好”提出了重要限定。其 58,000-run study 比较 raw、sender-generated compact、receiver-generated compact、trajectory drop；所有条件都保留工作树。结果显示高能力 receiver 接低能力 trajectory 时，减掉错误探索可能更好；低能力 receiver 接高能力 trajectory 时，保留 trajectory 又显著有帮助。citeturn15view1turn15view2 所以公开实证更支持**分层、可选择的交接表示**，而不是一个固定的“永远交全部 history”规则。

DreamBench-SWE 则把 handoff 推到真正的 multi-session memory hygiene：later session 的任务有意设计成仅凭当前 repository 无法推断，必须继承 earlier evidence；其 hidden executable oracle 检查 successor 是否真的做对，而不是让 LLM judge 判断“看起来记得”。citeturn13view1 这类 benchmark 与 Mnemosyne 的“像同一个对话”目标高度相似，因为它考的是**前一个 session 中形成的知识和约束能否改变后一个 session 的实际行为**。

**接收报告 / fail-closed。** 本次检索能找到大量“structured handoff”“checkpoint validation”“abstention”“permission gate”的相邻做法，但没有找到一个公开主流框架把“receiver 必须先生成接收报告，逐项验证 handoff 包，若不完整则拒绝继续”作为标准 handoff protocol，并有专门对照实验。因此：

> **“交接包 + 接收报告 + fail-closed 拒收”这一完整三段式协议的公开行业普及度与独立效果：UNKNOWN。**

有间接支持：LongMemEval 把 abstention 列为长期 memory 核心能力；DreamBench-SWE 使用严格 validity gates 和 executable oracles；LangGraph checkpoint 面向 failure recovery；安全资料强调 persistent state 不可默认可信。citeturn21view0turn13view1turn17view1turn20view3 但这些不能替代对该具体三段协议的直接实验。

**产品级 session recovery 的独立实测评价也仍有明显空白。** Claude Code、Codex 等官方明确支持 resume/fork，说明该能力已生产化；然而本次没有找到对“Claude Code resume vs Codex resume vs Copilot/其他产品”的独立、固定任务、固定模型的 continuation-success head-to-head benchmark。故该项为 **UNKNOWN**。Handoff Debt/Handoff Tax 是目前最接近的科学替代证据，但它们评估的是受控 coding-agent takeover，而不是现成产品 UI 的 resume 功能。citeturn20view1turn20view2turn15view0turn15view1

## Q5 · 需求与意图的长期管理

长期项目里的“需求”正在逐渐从聊天中的一次性 prompt 变成**repository artifact**。GitHub 的 Spec Kit 公开推广 spec-driven development，将 specification/plan/tasks 等作为 coding agent 可读取和执行的项目工件，而不是只保留某次 conversation。这个方向与 Claude Code 把 project instructions 放在受版本控制的 `CLAUDE.md` 中相同：团队知识脱离某个模型 session，进入可长期维护的文件层。citeturn9search4turn19view3

但是，现有公开产品通常解决的是“**把需求结构化**”，而不是“**把用户原文永久保存，再单独维护解释和获批版本**”。Claude Code 的 auto memory 会由模型根据 corrections/preferences 自动写 notes；ChatGPT Memory 会自动综合历史 context；这些都说明 mainstream product 更倾向于 derived/synthesized memory，而非一个明确的 immutable raw-request ledger。citeturn19view3turn19view1

2026 年的实验使“保留原始需求文本”获得了比过去更直接的证据。Verbatim Chunks study 的结论不是专门关于 requirements engineering，但其实验与需求保存问题高度对应：一旦 extractor/summary 在 write time 把限定词、时间或隐含细节舍弃，后续 retrieval 无法重构；逐字 source-preserving store 在两个长期 memory benchmark 上显著优于 extracted artifacts。citeturn14view0 因而“原文 + derived interpretation”至少有明确的 memory-fidelity 理由；至于“三层 raw / analysis / user-approved execution”这一具体 schema，本次未发现已标准化的公开 benchmark，故其额外收益仍为 **UNKNOWN**。

对于**演化和矛盾管理**，2026 的 evidence 比需求工程工具本身更清楚：Memora 要求反复 add/update/delete；StateMemBench 直接 adversarially revise facts、rules、decisions，并证明显式 supersession/dependencies 可以显著改善 current-state accuracy。citeturn16view1turn18view3 因此长期需求管理中至少应把“历史上说过的需求”和“目前生效的需求”视为两个不同问题。简单保留完整 Git 历史并不自动保证模型知道哪个版本当前有效；反过来，只保留最新版本又会损失 provenance。

目前较成熟的公开方法因此可以概括成：**原始/历史 artifact 可追溯 + 当前状态显式化 + change history/versioning + acceptance criteria/task artifacts + 检索层**。其中 Git/spec 文件和 path-scoped instructions 已产品化；而对“冲突检测、用户重新批准、原文不可变层”的综合自动化支持仍较碎片化。citeturn19view3turn18view3

## Q6 · 与委托方现行方案的对照

下述比较严格按任务书给出的五点公开方案进行，不推断未公开实现。

**业界普遍出现、但现行公开描述中未明确包含的机制：**

| 外部实践 | 对现行方案可能构成的“未明确机制” | 证据性质 |
|---|---|---|
| **semantic retrieval / reranking** | Git 可以保存真相，但当历史量增长后，如何从真相源定位当前任务需要的旧材料，是另一个问题。公开描述中没有说明是否有 vector/BM25/reranker 索引。 | AgentMemBench 中 EKV/dense retrieval 在统一 harness 上总体最强；AMA-Bench 则说明仅 similarity 又不足以覆盖 causal retrieval，所以更合理的结论是“需要 retrieval layer”，而非“必须只用向量”。citeturn16view0turn18view2 |
| **显式 temporal validity / supersession graph** | Git commit history 能告诉你“发生过变化”，但不自动给模型一个 current-state dependency graph。 | StateMemBench 中显式 supersession/state structure 带来显著 current-state gain；Memora 表明 stale reuse 是大量实际错误来源。citeturn18view3turn16view1 |
| **execution checkpoint/environment state** | 交接包是信息移交；checkpoint 是对“运行状态/执行状态”的直接保存。现行公开描述未说明是否保存工具/environment checkpoint。 | LangGraph 已把 thread checkpoint 与 cross-thread memory 分开；Handoff Debt 固定 repository state 再改变 handoff context，证明两者是独立变量。citeturn17view1turn15view0 |
| **自动 memory extraction / personalization** | Letta、Claude Code auto memory、ChatGPT native memory 都允许 agent/platform 自动维护长期记忆；现行原则“模型只作计算、Git 才是真相源”显然更保守。 | 这是**行业功能现状**，不是证据证明自动写入优于人工审核。自动 extraction 同时有 write-time loss 与 poisoning 风险。citeturn17view0turn19view3turn19view1turn20view3 |
| **共享/分 scope memory namespaces** | 主流框架逐渐显式区分 thread/user/agent/shared state。现行描述没有说明这一层是否存在。 | LangGraph 明分 single-thread checkpoint 与 cross-thread store；Letta memory block 可共享，也可设 read-only。citeturn17view1turn17view0 |

这里尤其要注意：上述是“公开描述未见”，不等于实际实现一定没有。

**现行方案有、而公开主流系统中相对少见的机制：**

第一是**“Git 文件是唯一 authoritative long-term truth，模型本身不拥有权威记忆”**。Letta、Claude Code auto memory、ChatGPT/Claude/Gemini native memory 都允许模型或平台自动形成 persistent memory，因此 Mnemosyne 的 trust model 明显更偏外部、可审计、human-governed。citeturn17view0turn19view3turn19view1turn19view0turn19view2

第二是**逐字 raw 用户原文与 analysis、approved execution 分层**。现有 memory 产品多会抽取、综合或分类用户信息；本次未发现主流 consumer/agent platform 把这三层作为标准 memory schema。它与 2026 “verbatim source 不应被 derived artifact 替换”的实验方向一致，但“三层”本身仍缺直接 benchmark。citeturn14view0

第三是**“交接包 + 接收报告 + fail-closed 拒收”**。OpenAI Agents SDK 有 structured handoff payload，Handoff Debt 有 raw/summary/structured handoff artifact，checkpoint 系统有恢复验证；但本次没有发现 mainstream framework 将 receiver acknowledgment + validation + refusal 组合成一个标准协议并公布对照结果。故该组合的行业普遍性为 **低/UNKNOWN**。citeturn20view0turn15view0

第四是**所有长期写入走 branch+PR 并由人合并**。coding-agent 生态当然大量围绕 Git branch/worktree/PR 操作，但“所有 memory 写入都必须经过 human merge 才成为 truth”并非上述 memory framework 的默认机制。例如 Letta block 默认 agent-managed/read-write，Claude Code auto memory 会在 session 中直接写 memory files，ChatGPT Memory 会自动更新。citeturn17view0turn19view3turn19view1

第五是**规则分层、按需加载且与长期事实分离的组合**。它并非完全独特：Claude Code 已公开支持 managed/user/project/local scopes、path-specific rules，并让子目录规则在读取相应目录时才进入 context；因此这部分实际上与 2026 coding-agent 主流实践高度同向。citeturn19view3

下面逐条看证据是支持还是提出质疑。

| 现行原则 | 支持证据 | 需要保留的质疑/UNKNOWN |
|---|---|---|
| **① Git 仓库文件为唯一长期真相源，模型只作计算** | Verbatim/source-preserving 实验支持保留可回溯 external evidence，而不是让一次 LLM extraction 取代原始信息；memory poisoning 研究也支持把 authoritative write 权限从随意 agent memory 中抽离。citeturn14view0turn20view3 | Git 本身不是 retrieval/state-resolution mechanism。AgentMemBench、StateMemBench 表明长期规模下还需要定位与“哪个版本当前生效”的机制。**直接证明 Git-only truth 优于其他 durable store 的 benchmark：UNKNOWN。**citeturn16view0turn18view3 |
| **② raw 原文 / analysis / user-approved execution 三层** | 这是五点中得到最直接新证据支持的部分之一：verbatim chunks 相比抽取 artifacts 在 LoCoMo +15.9pp、LongMemEval-S +22.0pp；69% 可诊断失败发生在 extraction write time。citeturn14view0 | 论文只证明“不要让抽取替代 source”，没有证明恰好三层是最优 schema，也没有证明每个项目对象都必须逐字永久保存。后一问题 **UNKNOWN**。 |
| **③ 交接包 + 接收报告 + fail-closed** | Handoff Debt 明确证明只有 work product 不够，handoff context 可显著减少 rediscovery，并有一定 solved-rate gain；LongMemEval 也把 abstention 视为长期 memory 能力。citeturn15view0turn21view0 | Handoff Tax 表明“交更多 context”不是单调增益，交接包必须控制低价值/错误 trajectory。对于“接收报告”及“fail-closed 阈值”的直接实验仍 **UNKNOWN**。citeturn15view1turn15view2 |
| **④ 行为规则分层按需加载** | Claude Code 的 managed/user/project/local hierarchy、path-scoped rules、subdirectory-on-demand loading 几乎是直接的公开产品类比；官方也指出更短、更具体的 instructions adherence 更好。citeturn19view3 | 必须区分“指导模型的 context”与“必须执行的安全 policy”。Claude Code 明确说 CLAUDE.md 不是 enforced configuration；不可违反的规则应放在执行 gate/hook，而不是仅靠加载文本。citeturn19view3 |
| **⑤ 所有写入 branch+PR，由人合并** | 与 memory poisoning 的 trust-boundary 问题方向一致，也与 coding-agent 的 review-before-edit/worktree isolation 思路一致。Claude Code 可用 plan mode 在落盘前要求 approval，并用 Git worktree 隔离并行改动。citeturn20view1turn20view3 | 本次没有找到 memory benchmark 证明“所有 persistent writes 都经过 PR”比 scoped automatic writes 在整体质量/成本上更优。因此强制全量 PR 的净收益、吞吐/人工成本权衡是 **UNKNOWN**。 |

对 Q6 最值得强调的并不是“现行方案超前”或“落后”，而是它选择了与多数自动 memory platform 不同的**信任边界**：行业主流越来越愿意让 agent 自动抽取、更新和共享 memory；现行方案则把 authoritative state 留在外部、人审、版本化介质。公开证据同时给这两侧提供了理由：automatic memory 可以降低重复输入和提升检索效率，但 extraction loss、stale state 和 persistent poisoning 说明“让 agent 自动写 authoritative truth”确实具有累积风险。citeturn18view0turn16view1turn14view0turn20view3

## Q7 · “像同一个对话”的验收指标候选

下面是**候选指标**，不是建议最终全部采用。一个重要原则是建立两类 baseline：**Same-Session Oracle**（不切换会话、保留相同工作状态）和 **Cold Restart**（只有当前工作产物、没有 handoff/memory）。这样才可以知道跨会话机制究竟保留了多少“同一对话”的性能，并产生多少额外成本。Handoff Debt 的 matched design 正是这种思路。citeturn15view0

| 指标候选 | 建议定义 | 依据 | 适用条件 |
|---|---|---|---|
| **Cross-Session Continuation Success，跨会话继续成功率** | `成功完成最终任务的 handoff cases / 总 cases`；对 software 可用 tests/oracles，对 research/workflow 用预先定义 acceptance criteria。另报告相对 Same-Session Oracle 的 retention：`handoff success / oracle success`。 | MemoryArena 直接按后续行动成功评估；Handoff Debt 用 SWE-bench resolution；DreamBench-SWE 用 hidden executable oracle。citeturn21view3turn15view0turn13view1 | **核心指标，几乎所有长期项目都适用。** 应尽量使用外部 oracle，不仅用 LLM judge。 |
| **Handoff Debt / Rediscovery Overhead，交接再发现成本** | 与同一 frozen state 下有完整可靠交接的 baseline 相比，额外 `agent events`、tool calls、prompt tokens、重复文件读取、重复测试或 wall time。可写成 `(handoff cost − oracle continuation cost)/oracle cost`。 | Handoff Debt 证明 context-bearing handoff 能降低 20–59% agent events、42–63% prompt tokens，是目前最直接的度量依据。citeturn15view0 | 特别适合 coding/research 等“旧工作可重新查，但代价很大”的任务。 |
| **Current-State Accuracy，当前状态正确率** | 对经过多次更新的 requirement/fact/decision，回答或行为究竟基于 `current`、`superseded` 还是 `other failure`；主要分数为 current/total，同时单报 stale-selection rate。 | StateMemBench 正采用 current/superseded/other closed-pool grading。citeturn18view3 | **需求会反复修改的长期项目必测。** |
| **FAMA / Obsolete-Memory Penalty，遗忘感知准确率** | 在普通 correctness 基础上，对输出中使用已撤销、已删除、已失效的 requirement/memory 扣分；同时报告普通 accuracy 与 FAMA 的 gap。 | Memora 提出的 FAMA 正是为解决普通 memory-presence accuracy 掩盖 obsolete-memory misuse。citeturn16view1 | 用户偏好、任务目标、架构决策、授权和规格会随时间改变时尤其重要。 |
| **Requirement / Constraint Retention，需求约束保持率** | 建立人工标注的 active-constraint set；验收时计算 `正确遵守的仍生效约束 / 所有仍生效约束`，再单报 `撤销约束误执行率`。精确措辞类要求可另计 exact fidelity。 | LongMemEval 的 knowledge update、MemoryAgentBench selective forgetting，以及 verbatim-vs-summary constraint probe 都说明“仍有效”和“已失效”必须分别评估。citeturn21view0turn21view2turn14view0 | 与 Mnemosyne 的 raw user requirements 最直接对应。 |
| **Source/Provenance Fidelity，来源忠实度** | 对需要引用历史依据的输出，检查每项关键 claim 是否能映射回 authoritative source span/commit/message；可报告 `supported claims / claims requiring provenance`，另计 verbatim-critical-field exact match。 | AgentMemBench公开使用 Faithfulness；Verbatim Chunks 表明 source-preserving representation 能避免 write-time information loss。citeturn16view0turn14view0 | 当“不能凭记忆改写用户原意”比自然语言流畅更重要时必测。 |
| **Retrieval Coverage，所需交接事实检索覆盖率** | 对每个 task 预标 required evidence，测 Recall@k；排序再用 MRR/nDCG@k。最好分 raw、decision、current-state、failure-history 四类 evidence。 | AgentMemBench 已标准化使用 Recall@k、MRR、nDCG@k；其结果也显示 retrieval strategy 差异很大。citeturn16view0 | 适用于使用搜索/index/RAG 的大型 Git/doc truth source。注意 retrieval 好不等于最后行为一定正确。 |
| **Fail-Closed Handoff Validity，交接拒收正确性** | 人工构造 `complete`、`missing-critical-field`、`stale`、`contradictory`、`wrong-project` handoff；计算 invalid case 的 true-reject rate 与 valid case 的 false-reject rate。可用 balanced accuracy/F1，避免“全部拒绝”刷分。 | LongMemEval 有 abstention；DreamBench-SWE 使用 validity gates/stale traps；StateMemBench明确区分 stale state。**“receiver report fail-closed”本身无现成标准 benchmark，故这是由相邻证据推导的候选。**citeturn21view0turn13view1turn18view3 | 对委托方现有 fail-closed 协议最重要；验收集必须包含故意损坏的交接包。 |
| **Useful Memory Precision / Context Pollution Rate** | `实际对完成任务有帮助的 loaded/retrieved memories / 所有 loaded/retrieved memories`；另计 irrelevant/stale/overscoped memory 注入率。 | DreamBench-SWE 报告 UsefulMemoryPrecision；其 reference typed pipeline 甚至只有 0.264，而 simple verbatim event baseline 为 0.556，证明“记得更多”可能反而是更差的 hygiene。citeturn15view3 | 当规则、memory 和 handoff package 已经变大时必测，可直接指导按需加载策略。 |
| **Efficiency per Successful Continuation，单位成功连续性的成本** | `tokens / successful continuation`、`tool events / success`、`wall-time / success`，而不是单独最低 token 数；可以附首次 handoff payload size。 | Handoff Debt 显示 raw trace 初始 prompt 很大，却可能因减少后续 rediscovery 而降低总 tokens；AgentMemBench同时报告 footprint/latency。citeturn14view3turn16view0 | 用于避免“摘要更短所以一定更好”这种错误优化。 |

在这组指标中，**“像同一个对话”的核心不是 raw recall，而是 performance retention**。一个可供后续方案自行选择的总体验收表达方式是：

`Continuity Retention = Cross-session performance / Same-session-oracle performance`

但该比率不能单独使用，因为一个系统可能最终做对，却浪费大量时间重新发现；也可能做对最终答案，却使用过期或未经授权的中间状态。因此至少应同时报告 **Continuation Success、Rediscovery Overhead、Current-State/Stale Error、Constraint Retention** 四个互补面。Handoff Debt、Memora、StateMemBench、MemoryArena 分别为这四个面提供了最直接的公开测量依据。citeturn15view0turn16view1turn18view3turn21view3

对于委托方特有的 raw/approved/handoff protocol，还可以设计一个与 DreamBench-SWE 类似的 adversarial evaluation fold：后续 session 所需的某些 requirement **故意不能从当前代码/文档表面重新推断**，只能从正确 handoff/source provenance 找到；另放入已经 superseded 的旧要求、错误摘要和缺字段 package。这样可以同时测 continuation、provenance、state freshness 与 fail-closed，而不是让“模型凭常识重新猜对”污染连续性分数。DreamBench-SWE 的 hidden non-inferable evidence 和 StateMemBench 的 adversarial revision 为这种测试设计提供了直接先例。citeturn13view1turn18view3

综合 2025H2–2026 的新证据，最值得纳入验收思维的变化是：**长期连续性的评测单位已经从“一个事实能否被回忆”升级为“一个有历史、有状态突变、有失败轨迹、有执行产物的工作能否由另一个 session/agent 以低再发现成本正确继续”。** MemoryArena、Handoff Debt、StateMemBench、DreamBench-SWE 和 Handoff Tax 共同构成了目前最接近这一目标的公开证据组。citeturn21view3turn15view0turn18view3turn13view1turn15view1

## 来源表

访问日期均为 **2026-08-31**。论文如同时有 HTML/摘要页，以下列 arXiv canonical URL；产品功能以官方文档为准。

| 编号 | 标题 | 类型 / 日期 | URL | 访问日期 |
|---|---|---|---|---|
| S01 | *Evaluating Very Long-Term Conversational Memory of LLM Agents*（LoCoMo） | 论文，2024-02 | https://arxiv.org/abs/2402.17753 | 2026-08-31 citeturn21view1 |
| S02 | *LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory* | ICLR 2025；v2 2025-03 | https://arxiv.org/abs/2410.10813 | 2026-08-31 citeturn21view0 |
| S03 | *Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory* | 系统作者论文，2025-04 | https://arxiv.org/abs/2504.19413 | 2026-08-31 citeturn18view0 |
| S04 | *Zep: A Temporal Knowledge Graph Architecture for Agent Memory* | 系统作者论文，2025-01 | https://arxiv.org/abs/2501.13956 | 2026-08-31 citeturn18view1 |
| S05 | *Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions*（MemoryAgentBench） | 论文，2025-07；v4 2026-06 | https://arxiv.org/abs/2507.05257 | 2026-08-31 citeturn21view2 |
| S06 | *MemoryArena: Benchmarking Agent Memory in Interdependent Multi-Session Agentic Tasks* | 论文，2026-02 | https://arxiv.org/abs/2602.16313 | 2026-08-31 citeturn21view3 |
| S07 | *AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications* | 论文，2026-02；v4 2026-05 | https://arxiv.org/abs/2602.22769 | 2026-08-31 citeturn18view2 |
| S08 | *From Recall to Forgetting: Benchmarking Long-Term Memory for Personalized Agents*（Memora/FAMA） | 论文，2026-04 | https://arxiv.org/abs/2604.20006 | 2026-08-31 citeturn16view1 |
| S09 | *AgentMemBench: A Systematic Benchmark for Evaluating Long-Term Memory Management Strategies in Conversational AI Agents* | 论文，2026-06 | https://arxiv.org/abs/2608.00009 | 2026-08-31 citeturn16view0 |
| S10 | *Can Agent Memory Systems Track Evolving State?*（StateMemBench） | 论文，2026-08-20 | https://arxiv.org/abs/2608.19652 | 2026-08-31 citeturn18view3 |
| S11 | *Handoff Debt: The Rediscovery Cost When Coding Agents Take Over Interrupted Tasks* | 论文，2026-06 | https://arxiv.org/abs/2606.02875 | 2026-08-31 citeturn13view0turn15view0 |
| S12 | *The Handoff Tax: Continuing Non-Native Trajectories in LLM Agents* | 论文，2026-08 | https://arxiv.org/abs/2608.24358 | 2026-08-31 citeturn13view2turn15view1turn15view2 |
| S13 | *DreamBench-SWE: A Multi-Session Memory-Hygiene Benchmark for Software Agents* | 论文，2026-08-21 | https://arxiv.org/abs/2608.20664 | 2026-08-31 citeturn13view1turn15view3 |
| S14 | *Verbatim Chunks Beat Extracted Artifacts: A Controlled Ablation of Memory Representations for Long LLM Conversations* | 论文，2026-01；v3 | https://arxiv.org/abs/2601.00821 | 2026-08-31 citeturn14view0 |
| S15 | Letta Docs — *Memory blocks (core memory)* | 官方框架文档 | https://docs.letta.com/v1-sdk/memory/memory-blocks | 2026-08-31 citeturn17view0 |
| S16 | LangGraph Docs — *Persistence* | 官方框架文档 | https://docs.langchain.com/oss/python/langgraph/persistence | 2026-08-31 citeturn17view1 |
| S17 | Claude Code Docs — *How Claude remembers your project* | 官方产品文档 | https://code.claude.com/docs/en/memory | 2026-08-31 citeturn19view3 |
| S18 | Claude Code Docs — *Common workflows* | 官方产品文档 | https://code.claude.com/docs/en/common-workflows | 2026-08-31 citeturn20view1 |
| S19 | OpenAI — *Memory FAQ* | 官方产品文档，2026-08 时有效 | https://help.openai.com/en/articles/8590148-memory-faq | 2026-08-31 citeturn19view1 |
| S20 | Anthropic — Claude Release Notes | 官方产品文档；2026-07 memory 改版 | https://support.claude.com/en/articles/12138966-release-notes | 2026-08-31 citeturn19view0 |
| S21 | Google — *Get personalization with memory of your past Gemini chats* | 官方产品文档 | https://support.google.com/gemini/answer/16598469 | 2026-08-31 citeturn19view2 |
| S22 | OpenAI Agents SDK — *Handoffs* | 官方开发文档 | https://openai.github.io/openai-agents-python/handoffs/ | 2026-08-31 citeturn20view0 |
| S23 | OpenAI Codex — *Developer commands*（`codex resume` / `fork`） | 官方开发文档 | https://learn.chatgpt.com/docs/developer-commands | 2026-08-31 citeturn20view2 |
| S24 | Microsoft — *AI Memory / Context Poisoning (Corruption)* | 官方安全文档，2026 | https://learn.microsoft.com/en-us/security/zero-trust/catalog-ai-attack-techniques/ai-memory-context-poisoning | 2026-08-31 citeturn20view3 |
| S25 | GitHub — *Spec Kit* | 官方开源项目 / spec-driven development | https://github.com/github/spec-kit | 2026-08-31 citeturn9search4 |