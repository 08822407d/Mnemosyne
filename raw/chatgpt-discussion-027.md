---
raw_id: RAW-0027
task_id: MNEMOSYNE-025B
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: public_repo_but_personal_design_content
language: zh-CN
---

# RAW-0027：self-improvement workflow 硬清理与候选需求补账

这不是完整原始对话，而是从当前 ChatGPT 对仓库的核对结果中整理出的修复记录。

## 当前问题

MNEMOSYNE-025 已创建 `notes/self-improvement-workflow.md`，但当前仍有以下问题：

- `notes/self-improvement-workflow.md` 接近单行压缩 Markdown；
- Codex Task Result Record 默认路径仍写成 `notes/codex-task-results/-result.md`，需要改成 `notes/codex-task-results/<TASK_ID>-result.md`；
- `notes/candidate-requirements.md` 中存在一个 self-improvement 相关孤立条目，没有 CAND ID；
- 若干 self-improvement 相关 CAND 状态尚未按实际反映情况同步；
- MNEMOSYNE-025A 的 result record 记录了修复完成，但实际仍有偏差，需要在本次 result record 中如实记录。

## 本次目标

本次任务只做修复和补账：

- 恢复 `notes/self-improvement-workflow.md` 为正常 Markdown；
- 修正 Codex Task Result Record 默认路径；
- 给孤立 candidate 补 ID；
- 将已被 workflow 文档反映的 self-improvement 候选需求标记为 reflected；
- 保留模板、similarity/conflict 最小格式、user decision 记录格式等后续项为 pending / todo；
- 记录本次 Codex 任务结果。
