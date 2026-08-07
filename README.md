# Mnemosyne

Mnemosyne 是一个用于设计、演化和交付 AI Agent 外部持久记忆系统的“记忆系统元 Agent”工作仓库。

这是一个设计工作仓库，不是传统软件开发项目。仓库可见性由用户控制，可能随 construction / operation 阶段在 public/private 之间变化。向仓库放入材料前必须核验当前可见性；当仓库为 public 或可见性未核实时，只允许放入公开、合成或已明确脱敏的材料。后续可见性变化不会消除既有 Git 历史暴露。

核心原则：**模型负责计算，文件负责记忆。**

当前阶段采用中文作为主要工作语言。

当前 live wayfinding：`current/post-interruption-live-wayfinding-status.md`；当前 review / validation 汇总：`current/review-and-validation-status.md`。这些文件都不是执行源；`current/human-approved-spec.md` 仍是唯一执行源。

FABLE5-GREENFIELD 最新执行偏差、续接与最终阶段交接入口：`current/fable-greenfield-execution-deviation-status.md`。最终阶段 handoff package：`handoff/fable5-greenfield-final-phase-handoff-package.md`；配套 startup prompt：`handoff/fable5-greenfield-final-phase-next-conversation-startup-prompt.md`。这些文件都不是执行源。

GitHub repository-writing 单任务单活跃 PR 谱系防护：`current/github-single-active-pr-lineage-guard.md`。PR 审查/合并回复中的合并后分支保留或可删除状态防护：`current/pr-merge-branch-disposition-guard.md`。当回复未显眼要求保留分支时，Owner 默认可在合并后删除该分支。这些文件是用户批准的行为防护与操作指南，不是独立执行源。

长 transfer artifact 文件优先交付与低风险 artifact 同回复直接生成防护：`current/artifact-delivery-and-direct-generation-guard.md`。Deep Research 单报告交付纠错：`current/deep-research-report-delivery-correction-guard.md`。这些文件不是执行源。

Deep Research、Fable-class research 与一次性外部研究/评审工作使用紧凑 UI 显示名称的行为防护：`current/external-research-display-name-guard.md`。项目缩写与已分配研究别名登记：`notes/registries/project-research-display-name-registry-v0.1.md`。Mnemosyne 采用 `MNE`，Meta-Agent 保留 `MA`；短名称不替代 canonical task ID、报告身份或运行元数据。

用户操作置顶、下一步收尾、模型能力与 Deep Research 需求预估、上下文化澄清交接和人类意图重构防护：`current/user-operation-next-step-capability-and-intent-guard.md`。研究后风险分流与架构裁决：`current/frontier-planning-clarification-handoff-adjudication-guard.md`。配套澄清模板：`notes/templates/frontier-planned-clarification-package-v0.1.md`；研究状态：`current/frontier-planning-clarification-handoff-research-status.md`；验证设计：`notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md`。这些文件不是执行源，也不自动修改任何目标项目的运行真相源。

目标项目从 Mnemosyne bootstrap workspace 迁入专属仓库的设计入口：`notes/migration-designs/meta-agent-dedicated-repository-migration-assessment-v0.1.md`。跨仓库 shadow copy、fresh-session recovery、行为等价、目标仓库 PR 与 rollback/no-dual-writer 验证设计：`notes/validation-designs/target-project-dedicated-repository-migration-and-pr-validation-v0.1.md`；迁移交接模板：`notes/templates/target-project-dedicated-repository-migration-handoff-v0.1.md`。这些材料是历史设计与方法证据，不授权重新执行已关闭的 Meta-Agent 迁移。

Meta-Agent 已完成专属仓库 target-truth cutover。当前唯一权威位置是 `08822407d/Meta-Agent@master:current/approved-spec.md`，cutover PR 为 `08822407d/Meta-Agent#3`，merge commit 为 `eb71ed350e7cf1783d73580466a3656fad2a3b69`；其 `effective_for_operational_use` 仍为 `false`。Mnemosyne PR #261（merge `c85ebba5425da4daf6f3344690778682b9f79d66`）已退役旧 truth/current/handoff/compatibility 入口；当前 Mnemosyne 分支清单仅剩 `master`。最终 closeout：`current/meta-agent-dedicated-repository-pre-migration-status.md`。旧 `target-projects/meta-agent/` 只作为历史 bootstrap、迁移证据和 rollback source，不再是 target truth 或活动 writer。

Mnemosyne 为 Meta-Agent 准备的初步持久记忆系统候选设计仍位于 `notes/memory-system-designs/meta-agent-initial-memory-system-design-v0.1.md`；配套 adoption / fresh-session / stale-state / case-feedback / no-dual-writer 验证设计位于 `notes/validation-designs/meta-agent-initial-memory-system-adoption-and-validation-v0.1.md`。该候选尚未采用或实现。仓库迁移本身不会自动启用该记忆系统，也不会授权 RAG、MCP、automation、private material、prototype、benchmark、pilot 或 operational use。

Frontier clarification validation 的 Fable 工作已由 Owner 无限期搁置，当前对话在相关记录合并后可归档。路线状态：`current/frontier-clarification-validation-handoff-status.md`；Fable 状态：`current/fable5-research-delivery-status.md`；暂停记录：`notes/route-pauses/frontier-clarification-validation-fable5-indefinite-pause-2026-08.md`；未来独立对话 receive-only 续接入口：`handoff/mnemosyne-frontier-clarification-validation-fable-resumption-package.md` 与 `handoff/mnemosyne-frontier-clarification-validation-fable-resumption-startup-prompt.md`。A1 `MNE-DR-001 验证包审计` 与 A2 `MNE-DR-002 表面威胁` 均未被选择或授权执行；quota 恢复不会自动解除暂停。

PR #231 后的 frontier clarification validation 专项 handoff package：`handoff/mnemosyne-frontier-clarification-validation-handoff-package.md`；配套 startup prompt：`handoff/mnemosyne-frontier-clarification-validation-startup-prompt.md`。该早期专项交接不覆盖 `handoff/handoff-current.md`，不接管 Meta-Agent 或 non-FABLE health-review 路线；未来 Fable 续接应优先使用上述暂停/恢复 package。

该专项的完整 public/synthetic、read-only 验证包入口：`notes/frontier-clarification-validation-package/README.md`。包内包含分离的公开场景与 hidden author keys、Q0–Q4 合同、answer ledger / escalation tests、rubric、V0 sentinel、V1 small-smoke taskbook、manifest、返回复核和执行表面决策包；当前仅为 prepared/not selected/not executed，不授权任何验证运行。

完成的 Pro/Fable 课题原文、报告身份和评审记录位于：`raw/research-reports/cycles/2026Q3-frontier-planning-clarification-handoff/`。`notes/research-prompts/` 中同名文件仅为完成态重定向，不应再次执行。

2026Q3 platform / Project memory / Apps / GitHub / surface delta 当前入口：`current/platform-context-apps-delta-status.md`。研究原件与复核位于 `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/`；均不是执行源。

Post-MNEMOSYNE-113 新维护对话交接入口：`handoff/mnemosyne-post-113-maintenance-options-handoff-package.md`。配套 startup prompt：`handoff/mnemosyne-post-113-maintenance-next-conversation-startup-prompt.md`。两者均不是执行源。
