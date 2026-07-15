| 平台日志/Compliance + 外部观察者 + 签名证明 | 可把“该次 run 未通过该 surface/app 发生写动作”做成审计链 | 仍不是数学意义“系统宇宙中无写入” | 高 |

具体回答你提出的三个 proving questions：

其一，**证明“没有 default branch 写入”**，现实可行的强组合是：`default branch ref before/after snapshot` + 运行窗口内未见 merge/force-push/PR merge 事件 + 本次 surface/app 为只读或未触发写动作。对公开 GitHub 仓库，这已经是比较实用的强证明。citeturn35view1turn35view4turn35view6

其二，**证明“没有任何 branch/PR/object 写入”**，门槛高得多。单靠聊天表层几乎不够。你至少需要：读写权限姿态本身就是只读（例如 GitHub App 安装只授读权限，或使用 Deep Research 这类官方只读 app-action surface），再辅以尽可能完整的 remote refs、PR、event 快照。即便如此，“object 写入”仍然比“branch/PR 写入”更难完全排除，因为 GitHub surface 不会给你一个简单的“全对象无变化证明”。citeturn10view5turn35view2turn35view3turn35view0

其三，**哪些证据只能说明“没有检测到写入”**：本地 diff、只看 default branch、不追分页的 branch/PR API、只看 connector 搜索结果、只看 app call log 而不看 repo 事件，这些都只能给“未检测到”级别结论。GitHub 分页规则和 PR commit list cap 已经足以说明为什么。citeturn35view0turn35view4

所以，关于 **Mnemosyne §19 是否需要未来研究性修订**，我的候选建议是：**需要，但应修成“分层证明 taxonomy”，而不是一个单一的 no-write 断言。** 更准确的做法是把证据等级写成三层：  
**Level A**：未检测到 default-branch 写入；  
**Level B**：未检测到 branch/PR 写入；  
**Level C**：run 使用的平台/app 写权限本身就是只读。  
这样既不把 marketing claim 当 mechanical proof，也不把“未见异常”误写成“绝对无写”。这一修订方向是候选 guidance，不应在本报告中直接改执行源。citeturn41view2turn35view0turn35view6

**observer-assisted run** 的建议设计也可以明确写出来：运行前由外部观察者记录 repo 默认分支 ref、现存 branches、open PR 清单、GitHub App 权限姿态；运行中保存 surface、picker、app availability、approval 卡片、拒绝/批准记录；运行后再次抓取 remote refs/PR/events，并导出或保全 Compliance/app logs。如此一来，模型输出只是其中一环，真正的证据链来自 Git、GitHub、平台日志和观察者共同签名。这个思路与 GitHub App 权限模型、OpenAI Compliance 公开说明、以及当前 surface 分化是一致的。citeturn35view6turn10view7turn31view3

**RQ8 的 artifact 与 handoff 结论同样已经相当成熟。** Issue #170 记录的风险非常具体：超长 Markdown/YAML/code block 在聊天正文中直接铺开，会有结构损坏、复制丢格式、上下文膨胀、甚至浏览器 UI 性能问题。与此同时，Projects 支持把响应保存为 project source，Work 支持直接生成可下载文档/表格/演示，Deep Research 也支持 Markdown/Word/PDF 导出。也就是说，从产品能力和仓库问题记录两边看，**“长 transfer artifact 默认文件化交付”已经不是偏好问题，而是结构完整性和可审计性的风险控制措施。** citeturn42view0turn28view1turn10view5turn33search0

对 **HO-GUIDANCE-001、Issue #170、Issue #171**，我给出的候选处理框架是：

第一，**文件优先规则**：凡是满足“内容长、要跨对话复制、要给 Codex/外部工具用、需要保持 Markdown/YAML/code block 结构”的 artifact，一律优先文件交付；正文只放用途说明、关键摘要、文件名/下载位置信息。这与 Issue #170 完全一致。citeturn42view0

第二，**同回复直接生成低风险 artifact 的边界**：只有在内容短、结构简单、无需再机器消费、且不会成为后续执行源时，才适合直接在同一回复正文给出。比如几行 checklist、非结构化 summary、短说明性 YAML。长 replay prompt、handoff package、Codex task、研究计划书都不应默认走这种路径。citeturn42view0

第三，**业务对话 guidance 分层装载**：Issue #171 其实已经把问题定义得很清楚了——目标项目业务对话不应默认灌入完整版 Mnemosyne 指导，因为会引起 context pollution、authority conflict 与 token cost。更合理的默认做法是：  
- 在目标项目中只装载 **项目本地 guidance**；  
- 另附一份 **裁剪后的 Mnemosyne 通用 operator appendix**，只保留 provenance、artifact hygiene、no-write caution、handoff discipline 这类横向元规则；  
- **完整版 Mnemosyne 指导** 留在维护对话、研究对话或合规审查 surface 中。  
这正好对应 Issue #171 想要解决的三选一困境。citeturn8view0

## 跨平台对照、分阶段工作包、未决问题与参考来源

如果把 OpenAI 的变化放到更大的平台格局里看，主线并不混乱，反而更清楚了。**Anthropic** 现在把 Claude Projects 定义为“self-contained workspaces with their own chat histories and knowledge bases”，并且另行推出跨会话 chat search 与 memory，且搜索边界可限定为项目内；Research 提供 agentic multi-search 与 citations；connectors 则已经明确支持“retrieve your data and take actions”，并继续继承源系统权限。这意味着 Claude 走的是“项目工作区、跨聊天记忆、研究、连接器动作”并列演进的路线。对 Mnemosyne 可迁移的机制是：**把 project context、cross-chat memory、tool actions 分开治理**，而不是混成一个“大记忆”。citeturn39view0turn39view1turn39view2turn39view3turn39view4

**Google Gemini** 的路线也很相似，只是命名不同。Gems 本质是可复用的定制指令包；Deep Research 默认用 Google Search，也可以加 Gmail、Drive、上传文件与 NotebookLM notebook；personalization 明确由“past Gemini chats memory + connected apps + instructions”三部分构成，而且 Google 还提供对单个 chat 关闭 Personal Intelligence 的开关。对 Mnemosyne 的启发是：**“个性化上下文”必须允许会话级关闭**，而不是只能全局关。OpenAI 在 project-only 和 Temporary Chat 上给了一部分能力，但“是否有会话级 personalization kill switch”这一点，Google 的产品语义更直接。citeturn39view5turn39view6turn39view7turn39view8

**Microsoft / GitHub Copilot / VS Code agents** 与 **Cursor** 提供的启发则主要在仓库与编码工作流上。GitHub Copilot cloud agent 明确在 GitHub 上后台工作：研究仓库、制订计划、在 branch 上改代码、再由用户 review diff / create PR；GitHub 还支持 repository custom instructions。Cursor 则把 **rules、cloud agents、MCP** 做成显式对象。和 ChatGPT 相比，这些 coding-agent 产品有一个更适合 Mnemosyne 的优点：**它们更强调 repo-local instructions、branch/diff/PR 这些可机械观察对象，而不是依赖隐式跨聊天记忆。** 这也是 Mnemosyne 在执行层最该保留的设计方向。citeturn39view9turn39view10turn24search0turn24search1turn24search2

再往上看，**MCP 与 A2A** 的共同趋势也支持 Mnemosyne 的总体方向。MCP 官方规范把它定义为让 LLM 应用接入外部数据源与工具的开放协议；Google 的 A2A 则把重点放到 agent 之间安全交换信息和协同行动；Anthropic 把 context engineering 定义为组织与维护推理时“最佳 token 集”的方法论。综合起来，适合 Mnemosyne 的成熟机制不是“更强的隐藏记忆”，而是**更显式的 context engineering、外部状态、协议化工具边界与可回放的审计链**。citeturn39view14turn39view15turn39view16

基于以上事实，我建议把 Mnemosyne 后续工作拆成四个 **staged work packages**，全部都先作为候选工作包，不自动改执行源：

**Work package A：Project/Memory/GitHub live test pack。** 目标是把当前仍属未知的边界做成实验：旧 project 是否还能通过任何移动/分享路径接近 project-only；GitHub 在 Project Chat 中是否有 sync 语义还是仅 search/fetch；Library 自动引用与 project-only 的交互；同一 account 在 Chat / Project / Deep Research / Agent 中 GitHub availability 的实际差异。这里属于 `unknown_requires_live_test`。citeturn10view1turn30view0turn11view2

