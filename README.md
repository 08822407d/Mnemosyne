# Mnemosyne

Mnemosyne 是一个用于设计、演化和交付 AI Agent 外部持久记忆系统的“记忆系统元 Agent”工作仓库。

这是一个设计工作仓库，不是传统软件开发项目。仓库可见性由用户控制，可能随 construction / operation 阶段在 public/private 之间变化。向仓库放入材料前必须核验当前可见性；当仓库为 public 或可见性未核实时，只允许放入公开、合成或已明确脱敏的材料。后续可见性变化不会消除既有 Git 历史暴露。

核心原则：**模型负责计算，文件负责记忆。**

当前阶段采用中文作为主要工作语言。

当前 review / validation wayfinding：`current/review-and-validation-status.md`。该文件不是执行源；`current/human-approved-spec.md` 仍是唯一执行源。

FABLE5-GREENFIELD 最新执行偏差、续接与最终阶段交接入口：`current/fable-greenfield-execution-deviation-status.md`。最终阶段 handoff package：`handoff/fable5-greenfield-final-phase-handoff-package.md`；配套 startup prompt：`handoff/fable5-greenfield-final-phase-next-conversation-startup-prompt.md`。这些文件都不是执行源。

GitHub repository-writing 单任务单活跃 PR 谱系防护：`current/github-single-active-pr-lineage-guard.md`。该文件是用户批准的行为防护与操作指南，不是独立执行源。

长 transfer artifact 文件优先交付与低风险 artifact 同回复直接生成防护：`current/artifact-delivery-and-direct-generation-guard.md`。Deep Research 单报告交付纠错：`current/deep-research-report-delivery-correction-guard.md`。这些文件不是执行源。

Deep Research、Fable-class research 与一次性外部研究/评审工作使用紧凑 UI 显示名称的行为防护：`current/external-research-display-name-guard.md`。项目缩写与已分配研究别名登记：`notes/registries/project-research-display-name-registry-v0.1.md`。Mnemosyne 采用 `MNE`，Meta-Agent 保留 `MA`；短名称不替代 canonical task ID、报告身份或运行元数据。

用户操作置顶、下一步收尾、模型能力与 Deep Research 需求预估、上下文化澄清交接和人类意图重构防护：`current/user-operation-next-step-capability-and-intent-guard.md`。研究后风险分流与架构裁决：`current/frontier-planning-clarification-handoff-adjudication-guard.md`。配套澄清模板：`notes/templates/frontier-planned-clarification-package-v0.1.md`；研究状态：`current/frontier-planning-clarification-handoff-research-status.md`；验证设计：`notes/validation-designs/frontier-planning-clarification-handoff-read-only-validation-v0.1.md`。这些文件不是执行源，也不自动修改任何目标项目的运行真相源。

目标项目从 Mnemosyne bootstrap workspace 迁入专属仓库的当前设计入口：`notes/migration-designs/meta-agent-dedicated-repository-migration-assessment-v0.1.md`。跨仓库 shadow copy、fresh-session recovery、行为等价、目标仓库 PR 与 rollback/no-dual-writer 验证设计：`notes/validation-designs/target-project-dedicated-repository-migration-and-pr-validation-v0.1.md`；迁移交接模板：`notes/templates/target-project-dedicated-repository-migration-handoff-v0.1.md`。这些材料只准备迁移与验证门，不创建目标仓库、不执行 cutover，也不改变任何目标 truth source。

Meta-Agent 新建专属仓库后的迁移前状态入口：`current/meta-agent-dedicated-repository-pre-migration-status.md`。当前目标仓库为 `08822407d/Meta-Agent` 且仍为空。原 Pro 迁移准备任务因普通 GitHub connector 无法证明完整递归 tree/blob closure 而正确 fail-closed；原始结果与裁决分别位于 `notes/codex-task-results/META-AGENT-DEDICATED-REPOSITORY-MIGRATION-PREPARATION-001-blocked-result.md` 和 `notes/adjudications/meta-agent-migration-preparation-enumeration-blocker-adjudication-2026-08-06.md`。新的串行方案先由 Codex/本地 Git 执行机械 inventory：`handoff/meta-agent-dedicated-repository-mechanical-inventory-codex-task.md`，再由 Meta-Agent 专用 Pro 对话执行不重复枚举的语义 mapping resume：`handoff/meta-agent-dedicated-repository-mapping-resume-taskbook.md`。两阶段均不授权目标仓库初始化、shadow copy、PR 或 cutover。

Mnemosyne 为 Meta-Agent 准备的初步持久记忆系统候选设计：`notes/memory-system-designs/meta-agent-initial-memory-system-design-v0.1.md`；配套 adoption / fresh-session / stale-state / case-feedback / no-dual-writer 验证设计：`notes/validation-designs/meta-agent-initial-memory-system-adoption-and-validation-v0.1.md`。该设计明确保持 file-based、human-reviewed、public-safe、无 RAG/MCP/auto-writeback，并建议先完成迁移与 destination-only recovery，再通过独立 PR 决定是否采用新增 memory foundation。

run-specific 迁移前只读预检：`notes/validation-designs/meta-agent-dedicated-repository-pre-migration-run-v0.1.md`；详细 readiness assessment：`notes/migration-designs/meta-agent-pre-migration-readiness-assessment-2026-08-06.md`；早期 receive-only handoff：`handoff/meta-agent-dedicated-repository-pre-migration-test-package.md`。Mnemosyne 与专属 target repository 的长期职责分工：`notes/target-project-delivery-models/mnemosyne-to-dedicated-target-repository-operating-model-v0.1.md`。

PR #231 后的 frontier clarification validation 专项交接入口：`current/frontier-clarification-validation-handoff-status.md`；handoff package：`handoff/mnemosyne-frontier-clarification-validation-handoff-package.md`；配套 startup prompt：`handoff/mnemosyne-frontier-clarification-validation-startup-prompt.md`。该专项交接不覆盖 `handoff/handoff-current.md`，不接管 Meta-Agent 或 non-FABLE health-review 路线。

该专项的完整 public/synthetic、read-only 验证包入口：`notes/frontier-clarification-validation-package/README.md`。包内包含分离的公开场景与 hidden author keys、Q0–Q4 合同、answer ledger / escalation tests、rubric、V0 sentinel、V1 small-smoke taskbook、manifest、返回复核和执行表面决策包；当前仅为 prepared/not selected/not executed，不授权任何验证运行。

完成的 Pro/Fable 课题原文、报告身份和评审记录位于：`raw/research-reports/cycles/2026Q3-frontier-planning-clarification-handoff/`。`notes/research-prompts/` 中同名文件仅为完成态重定向，不应再次执行。

2026Q3 platform / Project memory / Apps / GitHub / surface delta 当前入口：`current/platform-context-apps-delta-status.md`。研究原件与复核位于 `raw/research-reports/cycles/2026Q3-platform-context-apps-delta/`；均不是执行源。

Post-MNEMOSYNE-113 新维护对话交接入口：`handoff/mnemosyne-post-113-maintenance-options-handoff-package.md`。配套 startup prompt：`handoff/mnemosyne-post-113-maintenance-next-conversation-startup-prompt.md`。两者均不是执行源。
