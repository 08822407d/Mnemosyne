# MNE-DR-028 / FABLE5-REDESIGN-001-RQ13 · 总体架构抽象模型复核

**研究范围：**公开资料；重点覆盖 2024–2026 年长期运行 LLM agent 的总体架构/组织抽象，并按任务书要求追溯 MemGPT、Soar/ACT-R 等必要前史。本文刻意不把“向量库、图、压缩、checkpoint”等单独的记忆机制当作答案，而关注它们在更高层架构中分别被赋予什么角色。

**证据标记：**【论文实证】表示有实验或基准结果；【论文架构/观点】表示论文主要贡献是架构、分类或论证；【厂商/官方文档】表示生产框架、标准机构或产品文档；【社区经验】仅表示工程实践观察，不能与实验实证等量齐观。本文所称“高/中/低”均是对公开证据的综合评价，不是已有论文直接给出的分数。

**核心研究结论先行：**公开证据并不支持把“LLM = 经典 CPU、上下文 = RAM、文件 = 硬盘”当作严格计算模型；但越来越多 2024–2026 文献仍然主动使用这组计算机系统类比，并把 **LLM 改称概率处理器、把模型外的确定性控制面/治理面、持久状态和审计记录设为一等公民**。与此同时，事件溯源、认知架构、黑板、数据库和 Git/文档中心都各自解决了原类比没有覆盖的一部分问题，没有一个纯模型同时在可替换性、审计、人类可读、并发、多年演化和低迁移成本上占优。公开先例最一致的方向不是“找到另一个万能比喻”，而是**分层：权威历史、当前态投影、工作态、上下文装载、概率计算、确定性治理相互分离**。这只是证据覆盖判断，不构成委托方最终架构裁决。citeturn20search1turn21search1turn17view0turn17view5turn18search0

## 候选总体抽象盘点

**Q1 · 2024–2026 年有哪些可竞争的总体抽象/参考架构？**

### 操作系统／修正冯诺依曼类比

这一谱系至少有两个不同层次，不能混为一谈。

第一种是 **“LLM 自己像 OS，负责虚拟化有限上下文”**。MemGPT 的直接灵感是经典 OS 的层次存储与虚拟内存：有限 LLM context 相当于快速层，外部存储相当于更大但更慢的层，通过显式的数据迁入/迁出以及 interrupts，让有限上下文产生类似“虚拟上下文”的效果。论文在长文档分析和多 session 对话两个场景中做了实验，报告其可以处理超过底层模型上下文限制的文档，并维持跨会话对话记忆。MemGPT 初稿是 2023 年，但 v2 修订于 2024-02，因此它更适合作为 2024–2026 OS 路线的直接前史，而不是把它误列为 2024 年首创。citeturn15search0turn15search4

第二种是 **“agent runtime 自己成为 OS/kernel”**。AIOS（2024，COLM 2025）把 scheduling、context management、memory、storage、access control 等从具体 agent application 中抽离进 AIOS kernel，并提供 SDK 接口；论文实验报告，对来自不同 agent framework 的 agent 服务时最高可达到约 **2.1× 执行加速**。这比 MemGPT 的“memory paging”更接近真正的操作系统参考架构：OS 不是记忆隐喻，而是多个 agent 与模型、工具、存储资源之间的资源管理和隔离层。citeturn17view3

2025 年的 ArbiterOS 又把重点从资源调度推进到治理：它直接画出“经典冯诺依曼机器 vs Agentic Computer”的对应关系，把 LLM 称作 **Probabilistic CPU**、context 称作 volatile RAM、外部工具称作 I/O，同时强调真正重要的是两边的“不相同”：概率执行、语义 ISA、不透明内部状态、不断变化的“硬件”和不可靠 context；其解决办法是让一个确定性的 Symbolic Governor 位于概率处理器之外。该文是 perspective/architecture paper，不是证明 ArbiterOS 优于其他架构的实证论文，但它是目前找到的、**最直接讨论本任务所问“CPU/RAM 类比到底哪里成立、哪里危险”的公开文献之一**。citeturn21search6turn21search1

2026 年的 Model-Native Computing Architecture 则明确提出问题：“LLM 是否像 CPU、KV cache 是否像 processor cache、context 是否像 main memory、agent framework 是否像 OS？”其结论并非简单肯定，而是提出六层 Intelligent Computing Architecture，以及“probabilistic execution plane / deterministic control plane”双平面。作者明确说明这是 conceptual/survey contribution，**没有新的实验结果**。这说明到 2026 年，“计算机体系结构类比”并未消失，反而正在从粗粒度比喻向“有边界的分层参考架构”演化。citeturn20search1

**证据判断：**OS 类比的采用度很高，但公开研究支持的是“借用 OS 的分层、隔离、资源管理、HAL、checkpoint 等思想”，不是“LLM 在计算语义上真的等同于 CPU”。MemGPT、AIOS、ArbiterOS、ICA 对“OS”一词本身甚至指向不同层：memory manager、agent kernel、governor、整个模型原生系统栈。因此项目若继续说“类冯诺依曼”，必须首先规定它只是**separation-of-concerns mental model**，还是准备把对应关系当成技术不变量。citeturn15search0turn17view3turn21search1turn20search1

### 认知架构类比

传统认知架构提供的是另一套问题分解方式：不是“计算机哪里是 CPU/RAM/disk”，而是“一个持续行动的认知体拥有哪些不同功能的记忆、行动和控制过程”。

Soar 的经典划分包括 working memory，以及长期 procedural、semantic、episodic memory；CoALA 对 Soar 历史的回顾同时指出，这类认知架构曾广泛应用于机器人、军事仿真、智能辅导等领域，但传统符号 AI 所需的大量预先定义规则、逻辑谓词表示等也限制了它后来在主流 AI 中的影响。citeturn17view4

ACT-R 是这一传统的另一个重要分支。CMU 官方 ACT-R 说明把知识区分为 declarative 与 procedural，两类 memory module 通过 buffers 暂时呈现当前活跃信息；它的主要目标原本是建立人类认知理论，而不是给 LLM agent 设计数据库。换言之，ACT-R/Soar 值得借的是**功能分型和工作区思想**，不能因名字同叫“memory”就把它直接当作持久存储方案。citeturn14search7

CoALA 将这种传统系统化移植到 LLM agent。其总体架构有三个主轴：modular memory、能够操作内部记忆与外部环境的 structured action space、以及 generalized decision process。特别重要的是，CoALA **并不把 working memory 等同于 raw LLM context**：其 working memory 可以是跨多次 LLM 调用持续存在的数据结构，每次模型调用只把其中一个子集组织进 prompt/context；长期部分再细分 episodic、semantic、procedural memory，而 procedural memory 既可能在模型参数中，也可能在显式 agent code 中。这个区分正好击中了“context = RAM”过度字面化的问题。citeturn17view4turn11view0

CoALA 的证据性质需要谨慎标注：它主要是**参考分类框架和 retrospective survey**，贡献是把已有 agent 工作放入统一认知架构，而不是实验比较“CoALA 系统 vs OS 系统”然后证明前者长期性能更高。因此它对“概念是否清楚”有较强支持，对“这就是长期项目最优持久化总体架构”则没有直接实证。其论文还指出删除、修改、unlearning 等长期记忆操作相对研究不足，这一点对于跨年项目尤其关键。citeturn15search1turn17view4turn11view1

**优势：**语言上比 CPU/RAM/disk 更贴合“经验、事实、规则、当前思考”的功能差异，也天然提醒设计者“规则/技能”和“事实/事件”不是同一种长期信息。  
**主要缺口：**认知分类本身没有给出权威记录、并发写入、事务、审计、版本迁移、owner 授权的完整工程语义；因此它更像**上层信息模型**，而不是单独足够的 durable systems substrate。该判断是基于 CoALA 的职责范围做出的架构推论，而非 CoALA 作者的负面结论。citeturn17view4

### 事件溯源／账本模型

事件溯源的核心问题不是“我现在记得什么”，而是“**到底发生过什么，以及当前状态如何从这些事实派生出来**”。

微软 Azure Architecture Center 对成熟 Event Sourcing pattern 的定义非常直接：所有改变以 append-only event 记录，event store 是 system of record；当前业务对象通过 replay/rehydration 得到。因为每次从头 replay 成本高，实际系统通常另外维护 materialized views，并经常结合 CQRS，让写侧的权威历史和读侧的查询优化投影分开。这样天然提供事件历史、审计、状态重建、optimistic concurrency 等能力。citeturn17view0

这不是 LLM 专属的新发明。真正新的，是 2026 年已有研究开始把它提升成 agent 的**总体组织抽象**。ActiveGraph 的论文题目就是 *The Log is the Agent*：append-only event log 是 source of truth，working graph 只是从 log 做出的 deterministic projection；规则、工具调用、LLM 调用、产物及关系都成为事件。论文还增加 caused-by/provenance，并把 LLM/tool 返回值记入 content-addressed cache，使**对已经发生的运行**可以在 replay 时不重新调用模型，从而得到 byte-reproducible replay。这里必须强调：这并没有让新的 LLM 推理变成确定性的；确定的是“把历史中的非确定结果作为既成事件重新播放”。citeturn17view5

ActiveGraph 作者也非常明确地限制了证据强度：这是 systems/architecture paper，不报告相对 baseline 的任务准确率提升；论文给出了可复现 worked example、lineage、fork/diff 等架构能力，但明确“不声称证明”自我改进或任务性能优势。因此当前可以说“event-sourced agent 已有直接公开实现和架构论证”，不能说“实证已经证明它是最佳 agent architecture”。citeturn17view5

成熟 Event Sourcing 文献反过来也把代价写得很清楚：模式复杂；迁入迁出昂贵；projection 会引入 eventual consistency；多线程/多实例时事件顺序至关重要；event stream 本身不像 SQL 那样好查询；长历史需要 snapshots/materialized views，否则 replay 成本上升。微软甚至明确提醒，多数系统或多数系统部件使用传统数据管理已经足够。citeturn17view0

因此该模型在本项目中的独特价值不在“又一个记忆库”，而在它重新定义了 **truth**：

> authoritative truth = 不可覆盖的历史；  
> current truth = 从历史生成、可重建的当前投影。

这与“某个 Markdown 文件的最新内容就是唯一长期真相”在语义上差异很大。前者把修改也当事实保存；后者通常把当前文档作为主对象，Git history 作为它的版本历史。这两者可以组合，但不能视为同一个模型。citeturn17view0turn17view5

### 黑板模型

黑板（blackboard）架构将系统的中心从“单个 agent 的记忆”转向**所有参与者可读写的共享工作空间**。不同专家/agent 观察黑板当前状态，按能力或触发条件加入部分结果，其他 agent 再在其上继续、质疑或完善。

这在 2025–2026 已有直接 LLM 多 agent 实证。Google 等作者的 *LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science* 让 central agent 在共享 blackboard 上发布请求，各 subordinate agent 根据自身能力主动响应，不要求中央调度器预先知道所有专家能力。它在 KramaBench、修改版 DSBench 和 DA-Code 上报告相对最佳 baseline **13%–57% 的 end-to-end success 相对提升**，以及最高约 **9% 的 data-discovery F1 相对提升**。citeturn16search0turn17view6turn16search24

这是本次候选中少数拥有直接多-agent benchmark 的抽象。但它验证的是**信息发现和协同调度**，不是多年人机项目中的长期真相、审计和模型迁移。因此不能把“blackboard 在某组协同任务上有效”外推为“blackboard 最适合作长期 system of record”。citeturn17view6

其结构性强项是“当前共享态”：参与者不必逐对传消息，也不用单一 master 理解每个 agent。结构性弱点则是：**blackboard 告诉你大家现在看到了什么，却不自动回答为什么它变成这样、哪个历史版本是权威、冲突如何解决。** 若加入 append-only history/provenance，黑板就已经开始向事件溯源＋projection 的混合架构靠近。这一点是对 blackboard 与 event-sourced system 定义的比较推论。citeturn17view6turn17view5

### 数据库中心模型

“数据库中心”其实有两种含义。

较窄含义是 **数据库作为 agent memory substrate**。2026 年已有研究把 long-running agent memory 明确视为 data-management workload；也有工业产品把工作状态、长期事实、procedural memory 或 workflow state 放入数据库。LangGraph 官方把 persistence 分成两个互补系统：checkpointer 保存 thread/graph 的短期执行状态，store 保存跨 thread 的长期信息；DBOS 则更彻底，让 database 同时成为 workflow execution state 的 source of truth 和 crash recovery mechanism。citeturn18search0turn18search1turn18search5

数据库作为生产底座有明显工程优势：并发、索引、查询、约束、耐久性、事务和恢复都已有成熟工具链。但“数据库”并不是单一信息模型。关系、向量、图、时态数据库分别优化不同操作，而 agent 的“长期记忆正确性”可能要求的是整个状态演化，而非单条 record 是否 ACID。2026 年论文 *Is Agent Memory a Database?* 正是对此提出反例：作者认为现有数据库范式和多数 agent-memory family 都只覆盖所需能力的一部分，提出 Governed Evolving Memory，把 ingestion、revision、forgetting、retrieval 作为**状态层运算**，并明确写出其结论：“agent memory 是新的 data-management workload”，而不是把 CRUD 数据库本身当完整答案。citeturn16search1turn16search13

因此“database-centered”最强的解释是 **database as substrate**，而不是“数据库模式本身就是整个 agent 的认知/治理模型”。DBOS 是很好的反例：数据库保证执行状态和恢复，但上层仍然需要 workflow、tool、model、human approval 等语义。citeturn18search5turn18search9

厂商研究也显示这条路线仍在快速发展。例如 Oracle 在 2026-08 明确主张 agent memory 是 data-management problem，并把 working、long-term factual、procedural memory 放在数据库管理生命周期下。这是厂商架构立场，应与上述论文对“纯数据库抽象”的批判分开读取，而不能视为学界共识。citeturn16search29

### Git／文件／文档中心模型

这是与 Mnemosyne 当前形态最接近的一组证据，而且 2025–2026 明显增多。

【论文实证】Git Context Controller（GCC）把 agent context 组织为类似 Git 的 COMMIT / BRANCH / MERGE 结构，让 reasoning artifacts 成为持久、可解释、可分叉的对象。论文在 SWE-Bench-Lite 上报告 48.00% resolved bugs，并称超过所比较的 26 个系统；在一个 self-replication CLI 案例中，GCC augmented agent 得到 40.7% task resolution，而不使用 GCC 的版本为 11.7%。这至少说明：**结构化、版本化、可分支的文件/历史上下文并不只是一个方便人看的界面，能够在某些长程 coding workload 中改善 agent 表现。**但证据领域仍是软件工程，不能直接外推到所有长期协作。citeturn17view1turn18search27

【厂商文档】Anthropic 的 Claude Code 已把 plain-text project artifacts 做成正式产品接口。官方文档说明，每个 session 从新的 context window 开始；`CLAUDE.md` 提供持久项目指令，项目级文件可以通过 source control 与团队共享；`.claude` 中的 skills、subagents 等也可跟随项目进入版本控制。这显示“repository/files as durable interface”已经不是边缘实践。citeturn19search10turn19search3turn19search7turn19search17

但同一份 Anthropic 文档提供了一个关键反证：`CLAUDE.md` **只是被送进模型的 context，不是强制配置**；模型不保证严格服从，若需要真正阻断某动作，应使用 PreToolUse hook 等外部机制。这正说明“规则文件像程序”若理解成“模型读取了文件，因此规则具有机器指令的强制语义”，是不成立的。citeturn19search0turn19search10

Letta 的演化尤其值得注意：MemGPT 项目本身起源于 2023 年 LLM-as-OS/virtual context 思路，而 Letta 在 2026-02 又推出 **Context Repositories: Git-based Memory**，将 agent context 保存到本地 filesystem，并使用 Git-based versioning 和程序化 context management。也就是说，“OS 类比”和“Git 文件中心”并不是互斥的竞争哲学；同一研究/产品谱系已经出现从 OS-inspired memory management 到 Git-backed context interface 的组合。citeturn18search3turn18search11turn18search15

【社区经验】社区中确实可以找到“复杂 agent memory 最后回到 Git/文本文件”的经验帖子，赞赏其透明性、audit trail 和 temporal context；但这是个体经验和评论，不是受控研究，最多只能证明“这种工程偏好真实存在”，不能用来推导性能或可靠性结论。citeturn18search35

文件/Git 模型最容易被过度推论的地方，是把 **“Git 能保留文件版本历史”** 等同于 **“最新文件天然具有一致、并发、安全的单一真相语义”**。Git 很擅长人类可读 artifact、diff、review、branch/merge 和 portability，但高频并发 current state、查询和机器约束不是普通 Markdown/Git 的主要强项；而且随着 repository 增大，agent 仍然需要选择性装载，Anthropic 的大代码库文档也明确提醒，过多无关 instructions/file reads 会占满 context 并降低性能。citeturn19search13

### 候选抽象的证据状态

| 候选 | 核心中心对象 | 代表先例 | 当前最强证据 | 主要已知缺口 |
|---|---|---|---|---|
| OS／修正冯诺依曼 | kernel、层次资源、计算/存储边界 | MemGPT、AIOS、ArbiterOS、ICA | MemGPT 长上下文实验；AIOS 最高 2.1× serving speedup citeturn15search0turn17view3 | 类比若字面化会把概率处理器/context 错当经典 CPU/RAM；并不自然定义业务 truth |
| 认知架构 | working / episodic / semantic / procedural memory + action/control | Soar、ACT-R、CoALA | 强历史理论基础；CoALA 系统化整理 LLM agents citeturn14search7turn17view4 | 工程上的事务、审计、authority、并发写入未由分类本身解决 |
| 事件溯源／账本 | append-only event history | Azure ES/CQRS、ActiveGraph | 企业架构模式成熟；ActiveGraph 已直接 agent 化 citeturn17view0turn17view5 | 复杂、projection eventual consistency、schema/version/replay 成本 |
| 黑板 | shared current workspace | Google blackboard MAS | 数据发现任务相对成功率 +13%–57% citeturn17view6 | 长期权威历史和冲突语义不是默认能力 |
| 数据库中心 | persistent structured state | DBOS、LangGraph persistence、数据库型 agent memory | 生产 durable execution 和查询/并发基础强 citeturn18search0turn18search5 | “数据库 = memory/system ontology”过窄；状态演化治理仍需上层抽象 citeturn16search1 |
| Git／文档中心 | human-readable versioned artifacts | GCC、Claude Code、Letta Context Repositories | GCC 有 coding 实验；多家产品正式采用 file/repo interface citeturn17view1turn19search3turn18search3 | 高并发 current state、查询、强约束、强制授权不是普通文件/Git 默认能力 |

**UNKNOWN：**截至 2026-08-31，本次公开检索没有找到一个同行评审的 head-to-head study，用同一套多年人机协作 workload 同时比较上述六类总体架构，更没有针对“一个人类 owner、多厂商可替换模型、连续多年使用”给出统一 benchmark。因此后文的跨候选评分属于**证据综合与架构推论**，不是已有实验证明的总排名。citeturn20search1turn17view5

## 冯诺依曼类比的适配性批判

**Q2 · “模型像 CPU、context 像 RAM、Git 像硬盘、规则像程序、交接包像进程快照”哪些成立，哪些误导？**

最重要的复核结果是：**“类冯诺依曼”并不是一个已经被文献否定的坏比喻；恰恰相反，2025–2026 仍有论文主动采用它。但严肃文献越来越倾向把类比的价值放在“找出差异、规定边界”，而非一比一同构。** ArbiterOS 明确说，这个 mental model 真正的效用在于暴露经典计算机和 Agentic Computer 的 stark divergences；ICA 也把“类比边界和验证仍是开放问题”写进研究议程。citeturn21search1turn20search1

### 模型像 CPU：接口纪律可以成立，计算语义不能照搬

经典 CPU 的基本工程预期是可重复执行明确 instruction semantics。LLM 则是概率生成系统；CoALA形式上把语言模型描述成条件概率分布，而 ArbiterOS 直接以 **Probabilistic CPU** 区分于 deterministic CPU。即使固定 prompt，生成结果也不能被当作普通机器指令那样具有严格 deterministic semantics；模型升级还可能改变同一 prompt 的行为。citeturn17view4turn21search1

不过“模型 = 可替换 compute unit”仍然有强烈工程价值，只要把它定义为**接口抽象**。ArbiterOS 对“Non-Stationary Hardware”的处理正是 HAL：durable logic 不应耦合具体模型版本；ICA 也使用 probabilistic execution plane 与 deterministic control plane 分离。这与 Mnemosyne 希望不同供应商/不同代模型可替换的目标高度一致。citeturn21search1turn20search1

因此，更准确的表达不是：

> Model = CPU.

而是：

> Model = **可替换、概率性的语义计算后端**；稳定 contract、policy、truth 和 recovery state 应在模型之外。

“无状态”也要分两层理解。CoALA 指出基础 LM 本身在多次调用之间并不天然保存 agent state；这支持把“stateless model call”作为架构接口纪律。可是完整产品或 agent runtime 可以在模型外维护 conversation、cache、tools、memory，因此“整个模型服务天然无状态”并不是普遍事实。citeturn11view0

### Context 像 RAM：这是当前类比中最容易造成系统设计误判的一项

经典 RAM 具有地址化、明确读写和稳定数据语义；一个字节不会因为被放在地址空间中央而“比较难被 CPU 看见”。

LLM context 不具备这种性质。2024 年 TACL 论文 *Lost in the Middle* 在 multi-document QA 和 key-value retrieval 中发现，只改变相关信息在长 context 中的位置，就会显著改变模型使用该信息的能力；典型情况是开头或结尾表现更好，中间位置明显下降。它直接反驳了“只要东西在 context 里，就类似数据已装入 RAM、因此可以可靠读取”的隐含假设。citeturn14search6turn14search2

ArbiterOS 将这一点称作 context memory 的 **attention variance**，并进一步指出 summarization/eviction 本身也是概率认知操作：模型可能在压缩中静默丢失关键状态。citeturn21search1

CoALA 提供了一个更精确的术语修补：**working memory ≠ context window**。working memory 可以是模型外持久、结构化的当前状态；每次 inference 前只把当前任务需要的部分从 working memory 编译/synthesize 到 model input。citeturn11view0

因此 Mnemosyne 若继续使用 RAM 比喻，建议在设计层面至少把两个概念分开：

**Working state** 是系统管理的、可地址化/可审计的当前态；  
**Context** 是从 working state、历史、文档、规则中临时编译出的**有限注意力工作集**。

后一句是本报告基于 CoALA、Lost-in-the-Middle 和现有 context-management 文献作出的综合抽象，不是某一论文原句。citeturn11view0turn14search6

### KV cache 更不能被当作“系统记忆缓存”

KV cache 确实叫 cache，但它缓存的是 Transformer autoregressive decoding 中已经计算的 key/value tensors，用于避免为先前 token 反复重算，从而降低推理延迟；其存储占用随 context length 增长，当前大量系统工作讨论的是 eviction、compression、offloading 和 placement。citeturn20search3turn20search15

所以：

> context = 输入 token/语义工作集；  
> KV cache = 由这段输入计算出的**推理加速中间状态**。

KV cache 并不是“owner 可以放入一个项目事实并永久读取”的语义 memory，也不是文件/数据库 cache 的同义物。把它引入 Mnemosyne 的“记忆层级图”反而可能混淆 application state 与 inference implementation。citeturn20search3

### “规则像程序、数据像数据”：在 prompt injection 现实下没有硬件级隔离

这可能是原类比中安全含义最危险的部分。

经典体系结构至少在执行语义上知道什么是 instruction、什么是普通数据。LLM 的输入最终都成为 token；自然语言数据中的恶意文本可能被模型解释成新指令。2024 年 StruQ 正是因为这种问题，才提出特殊的 prompt/data channels 和经过相应训练的模型；论文在其攻击评估中把多类手工 prompt injection 成功率压至很低，但前提恰恰是**额外构造结构化隔离，而不是假定普通 LLM 天然拥有 instruction/data boundary**。citeturn20search6turn20search30

另一个专门研究 instruction-data separation 的工作直接报告：多种 LLM 都难以达到可靠的 instruction/data separation，常规 prompt engineering 或 fine-tuning 也不能简单消除问题。2025 年 SecAlign 同样把 prompt injection 的根因表述为模型难以区分 trusted instruction 与 untrusted data。citeturn20search14turn20search26

Anthropic 自己的 Claude Code 文档提供了生产系统层面的同样结论：`CLAUDE.md` 是 context，不是强制配置；若一个行为必须阻止，使用外部 hook，而不是只依赖模型“遵守文件”。citeturn19search0turn19search10

因此：

**“规则文件像程序”适合作为项目组织隐喻；不适合作为 authorization guarantee。**

真正的程序/政策边界必须至少在关键操作上由模型外的 deterministic mechanism 执行，例如 typed tool interface、permissions、hooks、policy gate 或 governor。NIST AI RMF 也要求组织识别哪些能力需要 human oversight，并建立相应 oversight practice，而不是把监督只写成模型可见的文本。citeturn22search10

### Git 文件像硬盘：耐久性成立，“唯一真相”是治理政策而不是文件系统自然属性

把长期信息从模型/context 外置是目前几乎所有长期 agent 架构的共同点；MemGPT、CoALA、LangGraph、DBOS、GCC、Letta 都以不同形式这样做。因此“不要把长期真相留在模型脑内或单次对话”这个原则有很强的跨架构支持。citeturn15search0turn17view4turn18search0turn17view1turn18search3

Git/plain text 又额外提供三项本项目很重视的性质：人可直接检查、可 diff/version-control、容易从一种模型工具迁到另一种工具。GCC、Claude Code 和 Letta Context Repositories 都提供了近年的直接先例。citeturn17view1turn19search3turn18search3

但“文件是唯一真相源”不是由 Git 自动证明的性质。它是项目施加的 **authority rule**：哪些文件是 canonical、谁可写、冲突怎样处理、被替代信息是否保留、派生 index 是否可以反写，都仍需架构规定。Event Sourcing 的对照尤其清楚：event log 把“发生过什么”设为权威，而最新文档只会是一个 projection；Git 模型则通常以当前文件树作为主要工作对象、历史 commit 保存演化。两者语义不同。citeturn17view0turn17view5

### “交接包像进程快照”：作为应用 checkpoint 成立，作为完整 machine snapshot 不成立

真实 OS process snapshot/checkpoint 的理想含义，是恢复足够多机器状态后继续同一计算。对于 LLM agent，模型的专有服务状态、sampling、模型版本、KV tensors、外部工具世界状态等未必能装进一个可移植 handoff 文件。

长时 workflow 系统的工程实践因此不是声称捕获“整个 LLM 进程”，而是保存**显式可恢复状态和事件历史**。LangGraph checkpointer 保存 graph state；Temporal 记录 workflow history 并通过 replay 恢复 deterministic orchestration；ActiveGraph 甚至把实际 model/tool responses 也保存下来，避免 replay 时重新执行非确定调用。citeturn18search0turn22search13turn17view5

因此“handoff package = snapshot”可以保留，但更精确的名称应该理解为：

> **portable application checkpoint / rehydration manifest**，

而不是“完整捕获模型内部计算进程”。

### 适配性总表

| 原类比 | 复核结论 | 仍可保留的价值 | 必须纠正的地方 |
|---|---|---|---|
| 模型 = CPU | **部分成立** | 模型接口抽象、替换、资源调度 | 改成 probabilistic/semantic processor；升级需 re-verification citeturn21search1 |
| Context = RAM | **强烈需要修正** | 都属于运行期有限工作集 | context 非随机访问、位置敏感；working state 应与 prompt context 分开 citeturn14search6turn11view0 |
| KV cache = cache | **只能在推理实现层成立** | 性能优化类比 | 不是 application knowledge/memory citeturn20search3 |
| 规则文件 = 程序 | **组织意义成立，执行意义不足** | 人类可读 policy/config | 模型看到规则不等于强制执行；instruction/data 无硬隔离 citeturn20search14turn19search0 |
| Git 文件 = 硬盘/长期真相 | **耐久与可审计成立** | portable、reviewable、versioned | “canonical truth”需治理约定；并发、projection、索引另议 citeturn17view1turn19search3 |
| handoff = process snapshot | **应用层成立，物理层不成立** | restart/迁移 checkpoint | 应保存显式状态、版本、provenance；不能假定恢复模型内部隐藏状态 citeturn17view5turn22search13 |

**Q2 结论：**原模型最大的价值不是硬件拟真，而是**强迫系统把概率计算、有限运行上下文、持久状态和执行规则分开**。最大的风险则是词语太熟悉，容易让设计者误以为拥有经典 CPU/RAM 所具备的确定性、寻址性和 instruction/data boundary。公开文献直接支持的修正方向是“Probabilistic Processor + Deterministic Control/Governance + Explicit Durable State”，而不是放弃所有计算机系统抽象。citeturn21search1turn20search1

## 人机长期协作的特殊要求

**Q3 · “一个人类 owner＋多家可替换模型＋跨年工作”比纯自动 agent 多了什么？**

自动 benchmark 中一个 agent 做完任务即可结束；Mnemosyne 类场景却有一个非常不同的生命周期：**人的认知、模型代际、规则和项目本身都可能在系统寿命内发生变化。**这使几个在短期 agent 中可作为“实现细节”的问题，上升为总体架构要求。

### 人类 owner 需要外部化，但又不能把认知主权交给外部记忆

认知科学长期将 cognitive offloading 定义为使用外部工具减少内部记忆/处理负荷。有关 external memory 的研究显示这种策略非常有效，但是否 offload、信任什么外部表示，本身受人的 metacognitive judgment 影响；近年的 AI 讨论又特别关注过度依赖可能把“信息检索外包”升级为“形成信念也外包”。citeturn14search1turn22academia38turn22search3

对长期 owner 而言，这意味着 archive 仅仅“机器能检索”不够。至少有一层状态必须做到：

**可发现、可浏览、可阅读、可修订、能说明来源和当前有效性。**

这正是纯向量 memory 很难单独提供、而文档/Git 与 event-derived human-readable projection 擅长的部分。这个需求是从 human cognitive offloading 文献与上述架构能力综合推导出的。citeturn17view1turn17view0

### 授权边界必须属于 owner，而不是属于“当前最聪明的模型”

纯 autonomous agent 可以把更多决策交给 agent policy；owner-centered 系统则需要回答：“谁有权修改 canonical rule？哪个动作需要人批准？模型自己写入的记忆是否自动成为 truth？”

NIST 的 AI RMF playbook 要求识别需要 human oversight 的系统能力并建立对应监督实践；Temporal 到 2026 年已把 human-in-the-loop 作为 durable workflow 的正式模式，可以等待审批小时、天甚至无限期，approval/timer 都写进 durable history。citeturn22search10turn22search1turn22search9

Anthropic 对 `CLAUDE.md` 和 hooks 的区分进一步表明：**owner 意图应该有“说明给模型看”的层和“模型不能绕过”的层。**前者适合 Markdown/rules；后者需要 deterministic enforcement。citeturn19search10turn19search16

因此在本场景中，“授权”不只是 agent prompt 的一个字段，而应该成为总体架构中与 memory/truth 同等级的一条轴。

### 模型换代不是普通 CPU 热插拔，而更接近不完全兼容的计算后端迁移

长期项目很可能经历多个模型世代。ArbiterOS 把这一点称为 **Non-Stationary Hardware**，主张用 HAL 使 durable logic 与具体模型解绑，并对新模型持续 re-verification。这个比“CPU 可替换”更符合现实：物理 CPU 换成兼容型号通常不要求重新解释每条业务规则，而 LLM 更换后，同一自然语言 policy、tool description、context ordering 的行为可能变化。citeturn21search1

因此长期可迁移 artifact 更应该是：

**typed state、plain-text facts/rules、event/provenance records、tool contracts、tests/evaluations、version metadata**

而不是依赖某一供应商会话内部的隐含记忆。Git/filesystem 路线近期受到重视，与这种可移植性要求高度吻合；Letta 从 MemGPT 演化到 Git-based Context Repositories 也是一个值得注意的产业信号。citeturn18search3turn19search3

**UNKNOWN：**目前没有公开多年纵向实验能够量化“同一长期项目连续跨 GPT/Claude/Gemini/开源模型世代迁移时，哪种总体抽象保真度最高”。现有证据主要是架构原则和产品实践，而不是多年 controlled trial。

### 多写入方会把“记忆”变成并发和 provenance 问题

一旦 writer 不只是一个模型，而是 owner、模型 A、模型 B、subagent、自动化任务乃至未来脚本，系统就必须回答：

谁写的？  
依据什么写的？  
是在看到哪个版本之后写的？  
两个同时修改如何合并？  
错误修改如何撤销但不抹掉历史？

这正是 Event Sourcing/CQRS 已经形成成熟工程语义的问题：ordered streams、optimistic concurrency、immutable history、compensating events；而微软文档也明确指出多线程/多实例环境中 event ordering 是关键难点。citeturn17view0

Git 对较低频、人类审阅型并行修改也很合适，因为 branch/merge/diff 本来就是其核心模型，GCC 正是把这套操作迁入 agent context。citeturn17view1turn18search27

这意味着在 Mnemosyne 场景中，“谁能写什么”比“能不能检索这条记忆”更接近总体架构层问题。

### 跨年运行要求“状态版本化”，不仅是“数据备份”

多年系统会同时面临两类变化：

一类是**数据变化**：事实、目标、决策更新；  
另一类是**解释数据的程序/规则变化**：workflow、schema、policy、tool contract、projection logic 更新。

Temporal 的 production model 很能说明第二类难题：长-running workflow 甚至可以持续数月或数年，所以 workflow code 修改必须考虑 replay compatibility；官方提供 Worker Versioning/Patching，让旧 execution 继续旧语义，新 execution 使用新代码。citeturn22search35turn22search4

这对“规则文件像程序”的 Mnemosyne 尤其重要：**保存旧规则文件的 Git commit 只是第一步；还需要知道某个历史行为当时适用的是哪一版规则/模型/tool contract。** Event provenance、version binding 或 manifest 才能把“历史文件存在”提升为“历史行为可解释”。

### 哪个候选覆盖这种特殊场景最好？

若坚持只比较**纯单一候选**，公开证据显示没有明显全胜者：

- **OS/修正冯诺依曼**最自然地处理模型替换、runtime、policy boundary 和工作态，但不天然定义长期历史 truth。citeturn17view3turn21search1
- **认知架构**最自然地表达“当前思考、事件经验、事实知识、规则技能”不同性质，但最缺少审计/并发/authority 工程语义。citeturn17view4
- **事件溯源**最强地覆盖 provenance、多人写入、时间演化和重建，但人直接阅读和高效当前查询需要额外 projection。citeturn17view0turn17view5
- **黑板**最适合共享当前工作空间和多 agent 协调，但历史/owner authority 不是其核心。citeturn17view6
- **数据库中心**最强于并发 current state、查询和 durability，但“数据库中的某条 record”不自动说明其长期认知/治理含义。citeturn16search1turn18search5
- **Git/文档中心**在模型可替换、人可读、owner review 和现状兼容性上特别强，但作为高频多 writer runtime state substrate 有明显结构性缺口。citeturn17view1turn19search3

因此，对“哪个覆盖最好”的证据化回答是：

**没有单一纯候选覆盖最好；若把“候选”允许扩展为分层参考架构，则“事件/账本作为历史权威＋人可读 Git/文档作为受治理投影＋显式 working/checkpoint state＋模型抽象层”对 Q3 要求的覆盖最完整。**

这是对现有先例的**综合推论**，不是已有论文的胜负结论，也不是本文替委托方做出的最终设计裁决。其主要缺点正是 Q4 的复杂度和一致性成本。citeturn17view0turn17view5turn18search0turn18search3turn21search1

## 混合与分层的先例

**Q4 · 是否已有“账本层＋投影层＋工作记忆层”一类成熟组合？**

答案是明确的 **有**，而且成熟度最高的组合先例反而来自 agent 之外的 durable systems；LLM agent 框架正在重新发现相同结构。

### Event log ＋ materialized projection 已是成熟模式

Event Sourcing 与 CQRS 就是最直接的先例：

`append-only authoritative events`
→ `projection/materialized view`
→ `query/current state`

微软官方文档明确指出，因为每次 replay 全历史成本高，event-sourced application 通常建立 materialized views，且 Event Sourcing 常与 CQRS 配合，将 write model/system-of-record 与 query-optimized read model 分开；进一步还可用 snapshot 减少全量 replay。citeturn17view0turn16search7

这与“账本层＋投影层”几乎完全对应，只是其起源是企业软件而不是 LLM memory。

### ActiveGraph 已把同一结构直接 agent 化

ActiveGraph 的对应关系是：

`append-only event log`
→ deterministic replay
→ `working graph`
→ reactive behaviors
→ 新 events。

而且 model/tool response 也作为已经发生的事实保存，因此可 replay、fork、diff，并追踪 goal 到 artifact 再到具体 model call 的 lineage。citeturn17view5

这里的 working graph 本质上已经是一个**可丢弃再重建的当前态 projection**。因此“长期 authoritative history 和 agent 当前工作状态不要是同一个物件”已经有明确 LLM-specific precedent。citeturn17view5

### LangGraph 已把 checkpoint 与 long-term store 分成两层

LangGraph 官方 persistence 则提供另一种分层：

`checkpointer` → thread 内 graph-state snapshots / 短期执行连续性；  
`store` → 跨 thread 的长期信息。

官方文档明确把两者称作 complementary persistence systems，而不是用一个 memory object 同时承担运行恢复和长期知识。citeturn18search0turn18search16

这不是 event sourcing 的完整语义，却很好地证明了“**当前执行态 ≠ 长期记忆**”在主流 agent framework 中已成为正式设计。

### Durable workflow 又增加了“历史＋代码版本＋人类事件”

Temporal 的总体抽象进一步表明长期 process 必须同时管理 event history、deterministic orchestration、non-deterministic activities、人类 signals 和 code versioning。2026 年其 AI 文档明确覆盖 long-running stateful agent loops、LLM/tool calls、human waits 和 failure recovery；human approval 可以作为 durable event 持续等待，而 workflow 定义升级有单独 versioning 机制。citeturn22search5turn22search1turn22search35

这对于“handoff package”特别有启发：成熟 durable execution 往往不依赖一个巨大的全量 snapshot，而依赖**历史＋有限 checkpoint＋可重放控制逻辑＋外部副作用记录**。

### Git 文件作为上层投影、数据库作为底层 substrate 也已有产品趋势

LangGraph 可以把 checkpointer/store 落在持久数据库；DBOS 直接让数据库承担 execution truth；同时 Claude Code、GCC、Letta 又让 agent 的上层长期接口保持 Markdown/repository 形态。citeturn18search0turn18search5turn19search3turn17view1turn18search3

这说明一个很重要的架构事实：

**“文件还是数据库？”往往是错误的单选题。**

文件可以是 owner-facing canonical/control interface；数据库可以是 transactional runtime substrate；event log 可以是历史 provenance；materialized Markdown/JSON/SQL view 可以分别服务人和机器。现有系统模式允许这些层共存。这个结论是对上述产品与架构模式的综合，而非声称任何一家厂商已经实现了本文完整组合。citeturn17view0turn18search0turn18search3

### 一个从公开先例抽出的分层骨架

以下不是对 Mnemosyne 的最终方案，而是将上述已有架构的共同结构归纳为一个**待设计阶段验证的参考骨架**：

```text
人类 Owner / 其他 Writer
          │
          ▼
  Authority / Policy Gate
          │
          ▼
┌──────────────────────────┐
│ Authoritative History    │  append-only events / provenance
└──────────────────────────┘
          │
          ├──────────────► Human-readable projections
          │                Git / Markdown / decision records
          │
          └──────────────► Machine projections
                           DB / index / graph / current state
                                  │
                                  ▼
                         Working State / Checkpoint
                                  │
                                  ▼
                         Context Compiler / Loader
                                  │
                                  ▼
                       Probabilistic Model Adapter
                      model A / model B / future model
                                  │
                                  ▼
                         deterministic tool gates
```

其中 Event Sourcing 支持前两层的“历史→projection”；LangGraph/Temporal 支持 checkpoint/workflow 层；CoALA 支持“working memory 不等于 raw context”的概念分离；ArbiterOS/ICA 支持概率执行与确定性控制分离；GCC/Claude/Letta 支持 Git/plain-text 成为 owner/agent 可共同操作的上层 artifact。citeturn17view0turn18search0turn11view0turn21search1turn20search1turn17view1

### 组合的代价有明确证据，不应低估

第一是**一致性复杂度**。一旦 log 和 projection 分离，projection 通常只能 eventual consistency；需要定义 lag、失败恢复、projection rebuild。citeturn17view0

第二是**schema/version evolution**。几十万事件之后改变 event schema、projection code、workflow logic 都比直接编辑一个当前态文档复杂；Event Sourcing 官方文档明确把 schema evolution 和 migration 成本列为重大 trade-off，而 Temporal 需要专门 versioning/patching 才能保证长运行 workflow 的 replay compatibility。citeturn17view0turn22search35

第三是**查询和加载复杂度**。原始事件流不适合所有查询，需要 read models、indexes、snapshots；这意味着系统中“真相只有一份”与“物理表示只有一份”必须区分。多个 projection 可以存在，但 authority 必须清楚。citeturn17view0

第四是**双写/多写风险**。如果既允许人直接编辑 projection，又允许事件系统把 projection 重建出来，就必须规定哪一个方向有写权，否则会形成 two sources of truth。这个问题是从 Event Sourcing 的 authoritative-store 约束推导出来的，并非某个 agent 框架已经替 Mnemosyne 自动解决。citeturn17view0

第五是**认知复杂度**。简单 Git repository 的一个优势恰恰是 owner 可以理解整个模型；引入 log、projection engine、DB、checkpointer、policy gate 后，即使机器可审计性提高，人可能更难掌握系统。对于“一个人长期维护”的项目，这不是次要成本，而是核心设计约束。

因此 Q4 的证据不是“混合总是更好”，而是：

> **分层混合能消除多个纯模型的结构性缺口，但会把简单性成本转换成一致性、版本和运维成本。**

微软对 Event Sourcing “only when benefits justify complexity”的明确警告尤其应该被视为反对无节制架构升级的高权重证据。citeturn17view0

## 证据化比较与路线支持度

**Q5 · 各候选如何对照；“沿用＋修补”与“换模型”两条路线的证据支持如何？**

先说明评分口径：

**高** = 抽象本身直接支持该属性，且有多个论文/成熟系统先例；  
**中** = 可以做到，但依赖额外机制，或证据来自有限 domain；  
**低** = 抽象本身没有解决该属性，必须明显外接另一层；  
**UNKNOWN** = 未找到足够公开资料。

这些不是统计显著性结果。不存在覆盖全部七维的公开统一 benchmark。

| 总体抽象 | 模型可替换性 | 可审计性 | 人类可读性 | 当前态管理 | 加载效率 | 迁移成本 | 与现状兼容 |
|---|---:|---:|---:|---:|---:|---:|---:|
| **现有字面冯诺依曼类比** | 高 | 中 | 高 | 中 | 中 | **低成本/高分** | **高** |
| **修正 OS／概率计算模型** | **高** | 中–高 | 中 | **高** | **高** | 中 | **高** |
| **认知架构 CoALA 型** | 高 | 低–中 | **高（语义层）** | **高** | 中 | 中 | 中 |
| **事件溯源／账本** | **高** | **高** | 中 | 中–高* | 中–高* | **低（昂贵）** | 中 |
| **黑板** | 高 | 低–中 | 中–高 | **高** | 高 | 中 | 中 |
| **数据库中心** | **高** | 中–高* | 低–中 | **高** | **高** | 中–低 | 中 |
| **Git／文档中心** | **高** | **高** | **高** | 中 | 中 | **高（容易迁移）** | **最高** |
| **分层混合** | **高** | **高** | **高** | **高** | **高** | 低–中 | 中–高 |

\* Event Sourcing 的当前态与加载效率只有在 projection/snapshot 做好时才高；数据库的审计只有在历史/version/provenance 被显式设计时才高，并不是 CRUD 数据库自动提供完整因果审计。citeturn17view0turn16search1

### 模型可替换性

最强的不是某个存储技术，而是**模型不能拥有 authoritative state**这一架构纪律。OS/HAL、event sourcing、Git/files 和数据库都可以做到模型无关；ArbiterOS 对 HAL 的论证最直接，而 human-readable/versioned artifacts 又降低供应商 lock-in。citeturn21search1turn19search3turn17view5

认知架构本身也并不要求特定 LLM，但如果 procedural memory 大量隐含在某个模型参数/行为里，迁移可能仍产生语义变化；CoALA 本身就把 procedural memory 区分为 implicit model knowledge 与 explicit code，因此该维度不能只看标签。citeturn11view0

### 可审计性

Event Sourcing 是结构上最强的候选，因为历史本身就是权威对象；ActiveGraph进一步保存 causality/model call lineage。Git 也非常强，因为 commit/diff 能保留文档演化，但 Git commit 不天然表达“这个事实由哪次模型调用、哪份证据、哪条规则触发”，除非项目额外规定 metadata/provenance。citeturn17view0turn17view5turn17view1

数据库可以实现非常强的审计，但传统 CRUD 数据库本身只保存 current record 时并不等于 event history；这正是 Event Sourcing 与传统 CRUD 的核心区别。citeturn17view0

### 人类可读性

Git/Markdown/document-centered 最强；认知架构的 episodic/semantic/procedural 分类也很适合人理解“信息是什么”。Event streams、normalized database tables 和内部 graph state 若直接暴露给 owner，则明显较差，因此需要 human-readable projection。Claude Code、Letta 与 GCC 的近年发展提供了“plain-text/repository 仍然是 agent-native interface”的实际证据。citeturn19search10turn18search3turn17view1

### 当前态管理

这里恰好与 human-readability 排名相反。黑板、数据库、显式 working-state/checkpointer 最自然；LangGraph 把 graph-state checkpoint 与 cross-thread store 分开，是很直接的生产先例。CoALA 也强调 persistent working memory 与 raw context 分离。citeturn18search0turn11view0turn17view6

单纯“从 Git repo 自己找出当前任务状态”可以工作，但它把 state-machine semantics 交给文件约定和模型解释；当任务并行、暂停、审批、失败恢复增加时，这一做法的脆弱性会提高。Temporal/DBOS 等 durable systems 的流行正针对这类运行态问题。citeturn22search5turn18search5

### 加载效率

数据库/index、materialized views、checkpoints 和按需 context compiler 天然比“每次把整个 archive 送给模型”更好；Event Sourcing 也只有配合 projection/snapshot 后才会高效。citeturn17view0turn18search0

Git/files 本身并不等于低效：GCC 与 Letta 都采用程序化、选择性 context 管理；Claude Code 的 auto-memory 也只自动加载有限 index/summary，再按需打开更详细 topic files。真正低效的是“文件即真相”被误实现为“文件全部进入 prompt”。citeturn17view1turn18search3turn19search10

### 迁移成本与现状兼容

任务书描述的现状已经以 Git 文件作为唯一长期真相并采用规则文件和 handoff package，因此 Git/document-centered 和修正后的 OS metaphor 显然能最大限度复用已有 artifact；Event Sourcing 若追溯历史重建完整 event model，会有显著迁移成本。微软对 event sourcing 明确警告：迁入和迁出都可能昂贵，并会约束未来系统设计。citeturn17view0

不过“分层混合”不一定意味着一次性重写。理论上可以把既有 Git 文件保留为 owner-facing canonical artifacts，只从某个时点开始增加 immutable change/event record、checkpoint manifest 或 machine projection。公开架构模式支持渐进分层，但**具体对 Mnemosyne 的迁移工作量 UNKNOWN**，因为本研究没有检查项目 repo、历史规模和实际 writer topology。

### 路线一：沿用现类比＋定点修补

**公开证据支持度：中高。**

支持它的最强理由不是“原比喻已经被证明正确”，而是：2025–2026 文献仍不断复用 CPU/OS/context/storage 这一系统思维，并主动对其做相同方向的修正。ArbiterOS 的 Probabilistic CPU、HAL、external governor，ICA 的 probabilistic execution/deterministic control 双平面，以及 AIOS 的 kernelized resource separation，都说明“计算机系统类比”仍具有活跃研究价值。citeturn21search1turn20search1turn17view3

若走这条路线，公开证据至少要求修补以下语义：

> **CPU → Probabilistic Model Backend**  
> **RAM → Working State + compiled Context，而非同义词**  
> **Program → human-readable rules + deterministic enforcement boundary**  
> **Disk → Durable Record Layer；Git 可作为其人类接口，但不必独占所有物理 persistence**  
> **Snapshot → portable application checkpoint/manifest，而非完整模型 process image**

这些修补分别得到概率执行、long-context 实验、prompt injection、durable workflow 和 Git-based agent context 文献支持。citeturn21search1turn14search6turn20search14turn22search5turn17view1

这条路线最大的证据优势是**迁移风险小**，而且保留 owner 已经形成的 mental model 和 Git artifact。最大结构性不足是：如果只改名而不新增 provenance/authority/current-state semantics，那么原模型没有回答的 **多 writer、历史因果、规则版本绑定、human approval** 仍然没有答案。

因此“定点修补”是否足够，关键不在术语，而在修补是否真的新增这些 architectural contracts。

### 路线二：换用其他候选总体抽象

**若指“用一个纯候选完全替换”：证据支持度中低至中。**

认知架构的功能语义明显优于 RAM/disk 二分，但没有完整 durable/audit substrate；blackboard 有真实 multi-agent benchmark，但主要解决协同当前态；database 可靠，却不能单靠 CRUD 描述长期认知演化；event sourcing 对历史和审计最强，却具有公开记录得非常清楚的复杂度和迁移成本；Git/document 本身又与现状太相似，不足以解决所有原问题。citeturn17view4turn17view6turn16search1turn17view0turn17view1

**若“换用候选”允许改成分层/混合参考架构：证据支持度中高，但长期实证仍不足。**

它的强项不是某篇论文证明了这种组合性能最好，而是每一层都有成熟先例：

- immutable history / provenance：Event Sourcing、ActiveGraph；citeturn17view0turn17view5
- current/query projections：CQRS/materialized views；citeturn17view0
- working/checkpoint state：LangGraph、Temporal、DBOS；citeturn18search0turn22search5turn18search5
- human-readable versioned context：GCC、Claude Code、Letta；citeturn17view1turn19search10turn18search3
- functional memory typing：CoALA/Soar/ACT-R；citeturn17view4turn14search7
- model-independent control/governance：ArbiterOS、ICA。citeturn21search1turn20search1

它的弱点同样有成熟证据：多层意味着 projection consistency、schema migration、versioning、更多 operational concepts，以及 owner 自己理解系统的负担。citeturn17view0turn22search35

### 两路线的最终证据状态

| 路线 | 正向证据 | 主要反证/风险 | 本研究证据支持度 |
|---|---|---|---|
| **沿用现类比＋定点修补** | OS/计算机体系类比仍活跃；HAL、probabilistic CPU、deterministic control 有直接近年文献；与现有 Git 体系兼容 citeturn21search1turn20search1 | 若只修辞不修 authority/provenance/working-state，仍继承原模型盲点 | **中高** |
| **换成单一认知架构** | 信息功能分类贴合 agent cognition citeturn17view4 | durable truth、审计、并发、权限需另补 | **中** |
| **换成单一事件溯源模型** | provenance、replay、历史重建最强 citeturn17view0turn17view5 | 复杂、迁移昂贵、需要 projections | **中** |
| **换成单一黑板模型** | 多 agent shared-state benchmark 较强 citeturn17view6 | 与长期 owner truth 问题错位较大 | **中低** |
| **换成单一数据库中心模型** | durability、查询、current state、并发成熟 citeturn18search5 | database≠完整 memory/governance semantics citeturn16search1 | **中** |
| **换成单一 Git/文档模型** | 人读、迁移、审计、现状兼容；已有 GCC/Claude/Letta 先例 citeturn17view1turn18search3 | 多 writer runtime、强授权和 current-state machine semantics 较弱 | **中高，但实质上接近现状演化而非彻底换模** |
| **改用分层混合参考架构** | 各层均有成熟/近年先例，需求覆盖最宽 citeturn17view0turn18search0turn21search1 | 复杂度、projection consistency、迁移和 owner cognitive load | **中高；但多年实证 UNKNOWN** |

**最终不裁决结论：**

现有“类冯诺依曼”模型没有证据支持被整体判为错误；其**“模型外置长期状态、计算与持久记录解耦、允许模型替换、将规则和状态显式化”**几项原则，与 2024–2026 agent architecture 的主流演化方向高度一致。citeturn17view3turn21search1turn20search1

真正需要复核的不是“还可不可以叫 CPU/RAM/硬盘”，而是原类比是否偷偷引入了五个现实中不存在的保证：**模型确定性、context 随机可寻址性、instruction/data 天然隔离、规则文本强制执行、handoff 等价完整 process snapshot。**公开论文对这五项均给出了明确反例或修正依据。citeturn21search1turn14search6turn20search14turn19search0turn17view5

另一方面，事件溯源带来了原模型最缺的“历史即一等公民”；认知架构带来了“不同长期信息有不同功能语义”；黑板带来了“共享当前态”；数据库/durable workflow 带来了并发、恢复和暂停；Git/document center 则最直接满足长期 owner 的人类可读与跨模型 portability。citeturn17view0turn17view4turn17view6turn18search5turn17view1

因而本次证据更支持这样的**设计阶段问题定义**，而不是某个单一答案：

> Mnemosyne 是否应继续把“类冯诺依曼”保留为顶层 **mental model**，同时在其下增加 event/provenance、explicit working state、policy enforcement 与 human-readable projections；  
> 还是应取消单一机器比喻，直接把这些层提升为新的 reference architecture？

两条路线都有公开证据支持。前者的优势主要是**连续性、低迁移成本和已有心智模型**；后者的优势主要是**语义精确、审计/多人写入覆盖和避免错误硬件类推**。截至 2026-08-31，没有公开纵向实证足以替委托方完成这项最终取舍，故本报告不作最终裁决。

## 来源表

| 来源 | 类型 | 日期 | 本报告用途 / 证据强度 |
|---|---|---|---|
| Packer et al., *MemGPT: Towards LLMs as Operating Systems* | 【论文实证】 | 初稿 2023-10-12；2024 修订 | OS-inspired virtual context；长文档与 multi-session chat 实验；OS 路线直接前史。citeturn15search0turn15search4 |
| Sumers et al., *Cognitive Architectures for Language Agents (CoALA)* | 【论文架构/综述】 | 2024 正式发表/版本 | working、episodic、semantic、procedural memory；LLM agent 的认知架构总框架。不是候选架构 head-to-head benchmark。citeturn15search17turn17view4 |
| Carnegie Mellon, ACT-R 官方说明 | 【官方/学术传统】 | 持续维护；访问 2026-08-31 | declarative/procedural memory 与 buffers；认知架构传统依据。citeturn14search7 |
| Mei et al., *AIOS: LLM Agent Operating System* | 【论文实证】 | 2024-03 起；COLM 2025 | kernel 提供 scheduling/context/memory/storage/access control；最高 2.1× agent serving speedup。citeturn17view3turn15search10 |
| Liu et al., *Lost in the Middle: How Language Models Use Long Contexts* | 【论文实证】 | TACL 2024 | context 中信息位置影响 retrieval/QA；直接反驳 context≈可靠随机访问 RAM。citeturn14search6 |
| Chen et al., *Defending Against Prompt Injection with Structured Queries (StruQ)* | 【论文实证】 | 2024-09 v2 | instruction/data 非天然隔离；结构化双通道及专门训练可降低 prompt injection。citeturn20search6turn20search30 |
| Zverev et al., *Can LLMs Separate Instructions From Data?* | 【论文实证】 | 2024 | 多模型 instruction/data separation 缺陷证据。citeturn20search14 |
| Xu et al., *From Craft to Constitution / ArbiterOS* | 【论文架构/观点】 | 2025-10-12 | 直接提出 Probabilistic CPU、volatile/unreliable memory、semantic ISA、non-stationary hardware、HAL 与 deterministic governor。无跨架构实证。citeturn21search6turn21search1 |
| Wu et al., *Git Context Controller* | 【论文实证】 | 2025-07 起；2026-03 v2 | Git-style commit/branch/merge agent context；SWE-Bench 与 CLI case 实验。领域主要限 coding。citeturn17view1turn18search27 |
| Salemi et al., *LLM-based Multi-Agent Blackboard System…* | 【论文实证】 | 2025-09；2026-01 v2 | blackboard multi-agent；三个 data-science benchmark 上 +13%–57% end-to-end relative success、最高 +9% F1。citeturn16search0turn17view6 |
| Microsoft Azure Architecture Center, *Event Sourcing Pattern* | 【厂商/架构文档】 | 当前页 2026-03-28 | append-only system of record、CQRS/projection/snapshot；同时给出 eventual consistency、ordering、query、migration 等成熟 trade-off。citeturn17view0 |
| Nakajima, *The Log is the Agent / ActiveGraph* | 【论文架构/系统】 | v1 2026-05-21；当前修订 2026-08 | agent event log as source of truth、working graph projection、lineage、fork、replay；作者明确不声称 task-accuracy 优势。citeturn15search3turn17view5 |
| Orogat & Mansour, *Is Agent Memory a Database?* | 【论文架构/原型】 | 2026-05-25 | 反驳“CRUD/database 已足够”；提出 Governed Evolving Memory/state-trajectory correctness。citeturn16search1turn16search13 |
| Lin et al., *Model-Native Computing Architecture* | 【论文架构/综述】 | 2026-05-29 | 直接复核 LLM=CPU、KV cache=cache、context=memory 等类比；提出 dual-plane ICA；明确无新实验。citeturn20search1 |
| Jiang et al., KV cache system survey | 【论文综述】 | 2026-07-09 | KV cache 是 autoregressive decoding tensor cache / serving optimization，不是长期语义 memory。citeturn20search3 |
| LangGraph Persistence 文档 | 【厂商文档】 | 访问 2026-08-31 | checkpointer 与 long-term store 两套互补 persistence；证明 working checkpoint 与 durable memory 分层已有主流实现。citeturn18search0turn18search16 |
| DBOS AI / durable workflow 文档 | 【厂商文档】 | 2026 | database 作为 workflow execution state truth 与 failure recovery substrate。citeturn18search1turn18search5 |
| Temporal AI / Versioning / HITL 文档 | 【厂商文档】 | 2026；HITL 页面 2026-08-14 | long-running stateful agent、human wait、event history、recovery、workflow code versioning；多年 process 的直接工程先例。citeturn22search1turn22search5turn22search35 |
| Anthropic Claude Code Memory / `.claude` 文档 | 【厂商文档】 | 访问 2026-08-31 | fresh context、CLAUDE.md、plain-text memory、Git sharing；并明确 rule files 是 context 而非强制 enforcement。citeturn19search10turn19search3 |
| Letta, *Context Repositories: Git-based Memory* | 【厂商研究/实现】 | 2026-02 | MemGPT 谱系转向 filesystem + Git-based context management；说明 OS 和 Git 抽象可组合。citeturn18search3turn18search11 |
| NIST AI RMF / GenAI Profile / Playbook | 【政府规范】 | GenAI Profile 2024-07-26；访问 2026-08-31 | human oversight、治理职责和风险管理依据。citeturn22search6turn22search10 |
| Gilbert, external/cognitive offloading review；2026 human-AI belief-offloading work | 【论文综述/研究】 | 2022；2026 | 人类长期 owner 为什么需要外部化、同时需要保留认知与判断主权的背景证据。citeturn14search1turn22academia38 |
| “2 years building agent memory…” 社区讨论 | 【社区经验】 | 2025；访问 2026-08-31 | Git/plain files 透明性、audit/history 的实践偏好；仅作 anecdotal evidence，不参与高权重结论。citeturn18search35 |

**明确 UNKNOWN 清单：**

公开资料中未发现对“OS、认知架构、event sourcing、blackboard、database、Git/document”六类总体抽象进行同一 workload、同一模型、同一成本约束下的直接总体 benchmark；**UNKNOWN**。citeturn20search1

未发现连续数年的公开实验，直接研究“一个稳定 human owner 在多个模型供应商和模型世代之间迁移同一项目”并量化知识/规则/授权保真率；**UNKNOWN**。

未发现足以证明 Git/document-as-truth 在非 coding、跨年、高并发多 writer 项目中优于 event-sourced/database architecture 的普遍性实证；当前强实证主要来自 coding-agent workload；**UNKNOWN beyond that domain**。citeturn17view1

未发现 ActiveGraph/event-sourced agent 相对于主流 agent frameworks 的任务准确率或总体 TCO 优势实验；作者明确未作该项 claim；**KNOWN NOT DEMONSTRATED**。citeturn17view5

未发现 CoALA 证明认知记忆分类本身能够提供 event-level provenance、强授权或 multi-writer consistency；这些能力应视为额外系统层，而非该框架已验证能力；**UNKNOWN / outside CoALA scope**。citeturn17view4

未发现证据足以支持“只要将现有术语 CPU/RAM/硬盘重新命名，而不改变任何运行机制，就能消除当前模型的风险”；相反，prompt injection、long-context position sensitivity、model non-stationarity 等证据表明，至少部分修补必须落实为真正的 architectural boundary。citeturn14search6turn20search14turn21search1

**建议导出文件名：** `MNE-DR-028-report.md`