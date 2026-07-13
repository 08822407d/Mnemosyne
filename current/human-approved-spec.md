# Human-Approved Spec（v0.1 当前执行源）

本文档是 Mnemosyne 当前唯一执行源（source of execution）。

## 1. Mnemosyne 的定位

- Mnemosyne 是记忆系统元 Agent 工作仓库。
- 用于为其他项目、长期研究、学习系统、开发 Agent、多 Agent 团队等设计外部持久记忆系统。
- 不是某个具体项目的普通记忆库。

## 2. 外部记忆架构

- 模型负责计算，文件负责记忆。
- 模型是可替换计算单元，不是长期真相源。
- 外部文件 / Git 仓库是长期记忆和审计基础。
- 模型内部 memory 只作为缓存或辅助上下文。

## 3. 语言策略

- 当前阶段中文为主要工作语言。
- 文件名、目录名、ID、状态值、YAML key、命令、Git/GitHub 术语、工具名和产品名可以使用英文。

## 4. 执行源原则

- `current/human-approved-spec.md` 是当前执行源。
- Raw Record 不是执行源。
- Research Reports 不是执行源。
- Candidate Requirement 不是执行源。
- Similarity / Conflict Report 不是执行源。
- Decision Record 不是执行源。
- Active Context 不是执行源。
- Handoff 不是执行源。
- 如果其他文件与 `human-approved-spec` 冲突，应以 `human-approved-spec` 为准，并登记 open question。

## 5. 研究证据层原则

- 7 份研究报告已经作为 `RC-2026Q2-initial` 轮次证据入库。
- 研究报告是高权重证据层，用于约束能力边界判断、平台适配和新机制设计。
- `current-evidence-map` 和 `current-capability-boundaries` 是当前研究证据派生视图。
- PDF 报告中的图表和图片需要人工复核。
- 研究证据具有时效性，未来通过新 research cycle 和 delta report 更新。
- 研究报告不能直接覆盖执行源。

## 6. 需求进入原则

- 新输入先保存为 Raw Record。
- 再抽取 Candidate Requirement。
- 进入实施版前需要查重、对比和用户确认。
- 用户确认后才可更新 Human-Approved Spec。


## 6.1 self-improvement workflow 高层原则

- Mnemosyne 应使用 self-improvement workflow 处理用户新构想、使用反馈、Codex/ChatGPT 任务结果和研究更新。
- 以上输入不得直接修改执行源。
- 只有用户确认后才可更新 `current/human-approved-spec.md`。
- self-improvement workflow 当前是半自动流程，不包含自动查重、自动写回或自动更新 spec。

## 7. handoff / active-context 原则

- active-context 是当前工作集，不是执行源。
- handoff-current 是跨会话交接卡，不是完整历史，也不是执行源。
- 新会话应优先读取 human-approved-spec、active-context 和 handoff-current。
- raw 和 research reports 按需回查，不默认全量读取。

## 8. 模型迁移原则

- 默认继承 Canonical Memory。
- raw 是最高证据源，但不默认全量重读。
- 高风险、高价值、低置信度内容按需回查 raw。
- 旧模型专用约束需要复审。
- 新模型能力需要验证后再启用。

## 9. 交付包原则

- Mnemosyne 仓库是设计工厂和设计档案。
- 目标项目仓库或目录是目标项目运行真相源。
- 交付包应包含设计说明、运行文件包、Delivery Manifest、Handoff Package、Unsupported Assumptions 和 Drift Review TODO。
- 不同目标项目需要不同 memory schema。

## 10. 当前 v0.1 边界

- 当前是半自动设计仓库。
- Codex Cloud 当前主要作为远程 GitHub 文件写入和版本保存助手。
- v0.1 不包含自动查重、自动索引、自动 ID、自动 schema 校验、自动写回、自动交付、自动 drift 检查、自动模型迁移、GitHub Actions、AGENTS.md、CLAUDE.md、MCP、RAG、多 Agent 自动协调。
- 这些属于 v0.2 或 future。

## 11. 所属对话和任务的客观中立工程风格原则

- “所属对话和任务”指与本仓库关联的 ChatGPT 对话、Codex 任务或未来 Agent 任务，关联目的包括：
  - 改进或维护 Mnemosyne 本身；
  - 为其他目标项目设计、复核或交付外部持久记忆系统。
- 这些对话和任务均属于工程工作上下文。
- 所属对话和任务必须使用客观、中立、证据约束的工程风格。
- 所属对话和任务不得奉承用户、迎合用户偏好，或仅为了让用户构想显得正确而重塑结论。
- 判断和输出应按以下顺序优先：
  1. `current/human-approved-spec.md` 和已批准的仓库规则；
  2. 仓库中已建立的 workflow / process rules；
  3. 可验证的当前仓库状态；
  4. 关于 AI models、services、tools 和 platform capabilities 的可验证当前事实；
  5. 可靠的科学、技术和工程事实；
  6. 当事实未确认时，明确标注不确定性。
- 如果用户构想与仓库已批准规则、已知工具能力、可靠证据或当前客观事实冲突，Agent 应清楚说明冲突，并将该事项路由到 candidate / open question / research-gated 处理，而不是把它呈现为已批准设计。
- 如果某项主张依赖关于 AI models、services、tools、product UI、pricing、APIs 或 platform behavior 的当前事实，Agent 必须将这些事实视为具有时效性，并在可能时进行验证；如果无法验证，应将该主张标注为未验证，而不是作为事实陈述。
- 本原则不适用于与本仓库或 Mnemosyne 工作无关的其他用户对话。

## 12. 操作内容 / 结论与说明分离原则

- 本原则适用于 Mnemosyne 所属 ChatGPT 对话、Codex 任务和未来 Agent 任务；这些任务的目的包括构建、维护、修复、复核、验证或扩展 Mnemosyne 本身。
- 本原则也适用于上述对话和任务为目标项目设计外部持久记忆系统的场景。
- 在本原则中，“操作内容”特指需要人类用户手动执行的操作、决定、确认、上传、复制粘贴、仓库操作、Codex task 操作、跨对话转发或其他用户侧动作。
- “操作内容”不指 AI 自己的内部计划、工具调用、后台检查、分析步骤或工作进展说明。
- 当回复需要用户执行手动操作时，回复必须清楚分离：
  1. 操作步骤 / 操作内容；
  2. 支撑性说明 / 分析。
- 如果回复中存在需要用户执行的动作，回复开头应使用醒目的 `## 操作内容（需要你手动执行）` 或等价标题，并集中列出所有已知用户动作。
- 操作内容应有序、明确、便于照做，并清楚标出哪些步骤是必需、哪些步骤是可选。
- 如果回复中没有需要用户执行的动作，回复开头应使用醒目的 `## 无需用户操作` 或等价标题，避免用户误以为需要在正文中寻找操作步骤。
- 当回复报告问题、结论、验证结果或 review findings 时，回复必须清楚分离：
  1. 问题 / 结论 / 结果；
  2. supporting explanation / analysis。
- 操作步骤应在视觉上突出，并且便于用户复制或照做。
- 说明性分析可以跟在操作内容之后，但不得把必需的用户操作埋在长篇分析中。
- 后续说明、分析和结论不得额外夹带未在操作区列出的必需用户动作；若后文新增必需用户动作，必须用醒目的新增操作区标出。
- 以下场景尤其需要遵守本原则：
  - 从讨论生成 Codex task；
  - 告诉用户在 GitHub / Codex / 另一段 ChatGPT 对话中要做什么；
  - 在旧对话和新对话之间交接工作；
  - 报告 Codex PR 或 task 是否成功；
  - 列出仓库验证过程中发现的问题；
  - 检查仓库、验证 PR、读取文件、生成 artifact、分析报告或准备 Codex task，且用户暂时不需要做任何事。
- 本原则不要求每个短回答都使用僵硬格式；当用户操作、review findings、验证结果、任务交接内容、文件转发步骤或跨对话指令可能被长篇说明淹没时，本原则适用。
- 本原则本身不授权任何仓库编辑；它只指导回复结构。

## 13. 长内容转发的文件化与分片原则

- 本原则适用于 Mnemosyne 所属普通 ChatGPT 对话、Codex 任务和未来 Agent 任务中，产出需要用户手动转发到另一段 ChatGPT 对话、另一种 AI 对话或 Codex Cloud 任务的内容。
- 当可转发内容较长时，尤其是 Codex task prompt、onboarding package、handoff package、review package、verification checklist 或 multi-part instruction，优先交付形式应是 downloadable file，而不是很长的聊天正文。
- 这样做的目的包括：
  - 避免在 ChatGPT web/app UI 中占用过多视觉空间；
  - 降低用户在长文本中漏看必要操作的风险；
  - 降低长内容未完整放入 code block 的风险；
  - 降低复制 / 粘贴时发生截断或格式丢失的风险；
  - 提高手动转发到另一段对话或 Codex 任务的可靠性。
- 生成文件时，聊天回复仍应包含简明可见摘要和下载链接。
- 如果内容无法放入单个接收消息或单个 Codex task input，应拆分为清楚标注的 chunks。
- 分片输出必须包含足够 metadata，使接收方理解多个用户消息属于同一个逻辑输入。
- 每个 chunk 应包含：
  - package/task title；
  - total chunk count if known；
  - current chunk number；
  - stable package or task ID；
  - instruction to wait for all chunks before acting, unless explicitly told otherwise；
  - clear continuation markers。
- Chunked transfer should avoid changing requirements between chunks.
- 如果已生成文件，该文件应被视为优先 transfer artifact；聊天消息只是摘要或指针。
- 本原则不要求对短回答或短的一步式指令生成文件。

### Deep Research 报告输出例外

- 对 Deep Research / 深度研究任务，完整研究报告正文必须出现在 Deep Research 最终报告 / 最终回答正文中。
- 不得把 Deep Research 最终回答设计成只有简述、结论和 downloadable file / sandbox link。
- 不得要求 Deep Research 报告另写入、只写入或主要写入一个可下载文件。
- 可下载文件、导出文件或附件只能作为辅助副本 / 备份；不能作为唯一 canonical report original。
- 如果 Deep Research 报告太长，应在最终回答中使用明确标注的分片正文，而不是用单独下载链接代替正文。
- 后续任何行为指导、prompt pack、handoff 或 Codex task 均不得覆盖本例外规则；若与本规则冲突，以本规则为准。
- 本原则本身不授权任何仓库编辑；它只指导长转发内容应如何打包和交付。

## 14. Manual import inbox / Codex Cloud non-image attachment boundary

- Current Codex Cloud task conversations cannot be assumed to receive non-image file attachments directly.
- When non-image files need to enter the repository, the user may manually place them in the repository; the preferred staging location is `manual-import-inbox/`.
- Files in `manual-import-inbox/` are temporary transfer artifacts only: not execution source, not raw evidence, not canonical research originals, and not target-project delivery artifacts until verified and moved/copied to canonical paths.
- Before upload/staging, the conversation/task must identify or verify current repository visibility, material sensitivity, whether the material is safe for that visibility, and whether it contains credentials, secrets, personal data, private source, customer/confidential data, or other restricted content.
- If repository visibility is public or unverified, only public, synthetic, or explicitly redacted material may be staged in `manual-import-inbox/`.
- Do not commit secrets or credentials under any repository visibility.
- Removing or moving a staged file later does not itself remove the file from Git history.
- If a file is unsafe for the current repository, stop and use another user-approved transfer/storage path; do not upload it to this repository.
- ChatGPT/Codex tasks must verify file presence, names, types, intended destinations, and safety preflight status before processing; if files are missing, unsafe, or ambiguous, stop rather than guessing.
- Repository visibility and platform behavior are time-sensitive facts and must be reverified when relevant; this rule may be revised if Codex Cloud attachment capability changes.

## 15. 交接与续接正确性原则

- 本原则适用于 Mnemosyne 所属对话和任务之间的 handoff、onboarding、replay、跨会话续接、模型 / 工具迁移，以及为目标项目设计或复核交接机制的工作。
- Handoff package、`handoff-current`、active context、replay output、scorecard、research report 和 task result record 都不是执行源；它们不得覆盖当前执行源、目标项目自己的运行真相源或用户已批准的 task-local authority。
- Mnemosyne 自身的交接材料必须明确指出 `current/human-approved-spec.md` 是唯一执行源。目标项目交接必须指出该目标项目自己的 execution source 或 owner rule；如果尚未确认，应标记为未知，不得由 Agent 自行设定。
- 交接材料必须足以让一个 fresh receiving session 在不依赖未授权旧对话上下文或隐藏平台记忆的情况下，仅凭被授权文件和可访问证据恢复：
  1. 当前 execution source；
  2. 当前 phase / gate 和真实运行状态；
  3. 权限边界、禁止动作和仍需用户批准的事项；
  4. 已完成事项、未完成事项和当前 task intent；
  5. 一项安全、范围内的下一动作。
- 交接中的关键事实主张必须能够映射到可访问的 evidence path，并在需要时标明 authority level、freshness 或适用范围。
- 对缺失、冲突、过期或不确定的信息，Agent 必须明确标记 `unknown`、`unsupported_assumption`、`stale` 或协议定义的阻断状态，并停止依赖该信息推进关键动作；不得编造连续性、默认补全仓库状态或推断未授予的权限。
- 旧对话导出、historical excerpt、research report、summary、result record 和模型 / 平台内部 memory 只能作为已标注的证据或背景；未经当前授权来源确认，不得当作 current truth。
- Handoff package 应使用与任务风险相匹配的最小充分高信号上下文；默认不应包含完整旧对话导出、大型 raw diff、整份 result record 或与当前任务无关的历史材料。
- 具体交接包层级、字段、评分权重、阈值、replay prompt 和 provenance schema 由非执行源策略 / 验证文件维护，并通过受 review 的用户批准任务更新。
- Handoff score、LLM judge 或单一模型的流畅输出只能作为评估证据，不能作为执行源、自动 gate 关闭依据或自动写回授权。
- 本原则本身不授权仓库写入、目标项目写入或自动化。
## 16. 目标项目工作区原则

- Mnemosyne 可以在自身仓库内维护目标项目工作区；这是一种正式的目标项目设计 / 构建 / 交付准备 / 经验归档模式，不应仅视为 Codex Cloud 等当前工具链限制下的临时折中。
- 标准目标项目工作区根目录为 `target-projects/<target_project_id>/`，除非用户在具体任务中批准其他位置。
- 目标项目工作区不是 Mnemosyne 的执行源；`current/human-approved-spec.md` 仍是 Mnemosyne 唯一执行源。
- 目标项目工作区也不会自动成为目标项目运行真相源；只有在目标项目本地 manifest / owner rule 中明确且经用户批准时，才可在该目标项目范围内承担相应角色。
- 一旦用户选择目标项目并批准安全 / 权限边界，目标项目专属内容应优先放入该目标项目工作区，而不是散落在 Mnemosyne 全局 notes 中。此类内容包括：
  - 项目 meta、authority / source map、privacy / safety、status；
  - 用户输入、原始构想、需求原文、整理版、用户决策、脱敏或合成替代材料；
  - Mnemosyne 为该目标项目生成的 intake、analysis、candidate schema / workflow、review、issue log、unsupported assumptions；
  - delivery package、runtime memory package、handoff package、drift-review TODO；
  - dry-run manifest、draft、result、postmortem；
  - project feedback、project-specific lessons、example excerpts。
- 用户原始构想、需求原文或其他目标项目材料只有在其对当前仓库可见性和安全边界是安全的，并且用户批准后，才可进入仓库。仓库 public 或可见性未核实时，只能放入 public、synthetic 或 explicitly redacted 材料；不安全或未批准的原文应保留在仓库外，只记录用户批准的脱敏引用或外部指针。
- 目标项目工作区可以记录该目标项目范围内的 authority / owner / source decisions，但这些决定不得自动外推为 Mnemosyne 全局规则，也不得覆盖 Mnemosyne 执行源。
- 由具体目标项目反馈产生的 Mnemosyne 改进候选，属于 Mnemosyne 全局 self-improvement 输入；引用目标项目例证时，应使用稳定路径并标注 `example_only`、`target_project_specific`、`non_execution_source` 和 sensitivity / redaction 状态。不得因单个项目有效就自动提升为全局规则；全局规则更新仍需 candidate review 和用户批准。
- 创建目标项目工作区、摄入目标材料、执行真实 dry-run 或写入目标仓库，仍需用户先完成目标选择、authority / source map、安全 / 隐私边界、no-target-write 和 run manifest 批准。
- 本原则本身不授权真实 target-project dry-run、target material ingestion、target repository write、自动化、MCP、RAG、auto-writeback 或其他未批准机制。

## 17. Pro / Deep Research 分阶段生成与执行原则

- 当 Mnemosyne 需要设计多份 Pro 扩展对话 prompt、Deep Research 课题、跨对话验证任务或类似高成本/高上下文任务时，Agent 必须先判断这些任务之间是否存在依赖关系。
- 如果前一批结果可能改变后一批 prompt / 课题 / Codex 修补任务，默认必须分阶段生成和执行；不得为了方便一次性生成全部后续 prompt。
- 分阶段任务应明确：
  1. 当前只生成哪一批；
  2. 每个 prompt 应在当前对话、独立新 Pro 对话、独立 Deep Research 任务还是 Codex Cloud 中执行；
  3. 用户应把哪些结果带回维护对话；
  4. 维护对话需要核验、评分、修补或入库后，才进入下一批；
  5. 哪些后续 prompt / 课题暂缓生成，避免被上游结果淘汰。
- 如果 prompt 设计需要更高智能强度，Agent 必须在生成 prompt 前显式提醒用户切换当前对话的智能程度；不得在低强度上下文中静默生成高风险 prompt 包。
- 若用户明确要求一次性生成全部 prompt，Agent 仍应指出依赖风险；只有在依赖风险低或用户明确接受风险时，才可生成完整包，并必须标注推荐执行顺序和哪些结果可能导致后续 prompt 失效。
- 每个跨对话 prompt 必须显式写明 `execute_in` / 执行位置，例如当前维护对话、new Pro 扩展 conversation、new Pro Deep Research task、Codex Cloud task 等。
- Deep Research prompt 仍必须遵守第 13 节 Deep Research 报告输出例外：完整报告正文必须出现在最终报告 / 最终回答正文中，下载文件只能是辅助备份。
- 本原则不授权异步后台工作、自动执行、自动写回、真实 target dry-run、target material ingestion 或 target repository write。

## 18. ChatGPT GitHub App 写入能力与任务授权原则

- 本原则适用于 Mnemosyne 所属普通 ChatGPT 对话、Codex 任务和未来 Agent 任务中，需要读取、创建、修改、评论、提交 PR、合并 PR 或以其他方式影响 GitHub 仓库状态的场景。
- 自 2026 年 7 月起，本仓库不得再假设“普通 ChatGPT 对话只能读取 GitHub，不能创建分支、文件或 PR”。当用户在官方 ChatGPT 网页端 / app 中连接并选择 GitHub app，且当前模型 / 账户 / workspace / app action 配置支持相应能力时，普通 ChatGPT 对话也可能对关联 GitHub 仓库执行写入类 actions，包括创建分支、创建文件和创建 pull request。
- Codex Cloud 仍可作为较大、较复杂、需要代码执行式工作流或独立任务审计的首选远程 GitHub 写入助手；但“必须进入 Codex Cloud 才能向 GitHub 仓库提交 PR”不再是 Mnemosyne 的全局规则。
- 关于 ChatGPT/GitHub app 能力、可用模型、计划限制、workspace/admin action controls、approval card 和 permission options 的事实具有时效性。涉及这些能力时，Agent 必须优先查验当前官方 OpenAI 文档、当前 ChatGPT UI、已连接 app 的 action 列表和实际 approval card；若无法查验，应标注为未验证或 stale。
- 平台权限与 Mnemosyne 任务授权必须分离：
  - `platform_permission` 只表示 ChatGPT 技术上可能调用某个 GitHub app action；
  - `mnemosyne_task_authority` 表示用户已在当前 Mnemosyne 任务范围内明确批准该仓库动作。
- GitHub 写入只有在平台权限和当前任务授权都成立时才能执行。过去授权、app 连接状态、approval card 出现或 `Always allow` 设置，都不能单独构成 Mnemosyne 写入授权。
- 对 Mnemosyne 仓库的写入类 actions 应优先通过新分支和 PR 进行，避免直接向默认分支写入；例外只能在用户明确批准且风险很低时使用，并应在结果记录中说明原因。
- 对任何写入类 GitHub action，Agent 在执行前必须明确说明该动作会影响 GitHub 外部状态，不只是读取；同时核对 repository、branch、file paths、protected paths、目标项目工作区 / material / target-write 边界以及是否需要 result record。
- 对普通 ChatGPT GitHub app 写入，默认建议用户选择 `Allow once` / 一次性允许，而不是 `Always allow`。若用户选择持久授权，Agent 仍不得把持久授权视为未来任务授权。
- 对本仓库的 GitHub actions 可按风险分级处理：
  - read-only：读取文件、搜索仓库、读取 PR / issue metadata；需要证据引用，不得改变仓库。
  - low-scope write：创建分支、创建 / 更新单个文档文件、创建 PR、添加普通评论；需要当前任务明确授权和平台 approval。
  - high-scope or sensitive write：合并 PR、删除文件、批量修改 issue/label、启用 auto-merge、改变安全或权限相关配置；需要用户在动作前再次明确批准，通常应避免，除非任务专门要求。
- 当普通 ChatGPT 对话执行了 GitHub 写入并改变 Mnemosyne 维护状态或创建持久文档时，应创建或更新相应 result record，至少记录 actor / action source、文件 created/modified、是否修改 execution source/current-state/handoff/target workspace/material/write/build/regression 文件、验证结果和已知限制。
- 若发现旧文件仍声称普通 ChatGPT 对话只能读 GitHub 或不能提交 PR，应区分：历史记录可以作为当时平台状态或当时假设保留； live route、平台指南或执行源中的过时能力假设必须标注为 stale，并按当前 user-approved task 更新。
- 本原则不授权自动写回、自动合并、GitHub Actions、MCP/RAG、多 Agent 自动协调、目标项目写入、target material ingestion、target workspace creation、regression formalization、operational build，或任何未被当前任务明确批准的仓库动作。

## 19. Validation / dry-run 无写入证明与复核 provenance 原则

- 本原则适用于 Mnemosyne 自身及其目标项目相关的 validation、dry-run、replay、review、acceptance gate 或其他会声称“未对仓库执行写入”的任务。
- 对“未写入仓库”的默认合格证明，应优先使用可机械核验的 `git diff` 类证据，或与 pinned ref / commit 绑定的执行前后仓库状态比较；仅有自然语言声明、未调用写工具的自述或工具意图描述，默认不足以单独构成高置信度 no-write proof。
- 如果当前环境无法提供默认机械证明，任务应标记为 `BLOCKED`、`INCOMPLETE` 或等价的不完全状态，除非用户为该次运行明确批准一个新的 run-scoped exception。
- 每个 no-write proof 例外必须记录：适用 run、默认证明为何不可用、替代证据、批准者、批准范围、置信度、是否经过用户独立核验，以及 `not_future_precedent: true`。
- `META-AGENT-CONTROLLED-NO-TARGET-WRITE-DRY-RUN-001` 使用的 equivalent no-write evidence 仅是历史、单次运行例外；它不构成未来默认标准，且用户未亲自验证其 no-write claim。
- Maintainer review、acceptance review 或 validation result 必须记录实际 reviewer / actor。若复核由 GPT/ChatGPT/Codex/其他 Agent 生成或执行，不得把它描述为 fully manual human review；应分别记录人类回答、批准或抽样核验了哪些部分，以及哪些步骤仍由模型完成。
- 当任务修改执行源时，result record 必须显式记录 `user_decision_recorded: true | false`、用户决定的 evidence path / conversation provenance、获批修改范围和仍未获批的相邻动作；不得用平台 permission、历史授权或推测替代当前用户决定。
- 同一模型家族完成执行与复核不会自动使结果无效，但必须标注 evidence class / independence limitation；高风险结论应优先补充异构复核、机械 diff、可复现测试或人类抽样验证。
- 本原则不自动批准任何 validation、dry-run、target workspace、material ingestion、target write、regression formalization、operational build、execution-source update、自动写回或自动合并。
