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
- 本原则本身不授权任何仓库编辑；它只指导长转发内容应如何打包和交付。

## 14. Manual import inbox / Codex Cloud non-image attachment boundary

- Current Codex Cloud task conversations cannot be assumed to receive non-image file attachments directly.
- When non-image files need to enter the repository, the user may manually place them in the repository.
- The preferred staging location for manually uploaded batches is `manual-import-inbox/`.
- Files in `manual-import-inbox/` are temporary transfer artifacts only.
- Files in `manual-import-inbox/` are not execution source, not raw evidence, not canonical research originals, and not target-project delivery artifacts until verified and moved/copied to canonical paths.
- ChatGPT/Codex tasks must verify file presence, names, types, and intended destination before processing.
- ChatGPT/Codex tasks must not assume they can detect manual file additions in real time; the user must notify the task/conversation after upload.
- If files are missing or ambiguous, the task must stop or ask for correction rather than guessing.
- This rule is based on current tool/platform behavior and may be revised if Codex Cloud attachment capability changes.
