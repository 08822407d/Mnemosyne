# Report Summary: RPT-2026Q2-0004

## 文件定位

- 本文件是研究报告摘要，不是原始报告；
- 本文件不是执行源；
- 当前执行源仍是 `current/human-approved-spec.md`；
- 如果本摘要与原始报告冲突，应以原始报告为证据来源，并登记 review note；
- 如果本摘要与 `human-approved-spec` 冲突，应以 `human-approved-spec` 为执行准则。

## 元数据

- report_id: RPT-2026Q2-0004
- source_file: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 3：Codex,Claude Code,Cursor 等本地开发 Agent 的文件式记忆能力.pdf
- cycle_id: RC-2026Q2-initial
- report_type: light
- topic: Codex / Claude Code / Cursor 等本地开发 Agent 的文件式记忆能力
- readability: PDF 文本可抽取；摘要仅基于可读取文本，图表 / 图片 / 版式未复核。
- summary_status: completed_from_readable_pdf_text
- figure_review_status: pending_manual_review
- created_by_task: MNEMOSYNE-030

## 摘要

本报告讨论本地或开发环境中的 coding agent 如何读写文件式记忆。总体上，Codex、Claude Code、Cursor 等开发 Agent 更适合在仓库内读取规则文件、维护 Markdown 状态、编辑代码 / 文档、运行检查并生成可审计 diff。报告强调 AGENTS.md、CLAUDE.md、Cursor Rules、Memory Bank、项目状态文件、任务列表和 handoff 文档等机制的现实基础，同时指出这些机制不是强制安全边界，仍需权限控制、人工 review、Git 历史和团队约定。

## 关键结论

- 开发 Agent 场景是文件式长期记忆最成熟的落地点之一。
- 仓库内 Markdown / 规则文件 / 状态文件可以支持跨会话接手和可审计更新。
- 本地 Agent 能写文件并运行命令，但仍应通过 Git diff、commit、review 和权限控制治理。
- 不同工具的规则文件和记忆机制并不完全同构，需要平台适配层。

## 对 Mnemosyne 设计的影响

支持 Mnemosyne 使用 Markdown/Git 组织执行源、active context、handoff、template pack 和 task result record。

## 对能力边界的影响

Codex / Claude Code / Cursor 可作为文件写入助手，但不应视为自动正确维护长期记忆的自治系统。

## 对目标项目模板 / delivery manifest 的影响

目标项目交付包可借鉴 AGENTS.md / CLAUDE.md / rules / memory 文件布局，但创建这些文件前需用户确认目标工具和落地方式。

## 风险与限制

- PDF 图表 / 图片 / 版式未复核。
- 工具版本和权限机制变化快。
- 规则文件不能替代真正的权限隔离或人工审查。

## 需要人工复核的内容

图表 / 图片 / 版式相关内容仍需人工复核；若后续设计依赖工具对比表或能力矩阵，应先复核。

## 可引用锚点

- 总体结论
- Codex 文件读写能力
- Claude Code 规则与记忆能力
- Cursor rules / project context
- 文件式记忆设计建议
- 限制与治理要求

## open questions / review notes

- 本摘要需要用户 review。
- 本摘要不得直接升级为执行源或最终规范。
- 如后续目标项目设计依赖本报告中的具体产品能力、表格、图示、图片或引用编号，应回查原始报告；PDF 报告还必须先完成人工图表 / 图片 / 版式复核。
