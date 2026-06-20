# Research Prompts: RC-2026Q2-initial / 研究课题原文目录

## 文件定位

本目录保存 `RC-2026Q2-initial` 的研究输入 prompt / 研究课题原文。prompt 是研究输入，不是研究报告结果；prompt 不是执行源。当前执行源仍是：

- `current/human-approved-spec.md`

如果 prompt、report、summary、motivation 与执行源冲突，以 `current/human-approved-spec.md` 为准，并登记 open question。

## 命名与保存约定

原始 prompt 文件应保持用户提供的文件名，不随意重命名。当前已保存：

- 1 个 pro 深度研究 prompt 原文；
- 6 个用户找回的 light research prompt 原文。

prompt originals 是研究输入，不是研究结论，也不是执行源。report / summary / evidence map 仍是研究输出或派生证据视图。若 prompt 与 report summary 存在差异，应记录 review note，不应静默重写研究结论。

## 当前 prompt originals

```text
raw/research-reports/cycles/2026Q2-initial/research-prompts/
  README.md
  research-prompt-index.md
  originals/
    AI_agent_external_persistent_memory_deep_research_prompt_pro.md
    01_non_dev_long_term_memory_cases.md
    02_chatgpt_claude_conversation_memory_boundaries.md
    03_local_coding_agents_file_memory.md
    04_cloud_coding_agents_github_memory_writeback.md
    05_theory_engineering_basis_external_memory.md
    06_transfer_dev_memory_to_general_dialogue.md
```

## 使用规则

- prompt 原文用于理解研究输入，不代表研究结论。
- report / summary / evidence map 用于理解研究结果或派生证据。
- research motivation 用于理解为什么发起这轮研究。
- prompt、topic mapping、report、summary、motivation 都不是执行源。
- recovered light research prompts supersede the earlier `missing_original_prompt` status for `PROMPT-2026Q2-0002` through `PROMPT-2026Q2-0007`.
- 如 prompt 与 report / summary / motivation 存在差异，应登记 delta / review note；不得用 prompt 静默覆盖研究结论。
