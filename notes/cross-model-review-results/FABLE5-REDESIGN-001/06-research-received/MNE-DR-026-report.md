# MNE-DR-026 / FABLE5-REDESIGN-001-RQ9 · 开发知识资产与自用代码库实践

## 开发知识资产实践现状

**Q1 · 2024–2026 团队与个人层面的“开发知识管理 × AI”实践、成熟度与失败经验**

**结论：用户设想并不是一个全新的方向，而是若干已经成熟或正在快速成形的实践的交汇点。** 其中，ADR、版本化运行说明、可复现环境、回归测试等“知识即工程制品”已经相当成熟；`AGENTS.md`、`CLAUDE.md`、Copilot instructions、Agent Skills 等“给 AI 使用的持久上下文”在 2025–2026 年迅速形成生态；但“让 AI 自动从多项目经验中形成可靠、长期、自我更新的个人开发知识体系”仍处于研究和早期实践阶段。现有证据尤其不支持把一个越来越大的 Markdown/向量库简单等同于“成熟的长期记忆”。citeturn17view0turn19view5turn18view2

**【论文实证】持久化 agent 上下文已经从零散技巧变成可观察的软件制品。** 2025 年 *Agent READMEs* 对 1,925 个公开仓库中的 2,303 个 agent context files 进行研究，发现这些文件并非静态 README，而像配置代码一样持续演化；69.9% 包含实现细节、67.7% 包含架构信息、62.3% 包含构建/运行信息。但安全与性能要求都只出现在 14.5% 的文件里，说明开发者很容易把“如何让 agent 跑起来”资产化，却没有同等程度地资产化非功能约束。citeturn19view5

这一现象也具有明显的维护特征：研究样本中，多提交维护的比例在 Claude、Copilot、Codex 三类 context files 上大约为 59%–67%，而修改以不断“追加”内容为主、删除较少。这说明上下文文件已经被当作持久配置，但也天然倾向于越积越多。另一项针对 100 个热门开源仓库的 2026 年研究随后发现，62% 存在把 linter 已能表达的规则重复写入上下文的 “Lint Leakage”，42% 有 Context Bloat，35% 有 Skill Leakage；Context Bloat 又经常与冲突指令共同出现。citeturn4view1turn19view6

**【论文实证】“有 context file”不等于“agent 一定做得更好”。** 这是目前最重要的负面证据。2026 年 AGENTbench 研究在 138 个真实 GitHub issue 任务上发现，开发者自己维护的 context file 相对于无 context 平均约有 **+4%** 成功率改善，但 LLM 自动生成的 context file 平均约 **-3%**，同时推理成本普遍增加约 20%；研究者因此主张文件应保留“最小必要要求”，而非堆积所有仓库知识。citeturn12view0 另一项 288 次运行、17 个任务、3 个仓库的双 agent 消融研究没有检测到可测量的正确率变化，并把许多失败归因于实现能力而不是仓库知识缺失。citeturn12view2

与此同时，也有较积极但测量目标不同的结果：一项 2026 年 Codex 实验中，使用 `AGENTS.md` 后平均墙钟时间从约 163 秒下降至约 130 秒、输出 token 下降约 20%；不过该研究明确没有评估语义正确性。因此现阶段更准确的判断是：**好的 context asset 能减少搜索、解释和重复沟通开销，但“提高正确率”没有普遍成立的结论。** citeturn4view0turn12view0

**【厂商文档】主流 coding agent 已把“长期配置”当作第一等能力。** OpenAI 当前 Codex 指南明确建议：把经常重复的规则放入 `AGENTS.md`，使用 `~/.codex/AGENTS.md` 保存个人全局默认、仓库级文件保存团队规范、目录级文件保存局部规则；并特别建议只有在看到“重复错误”以后才增加新规则。指南还把构建、测试、lint、完成条件、约束等列为适合持久化的项目上下文。citeturn16view0 GitHub Copilot 则同时支持 personal、repository-wide、path-specific、organization 和 agent instructions，其中部分 IDE 的个人 customization 明确可以“跟随用户跨项目”。citeturn19view4 Anthropic Claude Code 同样提供 `CLAUDE.md` 和自动 memory，并允许用户直接要求“始终使用 pnpm”“API 测试需要本地 Redis”之类的信息被记录。citeturn16view1

**【论文实证】prompt 已进一步从“文件”演化为“可调用的软件资产”。** 2026 年 Agent Skills 研究采集了 18,463 个 registry skill 和来自 5,876 个 GitHub 仓库的 **23,199 个 personal-use skills**，识别出 3,709 条复用关系。这类资产不仅包含自然语言提示，还可包含环境设置、工具/脚本使用方式、代码和配置、模板、验证步骤、失败处理与约束，已经非常接近用户设想的“开发知识资产包”。但复用大多仍是一次性复制，53% 的被复用 skill 采用后从未修改，后续修改又主要是增量追加，生命周期管理明显弱于传统 package dependency。citeturn18view2

**成熟度判断：** ADR、可执行测试、版本控制和声明式环境属于**成熟基础设施**；agent instructions/context files 属于**已进入实际生产使用、但效果依赖质量的成长期实践**；skills/程序化 workflow 属于**正在快速标准化的可复用资产层**；而“长期自动归纳、跨项目自动晋升、自动淘汰过时经验”的 personal knowledge system 仍是**研究前沿**。一项 2026 年 `PROJECTMEM` 工作甚至把 issue、attempt、fix、decision、note 建成 append-only event log，再产生 AI-readable projection 和失败前预警，但其真实使用验证仅是 207 个事件、10 个项目的作者自我研究，不能视作成熟行业证据。citeturn16view5turn15view2

## 从项目历史提炼可复用资产

**Q2 · AI 从既有项目、提交历史、需求记录中寻找复用线索的工具与实证**

这里需要区分三个不同难度的问题：**从历史找相关经验**已经有很强先例；**从仓库中发现现成 API/代码模式并复用**已有大量研究；但**从多个项目的需求历史中自动判断“这几次需求其实应该抽成一个个人公共库”**，本次研究没有找到已经得到可靠实证验证的直接先例。

**【论文实证】“提交历史 + issue = repository memory”已经被直接验证。** *Improving Code Localization with Repository Memory* 不再把每个新问题当作从零开始，而是建立两种长期记忆：一是最近 commit、commit message、patch 和 linked issues 组成的 episodic memory；二是通过修改频率选择活跃文件，并由 LLM 生成模块功能摘要形成 semantic memory。Agent 可以从当前 bug report 检索相似历史 commit，再读取当时的 issue 和补丁。研究报告称，该 memory augmentation 在 SWE-bench Verified 与更新的 SWE-bench Live 上都改善了 LocAgent 的定位表现。citeturn15view1

这与用户设想中的“从过去项目记录找线索”非常接近：这里的历史记录不是聊天日志，而是**问题描述 → commit → patch**形成的可验证链。它表明历史开发记录确实能成为 agent 的“案例记忆”，而不是只能把整个 Git 历史塞入上下文。citeturn15view1

*Code Researcher* 又证明，agent 可以跨大型代码库和庞大提交历史执行多步检索和推理。在 Linux kernel crash benchmark 上，它同时研究代码语义、模式和 commit history；以 GPT‑4o 为底座时 crash-resolution rate 为 48%，而论文报告的 SWE-agent 与 Agentless 对照约为 31%，增加采样预算后达到 54%。这证明“历史 mining 由 agent 自主执行”已经具有相当实证基础，但目标仍是解决当前故障，而不是自动产出通用库。citeturn13view0

HAFixAgent 则将 blame-derived repository history 引入自动程序修复。在 854 个 Defects4J 和 501 个 BugsInPy bug 的实验中，历史上下文在两套 benchmark 上继续提高修复效果，作者尤其观察到它对复杂多位置修改和故障定位噪声有帮助。也就是说，“曾经怎样改过这里”已经是可用的修复资产。citeturn13view1

**【论文实证】仓库内“发现可复用函数/模式”也已经有直接研究。** 2026 年 TICoder 从自然语言需求和测试出发，先生成实现计划，然后联合考虑函数功能与实现相似性寻找潜在 callee，再从仓库已有调用点中抽取 usage patterns；在 CoderEval 和 DevEval 上，论文报告相对最佳基线平均最高约 11.52% 的改善。更重要的是，论文同时指出：**单纯拿“语义相似代码”做复用并不可靠，甚至可能损害生成结果，因为仓库里不一定存在真正适配该需求的对应实现。** citeturn13view2

这给“自用代码库”一个重要边界：AI 已经能发现“本仓库里哪些函数和调用模式值得当前任务复用”，但**发现相似性与证明可抽象为跨项目公共组件是两个不同问题**。后者还必须解决隐含状态、依赖、生命周期、配置、许可证、测试语义和调用约定等迁移条件。跨仓库 redesign 的 2026 年实证研究同样发现代码和测试确实能迁移，但研究过程中也报告了四个 bug，并需要 backport/forward-port fixes 与 tests，说明移植仍然是一项工程活动，而非机械复制。citeturn14search20

Agentic Repository Mining 的研究则从另一方向确认了 mining 能力：在 commit、review、code line、repository 等四类任务、4,943 次分类上，让 LLM agent 自己通过 shell 动态探索 repository，可以达到与预先人工准备上下文的方法竞争的准确率，而且更不容易因为 artifact 太大而撑爆 context window。citeturn13view3

**“从需求记录找复用线索”的最近邻先例存在，但直接证据仍不足。** TICoder 和类似方法把自然语言 requirement 分解成 implementation steps，再寻找仓库可复用 API；Repository Memory 将历史 issue 与对应 commit/patch 建立可检索联系；Agent Skills 则证明开发者会把反复使用的流程和知识包装为独立资产。三者加起来已经覆盖“需求 → 历史案例 → 代码/流程资产”的大部分组成环节。citeturn13view2turn15view1turn18view2

**UNKNOWN：**在本次针对 2024–2026 一手公开材料的检索中，没有找到一个具有较强实证评估的系统，能持续读取**多个独立项目的需求/方案历史**，自动发现“这些需求重复出现”，进一步判断抽象边界，抽取为个人公共库/脚手架，并在未来项目中可靠选择和迁移它。因此，“跨项目需求历史 → 自动资产候选发现”可以视为有明确技术邻近项、但尚无成熟证据闭环的研究问题，而不能写成已有成熟最佳实践。citeturn15view1turn13view2turn18view2

## 环境与偏好的记录复用

**Q3 · 开发环境配置和个人习惯能否被 agent 记录并跨项目复用**

**结论：环境配置本身已经“现在可行且成熟”；个人偏好持久化也已产品化，但两者的可靠性层级不同。** 环境最好依赖机器可执行、可验证的声明式配置；偏好可以进入 agent memory/instruction，但这种自然语言记忆仍属于“提示”，不能被当作强制约束。citeturn16view3turn16view0turn16view1

**【厂商文档】环境资产化已经是传统 DevEx 能力。** Development Containers 规范和 GitHub Codespaces/VS Code 的 dev-container 体系可以把工具、runtime、扩展、端口和环境初始化跟仓库一起定义；GitHub Codespaces 又允许用户选定个人 dotfiles repository，新建 codespace 时自动 clone 并运行安装脚本，或者把 dotfiles 链接到 `$HOME`。因此“项目级工具链配置”和“用户级 shell/editor/tool preference”早已能够分别版本化和跨新环境恢复。citeturn16view2turn16view3

**【论文实证】2026 年甚至已经出现专门让 coding agent 把“环境调试经验”提炼成复用知识的工作。** BootstrapAgent 把首次启动陌生 repository 时试错得到的 dependencies、diagnostics、repair strategy 等提炼成可持久化、可验证的 `.bootstrap` contract，并用 Docker clean replay 验证。论文在三个 benchmark 上报告 92.9% bootstrap 成功率，相对基线提高超过 10%，下游 agent token 使用下降 25.9%，build time 下降 22.3%。这与“不要让下一个 agent 再重新踩一遍环境坑”高度吻合。citeturn16view6

**【厂商文档】个人 AI 工作偏好也已经有跨 session/跨 project 的明确载体。** Codex 支持 `~/.codex/AGENTS.md` 作为个人全局默认，并以 `~/.codex/config.toml` 保存模型、reasoning、sandbox、MCP、multi-agent 等持久设置；repo 可以再覆盖项目特定配置。citeturn16view0 GitHub Copilot 当前同时提供 personal instructions 和 repo instructions；JetBrains 的 personal customization 明确跟随用户跨项目，Copilot CLI 也有用户目录下的 personal instructions。citeturn19view4

Claude Code 则展示了更接近“agent 自己记住”的形式：用户可要求它记住“始终使用 pnpm”或“API 测试需要本地 Redis”，自动 memory 以 Markdown 保存，可由用户查看、修改和删除；不过它的自动 memory 本身按 project 存放，更适合作为项目经验，而全局 `CLAUDE.md` 等显式指令更适合真正的跨项目偏好。citeturn16view1

这里必须保留一个可靠性边界。Anthropic 自己明确说明 `CLAUDE.md` 是被模型读取并“尝试遵守”的上下文，不保证严格执行；对于模糊或互相冲突的指令尤其如此。必须执行的规则应改成 hook 等确定性机制。它同时提醒，过大的 instruction file 会消耗上下文并降低遵循表现。citeturn16view1

因此，可以把两层资产区别理解为：

| 对象 | 当前最成熟的载体 | 可靠性 |
|---|---|---|
| 编译器/runtime/package/toolchain | devcontainer、Docker/Nix 类声明、锁文件 | 高，可机器验证 citeturn16view2turn16view6 |
| shell/editor/CLI 个人环境 | dotfiles、安装 manifest | 高到中，可重放但有平台差异 citeturn16view3 |
| agent 工具与权限配置 | Codex/Claude/Copilot 的用户配置 | 中高，产品化配置 citeturn16view0turn19view4 |
| “我偏好怎样写代码/怎样工作” | global instructions、memory、skills | 中，属于上下文而非强制 invariant citeturn16view1turn18view1 |
| 必须遵守的禁令/验证规则 | tests、hooks、lint、CI、可执行 guardrails | 高于自然语言 instruction citeturn17view3turn18view1 |

**UNKNOWN：**现有产品已经能“保存显式偏好”，但本次没有找到充分证据证明 coding agent 能长期、自动、无监督地从用户行为中正确区分“永久个人偏好”“某项目临时约束”和“只对当前任务成立的选择”，再可靠提升到全局层。这个 promotion 问题应与“能不能把一条偏好写进文件”分开看。citeturn16view1turn19view4

## 缺陷与偏差资产化

**Q4 · bug、修复和“AI 输出不符预期”能否转化成回归测试、规则与检查清单**

这一环节是整个设想中证据最强的部分之一，因为它不是从零建立新范式，而是把软件工程原有的 **bug → reproducer → fix → regression test** 和 AI 工程新出现的 **trace → feedback → eval → harness change** 两条闭环合并起来。citeturn17view2turn17view1

**【厂商文档】bug → regression test 已进入 agent 产品工作流。** OpenAI Codex Security 当前文档要求，对已确认 finding，在安全且可行时创建一个“修复前失败、修复后通过”的聚焦回归测试，并重新验证正常行为；无法安全构造测试时，则显式记录 proof gap 和最强可重复验证证据。这正是把“故障历史”转成机器可执行资产，而不是只保留一段文字说明。citeturn17view2

Codex 的一般最佳实践同样要求 agent 写/更新测试、运行相应 suite、lint/type checking、确认最终行为满足原需求，并允许把 code-review rules 做成长期文件。更直接地，它建议当 Codex “同一个错误出现两次”时做 retrospective，然后更新 `AGENTS.md`。这已经形成了“偏差 → 复盘 → 持久规则”的厂商级实践。citeturn16view0

**【厂商文档】“AI 输出不符预期”也可以被转成 eval。** OpenAI 2026 年的 Agent Improvement Loop 从真实 traces 出发，加入 human/model feedback，然后把反馈转换成可以反复执行的 eval，最后据此修改 agent harness。文档明确把这一闭环描述为：trace 保存发生过什么，feedback 表示哪里重要，eval 将期待结果变成可复用判断标准。虽然示例不是 coding agent 专属，但机制正好对应“把用户纠正 AI 的历史变成下一轮自动回归”。citeturn17view1

**【论文实证】自然语言规则正在被进一步编译成机器检查。** ContextCov 研究针对 `AGENTS.md` 等 agent instructions，把其中约束转换成静态 AST checks、拦截 shell command 的 runtime shim、架构 validator 等 executable guardrails；研究在 723 个开源仓库中抽取了超过 46,000 个 executable checks，并报告 99.997% 的语法有效率。论文的核心论点是：只把要求写在自然语言里会出现 Context Drift，因此 agent instruction 应尽可能转成可验证 invariant。citeturn18view1

Claude Code 的 hook 机制已经提供产品级的相邻实现：例如 TaskCompleted hook 可在任务被标记完成前执行测试/lint 等完成条件，并以确定性结果阻断完成。Anthropic 同样明确建议，对“必须在固定生命周期节点执行”的要求用 hook，而不是依赖模型是否记得遵守 Markdown 指令。citeturn17view3turn16view1

**【论文/原型实证】失败历史本身也开始成为 agent memory 的结构化对象。** `PROJECTMEM` 直接记录 `issue / attempt / fix / decision / note` append-only events，并根据过去失败形成 pre-action warning：在 agent 重复一个已失败修复或碰触 known-fragile file 前提醒它。其本质上已经是“bug/错误尝试不是聊天残骸，而是治理资产”。不过其 207-event、10-project self-study 证据规模仍小，因此应看作很贴合本题的原型，而不是成熟标准。citeturn15view2turn16view5

最重要的实践分界因此不是“记不记录错误”，而是**错误记录最终属于哪一层**：能精确复现的行为错误最适合成为 test；静态编码约束适合 lint/check；工作流违规适合 hook/CI；难以机器表达但反复发生的行为偏差适合 concise instruction/checklist；纯粹的 agent 判断质量问题则更适合 eval。现有证据总体支持这种从“文字记忆”向“可执行资产”晋升的方向。citeturn17view2turn18view1turn17view1

## 个人级自用库公开案例

**Q5 · 个人开发者长期沉淀库、模板、脚手架，并由 AI 辅助维护/调用的公开实践**

这里已经有公开案例，而且到 2026 年数量足以形成实证研究；但“长期”必须谨慎定义。Agent Skills 作为流行的标准化形态非常年轻，所以现在能证明的是**个人级资产化已经真实发生并规模化**，不能证明这些库已经经历五年、十年式生命周期。citeturn18view2

**【论文实证】最强证据不是单个明星仓库，而是 5,876 个 personal-use repositories。** 2026 年 *From Registry to Repository* 直接区分 registry skills 与个人仓库内 skills，并找到 23,199 个 personal-use skills。这表明“个人维护一套 AI 可调用开发知识/流程”已经不是个别 anecdote。技能内容中可包含 workflow、environment setup、tool/script usage、templates、verification、failure handling、constraints 和 domain knowledge，覆盖范围与用户设想中的“自用代码库 + 开发知识资产”高度重合。citeturn18view2

**【社区经验】`zircote/.claude` 是非常直接的公开例子。** 仓库自述为个人 Claude Code 配置，包含 100+ domain-specific agents、60+ reusable skills、custom commands 和多语言 coding standards；安装到 `~/.claude/` 后由全局 `CLAUDE.md`、agents 和 skills 共同参与日常开发。这不是论文实验，却说明“个人 AI 开发平台配置作为 dotfiles 管理”已经实际存在。citeturn19view0

**【社区经验】`cassiewallace/dotfiles` 更清晰地把传统 dotfiles 与 AI assets 合并。** 作者称该仓库是其 “AI-era dev environment” 的 source of truth，其中同时存在 shell 配置、全局 Claude instructions、用于限制 Apple 平台工具调用的 hook、自写 Agent Skills，以及外部 Skills manifest。值得注意的是，作者刻意不 vendoring 外部 registry skills，而只记录安装 manifest，以避免本地副本与 upstream 漂移；这是一个很具体的“个人知识资产也需要 dependency/update policy”的经验。citeturn19view1

**【社区经验】`madflojo/dotfiles` 则明确把 Agent Skills 当作个人 workflow library。** 其仓库把 Vim/tmux 等传统配置与 PR、commit、review、repo discovery 等 reusable skills 放在一起，并有独立的 `AGENTS.md` 与 skills knowledge/action 目录。这里的资产重点不是代码函数，而是“怎样完成一类工程任务”，显示个人库正在从 dotfiles 扩展为 procedural knowledge library。citeturn19view2

传统“脚手架库”的研究也提供了补充背景。2026 年针对 GitHub template repositories 的大规模实证研究确认 template repo 是成熟的项目初始化复用机制，但发现不同生态的维护与质量差异很大；研究特别把“未经适配直接把普通仓库当模板”“维护状态不清”“模板与技术版本耦合不清”列为 pitfalls。也就是说，AI 即使能自动创建/调用模板，模板生命周期本身的传统问题仍然存在。citeturn18view3

个人资产化还有现实的工具兼容性成本。2026 年 3 月 Anthropic Claude Code 的公开 issue 就记录了一个典型问题：用户把 `~/.claude/skills` symlink 到 dotfiles repository 后，一次版本变化导致 user-level skills 无法被发现；issue 作者明确称这种 symlink 是常见 dotfiles 管理模式。它说明“个人 AI 库已经像 dotfiles 一样使用”，也说明 agent 生态的 discovery/packaging 接口目前还没有传统 package manager 那样稳定。citeturn19view3

**经验教训可以明确归纳为：个人资产库已经可行，但应把它当软件维护，而不是把聊天摘抄放进一个目录。** 2026 年 Agent Skills 生命周期研究发现，复用主要是一次性 copy，53% 被复用后的 skills 从未修改；而另一项对 138,133 个公开 `SKILL.md` 的质量研究发现 **91.8% 至少存在一个检测到的可复用性缺陷**，主要问题是 routing metadata 弱、内容臃肿/不可执行、资源组织差以及 portability 问题。citeturn18view2turn15view3

**UNKNOWN：**目前尚没有足够纵向证据说明“个人 AI skills/dotfiles/knowledge library”经过多年代码、框架、agent 平台迁移之后，其维护成本、淘汰率和净生产率收益是多少。现有公开案例证明“有人这样做、可以这样做”，但不能证明某一种组织方式已经成为长期最优实践。citeturn18view2turn15view3

## 主要失败模式与对策

**Q6 · 知识库腐化、过期方案复用、上下文错配、错误移植等失败类型**

现有材料中，最大的共识不是“agent 缺知识”，而是**错误知识、过多知识、错作用域知识以及没有验证的复用有时比缺知识更危险。**

| 失败类型 | 已观察证据 | 对策所指向的工程机制 |
|---|---|---|
| **知识/规格陈旧** | Codified Context 的单开发者案例中，spec staleness 被报告为主要失败模式；至少两次过时文档让 agent 生成与近期 refactor 冲突的代码，错误直到测试才暴露。citeturn13view4turn13view5 | 文档与代码 co-change；last-verified/status；drift detection；测试 |
| **上下文膨胀** | AGENTS/CLAUDE 配置研究中 Context Bloat 达 42%，并与冲突指令共同出现；Anthropic 也提醒过大的 context file 会降低遵循表现。citeturn19view6turn16view1 | 最小热上下文；按需加载；把 lint 能检查的内容移出 prompt |
| **冲突或错作用域指令** | Claude 官方说明不同 CLAUDE files 对同一行为有冲突时模型可能任意选择；ContextCov 同样把 conflicting input、legacy code patterns、context overload 列为 drift 原因。citeturn16view1turn18view1 | 明确 global/repo/path scope；优先级；机器 guardrail |
| **技能不可发现/不可移植** | 138,133 skills 中 91.8% 至少有一个检测到的 reusability defect；routing、portability、resource organization 是核心问题。citeturn15view3 | metadata lint；小而聚焦的 skill；测试安装/路由 |
| **复制后冻结、与上游漂移** | skill 复用主要是 copy，53% 采用后从未再改，后续演化又高度 additive。citeturn18view2 | provenance/upstream link；版本/更新策略；定期验证 |
| **相似代码误移植** | TICoder 明确指出，相似代码检索不保证存在真正适配当前 requirement 的实现，错误检索可能降低生成质量。citeturn13view2 | 同时验证行为、调用模式与 tests，而非只看 embedding similarity |
| **过期需求触发错误行动** | FixedBench 用 200 个“已经无需改代码”的 stale tasks 测试 agent；五种模型/四种 harness 仍在 35%–65% 情况下提出不必要代码修改。citeturn17view5 | patch 前先 reproduce/检查当前状态；允许明确 abstain |
| **AI 偏离用户意图** | 对 20,574 个真实 coding-agent sessions 的研究识别出 constraint violation、misread intent、faulty implementation、wrong diagnosis、overreach 等七类偏差；90.50% 主要造成 effort/trust cost，而可见解决案例中 91.49% 仍需用户明确纠正。citeturn18view0 | 保存反馈；把重复偏差提升为 eval/test/rule，而非期待 agent “自己记住” |
| **自然语言规则不可执行** | ContextCov 指出即使规则写得足够清楚，conflicting context、能力限制和代码库旧模式仍会造成违反。citeturn18view1 | 可检查的规则编译为 lint/hook/test/architecture check |

**【论文实证】最具体的“知识腐化”案例来自 Codified Context。** 该项目用 hot-memory constitution + 34 个按需 specs 管理约 108k 行 C# 系统，在 283 个开发 session 中进行观察。作者报告过时 specs 曾让 agent 沿已经废弃的 stat path 写代码；其解决方案之一是从 recent Git commits 检查源文件是否发生变化、而对应 spec 未变化，进而在 session start 注入 drift warning。但论文同时明确承认，这是单开发者、单项目、观察性研究，不能量化为普遍生产率收益。citeturn13view4turn13view6

这类结果对“长期知识资产”特别关键，因为知识库的危险并不主要来自“旧记录还在那里”，而来自**旧记录没有时间、作用域和验证状态，却仍然被当成当前真相检索出来**。ADR 的成熟做法值得借鉴：accepted decision 不回写历史，而是新建 superseding record 并链接旧决策，从而保留“当时为什么这样做”与“现在已经不用了”两个事实。citeturn17view0

**“更多上下文”也不是普遍对策。** AGENTbench 发现自动生成的 context file 可能降低成功率并增加成本；配置 smell 研究则观察到大范围的 bloat/conflict；Agent Skills 生态研究也发现大量不可执行或包装质量低的内容。这些结果共同支持一种更保守的理解：**长期资产库可以大，但每个任务实际加载到模型里的上下文应小、相关、有作用域，并尽可能有验证依据。** citeturn12view0turn19view6turn15view3

最后，现有数据还表明“agent 总会尝试做点什么”本身就是失败模式。FixedBench 专门构造无需代码变更的 stale bug reports，当前强模型仍大量产生不必要修改；仅仅添加“先复现”指令虽能改善一部分问题，却又可能在“问题只修了一半”的情况下造成过度 abstain。因此，历史知识检索之后仍需要**当前状态验证**，不能把历史 ticket、旧 patch 或旧方案直接当成当前事实。citeturn17view5

## 可行性三档判定

**Q7 · 六类记录对象逐项判定**

本题最好把“**记录/检索**”与“**自动抽象/自动采用**”分开。前五类在记录和受控复用层面已经有足够技术与实践证据；最薄弱的是最后一步——让 AI 从多项目需求历史里自动判断何时应该产生一个新的、真正通用且长期可维护的共享资产。

| 记录对象 | 判定 | 依据与边界 |
|---|---|---|
| **需求** | **【现在可行】** | Issue/spec/acceptance criteria 本来就可版本化；Repository Memory 已能把 linked issues 与 commit/patch 做长期 episodic memory，PROJECTMEM 也直接把 issue 作为 typed event。关键是保留状态与当前验证，避免 stale issue 被 agent 当作待修事实。citeturn15view1turn15view2turn17view5 |
| **AI 给出的方案：设计/实现/测试** | **【现在可行】** | ADR 已提供 context/options/decision/trade-off/supersede 的成熟历史模型；agent context、plans 和 event logs 均可保存方案。但“保存过”不能等于“仍有效”，必须能表达 superseded/failed/verified。citeturn17view0turn16view0turn15view2 |
| **系统环境与工具配置** | **【现在可行】** | devcontainer/dotfiles 等已成熟；BootstrapAgent 进一步直接证明 agent 可以把 repository bootstrap 试错提炼成可验证、可复用 startup contract。citeturn16view2turn16view3turn16view6 |
| **用户环境与工作偏好** | **【现在可行】** | Codex global `AGENTS.md`/config、Copilot personal instructions、Claude memory/global instructions 均已产品化。限制是自然语言 preference 属于 soft guidance，不保证遵循；强制项应进入 hook/test/config。citeturn16view0turn19view4turn16view1 |
| **bug 与“AI 不符预期”偏差** | **【现在可行】** | bug 可提升为 reproducer/regression test；agent feedback 可提升为 eval；重复 workflow mistake 可变成 instruction/hook/check。PROJECTMEM 和 ContextCov 又分别展示 failure memory 与 instruction→executable check。citeturn17view2turn17view1turn18view1turn15view2 |
| **跨项目复用线索** | **【需研究】** | Commit/issue memory、repo mining、实现感知 code reuse、skills 和 templates 都证明各子问题可做；但未找到强实证证明 agent 能可靠从多个项目需求历史自动识别抽象边界、生成公共库并决定未来采用。错误相似性和上下文错配已有明确反例。citeturn15view1turn13view2turn18view2 |

**没有一类记录对象在“把它保存为公开可审查的工程制品”这个意义上属于【当前不可行】。** 真正尚不能视为“现在可行”的，是更强的版本：**无人审核的 agent 自动从长期历史中决定什么应被永久记住、什么应升级成全局规则、什么应抽成跨项目公共代码、何时废弃旧资产，并安全地在新项目里自动移植。** 目前关于 context drift、stale tasks、skill defects、错误 code retrieval 和真实 developer-agent misalignment 的数据都不支持把这一级自动化当成已解决问题。citeturn13view5turn17view5turn15view3turn18view0

**最小可行起步形态。** 从现有证据看，风险最低的起点不是先建立一个“大而全的 AI 知识库”，而是让已经自然产生的工程制品成为记忆：项目内保留可版本化的需求/验收条件、append-only 或可 supersede 的决策记录、短而准确的 agent instructions、环境声明以及 bug regression tests；个人层保留显式的 dotfiles/tool config/global agent preferences，并把真正重复的 procedure 封装为 skill。AI 可以负责检索、总结、提出“疑似可复用候选”，但**跨项目公共代码/全局规则的 promotion 暂时保留人工确认和测试验证**；已经能被测试、lint、hook、CI 或 eval 表达的经验，优先晋升为这些可执行资产，而不是继续堆在提示词里。这个形态分别利用了 ADR 的历史性、devcontainer/dotfiles 的可重放性、Repository Memory 的案例检索、Skills 的按需复用以及 regression/eval 的机器验证，同时避开当前证据最明确的 context bloat、staleness 和错误自动移植风险。citeturn17view0turn16view3turn15view1turn18view2turn17view1turn19view6

总体判定可以概括为：**“长期开发知识资产”本身现在可行；“AI 帮助采集、检索、归纳和调用”也已大部分可行；“AI 自主决定跨项目抽象并持续自治维护个人代码库”仍需研究。** 最值得利用的不是模型的“记忆感”，而是把经验变成有 provenance、scope、status 和 executable verification 的软件工程制品。citeturn15view2turn18view1turn17view0

## 来源表

下表只列本报告实际依赖的主要公开一手来源。论文预印本与厂商产品文档分开标记；GitHub 个人仓库/issue 标为社区经验。厂商文档若页面没有稳定发布日期，以 **2026-08-31 访问**标示现行状态。

| 类型 | 来源 | 日期 | 本报告主要用途 |
|---|---|---:|---|
| **论文实证** | *Agent READMEs: An Empirical Study of Context Files for Agentic Coding* | 2025-11 | 2,303 context files；内容构成、维护模式和 NFR 缺口。citeturn19view5turn4view1 |
| **论文实证** | *Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?* | 2026-02-12 | developer-written context 小幅增益、自动生成 context 负效应及成本增长。citeturn12view0 |
| **论文实证** | *On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents* | 2026-03-30 版本 | AGENTS.md 对运行时间/output tokens 的效率结果；未验证语义正确率。citeturn4view0 |
| **论文实证** | *Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories* | 2026-07-28 | 288-run 消融研究；未检测到显著 correctness 改善。citeturn12view2 |
| **论文实证** | *Configuration Smells in AGENTS.md Files* | 2026-06 | Lint Leakage、Context Bloat、Skill Leakage、冲突等 context maintenance failures。citeturn19view6 |
| **论文实证** | *From Registry to Repository: How AI Agent Skills Are Written, Adapted, and Maintained* | 2026-07-06 | 18,463 registry skills、23,199 personal-use skills、3,709 reuse links；53% adoption 后未修改。citeturn18view2 |
| **论文实证** | *What Keeps Agent Skills from Being Reusable? Evidence from 138K SKILL.md Files* | 2026-08-09 | 138,133 skills；91.8% 至少有一个检测到的复用缺陷。citeturn15view3 |
| **论文实证** | *Improving Code Localization with Repository Memory* | 2025；2026 版本 | commit + linked issue episodic memory、活跃模块 semantic memory。citeturn15view1 |
| **论文实证** | *Code Researcher: Deep Research Agent for Large Systems Code and Commit History* | 2025-05-27；2026-05-20 v2 | 多步研究大型代码和 commit history；crash repair 实证。citeturn13view0 |
| **论文实证** | *HAFixAgent: History-Aware Program Repair Agent* | 2025–2026 | repository history 用于 agentic bug repair。citeturn13view1 |
| **论文实证** | *TICoder: Repository-Level Code Generation with Test-Driven Planning and Implementation-Aware Reuse* | 2026-06 | requirement/test 驱动的仓库代码复用；错误相似性检索风险。citeturn13view2 |
| **论文实证** | *Agentic Repository Mining: A Multi-Task Evaluation* | 2026-05 | agent 自主探索 repository 执行 MSR 分类任务。citeturn13view3 |
| **论文实证** | *BootstrapAgent: Distilling Repository Setup into Reusable Agent Knowledge* | 2026-05-15 | 将环境 bootstrap 试错蒸馏成 `.bootstrap` 可验证资产。citeturn16view6 |
| **论文/原型实证** | *PROJECTMEM: A Local-First, Event-Sourced Memory and Judgment Layer for AI Coding Agents* | 2026-06-10 | issue/attempt/fix/decision/note append-only memory、失败预警；小规模 self-study。citeturn16view5turn15view2 |
| **论文/观察性案例** | *Codified Context: Infrastructure for AI Agents in a Complex Codebase* | 2026-02 | stale specification 的实测失败、context drift detector；单开发者项目局限。citeturn13view4turn13view6 |
| **论文实证** | *ContextCov: Deriving and Enforcing Executable Constraints from Agent Instruction Files* | 2026-02-28 | agent instruction → executable checks；Context Drift。citeturn18view1 |
| **论文实证** | *How Coding Agents Fail Their Users: A Large-Scale Analysis…* | 2026-05-28 | 20,574 个真实 sessions 的开发者—agent misalignment。citeturn18view0 |
| **论文实证** | *Coding Agents Don’t Know When to Act* | 2026-05 | stale bug report、action bias、35%–65% 不必要修改。citeturn17view5 |
| **论文实证** | *GitHub Template Repositories: Served Domains, Maintenance, and Practitioner Guidelines* | 2026-06-12 | template/scaffold 复用、维护差异与错误移植 pitfalls。citeturn18view3 |
| **厂商文档** | Microsoft Azure Well-Architected — *Maintain an architecture decision record* | 2026-04-13 | ADR context/options/decision、append-only 与 supersede。citeturn17view0 |
| **厂商文档** | OpenAI Codex — *Best practices* | 2026-08-31 访问 | global/repo `AGENTS.md`、配置、测试/review、从重复错误更新规则。citeturn16view0 |
| **厂商文档** | OpenAI — *Build an Agent Improvement Loop with Traces, Evals, and Codex* | 2026-05-12 | trace + feedback → eval → harness change。citeturn17view1 |
| **厂商文档** | OpenAI Codex Security — *Fix and verify security findings* | 2026-08-31 访问 | bug/finding → 修复前失败、修复后通过的 regression test。citeturn17view2 |
| **厂商文档** | Anthropic Claude Code — Memory / CLAUDE.md | 2026-08-31 访问 | 自动 memory、显式 preference、context size 与遵循局限。citeturn16view1 |
| **厂商文档** | Anthropic Claude Code — Hooks reference | 2026-08-31 访问 | 确定性 lifecycle checks、测试/lint 完成门。citeturn17view3 |
| **厂商文档** | GitHub Copilot — Custom instructions support | 2026-08-31 访问 | personal/repository/path/org instructions；跨项目个人 customization。citeturn19view4 |
| **厂商文档** | GitHub Codespaces — Personalizing Codespaces with dotfiles | 2026-08-31 访问 | 个人环境配置在新 codespace 自动恢复。citeturn16view3 |
| **标准/厂商生态文档** | Development Container Specification | 2026-08-31 访问 | 声明式、可重建开发环境。citeturn16view2 |
| **社区经验** | `zircote/.claude` | 2026-08-31 访问 | 个人 Claude 配置、100+ agents、60+ reusable skills。citeturn19view0 |
| **社区经验** | `cassiewallace/dotfiles` | 2026-08-31 访问 | dotfiles + global AI instructions + hooks + skill manifest；upstream drift 处理。citeturn19view1 |
| **社区经验** | `madflojo/dotfiles` | 2026-08-31 访问 | 传统 dotfiles 与 PR/review/commit/repo-discovery Agent Skills 合并。citeturn19view2 |
| **社区经验 / bug report** | Anthropic Claude Code issue #38051 | 2026-03-24 | dotfiles symlink 管理 user skills 的 discovery regression，体现 portability/tooling 风险。citeturn19view3 |