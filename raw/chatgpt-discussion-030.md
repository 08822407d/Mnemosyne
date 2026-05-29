---
raw_id: RAW-0030
task_id: MNEMOSYNE-025H
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: public_repo_but_personal_design_content
language: zh-CN
---

# RAW-0030：Codex Task Result Record 路径占位符规范化

本任务不是完整原始对话，而是从当前用户与 ChatGPT 对话中整理出的路径占位符规范化记录。

## 当前问题

MNEMOSYNE-025G 合并后，仓库中仍然残留错误路径：

- `notes/codex-task-results/-result.md`

此前尝试使用尖括号占位符形式：

- `notes/codex-task-results/<TASK_ID>-result.md`

但多次任务后仍被错误写回为缺失 TASK_ID 的路径。

## 本任务目标

本任务用于修正残留错误路径，并将 Codex Task Result Record 默认占位符规范改为：

- `notes/codex-task-results/TASK_ID-result.md`

改用 `TASK_ID` 而不是 `<TASK_ID>` 的理由是降低 Markdown、HTML、工具转义或模型改写造成的歧义。

本任务不进入模板设计，不大规模重写文档。

## 本记录的性质

本记录属于 raw 证据层，不是执行源。

当前执行源仍是：

- `current/human-approved-spec.md`

如果本记录与 `current/human-approved-spec.md` 冲突，应以 `current/human-approved-spec.md` 为准，并登记 open question。
