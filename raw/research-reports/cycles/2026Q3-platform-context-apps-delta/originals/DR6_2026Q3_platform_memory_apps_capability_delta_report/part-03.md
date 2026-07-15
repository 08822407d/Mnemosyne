| 快速事实问答、轻量讨论 | Chat | 启动快、交互成本低 | Codex、Agent（过重）citeturn13view0 |
| 需要明确引用与多源合成的研究报告 | Deep Research | 计划可审、来源可控、只读 app actions、报告有 citations/activity history | 普通 Chat（证据可追踪性较弱）citeturn11view4turn11view5 |
| 项目持续性知识工作、同一主题多聊天累积 | Project Chat | project files/instructions/sources 与 project 内 memory 最适合持续推进 | Temporary Chat（不能持久）citeturn28view1turn28view4 |
| 长文档、表格、演示、站点交付 | Work | 明确面向 deliverables，可继续推进与调度 | Deep Research（以研究报告为主）citeturn13view0turn33search0 |
| 仓库代码改动、测试、diff、PR review | Codex | 明确面向 repo/tool/worktree/terminal/GitHub | Work、Deep Research citeturn13view0turn34search0turn34search8 |
| 需要网页登录、表单、动作编排、跨工具长任务 | Agent mode | browser + terminal + apps + approvals | Chat/Project Chat（动作能力不足）citeturn13view1 |
| Mnemosyne 的“只读研究 cycle” | Deep Research 或 Project Chat + 只读 apps | 风险最低、证据最好 | Codex、Agent mode 默认不合适 citeturn10view5turn28view1 |
| Mnemosyne 的“仓库代码执行/修补” | Codex，但需单独授权 | 有本地/云 repo 工作能力 | Chat、Deep Research citeturn13view0turn34search2 |

**RQ6 关于 model、reasoning 与 provenance 的结论，比很多团队直觉上更“保守”。** OpenAI 现在已经明说，至少在 Business workspace 中，**model picker 的标签是简化控制，不会改变底层模型或 usage limits**；同时 GPT-5.6 帮助页也明确说，自动路由可让 Instant 切到更高 reasoning，而当 GPT-5.6 reasoning allowance 用尽时，ChatGPT **可能继续使用 GPT-5.4 Thinking mini**。再结合 release notes 里“fallback model 不一定出现在 picker 中”的说明，可以得到一个对 Mnemosyne 很重要的取证结论：**可见 label 只能证明“用户看见了什么控件状态”，不能单独证明“这一轮实际底层模型恒为某个具体型号”。** citeturn38view0turn38view1turn17view0turn17view1turn17view2

因此，严格 replay / provenance 不应只写“model: GPT-5.x”。更适合 Mnemosyne 的 **最低充分 provenance schema** 应包含这些字段：

| 字段 | 是否建议必填 | 作用 |
|---|---|---|
| `timestamp_start` / `timestamp_end` | 是 | 绑定运行时点，便于对照 release/status/limits |
| `surface` | 是 | Chat / Project / Deep Research / Work / Codex / Agent |
| `workspace_or_plan` | 是 | Business / Enterprise / Pro / Plus 等，因为行为差异很大 |
| `project_id_or_name` 与 `project_memory_mode` | 若在 project 内则必填 | 区分 default 与 project-only |
| `visible_model_picker_state` | 是 | 记录用户看到的 Instant/Medium/High/Pro 等 |
| `model_auto_routing_setting` | 建议 | 例如是否开启 auto-switch |
| `known_fallback_notice_or_limit_event` | 建议 | 记录是否出现 allowance/fallback 提示 |
| `connected_apps_enabled` | 是 | 哪些 app 在该 run 可被调用 |
| `app_permission_mode` | 建议 | Always ask / Any changes / Important actions / Never ask |
| `repository_authorization_scope` | 涉 GitHub 时必填 | 哪些 repos 被 GitHub app 授权 |
| `sync_state_if_known` | 建议 | none / partial / complete / unknown |
| `sources_selected` | Deep Research 必填 | web / files / apps / sites |
| `tooling_evidence` | 建议 | sources used、activity history、diff、Compliance export 等 |
| `operator_observed_ui_facts` | 建议 | 例如“GitHub 在标准 Chat 不可见、在 DR 可见” |
| `before_after_git_evidence` | 涉 repo run 时必填 | 本地 diff、remote refs、PR/event snapshot |
| `status_incident_reference` | 有异常时建议 | 便于区分服务故障与产品规则 |

这个 schema 的核心思想是：**记录“可观察事实”和“外部可校验证据”，而不是让模型自己宣称它是谁、用了多少 reasoning。** 公开文档支持我们记录 picker、fallback、surface 与 app 边界，但并没有提供“模型可自我认证 reasoning setting”的能力承诺，因此把模型自述当成 provenance 证据并不稳妥。citeturn38view0turn38view1turn38view2

## No-write 证明、交接与 artifact 处理

**RQ7 的关键不是“能不能证明没写”，而是“你想证明到哪一层”。** GitHub 官方文档足以说明 repository 写权限与 reader 观察能力是分层的：GitHub App 安装时需要明确授予 repository/org 权限并选择可访问哪些仓库；某些 API 端点只需 read contents 或 read pull requests，另一些则需要 write 权限。与此同时，GitHub REST API 本身是分页的；list branches 默认一页 30、最多 100；pull request commit list 甚至有“最多 250 commits”这种硬上限。结果就是：**任何不完整枚举、未跨页追取、未覆盖全部 refs/events 的观察，最多只能证明“未检测到写入”，很难证明“绝无写入”。** citeturn35view6turn35view2turn35view1turn35view4turn35view0

基于这一点，可以把 Mnemosyne 需要的证明分成五档：

| 证明类 | 能证明什么 | 不能证明什么 | 强度 |
|---|---|---|---|
| 本地 working-tree / `git diff` | 当前 checkout 没有未提交改动 | 不能排除远端 branch/PR/object 写入 | 低 |
| 远端 default branch ref 前后快照 | 在观察窗口内 default branch ref 未移动 | 不能排除 side branch、PR、new objects | 中 |
| 远端 refs + PR + repository events 联合快照 | 在已枚举范围内未见 branch/PR/event 变化 | 仍受分页、覆盖范围与事件保留限制影响 | 中高 |
| GitHub App 只读安装 + surface 只读能力 | 当前授权姿态不允许经该 app 发起写入 | 不能排除其他 token/账户/通道写入 | 高 |
