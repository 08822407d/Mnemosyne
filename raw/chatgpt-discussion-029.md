---
raw_id: RAW-0029
task_id: MNEMOSYNE-025G
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: public_repo_but_personal_design_content
language: zh-CN
---

# RAW-0029：错误结果路径全仓库硬纠偏

本任务不是完整原始对话，而是从当前用户与 ChatGPT 对话中整理出的硬纠偏任务记录。

## 当前问题

MNEMOSYNE-025F 合并后，仓库中仍然存在错误 Codex Task Result Record 路径。

错误路径是：

- `notes/codex-task-results/-result.md`

正确路径是：

- `notes/codex-task-results/<TASK_ID>-result.md`

## 本任务目标

本任务用于修正仓库中残留的错误 Codex Task Result Record 路径，并进行最小状态落账。

本任务不进入模板设计，不重写 self-improvement workflow，不做大规模格式整理。

## 本记录的性质

本记录属于 raw 证据层，不是执行源。

当前执行源仍是：

- `current/human-approved-spec.md`

如果本记录与 `current/human-approved-spec.md` 冲突，应以 `current/human-approved-spec.md` 为准，并登记 open question。
