# MNE-DR-020 / FABLE5-REDESIGN-001-RQ1 · 平台能力刷新

## Q1 · ChatGPT 记忆与 Projects 现状

**截至 2026-08-31。** 目前 ChatGPT 的长期连续性不是一个单一“Memory”，而是至少由 **Saved memories、Reference chat history、Projects 的项目级上下文/项目记忆、全局 Custom Instructions，以及项目级 instructions** 共同构成。OpenAI 将 saved memories 定义为与聊天记录分开保存、可在未来回答中使用的信息；Reference chat history 则允许 ChatGPT 从过去对话中提取相关信息，而不是把整段旧对话原样塞入当前上下文。删除聊天本身不会自动删除已经形成的 saved memory；反过来，仅删除 memory 也不会自动清掉旧聊天中的原始文本。citeturn2search0turn15search5

| 能力结论 | 截至 | 当前事实与边界 | 证据 |
|---|---|---|---|
| Saved memories | 2026-08-31 | 可由用户明确要求记住，也可由 ChatGPT 在适用情况下形成；作为独立于聊天历史的记忆层保存。删除聊天 ≠ 删除对应 saved memory。 | OpenAI Memory FAQ。citeturn2search0 |
| Reference chat history | 2026-08-31 | 可从旧对话中寻找相关细节。2026-01 起 Plus/Pro 对“从历史聊天找具体细节”的能力又有强化，并可把用到的旧聊天显示为来源。 | OpenAI Release Notes。citeturn15search5 |
| Memory 自动管理 | 2026-08-31 | Plus/Pro 在 2026-01 获得更主动的 memory 管理：相关信息优先、低价值内容退居后台，并支持搜索/排序与恢复旧版本。 | OpenAI Release Notes。citeturn15search5 |
| Projects | 2026-08-31 | 是持续工作空间：把聊天、文件/来源、项目 instructions 组织在一起；项目中的聊天可利用该项目上下文。 | Projects 帮助文档。citeturn1search0turn2search4 |
| Project-only memory | 2026-08-31 | 项目内聊天可引用同一项目其他聊天，但不会引用项目外聊天；项目内信息也不进入项目外聊天的引用范围。过去的 saved memories 不用于该项目。 | Projects 帮助文档。citeturn1search0turn3search23 |
| **存量 Project 转换** | **2026-08-31** | **已经可以改。** 符合条件且未共享的现有项目可在 Project settings 中在 default memory 与 project-only memory 之间切换，不必重建项目。共享项目则保持 project-only，不能切回默认模式。 | Projects + Release Notes。citeturn1search0turn1search2 |
| 全局 Custom Instructions | 2026-08-31 | Web、Desktop、iOS、Android 均支持，适用于所有计划；修改后会应用于对话。 | Custom Instructions FAQ。citeturn1search1 |
| 项目级 instructions | 2026-08-31 | Projects 有自己的项目 instructions，用于给该工作空间施加更局部的指令/背景；因此实际存在“全局个性化 → 项目局部指令 → 当前对话”的分层。 | Projects 文档。citeturn1search0 |

这里最重要的 **5–7 月后变化** 是 project-only memory 的转换限制已经消失。旧时“只有新建 Project 时才能选、存量不能原地转换”的结论，当前已明确过期。citeturn1search2turn3search0

**跨对话引用的边界。** 默认 Project memory 与 project-only memory 的隔离强度不同。project-only 模式是最明确的项目边界：同项目聊天可互相成为上下文来源，但项目外的历史不会被带进来；共享项目会自动采用这种隔离模式。普通项目则可依赖用户开启的 saved memories/reference chat history；在 Plus/Pro 上，OpenAI 还明确说项目聊天和文件会被优先考虑。citeturn1search0turn2search4

**Plus / Pro / Business 差异。** 截至本次核查，三者都具有 Projects、Memory 和付费级历史引用能力；并不存在一个官方称为“Pro 专属 Memory 算法”的独立机制。差别主要落在 **容量/使用量、项目规模以及管理控制**：OpenAI 当前把 Pro 描述为具有“Maximum memory and context”和更大的 Projects 能力；Business 则是工作空间产品，增加组织管理员、共享项目、模型/应用可用性与数据治理控制。GPT-5.6 的模型级选择也不同：Plus 包含 Medium/High，而 Pro 和 Business 还包含 Extra High 与 GPT-5.6 Sol Pro。citeturn22search1turn16view0turn18view0

需要注意，**Custom GPT 与上述个人/项目 Memory 不是同一连续性通道**：OpenAI 的 GPTs 文档明确说明 GPT 对话不会使用 saved memory、Custom Instructions 或以前的 GPT 对话作为持续上下文，因此不能把“自定义 GPT”视为 Projects/Memory 的等价替代。citeturn1search20

## Q2 · ChatGPT deep research 模式现状

**截至 2026-08-31。** deep research 仍是 ChatGPT 内一个独立研究工作流，但 2026 年以来它的入口、报告界面、来源控制、模型体系和 legacy 模式均发生了明显变化。当前可以通过在 prompt 中输入 `/Deepresearch`、点击输入框 `+`/tools 菜单中的 Deep research，或从 sidebar 进入。启动后可先审阅/修改研究计划；运行时可以查看进度，并可中途打断、补充要求或调整方向。citeturn16view1turn4search0

**模型/“智能程度”需要分成两件事看。** 当前 ChatGPT 的通用付费模型选择器已经不再是简单的旧式 “Instant / Thinking / Pro” 三档。GPT-5.6 官方口径是：**Instant、Medium、High、Extra High、Pro**；其中付费计划上的 Instant/Medium/High/Extra High 均由 **GPT-5.6 Sol** 以不同推理强度提供，Pro 则由 **GPT-5.6 Sol Pro** 提供。Plus 有 Medium/High，不含 Extra High 和 Pro；Pro 与 Business 均有 Medium/High/Extra High/Pro。Instant 还能在开启 Higher intelligence 时自动增加推理。citeturn16view0turn18view0

但是，**不能据此断言一次 deep research 后台就“一定是 GPT-5.6 Sol High”或某个固定模型**。当前 deep research 官方帮助页只称其由最新模型驱动，并没有公开给出每一次 ChatGPT deep research 任务的稳定、可核验底层 model ID。因此：

> **当前 ChatGPT deep research 的精确运行时底层模型：UNKNOWN。**

这也是相对于 2025/早 2026 的重要变化：最初 deep research 被明确描述为由“专门针对网页浏览和数据分析优化的 o3 模型版本”驱动；这种 **“deep research = o3”** 的产品事实已经不能继续当作 2026-08 的现状。citeturn4search0turn16view1turn15search2

**Plus / Pro 配额。** 这是本次核查中一个值得明确写 `UNKNOWN` 的项目。OpenAI 当前 deep research FAQ **不再公开给出 Plus、Pro 各自固定的每周/月任务数**；官方写法是“usage varies by plan”，剩余额度以产品内 usage counter 为准；如果属于固定月度额度，则从首次使用日期起每 30 天重置。当前定价页只用“expanded deep research / maximum deep research”一类相对表述描述计划差异。故不能把旧资料中的某组 10/120、25/250 或其他数字当作 2026-08-31 当前官方配额。citeturn16view1turn22search1

| 项目 | Plus | Pro | 截至 2026-08-31 官方可确认值 |
|---|---:|---:|---|
| Deep research 固定“每周次数” | **UNKNOWN** | **UNKNOWN** | 当前公开 FAQ 未给固定 weekly 数字。citeturn16view1 |
| Deep research 固定“每月次数” | **UNKNOWN** | **UNKNOWN** | 当前 FAQ 要求查看产品内 counter；固定月额度按首次使用后每 30 天重置。citeturn16view1 |
| 相对等级 | expanded | maximum | 当前定价页的官方定性。citeturn22search1 |
| Agent mode，供对比 | 40 次/月 | 400 次/月 | **这是 agent mode，不是 deep research 配额。** citeturn16view2 |

这一点尤其容易混淆：**Agent mode 的 40/400 月额度不能套给 deep research。** OpenAI 当前对 agent mode 明确公布 Plus 40、Pro 400 次/月，而 deep research 当前没有相同的公开固定数字表。citeturn16view2turn16view1

**运行时长与来源规模。** OpenAI 最初发布 deep research 时给出的典型运行时间为约 **5–30 分钟**；当前帮助页已不把这个范围写成服务保证，因此它应被理解为官方历史上的典型量级，而非 2026-08 的 SLA。OpenAI 当前研究产品资料则以“hundreds of sources（数百来源）”描述其研究综合能力；实际单次报告没有承诺固定来源数。citeturn4search0turn8search7

**MCP / apps / connectors。** 这是 2026 年的显著扩展。2 月更新后，OpenAI 宣布 deep research 可以使用更广泛的 connected apps，并可把研究限制在指定可信网站；发布说明还明确提到可连接 MCP/app 来源。当前 FAQ 的限制更关键：**deep research 只调用连接 app 中可用的 read actions，不在研究过程中执行 app write actions。** 因而“把 GitHub/Drive/其他 MCP 当研究资料源”与“让 deep research 修改外部系统”是两种不同能力。citeturn4search0turn22search7turn16view1

**与 agent mode 的关系。** 两者目前是并列工具，不是“deep research 已被 agent mode 吞并”。Deep research 的核心产物是可检查引用、来源与 activity history 的研究报告，连接 app 时保持只读；Agent mode 则是更通用的执行型工作流，可以使用 apps、浏览器/计算机能力，并在需要时执行有副作用的任务及请求用户确认。Agent mode 本身也可以做研究，但它有独立配额与风险模型。citeturn16view1turn16view2

**导出。** 当前完成后的 fullscreen report view 可直接下载为 **Markdown、Microsoft Word、PDF**；PDF 导出早在 2025-05 已上线，当前已统一扩展为上述多格式。citeturn16view1turn22search3

**Legacy deep research。** 2026-03-26 已移除 legacy deep research 模式；历史对话和既有研究结果继续保留。因此任何把 “legacy” 当成当前可选运行模式的旧流程已经过期。citeturn4search5turn22search3

## Q3 · ChatGPT 的 GitHub 连接与 Codex

**截至 2026-08-31。最关键结论：普通 ChatGPT 的标准 GitHub app/连接器当前是只读。** OpenAI 当前 GitHub 帮助页直接说明，该连接让 ChatGPT **读取 repository 以搜索和分析代码**；若要“生成、编辑并直接 push 代码”，官方指向 Codex。也就是说，普通聊天中的标准 GitHub app 当前不能作为一个通用写 GitHub 的接口去创建 branch、修改文件或创建 PR。citeturn10view0

这与 2026-07 的观察结论出现了直接冲突，因此旧结论“普通对话经 GitHub app 可执行写入类操作”在当前公开产品口径下应判为 **已过期**。citeturn10view0

GitHub 读取也不是“把整个仓库预先同步到 ChatGPT 的永久索引”。当前文档说标准 GitHub connection 是 **on-demand retrieval**：ChatGPT 根据问题形成搜索请求，按相关性获取仓库内容，必要时进行多次搜索；当前个人 GitHub integration 没有一个本地/ChatGPT 侧的全仓 persistent synced index。citeturn10view0

因此，对“列出所有 branch / PR / 文件是否有完备枚举保证”应特别谨慎：当前官方文档能够确认其 **查询与相关性导向**，但没有发现官方承诺“某次聊天检索会完备枚举仓库中的所有对象”。这也是 Q8 中旧结论第 6 项不能简单标成完全确认的原因。citeturn10view0

**审批卡。** ChatGPT 的 app/action 框架现在存在通用 action approval 机制：对于具有写入/操作能力的 app action，ChatGPT 可以先展示拟执行 action 的审批卡，让用户拒绝、单次允许，或在适用情况下调整后续权限。**但这只是 app 框架能力，并不能反推标准 GitHub app 具有写 action**；标准 GitHub app 的当前专门文档仍明确是 read-only。citeturn9search2turn10view0

**Codex Cloud 一句话现状。** Codex Cloud 是在隔离云环境中执行 coding task 的代理，可连接代码仓库、修改代码、运行检查、展示 diff，并把成果提交为 PR/供用户审阅；这是 OpenAI 当前推荐的 GitHub 写入路径之一。citeturn11search19turn11search1

**Codex CLI 一句话现状。** Codex CLI 是本地终端代理，可读写工作区、运行命令、连接 MCP/开发工具，并支持保存和 `resume` 既有 session；其本地执行和权限边界与普通 ChatGPT GitHub connector 是两种不同产品模型。citeturn15search12turn11search3turn15search16

当前 GPT-5.6 也已经进入 Codex 产品线；OpenAI 的 2026-08 GPT-5.6 文档说明 Plus/Pro/Business/Enterprise 的 Codex 可使用 Sol、Terra、Luna，而 Free/Go 使用 Terra。citeturn16view0

## Q4 · Claude 侧现状

**截至 2026-08-31。** Claude 在 2026 年夏季，尤其 8 月，已经不再是“网页端只有 Projects 文件知识、没有真正跨聊天 Memory”的状态。当前 Claude web/Desktop/mobile 有 **chat search + memory**，且 memory 已按 topics 管理；Projects 又拥有彼此隔离的项目记忆与项目摘要。Anthropic 8 月 release notes 明确说明 Memory 现在可跨 chat 和云端 Cowork 工作，Free/Pro/Max 默认开启，Team/Enterprise 默认关闭并由组织控制。citeturn13view0turn20search12

| Claude 网页能力 | 截至 | 当前状态 |
|---|---|---|
| Past-chat search | 2026-08-31 | Pro、Max、Team、Enterprise 可搜索过去聊天；在 Project 内搜索时范围限制在该项目。citeturn13view0 |
| Memory | 2026-08-31 | Free/Pro/Max 当前默认开启；按独立 topics 保存，可查看、编辑、删除。Team/Enterprise 默认关闭，可由组织启用。citeturn13view0turn20search12 |
| Project memory | 2026-08-31 | 每个 Project 有独立 memory/project summary，与其他 Projects 及非项目聊天隔离。citeturn13view0 |
| Projects | 2026-08-31 | 所有用户可用；Free 最多 5 个。项目拥有自己的 chat histories、knowledge base 与 project instructions。citeturn20search32 |
| Project knowledge | 2026-08-31 | 付费项目在知识量接近上下文限制后会使用 RAG，仅检索相关内容；官方称可把可用知识容量扩展到约传统上下文的 10 倍量级。citeturn13view1 |
| Chat 移动 | 2026-08-31 | 可把聊天移入/移出/在 Projects 间移动，之后按目标项目的记忆边界工作。citeturn13view2 |

**Claude Code 的长期记忆机制。** Claude Code 官方明确说每个新 session 的 active conversation context 从新会话开始，但提供两类跨 session 持久层：用户维护的 **`CLAUDE.md`** 与 Claude 自动维护的 **auto memory**。`CLAUDE.md` 可以按组织、用户、项目等 scope 放置持续说明；auto memory 则记录 Claude 自己形成的项目相关经验、修正和偏好，并在之后 session 加载。二者是“注入上下文”，而不是不可违反的安全配置。citeturn13view3

Auto memory 当前按 repository 组织并可跨 worktree 共享；官方还限制初始自动加载量，较大的记忆文件会按需读取。自定义 subagent 也可有自己的 memory；subagent 与父 agent 的上下文继承方式取决于其启动类型，并不能假定父 agent 的全部长期记忆始终被复制进去。citeturn13view3turn20search19

**Compaction。** Claude Code 在 active context 接近窗口上限时自动 compact，把较早的对话压缩成摘要以释放空间；也可以显式执行 `/compact`。因此“session transcript 仍在磁盘”不等于“模型每一轮仍逐 token 看到完整早期 transcript”。官方最佳实践明确警告陈旧/过量 context 会降低质量，而 compaction 本身可能丢掉重要细节。citeturn14search1turn14search17turn14search28

**Session resume。** CLI 把 session 定义为“与项目目录绑定的已保存 conversation”，可通过 resume/continue 恢复；恢复同一 session 会继续原 session ID，而 fork 会建立新 session。CLI、VS Code、Desktop、Web 各自有自己的 session history，因此不能假定所有 surface 自动共享同一份列表。citeturn20search20turn14search5

**网页 Claude Code。** `claude.ai/code` 当前可在远程 VM 中克隆 GitHub repository、运行 Claude Code 任务并在完成后创建 PR；与 CLI 的同步式交互相比，它定位于可以离开页面后继续执行的远程任务。citeturn21search15

**上下文窗口当前公开规格。** 这是近期变化非常大的部分。Anthropic 当前付费 Claude Chat 官方表述是：**Opus 5、Sonnet 5 = 1M token；Opus 4.8/4.7/4.6、Sonnet 4.6 = 500K；其他模型通常为 200K。** 也就是说，“Claude 网页只有 200K”已经不是当前完整事实。citeturn23view1

Claude Code 更进一步：在 Pro/Max/Team/Enterprise 中，Sonnet 5、Fable 5、Opus 5、Opus 4.8/4.7/4.6 可支持 **1M**；Pro 使用部分 Opus 的 1M 档需要启用 usage credits。Sonnet 4.6 在 Claude Code 也可到 1M，但除 usage-based Enterprise 外需要开启 usage credits。citeturn23view1

**计划与配额结构。** Anthropic 当前个人付费结构为 Pro、Max 5x、Max 20x；官方列价为 Pro **US$20/月或 US$200/年**、Max 5x **US$100/月**、Max 20x **US$200/月**。Max 的“5x/20x”是相对于 Pro 的 session capacity，而不是固定“每月 N 条消息”。citeturn21search17turn21search0

Pro 的 session-based usage limit 每 **5 小时**重置；实际可发消息量取决于 prompt/附件长度、当前会话长度、所用模型与功能。Anthropic 同时维护 weekly limits，Usage 页面会显示当前 5 小时 session 使用量以及 weekly reset；Claude.ai、Claude Code、Desktop 等 surface 对个人订阅的使用量是共享计算的。达到包含额度后，Pro/Max 可以开启 usage credits 按 API 标准费率继续工作。citeturn21search26turn21search23turn21search20turn21search8

因此，Claude 的当前配额最好描述为 **“5 小时 session 限额 + weekly 限额 + 可选 pay-as-you-go credits”**，而不是一个稳定的“每周固定消息条数”。citeturn21search23turn21search8

## Q5 · 原生“跨会话连续性”功能盘点

**截至 2026-08-31。** 两家公司现在都已经拥有多层 native continuity，但它们解决的问题不同：有的是记住“用户与偏好”，有的是共享一个项目的知识，有的是直接恢复原 session，还有的是把早期上下文压缩后继续同一长任务。

| 产品 / 原生功能 | 连续性的粒度 | 能保留/引用什么 | 主要边界与失败场景 |
|---|---|---|---|
| ChatGPT Saved Memory | 账户级 | 被保存的事实、偏好等 | 不是完整 transcript；删除聊天不会自动删除独立 memory。citeturn2search0 |
| ChatGPT Reference chat history | 账户级相关性检索 | 过去聊天中的相关细节 | 不是保证逐字、完整、确定性召回；开启状态和计划会影响可用性。citeturn2search0turn15search5 |
| ChatGPT Projects / default memory | 项目级 | 项目文件、来源、instructions、项目聊天 | 默认模式并非最强隔离；行为还受账户 memory 设置影响。citeturn1search0 |
| ChatGPT project-only memory | 强项目级隔离 | 仅同项目聊天与项目资料 | 不使用项目外 saved memories/聊天；共享项目不能切回 default。citeturn1search0 |
| ChatGPT Computer History | 设备/工作连续性 | 用户明确开启后，让 ChatGPT/Codex 获得此前计算机工作上下文，以帮助恢复先前工作 | 需主动开启且依赖 Memory；不是完整应用状态快照。该功能是 2026-08 新近公开能力。citeturn15search26turn15search19 |
| Codex `resume` | 原 session | 恢复保存的 coding session | session/工作目录作用域仍重要；恢复不等于模型永远保有未经压缩的所有原始 token。citeturn15search12turn11search3 |
| Codex compaction | 长 session | 用摘要延续任务 | 压缩后早期原始上下文不再全部直接占 active context；细节依赖摘要质量。citeturn16view3turn11search6 |
| Claude Memory | 账户级 topic memory | 跨聊天记忆的独立 topics | 可暂停/删除；敏感 topic 默认不进入 memory；删除聊天并不必然移除已经形成的独立 memory。citeturn13view0turn20search12 |
| Claude Projects | 项目级 | 项目聊天、knowledge、instructions、独立 project memory/summary | Project memory 与其他项目/普通聊天隔离。citeturn13view0turn20search32 |
| Claude chat search | 旧对话检索 | 找过去聊天中的内容 | 项目内检索被限定在该项目；不是把全部旧聊天持续装入当前 context。citeturn13view0 |
| Claude Code `CLAUDE.md` | repo / user / org | 人工维护的稳定规则与背景 | 是上下文说明，不是强制执行的系统配置。citeturn13view3 |
| Claude Code auto memory | repository | Claude 自己总结的经验/修正 | 是抽取式记忆，不是完整历史；加载量受限。citeturn13view3 |
| Claude Code `resume` | 原 session | 恢复保存的 transcript/session | 各客户端 surface 的 session history 并非自动统一。citeturn20search20 |
| Claude Code compaction | 同一长 session | 用摘要腾出 context | Anthropic 明确承认重要细节可能在 compaction 中丢失，因此不是无损 handoff。citeturn14search28 |
| Perplexity Sessions | 原 Session | 保存问题、follow-up、回答和来源，可继续同一 Session | 官方 Session 文档保证的是同 Session 连续性；不应由此推导跨任意新 Session 都能完整召回旧工作。citeturn21search7 |

一个重要共同边界是：**“跨会话连续性”几乎都不是逐 token、无损复制上一会话 active context。** ChatGPT 的 Reference chat history 与 saved memory 是相关性/抽取式机制；Claude Memory 同样是 topic 化记忆；Claude Code/Codex 的超长 session 又会进入 compaction。它们都能增强连续性，但都不等同于把整个历史对话原样重新输入模型。citeturn2search0turn13view0turn14search1turn16view3

在“真正恢复同一个工作实例”这一类别，**Claude Code session resume 和 Codex resume** 比普通聊天的 memory 更接近传统会话恢复，因为它们恢复的是已保存的 agent session，而非只检索若干记忆条目；但模型可见的 active context 仍可能经过 compaction。citeturn20search20turn15search12turn14search28

## Q6 · 对话内模型自识别

**截至 2026-08-31。结论需要区分“产品客户端知道当前选择”和“让模型在自然语言回答中可靠自我识别”两件事。**

**ChatGPT 普通对话：未发现官方机制允许模型通过自然语言可靠自省当前实际运行 model ID。** OpenAI 当前专门的帮助文档明确说明，ChatGPT **看不到系统如何运行，也不能访问内部运行状态、系统日志或进行真实技术诊断**；它根据当前聊天配置描述自己的能力，不应把类似“我现在运行的是 X 模型”的自然语言声明当作实时运行时查询。citeturn23view0

这一点在当前自动路由体系下尤其重要。GPT-5.6 文档明确说明，即使 UI 仍选中 Instant，ChatGPT 可以自动增加推理；达到 reasoning allowance 后，还可能改用另一可用 reasoning model。因此 **model picker 显示用户选择，与“这一次具体请求实际上由哪个运行路径完成”并非在所有情况下等价**。citeturn16view0

所以对 ChatGPT 的精确回答是：

> **对话内靠问 ChatGPT 自己：未发现官方可靠运行时模型自识别机制。**  
> UI/产品层可以显示用户选择的模式，但不能把模型自己的文字回答当作可信 runtime model telemetry。citeturn23view0turn16view0

**Codex：客户端层存在官方模型配置/元数据机制，但这不等于自然语言“自省”。** Codex 的官方 config schema 有明确的 `model` 设置，并把 `model_context_window` 定义为“active model 可用的 context window”；TUI/配置体系也允许把 `model` 作为状态信息展示。因此由 Codex 客户端读取/显示已选择的 active model 是官方能力。citeturn16view3turn15search22

但若问题严格限定为 **“让 agent 自己在回答文本中通过内省确认实际后端 model ID”**，本次没有找到 OpenAI 官方保证；故这一更严格命题仍应写：

> **Codex 自然语言自报运行时 model ID：UNKNOWN / 未发现官方可靠自省保证。**

**Claude 网页对话：同样未发现把自然语言自报作为可靠 runtime 机制的官方保证。** 用户可以在产品 UI 中选择模型，但 Anthropic 当前甚至有专门文档解释某些请求为什么可能发生 model fallback/switch，这意味着“聊天顶部选择的模型”和“每次请求最终实际处理路径”也需要区别对待。citeturn20search29

**Claude Code 则有更明确的客户端级机制。** 官方支持 `/model` 修改当前模型；status-line 和 hook/runtime 数据可以由客户端输出当前 session 数据。因此脚本/客户端获得模型元数据属于受支持功能。citeturn20search6turn20search5

Anthropic 的 Agent SDK 类型进一步明确，assistant message 对象包含 `model` 字段。这能证明 **机器可读 assistant-message 元数据中可以存在 model ID**，但它仍不是“Claude 通过自然语言推理知道自己是谁”。citeturn20search34

因此 Q6 的最终分类是：

| Surface | 官方客户端/UI 可知模型？ | “问模型自己”可作为可靠自识别？ | 截至 2026-08-31 |
|---|---|---|---|
| ChatGPT 普通对话 | 可看到选择/模式；实际路由可能自动变化 | **否；未发现官方机制** | citeturn23view0turn16view0 |
| Codex | **是，客户端有 model 配置/状态字段** | **未发现官方自然语言自省保证** | citeturn16view3turn15search22 |
| Claude 网页对话 | 有模型选择 UI，但存在 fallback/switch 情形 | **未发现官方机制** | citeturn20search29 |
| Claude Code | **是，`/model` 与客户端/runtime metadata 可提供模型信息** | 不应等同于模型自然语言自省 | citeturn20search6turn20search5 |

## Q7 · 上下文窗口与长对话行为

**截至 2026-08-31。** 必须首先区分 **API 模型最大窗口**、**ChatGPT/Claude 产品实际开放窗口** 和 **长对话经过 compaction 后能够继续多久**。三者不是一个数字。

**ChatGPT。** 2026-02-20 的官方 release note 曾明确宣布，手动选择 Thinking 时，ChatGPT 总上下文达到 **256K tokens：128K input + 128K max output**，此前为 196K。这是可核验的 ChatGPT 产品数字。citeturn17search1turn17search20

随后 GPT-5.6 在 8 月进入新的模型/推理选择器。当前 GPT-5.6 ChatGPT 主文档公布了 Instant/Medium/High/Extra High/Pro 与计划可用性，但 **没有在该当前页面公布一组统一的 Plus/Pro ChatGPT UI context-window 数字**。因此不应拿 API 的 **1.05M** 直接替代 ChatGPT 产品数字。citeturn16view0turn17search3

OpenAI API 的 GPT-5.6 Sol 本身当前确实公开为 **1,050,000-token context window、128,000 max output**；这是 **API model specification**，不能据此推出普通 ChatGPT 对话必然获得 1.05M active context。citeturn17search3turn17search6

因此对于“2026-08-31 Plus/Pro 普通 ChatGPT GPT-5.6 的精确 active context window”：

> **UNKNOWN：当前公开 ChatGPT GPT-5.6 主文档没有给出一个可以安全泛化到所有 Plus/Pro 模式的统一数字。**

OpenAI 对标准 ChatGPT 超长对话究竟采用何种具体 truncation/summary 算法，也没有像 Claude 那样在当前消费者帮助页公开完整机制。官方曾说明 GPT-5.4 改进了 context-window management，但没有公开一个可以据此复现的截断/压缩规则。因此对“普通 ChatGPT 何时压缩、丢哪一段”的精确算法应记为 **UNKNOWN**。citeturn17search0turn19search4

**Codex。** Codex 明确有自动 compaction 配置：官方 config reference 提供 `model_auto_compact_token_limit`，用于设置触发自动 history compaction 的 token threshold，同时 `model_context_window` 表示 active model 可用的窗口。换言之，Codex 对超长 agent session 的公开模型不是“简单到上限就立即停止”，而是支持历史压缩。citeturn16view3

Codex 的实际上下文还取决于模型与客户端配置，不能用单一数字概括全部 Codex。官方曾宣布 GPT-5.4 在 Codex 中实验支持 **1M context**，而 GPT-5.3-Codex-Spark research preview 则明确是 **128K**。当前 GPT-5.6 Sol API 模型支持 1.05M，但 Codex 默认实际采用多少有效窗口仍可能受产品配置影响；因此“所有 Codex GPT-5.6 session 默认 1.05M”并没有官方依据。citeturn15search9turn17search26turn17search3

**Claude Chat 当前数字则非常明确。**

| Claude 模型 / surface | 官方窗口 | 截至 |
|---|---:|---|
| Claude Opus 5，Claude Chat 付费计划 | **1M** | 2026-08-31 |
| Claude Sonnet 5，Claude Chat 付费计划 | **1M** | 2026-08-31 |
| Opus 4.8 / 4.7 / 4.6，Claude Chat | **500K** | 2026-08-31 |
| Sonnet 4.6，Claude Chat | **500K** | 2026-08-31 |
| 其他付费 Chat 模型 | 通常 **200K** | 2026-08-31 |
| Claude Code：Sonnet 5、Fable 5、Opus 5、Opus 4.8/4.7/4.6 | **最高 1M**；具体计划/credits 条件适用 | 2026-08-31 |
| Claude Code Sonnet 4.6 | **1M**，通常需 usage credits；usage-based Enterprise 例外 | 2026-08-31 |

以上均来自 Anthropic 当前帮助页。citeturn23view1

Claude 对长聊天的处理也比 ChatGPT 公布得具体：在付费计划且开启 code execution 时，接近 context limit 后 Claude 会 **summarize earlier messages to make room for new content**；完整 chat history 仍保存供系统后续引用，因此在大多数情况下可以继续对话，而不是用户一碰硬上限就必须重新开 chat。官方也明确保留例外，例如单个首条输入过大或系统错误仍可触发长度限制。citeturn23view1turn20search22

Claude Code 的 compaction 则更直接地暴露给用户：`/compact` 可以主动执行，系统也会自动执行。Anthropic 自己警告，compaction 可能丢失重要细节，过多陈旧 context 也会让模型受到干扰、质量下降。因此“上下文窗口大”不能解读为“无限长任务中的每个旧事实都同等可靠保留”。citeturn14search1turn14search17turn14search28

## Q8 · 旧结论核对表

**判定基准：截至 2026-08-31；只在现有官方公开证据足以支持时判“仍成立”或“已过期”，否则按任务书要求记为“无法确认 / UNKNOWN”。**

| 旧结论 | 判定 | 2026-08-31 新事实 / 核对说明 | 主要证据 |
|---|---|---|---|
| **1. “ChatGPT 普通对话经 GitHub app 可执行写入类操作（建分支/文件/PR）。”** | **已过期** | 当前标准 GitHub app 官方明确为 **read-only repository access**；编辑、push、PR 等写入路径官方指向 Codex。通用 app approval 卡的存在不能改变 GitHub app 自身只读这一事实。 | OpenAI GitHub FAQ。citeturn10view0turn9search2 |
| **2. “Deep Research 由 o3 类模型执行。”** | **已过期** | 这是早期 deep research 的官方描述，但当前 deep research 页面只称由“latest models”驱动；legacy deep research 也已在 2026-03-26 移除。当前每次 DR 的精确后台 model ID 为 **UNKNOWN**。 | Deep Research 当前 FAQ、发布页、Release Notes。citeturn16view1turn4search0turn4search5 |
| **3. “Project-only memory 只能在新建 Project 时选择，存量 Project 不能原地转换。”** | **已过期** | 当前符合条件的**现有未共享 Project 可在 settings 中转换** default ↔ project-only；共享 Project 保持 project-only，不可切回。 | Projects + Release Notes。citeturn1search0turn1search2 |
| **4. “Deep Research 期间对连接的 app 只执行读取类动作。”** | **仍成立** | 当前 FAQ 仍明确写：deep research 使用连接 app 的 available read actions，**不使用 write actions**。 | OpenAI Deep Research FAQ。citeturn16view1 |
| **5. “同步的 app 数据可能进入 ChatGPT Memory；断开连接不删除既往对话中的数据。”** | **无法确认** | 当前 Memory 文档能确认聊天与 saved memory 是独立存储关系，但本次检索**没有找到一条当前官方文档继续完整确认“synced app 数据可进入个人 Memory”这一整句机制**。因而不能把旧观察整体继续定性为成立。断开 app 与历史聊天/Memory 删除也应分别处理，不能假定断开连接等于清除既有持久数据。 | Memory FAQ、Apps 文档。citeturn2search0turn9search2 |
| **6. “GitHub 搜索/同步是相关性导向，不保证完整枚举分支/PR。”** | **无法确认（核心机制吻合，保证性措辞无官方明示）** | 当前标准 GitHub integration 确实是 **on-demand、query/relevance-oriented retrieval**，而且没有个人仓库的预同步索引；但本次未找到 OpenAI 明文写“绝不保证枚举所有 branches/PRs”。因此“相关性导向”成立，“不保证完整枚举”作为正式保证性命题只能记 UNKNOWN。 | GitHub integration FAQ。citeturn10view0 |
| **7. “ChatGPT 对话无可靠的运行时模型自识别能力。”** | **仍成立** | OpenAI 当前官方明确说 ChatGPT 看不到其系统实时如何运行、不能做内部诊断。当前自动 reasoning/fallback 进一步说明模型自报不能替代 runtime telemetry。 | OpenAI “How to Ask ChatGPT About Its Features”、GPT-5.6 FAQ。citeturn23view0turn16view0 |
| **8. “Claude 网页 Research 模式读不到 GitHub 仓库，需用 Project knowledge 替代。”** | **无法确认；旧基础已明显变化** | 2026-07-10 起官方已有 Claude GitHub integration，可把 repo 直接连接到 Claude；Research 也明确能跨 web 与 connected internal context 研究。但当前 Research FAQ举出的已确认 connected context 主要是 Google Workspace，本次未找到一句足以证明“GitHub connector 必然可作为 Research source”的官方明文，因此不能直接把旧结论判为完全反转。Project knowledge 已不再是唯一公开的 GitHub 上下文途径。 | Claude GitHub integration、Research FAQ。citeturn20search0turn23view2 |
| **9. “Claude Code 会话记录（JSONL）含逐响应模型标识。”** | **无法确认** | Anthropic 官方确认 Agent SDK 的 assistant message 对象包含 `model`，也确认 session transcript 默认以 JSONL 形式持久化；但本次未找到当前 Claude Code 文档对**本地原始 transcript JSONL schema**作出“每一条 assistant response 必有 model 字段”的正式保证。故不能把 SDK message schema 等同于持久化 transcript schema。 | Agent SDK types、session storage。citeturn20search34turn20search13 |

综合 5–7 月旧结论，**确定发生的三项关键反转**是：普通 ChatGPT GitHub connector 当前明确只读；project-only memory 已支持符合条件的现有 Project 原地转换；“deep research = o3”已不能作为当前模型事实。与此同时，**deep research 对 app 保持 read-only** 与 **ChatGPT 无可靠自然语言 runtime 模型自省** 仍有明确官方证据继续成立。citeturn10view0turn1search2turn16view1turn23view0

Claude 侧变化则更大：到 2026-08，网页 Claude 已有正式跨聊天 Memory/project memory，付费 Chat 的新模型已出现 1M context，Claude Code 则继续提供 `CLAUDE.md`、auto memory、resume、compaction、subagents 等多层连续性机制。citeturn20search12turn23view1turn13view3turn20search20

**来源表（访问日期均为 2026-08-31）**

| 编号 | 标题 | URL | 访问日期 |
|---|---|---|---|
| S01 | OpenAI · Memory FAQ | https://help.openai.com/en/articles/8590148-memory-faq | 2026-08-31 |
| S02 | OpenAI · Projects in ChatGPT | https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt | 2026-08-31 |
| S03 | OpenAI · ChatGPT Release Notes | https://help.openai.com/en/articles/6825453-chatgpt-release-notes | 2026-08-31 |
| S04 | OpenAI · ChatGPT Custom Instructions | https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions | 2026-08-31 |
| S05 | OpenAI · GPTs in ChatGPT | https://help.openai.com/en/articles/8554407-gpts-in-chatgpt | 2026-08-31 |
| S06 | OpenAI · Deep research in ChatGPT | https://help.openai.com/en/articles/10500283-deep-research-in-chatgpt | 2026-08-31 |
| S07 | OpenAI · Introducing deep research | https://openai.com/index/introducing-deep-research/ | 2026-08-31 |
| S08 | OpenAI · GPT-5.6 in ChatGPT | https://help.openai.com/en/articles/20001354 | 2026-08-31 |
| S09 | OpenAI · Model Release Notes | https://help.openai.com/en/articles/9624314-model-release-notes | 2026-08-31 |
| S10 | OpenAI · ChatGPT Pricing | https://openai.com/chatgpt/pricing/ | 2026-08-31 |
| S11 | OpenAI · ChatGPT agent | https://help.openai.com/en/articles/11752874-chatgpt-agent | 2026-08-31 |
| S12 | OpenAI · Apps in ChatGPT | https://help.openai.com/en/articles/11487775-connectors-in-chatgpt | 2026-08-31 |
| S13 | OpenAI · Connecting GitHub to ChatGPT | https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt | 2026-08-31 |
| S14 | OpenAI · Using Codex with your ChatGPT plan | https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan | 2026-08-31 |
| S15 | OpenAI · Codex Cloud | https://developers.openai.com/codex/cloud | 2026-08-31 |
| S16 | OpenAI · Codex CLI | https://developers.openai.com/codex/cli | 2026-08-31 |
| S17 | OpenAI · Codex Configuration Reference | https://learn.chatgpt.com/docs/config-file/config-reference | 2026-08-31 |
| S18 | OpenAI · Computer History | https://developers.openai.com/codex/customization/computer-history | 2026-08-31 |
| S19 | OpenAI · GPT-5.6 Sol Model | https://developers.openai.com/api/docs/models/gpt-5.6-sol | 2026-08-31 |
| S20 | OpenAI · Research use case | https://openai.com/solutions/use-case/research/ | 2026-08-31 |
| S21 | OpenAI · How to Ask ChatGPT About Its Features | https://help.openai.com/en/articles/12548278-how-to-ask-chatgpt-about-its-features | 2026-08-31 |
| S22 | Anthropic · Use Claude’s chat search and memory to build on previous context | https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context | 2026-08-31 |
| S23 | Anthropic · What are projects? | https://support.claude.com/en/articles/9517075-what-are-projects | 2026-08-31 |
| S24 | Anthropic · Claude Code: Memory | https://code.claude.com/docs/en/memory | 2026-08-31 |
| S25 | Anthropic · Manage sessions | https://code.claude.com/docs/en/sessions | 2026-08-31 |
| S26 | Anthropic · How Claude Code works | https://code.claude.com/docs/en/how-claude-code-works | 2026-08-31 |
| S27 | Anthropic · How large is the context window on paid Claude plans? | https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans | 2026-08-31 |
| S28 | Anthropic · How do usage and length limits work? | https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work | 2026-08-31 |
| S29 | Anthropic · What is the Pro plan? | https://support.claude.com/en/articles/8325606-what-is-the-pro-plan | 2026-08-31 |
| S30 | Anthropic · Choose a Claude plan | https://support.claude.com/en/articles/11049762-choose-a-claude-plan | 2026-08-31 |
| S31 | Anthropic · What is the Max plan? | https://support.claude.com/en/articles/11049741-what-is-the-max-plan | 2026-08-31 |
| S32 | Anthropic · Manage usage credits for paid Claude plans | https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans | 2026-08-31 |
| S33 | Anthropic · Usage limit best practices | https://support.claude.com/en/articles/9797557-usage-limit-best-practices | 2026-08-31 |
| S34 | Anthropic · Use research on Claude | https://support.claude.com/en/articles/11088861-use-research-on-claude | 2026-08-31 |
| S35 | Anthropic · Use the GitHub integration | https://support.claude.com/en/articles/10167454-use-the-github-integration | 2026-08-31 |
| S36 | Anthropic · Claude Code on the web | https://support.claude.com/en/articles/12618689-claude-code-on-the-web | 2026-08-31 |
| S37 | Anthropic · Model configuration | https://code.claude.com/docs/en/model-config | 2026-08-31 |
| S38 | Anthropic · Customize your status line | https://code.claude.com/docs/en/statusline | 2026-08-31 |
| S39 | Anthropic · Agent SDK reference — TypeScript | https://code.claude.com/docs/en/agent-sdk/typescript | 2026-08-31 |
| S40 | Anthropic · Persist sessions to external storage | https://code.claude.com/docs/en/agent-sdk/session-storage | 2026-08-31 |
| S41 | Anthropic · Claude Release Notes | https://support.claude.com/en/articles/12138966-release-notes | 2026-08-31 |
| S42 | Perplexity · What is a Session? | https://www.perplexity.ai/help-center/en/articles/10354769-what-is-a-thread.html | 2026-08-31 |