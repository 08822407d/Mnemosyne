# Candidate Requirements

> 说明：以下为从交接记录抽取的候选需求，不等同于最终实施版。

## CAND-0010
- 标题：Mnemosyne 作为记忆系统元 Agent
- 状态：reflected
- 说明：仓库定位是“记忆系统架构师”工作空间，不是单一项目记忆库。
- 来源引用：RAW-0003
- 已反映到 human-approved-spec.md：是

## CAND-0011
- 标题：采用冯诺伊曼式外部记忆架构
- 状态：reflected
- 说明：模型负责计算，外部文件 / Git 仓库负责长期记忆与审计。
- 来源引用：RAW-0003
- 已反映到 human-approved-spec.md：是

## CAND-0012
- 标题：原文保存为长期证据
- 状态：reflected
- 说明：需求与反馈原文长期保留，用于迁移复查与意图还原。
- 来源引用：RAW-0003
- 已反映到 human-approved-spec.md：是

## CAND-0013
- 标题：Human-Approved Spec 作为唯一执行源
- 状态：reflected
- 说明：原文、候选需求、模型摘要均非执行源。
- 来源引用：RAW-0003
- 已反映到 human-approved-spec.md：是

## CAND-0014
- 标题：新需求必须查重并输出差异说明
- 状态：reflected
- 说明：进入实施版前需比对历史想法/需求/决策，形成可审阅差异说明并等待用户确认。
- 来源引用：RAW-0003
- 已反映到 human-approved-spec.md：是

## CAND-0015
- 标题：模型迁移复审机制（model migration review）
- 状态：todo
- 说明：模型升级时需基于旧加工版与原文证据做选择性回查与约束复审。
- 来源引用：RAW-0003
- 已反映到 human-approved-spec.md：否（仅 TODO）

## CAND-0016
- 标题：Idea Capture Buffer 作为未来功能
- 状态：todo
- 说明：临时点子速记池为后续功能，当前仅保留设计任务。
- 来源引用：RAW-0003
- 已反映到 human-approved-spec.md：否（仅 TODO）

## CAND-0017
- 标题：第一阶段坚持半自动流程
- 状态：reflected
- 说明：手工 ChatGPT 对话澄清 + Codex Cloud 小步写入 + 用户 review。
- 来源引用：RAW-0003
- 已反映到 human-approved-spec.md：是

## CAND-0018
- 标题：Codex Cloud 作为远程保存助手
- 状态：reflected
- 说明：当前仅承担远程文件写入与版本保存，不承担自动化系统实现。
- 来源引用：RAW-0003
- 已反映到 human-approved-spec.md：是


## CAND-0019
- 标题：建立 Mnemosyne 核心对象模型
- 状态：reflected
- 说明：需要统一对象用途、字段、状态、关系和更新原则，避免仓库散乱。
- 来源引用：RAW-0004
- 是否已反映到 notes/core-object-model.md 或 human-approved-spec.md：是（core-object-model + human-approved-spec）

## CAND-0020
- 标题：Raw Record 必须作为证据源而非执行源
- 状态：reflected
- 说明：Raw Record 用于保存原文证据，不能直接作为执行依据。
- 来源引用：RAW-0004
- 是否已反映到 notes/core-object-model.md 或 human-approved-spec.md：是（两者均已体现）

## CAND-0021
- 标题：Human-Approved Spec Entry 必须作为执行源
- 状态：reflected
- 说明：实施规则必须由人类确认后生效，执行时以 Approved Spec 为准。
- 来源引用：RAW-0004
- 是否已反映到 notes/core-object-model.md 或 human-approved-spec.md：是（两者均已体现）

## CAND-0022
- 标题：Candidate Requirement 必须引用来源
- 状态：reflected
- 说明：候选需求应可追溯到 raw 或其他证据来源，避免无来源结论。
- 来源引用：RAW-0004
- 是否已反映到 notes/core-object-model.md 或 human-approved-spec.md：是（core-object-model 已定义）

## CAND-0023
- 标题：新需求进入实施版前需要 Similarity / Conflict Report
- 状态：pending
- 说明：查重与差异报告应作为实施前步骤，但报告格式仍待定。
- 来源引用：RAW-0004
- 是否已反映到 notes/core-object-model.md 或 human-approved-spec.md：部分（原则已反映，模板未定）

## CAND-0024
- 标题：Handoff 必须保持短上下文，不复制完整历史
- 状态：reflected
- 说明：handoff 用于快速恢复当前状态，应引用关键对象而不是拷贝全部原文。
- 来源引用：RAW-0004
- 是否已反映到 notes/core-object-model.md 或 human-approved-spec.md：是（core-object-model 已定义）

## CAND-0025
- 标题：Model-Specific Digest 作为未来对象
- 状态：todo
- 说明：未来用于模型迁移与多工具适配的压缩视图，当前阶段不实现。
- 来源引用：RAW-0004
- 是否已反映到 notes/core-object-model.md 或 human-approved-spec.md：是（core-object-model 标记为未来对象）

## CAND-0026
- 标题：Delivery Manifest 作为未来交付对象
- 状态：todo
- 说明：未来用于面向具体目标项目的交付记录与假设管理，当前阶段不实现。
- 来源引用：RAW-0004
- 是否已反映到 notes/core-object-model.md 或 human-approved-spec.md：是（core-object-model 标记为未来对象）


## CAND-0027
- 标题：Mnemosyne 需要对象模板
- 状态：reflected
- 说明：需要统一 Raw/Candidate/Decision/Spec/Handoff 等对象写法，减少手工维护偏差。
- 来源引用：RAW-0005
- 是否已反映到 object-templates-and-id-rules.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0028
- 标题：Mnemosyne 需要基础 ID 规则
- 状态：reflected
- 说明：通过前缀 + 编号规则保证对象可追溯与可审阅。
- 来源引用：RAW-0005
- 是否已反映到 object-templates-and-id-rules.md 或 human-approved-spec.md：是（object-templates 已反映）

## CAND-0029
- 标题：Mnemosyne 需要状态值规则
- 状态：reflected
- 说明：对象状态应保持简洁稳定，降低跨阶段歧义。
- 来源引用：RAW-0005
- 是否已反映到 object-templates-and-id-rules.md 或 human-approved-spec.md：是（object-templates 已反映）

## CAND-0030
- 标题：派生对象应保留 source_refs
- 状态：reflected
- 说明：由 raw 或其他对象派生出的条目应尽量携带来源引用。
- 来源引用：RAW-0005
- 是否已反映到 object-templates-and-id-rules.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0031
- 标题：Human-Approved Spec Entry 是唯一执行源
- 状态：reflected
- 说明：其余对象均不直接作为执行依据。
- 来源引用：RAW-0005
- 是否已反映到 object-templates-and-id-rules.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0032
- 标题：当前不实现自动 ID、自动校验、自动查重
- 状态：reflected
- 说明：当前阶段只定义模板与规则，不做自动化实现。
- 来源引用：RAW-0005
- 是否已反映到 object-templates-and-id-rules.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0033
- 标题：未来可将模板拆分到 templates/ 目录
- 状态：todo
- 说明：待模板稳定后再评估目录拆分与维护成本。
- 来源引用：RAW-0005
- 是否已反映到 object-templates-and-id-rules.md 或 human-approved-spec.md：部分（作为未来方向记录）

## CAND-0034
- 标题：未来可用 GitHub Actions 做轻量检查
- 状态：todo
- 说明：可在后续阶段对模板一致性进行轻量校验，当前不实现。
- 来源引用：RAW-0005
- 是否已反映到 object-templates-and-id-rules.md 或 human-approved-spec.md：部分（作为未来方向记录）


## CAND-0035
- 标题：Mnemosyne 需要需求进入流程
- 状态：reflected
- 说明：应定义新需求从 raw 到 candidate、similarity report、用户确认、spec 更新的流程。
- 来源引用：RAW-0006
- 是否已反映到 requirement-intake-workflow.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0036
- 标题：新输入必须先保存为 Raw Record
- 状态：reflected
- 说明：任何新需求、反馈或想法应先入证据层。
- 来源引用：RAW-0006
- 是否已反映到 requirement-intake-workflow.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0037
- 标题：新输入应抽取为 Candidate Requirement
- 状态：reflected
- 说明：Raw 输入应转为候选需求以便后续比较与决策。
- 来源引用：RAW-0006
- 是否已反映到 requirement-intake-workflow.md 或 human-approved-spec.md：是（requirement-intake 已反映）

## CAND-0038
- 标题：新候选进入实施版前必须经过查重和对比
- 状态：reflected
- 说明：进入执行层前要与历史对象进行相似/冲突分析。
- 来源引用：RAW-0006
- 是否已反映到 requirement-intake-workflow.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0039
- 标题：Similarity / Conflict Report 应向用户展示差异
- 状态：reflected
- 说明：报告应可审阅地呈现重复、相似、冲突与建议动作。
- 来源引用：RAW-0006
- 是否已反映到 requirement-intake-workflow.md 或 human-approved-spec.md：是（requirement-intake 已反映）

## CAND-0040
- 标题：用户确认是更新 Human-Approved Spec 的必要条件
- 状态：reflected
- 说明：模型只能建议，不能替用户静默决定。
- 来源引用：RAW-0006
- 是否已反映到 requirement-intake-workflow.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0041
- 标题：上游 Agent 转交需求必须走同一流程
- 状态：reflected
- 说明：来源不同不改变流程约束，仍需 raw/candidate/compare/decide/apply。
- 来源引用：RAW-0006
- 是否已反映到 requirement-intake-workflow.md 或 human-approved-spec.md：是（requirement-intake 已反映）

## CAND-0042
- 标题：临时点子速记未来应进入 Idea Capture Buffer
- 状态：todo
- 说明：当前仅记录方向，后续再与正式流程衔接。
- 来源引用：RAW-0006
- 是否已反映到 requirement-intake-workflow.md 或 human-approved-spec.md：部分（流程文档已占位）

## CAND-0043
- 标题：当前不实现自动查重和自动写回
- 状态：reflected
- 说明：第六阶段只做流程设计与手工半自动执行。
- 来源引用：RAW-0006
- 是否已反映到 requirement-intake-workflow.md 或 human-approved-spec.md：是（两者均已反映）


## CAND-0044
- 标题：Mnemosyne 需要 active-context
- 状态：reflected
- 说明：需要稳定维护当前工作集以支持跨会话接手。
- 来源引用：RAW-0007
- 是否已反映到 handoff-active-context-review.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0045
- 标题：Mnemosyne 需要 handoff-current
- 状态：reflected
- 说明：需要为新会话启动提供最小交接卡。
- 来源引用：RAW-0007
- 是否已反映到 handoff-active-context-review.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0046
- 标题：active-context 是当前工作集，不是执行源
- 状态：reflected
- 说明：active-context 仅用于短期工作上下文恢复。
- 来源引用：RAW-0007
- 是否已反映到 handoff-active-context-review.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0047
- 标题：handoff-current 是跨会话交接卡，不是完整历史
- 状态：reflected
- 说明：handoff 应最小化并通过路径引用细节。
- 来源引用：RAW-0007
- 是否已反映到 handoff-active-context-review.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0048
- 标题：未来 AI 会话应按推荐顺序读取关键文件
- 状态：reflected
- 说明：先读执行源与上下文，再读模型与流程，最后按需回查 raw。
- 来源引用：RAW-0007
- 是否已反映到 handoff-active-context-review.md 或 human-approved-spec.md：是（handoff-active-context-review 已反映）

## CAND-0049
- 标题：阶段性回顾应在关键场景触发
- 状态：reflected
- 说明：包括阶段结束、模型切换、工具切换、长期暂停后恢复等。
- 来源引用：RAW-0007
- 是否已反映到 handoff-active-context-review.md 或 human-approved-spec.md：是（handoff-active-context-review 已反映）

## CAND-0050
- 标题：回顾结果不能直接覆盖 human-approved-spec
- 状态：reflected
- 说明：回顾结果是建议与检查材料，执行仍以实施版为准。
- 来源引用：RAW-0007
- 是否已反映到 handoff-active-context-review.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0051
- 标题：handoff/active-context 与实施版冲突时以实施版为准
- 状态：reflected
- 说明：发现冲突应登记 open question 并后续处理。
- 来源引用：RAW-0007
- 是否已反映到 handoff-active-context-review.md 或 human-approved-spec.md：是（两者均已反映）


## CAND-0052
- 标题：Mnemosyne 需要模型迁移机制
- 状态：reflected
- 说明：需要在模型升级或工具切换时稳定继承并复审历史成果。
- 来源引用：RAW-0008
- 是否已反映到 model-migration-and-constraint-lifecycle.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0053
- 标题：模型迁移默认继承 Canonical Memory
- 状态：reflected
- 说明：迁移应以模型无关正式记忆层作为默认基线。
- 来源引用：RAW-0008
- 是否已反映到 model-migration-and-constraint-lifecycle.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0054
- 标题：模型迁移不默认全量重分析 raw
- 状态：reflected
- 说明：应控制成本并避免无必要重建，优先使用分级回查策略。
- 来源引用：RAW-0008
- 是否已反映到 model-migration-and-constraint-lifecycle.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0055
- 标题：高风险内容需要关键原文回查
- 状态：reflected
- 说明：高价值、低置信度、曾被纠正、涉及边界的内容应按需回查 raw。
- 来源引用：RAW-0008
- 是否已反映到 model-migration-and-constraint-lifecycle.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0056
- 标题：约束需要生命周期状态
- 状态：reflected
- 说明：约束应有 active/deprecated/replaced 等状态，支持升级复审。
- 来源引用：RAW-0008
- 是否已反映到 model-migration-and-constraint-lifecycle.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0057
- 标题：旧模型专用补丁在升级时需要复审
- 状态：reflected
- 说明：避免旧模型能力补丁长期固化为通用规则。
- 来源引用：RAW-0008
- 是否已反映到 model-migration-and-constraint-lifecycle.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0058
- 标题：新模型能力验证后再启用
- 状态：reflected
- 说明：不能默认新模型一定更可靠，需小规模验证。
- 来源引用：RAW-0008
- 是否已反映到 model-migration-and-constraint-lifecycle.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0059
- 标题：Model-Specific Digest 未来用于模型与工具适配
- 状态：todo
- 说明：当前仅定义方向，未来再落地到模板与流程。
- 来源引用：RAW-0008
- 是否已反映到 model-migration-and-constraint-lifecycle.md 或 human-approved-spec.md：是（迁移文档已反映为未来对象）

## CAND-0060
- 标题：模型迁移中新需求仍走需求进入流程
- 状态：reflected
- 说明：迁移过程中出现的新反馈与建议仍需走 intake workflow。
- 来源引用：RAW-0008
- 是否已反映到 model-migration-and-constraint-lifecycle.md 或 human-approved-spec.md：是（两者均已反映）


## CAND-0061
- 标题：Mnemosyne 需要面向目标项目的交付包流程
- 状态：reflected
- 说明：需要定义从设计到交付、再到反馈迭代的结构化流程。
- 来源引用：RAW-0009
- 是否已反映到 delivery-package-workflow.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0062
- 标题：Mnemosyne 仓库是设计工厂和设计档案
- 状态：reflected
- 说明：用于沉淀跨项目设计、决策、模板和交付记录。
- 来源引用：RAW-0009
- 是否已反映到 delivery-package-workflow.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0063
- 标题：目标项目仓库或目录是运行真相源
- 状态：reflected
- 说明：交付后应以目标项目运行文件为准，不保持冲突双真相。
- 来源引用：RAW-0009
- 是否已反映到 delivery-package-workflow.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0064
- 标题：交付包应包含 Memory System Design Spec
- 状态：reflected
- 说明：作为目标项目记忆系统设计总说明。
- 来源引用：RAW-0009
- 是否已反映到 delivery-package-workflow.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0065
- 标题：交付包应包含 Target Project Memory Package
- 状态：reflected
- 说明：列出目标项目实际要放置的运行文件清单。
- 来源引用：RAW-0009
- 是否已反映到 delivery-package-workflow.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0066
- 标题：交付包应包含 Delivery Manifest
- 状态：reflected
- 说明：用于记录交付版本、路径、包含项、排除项和人工步骤。
- 来源引用：RAW-0009
- 是否已反映到 delivery-package-workflow.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0067
- 标题：交付包应记录 Unsupported Assumptions
- 状态：reflected
- 说明：明确当前能力边界，避免隐式承诺。
- 来源引用：RAW-0009
- 是否已反映到 delivery-package-workflow.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0068
- 标题：交付后需要 Drift Review
- 状态：pending
- 说明：需复查目标项目运行文件与 Mnemosyne 设计档案的偏离。
- 来源引用：RAW-0009
- 是否已反映到 delivery-package-workflow.md 或 human-approved-spec.md：部分（原则已反映，模板待定）

## CAND-0069
- 标题：不同目标项目类型需要不同记忆系统 schema
- 状态：pending
- 说明：软件开发、学习、研究等场景应采用不同结构。
- 来源引用：RAW-0009
- 是否已反映到 delivery-package-workflow.md 或 human-approved-spec.md：部分（方向已反映，模板待定）

## CAND-0070
- 标题：目标项目反馈应回到 requirement intake workflow
- 状态：reflected
- 说明：交付后新反馈仍需经过 raw/candidate/similarity/确认流程。
- 来源引用：RAW-0009
- 是否已反映到 delivery-package-workflow.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0071
- 标题：当前不自动交付、不自动同步、不自动 drift 检查
- 状态：reflected
- 说明：第九阶段只定义交付机制草案，不实现自动化。
- 来源引用：RAW-0009
- 是否已反映到 delivery-package-workflow.md 或 human-approved-spec.md：是（两者均已反映）


## CAND-0072
- 标题：Mnemosyne 需要 v0.1 收束与一致性检查
- 状态：reflected
- 说明：在前九阶段基础上明确 v0.1 边界，避免机制无限扩散。
- 来源引用：RAW-0010
- 是否已反映到 v0.1-scope-and-consistency-check.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0073
- 标题：v0.1 需要明确包含与不包含范围
- 状态：reflected
- 说明：已纳入机制与延期能力需明确区分，避免误判为已实现。
- 来源引用：RAW-0010
- 是否已反映到 v0.1-scope-and-consistency-check.md 或 human-approved-spec.md：是（两者均已反映）

## CAND-0074
- 标题：v0.2 方向应由用户 review v0.1 后选择
- 状态：pending
- 说明：下一阶段优先级应由用户基于 v0.1 收束结果决定。
- 来源引用：RAW-0010
- 是否已反映到 v0.1-scope-and-consistency-check.md 或 human-approved-spec.md：部分（方向已记录，待用户决策）

## CAND-0075
- 标题：需要保存早期核心构想来源摘录
- 状态：reflected
- 说明：将“近原文核心构想与讨论摘录 v2”保存为 raw 证据层文件，供后续回查。
- 来源引用：RAW-0011 / raw/concept-origin-extract-001.md
- 是否已反映到相关文件：是（raw/concept-origin-extract-001.md）

## CAND-0076
- 标题：近原文摘录必须标明不是完整 transcript
- 状态：reflected
- 说明：避免将近原文摘录误解为完整逐字对话记录。
- 来源引用：RAW-0011 / raw/concept-origin-extract-001.md
- 是否已反映到相关文件：是（raw/concept-origin-extract-001.md）

## CAND-0077
- 标题：近原文摘录属于 raw 证据层且不是执行源
- 状态：reflected
- 说明：该摘录用于证据回查，不能替代 current/human-approved-spec.md。
- 来源引用：RAW-0011 / raw/concept-origin-extract-001.md
- 是否已反映到相关文件：是（raw/concept-origin-extract-001.md 与 current/active-context.md）

## CAND-0078
- 标题：应尽量保留用户提出构想时的理由、担忧和取舍
- 状态：reflected
- 说明：保证后续模型迁移、需求复核和设计解释有完整动机上下文。
- 来源引用：RAW-0011 / raw/concept-origin-extract-001.md
- 是否已反映到相关文件：是（raw/concept-origin-extract-001.md）

## CAND-0079
- 标题：未来迁移、复核、查重与回顾可按需回查该摘录
- 状态：pending
- 说明：在模型迁移、需求复核和冲突分析中，按需读取该 raw 摘录作为证据补强。
- 来源引用：RAW-0011 / raw/concept-origin-extract-001.md
- 是否已反映到相关文件：部分（current/active-context.md 与 handoff/handoff-current.md 已反映）

## CAND-0080
- 标题：若摘录与 human-approved-spec 冲突应以实施版为准
- 状态：reflected
- 说明：冲突需登记 open question，不得由摘录直接覆盖执行源。
- 来源引用：RAW-0011 / raw/concept-origin-extract-001.md
- 是否已反映到相关文件：是（raw/concept-origin-extract-001.md）
