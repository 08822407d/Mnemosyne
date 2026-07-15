**Work package B：Mnemosyne provenance/no-write evidence pack。** 把本报告中的 provenance schema 与 no-write taxonomy 变成一份“可选附录模板”，并要求所有高风险 run 至少附带 surface、plan、memory mode、app list、repo auth scope、before/after refs 这些字段。此包应先在研究性文档中试运行，再决定是否升级到执行源。citeturn38view0turn38view1turn35view0turn35view6

**Work package C：artifact/handoff hygiene pack。** 把 Issue #170 与 #171 的候选框架沉淀为文件优先、正文摘要、分层 guidance 装载、低风险同回复生成边界。这个包最接近立刻可用，但仍建议先在维护对话中 review，而不是直接写规章。citeturn42view0turn8view0

**Work package D：Surface playbooks。** 为 Chat、Project Chat、Deep Research、Work、Codex、Agent 各写一版一页式 playbook，专门描述“适合做什么、不适合做什么、memory/authority 风险、需要的证据”。这样能把“surface 选择”从经验判断变成半结构化决策。citeturn13view0turn13view1turn9view2

仍须保留为 **unsupported assumptions / unresolved uncertainties** 的问题主要有六个：  
一，OpenAI 公开文档尚未给出足以做完整取证的 Compliance API 字段级 schema；  
二，GitHub connector 对 branch/ref enumeration 的完备性没有官方保证；  
三，GitHub app 在 Project Chat 中是否有独立 sync 行为，公开文档未明示；  
四，Library 自动引用与 project-only/Workspace policy 的精确交互没有完整矩阵；  
五，模型是否能可靠自知其当前 reasoning setting，公开文档未承诺；  
六，plan、workspace、region、surface rollout 都在变化，某些“今天可见/不可见”的事实仍需操作员记录 UI 观察而非从文档反推。citeturn9view8turn32view0turn11view2turn30view1turn38view1turn38view0

本报告也有明确 **limitations**。我没有在本次会话中对 ChatGPT UI 做登录态实操验证，也没有读取需要登录 Enterprise workspace 才能看到的 Compliance API 细节页面；因此，凡涉及确切日志字段、管理员后台具体 payload、或某个 plan 当下 rollout 状态的地方，我都只把公开帮助页可支持的部分记为 confirmed，其余保留为 unknown/live-test。GitHub 仓库部分以公开网页与 raw 文件为基线，不把任何“连接器当前看到了什么”当成完备覆盖证明。citeturn9view8turn35view0turn35view4

总体结论可以压缩成一句话：**2026Q3 最值得 Mnemosyne 接受的不是“更多平台内记忆”，而是“更明确的边界学”：把 project memory、platform memory、connected apps、GitHub auth、surface selection、provenance 与 no-write proof 全部拆开治理。** 这与仓库在 README 中坚持的“模型负责计算，文件负责记忆”并不冲突，反而要求把这句原则执行得更严格：**复杂知识交接靠文件与项目 sources，研究取证靠 Deep Research，代码改动留给 Codex，no-write 证明靠外部证据链，不靠模型自述。** citeturn41view2turn9view2turn13view0turn34search0turn35view6

**参考来源与来源清单**：  
OpenAI：Projects in ChatGPT；How memory works；Deep research in ChatGPT；Apps in ChatGPT；Apps with sync；Connecting GitHub to ChatGPT；Plugins in ChatGPT and Codex；Developer mode and MCP apps in ChatGPT；Admin controls, security, and compliance for plugins and apps；ChatGPT Work and Codex；ChatGPT agent；GPT-5.6 in ChatGPT；What to expect when models change；ChatGPT Business - Models & Limits；File storage and Library in ChatGPT；Temporary Chat FAQ；ChatGPT Enterprise & Edu - Release Notes。citeturn9view0turn9view1turn9view2turn15view0turn32view0turn9view4turn13view2turn15view1turn9view3turn13view0turn13view1turn38view1turn38view2turn38view0turn30view0turn36search0turn40search0

GitHub：Permissions required for GitHub Apps；Authorizing GitHub Apps；Installing a GitHub App from a third party；Access permissions on GitHub；REST API endpoints for branches；pull requests；commits；Using pagination in the REST API。citeturn35view2turn35view6turn35view3turn35view7turn35view1turn35view4turn35view5turn35view0

Anthropic / Google / Microsoft / Cursor / standards：Claude Projects；Claude chat search and memory；Claude Research；Claude connectors；Claude GitHub integration；Gemini Deep Research；Gems；Gemini personalization / Personal Intelligence；GitHub Copilot cloud agent；GitHub Copilot repository custom instructions；Cursor Rules；Cursor Cloud Agents；Cursor MCP；MCP specification；A2A；Anthropic context engineering。citeturn39view0turn39view1turn39view2turn39view3turn39view4turn39view5turn39view6turn39view7turn39view8turn39view9turn39view10turn24search0turn24search1turn24search2turn39view14turn39view15turn39view16

Mnemosyne 仓库基线：README；Issue #170；Issue #171。citeturn41view2turn42view0turn8view0

```yaml
deep_research_result_handoff:
  prompt_id: PROMPT-2026Q3-PLATFORM-DELTA-0001
  proposed_cycle_id: RC-2026Q3-platform-context-apps-delta
  report_title: 2026Q3 AI Agent 平台、项目记忆、Apps、GitHub 与工作模式能力增量研究
  execution_surface: chatgpt_deep_research_style_report_compiled_from_official_public_sources
  sources_used:
    - openai_help_center
    - openai_developers
    - github_docs
    - anthropic_official_docs
    - google_gemini_official_help
    - github_copilot_official_docs
    - cursor_official_docs
    - mcp_official_spec
    - mnemosyne_public_repository
  connected_apps_used:
    - none_in_this_chat_environment
  repository_paths_read:
