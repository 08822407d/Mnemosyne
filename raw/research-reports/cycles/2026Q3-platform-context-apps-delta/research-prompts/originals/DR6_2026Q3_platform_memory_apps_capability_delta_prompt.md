# DR6 — 2026Q3 AI Agent 平台、项目记忆、Apps、GitHub 与工作模式能力增量研究

## 文件定位

```yaml
prompt_id: PROMPT-2026Q3-PLATFORM-DELTA-0001
proposed_cycle_id: RC-2026Q3-platform-context-apps-delta
prompt_type: ChatGPT_Deep_Research_prompt
artifact_role: external_research_input
repository_write_authorized: false
execution_source: false
```

本提示词用于启动一次新的 ChatGPT Deep Research。它是研究输入，不是研究结论，也不授权修改 Mnemosyne 仓库或执行源。

---

# Part A — 建议的手动设置

1. 新建一个独立的 Project，建议名称：
   `Mnemosyne Research 2026Q3 — Platform Delta`。
2. Memory 选择 `Project-only`。
3. Project instructions 留空。
4. 不移动旧 Mnemosyne 对话进入该 Project。
5. 在该 Project 的第一段研究对话中选择 **Deep research**。
6. 通过 `+` 选择 GitHub，并确认全局 GitHub 设置已允许访问：
   `08822407d/Mnemosyne`。
7. Deep Research 来源设置：
   - 允许公开 Web；
   - 允许已连接 GitHub app；
   - 优先官方产品文档、官方技术文档、原始研究论文和标准组织资料；
   - 不使用 GitHub 写操作。
8. 将 Part B 的完整提示词作为一条消息发送。
9. Deep Research 提交研究计划后，先检查计划是否覆盖全部研究问题，再批准执行。

---

# Part B — Deep Research 单条提示词

## BEGIN DEEP RESEARCH PROMPT

# 研究课题

请完成一份截至当前日期的系统性增量研究报告：

> **2026Q3 AI Agent 平台、项目记忆、连接 Apps、GitHub 集成、Deep Research、Chat/Work/Codex 工作模式，以及这些机制对 Mnemosyne 外部持久记忆系统、跨对话交接、Cleanroom 测试和可审计工作流的影响。**

这是一次 Mnemosyne research cycle 输入，不是仓库维护或执行源修改任务。

## 研究目标

Mnemosyne 当前研究证据主体形成于 2026Q2。近期实际使用暴露了多项平台变化和不确定性，包括：

- ChatGPT Project 的 Default memory 与 Project-only memory；
- 同一 Project 内跨对话上下文可见性；
- 全局 GitHub repository authorization 与单次对话中通过 `+` 调用 GitHub app 的关系；
- GitHub app 的搜索、同步、索引、文件读取、commit/PR/branch/ref 可见性；
- Deep Research、普通 Chat、ChatGPT Work、Codex 和 Agent mode 的职责与上下文边界；
- app read/write actions、approval、审计和权限配置；
- visible model label、reasoning setting、fallback、服务故障和 provenance 的可验证范围；
- 连接器返回空结果、索引延迟、数据新鲜度和 pagination/coverage 无法证明的问题；
- 长跨对话提示词应文件化，以及低风险 artifact 是否应在同一回复直接生成。

请研究当前平台事实，识别 2026Q2 证据中的 stale assumptions，并提出经过证据约束的 Mnemosyne 候选改进建议。

## 授权来源与仓库范围

通过已连接的 GitHub app，以只读方式检查仓库：

```text
08822407d/Mnemosyne
```

至少读取并使用以下仓库文件作为现状基线：

- `README.md`
- `current/human-approved-spec.md`
- `current/review-and-validation-status.md`
- `current/meta-agent-test-route-status.md`
- `current/handoff-guidance-open-question.md`
- `raw/research-reports/current/current-evidence-map.md`
- `raw/research-reports/current/current-capability-boundaries.md`
- `raw/research-reports/current/current-research-prompts.md`
- `notes/chatgpt-work-mode-assessment-2026-07.md`
- GitHub Issues #170 和 #171

这些文件只是执行源、当前状态、研究证据或问题记录。不得把研究报告、current view、issue 或本提示词当作执行源。

## 允许和禁止的动作

允许：

- 读取公开网页；
- 读取官方产品和技术文档；
- 读取原始论文、标准和可信技术资料；
- 通过 GitHub app 只读访问授权仓库；
- 比较不同平台、模式和权限模型；
- 生成带引用的完整报告。

禁止：

- 创建或修改 GitHub 文件、branch、commit、PR、issue、comment、review、label、reaction、release、workflow 或设置；
- 修改 `current/human-approved-spec.md`；
- 自动关闭任何 Mnemosyne issue 或 open question；
- 把研究建议描述为已批准规则；
- 访问或写入 Meta-Agent 目标仓库；
- 创建 target workspace、摄入目标材料或启动 build；
- 将平台营销声明未经核验地当作实际能力事实。

## 来源优先级

按以下优先级使用来源：

1. 官方产品文档、Help Center、API 文档、release notes、状态页；
2. GitHub、OpenAI、Anthropic、Google、Microsoft、Cursor 等供应商的官方技术文档；
3. 原始研究论文、标准组织、正式技术报告；
4. 高质量工程实践资料；
5. 二手新闻和社区观察，仅用于补充，不得覆盖官方或机械证据。

对于每项平台事实，记录：

- 来源；
- 页面最后更新时间或发布日期；
- 当前适用的 plan、surface、workspace、region 或角色限制；
- 是否为官方承诺、实际可验证行为、推断或未知。

## 核心研究问题

### RQ1 — ChatGPT Projects 和记忆隔离

研究：

- Default memory 与 Project-only memory 的精确定义；
- 旧 Project 是否能切换到 Project-only；
- 同一 Project 内多聊天能否相互引用；
- Project 外聊天、saved memory、custom instructions 的可见范围；
- Temporary Chat 与 Project 的关系；
- strict fresh-session / cleanroom test 的最低可靠配置；
- Project instructions、Project files、Library access 和 connected apps 的区别。

输出一个“上下文与隔离矩阵”。

### RQ2 — Apps / Plugins / MCP 的权限与调用模型

研究：

- 全局连接、workspace enablement、per-chat invocation、sync、indexing 和 action permission 的区别；
- `+` 菜单、`@App`、Plugin Directory、Projects 中 app invocation 的当前语义；
- read actions、write actions、approval cards、Always ask / Any changes / Important actions / Never ask；
- 个人账户与 Business/Enterprise/Edu 管理能力差异；
- app 调用日志、Compliance Logs、审计证据和可用范围；
- app 内容是否可能进入 memory 或影响 web search。

输出一个“权限、授权和审计矩阵”。

### RQ3 — GitHub 与 ChatGPT 的当前能力边界

研究不同 surface 中的 GitHub 能力：

- 普通 Chat；
- Project Chat；
- Deep Research；
- Agent mode；
- ChatGPT Work；
- Codex。

至少覆盖：

- repository authorization；
- sync 与 search indexing；
- file/code read；
- commit metadata；
- PR metadata；
- branch/ref enumeration；
- pagination/coverage guarantees；
- data freshness、cache 和 indexing delay；
- write actions；
- mechanical before/after proof 能力；
- plan/surface/account differences。

明确区分：

```text
platform capability
≠ app permission
≠ repository authorization
≠ current task authority
```

输出一个“GitHub capability-by-surface 矩阵”。

### RQ4 — Deep Research 的来源、Apps 和报告行为

研究：

- Deep Research 可使用哪些来源；
- connected apps 是否仅使用 read actions；
- specific sites / trusted sites 控制；
- 研究计划 review、实时进度、interrupt/refine；
- Project 内 Deep Research 的可用性和上下文行为；
- 报告引用、sources-used、activity history 和下载格式；
- plan/region/workspace 限制和 usage counter；
- Deep Research 与 Agent mode、Work 的区别。

给出 Mnemosyne 未来选择 Deep Research 的明确适用条件和不适用条件。

### RQ5 — Chat、Work、Deep Research、Codex 与 Agent mode 的 surface selection

研究每个 surface 的：

- 主要任务类型；
- 长任务能力；
- repository/tool 能力；
- context/memory 行为；
- artifact 生成和迁移；
- 用户 approval；
- 任务恢复；
- 可审计性；
- 适合 Mnemosyne 的任务类型。

输出一个“surface selection 决策表”，但不得直接升级为执行源规则。

### RQ6 — 模型、reasoning 和 provenance

研究：

- visible model label 能证明什么，不能证明什么；
- reasoning setting 是否可被模型自身观察；
- model fallback、quota fallback 和服务故障的官方行为；
- 如何记录 operator-observed UI facts；
- 如何区分模型身份、surface、effort、tool availability 和实际输出质量；
- strict replay 中最低充分 provenance schema。

提出一份候选 provenance schema。

### RQ7 — Mechanical no-write proof 与外部观察者

研究以下 proof classes 的可行性、强度和限制：

- local Git working-tree diff；
- remote refs snapshot；
- GitHub branch/PR/repository event snapshot；
- GitHub App read-only installation；
- platform-enforced read-only action surface；
- app/action audit logs；
- external observer；
- signed attestation；
- tool call log；
- run-scoped exception。

回答：

- 什么证据可以证明“没有默认分支写入”；
- 什么证据可以证明“没有任何 branch/PR/object 写入”；
- 什么证据只能说明“没有检测到写入”；
- Mnemosyne §19 是否需要未来研究性修订；
- observer-assisted run 应如何设计。

仅提出候选方案，不修改执行源。

### RQ8 — Handoff、artifact 和业务对话约束

研究：

- 长 transfer artifact 的文件优先交付；
- 同一回复直接生成低风险 artifact；
- Markdown/code-block 结构损坏风险；
- 目标项目业务对话应加载项目本地指导、裁剪后的 Mnemosyne 通用指导，还是完整 Mnemosyne 指导；
- context pollution、authority conflict、token cost、auditability 和 usability 的权衡。

对 `HO-GUIDANCE-001`、Issue #170 和 Issue #171 给出候选处理框架。

### RQ9 — 跨平台对照

在不失去主线的前提下，对比：

- Anthropic Claude Projects / memory / connectors / research；
- Google Gemini Gems / Deep Research / connected sources；
- Microsoft Copilot / GitHub Copilot / VS Code agent workflows；
- Cursor 或其他主流 coding agents；
- 相关 MCP、Agent-to-Agent、context engineering 和 memory evaluation 实践。

目的不是罗列产品，而是识别可迁移到 Mnemosyne 的成熟机制和不可迁移的差异。

## 必须交付的报告结构

1. Executive summary
2. Research scope and method
3. Source manifest
4. Current product/surface facts
5. Delta against Mnemosyne 2026Q2 evidence
6. Project memory and cleanroom isolation matrix
7. Apps/plugins permission and audit matrix
8. GitHub capability-by-surface matrix
9. Deep Research source/control assessment
10. Surface-selection decision table
11. Model/reasoning provenance schema
12. Mechanical no-write proof taxonomy
13. Handoff and artifact-delivery implications
14. Open-question disposition candidates
15. Recommended staged Mnemosyne work packages
16. Unsupported assumptions and unresolved uncertainties
17. Limitations
18. Conclusion
19. Full bibliography / sources used

## Delta 分类要求

对每一项重要发现标记：

```yaml
classification:
  - confirmed_current_fact
  - changed_since_2026Q2
  - repository_assumption_still_valid
  - repository_assumption_stale
  - repository_assumption_partially_stale
  - unknown_requires_live_test
  - candidate_guidance_only
```

并给出：

- 当前仓库路径；
- 支持或冲突的外部来源；
- 建议动作；
- 是否需要用户批准；
- 是否可能影响执行源；
- 是否应先做 live test。

## 结论边界

- 研究报告是高权重证据，不是执行源。
- 不得直接修改 Mnemosyne 规则。
- 不得把单个平台当前行为外推为永久保证。
- 不得把 marketing claim 与 mechanically verified capability 混为一谈。
- 不得将 PASS、研究建议或 capability availability 转换成写入授权。

## 输出要求

- **完整报告正文必须出现在 Deep Research 最终报告正文中。**
- 不得只提供摘要和下载文件。
- 可以同时提供 Markdown、Word 或 PDF 下载副本，但它们只能是辅助备份。
- 关键事实必须有可核验引用。
- 重要矛盾必须同时展示各来源证据。
- 使用中文撰写，保留必要英文术语、文件路径和产品名称。
- 最后提供一个可直接带回 Mnemosyne 维护对话的高信号 handoff：

```yaml
deep_research_result_handoff:
  prompt_id: PROMPT-2026Q3-PLATFORM-DELTA-0001
  proposed_cycle_id: RC-2026Q3-platform-context-apps-delta
  report_title:
  execution_surface:
  sources_used:
  connected_apps_used:
  repository_paths_read:
  key_confirmed_deltas:
  stale_repository_assumptions:
  candidate_repairs:
  live_tests_recommended:
  execution_source_changes_proposed_but_not_approved:
  unresolved_questions:
  limitations:
  safe_next_action: return_full_report_to_Mnemosyne_maintenance_conversation_for_review
```

## END DEEP RESEARCH PROMPT
