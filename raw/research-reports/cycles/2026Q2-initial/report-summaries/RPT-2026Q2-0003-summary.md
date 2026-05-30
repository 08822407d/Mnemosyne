# Report Summary: RPT-2026Q2-0003

## 文件定位

- 本文件是研究报告摘要，不是原始报告；
- 本文件不是执行源；
- 当前执行源仍是 `current/human-approved-spec.md`；
- 如果本摘要与原始报告冲突，应以原始报告为证据来源，并登记 review note；
- 如果本摘要与 `human-approved-spec` 冲突，应以 `human-approved-spec` 为执行准则。

## 元数据

- report_id: RPT-2026Q2-0003
- source_file: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 2：ChatGPT,Claude 纯对话场景的外部记忆能力边界.pdf
- cycle_id: RC-2026Q2-initial
- report_type: light
- topic: ChatGPT / Claude 纯对话场景的外部记忆能力边界
- readability: PDF 文本可抽取；摘要仅基于可读取文本，图表 / 图片 / 版式未复核。
- summary_status: completed_from_readable_pdf_text
- figure_review_status: pending_manual_review
- created_by_task: MNEMOSYNE-030

## 摘要

本报告的核心结论是：在纯 Web / App 对话入口下，ChatGPT 和 Claude 对外部持久记忆的自动化能力非常有限。它们可以通过上传文件、Projects、项目知识库、连接器或 Apps 获取外部信息，也可以在部分 Agent / Apps 模式中经授权与确认执行写入动作；但标准纯对话过程不能默认自动拉取指定 memory 文件，也不能默认在对话结束后自动写回 GitHub 或外部数据库。ChatGPT GitHub app / connector 更适合读取、搜索和分析仓库，而不是提交更新；Claude Projects 能组织知识库和对话，但写回外部仓库仍需人工或工具链。

## 关键结论

- 纯对话入口下的外部记忆维护应定义为手动或半自动。
- 项目 / Projects 可提供主题级上下文容器，但不能替代后台持久存储和版本治理。
- 写回 GitHub、数据库或外部文件通常需要 Codex、API、MCP、脚本、外部工具或用户手动操作。
- 用户确认、授权和隐私控制是纯对话外部记忆能力的关键边界。

## 对 Mnemosyne 设计的影响

支持 Mnemosyne 在目标项目模板中显式记录期望 AI 工具、工具权限、写回方式和 unsupported assumptions。

## 对能力边界的影响

不应默认普通 ChatGPT / Claude 能自动写回目标项目仓库；普通对话生成的更新应由用户复制、确认或交给具备文件写入能力的工具执行。

## 对目标项目模板 / delivery manifest 的影响

delivery manifest 应区分 Mnemosyne 设计档案与目标项目运行真相源，并列出人工设置步骤与不可自动化前提。

## 风险与限制

- PDF 图表 / 图片 / 版式未复核。
- 产品能力随时间变化，尤其是 Agent / Apps / Connectors / Projects。
- 写入外部系统可能涉及管理员权限、用户确认和隐私风险。

## 需要人工复核的内容

图表 / 图片 / 版式相关内容仍需人工复核；若后续依赖具体产品限制或流程图，应先复核。

## 可引用锚点

- 总体结论
- ChatGPT 能力边界
- Claude 能力边界
- 纯对话可半自动完成的步骤
- 需要 API / MCP / 脚本 / 外部工具的步骤

## open questions / review notes

- 本摘要需要用户 review。
- 本摘要不得直接升级为执行源或最终规范。
- 如后续目标项目设计依赖本报告中的具体产品能力、表格、图示、图片或引用编号，应回查原始报告；PDF 报告还必须先完成人工图表 / 图片 / 版式复核。
