---
raw_id: RAW-0027
task_id: MNEMOSYNE-025E
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: public_repo_but_personal_design_content
language: zh-CN
---

# RAW-0027：系统建设基线快照与路线图纠偏

本任务不是完整原始对话，而是从当前用户与 ChatGPT 对话中整理出的阶段性系统建设基线与路线图纠偏记录。

## 当前用户意图

用户希望把当前已经相对确定的系统建设目标、工作约定、后续路线和当前诊断暂存到 GitHub 仓库中。

这样做的目标是避免后续因 ChatGPT 对话上下文过长、压缩、遗忘或任务交接不完整，导致 Mnemosyne 的系统建设方向跑偏。

## 本任务目标

本任务需要创建更明确的系统建设基线快照，并纠正当前已知路线和记录问题，包括：

- Codex Task Result Record 默认路径应统一为 `notes/codex-task-results/<TASK_ID>-result.md`；
- 后续 Codex 任务是否必须新开，应按“是否必须在全新 Codex Cloud 任务中执行”判断；
- 后续 Codex 任务内容应优先以可下载 `.txt` 任务文件形式提供，避免聊天界面代码块嵌套导致复制不完整；
- 后续每个 Codex 任务都应写入 task result record，且该记录不是执行源。

## 本记录的性质

本记录属于 raw 证据层，不是执行源。

当前执行源仍是：

- `current/human-approved-spec.md`

如果本记录与 `current/human-approved-spec.md` 冲突，应以 `current/human-approved-spec.md` 为准，并登记 open question。
