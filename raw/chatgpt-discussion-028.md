---
raw_id: RAW-0028
task_id: MNEMOSYNE-025F
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: public_repo_but_personal_design_content
language: zh-CN
---

# RAW-0028：任务结果路径纠偏与 self-improvement 工作流格式清理

本任务不是完整原始对话，而是从当前用户与 ChatGPT 对话中整理出的纠偏任务记录。

## 当前用户意图

用户发现仓库中仍有文件把 Codex Task Result Record 默认路径写成缺失 TASK_ID 的错误形式。

正确形式应为：

- `notes/codex-task-results/<TASK_ID>-result.md`

用户还指出 `notes/self-improvement-workflow.md` 和 `notes/system-construction-baseline.md` 需要保持正常 Markdown 格式，便于 review、diff 和后续局部维护。

## 本任务目标

本任务用于：

- 修正 Codex Task Result Record 默认路径；
- 清理 `notes/self-improvement-workflow.md` 的 Markdown 格式；
- 清理 `notes/system-construction-baseline.md` 的 Markdown 格式；
- 更新 active-context、todo、handoff、candidate、decision 和 task result record；
- 在进入 MNEMOSYNE-026 模板设计前完成路径纠偏与格式清理。

## 本记录的性质

本记录属于 raw 证据层，不是执行源。

当前执行源仍是：

- `current/human-approved-spec.md`

如果本记录与 `current/human-approved-spec.md` 冲突，应以 `current/human-approved-spec.md` 为准，并登记 open question。

## 范围限制

本任务不进入模板设计，不创建自动化机制，不修改 `current/human-approved-spec.md`，也不修改研究报告原件。
