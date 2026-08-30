## 评分快照与总结果

读取开始及评分结束时，`master` 均指向：

`06508683faa8a1f23ff10a2bfe5e1bc422479ba7`

用于核对设计稿引用的 5 份执行源/阅读材料固定为：

`1ba2a2eb24d3d3a5651b958b2a863b61fdda4b46`

评分期间 `master` 未发生漂移。fileciteturn21file0L2-L2

| 臂 | 客观项 | 分级项总分 | T1-记录 / 加载 / 失效 | D 节结果 |
|---|---:|---:|---|---|
| A＝Claude 网页 | 9/12 PASS | 11/15 | FAIL / PASS / PASS | **无明显表面差异** |
| B＝Claude Code 子代理 | 10/12 PASS | 11/15 | FAIL / PASS / PASS | **无明显表面差异** |

证据类别：

- **[D]** 两臂设计稿中的直接文本。
- **[S]** 在 `1ba2a2e…` 上对 5 份阅读材料的核对。
- **[M]** `05-trial-run-record.md` 中的机械计数或机械核验汇总。
- **[T]** 三轮试跑回复与 runner 直接读取工作区所得事实。
- **[J]** 我依据预冻结细则作出的评分判断。

我对 R7 采用细则表中写明的核验方法，即“行数＋是否依赖未提供的外部内容”；记录字段是否真正复现第 2 节，则另在 T1-记录和 Q3 中判定。细则全文见评分文件。fileciteturn2file0L2-L2

---

## 1. A 臂评分表：Claude 网页

| 项 | 判定 | 一句证据或理由 |
|---|---|---|
| R1 | **FAIL** | **[D+S+J]** 转移说明明确承认正文 2.4 的 `scope_zh` 被标成“材料2”，实际来自 `guard-registry.yaml`；底层内容虽属于允许的 5 份文件，但逐句来源归属并不准确，按 R1 的严格来源核对不能 PASS。fileciteturn4file0L2-L2 fileciteturn17file0L2-L2 |
| R2 | **FAIL** | **[D+M]** A 的读取清单只列出对 spec §9/§11/§14/§16/§18 的使用，未援引 §2；机械汇总又确认 §20 援引次数为 0，因此未满足四项“至少各一次”的合取条件。fileciteturn6file0L2-L2 fileciteturn10file0L2-L2 |
| R3 | **PASS** | **[D]** 第 2 节分别覆盖字段、YAML/Markdown 格式、工作区位置、写入者与时机、更新规则、失效与标记，并附示例。fileciteturn4file0L2-L2 fileciteturn5file0L2-L2 |
| R4 | **PASS** | **[D]** 默认只读 `env-profile.yaml`，日志冷存，并按安装、文档、故障排查等触发条件选择性加载。fileciteturn5file0L2-L2 |
| R5 | **PASS** | **[D]** 明确规定当前指令优先，冲突先记观察；`stale_check_due` 与 volatile 值降级为待验证提示，并给出无法复验时的处理。fileciteturn5file0L2-L2 |
| R6 | **PASS** | **[D+S]** 引用了多条 Owner 原文并使用 G/C/O/H 标签，边界部分还明确识别了 P＋O 的输出偏好，同时区分需求、方案、bug、代码库线索等相邻切片。fileciteturn4file0L2-L2 fileciteturn14file0L2-L2 fileciteturn15file0L2-L2 |
| R7 | **PASS** | **[D+M+J]** 提示词机械计数为 17 行，未要求 agent 另读一个未提供的模板或外部文件；其字段覆盖不完整的问题不改变本项的窄义核验，但会导致 T1-记录失败。fileciteturn5file0L2-L2 fileciteturn10file0L2-L2 |
| R8 | **PASS** | **[D]** 有 T1、T2、T3 三个场景，每个都有 expected/observed 表，T3 明确是缺失/过期负向测试。fileciteturn5file0L2-L2 |
| R9 | **PASS** | **[D+J]** 抽查中，来源可定位的规则陈述标 VERIFIED，字段设计、阈值和应用方式标 INFERENCE，材料未给出的写权/git 化等标 UNKNOWN；R1 的材料编号错误是来源定位错误，不是把推断伪装成 VERIFIED。fileciteturn4file0L2-L2 fileciteturn5file0L2-L2 |
| R10 | **PASS** | **[D]** 给出了机器/沙箱混淆、偏好阈值拍脑袋、字段缺少实证等至少三条实质弱点，并另列敏感灰区、迁移性和 Owner 可编辑性盲区。fileciteturn5file0L2-L2 |
| R11 | **PASS** | **[D]** 明确声明未写仓库、未创建文件；所有新目录和记录均作为 `[INFERENCE]` 设计方案或合成示例呈现，没有声称其已存在。fileciteturn4file0L2-L2 fileciteturn6file0L2-L2 |
| R12 | **FAIL** | **[D+M+J]** 八个编号节本身为 182 行、满足 ≤250，但实际回复还增加了 `## 无需用户操作` 与 `## 下一步` 两个独立节；按“严格八节结构”的字面要求，不能由回答自行宣布这两节“不属正文”而豁免。fileciteturn4file0L2-L2 fileciteturn6file0L2-L2 fileciteturn10file0L2-L2 |
| Q1 | **4/5** | **[D+J]** 分节清楚、操作与说明分离，示例较直观；但材料编号、guard、scope、volatility 等内部术语和压缩式 YAML 仍增加了 Owner 阅读成本。 |
| Q2 | **4/5** | **[D+S+J]** §16 被用于确定位置、§18 用于权限、§14 用于敏感信息、loader/registry 用于分层与整编，确实进入了设计决策；一处来源错标以及 §2/§20 缈失使其未达到满分。fileciteturn11file0L2-L2 fileciteturn13file0L2-L2 fileciteturn19file0L2-L2 |
| Q3 | **3/5** | **[D+T+J]** 提示词和测试可直接启动，但提示词没有携带第 2 节要求的完整画像字段与状态枚举，试跑 agent 因而漏掉 `id/source/scope` 并自行使用 `active`，可复现性只属中等。fileciteturn5file0L2-L2 fileciteturn10file0L2-L2 |

**A 臂客观项：9 PASS / 3 FAIL。分级项：11/15。**

---

## 2. B 臂评分表：Claude Code 子代理

| 项 | 判定 | 一句证据或理由 |
|---|---|---|
| R1 | **PASS** | **[D+S]** 抽查 Owner“记录不能只占空间”、spec §2“文件负责记忆”、loader 的 core/conditional 与冷原件按需规则，均能在固定的 5 份材料中定位，未发现引用第六份材料的实质内容。fileciteturn7file0L2-L2 fileciteturn8file0L2-L2 fileciteturn11file0L2-L2 fileciteturn19file0L2-L2 fileciteturn20file0L2-L2 |
| R2 | **FAIL** | **[D+M]** B 正确使用了 §2、§16 和分层加载模式，但机械汇总确认 §20 援引次数为 0；该项是合取条件，故整体 FAIL。fileciteturn7file0L2-L2 fileciteturn8file0L2-L2 fileciteturn10file0L2-L2 |
| R3 | **PASS** | **[D]** 字段表、文件格式、`memory/env/` 目录、写入与升格时机、更新、stale/retired 失效规则六要素齐全，并附完整 YAML 示例。fileciteturn7file0L2-L2 fileciteturn8file0L2-L2 |
| R4 | **PASS** | **[D]** 会话先读 README＋索引，仅在 `use_when` 命中时读取对应 category，observed/archive 默认不读，明确避免全量加载。fileciteturn8file0L2-L2 |
| R5 | **PASS** | **[D]** 当前用户指令优先，冲突只写 observed；stale 视为 unknown，能复验则复验，关键动作依赖无法复验的过期条目时停止并询问。fileciteturn8file0L2-L2 |
| R6 | **PASS** | **[D+S]** 八条 Owner 原文均带 G/C/O/H 类标注，并明确划分开发需求、方案、bug、跨项目代码线索、对话偏好和平台能力边界。fileciteturn7file0L2-L2 fileciteturn14file0L2-L2 |
| R7 | **FAIL** | **[D+T+J]** 虽只有 27 行，但第 6 条要求“字段按 README 模板”，固定试跑却只加载提示词和空工作区；README 不是已提供依赖，agent 只能自行发明模板，并实际漏掉第 2 节要求的 `scope/sensitivity`。fileciteturn8file0L2-L2 fileciteturn10file0L2-L2 |
| R8 | **PASS** | **[D]** 有三个 fresh-context 测试，均含 expected/observed 表，其中 T2 是过期负向测试，T3 是缺失＋冲突负向测试。fileciteturn8file0L2-L2 |
| R9 | **PASS** | **[D+J]** 规则原文、文件事实与 checklist 条目使用 VERIFIED；字段设计、升级门和目录方案使用 INFERENCE；共享层、写权、阈值和平台能力缺口使用 UNKNOWN，未见把设计判断伪装成已验证事实。fileciteturn7file0L2-L2 fileciteturn9file0L2-L2 |
| R10 | **PASS** | **[D]** 列出写权前提、复验成本、跨项目共享、无机械强制四项实质弱点，并说明 shell 假设、字段经验默认和“索引＋分层”锚定偏差等盲区。fileciteturn9file0L2-L2 |
| R11 | **PASS** | **[D]** 明确声明未写仓库；目录、README 和 schema 都作为草案设计描述，写权不存在时采用不落盘降级，没有声称虚构文件已经存在。fileciteturn7file0L2-L2 fileciteturn9file0L2-L2 |
| R12 | **PASS** | **[D+M]** 正文按 `## 1` 至 `## 8` 排列，没有额外的同级交付节，机械汇总为 211 行，低于 250 行。fileciteturn7file0L2-L2 fileciteturn9file0L2-L2 fileciteturn10file0L2-L2 |
| Q1 | **3/5** | **[D+J]** 结构精确但明显偏工程内部文档：十二字段 schema、三层状态目录、升格门、`verify_cmd_pass×2` 等内容让 Owner 必须理解较多内部机制后才能作判断。 |
| Q2 | **5/5** | **[D+S+J]** §2 决定文件化、§16/§9 决定项目工作区和真相边界、§18 决定写权、registry/loader 决定索引与条件加载、反模式清单决定预算和效用测试，引用不是装饰而是逐项转化成设计选择。fileciteturn11file0L2-L2 fileciteturn13file0L2-L2 fileciteturn16file0L2-L2 fileciteturn17file0L2-L2 |
| Q3 | **3/5** | **[D+T+J]** 测试场景和核验指标很具体，但提示词缺少其所依赖的 README 模板，且强制确认流程让固定三轮试跑始终停在 observed 层；agent 能运行，却需要自行补出关键 schema。fileciteturn8file0L2-L2 fileciteturn10file0L2-L2 |

**B 臂客观项：10 PASS / 2 FAIL。分级项：11/15。**

---

## 3. 试跑判定

细则 C 要求：

- **记录 PASS**：位置和字段均与本臂第 2 节一致。
- **加载 PASS**：第二轮答案与记录一致，并声明依据来自记录。
- **失效 PASS**：第三轮按本臂失效规则标记或更新，不静默覆盖、不拒绝修改。fileciteturn2file0L2-L2

| 臂 | T1-记录 | T1-加载 | T1-失效 | 判定依据 |
|---|---|---|---|---|
| A | **FAIL** | **PASS** | **PASS** | **[T+M]** 位置正确，但 profile 缺第 2 节必填的 `id/source/scope`，且把 `current` 写成 `active`；第二轮按画像选择 `rg`、Python 3.12＋venv并逐项声明画像依据；第三轮把 rg 留作 `superseded` history，并把当前值改为 grep。fileciteturn10file0L2-L2 |
| B | **FAIL** | **PASS** | **PASS** | **[T+M]** 位置正确，但 observed 条目缺第 2 节必填的 `scope/sensitivity`；第二轮明确以 observed 线索而非 confirmed 事实给出 rg 和 Python 方案；第三轮将旧 rg 条目标 stale 归档，并新增 grep observed 条目。fileciteturn10file0L2-L2 |

补充但**不进入细则 C 的三项二元结果**：

- A 的 Owner-touch 为 **0**。
- B 的 Owner-touch 为 **2**，分别在第一轮和第三轮要求编号确认。fileciteturn10file0L2-L2

---

## 4. D 节判定

预冻结条件要求同时满足：

1. 客观 PASS 数之差 ≤1；
2. 分级总分之差 ≤2；
3. T1 三项结果相同。fileciteturn2file0L2-L2

本次结果：

- 客观项：A 9，B 10，差 **1**；
- 分级项：A 11，B 11，差 **0**；
- 试跑：两臂均为 **FAIL / PASS / PASS**。

因此按 D 节必须判：

> **本次观察无明显表面差异。**

差异分布如下：

- **客观项**：B 多 1 个 PASS。A 的问题集中在一处错误来源标记和额外回复节；B 的问题集中在提示词依赖未提供的 README 模板。两臂共同漏掉 §20。
- **分级项**：总分相同，但特征不同。A 在 Owner 可读性上高 1 分；B 在取证深度上高 1 分；可试跑性相同。
- **试跑项**：三个冻结二元结果完全相同；唯一明显的操作成本差异是 Owner-touch 0 对 2，但 D 节没有把它纳入决定条件。

所以不能据本次 n=1 观察形成 Claude 网页或 Claude Code 的表面偏好。重新设计时仍应按交互便利选择表面。

---

## 5. 我认为评分细则存在的缺陷

### 5.1 R1 的“抽查三处”会造成样本依赖

A 文件自己明示有一处来源编号错误，但 `05` 的机械汇总仍记为“8/8 命中”。这说明只抽中其他引用时会 PASS，抽中该处时会 FAIL，同一文本可能因抽样位置不同得到不同结论。更稳定的做法是：对所有显式 `VERIFIED·材料N` 标记做机械枚举，或冻结具体抽查位置。fileciteturn4file0L2-L2 fileciteturn10file0L2-L2

### 5.2 R2 是全有或全无，且本次对两臂没有区分力

两臂都因为 §20 为 0 而整体 FAIL，即使 B 已正确使用 §2、§16和分层加载，A 也使用了大量其他相关规则。它能检查遵从性，但不能区分“只漏一项”和“几乎完全未取证”；同时与 Q2 的取证深度有较强重叠。

更合适的形式是把 §2、§16、§20、分层加载拆成四个机械子项，再决定是否汇总。

### 5.3 R7 与 T1-记录之间的责任边界不够清楚

R7 的表格核验方法只写“行数＋是否依赖未提供内容”，而任务书正文还要求提示词使 agent 能“按第 2 节记录”。这导致两种合理评分方式：

- 窄义：A R7 PASS，但 T1-记录 FAIL；
- 广义：A 因遗漏字段在 R7 和 T1-记录各 FAIL 一次。

细则应明确是否允许对同一个“字段契约没有进入提示词”的问题进行双重扣分。

### 5.4 T1-记录要求完整字段一致，但固定输入只加载提示词

这个设计实际上检验的是“40 行内是否完整压缩了第 2 节 schema”，而不仅是 agent 是否会记录。B 的提示词又明确把 schema 放在 README 中，却不给 README；因此这一项部分变成“agent 能否正确发明缺失模板”。

可以改成二选一：

- 固定场景同时提供提示词及其声明依赖的最小模板；
- 或在 R7 明文规定提示词必须内嵌所有必填字段和状态枚举。

### 5.5 R12 的计数对象存在歧义

A 把 `无需用户操作` 和 `下一步` 宣布为八节正文之外的执行源结构；机械汇总只报告“八节正文 182 行”，但 R12 写的是“严格八节结构、≤250 行”，没有说明：

- 标题、状态 YAML 是否计入；
- 执行源强制的开头/结尾节是否允许；
- 总回复行数还是八节主体行数作为上限。

我按字面把 A 的两个额外标题节判为结构 FAIL；若 Owner 认定执行源外框允许，则 A 的 R12 应翻为 PASS，但 D 节总判定仍不会变化。

### 5.6 D 节忽略了已经机械记录的 Owner-touch 差异

反模式 #8 和两臂自己的测试都把 Owner-touch 视为一等指标，但 D 节只比较三项 PASS/FAIL。于是 A 的 0 次与 B 的 2 次确认请求不会改变试跑结果，也不会直接进入最终判定。fileciteturn16file0L2-L2 fileciteturn10file0L2-L2

可增加一项：

- `T1-Owner-touch`：0、1、≥2 分档；
- 或把 Owner-touch 纳入 Q3 的预冻结机械评分，而非仅由评分者主观吸收。

### 5.7 各客观项等权，可能让轻微格式错误决定表面偏好

R1 的单个材料编号错误、R12 的额外标题节，与 R3 六要素缺失、R5 没有冲突/过期处理被赋予相同的一个 PASS 差额。若客观差异刚好达到 2，D 节会宣布表面偏好，即使差异全是轻微格式项。

可将客观项至少分成：

- **关键功能项**：R3、R4、R5、R7、R8；
- **证据与安全项**：R1、R2、R9、R11；
- **呈现合规项**：R6、R10、R12。

### 5.8 n=1 试跑无法区分提示词问题和随机执行偏差

两臂各只运行一个同族 Fable agent。记录字段遗漏可能来自提示词，也可能来自一次采样中的执行偏差。最低限度可对每臂重复三次，报告“完全一致率”和字段遗漏频率，而不是只给一次 PASS/FAIL。

### 5.9 试跑记录中的 A 表面名称有一处 provenance 文案不一致

`03` 明确写的是 `claude.ai` 网页回复，而 `05` 的 A 臂标题写成“ChatGPT-网页 Fable 设计”。从片段版本和内容看，试跑对象仍可识别为 A 的 `v0-draft`，但表面名称应机械生成，避免 provenance 文案错误。fileciteturn4file0L2-L2 fileciteturn10file0L2-L2

---

## 6. 实际读取的文件清单

### 6.1 评估文件：读取自 `master@06508683faa8a1f23ff10a2bfe5e1bc422479ba7`

| 文件 | 实际读取范围 | 用途 |
|---|---|---|
| `notes/cross-family-experiments/EXP-7-surface-comparison/01-task-brief.md` | 全文 | 确认两臂共同任务、八节要求和允许阅读材料。fileciteturn1file0L2-L2 |
| `notes/cross-family-experiments/EXP-7-surface-comparison/02-preregistered-rubric.md` | 全文 | 唯一评分规则。fileciteturn2file0L2-L2 |
| `notes/cross-family-experiments/EXP-7-surface-comparison/03-A-arm-claude-web-response.md` | 全文，分段读取 | A 臂设计稿与转移说明。fileciteturn4file0L2-L2 fileciteturn5file0L2-L2 fileciteturn6file0L2-L2 |
| `notes/cross-family-experiments/EXP-7-surface-comparison/04-B-arm-claude-code-response.md` | 全文，分段读取 | B 臂设计稿。fileciteturn7file0L2-L2 fileciteturn8file0L2-L2 fileciteturn9file0L2-L2 |
| `notes/cross-family-experiments/EXP-7-surface-comparison/05-trial-run-record.md` | 全文 | 三轮逐字记录、runner 文件核验和机械汇总。fileciteturn10file0L2-L2 |

### 6.2 引用核对材料：读取自 `1ba2a2eb24d3d3a5651b958b2a863b61fdda4b46`

| 文件 | 实际读取范围 | 限定用途 |
|---|---|---|
| `current/human-approved-spec.md` | 全文，分段读取 | 核对 §2、§6、§9、§11、§14、§16、§18、§19、§20 等引用。fileciteturn11file0L2-L2 fileciteturn12file0L2-L2 fileciteturn13file0L2-L2 |
| `raw/owner-intent-records/2026-08-30-owner-goals-and-input-classification-verbatim.md` | 全文，分段读取 | 核对 Owner 原文、消息一至三及附录 G/C/O/H/P。fileciteturn14file0L2-L2 fileciteturn15file0L2-L2 |
| `notes/cross-family-cooperation/foundational-agent-antipattern-checklist-v1.md` | 全文 | 核对 #2、#3、#4、#6、#8、#15 和“值得延续”。fileciteturn16file0L2-L2 |
| `current/guard-registry.yaml` | 全文，分段读取 | 核对导航层、load class、triggers、maintenance 与 consolidation。fileciteturn17file0L2-L2 fileciteturn18file0L2-L2 |
| `commands/load-mnemosyne-guidance.md` | 全文，分段读取 | 核对 core/conditional、uncertain-read、规则 13/29/34 和 Boundaries。fileciteturn19file0L2-L2 fileciteturn20file0L2-L2 |

除此之外，我只读取了 GitHub 的 `master` 分支元数据以锁定并复核 SHA；**未读取 EXP-7 目录内的其他评估文件，也未读取上述 5 份材料以外的任何仓库内容，未执行任何仓库写入。**
