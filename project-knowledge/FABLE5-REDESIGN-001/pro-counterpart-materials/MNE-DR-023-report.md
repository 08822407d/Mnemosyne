# MNE-DR-023 / FABLE5-REDESIGN-001-RQ6 · 文件/Git 真相源上的检索与按需加载

**研究日期：2026-08-31；范围：公开资料，重点为 2025–2026 年实践与实证。**

本报告所说的“真相源”专指：**Git 仓库内 Markdown/YAML 等原始文件保持唯一权威，任何目录、登记表、全文索引、摘要、embedding 或向量库均视为可重建的派生层**。证据标签采用：**[论文实证]**、**[厂商文档]**、**[社区实证]**、**[工程归纳]**、**[UNKNOWN]**。尤其需要先说明一个贯穿全文的结论：截至本次检索，**没有发现可信公开研究给出“知识库小于 X MB 就不需要向量检索”的通用阈值**；公开实证更多按“文档/块数量、查询类型、词汇重叠、任务难度”而不是按 MB 划界，因此不能把某个文档数实验机械换算成 10–50 MB 阈值。citeturn15search0turn20academia8

## 中小规模文本库的检索实证

**Q1 · 中小规模文本库的检索实证**

### 直接比较证据

最接近本任务规模问题的一项 2026 年系统实验是 *As We May Search*。研究在消费级硬件上比较 dense、BM25 与 hybrid，并把集合规模从 **1K 扩展到 1M documents**。在其受控扩缩实验里，dense 的 nDCG@10 在 1K/10K/100K/1M 文档时约为 **0.990/0.969/0.910/0.736**，BM25 约为 **0.835/0.711/0.592/0.409**，未专门调优的 hybrid 约为 **0.958/0.903/0.849/0.680**。这里一个很重要的反例是：**hybrid 并不自动优于最好的单路检索**；作者的融合权重与数据条件让 dense 单独领先。citeturn2view1turn2view2turn15search0

同一实验说明，小库上的主要工程差异往往不是“搜不搜得动”，而是**是否值得为语义召回支付 embedding 初始化与派生状态维护成本**。其参考实现中，dense 冷启动时间从 1K 文档约 2.4 秒增到 100K 约 3.2 分钟、1M 约 47.5 分钟；BM25 对应约 17 毫秒、2.1 秒和 19 秒。作者也明确提醒其 Python `rank_bm25` 查询实现不是工业级倒排引擎，PISA、Pyserini、Tantivy 等原生实现会快一个到两个数量级，因此这些绝对延迟不能直接拿来预测 SQLite FTS5/Tantivy。citeturn2view1

作者把本地 dense 的经验区间概括为：**低于约 10K documents 时冷启动仍很轻，10K–100K 仍保持较高检索质量，100K 以上 embedding 冷启动与扩缩成本才迅速突出**。但这是“documents”的实验结论，不是“MB”的无向量阈值；对一个文档可长可短的 Markdown 库，把 10K documents 换算为 10 MB、50 MB 或任何固定字节数都没有证据依据。citeturn2view1turn15search0

更重要的是，**查询性质可以反转排序**。2026 年一个金融文档 QA 实验发现，领域术语、精确标识符和表格语境下 BM25 非常有竞争力；hybrid 总体优于单路，但融合算法与参数显著影响结果，例如经调优的线性组合 Recall@5 达到约 0.726，而一个 RRF 设置约为 0.695，后续 cross-encoder reranking 又能明显提高排名指标。也就是说，“加向量”不是一个单参数升级，而是会引入 chunking、融合和 reranking 的新调优面。citeturn1view1

另一项 2026 年规模很小、因此只能列为 **[社区实证]** 的 section-level RAG 基准尤其值得本任务注意：45 个查询、3 篇 arXiv PDF 中，按章节标题形成强词法边界后，keyword-section MRR 约 **0.53**，hybrid-section 反而约 **0.36**；作者分析其原因为 dense 通道引入的相似但错误章节经 RRF 把 BM25 的正确 rank-1 往下推。样本很小且不是正式同行评审，但它提供了一个有价值的失败样本：**结构化良好的文档中，heading/path/title 本身可能就是极强的检索信号，hybrid 也能因语义噪声变差。** citeturn1view3

长上下文研究从另一方向说明为什么“反正库小，全部塞进去”也不是理想基线。NoLiMa 在 12 个支持至少 128K context 的模型上去除了明显词汇匹配后，发现从短上下文增长到 32K 时，12 个模型中的 10 个跌到其短上下文基线的 50% 以下；GPT-4o 的一个结果从 99.3% 降到 69.7%。Chroma 2025 年对 18 个模型的受控实验也发现，即使任务复杂度不变，输入长度增加仍会产生非单调、模型相关的性能下降。citeturn20academia8turn20search0

### 四类方案在本项目语境下的证据画像

| 方案 | 已有实证最支持的场景 | 主要失败面 | 对“数百 Markdown/YAML、数 MB”含义 |
|---|---|---|---|
| **grep/ripgrep / 精确关键词** | 文件名、标题、变量名、ID、规则编号、错误码、专有术语；无派生索引所以没有 index drift。ripgrep 默认递归、遵守 `.gitignore`、跳过隐藏/二进制文件，并持续维护到 2026 年。citeturn18search0turn18search12 | 同义改写、隐含概念、查询词与原文词汇差异大时 recall 下降；结果本身没有 BM25 式相关性排序。citeturn20academia8 | **最低维护成本基线非常强**；该量级没有性能证据逼迫引入向量。是否需要升级主要取决于 lexical miss，而非 MB。 |
| **结构化索引：目录＋登记表＋metadata** | 文档本身有 doc type、path、authority、state、effective date、topic 等结构时，可先做确定性裁剪；coding-agent 厂商正大量使用路径作用域和分层规则。citeturn13search0turn13search3turn14search0 | 登记表本身可能 stale；人工分类漏项；跨领域问题可能不符合单一路由。 | 对 Git 真相源尤其自然；其价值首先是**适用性过滤和按需加载**，不是替代内容检索。 |
| **dense embeddings** | 查询与原文词汇重叠低、存在同义改写或语义关联时；小集合也可能从 dense 获益，因此“库小就不需要语义检索”并不成立。citeturn15search0turn20academia8 | 旧版和新版常因只改一个值而在 embedding 空间几乎相邻；精确标识符也可能不如词法检索；另有模型、chunking、re-embedding 生命周期。citeturn21search1turn21search4 | **应由代表性查询中的 semantic miss 触发，而非文件量触发。** |
| **hybrid** | lexical 与 semantic 互补、且有验证集可调融合时通常是稳健升级方向。citeturn1view1 | 并非“BM25+dense=必然更好”；噪声 dense 结果可把正确 sparse rank-1 降级，fusion 参数与 chunk 粒度成为新失败面。citeturn1view3turn15search0 | 更适合作为已有 BM25 基线证明 recall 不足后的升级，不应成为无测量的默认复杂度。 |

### 关于“规模多大之前根本不需要向量”

**[UNKNOWN]：没有找到可 defend 的 10 MB、20 MB、50 MB、N 个文件之类公共阈值。** 现有证据支持的判断变量是：

**第一，词汇错配率。** 当用户常以原文没有出现的表达提问时，dense 在很小的库也有价值；反之如果查询多为文件名、规则号、API 名、状态名、标题和精确术语，BM25/grep 可能长期足够。citeturn20academia8turn1view1

**第二，适用性复杂度。** 只要“当前版/历史版、适用路径、文档权威等级”很重要，问题就已经不是纯 similarity search；即使只有几十份文件，也需要结构化过滤。版本化文档研究和法律 RAG 都显示，单纯检索最相似文本不足以判断哪一版适用。citeturn21academia24turn21search2

**第三，上下文污染而非磁盘容量。** 更多可加载文本不等于应该加载更多。受控研究显示 distractor 和长上下文会降低模型表现，所以“库只有几 MB，全塞入 prompt”不是向量数据库的合理零成本替代。citeturn19search1turn20search0

因此，对题述“**数百文件、约数 MB、继续增长**”的案例，证据允许得出的最强结论是：**没有规模理由要求现在就做 dense/vector；但也没有规模理由证明永远不需要。是否升级应该由实际查询集中的 lexical-recall 缺口决定。**

## 编码代理的按需加载机制

**Q2 · coding-agent 生态的按需加载机制盘点**

2025–2026 的 coding-agent 生态已经明显从“一个巨大的全局 instructions 文件”向**分层、路径作用域、触发式、技能式和按需读取**演进。这与任务书中的“记录≠加载”原则高度一致，但公开实证同时表明：**规则文件存在本身并不保证提高任务成功率；加载不必要的规则很可能增加推理和工具成本。** citeturn13search0turn15search1turn15search2

| 生态 | 当前公开机制 | 公开失败/限制 |
|---|---|---|
| **Claude Code** | 当前工作目录及祖先层级的 `CLAUDE.md` / `CLAUDE.local.md` 在启动时加载；当前工作目录以下的 nested `CLAUDE.md` **等到 Claude 读取相应子目录文件时才进入上下文**。`.claude/rules` 可按路径作用域；`InstructionsLoaded` hook 还能记录何时、为何加载某个规则。citeturn13search0turn13search6 | Anthropic 明确写道：模糊或冲突规则没有严格遵循保证；冲突规则可能被任意选择。文档还警告 **CLAUDE.md 超过约 200 行会消费更多 context 并可能降低 adherence**，超过 4 MiB 的单文件会被跳过，建议转成 path-scoped rules。citeturn13search0 |
| **Claude auto-memory / skills** | auto-memory 以 `MEMORY.md` 作索引并可拆 topic files；当前文档规定每次会话常驻加载 MEMORY.md 的前 **200 行或 25 KB**，更详细 topic files 由文件工具按需读取。Skills 更彻底：skill body 仅在被使用时加载，且可用 `paths` glob 限定自动激活。citeturn13search0turn13search2 | 如果关键内容被放到未触发的 topic/skill，可能产生漏加载；反之描述过宽则过度触发。官方因此提供 `/context` 等机制检查实际加载集合。citeturn13search0turn13search2 |
| **Cursor** | Project Rules 存于 `.cursor/rules`；公开规则机制包含 always、按智能判断触发、按文件 glob 触发和显式调用；当前生态也把 dynamic rules 向 skills 方向整合。`AGENTS.md` 被提供为更简单、少元数据的替代。citeturn14search0turn14search2 | 智能触发依赖描述/模型判断，glob 则依赖路径匹配，因此分别有“不触发”和“匹配范围错误”的失败面；这类错误与人工条件加载表本质相同，只是触发器由产品运行时执行。citeturn14search0 |
| **GitHub Copilot** | repo-wide 使用 `.github/copilot-instructions.md`；path-specific 使用 `.github/instructions/*.instructions.md` 的 `applyTo`；若当前文件同时匹配 repo-wide 与 path-specific，则两者都会加载；`AGENTS.md` 可多层存在，目录树上最近者优先。Copilot CLI 也只在 `applyTo` 匹配当前工作文件时包含 path-specific instructions。citeturn13search3turn13search9 | GitHub 明确警告行为具有非确定性，长 instruction 文件会出现规则被忽略；其代码审查指南建议单文件约不超过 1,000 行，并强调短、清晰、具体。不同 Copilot surface 对不同 instructions 类型的支持也不完全相同。citeturn13search1turn13search12 |
| **AGENTS.md 生态** | 公共规范支持仓库中的嵌套 AGENTS.md，monorepo 中通常由更接近目标文件的规则覆盖/细化上层规则；该格式已由多种 coding agents 采用。citeturn12view3 | 格式互操作不代表各 agent 的加载和优先级完全一致；例如 Claude Code 官方仍以 `CLAUDE.md` 为原生记忆格式，并建议需要兼容时从 `CLAUDE.md` 引入 `AGENTS.md`。citeturn13search0 |

### 最关键的失败实证

2026 年 *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?* 在 SWE-bench 类任务与含开发者真实 context files 的仓库任务上测试多个 agent/LLM，结论相当反直觉：**context files 整体倾向于降低任务成功率，同时把 inference cost 提高超过 20%**。行为分析发现，agent 的确会遵循这些文件，但因此进行更多目录遍历、测试和探索；额外要求本身可能让任务变难。论文据此建议人工 context files 只保留最小必要约束。citeturn15search1turn15search9turn15search24

需要保留统计上的细节：该研究内部并不是“任何人工规则必然有害”；开发者编写 context 和自动生成 context 的方向存在差别，而且部分差异并不统计显著。因此不能从论文推出“删除所有 AGENTS.md”。能可靠推出的是：**“更多持久上下文一定更好”缺乏证据，而额外 token、步骤与要求有可测成本。** citeturn15search9turn15search24

2026-07-28 的另一项独立消融研究进一步测试 Claude Code 和 Codex、17 个真实任务、288 次评估运行；其结论是，不同 context-file 注入策略**没有可测量地改变两种 agent 的 correctness**，等价性检验把可检测效应约束在 10–15 个百分点以内。其失败归因更多指向 feature design、pattern selection 和 exact wiring，而非缺少一个通用 repo context 文件。citeturn15search2turn15search6

因此，对本项目最相关的经验不是“维护更大的核心集”，而是：

> **常驻层只放“每个任务都必须知道且无法安全从文件现查”的小集合；其余规则尽量绑定路径、文档类型、任务类型或显式 skill，并且必须能观测“这次到底加载了什么”。**

这与 Claude Code 当前的 nested lazy loading、path-scoped rules、topic memory 以及 GitHub/Cursor 的 path-specific instructions 是同方向的工程模式；但截至目前，没有找到大规模随机实验直接证明“路径懒加载比人工分层表提高 X% 成功率”，因此该因果收益仍应标为 **[UNKNOWN]**。citeturn13search0turn13search3turn14search0

## 派生索引的漂移与一致性

**Q3 · 派生索引的漂移问题**

这里最重要的架构原则不是“怎样让索引永远正确”，而是**怎样让任何派生层出错时都不能篡夺 Git 原文的权威地位**。数据库和 RAG indexing 工具的公开实践基本形成了四类一致性策略。

SQLite FTS5 对 external-content table 的文档非常直接：**FTS 索引与内容表的一致性由使用者负责**；可通过 triggers 跟随增删改，而一旦两者不一致，可以执行 `rebuild`，丢弃现有全文索引并从当前内容重新构建。这里尤其有一个典型坑：事后才增加同步 trigger 并不会自动修复此前已经漏掉的历史内容，因此仍需一次完整重建。citeturn16search0

LlamaIndex 的文档管理采用另一种常见模式：docstore 维护 document identity/hash，对新文档插入、对 hash 改变的文档重新处理，并在相应的 `UPSERTS_AND_DELETE` 策略下删除源集合中已消失的文档。这说明**content hash + stable source id** 已是公开 RAG 索引实践中的标准组成，而不是必须依赖时间戳猜测变化。citeturn7search0turn7search4turn7search10

针对 Git 真相源，可把四类对策映射为：

| 时点 | 证据支持的模式 | 适合本项目的实现含义 |
|---|---|---|
| **生成时校验** | 基于 source/document identity 与 content hash 判断“新增、未变、更改、删除”，仅重新处理变化项。citeturn7search4turn7search10 | 每个派生记录至少绑定 `source_path`、稳定 document id、source content hash；可再附 Git commit/blob id、generator version。这些附加字段是**工程建议**，不是某篇论文规定。 |
| **CI 校验** | 上述 hash/incremental indexing 原理允许在构建管线中验证派生数据是否对应当前源；SQLite 也提供完整重建作为最终一致性手段。citeturn16search0turn7search10 | **[工程归纳]** CI 可重新生成 manifest/index 并要求工作树无未提交差异，或逐项比较 source hash；失败即禁止把派生层视为 current。 |
| **访问时校验** | 本次检索未发现一个成为跨工具事实标准的“每次 retrieval 都验证源 hash”协议。**[UNKNOWN]** | 对高价值规则可在返回结果前比对当前 source hash；不一致就丢弃派生内容、直接读取 Git 原文。对几 MB 库，这种 fallback 的成本通常很容易接受，但应由本项目自行 benchmark。 |
| **定期/故障后重建** | SQLite FTS5 官方 `rebuild` 明确把“丢弃索引并按当前内容重建”作为恢复不一致的方法。citeturn16search0 | 派生索引应设计成 disposable artifact；重建应是正常维护动作，而不是灾难恢复特例。 |

这意味着“登记表”也应被分成两类。**人工语义判断**，例如某份规范的 authority、适用域、是否 current，可能本身就是业务事实，应回写到 Git 中某个明确的源文件；而**可以机械推导的字段**，如标题、路径、hash、mtime、heading、chunk offsets，不宜人工维护第二份真相。否则所谓“结构化索引”只是把 stale-index 风险从向量库移到了 Markdown 表格里。

对本项目，一个尤其安全的 invariant 是：

`检索索引损坏/过期 ⇒ 最多降低 recall 或性能；不能改变哪份文件是真相。`

实现上应让每个检索命中都能反向定位至 **source path + source revision/hash + 原文 span**。这个设计是根据 SQLite 可重建索引、LlamaIndex hash-based refresh 以及后述版本检索失败实证作出的**工程归纳**。citeturn16search0turn7search10turn21academia24

## 规则规范文本中的版本与适用性失败

**Q4 · 规则/规范文本场景的检索失败模式**

这是本研究中对“不要只靠 embeddings”最强的一组证据。

2025 年 *VersionRAG* 专门构造了**会演化的技术文档**问答基准：100 个手工整理问题、34 份 versioned technical documents。普通 naive RAG 达 **58%**，GraphRAG **64%**，显式建模版本序列、内容边界和变更，并在检索阶段执行 version-aware routing/filtering 的 VersionRAG 达 **90%**；在隐含变更问题上 VersionRAG 为 **60%**，对照方法只有 **0–10%**。这说明“语义最相似”与“版本正确”是两个不同的判定维度。citeturn21academia24

2026 年德国成文法研究用 **312 个专家验证的时间敏感 QA 对**研究 post-cutoff staleness 和 recency bias。两种强制执行 fact-date extraction + version filtering 的 RAG 设置都显著改善表现，而普通 web search 对历史问题出现不稳定收益和明显的 **recency bias**。作者的核心结论是：可靠的时间敏感 QA 应把 temporal validity 当作**硬约束**，而不是一个“越新越高分”的软偏好。citeturn21search2turn21search5

另一篇 2026-08-10 的法国税法研究把现象命名为 **temporal misgrounding**：系统会检索和引用“今天仍有效”的版本，即使问题所需的是更早或未来生效的版本。也就是说，简单使用 `latest=true` 仍然会把 historical/as-of 查询做错；正确条件必须是“对问题中的事实时间有效”。citeturn15search3turn21search8

最直接针对 embedding 的反证来自 2026 年 *Temporal Validity in Retrieval Memory*。在 98 个标注 pair 上，仅用 cosine similarity 区分“只是同义复述”与“对旧事实的矛盾/更新”，AUROC 只有 **0.59**；作者观察到值被修改后的矛盾句往往比真正的改写还更接近原句。其普通 RAG 在变化知识上被迫回答时，会有约 **15–40%** 的情况给出 superseded value，而显式确定性 supersession 机制把该类错误压到接近零。citeturn21search1turn21search4

对 Git/代码语境还有一项非常新的、但需要谨慎看待的 2026-08-21 预印本：作者从 707 个真实 GitHub issues 中筛出 130 个“干净的原子状态变化”，普通 RAG 准确率约 **0.57–0.59**，确定性 supersession 方法约 **0.91**；普通 RAG 被迫回答时 **36–38%** 会给旧值。作者同时明确承认这种 clean atomic transition 只覆盖真实 fixes 的约 18%，因此它不能证明一套 supersession schema 能解决所有代码演化，但它非常直接地验证了“新旧配置/API 值高度相似，semantic retrieval 无法自动知道谁 current”这一失败面。citeturn21academia26

### 对规则库最合理的检索顺序

上述证据支持的不是“给 authority/freshness 多加一点分”，而是**先排除不适用项，再排名相关性**：

1. **硬适用性过滤**：repo/ref、scope/path、document type、jurisdiction/domain、lifecycle state、`valid_from ≤ as_of < valid_to` 等。历史查询中的旧版本不是“低 freshness 的坏结果”，而可能正是唯一正确结果。citeturn21search2turn21academia24
2. **权威性约束**：把 canonical/approved/authoritative source 与 note/draft/derived summary 区分。**[UNKNOWN]**：本次没有找到针对 Markdown 规则库、公开证明某套固定“authority score 权重”最优的标准基准，因此更安全的做法是把不允许回答的低权威源做 hard gate，而不是靠小幅 score penalty。
3. **相关性排名**：通过 heading/path/BM25，必要时再加 dense；dense 负责“含义相近”，而不是负责“当前有效”。citeturn21search4turn1view1
4. **冲突检测**：如果仍存在两个同权威、同适用时间且相互冲突的 current source，系统应暴露冲突并回到源文件，而不是让最高 cosine score 隐式决定真相。这是由 version/temporal failure evidence 导出的**工程归纳**。citeturn21academia24turn21search1

所以，在规则/规范场景中最危险的数据模型是只有：

`{chunk_text, embedding}`

更稳健的候选至少应保有类似：

`{source_id, revision_id, source_path, authority, lifecycle_state, valid_from, valid_to, content_hash, chunk_span, text}`

其中哪些字段必需，应由实际项目语义决定；关键不是字段名，而是**“适用性/当前态不能从 cosine similarity 推断”**。citeturn21search2turn21search4

## 本地 CLI 组件与成熟度

**Q5 · 可嵌入本地 CLI agent 的检索工具现状**

题述规模并不要求一个常驻搜索服务。2026 年可用组件已经覆盖“完全无索引扫描 → 嵌入式 BM25 → 嵌入式向量 → hybrid”，可以把复杂度逐档增加。

| 组件 | 能力 / 当前成熟度 | 维护面 | 对本项目的角色 |
|---|---|---|---|
| **ripgrep (`rg`)** | 成熟的跨平台递归 line-oriented regex search；默认识别 `.gitignore` 并过滤隐藏/二进制内容。2026-07-15 发布 15.2.0，仍在修复 ignore matching 并优化大 corpus 遍历。citeturn18search0turn18search12 | **极低**：无索引、无 schema、无 embedding；注意 `.gitignore` / `.rgignore` 可能导致“实际上存在但被过滤”的文件。citeturn18search21 | 最好的 Tier-0 fallback；agent 可要求先 `rg` 再精确读取文件。 |
| **SQLite FTS5** | SQLite 官方全文检索模块，支持 BM25 ranking、column filtering/weighting、prefix/phrase 查询；单数据库文件，无搜索服务。citeturn16search0turn16search15 | **低至中**：需定义 tokenizer/schema 与更新方式；external-content 模式若同步错误会 stale，但有 triggers/rebuild 恢复机制。citeturn16search0 | 对 Markdown/YAML 建 `title/path/tags/body` 多字段 BM25 是很自然的第一层索引。 |
| **Tantivy** | Rust 编写、受 Lucene 启发的全文搜索库，支持 incremental indexing；不是一个必须部署的 Elasticsearch 类 server，而是供应用嵌入的 library。citeturn18search1 | **中**：要承担 Rust binding/schema/index writer；文档更新采取 delete + re-index，commit/reload 后新结果才可见。citeturn18search1 | 当 SQLite FTS5 的排名、吞吐或 tokenizer 不够时再考虑；题述数 MB 规模目前没有性能证据要求它。 |
| **sqlite-vec** | 极小、纯 C、无外部依赖的 SQLite vector extension，可把向量和 metadata 放在同一个 SQLite 体系。官方 README 截至访问日仍明确标注 **pre-v1，预计会有 breaking changes**。citeturn16search2 | **中**：API 稳定性明显低于 SQLite FTS5；早期 v0.1 明确以 brute-force 为主，项目另设 ANN 工作项，因此在把它当大规模 ANN 基础前应重新核验当前版本能力。citeturn16search5 | 对数千/低万级 chunks 的“小型 semantic sidecar”有吸引力，尤其可与 FTS5 共数据库；成熟度风险必须单列。 |
| **FastEmbed** | Qdrant 维护的轻量本地 embedding library，基于 ONNX Runtime，不要求 GPU，也不必安装 GB 级 PyTorch 依赖；首次使用会下载/初始化模型。citeturn18search2 | **中**：仍要固定 embedding model/version、下载与缓存模型、批量 re-embed；模型升级会导致派生向量生命周期。 | 适合作为“证明 BM25 recall 不足后”加入的本地 embedding producer，而非真相层。 |
| **FTS5 + sqlite-vec hybrid** | 2026 年已有 local-agent 社区设计直接提出“一个 SQLite 文件同时承载 FTS5 BM25 与 sqlite-vec vector，零独立 server process”。这是集成先例/设计讨论，不是经过长期生产验证的厂商 SLA。citeturn16search8 | **中到高**：要同步两套索引并定义 fusion、版本过滤与重建。 | 很符合本任务“无服务依赖”的上限方案，但应在 Tier-1 FTS5 有 benchmark 后才引入。 |

### 一个容易被忽视的“工具成熟度”差异

`rg` 和 SQLite FTS5 的最大优势不仅是快，而是**状态空间小**：前者直接搜真相源，没有派生状态；后者只有可重建的词法索引。加入 embeddings 后，必须额外管理“chunking algorithm version、embedding model/version、vector dimensions、re-embed trigger、fusion configuration、semantic regression benchmark”。sqlite-vec 把运行时依赖压得很小，并没有消除这些语义维护成本。citeturn16search2turn18search2

因此“本地运行/零服务”与“零维护”是两回事。对长期 Git 真相源，最有价值的属性往往不是检索引擎的峰值 QPS，而是：**index 是否可一条命令重建、每个 hit 是否可追溯到当前 Git 原文、发生 mismatch 时能否可靠降级到 `rg`/直接读取。** 这是综合 SQLite FTS5 重建机制、版本检索失败和 coding-agent 文件按需读取方式得到的工程判断。citeturn16search0turn13search0turn21academia24

## Token 预算下的选择与污染测量

**Q6 · Token 预算下的选择策略**

公开研究并不支持一个固定的：

`0.6 * relevance + 0.2 * authority + 0.1 * freshness + 0.1 * current_state`

之类“通用最优公式”。尤其 **freshness 不是单调正效用**：历史问题里越新的规则可能越错误。德国法律 QA 的 recency-bias 实验证明，时间有效性应成为查询条件，而不是简单偏好 newer document。citeturn21search2turn21search5

### 更符合证据的预算算法

**第一层：Eligibility gate，不花 token 给明知不适用的材料。**

先根据 scope/path、authority 下限、lifecycle state、validity interval、branch/ref 等结构条件裁剪集合。这一步把 **current-state / applicability** 从相似度问题中拿出来。VersionRAG 和 temporal legal RAG 的结果都支持这种 version-aware hard filtering。citeturn21academia24turn21search2

**第二层：Relevant candidate retrieval。**

先跑便宜且可解释的结构路由 + BM25/`rg`。对 query 存在明显 paraphrase/概念性表达，或 lexical candidate 分数低、无命中、benchmark 已知此类 query 容易 miss 时，再启用 dense 通道。若两路都启用，fusion 参数必须在项目自己的 query set 上验证；公开实证已经出现 hybrid 胜、dense 胜、BM25 胜三种情况。citeturn1view1turn15search0turn1view3

**第三层：Adaptive context size，而不是固定 top-k 填满预算。**

2025 年 Dynamic Context Selection 的受控测试发现，2-hop 问题只加入一个 distractor，性能就下降 **超过 26%**，更多 distractor 的影响会累积。另一项 Adaptive-k 研究在不同 QA 条件下，用 similarity score 分布决定文档数，可比固定 k 更省上下文；这些工作共同说明，“预算还有空位”不是继续装文档的理由。citeturn19search1turn19academia31

**第四层：必要时做 coverage-controlled pruning。**

2025/2026 的 conformal context engineering 实验在 NeuCLIR 和 RAGTIME 上做到目标证据 coverage 的同时把保留 context 压缩约 **2–3 倍**，且中等/严格过滤下 factual quality 稳定或改善。它比“固定取前五条”更接近一个可校准的 token-budget policy，但实现复杂度也明显高于本项目初期所需。citeturn19search8turn19academia28

### 如何定义“上下文污染率”

Ragas 的 **Context Precision** 已提供一个公开、可复用的检索指标：考察 relevant chunks 是否排在 irrelevant chunks 之前，本质上对各 rank 的 precision 进行汇总。它适合作为基础指标，而不是只看“答案最后对不对”。citeturn19search3turn19search6

针对本任务，可以在此基础上增加三项**项目自定义指标**；下述名字与公式不是行业标准，因此明确标为 **[工程归纳]**：

\[
\text{Token Pollution Rate}
=
\frac{\text{irrelevant + wrong-scope + wrong-version tokens}}
{\text{all retrieved context tokens}}
\]

它回答最直接的“装了多少没用或有害的东西”。对规则库，**wrong-version 应计入污染，而不只是 irrelevant**，因为其语义往往高度 relevant、事实却已经失效。该分类必要性由 temporal retrieval 实证支持。citeturn21search1turn21academia24

\[
\text{Stale Context Rate}
=
\frac{\text{superseded-source tokens loaded}}
{\text{all rule/source tokens loaded}}
\]

这能把“旧规则被命中”从普通 precision 中独立出来；MemStrata 一类工作实际上采用 stale-fact error 作为核心评价维度，说明单独测 temporal failure 很有价值。citeturn21search1turn21academia26

\[
\text{Rule Scope Error Rate}
=
\frac{\text{loaded rule units whose path/task applicability is false}}
{\text{all loaded rule units}}
\]

它尤其适合评估人工分层表、Cursor/Copilot globs 和 nested instruction routing。官方工具已经提供“检查实际加载了什么”的观测机制，例如 Claude Code `/context` / `InstructionsLoaded`，说明 load-set observability 本身已经成为产品能力。citeturn13search0turn13search6

还应同时测**端到端成本**。AGENTS.md 研究非常有启发性：即使一个 context 文件被模型认真遵循，它仍可能让 agent 多搜索、多测试、多走步骤，最终不提高正确率且增加 20% 以上 inference cost。因此推荐每个 retrieval/load policy 至少同时记录：

`task success / critical recall / context precision / stale rate / loaded tokens / agent steps or tool calls`

而不是仅优化 retrieval recall。citeturn15search1turn15search2

Chroma 的 18 模型 Context Rot 测试进一步说明，上述“token pollution”不能只理解成账单成本；即使模型支持很大的 advertised context window，性能也可能随额外输入增长而下降，所以**少加载是可靠性优化，不只是价格优化。** citeturn20search0

## 证据结论与候选升级路径

**Q7 · 结论清单**

以下是**证据支持的候选与升级路径，不是替委托方做最终选型裁决**。

### 最低成本候选

对题述现状——**数百 Markdown/YAML 文件、数 MB、Git 唯一长期真相源、已有人工核心集＋条件触发集**——公开证据最支持把最低复杂度候选定义为：

**Git 原文 + 人工/路径分层 + `rg` + 一个可校验的轻量结构登记层。**

理由不是“这个库太小，embeddings 没用”，而是：

- `rg` 对 Git 文本没有索引漂移，工具成熟且仍积极维护；精确名词、规则号、文件名、状态值等是其天然强项。citeturn18search0turn18search12
- Claude Code、Cursor、Copilot、AGENTS.md 的当前设计都表明，**路径/作用域驱动的按需 instruction loading 已成为主流工程模式**，并非落后的临时方案。citeturn13search0turn13search3turn14search0
- coding-agent 的 2026 实证反而警告，不必要的常驻 context 会增加成本乃至降低成功率。citeturn15search1turn15search2
- 没有找到任何按 MB 给出的证据，能证明此量级必须建 vector layer。citeturn15search0

这里建议给现有人工分层表补的不是 vectors，而首先是**可测性**：每条代表性任务记录“理想应加载哪些 source、实际加载哪些、漏了哪些、装错哪些、最终用了多少 token”。没有这样的 eval set，就无法知道未来 BM25/vector 究竟解决了真实问题还是只增加了系统组件。

### 有证据支持的渐进式升级阶梯

| 候选档位 | 增加的东西 | 何时有证据理由升级 | 维护代价 | 主要失败面 |
|---|---|---|---|---|
| **人工路由 + `rg`** | 现有核心/条件表；路径约定；直接 grep 原文 | 默认基线。适合路径、heading、ID、规则名和任务类别高度可预测的库。厂商 lazy/path rules 与 agent-context 实证均支持保持常驻上下文小。citeturn13search0turn15search1 | **低** | 人工 trigger 漏项；表变 stale；同义改写 recall 不足；跨领域任务不知道该走哪条 route。 |
| **结构 manifest + SQLite FTS5/BM25** | 自动抽取 title/path/headings/tags/hash，加 FTS5 排名；保留 `rg` fallback | 当人工 route 的候选集开始变多、全文关键词常要多次 grep、希望有 top-k ranking，或需要统一字段过滤时。SQLite FTS5 原生支持 BM25，且可完整 rebuild。citeturn16search0turn16search15 | **低—中** | tokenizer/schema；manifest/index drift；人工填写的 authority/state 元数据本身可能错。 |
| **本地 dense sidecar** | FastEmbed 等本地 embeddings；sqlite-vec 或其他本地 vector store | **不是按 MB，而是在代表性 eval 中证明 lexical retrieval 因 paraphrase/概念表达持续漏掉正确源时。** NoLiMa 等实验证明低 lexical overlap 是真正的 dense 需求信号。citeturn20academia8turn18search2 | **中** | chunking、模型版本、re-embedding、semantic false positives；sqlite-vec 当前仍是 pre-v1。citeturn16search2 |
| **metadata-filtered hybrid** | FTS5/BM25 + dense union/fusion；先 state/version filter | 当 lexical 和 semantic 各自都存在独立 critical misses，并且项目 query set 证明 hybrid 有净收益时。公开结果既有 hybrid 获益也有 hybrid regression，因此必须本地调参/验证。citeturn1view1turn1view3 | **中—高** | 两套索引漂移、fusion 权重、候选重复、dense noise 降低 BM25 rank-1。 |
| **version-aware / reranked retrieval** | 显式 revision lineage、validity intervals、supersession、必要时 reranker | 当“截至某时”“旧规范为何改”“当前版与历史版比较”“多个版本几乎同文”成为高频任务。VersionRAG、法律 QA、Git state-transition 实证对此有直接支持。citeturn21academia24turn21search2turn21academia26 | **高** | version metadata 建模错误；历史有效期不完整；reranker domain mismatch；更多 eval 与迁移负担。 |

从这条阶梯看，**SQLite FTS5 是比 vector DB 更自然的第一层“真正检索层”候选**：它保留本地、单文件、无服务、BM25、metadata filtering 的特性，又不需要 embedding 生命周期。等到实测暴露 semantic recall 缺口时，再在旁边增加 dense sidecar，而不是反过来让所有简单精确查询都依赖 embedding。SQLite FTS5 可重建机制和 sqlite-vec 的共同 SQLite 形态也使后续 hybrid 不必推倒重来。citeturn16search0turn16search2

### 每档维护成本真正来自哪里

**人工分层表的成本是认知维护。** 文件增加时要判断归哪层、什么任务触发、规则是否已经改名或迁移；优点是逻辑可读、diff 友好、不需要 embedding migration。它最危险的不是性能，而是 silent omission。

**FTS/BM25 的成本是派生一致性。** 要同步增删改、决定 tokenizer/field weights，并确保 source hash 对得上；但索引完全可重建，失败面相对窄。SQLite 官方对 external-content inconsistency 和 rebuild 有明确恢复机制。citeturn16search0

**dense 的成本是模型化状态。** 一个 chunk 不再只有“文本是什么”，还会有“用哪个 splitter、哪个 embedding model、哪个 model revision、多少维生成的”。这使“Git 文件没变但 embedding pipeline 变了”也需要 re-index。FastEmbed 可以去掉外部服务，但不会去掉这类维护状态。citeturn18search2

**hybrid/reranker 的成本是决策面扩张。** 需要决定 candidate pools、fusion/RRF 参数、metadata pre-filter、rerank cutoff、token cutoff，并防止 dense noise 把 BM25 的正确 exact hit 拉低。公开实证已经证明默认 fusion 并非稳胜。citeturn15search0turn1view3

**version-aware 层的成本主要不是检索算法，而是数据治理。** 必须知道“哪一 revision 在什么 interval 有效、什么 revision supersede 什么、authority 如何排序”。但一旦当前态是重要事实，这项成本不能靠更好的 embedding 逃掉，因为 similarity 对 contradiction/currentness 的判别本身可能接近随机。citeturn21search4turn21academia24

### 人工分层加载表何时仍可视为合理最优

这里的答案必须明确分成“证据”与“未知”。

**[UNKNOWN]：不存在可信的“到 N 个文件 / N MB / N 万行后人工分层表不再最优”的公开阈值。** 本次研究没有找到这样一条经验定律。按现有研究，规模不是最好的升级变量。citeturn15search0

更有证据依据的是采用**复杂度退出条件**。人工分层仍是强候选，只要以下事实在项目自己的 eval 中继续成立：

人工 trigger 能稳定覆盖关键 source；大多数 query 可通过 path/title/heading/ID/领域词定位；跨目录、跨规则的组合问题比例低；规则 churn 没有使路由表频繁 stale；loaded-context pollution 保持低；而且与更复杂 retriever 的 A/B 相比没有显著 critical-recall 缺口。coding-agent 对 path-specific/lazy instructions 的广泛采用以及“不必要 repo context 可能增加 >20% inference cost”的实证，都支持这种**“先保持最小、用失败触发升级”**的策略。citeturn13search0turn13search3turn15search1

人工表开始失去优势的信号，则不是“仓库到了 20 MB”，而是**路由函数本身开始变成搜索问题**：同一个自然语言任务可能对应很多无法由路径预先编码的 source；同义表达造成持续 lexical miss；大量规则横跨多个目录；current/historical 状态无法从目录层级表达；人工表变化频率高到 stale routing 成为可观测故障。此时首先加结构化 metadata + FTS5，通常比直接跳到向量层更容易验证收益。版本适用性复杂时还必须独立加 state/version gate。这个顺序是对全文检索成熟度、coding-agent lazy-loading 实践和 temporal-RAG 实证的综合归纳。citeturn16search0turn13search0turn21search2

### 对本任务最值得保留的几条证据结论

**一，库大小不是是否需要 vectors 的可靠代理变量。** 对数 MB/数百文件，没有“必须上 vector”的证据；同样，小库在低词汇重叠查询下也可能获益于 dense。citeturn15search0turn20academia8

**二，人工分层/路径触发不是过时方案。** 2026 年主流 coding-agent 产品仍在主动强化 nested、glob、skills、lazy memory 等按需机制。citeturn13search0turn13search2turn13search3turn14search0

**三，“记得更多”不等于“agent 做得更好”。** 2026 年两项 context-file 实证分别发现额外 context 可增加 20% 以上 inference cost 并倾向降低成功率，以及在另一组 288 次运行中没有测出 correctness 改善。citeturn15search1turn15search2

**四，BM25/keyword 应保留为一级公民，而不是 vector 的遗留 fallback。** 精确术语和结构化 headings 会让 sparse 成为最强通道；hybrid 也有被 dense noise 拖差的公开案例。citeturn1view1turn1view3

**五，当前态、版本、权威性不能交给 semantic similarity 猜。** 版本化技术文档、德国法律 QA、法国税法和 evolving-memory 实验都给出了同方向证据；尤其 cosine 对 contradiction/duplicate 的 AUROC 0.59 是一个很强的警告。citeturn21academia24turn21search2turn15search3turn21search4

**六，派生索引应“可删、可重建、可验 hash、可回源”。** SQLite FTS5 的 rebuild 和 hash-based document refresh 都是成熟先例。citeturn16search0turn7search10

**七，最合理的升级触发器是项目自己的 retrieval eval，而不是仓库尺寸。** 应先建立代表性 query → expected sources 数据集，分别测 route-only、`rg`、BM25、dense、hybrid 的 critical recall、context precision、stale/wrong-scope rate、token 数与端到端 task success；Ragas 等工具的公开指标体系也强调组件指标与 end-to-end 指标需要同时评价。citeturn19search3turn19search6

综合来看，题述体系的候选路线可以浓缩为：

**Git truth → 最小常驻核心 → 路径/任务触发 → `rg` 回源 → 可校验 manifest → FTS5/BM25 → 仅在实测 lexical miss 后加本地 dense → 实测证明互补后 hybrid → 只有真实版本问题出现时才加显式 version/supersession 层。**

这条路线不是“向量没有价值”，而是让**每一档额外复杂度都必须购买一个已经测出来的失败面**；它与 2025–2026 年检索、coding-agent context、temporal RAG 和 context-pollution 证据最一致。citeturn15search0turn15search1turn21academia24turn19search8

## 来源表

| 日期 | 类型 | 来源 | 本报告使用范围 |
|---|---|---|---|
| 2026-06-28 | 论文实证 / arXiv | *As We May Search* citeturn15search0turn2view1turn2view2 | 1K–1M documents 下 dense/BM25/hybrid 的质量、冷启动与扩缩；说明文档数≠MB 阈值。 |
| 2026-06-06 | 社区实证 | *Section-Level RAG: Why BM25 Beat Hybrid Search…* citeturn1view3 | 小型结构化 corpus 中 hybrid 被 dense noise 拖差的失败样本；样本量很小，未当成通用结论。 |
| 2026 | 论文实证 | *From BM25 to Corrective RAG…* citeturn1view1 | 金融文档检索中 BM25、hybrid、fusion tuning 与 reranking 的对比。 |
| 2025-02-07 | 论文实证 / arXiv | *NoLiMa: Long-Context Evaluation Beyond Literal Matching* citeturn20academia8 | 低 lexical overlap 下长上下文/直接匹配能力下降；证明 semantic need 不由库大小决定。 |
| 2025-07-14 | 技术报告 / 可复现实验 | Chroma, *Context Rot* citeturn20search0turn20search7 | 18 个模型在增加输入长度时的非均匀退化；支持“不要因 context window 大就全加载”。 |
| 访问 2026-08-31 | 厂商文档 | Anthropic Claude Code Memory / CLAUDE.md citeturn13search0 | 层级 CLAUDE.md、nested lazy loading、auto-memory 200 行/25 KB、>200 行 adherence 警告、4 MiB 限制。 |
| 访问 2026-08-31 | 厂商文档 | Anthropic Claude Code Skills citeturn13search2 | skill body 按使用加载；paths 条件触发。 |
| 访问 2026-08-31 | 厂商文档 | Anthropic Claude Code Hooks citeturn13search6 | `InstructionsLoaded` 等规则加载可观测性。 |
| 访问 2026-08-31 | 厂商文档 | Cursor Rules / Skills citeturn14search0turn14search2 | `.cursor/rules`、dynamic/path rules、AGENTS.md 与 skills。 |
| 访问 2026-08-31 | 厂商文档 | GitHub Copilot repository custom instructions / CLI citeturn13search3turn13search9 | repo-wide、`applyTo` path-specific、nearest AGENTS.md、CLI 条件加载。 |
| 访问 2026-08-31 | 厂商文档 | GitHub Copilot custom-instruction best practices citeturn13search1turn13search12 | 长规则可能被遗漏、非确定性、不同 surface 支持差异。 |
| 2026-02-12 | 论文实证 / arXiv、OpenReview | *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?* citeturn15search1turn15search24 | context files 对成功率、探索行为、步骤与 >20% inference cost 的影响。 |
| 2026-07-28 | 论文实证 / arXiv | *Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories* citeturn15search2turn15search6 | Claude Code/Codex、17 tasks、288 runs；context strategy 未测得 correctness 改善。 |
| 访问 2026-08-31 | 官方文档 | SQLite FTS5 Extension citeturn16search0turn16search15 | BM25、external-content 一致性风险、trigger/rebuild、可重建索引。 |
| 访问 2026-08-31 | 厂商/项目文档 | LlamaIndex document management / docstore strategy citeturn7search0turn7search4turn7search10 | stable document id、hash-based refresh、upsert/delete；派生层 drift 控制先例。 |
| 2025-10-09 | 论文实证 / arXiv | *VersionRAG: Version-Aware Retrieval-Augmented Generation for Evolving Documents* citeturn21academia24 | 100 questions/34 versioned technical docs；90% vs naive RAG 58% / GraphRAG 64%。 |
| 2026-05-22 | 论文实证 / arXiv | *Asking For An Old Friend: Diagnosing and Mitigating Temporal Failure Modes…* citeturn21search2turn21search5 | 312 德国成文法时间敏感 QA；version filtering、hard temporal validity、recency bias。 |
| 2026-08-10 | 论文实证 / arXiv | *Temporal Misgrounding in Legal RAG* citeturn15search3turn21search8 | “当前有效版本”被错误用于历史/未来问题的 failure mode。 |
| 2026-06-25 | 预印本实证 / arXiv | *Temporal Validity in Retrieval Memory* citeturn21search1turn21search4 | contradiction vs duplicate cosine AUROC 0.59；stale facts 与 deterministic supersession。 |
| 2026-08-21 | 预印本实证 / arXiv | *Temporal Validity on Real Software Histories* citeturn21academia26 | 真实 GitHub fixes 中 clean atomic transitions 的 stale-value 检索验证；范围有限，结论谨慎使用。 |
| 访问 2026-08-31；15.2.0 发布 2026-07-15 | 开源项目 / 官方仓库 | ripgrep citeturn18search0turn18search12 | Git-aware 递归 grep、成熟度与当前维护状态。 |
| 访问 2026-08-31 | 开源项目 / 官方仓库 | Tantivy citeturn18search1 | 嵌入式 Rust 全文检索、incremental indexing、更新/commit 语义。 |
| 访问 2026-08-31 | 开源项目 / 官方仓库 | sqlite-vec citeturn16search2turn16search5 | 无服务 SQLite vector extension；pre-v1 成熟度警告及早期 brute-force/ANN 路线。 |
| 访问 2026-08-31 | 开源项目 / 官方仓库 | Qdrant FastEmbed citeturn18search2 | ONNX 本地 embedding、无 GPU/PyTorch 大依赖；模型 artifact 生命周期。 |
| 2026-03-10 | 社区设计先例 | Hermes Agent issue：SQLite FTS5 + sqlite-vec local hybrid proposal citeturn16search8 | 零独立搜索服务的 agent 集成先例；仅作为社区设计证据，不视为成熟生产验证。 |
| 访问 2026-08-31 | 评估框架文档 | Ragas Context Precision / Metrics citeturn19search3turn19search6 | retrieval context precision、组件级与端到端评价。 |
| 2025-12-16 | 论文实证 / arXiv | *Dynamic Context Selection for Retrieval-Augmented Generation* citeturn19search1turn19academia29 | distractor 对生成质量的影响；2-hop 单 distractor >26% 下降；dynamic k。 |
| 2025-11-22；修订 2026-01-19 | 论文实证 / arXiv | *Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction* citeturn19academia28turn19search8 | coverage-controlled pruning；context 压缩 2–3× 且答案质量稳定/改善。 |
| 2025-06-10 | 论文实证 / arXiv | *Efficient Context Selection for Long-Context QA: … Adaptive-k* citeturn19academia31 | 按 query/candidate score 分布自适应 context size，而非固定 top-k。 |