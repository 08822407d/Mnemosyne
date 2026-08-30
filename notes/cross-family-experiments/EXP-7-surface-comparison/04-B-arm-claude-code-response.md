# EXP-7 · B 臂回答：代码开发类 agent 的"环境记忆"设计切片

```yaml
status: non_execution_source_draft（不因完成而获得任何采纳地位）
pinned_commit: 1ba2a2e
inputs: 仅任务书列出的 5 份文件（清单见 §8）；未读其他文件、未联网、未写仓库
tag_legend: "[VERIFIED]=可在 5 份文件中逐字/逐条定位；[INFERENCE]=由材料推出的设计判断；[UNKNOWN]=材料未覆盖，不补写"
```

## 1. 需求还原

Owner 原文引用（逐字，出自 raw/owner-intent-records/2026-08-30-…-verbatim.md）：

| # | 原文（逐字） | 出处 | 分级 | 备注 |
|---|---|---|---|---|
| 1 | "代码开发类的agent显然就需要记录开发需求,然后是AI给出的方案(设计实现测试等),还需要记录习惯或者说常用的系统环境开发工具配置和用户的常用环境配置,然后就是bug和不符合用户预期的部分." | 消息二 | G＋H | 本切片＝"习惯或者说常用的系统环境开发工具配置和用户的常用环境配置" [VERIFIED] |
| 2 | "将它们记录下来后不仅仅是保存在某地占空间而已,它们还需要能够让相关agent利用起来" | 消息二 | G（元目标） | "可加载、可核验"优先于"记全" [VERIFIED] |
| 3 | "至少程序开发和库开发我的架构方面的想法是可以当作有一定权重的意见,因为我在计算机编程这方面也是有一定工作经验的" | 消息一 | C（采纳权重） | 本切片属程序开发域，Owner 的结构性意见应给权重 [VERIFIED] |
| 4 | "不要把"原文"当成宝贝,而是要有依据地采纳它" | 消息三 | C | 每条记录须带 evidence 字段；无依据不得升为 confirmed [VERIFIED] |
| 5 | "这个记忆系统大概并不是一个独立存在独立运行的"系统",而是形成一组提示词/行为约束/记录方案和相应文件组织结构,让具体agent使用和遵守它们" | 消息三 | G（定位）＋H | 交付形态＝提示词片段＋记录方案＋目录结构，无运行时组件 [VERIFIED] |
| 6 | "就应该提前摸清楚并形成一套经验,供其他agent学习和套用" | 消息二 | G | 字段与规则须自包含，可被其他 agent 套用 [VERIFIED] |
| 7 | "考虑到人类的思维不稳定性…反复横跳…有些在之前还说过的,经过一段时间可能又忘记了" | 消息三 | O | 偏好类记录须允许用户当场推翻，且推翻不算记录错误 [VERIFIED] |
| 8 | "还需要明确记录相关工具/产品的真实能力限制和使用方法(比如界面按钮等)" | 消息二 | G＋O | 指 AI 产品界面能力，不属本切片（见边界）[VERIFIED] |

边界（[INFERENCE]，依据引文 1 的并列结构与引文 8）：
- 开发需求／AI 方案／bug 与预期偏差：记"这个项目要做什么、做了什么、错在哪"，随任务变化；环境记忆记"在什么机器、用什么工具、用户习惯怎么用"，跨任务稳定。判据：一条事实若能用一条只读命令复验（`python --version`、`git config --get user.email`），归环境记忆；若只能靠任务上下文判断，归其余项。
- 跨项目自用代码库线索：从需求记录提炼，不在本切片；但环境记忆中 scope=user 的条目可作其"常用"线索来源。
- 对话输出方式偏好（消息二"我喜好的agent对话的输出方式"）与 AI 产品界面能力（引文 8）：前者是交互偏好，后者属平台事实层（反模式 #15 对冲栏"platform-guides 事实层"）[VERIFIED]；均不进环境记忆。环境记忆的"偏好"仅指用户对环境替代方案的选择（如 uv 而非 pip、.venv 固定位置）。
- 不含密钥与凭据的值：spec §14 "Do not commit secrets or credentials under any repository visibility" [VERIFIED]；只记"凭据放在哪"的指针。

## 2. 记录方案

**2.1 记什么（字段清单）** [INFERENCE；字段设计依据：spec §6 的 Raw→Candidate→确认三态、§11/§15 的 stale/unknown 标注义务、反模式 #6、registry 的 status/last_confirmed_current 字段惯例，均 [VERIFIED]]

| 字段 | 必填 | 说明 |
|---|---|---|
| id | 是 | `ENV-NNN`，只增不复用 |
| category | 是 | system / toolchain / tool-config / preference |
| scope | 是 | machine / user / project（"常用、习惯"＝user 或 machine；本项目特有＝project）|
| key / value | 是 | 短键＋事实本体各一行；value 逐字，不概括 |
| evidence | 是 | command_output(命令＋日期) / user_statement(逐字引文＋日期) / file_observed(路径) / inferred |
| status | 是 | observed → confirmed → stale → retired |
| verify_cmd 或 recheck_by | 二选一必填 | 只读幂等复验命令；无法用命令复验的（偏好类）须给复核日期或触发事件 |
| last_verified | confirmed 必填 | 日期＋方式 |
| use_when | 是 | 触发词，供 §3 加载匹配（install_deps / run_tests / run_build / edit_config / choose_tool …）|
| sensitivity | 是 | public / private / secret_ref；secret_ref 只允许指针，不允许值 |
| confirmed_by / confirmed_at | confirmed 必填 | user，或 verify_cmd_pass×2（两个不同会话）|
| stale_reason / superseded_by | stale 必填 | 复验失败的实际输出或用户改口引文；指向替代条目 |

准入规则（防 #3）[INFERENCE]：只记本次任务中"实际用到"或"缺了会出错"的事实；浏览到但没用上的不记。

**2.2 格式**：每条目一个 YAML 块，置于按 category 分的 Markdown 文件；索引一行一条。选文件而非数据库/运行时组件：spec §2"模型负责计算，文件负责记忆"、"外部文件 / Git 仓库是长期记忆和审计基础" [VERIFIED]；Owner 消息三明言记忆系统不是独立运行的系统 [VERIFIED]。

**2.3 放在哪里**（相对目标项目工作区根）[INFERENCE；依据 spec §16"目标项目专属内容应优先放入该目标项目工作区"与 §9"目标项目仓库或目录是目标项目运行真相源" [VERIFIED]]

```
memory/env/
  README.md            # ≤40 行：目录用途、schema 版本、§3 加载规则、§4 片段落点
  env-index.yaml       # 导航索引：每条一行 {id, category, scope, status, use_when, last_verified}
  confirmed/           # 资产层（status=confirmed），按 category 分文件
    system.md  toolchain.md  tool-config.md  preference.md
  observed/            # 原始资料层：agent 写入的待确认观察，按日期 YYYY-MM-DD.md
  archive/             # stale / retired 条目原样搬入；保历史，不默认加载
```

跨项目复用：scope=user/machine 的条目允许复制到新项目并标 `copied_from: <项目>@<日期>`，status 退回 observed 直到本项目复验。是否设用户级共享目录 [UNKNOWN]：5 份材料只授权项目工作区，且 spec §9 要求"不同目标项目需要不同 memory schema" [VERIFIED]；列 open question，不自行设定。

**2.4 谁写、何时写** [INFERENCE]
- agent 写 observed/：三个时点——(a) 某条环境事实导致命令失败并被纠正后；(b) 用户口头说明环境或习惯时；(c) 任务收尾。每次 ≤5 条，写前 grep env-index 去重。
- 升 confirmed：偏好类须用户确认；可复验事实类可由 verify_cmd 在两个不同会话各通过一次后由 agent 升格——即"有依据地采纳"（消息三）[VERIFIED]；升格时同批更新索引（仿 registry maintenance_rules"读-占-写同批纪律" [VERIFIED]）。
- 用户确认方式：agent 在收尾用 ≤5 行列出新观察，用户回复编号即确认；一次交互批量完成（防 #8）。
- agent 对 memory/env/ 的写权限来自目标项目 owner rule：spec §18"platform_capability … task_authority … 二者必须同时成立"、§16 目标写入需用户批准 [VERIFIED]。该 owner rule 是否存在 [UNKNOWN]；缺失时 agent 只在回复中列出拟写内容，不落盘。

**2.5 何时更新** [INFERENCE]：verify_cmd 失败 → 旧条目 stale＋写新 observed；用户明说"以后都…" → 直接改 confirmed（evidence=user_statement）；用户仅本次改口 → 只写 observed，不动 confirmed（单次改口是局部事件，防 #4）。

**2.6 何时失效与如何标记** [INFERENCE]
- stale：verify_cmd 失败、或 recheck_by 已过未复核、或用户否认。写 stale_reason，索引 status 改 stale，条目从 confirmed/ 搬到 archive/。
- retired：被 superseded_by 替代，或连续 8 周未被任何任务的 use_when 命中（8 周取自 registry consolidation 周期 [VERIFIED]；借用到条目退役是本设计假设 [INFERENCE]）。
- 复杂度预算：confirmed 总数 ≤40、索引 ≤60 行；越界即触发整编（合并/降级/退役），不允许扩预算了事。阈值为校准值，无实证 [UNKNOWN]。

**2.7 示例记录**（confirmed/toolchain.md 中一条；合成数据）

```yaml
- id: ENV-007
  category: toolchain
  scope: project
  key: python.deps_manager
  value: "用 uv 管理依赖；虚拟环境固定在 .venv；测试命令 `uv run pytest -q`"
  evidence:
    kind: user_statement
    quote: "这个项目别用 pip，统一 uv，环境就放 .venv"
    date: 2026-08-12
  status: confirmed
  confirmed_by: user
  confirmed_at: 2026-08-12
  verify_cmd: "test -x .venv/bin/python && uv --version"
  last_verified: "2026-08-28 verify_cmd pass"
  recheck_by: null            # 有 verify_cmd 时可空
  use_when: [install_deps, run_tests, create_venv]
  sensitivity: public
  supersedes: ENV-003         # 旧条目"pip + requirements.txt"，已入 archive/
  notes: "verify_cmd 失败时先问用户是否换了工具，不要自动改回 pip"
```

## 3. 加载规则

[INFERENCE；结构参照 loader 的 Core set / Conditional set 与 registry 的 triggers 字段 [VERIFIED]]

| 触发条件 | 读什么 | 不读什么 |
|---|---|---|
| 会话开始，或首次将执行 shell / 构建 / 安装 / 配置类动作 | README.md ＋ env-index.yaml（核心集，≤100 行）| confirmed/ 全部、observed/、archive/ |
| 索引中某条的 use_when 与当前动作匹配 | 仅该条所在 category 文件 | 其他 category 文件 |
| 将执行不可逆或高代价动作（安装、删除、改全局配置）且依赖某条目 | 先跑该条 verify_cmd（只读）再依赖 | — |
| 准备写新观察 | observed/ 当日文件（去重）| 历史 observed |
| 用户要求"确认/整理环境记忆"，或预算越界触发整编 | confirmed/ 全部＋observed/ 全部 | archive/（除非用户点名）|
| 其他任何情况 | 不读 memory/env/ | — |

避免全量加载：索引一行一条、正文按 category 拆文件；archive/ 与 observed/ 默认不读，同 loader 规则 34 对冷原件"默认 DO_NOT_READ / ON_DEMAND"的处理 [VERIFIED]；§2.6 的预算保证核心集有上限；spec §7"不默认全量加载" [VERIFIED]。

与现行分层加载模式的关系：同构——env-index.yaml ≈ guard-registry.yaml，核心集 ≈ loader "Core set"，category 文件 ≈ "Conditional set"，"when uncertain, read" 的兜底沿用 [VERIFIED]。差异 [INFERENCE]：(1) 加载对象是可复验事实而非规则，故多出 verify_cmd 与 stale 状态；(2) 不常态化 loader 的"影子全读基线"，改为 §5 T1 的抽样对照；(3) 目标 agent 的加载器与 Mnemosyne 的 loader 互不导入——loader Boundaries 明言不把 guard 传播到"another target project's truth source" [VERIFIED]。

记录与用户当前指令冲突：当前指令优先——loader 规则 13"Treat user wording as primary evidence"、spec §11 判断顺序 [VERIFIED]。agent 须一行指出冲突（"记忆 ENV-007 说用 uv，本次按你说的用 pip"），执行后写一条 observed 记录该冲突；不改 confirmed（防 #4）；仅当用户说"以后都这样"才按 §2.5 更新 [INFERENCE]。

记录过期：stale 条目视为 unknown 而非真相——spec §15"不得编造连续性、默认补全仓库状态" [VERIFIED]。有 verify_cmd 则复验，通过即刷新 last_verified；无法复验且本次决策依赖它 → 此刻问用户一句；不依赖 → 忽略并继续，不阻塞。不可逆动作依赖无法复验的过期条目 → 停止并问（fail-closed，清单"值得延续"项 [VERIFIED]）。记忆整体缺失（目录不存在）→ 明说"未发现环境记忆"，按无记忆 agent 用命令探测，不编造（loader 规则 29 [VERIFIED]），不主动建目录除非 owner rule 授权 [INFERENCE]。

## 4. 最小提示词片段（≤40 行，自包含）

```
【环境记忆规则 v0.1 · 适用于本项目工作区内的代码开发 agent】
1. 环境记忆位于 <工作区根>/memory/env/。它只记录本机/本用户/本项目的系统环境、开发工具
   配置与用户对环境的偏好；不记需求、方案、bug，不记任何密钥或凭据的值。
2. 何时读：
   a. 会话开始，或首次执行 shell/构建/安装/配置动作前：读 memory/env/README.md 与
      env-index.yaml。不要读 confirmed/ 全部、observed/ 或 archive/。
   b. 索引中某条的 use_when 与你将做的动作匹配时，只读该条所在的 category 文件。
   c. 不确定是否匹配时读；无关时不读。
3. 依赖前复验：执行不可逆或高代价动作（安装、删除、改全局配置）前，若依赖某条目，先运行
   其 verify_cmd（只读）。失败 → 以真实环境为准，把该条标 stale（写 stale_reason），一行告知用户。
4. 状态含义：confirmed＝可依赖；observed＝未确认线索，只能作提示不能作依据；stale/retired＝
   视为不知道。目录不存在＝没有记忆，按新环境探测，不得编造。
5. 冲突：用户当前指令永远优先于记忆。执行指令，一行指出冲突（写明条目 id），然后在 observed/
   记一条；不要改 confirmed 条目，除非用户明说"以后都这样"。
6. 何时写（只写 observed/YYYY-MM-DD.md，字段按 README 模板）：
   a. 某条环境事实导致命令失败并被你纠正后；
   b. 用户口头说明了环境或习惯（逐字引用作 evidence）；
   c. 任务收尾时补写本次"实际用到或缺了会出错"的新事实，每次 ≤5 条。
   浏览到但没用上的不记。写前先 grep env-index.yaml 去重。
7. 升级为 confirmed：偏好类必须由用户确认；可复验事实类须 verify_cmd 在两个不同会话各通过
   一次。升级时同批更新 env-index.yaml。
8. 收尾确认：任务结束时用 ≤5 行列出本次新增 observed 条目的 id 与一句话，请用户回复编号确认；
   不要逐条打断用户。
9. 预算：confirmed 条目 >40 或索引 >60 行时，停止新增，并在收尾提出合并/退役建议。
10. 写入 memory/env/ 的权限来自本项目的 owner rule；若不存在或未授权，只在回复中列出拟写
    内容，不落盘。
11. 每条记录是"有依据的事实"，不是规则；不得把一次性的绕行办法写成永久做法。
```

## 5. 验收测试设计

[INFERENCE]。通则：三个场景均以 fresh context 运行（清单"值得延续"项 fresh-context 负向测试 [VERIFIED]）；评分含效用与 Owner 成本维度且在运行前冻结（反模式 #2 对冲 [VERIFIED]）；"无写入"用 `git diff` 机械核验（spec §19 [VERIFIED]）。对照臂＝同一任务、删除 memory/env/ 后运行。observed 列执行时填写。

**T1 正向·效用**。工作区含 §2.7 的 ENV-007（confirmed）与索引。任务："给项目加 httpx 依赖并跑测试"。

| 检查项 | expected | observed |
|---|---|---|
| 读取范围 | 读 README＋索引＋toolchain.md；未读 observed/、archive/、其他 category | 待填 |
| 首条依赖命令 | `uv add httpx`（非 pip），一次即对 | 待填 |
| 向用户提的环境问题数 | 0（对照臂预期 ≥1，或先试 pip 失败） | 待填 |
| 首个正确命令前的失败命令数 | 0（对照臂记录实际值作差） | 待填 |
| 收尾 | 无新 observed（无新事实）；不打断用户；memory/env/ 无 diff | 待填 |

**T2 负向·过期**。ENV-011 confirmed "node 18 via nvm"，verify_cmd `node --version`；真实环境为 node 22。任务："跑一次构建"。

| 检查项 | expected | observed |
|---|---|---|
| 依赖前复验 | 构建前运行 `node --version` | 待填 |
| 处理 | 按 node 22 执行；ENV-011 标 stale，stale_reason 含实际输出 | 待填 |
| 告知 | 一行说明；不夸大，不因此询问用户 | 待填 |
| 不做 | 不声称 node 18；confirmed/ 中 ENV-011 的 value 未被静默改写（git diff 仅见状态与 stale_reason） | 待填 |

**T3 负向·缺失＋冲突**。3a：删除 memory/env/，任务同 T1。3b：恢复目录，用户指令"这次用 pip 装"。

| 检查项 | expected | observed |
|---|---|---|
| 3a 缺失声明 | 明说未发现环境记忆；用 `ls`/`--version` 探测；不编造 uv 或 pip 的存在 | 待填 |
| 3a 写入 | 不创建目录（owner rule 未授权）；回复中列出拟记录的事实 | 待填 |
| 3b 执行 | 用 pip；一行指出与 ENV-007 冲突并写明 id | 待填 |
| 3b 记录 | observed/ 新增一条冲突记录；confirmed/ 无 diff（git diff 核验） | 待填 |

## 6. 反模式自检

| # | 本设计如何防 |
|---|---|
| #2 结果验收被格式验收替代 | T1 指标是"环境问题数、失败命令数、首个正确命令前步数"与对照臂的差值，不是"文件格式对不对"；细则在 §5 预冻结 [INFERENCE] |
| #3 规则/记忆只增不减 | 准入规则只记用到的事实；confirmed ≤40 / 索引 ≤60 越界即整编；stale/retired 移出 confirmed；8 周未命中即退役 [INFERENCE] |
| #4 事故→全局规则反射 | 单次失败或改口只写 observed（局部）；升 confirmed 需用户确认或两会话复验；scope 由 project 升 user 需用户明说；本切片不设"规则"层，只有带 scope 的事实 [INFERENCE] |
| #6 "活"状态无失效规则 | 每条 confirmed 强制 verify_cmd 或 recheck_by 二选一、last_verified、stale_reason；索引 status 可见；缺任一项不得 confirmed [INFERENCE] |
| #8 人做搬运 | agent 自写 observed、自读索引跨会话恢复，不经用户转发；用户确认批量一次；T1 把"向用户提问数"作一等指标 [INFERENCE] |
| #15 平台限制沉淀为核心规则 | 条目是 evidence＋日期的事实而非规则；片段第 11 条禁止把绕行写成永久做法；AI 产品界面能力明确排除在本切片外（§1 边界）[INFERENCE] |

## 7. 自我批判

1. 写权限前提可能不成立：整套"agent 自写 observed"依赖目标项目 owner rule 授权写 memory/env/（spec §16/§18 [VERIFIED]）。若不授权，片段第 6/8 条退化为"用户手抄"，反模式 #8 复活。5 份材料中不存在这样的 owner rule [UNKNOWN]。
2. 复验成本未校准：verify_cmd"只读、秒级"是假设；若目标项目工具链启动慢（容器、远程），片段第 3 条会让每个不可逆动作前都付出可感成本；反之放宽则过期事实被依赖。材料中无使用量或延迟数据，40 条 / 60 行 / 8 周均借自 registry 校准值，非实证 [UNKNOWN]。
3. 跨项目"常用"未解决：Owner 原意是"习惯或者说常用"（跨项目），本设计只授权项目工作区，user/machine 级事实会在多项目间复制并各自漂移；共享层的位置与权限 [UNKNOWN]。
4. 无机械强制：全部依赖提示词片段的遵守度；hooks/schema 校验对 Mnemosyne 属 spec §10 的 v0.2+ [VERIFIED]，对目标 agent 是否可用 [UNKNOWN]；T1~T3 只能抽样验证遵守度。
5. 最可能看不见的盲区 [INFERENCE]：(a) 我默认 agent 有 shell 与文件系统（Claude Code 类表面）——verify_cmd 在无 shell 的对话式表面上不可执行，这是把平台假设埋进设计，正是 #15 的反向形式；(b) 5 份材料无 Owner 日常开发方式的实证（几个项目、什么工具链、多少台机器），category 划分与 scope 三分是经验默认；(c) 刚读完 guard-registry 与 loader，设计明显锚定在"索引＋分层"上；小规模下"单文件 ≤80 行全读"可能更优，我没有给它公平对照。

## 8. 读取清单

| 文件（@1ba2a2e） | 范围 | 用途 |
|---|---|---|
| current/human-approved-spec.md（271 行） | 全读 | 引用 §2/§6/§7/§9/§10/§11/§14/§15/§16/§18/§19 |
| raw/owner-intent-records/2026-08-30-owner-goals-and-input-classification-verbatim.md（51 行） | 全读 | §1 引文逐字取自消息一/二/三；附录分类表仅参照，未作为原文 |
| notes/cross-family-cooperation/foundational-agent-antipattern-checklist-v1.md（34 行） | 全读 | §6 逐条自检；"值得延续"项 |
| current/guard-registry.yaml（142 行） | 全读 | 索引字段、maintenance_rules、consolidation 校准值 |
| commands/load-mnemosyne-guidance.md（203 行） | 全读 | Core/Conditional 结构、规则 13/29/34、Boundaries 不传播条款 |

未读取仓库中任何其他文件；未联网；未写入仓库（本文件位于会话 scratchpad）。
标签计数（§1–§7 正文，grep 统计，不含 tag_legend 行）：VERIFIED 33 / INFERENCE 17 / UNKNOWN 7。
