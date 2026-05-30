# Report Summary: RPT-2026Q2-0002

## 文件定位

- 本文件是研究报告摘要，不是原始报告；
- 本文件不是执行源；
- 当前执行源仍是 `current/human-approved-spec.md`；
- 如果本摘要与原始报告冲突，应以原始报告为证据来源，并登记 review note；
- 如果本摘要与 `human-approved-spec` 冲突，应以 `human-approved-spec` 为执行准则。

## 元数据

- report_id: RPT-2026Q2-0002
- source_file: raw/research-reports/cycles/2026Q2-initial/originals/轻度研究子课题 1：非开发长期对话记忆是否已有真实实践.pdf
- cycle_id: RC-2026Q2-initial
- report_type: light
- topic: 非开发长期对话记忆是否已有真实实践
- readability: PDF 文本可抽取；摘要仅基于可读取文本，图表 / 图片 / 版式未复核。
- summary_status: completed_from_readable_pdf_text
- figure_review_status: pending_manual_review
- created_by_task: MNEMOSYNE-030

## 摘要

本报告判断：非开发场景下的外部持久对话记忆正在兴起，但还没有形成开发者编码场景那样成熟、统一、版本化的生态。报告列举了 ChatGPT Memory / Projects / Apps、Claude Projects / Memory、Gemini / NotebookLM、Khanmigo、Classover、MemGPT、Notion 记忆方案等产品或研究实践，说明长期主题、学习档案、资料库对话和用户偏好记忆已经存在真实需求与局部实现。但这些能力多偏平台内部记忆、项目知识库、RAG 式资料库、教育平台记录或开发者自建方案，通常缺少用户可审计、可迁移、可回滚的外部 memory repo。

## 关键结论

- 非开发长期对话记忆已有真实实践，但成熟度低于开发 / coding agent 场景。
- 平台内置记忆更擅长保存偏好、项目资料和学习进度，不适合替代完整对话归档或可审计外部仓库。
- 普通用户仍常依赖手动笔记、Notebook、知识库或外部工具维护长期状态。
- 可迁移的开发经验包括文件式状态、结构化规则、handoff、任务清单和审计记录。

## 对 Mnemosyne 设计的影响

支持 Mnemosyne 把非开发场景纳入目标项目类型，但需要以半自动、可裁剪的模板处理，而不是默认全自动。

## 对能力边界的影响

普通对话与项目容器可辅助长期记忆，但不等于可审计写回；连接器和 Apps 依赖授权、外部服务和用户维护。

## 对目标项目模板 / delivery manifest 的影响

目标项目模板应覆盖个人长期对话 / 知识管理、学习系统和长期研究场景，并要求用户明确是否允许保存原文、隐私级别和外部资料来源。

## 风险与限制

- PDF 图表 / 图片 / 版式未复核。
- 产品能力和限制具有时效性。
- 个人长期对话可能含敏感信息，完整归档需谨慎。

## 需要人工复核的内容

图表 / 图片 / 版式相关内容仍需人工复核；如后续设计依赖该报告中的具体案例表格或引用编号，应先登记复核。

## 可引用锚点

- 总体结论
- 真实案例清单
- 非开发场景与开发场景的差异
- 可迁移的开发场景经验
- 尚缺成熟实践的领域

## open questions / review notes

- 本摘要需要用户 review。
- 本摘要不得直接升级为执行源或最终规范。
- 如后续目标项目设计依赖本报告中的具体产品能力、表格、图示、图片或引用编号，应回查原始报告；PDF 报告还必须先完成人工图表 / 图片 / 版式复核。
