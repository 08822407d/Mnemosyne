# 任务书 · MNE-DR-031 盲评 Pro 设计稿（Claude 侧，全新 Claude Code 会话）

> 本任务由**全新的 Claude Code 会话**执行（不得由 FABLE5-REDESIGN-001 轨道会话执行——它是被评方之一的作者，且对 Pro 稿保持防火墙）。完整读取本任务书后执行。

```yaml
display_name: MNE-DR-031 盲评Pro稿（CC）
canonical_task_id: FABLE5-REDESIGN-001-BR2
execute_in: 本机新开 Claude Code 会话（模型 Fable 5 或 Opus 5 皆可，如实记录）· 工作目录 /home/cheyh/projs/Mnemosyne · 分支 fable5-redesign-001-workspace（只读，不切分支不提交）
language: 中文
blind_condition: 你评审的是 GPT 侧对照设计稿。禁止读取 Claude 侧设计稿及其派生分析（见 §1 禁读清单）；不做两稿比较；本会话上下文外的任何"项目记忆"不得当作评审依据。
```

## 1. 读取边界（先执行 `git branch --show-current` 确认分支）

**允许读（仅此七类）**：
- 评审细则：`project-knowledge/FABLE5-REDESIGN-001/MNE-DR-030-031-shared-review-rubric.md`（先读）
- 被评稿：`notes/cross-model-review-results/FABLE5-REDESIGN-001/06-research-received/MNE-DR-029-counterpart-design.md`
- 判定依据三件：`project-knowledge/FABLE5-REDESIGN-001/pro-counterpart-materials/` 下 `01-goals-register.md`、`02a-contradiction-clarification-package.md`、`foundational-agent-antipattern-checklist-v1.md`
- 证据库（仅核对引证时按需）：同目录 `MNE-DR-020~028` 各件
- 本任务书自身

**禁止读（违例即停止并报告）**：`04-redesign-fable.md`、`02-consistency-and-feasibility.md`、`05-pro-counterpart-package.md`、`05a*`、`06-research-received/01-ingest-digest.md`、`09-continuation/` 全部、`03-research-questions.md`；以及仓库其余一切与评审无关路径。

## 2. 工作与交付

按细则 R1~R8 逐项评审；交付两文件**写到 `~/Downloads/`（不写仓库、不 commit、不 push）**：
`MNE-DR-031-review.md`（逐项表＋三优点/三缺陷带节号＋采纳建议清单＋标签纪律）＋ `MNE-DR-031-complete-response.md`（最终回复逐字副本）。回复正文只给摘要，并报告实际读取文件清单（自证输入面）。

## 3. 禁止与停止条件

只读仓库；不比较两稿；不重新设计；读到禁读清单任一文件即违例停止；材料缺失即停止。

## 4. 操作者流程（给 Owner）

1. 新开一个 Claude Code 会话（本机，目录 /home/cheyh/projs/Mnemosyne）；
2. 首条消息粘贴：`请读取并严格执行 project-knowledge/FABLE5-REDESIGN-001/MNE-DR-031-blind-review-pro-design-taskbook.md（注意其读取边界）`；
3. 完成后把 Downloads 里的两个 MNE-DR-031 文件发回主轨道会话。
