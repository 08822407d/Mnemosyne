MNE-DR-024 / FABLE5-REDESIGN-001-RQ7 · 交接效果评测工具与小样本测试方法

# 交接效果评测工具与小样本测试方法：落地情报报告

研究范围严格限定为公开资料核查；未运行任何基准、未下载或执行其代码，也不替 Mnemosyne 项目选定最终测试方案。检索截至 **2026-08-31**。下文把“可复用”拆成三个等级：**可直接用**＝公开代码、数据和许可基本齐全，官方路径允许抽小样本；**可借鉴改造**＝公开材料足够形成个人规模版本，但官方评测含隐藏组件、复杂环境或许可缺口；**只可参考思想**＝未能定位可独立使用的 benchmark artifact，或重建成本/法律状态不足以支持直接使用。

## 上述基准的可复用性核查

**Q1**

### 核查总表

| 基准 | 代码 / 数据与许可证 | 原版依赖与规模 | 个人规模抽子集 | 判定 |
|---|---|---|---|---|
| **Handoff Debt** | 论文公开；本次检索**未定位到该 takeover benchmark 自身的官方代码仓库、冻结 handoff checkpoint 数据包或对应 artifact LICENSE**，故代码/交接数据 license = **UNKNOWN**。论文使用 SWE-bench Verified 作为上游任务源，但这不等于 handoff artifact 已发布。论文页面本身采用 CC BY 4.0。citeturn8view3turn22academia32 | OpenHands 风格运行时；前任在确定性阶段被中断、冻结 repo，再让 successor 看 repository-only / raw trace / summary notes / structured notes。75 个源任务生成 181 个 handoff points，每个 successor 724 次 takeover；三个 successor 共 2,172 次。实验用本地 vLLM、约 24–31B 模型，论文报告 RTX PRO 6000 Blackwell Max-Q、最长 4 小时和 500 agent steps，明显属于重型原版。citeturn8view4turn8view2turn22academia32 | **思想上非常容易缩小**：取 5–20 个真实项目 checkpoint、冻结工作目录并比较不同 handoff view 即可；但官方 181 个 checkpoint/trace 未被本次检索找到，因此不能称为复现官方子集。 | **只可参考思想**。最值得复制的是“同一冻结状态、只改变 handoff 信息”的配对实验结构，而不是原 benchmark harness。 |
| **DreamBench-SWE** | 官方仓库：[iroiro147/dreambench-swe](https://github.com/iroiro147/dreambench-swe)。仓库明确写明代码、脚本、公开 fixtures、公开分析 artifact 和 metadata 为 **Apache-2.0**；LICENSE 也给出 Apache License 2.0。但用于正式评分的隐藏 oracle / reference solution 有意不向被测 agent 暴露，公开包不是一个“把官方隐藏答案全拿走本地评分”的普通测试集。citeturn11view0turn11view1 | 多会话 SWE 任务；后续 S3 必须依赖前期**不可重推**证据，并由 executable hidden oracle 判分。v2.1 successor audit 为 360 work units / 720 S3 cells、四种条件；仓库提供 artifact requirements、smoke/validation 流程，完整 agent 路径还涉及 Docker/API agent 等。citeturn22academia34turn3view1turn11view0 | fixtures/sequence 结构是模块化的，因此**非常适合抽 5–20 个 trap schema 进行改造**。但若要声称复现官方隐藏评分，需要作者的隐藏评分组件；个人项目更合适的是复制其 trap 生成和 executable-oracle 结构。 | **可借鉴改造**。它是本课题“自建 oracle”最接近现成施工图的先例之一。 |
| **StateMemBench** | 论文公开：[arXiv 2608.19652](https://arxiv.org/abs/2608.19652)。截至本次检索，**没有定位到 StateMemBench 官方 benchmark repo/data release 或其 artifact LICENSE**；因此代码、benchmark data license 均记 **UNKNOWN**，不能以论文许可替代数据许可。citeturn22search1turn22academia33 | 234 个 multi-session scenarios、322 个 graded probes；短集约 18 sessions / 165 turns / ~3k tokens，长集约 38 sessions / 599 turns / 7–15k tokens。StateMem 原方法每 turn 可能触发一次 LLM 更新，因此约 165–600 次调用/场景；论文使用 Qwen-3.5 本地 vLLM、GPT-5.4-Nano、DeepSeek-V4-Flash 等。citeturn13view2turn13view5 | **闭池判分方法极易复制**，但在没有公开场景包的前提下只能自建类似数据，不能声称跑了 StateMemBench 子集。 | **只可参考思想**；尤其值得拿走的是 `current / superseded / other` 三分法及 anti-trap。 |
| **MemoryArena** | 官方代码：[ZexueHe/MemoryArena](https://github.com/ZexueHe/MemoryArena)；官方数据：[ZexueHe/memoryarena](https://huggingface.co/datasets/ZexueHe/memoryarena)。数据明确为 **CC-BY-4.0**。代码仓库根目录当前可见文件列表中**没有 LICENSE 文件，README 也未声明代码许可证**，故代码 license = **UNKNOWN**。citeturn14view0turn15view0turn15view1 | 五类数据配置；agent—environment—memory 多组件。WebShop 例需 Python 包、spaCy、JDK、独立产品数据库，可调用 OpenAI-compatible endpoint；search 环境涉及 FAISS、Java 21、BrowseComp-Plus corpus。仓库仍明确标为 preview。citeturn15view0turn17view0turn17view1 | 很好抽：例如 shopping config 有 `task_file_limit`，HF 数据也按任务逐行组织；甚至可关闭 LLM judge 改用 string matching。但环境本身远重于“个人会话交接”。citeturn17view0 | **可借鉴改造**。数据可直接抽，代码许可证缺口和环境复杂度使“直接照搬”不够稳妥。 |
| **Memora / FAMA** | 官方仓库：[geniesinc/Memora](https://github.com/geniesinc/Memora)，数据直接随 repo 发布。顶层 LICENSE 为 **Apache-2.0**；数据 README 明确说 dataset 同样按 Apache-2.0 发布。citeturn18view0turn19view2turn19view1 | 10 personas；weekly 约 150 sessions/persona、monthly 约 600、quarterly 约 2,000；问题数分别 15/15/30。Python 3.11 + `uv`；官方 evaluator 可 `--limit 5`。默认评分由 GPT-4.1、Claude Haiku 4.5、Gemini 2.5 Flash 三裁判多数票；agent track 还连接本地或云 memory 系统。citeturn18view0turn19view0 | **官方就提供 `--limit 5`**，并可只取 weekly 的一个 persona，因此 5–20 题非常自然。其 evaluation question 已拆成 `memory_presence` 与 `forgetting_absence` yes/no 子问题。citeturn19view0turn19view1 | **可直接用（小子集）**，同时特别适合作为“记住当前事实 + 不复活旧事实”的评分结构素材。 |
| **AgentMemBench** | 论文：[arXiv 2608.00009](https://arxiv.org/abs/2608.00009)。论文称 benchmark “fully reproducible”并描述完整代码/Docker/results，但本次针对标题、作者和 benchmark 名的检索**未定位到可确认的作者官方代码仓库或 LICENSE**，故 benchmark code license = **UNKNOWN**。其三项上游数据集是公开数据，但各自许可必须分别核查，不能用论文声明代替。citeturn22search2turn3view5 | 共 491 scored turns：LoCoMo 200、MultiDoc2Dial 187、MSC 104；比较 ICW、EKV、GEM、CBS、WAM 五种策略。统一使用 Qwen2.5-7B-Instruct 4-bit；论文称单 NVIDIA T4/P100 可运行，另有 FAISS/SentenceTransformers、spaCy/NetworkX 等依赖。citeturn4view3turn5view0 | 上游数据可以手工抽题，7B 4-bit 资源也比其他 agent benchmark 友好；但缺失可确认的官方 harness/repo 意味着实际是在“按论文重建”，而非正式 benchmark subset。 | **只可参考思想**，除非后续找到作者正式 artifact release；届时应重新核查 LICENSE。 |
| **LongMemEval** | 官方 repo：[xiaowu0162/LongMemEval](https://github.com/xiaowu0162/LongMemEval) 为 **MIT**；当前 cleaned dataset：[xiaowu0162/longmemeval-cleaned](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned) 也标 **MIT**。citeturn21view1turn21view0 | 500 题、五类能力，包括 knowledge update 与 abstention。evaluation-only 只需 Python 3.9 + `requirements-lite`; 官方 QA evaluator 使用 GPT-4o。完整 `S` history 约 115k tokens/~40 sessions，`M` 约 500 sessions；`oracle` 版本只保留 evidence sessions。citeturn20view0 | **非常好抽**：每题有 `question_id`，可直接选 5–20 项；若只想测试判分接口，可用 oracle history 大幅降低上下文开销。当前 cleaned package 全量约 3.03 GB，但并不要求个人研究先跑 500 题。citeturn20view0turn21view0 | **可直接用（小子集）**；尤其适合作为 update / abstention 的外部 sanity check，而不是直接模拟“会话交接文件”。 |

### 对“可直接用”的严格解释

这里不应把“GitHub 仓库公开”与“可合法、可独立重跑”混为一谈。MemoryArena 是典型例子：**数据许可清楚，但当前代码仓库没有可确认 LICENSE**；因此可以合法重用 CC-BY-4.0 数据，却不宜把整个代码库直接归入“已明确许可可重用”。citeturn14view0turn15view0 相反，Memora 与 LongMemEval 的代码/数据许可、子集入口都明确，是本批材料里最干净的“个人规模可直接抽取”候选。citeturn19view1turn19view2turn20view0turn21view0

另一个重要区别是**“任务结构可复刻”与“官方分数可复现”**。DreamBench-SWE 的核心价值恰恰依赖 hidden executable oracle；公开仓库有意把被测系统不应看到的内容隔离，因此它特别适合抄其实验结构，却不能把“能运行公开 smoke artifact”写成“掌握了官方隐藏测试答案”。citeturn11view0turn22academia34

## 自建 oracle 的方法

**Q2**

对个人项目，最有效的方向不是先造一个“大 benchmark”，而是把每次交接转成一个**有明确真值、可重复执行的 case**。DreamBench-SWE、StateMemBench、Memora 和 LongMemEval 实际提供了四种互补的公开先例：不可重推隐藏事实、闭池状态判断、正/负记忆约束、以及应当 abstain 的无答案样本。citeturn22academia34turn22academia33turn19view1turn20view0

### 可复制的 oracle 结构

| 类型 | 最小实现 | 适合测什么 | 公开先例 |
|---|---|---|---|
| **可执行 oracle** | successor 完成后运行一个不依赖自然语言审美的检查：测试是否通过、目标文件字段是否等于预期、指定 artifact/hash 是否存在、最终状态机是否到达目标状态。评分只取 exit code / boolean / structured value。 | “交接后工作有没有真的继续对”，而不是“handoff 写得是否像样”。 | Handoff Debt 最终仍以 SWE-bench 任务正确性为结果层；DreamBench-SWE 更进一步，把 later-session 结果交给 executable hidden oracle。citeturn8view4turn22academia34 |
| **隐藏事实探针** | 在早期会话植入随机高熵事实，例如 `handoff_secret = P7Q4-K9M2`，后续绝不重复，也不能由 repo、常识或互联网推导；successor 必须使用该值才能通过机械检查。oracle 在被测上下文之外保存真值。 | 区分“真正继承了早期信息”与“重新推理碰巧做对”。 | DreamBench-SWE 明确将后续任务设计成依赖 earlier-session 的 non-inferable evidence，并用隐藏 executable oracle 判分。citeturn3view1turn22academia34 |
| **状态闭池 oracle** | 对每个状态问题预存 `{current, superseded, other}`；答案首先用精确/规范化匹配映射到池中，而不是让裁判自由评价“差不多”。 | 旧决定被新决定覆盖后，系统是否仍复活 stale value。 | StateMemBench 明确采用 closed-pool grading，把输出归为 current state、superseded state 或其他错误。citeturn22academia33turn13view2 |
| **正负双向 oracle** | 对一份回答同时有 `must_include` 和 `must_not_include`。例如当前需求 B 必须出现，而已撤销需求 A 不得出现。 | 防止“记得越多分越高”的错误目标。 | Memora 把子问题拆成 `memory_presence` 与 `forgetting_absence`，FAMA 同时奖励保留有效记忆和不复活已删除/更新记忆。citeturn19view0turn19view1 |
| **拒答 / 拒收 oracle** | 明确列出“信息不足，正确行为是拒绝继续/请求补充”的 case，并给 `expected_action=REJECT`；不要允许随便猜一个值也获得部分分。 | handoff 缺关键字段、证据不存在时的安全行为。 | LongMemEval 把 abstention 作为独立长期记忆能力，并有专门 abstention instances。citeturn20view0 |

### 一个适合交接项目的 case 记录格式

不需要专用评测框架。一个 case 最少可以保存以下逻辑字段：

```yaml
case_id: project-017
source_checkpoint: <immutable id/hash>

early_hidden_facts:
  build_target: "P7Q4-K9M2"

state_history:
  - value: "方案 A"
    status: superseded
  - value: "方案 B"
    status: current

handoff_required_fields:
  - current_goal
  - current_decision
  - unresolved_blocker
  - evidence_pointer

probe:
  task: "继续完成下一步，并使用当前 build target"
  closed_pool:
    current: "方案 B"
    superseded: "方案 A"

oracle:
  executable_checks:
    - "result.build_target == P7Q4-K9M2"
    - "result.decision == 方案 B"
    - "方案 A not in active_decisions"
  expected_acceptance: ACCEPT
```

关键点不是 YAML 格式，而是让**真值与被测 handoff 分离**。DreamBench-SWE 的 non-inferable evidence 说明了为什么隐藏值要不可推导；Memora 的 forgetting-absence 又说明 oracle 不应只记录“必须记住什么”，还必须记录“必须不再使用什么”。citeturn22academia34turn19view1

### 隐藏事实必须做“不可重推审计”

一个糟糕的隐藏探针是：“项目使用 Python 3.11”，因为 successor 可以从 `pyproject.toml` 重新发现。更好的探针是随机 ID、一次性用户偏好、尚未写入 repo 的批准决定、实验时临时分配的随机参数，或者“用户在早期两项等价方案中随机选了哪一项”。这正是 DreamBench-SWE 使用 non-inferable earlier evidence 所试图隔离的能力。citeturn22academia34

落地时，每个隐藏探针在冻结前应人工回答三个问题：**后续输入里是否泄漏？工作区里是否可重新发现？从常识/外部检索是否可推出？** 任一答案为“是”，它就不是纯 handoff-memory probe。

### 闭池法比开放式文本裁判更适合“当前状态”

StateMemBench 的 `current / superseded / other` 很适合直接移植为项目级 oracle。citeturn22academia33 例如：

> 早期：数据库选 SQLite。  
> 后来：由于并发要求，明确改为 PostgreSQL。  
> Probe：当前数据库选择是什么？

机械分类可以是：

`PostgreSQL → current`；`SQLite → superseded`；其他 → `other`。

这比问 LLM 裁判“这个回答总体上有多好？”的信息密度更高：失败时直接知道是**旧状态复活**，还是**根本没有拿到相关信息**。

## LLM 裁判的边界

**Q3**

公开证据足以否定一种常见做法：**把单个 LLM judge 当成与机械 oracle 等价的客观测量仪器**。

FairEval 发现仅改变候选答案在 prompt 中的出现顺序，就能显著改变 LLM evaluator 的比较结果，并提出 balanced-position、multiple-evidence 与 human-in-the-loop calibration。citeturn23search1 独立的 position-bias 系统研究也发现 pairwise/listwise judge 对位置存在稳定性和公平性问题。citeturn23search0

长度同样是混杂变量。Length-Controlled AlpacaEval 显示，自动 judge 的 preference 与输出长度存在系统联系；控制长度后，指标对 verbosity manipulation 更稳健，并提高了与人类 Arena 排名的相关性。citeturn23search2turn23search10 因此，两个 handoff 若一个格式天然更长，不应让“更长、更解释性”本身成为隐藏奖励。

第三类问题是**自我偏好**。Panickssery、Bowman 和 Feng 的实验表明，LLM evaluator 能在一定程度上识别自己的 generation，且 self-recognition 与 self-preference 强度存在关系。citeturn23search3 这对交接评测尤其重要：**不要让产生 candidate handoff 的同一模型族独占主观评分权**。AgentMemBench 本身也承认生成模型与 judge 共用会带来 leniency 风险，正好可视为一个应避免的设计点。citeturn4view2

### 推荐的职责边界

**机械 oracle 应决定“有没有交接成功”；LLM judge 只处理机械规则无法合理表达的质量维度。** 例如“是否恢复了隐藏事实”“是否使用 current 而不是 superseded 值”“测试是否通过”“输入缺关键字段时是否拒绝”都应机械化；“交接摘要是否容易读”“说明是否足以让人快速理解为什么做出该决定”才适合进入 LLM/human rubric。这个划分与 DreamBench-SWE 的 executable scoring、StateMemBench 的 closed pool 和 Memora 的结构化子问题方向一致。citeturn22academia34turn22academia33turn19view1

### 校准办法

最便宜而有效的校准不是“多问 judge 一遍”，而是建立一个很小的、冻结的 **judge calibration set**，其中故意含：明显优/劣对、等价但位置互换对、等内容不同长度对、同模型/异模型来源对。正式评测前后都跑这组 anchors，并记录 judge model ID、prompt、参数和日期。FairEval 的 balanced-position calibration 和 human-in-loop 方法直接支持这种做法。citeturn23search1

pairwise 裁判至少做 **A/B 与 B/A 两个顺序**；如果 verdict 翻转，不应简单投票后隐藏分歧，而应标记为“judge-unstable”。这正面处理位置偏差。citeturn23search0turn23search1

对确实需要 LLM 判分的主观维度，可以复制 Memora 的“多模型 judge、逐子问题记录、再多数票”思路，而不是只保存最后一个总分。Memora 默认使用 GPT-4.1、Claude Haiku 4.5 和 Gemini 2.5 Flash 三个 judge，并在结果文件中保留 per-judge 明细。citeturn19view0 多裁判并不能消除共同偏差，但可以暴露裁判间不一致。

### 机械 oracle 与 LLM judge 的配比

公开文献**没有一个经过验证的通用“80/20”或“70/30”标准**，因此不能把某个比例写成学术共识。结合上述偏差证据和这些 benchmark 的实践，本项目规模下可把下面作为**工程预算线，而非文献定律**：

> **约 80–90% 的主要判定权放在机械/闭池 oracle；约 10–20% 留给 LLM judge 的主观诊断。**

这里的百分比指**最终决策权重/评分项**，不是题目数。只要某一项能机械判，就不要为了“智能”改成 LLM 判。citeturn22academia34turn22academia33turn23search1

因为总样本本来只有 5–20，人工抽查也无需按大 benchmark 的比例节省：建议对**所有会改变 pass/fail 结论的 LLM judgment 做人工复核**；其余 LLM-only 主观项至少随机复核一部分，并完整保留分歧。FairEval 明确把 human-in-the-loop 作为偏差校准手段。citeturn23search1

所谓“judge 漂移”还应分成两件事。一次实验内的随机/顺序不稳定，可以通过固定设置、换位评判和 anchor set 暴露；跨日期 provider/model revision 则应通过**固定明确 model ID、保存原始 judge 输出、不把不同 judge 版本直接合并为同一时间序列**来控制。Memora 和 StateMemBench 都固定具体 judge/model 配置并保存详细结果，这支持这种配置冻结做法。citeturn19view0turn13view4

## 小样本统计

**Q4**

当每个交接条件只有 5–20 次时，最重要的不是寻找“最强检验”，而是**让每一份样本承担尽可能少的无关方差**。因此首先应该把设计做成配对：同一个真实 checkpoint、同一个 successor 模型、相同温度/工具权限/时间预算，只改变 handoff 条件。Handoff Debt 正是通过冻结同一 repository checkpoint，再切换不同 handoff views 来隔离 handoff 信息本身。citeturn8view4turn22academia32

### 为什么配对比扩大几个随机样本更值钱

假设 case A 本身很难，case B 很简单。若 baseline 跑 A、candidate 跑 B，样本再小一点几乎无法区分是方案差异还是任务差异。配对后直接观察每个 case 的：

\[
d_i = score_{candidate,i} - score_{baseline,i}
\]

以及 pass/fail 是否发生翻转。统计对象变成**每个 checkpoint 的变化**，而不是两个高度异质的小组均值。

### 二元主指标：优先 exact McNemar / discordant pairs

若主指标是“handoff 后最终成功 / 失败”，最自然的是 paired 2×2 表：

| | Candidate 通过 | Candidate 失败 |
|---|---:|---:|
| Baseline 通过 | both-pass | **candidate-worse** |
| Baseline 失败 | **candidate-better** | both-fail |

McNemar 检验只使用两个 discordant cell；小样本可用 exact version。统计文献把 McNemar 明确作为 binary matched-pairs 的标准方法，并讨论了小样本 exact test。citeturn24search7turn24search3 DreamBench-SWE 也实际采用了 paired exact McNemar 类比较，并对多重比较做校正。citeturn10view5

这里有一个对 n=5 极其重要的算术事实：若恰好 **5 个 pair 全部都是 candidate-better、0 个 candidate-worse**，双侧 exact sign/McNemar 的极端概率仍是

\[
2(1/2)^5 = 0.0625.
\]

也就是说，**n=5 时即使方向完美一致，传统双侧 0.05 显著性门槛仍可能过不了**。到了 6 个全部同方向才是 0.03125。于是“n=5 没显著”绝不能被写成“没有效果”；这时应把原始 5 对、5:0 discordance 和效应大小放在结论中心。

### 连续指标：paired delta + exact/sign-flip permutation

handoff debt 常见的连续结果有 token 数、agent steps、重新搜索次数、恢复到第一次有效动作所需时间。对于 5–20 个 paired deltas，首先报告每个 \(d_i\)、均值/中位数变化及相对百分比，然后再做配对置换或 sign-flip sensitivity analysis。置换检验在满足其交换性/随机化条件时具有有限样本 Type-I-error 保证。citeturn24search0

20 个 pair 的全部正负号排列也不过：

\[
2^{20}=1,048,576
\]

种，所以个人机器在统计计算层面完全没有必要依赖渐近近似；真正昂贵的是 LLM run，不是 permutation enumeration。

严格地说，若实验并非随机化设计，sign-flip 需要对 paired-difference 对称性等假设保持谨慎。因此最稳妥的做法是在跑之前就随机化/平衡条件顺序、固定其他条件，并把 exact sign test 作为更弱假设的方向性检查。

### Bootstrap 可以用，但不应成为 n=5 的“确定性机器”

bootstrap 应**以 pair 为重采样单位**，绝不能把 candidate outputs 和 baseline outputs 分开重采样，否则会毁掉最宝贵的 pairing。BCa interval 可以作为效应区间的敏感性分析，但极小 n 下 bootstrap 分布本身只有很少独立信息。Hesterberg 对 bootstrap interval 的分析特别指出，普通 percentile interval 在小样本下可能有较差 coverage accuracy。citeturn24search10

因此比较可辩护的层级是：

**n≈5–7**：完整呈现所有 pairs、discordant counts、exact sign/McNemar；bootstrap 只做探索，不以 CI 是否跨零决定“有效/无效”。

**n≈8–12**：仍以 exact paired inference 为主，可同时报告 paired bootstrap/BCa CI 作为区间敏感性。

**n≈13–20**：paired permutation + effect interval 已经更有解释力，但仍不应只报 p 值。

这些区间是本报告的工程分档，不是统计学中的硬阈值；其原则依据是有限样本 exact inference 的优势，以及 bootstrap 小样本 coverage 风险。citeturn24search0turn24search10

### 效应量至少同时报“成败”和“债务”

对交接测试，比单一 aggregate score 更可解释的是两条轴：

**效果轴**：通过率差、candidate-better 与 candidate-worse 的 pair 数、`current/superseded/other` 的变化。

**成本轴**：每个 pair 的 successor token delta、agent-step delta、恢复时间 delta。

Handoff Debt 的核心贡献正是强调“最终 solved-rate 差异可能不大，但 rediscovery effort 可以明显下降”，因此只看 pass rate 会漏掉交接方案真正要优化的东西。citeturn22academia32

### 序贯停止

最简单、最难被质疑的做法是**事前固定 N，不因中途看见漂亮结果就停**。若资源必须分批，可预先写 `5 → 10 → 15 → 20` 的检查节点，但不重复使用普通固定样本 p 值来决定“显著就停止”。

若确实需要 outcome-dependent early stopping，应使用为 sequential observation 设计的 anytime-valid 方法，例如 confidence sequence。Howard 等定义的 confidence sequence 在整个时间轴上具有统一覆盖保证，正是为了避免反复查看数据造成 nominal coverage 失真。citeturn24search1 对个人项目而言，另一种更低复杂度的可辩护做法是：**允许因成本/故障停止，但不因效果方向停止；最终明确报告实际 N。**

## 对抗折设计

**Q5**

“该拒收时拒收”不能只靠放几个明显坏 JSON。一个有信息量的 adversarial fold 必须同时包含**应拒的坏 handoff**和**看起来可疑、实际上应接受的 anti-trap**；否则最保守的系统只要“什么都拒绝”就会拿高分。

这有直接公开先例。StateMemBench 专门设置 anti-trap 来检查过度 invalidation：旧事实如果仍然有效，就不能因为它“旧”而自动抹掉。citeturn13view2 DreamBench-SWE 则系统构造 stale/superseded、scope mismatch 等 memory-hygiene trap，并把 later behavior 放到隐藏 oracle 下验证。citeturn3view1turn10view2 LongMemEval 的 abstention cases 又提供了“事实上无可用证据时应当不猜”的对应侧。citeturn20view0

### 推荐的故障矩阵

| 输入变形 | 预期动作 | 设计意义 |
|---|---|---|
| handoff 写着已被后续明确替代的旧决定 | **不要采用旧值**；若当前值已知，应继续而不是整个拒收 | 测 stale suppression；对应 StateMem current/superseded 与 Memora forgetting-absence。citeturn22academia33turn19view1 |
| 同时出现 A、B 两个矛盾值，但时间/优先级明确说明 B supersedes A | **接受并使用 B** | 这是重要 anti-trap；“有冲突”不应机械等于“拒收”。citeturn13view2 |
| A 与 B 冲突，且没有任何 provenance、时间或 supersession 信息决定哪个有效 | **拒收 / 请求澄清** | 测系统是否会在无依据时自选一个漂亮答案。 |
| 缺 `current_goal`、关键 secret、下一步不可恢复 | **拒收 / 请求关键字段** | 对应 LongMemEval abstention 的基本逻辑：缺 evidence 时不要编。citeturn20view0 |
| 只缺一个声明为 optional 的说明字段 | **接受** | 防止“schema 越严格越好”的伪改进。 |
| handoff 的 task ID、checkpoint hash 与实际 workspace 不一致 | **拒收** | 测 provenance / cross-task contamination。 |
| handoff 包含冗余旧历史，但 current marker 与 evidence 均正确 | **接受** | 测误拒；避免把“长/旧”本身当毒性。 |
| handoff 内容流畅完整，但隐藏事实被删掉 | **接受 handoff 后会失败 oracle，不能由文风分掩盖** | DreamBench-SWE 的 non-inferable trap 思路：测“真正携带了必要状态”而非摘要美观。citeturn22academia34 |

### 不要只报一个“拒收准确率”

至少分别报告：

\[
TRR=\frac{\text{坏 handoff 被正确拒收}}{\text{全部应拒 handoff}}
\]

和

\[
FRR=\frac{\text{好 handoff 被错误拒收}}{\text{全部应接受 handoff}}.
\]

前者越高越好，后者越低越好。这样，一个“一律拒绝”的系统会有 TRR=100%，同时 FRR=100%，不会被总体 accuracy 掩盖。

再给一个简单的 balanced 指标即可：

\[
BalancedAcceptance=\frac{TRR+(1-FRR)}{2}.
\]

但在 5–20 个样本下，**原始分子/分母比小数点后两位的综合分更重要**。例如写“坏包 5/6 正确拒绝；好包 1/6 误拒”，远比“balanced score=83.3”透明。

### 对抗折必须冻结

不能在看见 candidate 失败后才补一个“针对它弱点”的 case，然后把这个 case 算进同一次确认性结果。DreamBench-SWE v2.1 特别强调 successor audit 在结果检查前 preregister/freeze；这就是值得复制的 anti-self-beautification 机制。citeturn22academia34

个人项目可以把 adversarial cases 分成两层：**开发折**可以持续加新 trap；**冻结确认折**一旦进入 pre-freeze test 就只读。新发现的问题进入下一版折，不回写当前版胜负。

## 持续评测流水线

**Q6**

不依赖 CI 服务完全可行。LongMemEval 的官方接口本质上就是“系统产生 JSONL hypothesis → evaluator 生成逐题 log → aggregator 汇总”；Memora 则把每次运行保存为 timestamped detailed result 与 aggregated report。citeturn20view0turn19view0 DreamBench-SWE 更强调 canonical analyzer outputs、release artifact 与冻结证据，而不是从手工表格重新拼一个漂亮结论。citeturn11view0

### 最轻量的本地流水线

每一次真实交接先产生不可变的 raw record，再评分：

```text
eval/
  cases/
    <case-id>/
      source_manifest.json
      handoff.txt
      successor_output.json
      oracle_private.json
      mechanical_score.json
      judge_score.json
      audit.json

  ledger.jsonl
  scorer/
    score_mechanical.py
    score_subjective.py
  reports/
    aggregate.json
```

`ledger.jsonl` 每行至少保存：`case_id`、source checkpoint/hash、handoff schema version、candidate version、successor model ID、judge model ID、timestamp、oracle version、机械得分、judge 得分、人工复核状态。Memora 的 result schema 同样保存 evaluation timestamp、model/memory system、judge models、逐题结果和 per-judge breakdown；LongMemEval 的 evaluator 也在逐题日志里加入 `autoeval_label`。citeturn19view0turn20view0

实际入口甚至可以只是一个本地命令：

```text
real handoff
   ↓
freeze raw artifact
   ↓
run successor
   ↓
mechanical scorer
   ↓
optional independent judge
   ↓
append ledger
   ↓
recompute aggregate report
```

关键是 aggregate report **必须从 raw record 重算**，而不是人工在报告里维护“目前 83%”。DreamBench-SWE 的 artifact discipline——固定 analyzer 输出、checksums/release metadata、区分既有发布结果与新 rerun——是很好的公开范例。citeturn11view0

### 防止“每跑一次就把自己越评越好”

最有效的不是再加一个复杂平台，而是分离四种权力：

**生成者与 oracle 分离。** successor 不得看到 hidden facts、expected answer 或 reject label。DreamBench-SWE 的 hidden executable oracle 正是这种隔离。citeturn22academia34

**生成者与主观评分者分离。** 尽量不要让 candidate handoff 的同一模型自己给 candidate 判主观质量；self-preference 的实验依据很强。citeturn23search3

**实验代码与结果编辑分离。** scoring rubric/schema/version 在本轮结果生成前冻结；跑完以后修改 scorer 必须产生新 `scorer_version`，不能静默覆盖旧结果。DreamBench-SWE 的 preregistered/frozen successor audit 是直接先例。citeturn22academia34

**raw log 与汇总叙事分离。** 报告只能由 raw logs 重算；任何人工 override 都作为独立字段保留原机器结果和 override reason，而不是直接改分。

Git 本身就足以提供一个个人规模的 append/版本历史；不要求 GitHub Actions、云 CI 或评测 SaaS。运行频率可以是“每发生一次真实 handoff 就记录，达到预定 batch 才做统计”，因此**生产记录连续、统计判断离散**，不会因每天看累计胜率而无意间做 optional stopping。

### 建议保留两条时间序列

一条是**冻结 benchmark cohort**：始终跑相同的 5–20 个 anchor cases，用来判断版本回归。

另一条是**真实 handoff cohort**：随着项目进行自然增加，只做现实世界监控。

两者不要混成一个总体分数。固定 cohort 能比较版本，真实 cohort 能体现外部效度；若新版本碰巧遇到更简单的实际交接，至少不会被误认为 benchmark 改进。这与 Handoff Debt“冻结同一 checkpoint、只换 view”的识别逻辑一致。citeturn8view4

## 三档预冻结测试素材

**Q7**

以下三档是**可组合的素材包，不构成最终方案推荐或优先级排序**。其中人力和 token 数是本报告用于规划的工程估算，不是论文实测价格。为避免把未来模型价格写死，统一以：

\[
U=20,000\ \text{input+output tokens / successor run}
\]

作为预算单位；实际项目测出自己的 \(U\) 后直接按比例替换即可。LLM judge token 另计；机械 oracle 基本不产生推理 token。

### 低档素材包

| 组件 | 可落地配置 | 依据 |
|---|---|---|
| **样本来源** | 5–8 个真实 Mnemosyne 历史 checkpoint；每个 checkpoint 同时跑 baseline handoff 与 candidate handoff。额外让其中约 2 个包含 supersession / missing-field trap。 | Handoff Debt 的核心就是冻结相同工作状态后只改变 handoff view；这是小样本 pairing 的最直接公开先例。citeturn8view4turn22academia32 |
| **Oracle** | 每 case 1 个最终可执行/structured assertion + 1 个 `current/superseded/other` probe；至少一个 case 放不可重推随机 fact。 | DreamBench-SWE 的 non-inferable executable oracle；StateMemBench 的 closed pool。citeturn22academia34turn22academia33 |
| **评分者** | **主分全部机械化**；主观 handoff 可读性只作为不计入主 pass/fail 的人工备注。 | LLM judge 有 position、自我偏好和长度偏差，因此已有机械真值时没有必要增加 judge 噪声。citeturn23search1turn23search2turn23search3 |
| **统计** | 原始 paired table + exact McNemar/sign test；报告 success-rate delta、better/worse counts、token delta。不以 n=5 的 p>.05 写成“无效”。 | Binary matched pairs 适用 exact McNemar；n=5 全同方向的双侧极限仍为 p=.0625。citeturn24search7 |
| **人力估计** | 约 **4–8 小时**：主要花在选 checkpoint、写 oracle 和人工验证不可重推性。此数为工程估算。 | 可通过只取 5–8 个 paired cases 控制规模；LongMemEval/Memora 都证明 eval interface 本身可以对极小 subset 操作。citeturn20view0turn19view0 |
| **Token 估计** | 5–8 pairs × 2 conditions × \(U\) ≈ **0.20–0.32M tokens**；机械评分额外 token≈0。 | 预算公式为本报告估算；采用 paired 两条件结构的实验依据来自 Handoff Debt。citeturn22academia32 |

这一档的优势不是“显著性强”，而是很快回答最基础问题：**candidate 是否在相同真实 checkpoint 上频繁把失败翻成成功、减少 rediscovery，并且没有明显增加 stale-state 错误。**

### 中档素材包

| 组件 | 可落地配置 | 依据 |
|---|---|---|
| **样本来源** | 10–15 个 paired cases；约 2/3 取真实历史，约 1/3 为预先冻结的 synthetic hidden-fact / stale-state / missing-field cases。 | DreamBench-SWE 展示 non-inferable synthetic trap；StateMemBench 展示状态更新和 anti-trap；混合真实与控制 case 可以同时保留外部效度与故障诊断能力。citeturn22academia34turn13view2 |
| **Oracle** | executable + closed-pool 为主；加入 `must_include/must_not_include` 双向评分和独立 reject label。 | Memora 的 memory-presence/forgetting-absence 与 StateMem closed-pool 提供直接结构先例。citeturn19view1turn22academia33 |
| **评分者** | 约 **80–90% 决策权机械化**；剩余主观项目用一个**与生成者不同的固定 judge**；A/B、B/A 两次顺序；所有会改变结论的 judge verdict 人工复核。 | position calibration 来自 FairEval；避免同模型 judge 来自 self-preference 证据；比例本身是工程建议而非文献标准。citeturn23search1turn23search3 |
| **统计** | binary：exact McNemar；连续 debt：paired deltas + exact/sign-flip permutation；paired bootstrap/BCa 只作为 CI sensitivity；事前确定一个 primary endpoint。 | permutation 有有限样本优势；普通 percentile bootstrap 在小样本有 coverage 风险。citeturn24search0turn24search10 |
| **对抗折** | 坏包与有效 anti-trap 都放入：stale、明确 supersession、无解冲突、关键字段缺失、optional 字段缺失、错误 task ID。分别报告 TRR/FRR。 | StateMem anti-trap、LongMemEval abstention、Memora forgetting-absence。citeturn13view2turn20view0turn19view1 |
| **人力估计** | 约 **1–2 人日**，其中大头是 case authoring、oracle 复核、judge calibration；为工程估算。 | 官方 benchmark 中真正可复用的是结构化 question/oracle；Memora 已展示按 sub-question 写 rubric 的轻量组织方式。citeturn19view1 |
| **Token 估计** | 12 个代表性 pairs × 2 × \(U\) ≈ **0.48M** successor tokens；加主观 judge/calibration 后可预留 **约 0.5–0.8M** 总量。 | 数值为预算假设，不是论文成本报价；实际应由首批真实 run 的 \(U\) 回填。 |

这一档开始能区分“总体不错”与具体 failure mode：candidate 是**忘了必要事实、复活旧状态、错误拒收，还是只是写得不好看**。

### 高档素材包

| 组件 | 可落地配置 | 依据 |
|---|---|---|
| **样本来源** | 15–20 个冻结 checkpoint，按任务类型/会话长度/更新次数分层；同时比较 baseline、candidate、**deliberately degraded handoff control** 三种条件。degraded control 可以故意删关键事实、插入 stale state 或移除 provenance。 | Handoff Debt 用多个 handoff views 识别信息价值；DreamBench-SWE 用明确 trap/control 形成可判别 profile。citeturn22academia32turn22academia34 |
| **Oracle** | 每 case 组合 hidden non-inferable fact、可执行最终检查、current/superseded/other、forgetting-absence、accept/reject 标签；oracle 文件和 successor input 物理分离。 | 分别取自 DreamBench-SWE、StateMemBench、Memora/LongMemEval。citeturn22academia34turn22academia33turn19view1turn20view0 |
| **评分者** | 机械 oracle 为 primary；主观层使用独立 judge panel 或两家模型交叉评判，顺序交换；固定 calibration anchors；最终 decision-changing disagreements 全部人工 adjudicate。 | FairEval 的 balanced-position/human-in-loop、Memora 的多模型多数票和 per-judge logging、自我偏好研究共同支持这种隔离。citeturn23search1turn19view0turn23search3 |
| **统计** | 预先注册 primary endpoint；binary exact McNemar；continuous exact paired permutation；报告 paired effect + interval；secondary endpoints 做明确 multiplicity control。 | DreamBench-SWE 实际使用 paired exact tests/Holm；permutation 检验有有限样本保证。citeturn10view5turn24search0 |
| **序贯** | 预写 10/15/20 checkpoints；最省争议的是不因效果方向提前停。若确需 anytime stop，则使用 confidence sequence，而非每 5 个样本重新跑普通 p<.05。 | Time-uniform confidence sequence 对任意观察时点维持覆盖保证。citeturn24search1 |
| **防自我美化** | 冻结 case fold、oracle hash、scorer version；raw logs append-only；aggregate 全部从原始记录重新算；修改 rubric 产生下一 benchmark version，绝不回写本轮。 | DreamBench-SWE 的 preregistered successor audit 和 canonical artifact 实践；Memora/LongMemEval 的逐题日志与 timestamped report。citeturn22academia34turn11view0turn19view0turn20view0 |
| **人力估计** | 约 **3–5 人日**，主要成本仍是 case/oracle 设计和复核，而不是统计代码；为工程预算。 | DreamBench、StateMem、Memora 均表明真正高价值的 benchmark 工程集中在 controlled evidence、state changes 与评分结构，而非最后一层 aggregate。citeturn22academia34turn22academia33turn19view1 |
| **Token 估计** | 20 cases × 3 conditions × \(U\) ≈ **1.2M successor tokens**；judge、校准和必要 rerun 可按 **约 1.4–2M** 规划。若实际每 run 为 50k 而非 20k，则对应约放大 2.5 倍。 | 均为透明预算公式，不代表任何厂商当前价格。 |

### 三档共同应有的最小“冻结证据包”

无论采用哪档，真正决定结果能否辩护的是以下四件东西同时存在：**冻结 case manifest、私有 oracle、原始 successor outputs、可重算 scoring ledger**。DreamBench-SWE 的隐藏 oracle/冻结审计、Memora 的逐 question/逐 judge 报告和 LongMemEval 的 output→log 流程都指向同一个结论：评测证据必须比最终的一行平均分更完整。citeturn22academia34turn19view0turn20view0

因此，对本项目而言，“预冻结效果测试”不需要追求 500 题 benchmark 的外形；5–20 个**高诊断性、成对、真值冻结、包含正例与拒收 anti-trap 的案例**，通常比 100 个靠 LLM judge 模糊打分的随机交接更能支撑设计冻结。这是综合上述公开方法得出的工程推论，而不是某一篇论文的原文结论。citeturn22academia32turn22academia34turn22academia33turn23search1turn24search0

## 来源表

**Q1–Q7 的主要一手来源如下。UNKNOWN 项均按“本次公开检索未找到足以确认的 artifact/license”处理，不由缺失信息反推许可证。**

| 来源 | 公开入口 | 本报告使用点 |
|---|---|---|
| KC & Budathoki, **Handoff Debt: The Rediscovery Cost When Coding Agents Take Over Interrupted Tasks** | [arXiv 2606.02875](https://arxiv.org/abs/2606.02875) | 冻结 checkpoint、四种 handoff view、handoff debt、配对 takeover 规模及资源配置。citeturn22academia32turn8view4 |
| Singh, **DreamBench-SWE** 论文 | [arXiv 2608.20664](https://arxiv.org/abs/2608.20664) | non-inferable evidence、hidden executable oracle、preregistered/frozen successor audit。citeturn22academia34 |
| DreamBench-SWE 官方仓库 | [GitHub](https://github.com/iroiro147/dreambench-swe) | 公开 artifact、smoke/validation、隐藏 oracle 边界、release discipline。citeturn11view0 |
| DreamBench-SWE LICENSE | [仓库 LICENSE](https://github.com/iroiro147/dreambench-swe/blob/main/LICENSE) | Apache License 2.0 原文依据。citeturn11view1 |
| Fan et al., **Can Agent Memory Systems Track Evolving State? / StateMemBench** | [arXiv 2608.19652](https://arxiv.org/abs/2608.19652) | 234 scenarios、closed-pool current/superseded/other、state tracking 与 anti-trap。citeturn22academia33turn13view2 |
| He et al., **MemoryArena** 项目页 | [项目页](https://memoryarena.github.io/) | benchmark/data structure、五种任务配置、dataset CC-BY-4.0。citeturn14view0 |
| MemoryArena 官方代码 | [GitHub](https://github.com/ZexueHe/MemoryArena) | preview framework、API/memory backend、代码仓库当前无可见 LICENSE 的核查依据。citeturn15view0 |
| MemoryArena 官方数据 | [Hugging Face](https://huggingface.co/datasets/ZexueHe/memoryarena) | 可按 config/row 抽子集、数据规模与结构。citeturn15view1 |
| MemoryArena WebShop setup | [GitHub setup](https://github.com/ZexueHe/MemoryArena/blob/main/setup_web_shopping.md) | JDK/spaCy/product DB、OpenAI-compatible backend、`task_file_limit`、LLM/string judge。citeturn17view0 |
| Uddin et al., **From Recall to Forgetting / Memora** | [ACL Anthology](https://aclanthology.org/2026.findings-acl.1337/) | 长期 personalised memory、obsolete/invalidated memory 与 FAMA 动机。citeturn18view2 |
| Memora 官方仓库 | [GitHub](https://github.com/geniesinc/Memora) | 数据、代码、`--limit 5`、模型/agent 配置。citeturn18view0 |
| Memora evaluation specification | [evals README](https://github.com/geniesinc/Memora/blob/main/evals/README.md) | FAMA 公式、多 judge、timestamped result schema、per-judge breakdown。citeturn19view0 |
| Memora dataset specification | [data README](https://github.com/geniesinc/Memora/blob/main/data/README.md) | `memory_presence` / `forgetting_absence`、weekly/monthly/quarterly 规模、dataset Apache-2.0。citeturn19view1 |
| Memora LICENSE | [LICENSE](https://github.com/geniesinc/Memora/blob/main/LICENSE) | Apache License 2.0 原文依据。citeturn19view2 |
| Cherif, **AgentMemBench** | [arXiv 2608.00009](https://arxiv.org/abs/2608.00009) | 491 turns、五种 memory strategy、7B 4-bit / 单 GPU 资源轮廓，以及 artifact release 声明。citeturn22search2turn3view5 |
| Wu et al., **LongMemEval** 官方仓库 | [GitHub](https://github.com/xiaowu0162/LongMemEval) | 500 题、knowledge-update/abstention、oracle history、lite evaluator、GPT-4o judge、MIT code。citeturn20view0turn21view1 |
| LongMemEval cleaned data | [Hugging Face](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned) | 当前 cleaned release、MIT dataset license、3.03 GB 全量大小。citeturn21view0 |
| Wang et al., **Large Language Models are not Fair Evaluators / FairEval** | [arXiv 2305.17926](https://arxiv.org/abs/2305.17926) | position bias、balanced-position calibration、multiple evidence、human-in-the-loop。citeturn23search1 |
| Dubois et al., **Length-Controlled AlpacaEval** | [arXiv 2404.04475](https://arxiv.org/abs/2404.04475) | verbosity/length confounding 与 length control。citeturn23search2turn23search10 |
| Panickssery, Bowman & Feng, **LLM Evaluators Recognize and Favor Their Own Generations** | [arXiv 2404.13076](https://arxiv.org/abs/2404.13076) | self-recognition / self-preference；评分者独立性的依据。citeturn23search3 |
| Kim et al., **Minimax optimality of permutation tests** | [Annals of Statistics](https://projecteuclid.org/journals/annals-of-statistics/volume-50/issue-1/Minimax-optimality-of-permutation-tests/10.1214/21-AOS2103.pdf) | permutation tests 的有限样本 Type-I-error 性质。citeturn24search0 |
| Fagerland et al., **The McNemar test for binary matched-pairs data** | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3716987/) | binary matched-pair 与 small-sample exact McNemar。citeturn24search7 |
| Hesterberg, **What Teachers Should Know about the Bootstrap** | [arXiv 1411.5279](https://arxiv.org/abs/1411.5279) | percentile bootstrap 在小样本中的 coverage/accuracy 风险。citeturn24search10 |
| Howard et al., **Time-uniform, nonparametric, nonasymptotic confidence sequences** | [Annals of Statistics](https://projecteuclid.org/journals/annals-of-statistics/volume-49/issue-2/Time-uniform-nonparametric-nonasymptotic-confidence-sequences/10.1214/20-AOS1991.full) | anytime-valid / sequential stopping 的统计依据。citeturn24search1 |