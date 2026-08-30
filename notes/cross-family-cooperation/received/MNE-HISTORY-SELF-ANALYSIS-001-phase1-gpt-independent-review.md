# MNE-HISTORY-SELF-ANALYSIS-001  
## Mnemosyne 2026-06 至 2026-08 建设史：GPT 侧独立复盘

## 证据范围与总判断

> 本次仅使用 GitHub 只读访问；未使用 Web、Deep Research，也未创建或修改文件、分支、PR、Issue、评论或标签。未读取材料导航中明确排除的另一家族评估目录。

证据标注口径：`VERIFIED` 只用于本报告实际读取的原件或索引；日期采用文件头 `Created` 或 inventory 的 `created` 字段。`INFERENCE` 是由这些材料推出、但档案未直接陈述的判断；`UNKNOWN` 表示已读范围不足以作可靠判断。

**VERIFIED**　ALAYA 在其 `README.md` 中被定义为私有对话档案与“数字分身”原料库，而不是 Mnemosyne 的执行源；本报告据此把对话原件当历史证据，不把归档索引本身当项目真相源。fileciteturn45file0L2-L2

**INFERENCE**　两个月的核心成绩可以概括为：Mnemosyne 已经较好地实现了“可恢复、可审计、遇到身份冲突时可拒收”，但尚未充分证明“以较低 Owner 操作负担持续提高真实长任务的效率与准确性”。8 月 21 日的 fresh-context 测试证明极少量 onboarding 文件足以让新会话正确保持只读、拒绝无任务接管；而 8 月 10 日的 Owner 指令仍要求把“实际提高效率和准确性”列为尚待真实档案评估的问题。fileciteturn40file0L2-L2 fileciteturn41file0L2-L2 fileciteturn19file0L193-L251

**INFERENCE**　因此，本报告的总评是：**核心目标部分达成，工程可靠性高于产品性证明；防错能力的证据强，省事与增效的证据弱。**

---

# Q1　目标轨迹

## 结论

**VERIFIED**　项目最初的核心目标并不是一般意义上的“做一套 Agent 治理平台”，而是解决长工作中模型上下文有限、开新对话交接麻烦的问题。Owner 的谱系口述明确给出：GeodataMaster 的自动化开发需求先产生 Meta-Agent 构想，随后因“AI 对话上下文记忆有限、开新对话交接麻烦”产生 Mnemosyne。fileciteturn44file0L2-L2

**VERIFIED**　2026-06 中旬，目标被工程化为两件事：一是让全新的普通 ChatGPT 仅凭仓库完成接手验证；二是尽快把 Mnemosyne 用于真实或半真实 target project 的首个应用测试。6 月 16 日主线以 fresh onboarding verification 开场；6 月 20 日 Meta-Agent 主线又把近期优先级写成“尽快可用于真实 target projects”，并给出 first application test。fileciteturn6file0L2-L2 fileciteturn21file0L1-L80

**VERIFIED**　2026-06-23，目标进一步收敛为“可恢复性续接”：fresh session 不依赖旧对话隐式上下文，必须恢复执行源、阶段、真实状态、权限、未完成任务与安全下一步，并在未知时停下而不是编造；同时用 100 分量表和 blocking gates 进行 replay 验收。fileciteturn24file0L1-L1000

**VERIFIED**　2026-07，工作范围显著外扩：从单次 handoff 扩展到 guidance locality、跨模型裁定来源、并行 workstream、PR 谱系、目标记忆迁移、前沿模型澄清包和 Meta-Agent 产品线。主线索引把这一时期概括为从“两步 receive/guidance”到“专项任务绑定交接包”和多路线隔离。fileciteturn6file0L2-L2 fileciteturn7file0L2-L2

**VERIFIED**　2026-08-10，Owner 明确修正建设方向：不再“又细又慢”地抽象推进，而要用真实需求、真实使用、失败与反馈证明价值；同一主线新旧对话交接要用完整历史档案评估实际效果，而不是只检查字段。该指令被记录到公开 Issue #265。fileciteturn19file0L2-L6 fileciteturn19file0L100-L148 fileciteturn19file0L193-L251

## 是否发生漂移、由谁引发

**INFERENCE**　发生的是**加法式漂移**，不是核心目标被正式替换：handoff 一直存在，但围绕它不断增加研究、审计、平台能力、模型 provenance、并发治理、验证包与发布流程，导致“帮助真实工作续接”在一段时间内被“建设保证续接的制度”压到次位。

**VERIFIED**　Owner 直接引发的两次方向变化最明确：第一次是项目起源时把上下文与交接困难定义为问题；第二次是 8 月 10 日要求 real-use-first、actual-failure-evidence-priority。fileciteturn44file0L2-L2 fileciteturn19file0L193-L299

**VERIFIED**　GPT 侧也主动扩大过范围。最清楚的例子是 8 月 7 日：Owner 只要求“从未完成工作中选择一个推进”，GPT 自行选择 `HO-GUIDANCE-001`，并产出 18-cell 的合成受控实验准备包，而不是选择一个真实目标需求。fileciteturn36file0L2-L2

**VERIFIED**　事故反应引发了第三类漂移：7 月 8 日因 guidance load 错把 maintenance route 导入本地任务而拆分命令；8 月 13 日因接收方补全不存在的 40 位 SHA、无依据声称 `worktree_clean` 而加 canonical schema；8 月 19–20 日因路径、blob、执行面和 exact-byte 发布连续失败而继续增加门禁，之后才反向简化。fileciteturn30file0L2-L2 fileciteturn37file0L2-L2 fileciteturn8file0L2-L2

**UNKNOWN**　若要把 6–7 月每一个任务精确归因为“Owner 首创”或“GPT 首创”，档案仍不足：不少原件只保存了执行提示词，没有保存提示词最早由谁提出、在哪次未归档讨论中形成。

---

# Q2　产出结构

## 结论

统计口径：把能直接支持接手、恢复、权限/路线隔离与安全下一步的可复用机制计为“产品性”；把规范、任务书、验收、发布、记录、迁移和收口计为“流程性”；把 Deep Research、Pro 研究/评审及其综合计为“研究性”。同一工作兼有多重性质时，按其主要投入目的归类。

**INFERENCE**　按“投入工作量”而非文件数量估算，我给出的点估计是：

| 类别 | 估计占比 | 合理区间 |
|---|---:|---:|
| 产品性产出 | **28%** | 22%–35% |
| 流程性产出 | **47%** | 40%–55% |
| 研究性产出 | **25%** | 20%–32% |

**VERIFIED**　估计基础之一是档案构成：Mnemosyne 线有 56 份，Meta-Agent 线有 26 份；MNE 专项组中有大量 DR、Pro review、验证、门禁与收口会话，MA 线又至少登记了 15 个 DR 编号，包括原件丢失的 DR-03。fileciteturn13file0L2-L2 fileciteturn43file0L2-L2

**VERIFIED**　产品性产出并非没有：唯一执行源边界、三层 handoff、官方仓库交接工件、guidance/handoff 命令拆分、task-bound package、fail-closed identity check、AI onboarding 包，均形成了可复用机制；8 月 21 日的 fresh-context case 表明 onboarding 能在只读三到五个文件时正确拒绝无授权接管。fileciteturn6file0L2-L2 fileciteturn15file0L2-L2 fileciteturn40file0L2-L2 fileciteturn41file0L2-L2

**INFERENCE**　流程性占比最高，是因为主线的大量工作不是直接让目标 Agent 记得更好，而是在生成、搬运、验收、裁决、合并、收口和再交接这些机制的证据。最大对话长达 24,755 行；其开头的 first application test 已有大量字段、阶段和回传格式，结尾仍在做 receive-only、独立 guidance refresh、旧会话复核新会话回执。fileciteturn43file0L2-L2 fileciteturn21file0L300-L469 fileciteturn21file0L24540-L24754

**VERIFIED**　7 月 2 日的 Meta-Agent dry-run 被判 `PASS_WITH_WARNINGS`，但它明确是受控无写、无真实 target workspace、无目标仓库写入；这说明一部分看似“应用验证”的工作仍属于流程/模拟证据，而非已投入使用的产品能力。fileciteturn27file0L2-L2

**UNKNOWN**　档案没有统一的工时账、模型调用成本账或 Owner 手工时间日志，所以无法把上述比例提高到精确统计；这是基于文件体量、会话类型和工作内容的中等置信度估算。

---

# Q3　需求分析：何时首次形成可验收的“结果标准”

## 结论

**VERIFIED**　严格按题目所说的“结果标准，而非格式字段清单”，第一次清楚出现是在 **2026-08-10 的 Owner 指令，随后写入 Issue #265**。它要求用真实完整对话档案看：新会话是否恢复目标与阶段、handoff 后是否实际提高效率与准确性、错误究竟来自 artifact、receiver、live-state 还是用户操作；并明确说不能只检查格式字段。fileciteturn19file0L193-L251

**VERIFIED**　2026-06-23 的 DR2 是重要前身，也是第一次把 handoff 做成可重复、可记分、可审计的**代理验收标准**：给出正确交接的操作性定义、100 分量表、blocking gates 和 PASS/PASS_WITH_WARNINGS/FAIL/BLOCKED。fileciteturn24file0L1-L1000

**INFERENCE**　两者的差别是：6 月 23 日主要测“fresh receiver 能否从允许输入恢复正确状态并给出安全下一步”；8 月 10 日才把“真实工作后来是否更快、更准、少重复、维护成本是否可接受”纳入成败。前者是安全续接 proxy，后者才是产品结果。

**VERIFIED**　在 6 月 23 日之前，迭代主要由四种信号驱动：字段/清单覆盖、仓库一致性核验、fresh replay 或 dry-run、以及明显事故。6 月 16–23 日旧主线先出现重复回答、旧问题回流、任务主语错配和上下文过长，随后才启动 detailed handoff 与 DR2。fileciteturn22file0L8001-L13000 fileciteturn23file0L1-L2000

**UNKNOWN**　更早、未入 ALAYA 的前身对话是否已经写过真正 outcome-based 的 handoff 验收标准，现有档案无法判断。

---

# Q4　Deep Research 委托及其后续引用

## 口径

**VERIFIED**　以下只把档案中明确标为 ChatGPT Deep Research/DR 的委托列入；`ChatGPT-DR - Mnemosyne - review batch-B` 虽文件名带 DR，但索引明确认定它是 Pro review，不计为 Deep Research。Fable 的 MNE-DR-003/005 也属于另一模型家族的 Research，不混入本表。fileciteturn14file0L2-L2 fileciteturn8file0L2-L2

## A. Mnemosyne 线

| 委托 | 档案中找到的后续实际引用 | 证据判定 |
|---|---|---|
| DR1《AI Agent 持久记忆研究》，2026-06-22 | 被 Batch A/B 作为证据层使用；其五层可测分解和建议进入 pre-dry-run 小修语境 | **VERIFIED** fileciteturn13file0L2-L2 |
| DR2《Mnemosyne 交接包策略》，2026-06-23 | 直接形成三层 handoff、scorecard、执行源 §15 与 MNEMOSYNE-083 官方交接工件 | **VERIFIED** fileciteturn6file0L2-L2 fileciteturn14file0L2-L2 |
| DR4 用户原文/脱敏治理，2026-06-29 | 形成 `user-input-storage-governance-v0.1`；本次样本未找到后续某一设计决定明确引用它 | **UNKNOWN**（产出存在已验证，后续采用未验证） fileciteturn14file0L2-L2 |
| DR5 v2 首个真实 dry-run 评测框架，2026-06-30 | 形成 evaluation framework/scorecard；7 月 Phase A 明确把这两个文件列为基础补丁对象 | **VERIFIED** fileciteturn14file0L2-L2 fileciteturn32file0L2-L2 |
| DR6 平台能力增量，2026-07-15 | 产出 5 项候选修复，含 file-first delivery；后续指导中确有 file-first guard，但本样本未见逐条 provenance 回链 | **INFERENCE**（很可能被采用，缺显式引用链） fileciteturn15file0L2-L2 |
| DR7 多模型裁定与 provenance，2026-07-21，Thinking/Pro 两次平行运行 | 服务 PR #198 guard，后由 PR #200 做 v0.2 修补 | **VERIFIED** fileciteturn15file0L2-L2 |
| 并行工作主线治理，2026-07-24 | two-plane、事务声明、one-immediate-merge-target 后续进入 8 月 V2A 并发验证线 | **VERIFIED** fileciteturn16file0L2-L2 fileciteturn46file0L2-L2 |
| DR8 HO-GUIDANCE，2026-07-28 | “task-local policy、默认 B、永不默认全量 C”直接成为 8 月 HO-GUIDANCE A/B/C 受控实验的依据 | **VERIFIED** fileciteturn35file0L2-L2 fileciteturn36file0L2-L2 |
| DR9 learner cognitive coaching，2026-07-28 | 与外语教师方向语义相关，但已读材料未见明确 task/commit 把某项结论写入设计 | **UNKNOWN** fileciteturn47file0L2-L2 |
| DR10 cross-agent shared memory，2026-07-28 | 形成六层共享记忆治理建议；已读材料未找到明确的后续设计决定引用 | **UNKNOWN** fileciteturn47file0L2-L2 |
| DR11 target-memory migration，2026-07-28 | 索引明确把它列为 8 月 Target Lifecycle V0/V1 的理论基础 | **VERIFIED** fileciteturn47file0L2-L2 |
| DR12 adaptive explanation，2026-07-28 | 形成候选框架；索引明确写“具体落库任务号未见” | **UNKNOWN** fileciteturn47file0L2-L2 |
| DR13 frontier clarification，2026-07-29 | 直接对应 FCV 验证包和 Fable A1/A2 轨道 | **VERIFIED** fileciteturn47file0L2-L2 |

## B. Meta-Agent 线

| 委托 | 档案中找到的后续实际引用 | 证据判定 |
|---|---|---|
| MA-DR-01 Research Overview，2026-06-22 | 在首代主线中被综合为“人主导、文件化、可审计的设计控制平面” | **VERIFIED** fileciteturn21file0L4920-L7000 |
| MA-DR-02 Project Overview，2026-06-22 | 被用于 single-agent/workflow/multi-agent 选择与“workflow 优先”原则 | **VERIFIED** fileciteturn21file0L4920-L7000 |
| MA-DR-03 memory/handoff/learning，2026-06 批次（原对话精确日期 UNKNOWN） | 首代主线显示它曾被读入并参与综合，但 ALAYA 原对话已确认丢失，只剩外部归档指针 | **UNKNOWN**（使用痕迹可见，原件质量与精确内容不可独立复核） fileciteturn43file0L2-L2 fileciteturn21file0L4920-L7000 |
| MA-DR-04 Design Concept，2026-06-22 | 被综合为 capability-based routing、人类边界和治理代理定位 | **VERIFIED** fileciteturn21file0L4920-L7000 |
| MA-DR-05 Research Concept，2026-06-22 | 被综合为 evaluation/trace/review/failure catalog 必须进入首版 | **VERIFIED** fileciteturn21file0L4920-L7000 |
| MA-DR-06 自动化系统设计与工作流搜索，2026-08-01 | 与 DR-07 构成 Batch A，实际决定 DR-08/09 是否解锁；被接受为非执行源 evidence | **VERIFIED** fileciteturn43file0L2-L2 fileciteturn21file0L11936-L14716 |
| MA-DR-07 安全威胁模型与对抗评估，2026-08-01 | 同上；其有效性与纠正状态直接控制后续研究 gate | **VERIFIED** fileciteturn43file0L2-L2 fileciteturn21file0L11936-L14716 |
| MA-DR-08 Portable Agent Design，2026-08-04 | 进入七报告 formal adjudication、convergence 与 downstream gates | **VERIFIED**（被研究治理决策引用）；**UNKNOWN**（是否有具体建议升格为 canonical 产品设计） fileciteturn43file0L2-L2 fileciteturn21file0L14717-L21000 |
| MA-DR-09 Benchmark Research，2026-08-04 | 形成 benchmark/ablation/pilot protocol，并在主线中完成 formal review | **VERIFIED**（被 gate/评审引用）；**UNKNOWN**（是否实际进入 pilot） fileciteturn43file0L2-L2 |
| MA-DR-10 需求到 Agent 设计方法论，2026-08-04 | 进入七报告 formal adjudication 与 candidate ledger | **VERIFIED**（被裁决）；**UNKNOWN**（未见明确 canonical promotion） fileciteturn43file0L2-L2 fileciteturn21file0L14717-L21000 |
| MA-DR-11 Methodology Promotion，2026-08-04 | 除 formal adjudication 外还有 enhanced correctness review | **VERIFIED**（被裁决）；**UNKNOWN**（未见明确 canonical promotion） fileciteturn21file0L14717-L21000 |
| MA-DR-12 动态委派与自主性，2026-08-04 | 进入七报告 formal adjudication 与 downstream gates | **VERIFIED**（被裁决）；**UNKNOWN**（未见明确 canonical promotion） fileciteturn43file0L2-L2 |
| MA-DR-13 Long-Term Product，2026-08-04 | 进入七报告 formal adjudication 与 downstream gates | **VERIFIED**（被裁决）；**UNKNOWN**（未见明确 canonical promotion） fileciteturn43file0L2-L2 |
| MA-DR-14 私有目标材料存储，2026-08-04 | 进入七报告 formal adjudication；仍被限制为公开资料/合成场景 | **VERIFIED**（被裁决）；**UNKNOWN**（未见真实私有材料设计启用） fileciteturn21file0L14717-L21000 |
| MA-DR-15 能力矩阵与治理，2026-08-04 | 进入七报告 formal adjudication 与 downstream gates | **VERIFIED**（被裁决）；**UNKNOWN**（未见明确 canonical promotion） fileciteturn43file0L2-L2 |

**INFERENCE**　研究利用率呈两极分化：最靠近当时工程 blocker 的 DR2、DR7、并发治理、DR8、DR11、DR13，后续链最清楚；面向未来应用领域或产品远景的 DR9/10/12 及 MA-DR-08–15，多数先进入 evidence/adjudication 层，离实际产品采用还有一层甚至多层。

---

# Q5　方案设计：交接机制各代变化及触发

| 代际 | 主要机制 | 触发 | 判定 |
|---|---|---|---|
| G0，5 月末–6 月中 | 聊天内详细 handoff；旧对话充当新对话接手验证者 | 上下文有限、需要换对话 | **VERIFIED** fileciteturn6file0L2-L2 |
| G1，6 月 16 日 | fresh onboarding；以仓库 execution source/current/handoff 文件恢复状态 | 验证“普通新会话能否只靠仓库接手” | **VERIFIED** fileciteturn22file0L1-L120 |
| G2，6 月 23 日 | minimum/standard/extended 三档包、100 分 rubric、blocking gates、官方 083 工件 | 旧会话上下文退化 + DR2 研究 | **VERIFIED** fileciteturn6file0L2-L2 fileciteturn24file0L1-L1000 |
| G3，7 月 8–17 日 | guidance load 与 handoff receive/prepare 分离；receive 后再单独 refresh guidance | guidance 命令把维护路线误导入本地任务 | **VERIFIED，事故驱动** fileciteturn30file0L2-L2 fileciteturn31file0L2-L2 |
| G4，7 月 26 日起 | task-bound package；多工作线各有 owner conversation，不再做全局接管 | Meta-Agent、health review、FCV 等路线并行，需防串线 | **VERIFIED** fileciteturn7file0L2-L2 fileciteturn32file0L2-L2 |
| G5，7 月 30 日–8 月 19 日 | fail-closed baseline、expected/actual identity、逐 blob 校验、canonical receive schema/oracle | 未合并 PR、错误路径/blob、伪造完整 SHA、无依据的 worktree 声明 | **VERIFIED，事故驱动** fileciteturn33file0L2-L2 fileciteturn37file0L2-L2 fileciteturn8file0L2-L2 |
| G6，8 月 7–21 日 | 无 handoff package 的仓库自足恢复；三到五个 onboarding 文件的 fresh-context 测试 | 真实 cold-start 测试和实用化转向 | **VERIFIED，测量/测试结果驱动** fileciteturn7file0L2-L2 fileciteturn40file0L2-L2 fileciteturn41file0L2-L2 |
| G7，8 月 20–21 日 | 从 exact-byte 过程合同转向自然语言目标 + 最终工件约束的柔性工作书 | MNEMOSYNE-235–239 五连败及 Owner 质疑；241 一次成功 | **VERIFIED，事故与 Owner 纠偏驱动** fileciteturn8file0L2-L2 |

**INFERENCE**　G2 经常被描述为“量化驱动”，但严格说它是**先设计量表**，不是因已有量化结果而改版；真正清楚的“测完再改”主要出现在 G6 的 fresh-context/onboarding 和 8 月并发验证线。

**INFERENCE**　这条演化路线表现出一个反复模式：事故先产生更严的合同，合同与执行面不匹配又产生新事故，直到 Owner 要求做减法；因此后续 Meta-Agent 不应把“每次事故新增一层永久协议”当默认修复策略。

---

# Q6　操作负担

## 典型手工步骤

**INFERENCE**　6 月早期一次交接通常约 **4–6 个 Owner 动作**：让旧对话生成包、开新对话、粘贴或上传包、必要时再上传旧对话全文、把新会话报告带回旧会话、确认旧会话退役。6 月 23 日实际就是“handoff 包 + 旧全文导出 + 新会话复盘”。fileciteturn22file0L12001-L13000 fileciteturn23file0L1-L2000

**INFERENCE**　7 月成熟两步协议通常升到 **7–9 个动作**：旧线准备并合并 package、开新对话、发送 receive startup、复制 receive report 回旧线或做外部验收、再发送独立 guidance refresh、必要时切模型、发送实质 continuation、再审查或合并下一 PR。7 月 17 日原件明确要求 receive 与 guidance 不能同一操作。fileciteturn31file0L2-L2

**INFERENCE**　8 月事故链中，一个失败的高保证循环可能达到 **9–15 个动作甚至更多**：修路径或 blob、重开对话、再次 receive、返回报告、修 schema/oracle、合并 PR、再 rehearsal、手动切 Pro/次一档/Fable、搬运输出。Fable 管理索引明确称这一阶段是“人肉模型调度器”，并记录 Pro 额度因交接失败消耗后停工。fileciteturn8file0L2-L2

**VERIFIED**　高保证 receive report 本身也显著膨胀。8 月 19 日成功样本要求 package、schema、execution source、commands、candidate、manifest、source archive、文件数、禁止项等逐字段 `expected/actual/exact_match`。fileciteturn39file0L2-L2

**VERIFIED**　8 月 21 日的 onboarding 包证明另一条更轻的路径可行：单条 pinned-ref 指令加 3–5 个导航文件，就能正确做 read-only assessment 或 `BLOCKED_NO_EXACT_TASK`；但这验证的是“安全冷启动/不越权”，不是完整长任务续作。fileciteturn40file0L2-L2 fileciteturn41file0L2-L2

**INFERENCE**　所以两个月总体不是单调减负：**6 月到 8 月中旬明显增加；8 月下旬开始分叉**。轻量 onboarding 变简单，高保证跨路线交接仍然很重。若把 Owner 人工步骤视为产品成本，净负担截至档案末尾仍高于项目初期。

---

# Q7　方向质疑

**VERIFIED**　GPT 侧并非完全没有收缩意见。DR2 明确说 first real dry-run 前“最该做的不是继续堆更多文件”，而是跑一次可记分 replay；DR8 又明确反对把完整 Mnemosyne guidance 默认加载进目标业务对话，主张精简的 task-local B。fileciteturn24file0L1-L1000 fileciteturn35file0L2-L2

**INFERENCE**　但这些都是**局部机制收缩**，不是对总体工作方向的质疑。在已读样本中，我没有找到 GPT 在 8 月 10 日之前主动提出：“暂停继续扩展 Mnemosyne 自身制度，把主要资源转去两个真实需求，用真实使用决定后续设计。”

**VERIFIED**　相反，8 月 7 日在有权自主选择未完成工作时，GPT 选择的是 HO-GUIDANCE 合成实验包；宏观 real-use-first 转向由 Owner 在 8 月 10 日明确提出。fileciteturn36file0L2-L2 fileciteturn19file0L100-L148

**INFERENCE**　当时应该提出宏观收缩，最迟时点是 **2026-07-02 受控无写 dry-run 完成后**：此时已有大量治理、研究和验证资产，却仍无真实 target write/use；6 月的上下文退化也已证明流程本身会吞噬会话容量。7 月 8 日 guidance-locality 事故后是第二个明确时点。

**UNKNOWN**　未全文读取的其他小会话中是否有更早、措辞明确的宏观反对意见，不能排除；本结论限定为本报告实际读样本。

---

# Q8　教训清单

## 不应带进 Meta-Agent 与具体项目 Agent 的工作模式

| 工作模式 | 档案实例 | 结论 |
|---|---|---|
| 1. 每次事故只加新 guard，不同步删除旧层 | 7/8 命令拆分后，8/19 receive 又增长为巨型逐字段 schema | **INFERENCE**　应采用“新增一条、删除或合并一条”的协议预算 |
| 2. 把 artifact 完整和 PASS verdict 当产品价值代理 | 7/2 dry-run PASS_WITH_WARNINGS，但无 target workspace/write | **VERIFIED**　不得把模拟通过写成真实可用 |
| 3. 让一个超长主线兼任研究路由、发布、验收、handoff 总线 | 《通用目的元Agent建设》24,755 行；末尾仍靠旧对话核验新对话 | **VERIFIED**　应按稳定产品对象或任务边界拆线，而不是按“一个总主持对话”聚合 |
| 4. 把 Owner 变成人工 transport、模型切换器和 quota scheduler | 8 月 Fable 管理线反复切 Pro/次一档/Fable、搬运报告与回执 | **VERIFIED**　Agent 系统应显式优化 Owner touches |
| 5. 在执行面未验证前设计 exact-byte 全过程合同 | 235–239 因大小写、connector blob、无网络或 gh、MAX_PATH 连败 | **VERIFIED**　先验证 execution surface，再选择合同强度 |
| 6. 研究先批量立项，后补 adoption traceability | MNE DR9/10/12 与多份 MA DR 虽有报告，具体产品升格链不清 | **INFERENCE**　每项研究必须在立项时绑定“可能改变的决定”和到期 disposition |
| 7. 用同族模型自我证明独立性 | 多次旧 GPT 验新 GPT、Thinking/Pro 同族复核；后来才引入 evidence tier | **INFERENCE**　同族复核可做一致性检查，不应单独承担高影响独立性 |
| 8. 让发布/收口工作反客为主 | 8/19–21 的 235–243 大量精力用于保全、发布、closeout、onboarding | **INFERENCE**　发布链应是薄层工具，不应成为产品主线 |
| 9. 默认完整加载元系统指导 | 7/8 已证明会导入错误 maintenance route；DR8 也反对全量 C | **VERIFIED**　项目 Agent 只加载最小 task-local 公共合同 |
| 10. 把“不知道”视为待补字段，而非可接受终态 | 8/21 no-task case 的正确结果恰是 BLOCKED_NO_EXACT_TASK | **VERIFIED**　安全停止应是一等成功结果 |

支撑实例：fileciteturn27file0L2-L2 fileciteturn30file0L2-L2 fileciteturn39file0L2-L2 fileciteturn8file0L2-L2 fileciteturn40file0L2-L2

## 值得延续的模式

| 模式 | 为什么值得保留 | 结论 |
|---|---|---|
| 1. execution source / evidence / candidate / historical artifact 分层 | 多次防止 handoff、研究或旧导出覆盖当前真相 | **VERIFIED**　这是两个月最稳定、最有复用价值的设计 |
| 2. fail-closed + expected/observed + 不刷新期望值 | 7/30 未合并 PR 正确拒收；8/18 错路径/错 blob 也正确停下 | **VERIFIED**　适合高影响写入与身份门，不宜无差别用于所有聊天 |
| 3. task-bound handoff 与 route locality | 7 月后能阻止 Meta-Agent、health review、maintenance 互相接管 | **VERIFIED**　应保留，但包体需瘦身 |
| 4. fresh-context 正负测试 | S8 和 8/21 onboarding 测试验证了“信息不足时诚实失败” | **VERIFIED**　比模型自评或格式检查更可信 |
| 5. 用完整 archive 区分当时 handoff 效果与事后全知推断 | Issue #265 明确提出该方法学区分 | **VERIFIED**　应成为后续 Meta-Agent/项目 Agent 的标准复盘方法 |
| 6. 事故保全、可回滚、禁止静默修复 | 236 等失败虽未完成任务，但没有错误 tree/commit/PR | **VERIFIED**　对不可逆写入尤其有价值 |

支撑实例：fileciteturn33file0L2-L2 fileciteturn47file0L2-L2 fileciteturn40file0L2-L2 fileciteturn19file0L227-L251

---

# Q9　自我盲区

**INFERENCE**　第一盲区是 GPT 会天然高估形式化、可审计和 fail-closed 的价值，因为这些正是 GPT 侧最容易从文件中观察和证明的成果；Owner 的疲劳、被打断感和“这件事本来应很简单”的损失更难从仓库记录量化。

**UNKNOWN**　第二盲区是档案选择偏差：ALAYA 是 8 月末整理出的导出集合；是否遗漏某些失败对话、口头决策或未导出的早期讨论，无法从库内自证。`MA-DR-03` 原对话已确认丢失，是明确实例。fileciteturn43file0L2-L2

**UNKNOWN**　第三盲区是本报告采用覆盖式抽样而非 82 份全文通读，因此“没有找到某项质疑或引用”只能证明已读样本中没有，不能证明全档案绝对不存在。

**UNKNOWN**　第四盲区是缺少真实工时与交互计数：无法精确回答每次 handoff 节省了多少重述时间、增加了多少点击、复制或模型切换，净收益是多少。

**INFERENCE**　第五盲区是同族自评：我可能把“事故后协议变严”解释为合理工程演进，而另一家族会更敏感地把它看成 GPT 反复为自身失误建立制度性护栏。

需要另一家族或 Owner 优先核验的两点是：

1. **UNKNOWN**　从主观与时间成本看，哪几次 handoff 真正让 Owner 感到“省事”，哪几次虽然正确但比重做更麻烦；
2. **UNKNOWN**　把 handoff artifact 隐去、只给允许的接收输入重放时，各代方案对真实下一步质量的净提升是多少；这需要按 Issue #265 的案例集方法做盲评，而不是继续读更多规范。

---

# 实际读取文件清单

## 全文读

1. `README.md`
2. `indexes/project-genealogy-origin.md`
3. `indexes/archive-inventory-mainline.yaml`
4. `indexes/archive-inventory-ma.yaml`
5. `indexes/archive-inventory-batch2.yaml`
6. `indexes/archive-inventory-specialized.yaml`
7. `conversations/chatgpt/MA/ChatGPT-MA-受控无写DryRun执行-20260702.md`（89 行）
8. `conversations/chatgpt/MNE/ChatGPT-（Finish）MNE-AI-ONBOARDING-FRESH-TAKEOVER-NO-TASK-001-20260821.md`
9. `conversations/chatgpt/MNE/ChatGPT-（Finish）MNE-AI-ONBOARDING-FRESH-WEB-ASSESSMENT-001-20260821.md`
10. `08822407d/Mnemosyne` Issue #265：**issue body 全文与元数据**；6 条评论未读。

## 抽读

1. `indexes/archive-mech-stats.json`：前部及与体量、日期有关的条目。
2. `MA/ChatGPT-MA-通用目的元Agent建设-20260620.md`：**首 500 行、尾 500 行**；另检索并读 MA-DR-01–15 接收、综合、formal adjudication、handoff 相关命中段。
3. `MNE/ChatGPT-（Depre 01）AI Agent 记忆系统设计-20260616.md`：文件头、fresh onboarding 开场、6/23 09:41–10:17 上下文退化与 detailed handoff 段。
4. `MNE/ChatGPT-（Depre 02）AI Agent 记忆系统设计-20260623.md`：开场接收、旧对话偏差诊断、DR2/083/结尾交接相关段。
5. `MNE/ChatGPT-Mnemosyne 交接包策略-20260623.md`：任务要求、执行摘要、正确交接操作性定义、100 分 rubric、blocking gates、verdict。
6. `MNE/ChatGPT-Pro-level Mnemosyne review batch-A-20260622.md`：任务开场、评审问题、结论与建议段。
7. `MNE/ChatGPT-DR - Mnemosyne - review batch-B-20260622.md`：任务开场、Stage B 就绪问题、结论段。
8. `MNE/ChatGPT-（Depre 03）AI Agent 记忆系统设计-20260710.md`：开场 post-handoff validation、Fable/guidance-locality、结尾因上下文与浏览器性能交接段。
9. `MNE/ChatGPT-（Depre 04）AI Agent 记忆系统设计-20260709.md`：开场 Fable handoff、两步 receive/guidance、结尾交接相关段。
10. `MNE/ChatGPT-分析 Mnemosyne 加载行为-20260708.md`：问题结论、failure chain、conversation taxonomy、命令拆分与修复结果。
11. `MNE/ChatGPT-（Depre-02 01）AI Agent 记忆系统设计-20260717.md`：开场 receive-only、独立 guidance refresh、Fable STEP4 storage-only 入口。
12. `MNE/ChatGPT-（Depre-02 02）AI Agent 记忆系统设计-20260726.md`：开场 receive、独立 guidance refresh、Phase A 决策与 task-bound 范围段。
13. `MNE/ChatGPT-（Finish-02）AI Agent 记忆系统设计-20260730.md`：首次因 PR 未合并拒收、合并后重收、PR #233 准备段。
14. `MNE/ChatGPT-DR-并行工作主线治理-20260724.md`：完整任务问题集、报告 executive summary 与核心建议段。
15. `MNE/ChatGPT-DR-08_HO-GUIDANCE-001-20260728.md`：执行摘要、A/B/C 论证、task-local B 结论及表面建议段。
16. `MNE/ChatGPT-（Depre-03 01）AI Agent 记忆系统设计-20260807.md`：开场自主选题、HO 实验包、8/10 Owner 实用化指令、结尾交接相关段。
17. `MNE/ChatGPT-（Depre-03 02）AI Agent 记忆系统设计-20260813.md`：开场 receive/guidance、TLR 操作流、伪造 SHA/`worktree_clean` 事故分析、纠错后 receive。
18. `MNE/ChatGPT-（Depre-02 01）Fable5研究集中管理-20260807.md`：暂停态 receive、8/15 F1–F4 规划、交接失败链相关段。
19. `MNE/ChatGPT-（Depre-02 02）Fable5工作集中处理-20260819.md`：开场 canonical receive schema、235–243 发布/恢复/onboarding 事故链相关段。
20. `MNE/ChatGPT-(Finish)只读准备度审查-20260818.md`：任务合同、readiness 检查项和执行边界；未通读完整输出。

## 选样理由

- 6、7、8 月各自超过 4 份原件；
- 覆盖主线交接链、两份 Pro 周对话、两份以上 Deep Research、7 月 2 日 dry-run；
- 对最大文件严格读取首尾各 500 行；
- 额外偏向“目标变化点、事故点、真实 fresh-context 测试”，因为这些对 Q1、Q3、Q5、Q6 的辨识力高于随机均匀抽样；
- 未读取 `notes/cross-model-review-results/FABLE5-REVIEW2-001/` 或其中任何另一家族评估产物。

---

# 证据类别统计

- VERIFIED：58 条
- INFERENCE：24 条
- UNKNOWN：22 条
- 合计：104 个显式证据类别标签。

统计口径：按正文中显式粗体标签出现次数计数；同一条目同时含两类标签时分别计入。

# 本报告最薄弱的两个结论

1. **INFERENCE**　Q2 的 28%/47%/25% 工作量比例：没有工时账，只能从文件体量、会话类型和内容结构估计。
2. **INFERENCE**　Q7 的“GPT 最迟应在 7 月 2 日提出宏观收缩”：这是事后判断；当时模型面对的局部授权、额度和未归档约束可能使该时点并非唯一合理选择。
