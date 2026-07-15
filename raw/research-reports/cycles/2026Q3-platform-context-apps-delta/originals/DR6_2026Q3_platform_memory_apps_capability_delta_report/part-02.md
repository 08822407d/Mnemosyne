|---|---|---|---|---|---|---|
| 普通 Chat | 取决于 memory 设置 | 不适用 | 可能引用过往聊天 | 全局 custom instructions 生效 | 不适合 | Memory FAQ 说明 memory 会个性化，临时聊天才是 blank slate。citeturn9view1turn36search6 |
| Temporary Chat | 不用已有 memory，也不创建新 memory | 否 | 否 | 在一般 Temporary Chat 中不创建记忆；macOS 说明自定义 instructions 仍会生效 | 适合短时 cleanroom，但不能并入 project | Temporary chats 不进 history，不建 memory，且不能加入 project。citeturn36search0turn36search3turn10view2 |
| Project default on Enterprise/Edu | 参考 saved memory 受设置影响 | 是 | 否 | 仅 project instructions；project 内建 memory | 中等，取决于 workspace/personal settings | Enterprise/Edu 的 default 仍限制在 project 内。citeturn10view0turn11view0 |
| Project default on Non-Enterprise | 是 | 是 | **是**，可引用 project 外聊天 | 仅 project instructions | 不适合 strict cleanroom | Plus/Pro/Business 下 default project 仍可能跨项目引用。citeturn11view0 |
| Project-only | 不引用既有 saved memory | 是 | 否 | 仅 project instructions，覆盖全局 custom instructions | **最适合** | 这是官方当前最强的项目隔离模式。citeturn10view0turn28view3 |
| Shared project | 转为 project-only | 是 | 否 | 共享 project 的 instructions/files/chats 共同构成上下文 | 适合团队内隔离，不适合个人隐私上下文 | Shared project 自动 project-only，成员可见 chats/files/members。citeturn10view0turn10view1 |

对 Mnemosyne 的直接含义是：**“Project-only + 新建 + private + 不搬旧聊天进入项目”** 才是最接近你在提示词里要求的最低可靠 cleanroom 配置。仅仅“新开一个聊天”或“把聊天放进某个旧 project”都不够；尤其在非 Enterprise 环境下，default project 仍可能把项目外聊天带进来。citeturn10view1turn11view0

再看 **“权限、授权和审计矩阵”**。这里最容易混淆的是：**Plugin Directory 可见**、**workspace app enabled**、**user OAuth connected**、**sync 已完成**、**某个 action 被允许**、**这一轮是否要审批**，实际上是六个不同层级。citeturn31view0turn31view1turn31view2

| 层级 | 当前语义 | 关键限制 | 审计/证据 |
|---|---|---|---|
| Plugin discovery | 用户能在 Plugin Directory 看到某个 workflow capability | 可见不代表可安装/可调用 | 主要是 UI 事实，不代表 runtime authority。citeturn31view1turn31view2 |
| Workspace app enablement | 管理员决定 app 在 workspace 中是否可用；Business 默认开，Enterprise/Edu 默认关 | 仍不等于用户已连接 | 管理面可记录，但公开文档未给取证级字段。citeturn31view1turn15view0 |
| User connection / OAuth | 用户在 Settings/Directory 中完成 app 登录与授权 | 只授予 source-system 允许的范围 | 源系统权限继续生效，ChatGPT 不能越权。citeturn31view1turn31view2turn39view3 |
| Sync / indexing | 预索引内容，提高质量与速度 | 初始可能 partial sync，结果可能缺失；有刷新延迟 | 只能证明“已索引到某状态”，不能证明覆盖完整。citeturn32view0 |
| Action control | 管理员规定允许读、允许写、或自定义动作集合；新动作默认关闭 | 并非所有 app 都支持 granular action control | 新动作/变更动作支持 diff，有利于审计。citeturn11view1turn31view3 |
| Approval policy | Always ask / Any changes / Important actions / Never ask | “Never ask” 风险最高 | Enterprise/Edu conversations 与 app calls 可进 Compliance。citeturn10view6turn10view7turn31view0 |

对 memory 的一个新增风险也必须单独指出：**synced app data 现在不只是“会被聊天用到”，官方还明确写到如果 Memory 开着，ChatGPT 可能把从 connected apps 访问到的相关信息保存并再次使用。** 这意味着 Mnemosyne 的“外部持久记忆”与平台原生 memory 已经开始出现双层持久化风险：一个在仓库/文件/外部 artifacts，另一个在平台 personalization/memory。做 cleanroom 时，必须把 **memory 开关、project memory mode、connected apps、sync** 一并纳入前置检查。citeturn32view0turn9view1

最后给出 **“GitHub capability-by-surface 矩阵”**。为了避免把平台能力、app 权限、仓库授权和当前任务 authority 混淆，下面每行都按“能读什么、写路径是什么、已知新鲜度/索引限制、Mnemosyne 风险判断”写。

| Surface | 读能力 | 索引/新鲜度 | 写能力 | Mnemosyne 判断 |
|---|---|---|---|---|
| 普通 Chat | 对 Enterprise/Edu，官方已公开 GitHub chat connector；对部分 consumer/Plus，GitHub 可能在标准 Chat 不可见，但在 DR/Agent 可见 | 新 repo 约 5 分钟显示延迟；GitHub search index 可能缺失 | OpenAI 公开 GitHub Chat 文档没有给出明确 GitHub 写动作矩阵 | **可做轻量问答，不可用于 no-write 证明**。citeturn11view2turn40search0 |
| Project Chat | 继承 project files/instructions/sources，并可调用 connected apps；项目内使用 app 时可能先要求确认能否到项目外取数 | Project sources 是显式上下文；外部 app 仍可能越出 project 去读外部系统 | 未见 GitHub project-chat 写路径的公开明示 | **适合 bounded read context，不适合把 project 当写保护证明**。citeturn28view1turn28view3 |
| Deep Research | 公网、上传文件、connected apps；对 apps 仅使用 read actions，并提供 citations、sources used、activity history 与导出 | 支持 specific sites / prioritize sites；可中断与修改计划 | **Research 过程中不调用 app write actions** | **最适合研究性只读 run**。citeturn11view4turn11view5turn10view5 |
| Agent mode | 可用 browser、code interpreter、apps、terminal；GitHub availability 依 plan/experience | 任务通常 5–30 分钟；可调度、可中断 | agent mode 本身可代表用户采取行动，但公开 GitHub 专项写矩阵不足 | **适合长任务/网页登录/动作编排；默认不适合 Mnemosyne no-write**。citeturn13view1turn11view2 |
| Work | 面向研究、分析与文档/表格/演示生成；web/mobile 为 cloud Work，desktop 还可用本地文件 | 不是 repo-first surface；插件目录可在 Work 中可见 | 公开文档未把 Work 定位为 GitHub 写入主 surface | **适合 deliverable，不适合仓库写证明**。citeturn13view0turn31view2turn38view1 |
| Codex | 明确面向代码、测试、仓库、终端；可在桌面与 GitHub/云环境工作；官方有 GitHub PR review 与 cloud task 文档 | 可连接 GitHub repo、环境、diff/worktree；强调 reviewable diffs | **可以在 GitHub 上发 review、在分支上改动、甚至提出 PR** | **适合编码和受控改动；默认高风险，不适合作为“无写”运行面**。citeturn13view0turn34search0turn34search2turn34search8turn18search5 |

这张表对应 Mnemosyne 最重要的一句 operational rule：**平台 capability ≠ app permission ≠ repository authorization ≠ current task authority。** GitHub 被连接了，不代表当前 surface 一定能调用；能调用，不代表在 sync；在 sync，不代表结果完备；能看到 repo，不代表本轮被允许写。citeturn11view2turn31view0turn32view0turn35view6

## Deep Research、Work、Codex、Agent 与 provenance

**RQ4 的答案相对干净。** OpenAI 现在把 Deep Research 定义为：用户先给目标、再选来源（public web、uploaded files、connected apps、specific sites），系统先生成可审阅的 research plan，用户能在开跑前编辑计划、在运行中实时看进度、随时 interrupt/refine，并在完成后得到带引用的结构化报告、sources used、activity history，以及 Markdown、Word、PDF 导出。对 Enterprise/Edu，Deep Research 还受 RBAC 控制；而 connected apps 在 Deep Research 中只启用 **read actions**。这意味着它非常适合作为 Mnemosyne 的**研究 evidence 采集面**，而不是仓库执行面。citeturn10view4turn11view4turn11view5

**RQ5 的 surface selection 现在比 2026Q2 明显更清楚。** OpenAI 的 Work and Codex 页面已经把三件事直接分开：**Chat** 用于 quick conversational help；**Work** 用于 research、analysis，以及 document/spreadsheet/presentation/report/Site 等 deliverables；**Codex** 用于 write/debug code、run tests and commands、review changes、work with a repository。与此同时，agent mode 侧重点是“网上完成复杂任务并在你控制下采取动作”，而 Deep Research 则是“多源研究与带证据报告”。这几个 surface 的主任务、工具边界和可审计性，已经不应该再被视为一个连续光谱上的微调，而是**不同治理等级的工作面**。citeturn13view0turn13view1turn9view2

下面是建议性的 **surface selection 决策表**。它是候选 guidance，不是执行源。

| 任务类型 | 首选 surface | 原因 | 不宜使用的 surface |
|---|---|---|---|
