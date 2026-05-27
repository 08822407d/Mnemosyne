# Decision Log

## DEC-0008
- 决策：将 Mnemosyne 定位为记忆系统元 Agent，而不是具体项目记忆库。
- 理由：目标是为不同场景设计与交付外部记忆系统，避免仓库定位过窄。
- 状态：accepted
- 来源引用：RAW-0003

## DEC-0009
- 决策：采用“模型负责计算，文件负责记忆”的外部记忆架构。
- 理由：确保关键状态外部化、可审查、可回滚，降低模型内部记忆不稳定性风险。
- 状态：accepted
- 来源引用：RAW-0003

## DEC-0010
- 决策：将原文证据层与实施版执行层严格分离。
- 理由：保留原始意图证据，同时避免原文噪声直接进入执行。
- 状态：accepted
- 来源引用：RAW-0003

## DEC-0011
- 决策：将 Human-Approved Spec 设为当前唯一执行源。
- 理由：统一执行依据，降低并行文档解释冲突。
- 状态：accepted
- 来源引用：RAW-0003

## DEC-0012
- 决策：新需求进入实施版前必须查重并对比历史版本。
- 理由：后提出想法不一定更优，需通过差异说明与用户决策降低误覆盖。
- 状态：accepted
- 来源引用：RAW-0003

## DEC-0013
- 决策：第一阶段不做全自动，仅采用半自动小步保存。
- 理由：当前优先固化核心设计状态与审阅机制，避免过早工程化。
- 状态：accepted
- 来源引用：RAW-0003

## DEC-0014
- 决策：当前不创建 AGENTS.md、CLAUDE.md 和 GitHub Actions。
- 理由：相关能力属于后续设计事项，当前阶段只做最小可审阅固化。
- 状态：accepted
- 来源引用：RAW-0003


## DEC-0015
- 决策：建立 `notes/core-object-model.md` 作为核心对象模型草案文档。
- 理由：统一对象边界和关系，降低后续文档演化歧义。
- 状态：accepted
- 来源引用：RAW-0004

## DEC-0016
- 决策：明确区分 Raw Record、Candidate Requirement、Human-Approved Spec Entry。
- 理由：保证证据层、候选层、执行层分离，避免未经确认内容直接执行。
- 状态：accepted
- 来源引用：RAW-0004

## DEC-0017
- 决策：将 Human-Approved Spec Entry 设为执行源。
- 理由：执行依据必须稳定、可追溯且经用户确认。
- 状态：accepted
- 来源引用：RAW-0004

## DEC-0018
- 决策：当前阶段暂不实现自动 ID、自动查重、自动索引和 schema 校验。
- 理由：先固化对象模型与人工审阅流程，避免过早自动化引入复杂度。
- 状态：accepted
- 来源引用：RAW-0004

## DEC-0019
- 决策：将 Model-Specific Digest 和 Delivery Manifest 暂列为未来对象。
- 理由：两者对交付和迁移重要，但当前阶段先做定义不做实现。
- 状态：accepted
- 来源引用：RAW-0004


## DEC-0020
- 决策：建立 `notes/object-templates-and-id-rules.md` 作为模板与规则草案文档。
- 理由：统一对象填写方式，降低人工维护不一致问题。
- 状态：accepted
- 来源引用：RAW-0005

## DEC-0021
- 决策：当前使用简单 ID 前缀规则（前缀 + 四位数字）。
- 理由：先满足可读与可追溯，避免过早引入复杂编号系统。
- 状态：accepted
- 来源引用：RAW-0005

## DEC-0022
- 决策：当前不实现自动 ID 生成。
- 理由：本阶段聚焦模板草案与人工流程，不做自动化开发。
- 状态：accepted
- 来源引用：RAW-0005

## DEC-0023
- 决策：当前不创建 `templates/` 目录。
- 理由：先验证单文件模板草案稳定性，避免目录结构过早膨胀。
- 状态：accepted
- 来源引用：RAW-0005

## DEC-0024
- 决策：所有派生对象尽量保留 `source_refs`。
- 理由：保证证据可追溯，支持后续模型迁移与人工复核。
- 状态：accepted
- 来源引用：RAW-0005

## DEC-0025
- 决策：仅 Human-Approved Spec Entry 作为执行源。
- 理由：避免候选、分析、交接材料被误用为执行依据。
- 状态：accepted
- 来源引用：RAW-0005

## DEC-0026
- 决策：未来待模板稳定后再考虑自动化校验（含 GitHub Actions 选项）。
- 理由：当前阶段先稳住内容规范，再评估自动化性价比。
- 状态：accepted
- 来源引用：RAW-0005


## DEC-0027
- 决策：建立 `notes/requirement-intake-workflow.md` 作为需求进入流程草案。
- 理由：为新需求处理提供统一路径，避免直接写入执行源。
- 状态：accepted
- 来源引用：RAW-0006

## DEC-0028
- 决策：所有新需求先进入 Raw Record。
- 理由：先保留证据，再进行候选提炼和对比分析。
- 状态：accepted
- 来源引用：RAW-0006

## DEC-0029
- 决策：Candidate Requirement 不是执行源。
- 理由：候选内容可能存在误解或阶段性想法，需人工确认。
- 状态：accepted
- 来源引用：RAW-0006

## DEC-0030
- 决策：进入 Human-Approved Spec 前必须经过用户确认。
- 理由：确保执行层稳定且符合用户真实意图。
- 状态：accepted
- 来源引用：RAW-0006

## DEC-0031
- 决策：Similarity / Conflict Report 只提供分析和建议，不替用户决定。
- 理由：模型建议应受人工审阅，避免静默覆盖旧规则。
- 状态：accepted
- 来源引用：RAW-0006

## DEC-0032
- 决策：上游 Agent 转交需求也必须走同一需求进入流程。
- 理由：统一来源处理规则，保持可追溯与一致性。
- 状态：accepted
- 来源引用：RAW-0006

## DEC-0033
- 决策：当前不实现自动查重、自动写回或自动索引。
- 理由：第六阶段聚焦流程定义，不引入自动化系统复杂度。
- 状态：accepted
- 来源引用：RAW-0006


## DEC-0034
- 决策：建立 `notes/handoff-active-context-review.md`。
- 理由：统一跨会话交接与阶段回顾机制，降低接手成本。
- 状态：accepted
- 来源引用：RAW-0007

## DEC-0035
- 决策：区分 active-context 与 handoff-current 的职责。
- 理由：前者服务当前工作集，后者服务新会话启动。
- 状态：accepted
- 来源引用：RAW-0007

## DEC-0036
- 决策：active-context 与 handoff-current 均不是执行源。
- 理由：执行依据应稳定在 human-approved-spec，避免上下文材料越权。
- 状态：accepted
- 来源引用：RAW-0007

## DEC-0037
- 决策：未来 AI 会话优先读取 human-approved-spec、active-context、handoff。
- 理由：先建立执行边界和当前状态，再进入细节文档。
- 状态：accepted
- 来源引用：RAW-0007

## DEC-0038
- 决策：raw 只按需回查，不默认全量读取。
- 理由：控制上下文负载，避免低效读取和噪声干扰。
- 状态：accepted
- 来源引用：RAW-0007

## DEC-0039
- 决策：阶段性回顾当前只手工触发，不自动化。
- 理由：现阶段先验证回顾机制有效性，再评估自动化。
- 状态：accepted
- 来源引用：RAW-0007

## DEC-0040
- 决策：handoff/active-context 与 human-approved-spec 冲突时以后者为准。
- 理由：保持执行源唯一性，并通过 open question 管理冲突。
- 状态：accepted
- 来源引用：RAW-0007


## DEC-0041
- 决策：建立 `notes/model-migration-and-constraint-lifecycle.md`。
- 理由：集中定义模型迁移与约束复审原则，避免迁移过程失控。
- 状态：accepted
- 来源引用：RAW-0008

## DEC-0042
- 决策：模型迁移默认继承 Canonical Memory。
- 理由：以已确认正式记忆为基线，减少重建成本与偏差。
- 状态：accepted
- 来源引用：RAW-0008

## DEC-0043
- 决策：不默认全量重分析 raw。
- 理由：全量回读成本高且不总能提升质量。
- 状态：accepted
- 来源引用：RAW-0008

## DEC-0044
- 决策：关键内容按需回查 raw。
- 理由：对高风险、高价值、争议内容保持证据核实能力。
- 状态：accepted
- 来源引用：RAW-0008

## DEC-0045
- 决策：引入约束生命周期状态。
- 理由：区分长期原则与模型专用补丁，支持升级复审。
- 状态：accepted
- 来源引用：RAW-0008

## DEC-0046
- 决策：新模型能力验证后再启用。
- 理由：不假设新模型天然更可靠，先小规模验证。
- 状态：accepted
- 来源引用：RAW-0008

## DEC-0047
- 决策：Model-Specific Digest 当前仍作为未来对象。
- 理由：先固化迁移原则，后续再实施摘要对象。
- 状态：accepted
- 来源引用：RAW-0008

## DEC-0048
- 决策：模型迁移中新出现的需求仍走需求进入流程。
- 理由：保持执行源更新闸门一致，避免迁移通道绕过确认流程。
- 状态：accepted
- 来源引用：RAW-0008


## DEC-0049
- 决策：建立 `notes/delivery-package-workflow.md`。
- 理由：统一面向目标项目的交付结构与流程。
- 状态：accepted
- 来源引用：RAW-0009

## DEC-0050
- 决策：采用双层仓库原则。
- 理由：区分设计工厂与运行真相源，避免角色混淆。
- 状态：accepted
- 来源引用：RAW-0009

## DEC-0051
- 决策：Mnemosyne 仓库保存设计原本和交付档案。
- 理由：保障跨项目复用、追溯与演进管理。
- 状态：accepted
- 来源引用：RAW-0009

## DEC-0052
- 决策：目标项目仓库或目录保存运行真相源。
- 理由：运行期应以目标项目实际文件为准。
- 状态：accepted
- 来源引用：RAW-0009

## DEC-0053
- 决策：交付包必须包含 Delivery Manifest。
- 理由：提高交付可审计性，明确包含/排除项与人工步骤。
- 状态：accepted
- 来源引用：RAW-0009

## DEC-0054
- 决策：交付后需要进行 drift review。
- 理由：识别运行文件与设计档案偏离并决定是否回收。
- 状态：accepted
- 来源引用：RAW-0009

## DEC-0055
- 决策：不同目标项目类型需要不同记忆系统设计。
- 理由：场景差异导致记忆对象和流程不同，不能强行统一。
- 状态：accepted
- 来源引用：RAW-0009

## DEC-0056
- 决策：当前不实现自动交付或自动同步。
- 理由：先稳定交付模型与手工审阅机制，再评估自动化。
- 状态：accepted
- 来源引用：RAW-0009


## DEC-0057
- 决策：建立 `notes/v0.1-scope-and-consistency-check.md`。
- 理由：集中说明 v0.1 边界与一致性检查清单，降低认知分散。
- 状态：accepted
- 来源引用：RAW-0010

## DEC-0058
- 决策：将 v0.1 定义为最小可用设计工作仓库。
- 理由：当前目标是可读、可审查、可迭代，而非完整自动化系统。
- 状态：accepted
- 来源引用：RAW-0010

## DEC-0059
- 决策：v0.1 不包含自动化、AGENTS.md、CLAUDE.md、GitHub Actions、MCP、RAG。
- 理由：这些属于后续阶段能力，当前仅保留为 TODO/方向。
- 状态：accepted
- 来源引用：RAW-0010

## DEC-0060
- 决策：第十阶段以一致性检查与收束为主，不引入大型新机制。
- 理由：避免基础机制继续膨胀，优先形成稳定 v0.1 基线。
- 状态：accepted
- 来源引用：RAW-0010

## DEC-0061
- 决策：v0.2 方向由用户 review v0.1 后选择。
- 理由：下一步优先级应由用户业务目标与风险偏好驱动。
- 状态：accepted
- 来源引用：RAW-0010

## DEC-0062
- 决策：将用户直接粘贴的“近原文核心构想与讨论摘录 v2”保存为 raw 证据层文件 `raw/concept-origin-extract-001.md`。
- 理由：该内容包含早期构想来源、修正过程和背景动机，适合长期回查与审计。
- 状态：accepted
- 来源引用：RAW-0011

## DEC-0063
- 决策：该文件不是完整逐字 transcript。
- 理由：文件定位为“近原文核心构想摘录”，已去除几乎完全重复的回顾性段落。
- 状态：accepted
- 来源引用：RAW-0011

## DEC-0064
- 决策：该文件不是执行源。
- 理由：执行源仍由 `current/human-approved-spec.md` 承担，raw 仅作为证据层。
- 状态：accepted
- 来源引用：RAW-0011

## DEC-0065
- 决策：该文件应尽量保留用户提出构想时的理由、担忧、取舍和使用体验背景。
- 理由：后续模型迁移、需求复核与冲突解释需要“为什么”的证据上下文。
- 状态：accepted
- 来源引用：RAW-0011

## DEC-0066
- 决策：未来模型迁移、需求复核和查重可按需回查该文件。
- 理由：该摘录提供近原文动机线索，可补强 candidate/decision 的证据追溯。
- 状态：accepted
- 来源引用：RAW-0011
