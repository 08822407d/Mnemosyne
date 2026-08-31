# 任务书 · MNE-DR-029 Mnemosyne 独立对照重设计（GPT-Pro 普通对话，非深度研究）

> 本文件是一份完整任务书。请完整读取全文与全部附件后再开始；若附件缺失或本文件不完整（看不到最后一节"禁止与停止条件"），请回复"输入不完整"并停止。

```yaml
display_name: MNE-DR-029 对照设计（普）
canonical_task_id: FABLE5-REDESIGN-001-CP1
execute_in: ChatGPT 官方入口 · 新普通对话（非深度研究）· 模型选 "GPT-5.6 Pro"（选择器 Pro 档）
language: 中文
issued_by: Mnemosyne 项目（FABLE5-REDESIGN-001 轨道，2026-08-31）
independence_firewall: 本任务是与 Claude 侧设计稿的"独立对照设计"。你不会拿到、也不得请求或猜测 Claude 侧设计内容；只依据附件材料独立完成你自己的设计。
```

## 1. 任务

你是 GPT-5.6 Pro，受项目 Owner 委托，对 Mnemosyne（记忆系统元 Agent 仓库）做一次**独立重新设计**。你只对《目标登记表》（附件 01）负责：允许抛弃任何现行架构（它们属 H 类机制猜想），但每处抛弃须写明理由；Owner 已裁定的公理（附件 02a 中 X-1~X-4 与 N-17/18/19）必须遵守。

## 2. 附件清单（Owner 将随本文件一并提供；逐件核对，缺任一件即停止）

1. `01-goals-register.md` — 目标登记表（52 条＋裁决更新，你的唯一"需求方"）
2. `02a-contradiction-clarification-package.md` — Owner 矛盾澄清裁决（逐字）
3. `foundational-agent-antipattern-checklist-v1.md` — 反模式清单 16 条（你的设计须逐条自检）
4. `MNE-DR-020-report.md` ~ `MNE-DR-026-report.md`、`MNE-DR-028-report.md` — 八份研究报告（平台现状、连续性实践、需求生命周期、检索加载、交接评测、学习者建模、开发知识资产、总体抽象复核）
5. `MNE-DR-027-result.md` — ChatGPT GitHub 写能力实测记录

## 3. 交付物（一份设计文档，必含以下十二节）

架构总览；"耐久核心/可再生层"文件组织（可再生层标注为哪代模型而建）；"原始资料→经检查构想→实现层"三态循环记录方案；需求生命周期状态机（含新模型触发重评、反馈全材料捕获、定期测试）；加载/投影机制（记录≠加载）；目的核查机制（与 fail-closed 同级的停止条件）；Owner-touch 预算；**交接方案（核心目标）及预冻结效果测试**；自现状迁移计划；反模式清单 16 条逐条自检；自我批判与盲区；证据引用（结论逐条标注依据的附件与章节，无依据处标 INFERENCE/UNKNOWN）。

设计中任何提示词片段/模板须内嵌全部必填字段与状态枚举（不得给残缺片段）。

## 4. 交付方式（两个文件都必须在同一最终回复中生成）

```yaml
complete_response_transfer_file:
  required: true
  files:
    - MNE-DR-029-counterpart-design.md   # 设计文档本体（可下载）
    - MNE-DR-029-complete-response.md    # 完整最终回复逐字副本（可下载，含状态行与警告）
  create_in_same_final_response: true
```

聊天正文给简明摘要；完整内容以可下载文件交付。若你的界面无法生成文件，如实声明并给出单一最小操作请求，不得声称文件已存在。

## 5. 禁止与停止条件

- 不请求/不猜测 Claude 侧设计；不访问外部仓库或连接器（附件已足）；不联网检索（证据以附件为准，附件外主张标 UNKNOWN）；
- 不修改任何仓库；这是设计文档任务；
- 附件缺失、内容不完整或主题被替换即停止。

## 6. 操作者收尾（给 Owner）

两个下载文件发回 Claude 侧会话即可；后续"双向盲评"是另一个独立任务，届时另发任务书（本次不含）。
