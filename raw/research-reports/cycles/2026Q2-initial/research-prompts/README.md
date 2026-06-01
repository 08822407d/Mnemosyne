# Research Prompts: RC-2026Q2-initial / 研究课题原文目录

## 文件定位

本目录保存 `RC-2026Q2-initial` 的研究输入 prompt / 研究课题原文。prompt 是研究输入，不是研究报告结果；prompt 不是执行源。当前执行源仍是：

- `current/human-approved-spec.md`

如果 prompt、report、summary、motivation 与执行源冲突，以 `current/human-approved-spec.md` 为准，并登记 open question。

## 命名与保存约定

原始 prompt 文件应保持用户提供的文件名，不随意重命名。当前约定的 pro 深度研究 prompt 路径是：

- `raw/research-reports/cycles/2026Q2-initial/research-prompts/originals/AI_agent_external_persistent_memory_deep_research_prompt_pro.md`

当前已知只有 pro 深度研究 prompt 原文被保留。6 个轻度研究 prompt 原文缺失，不得编造。对缺失 prompt，只能记录 report title / topic title / inferred topic，并明确标记 prompt 原文缺失。

如果未来找回轻度研究 prompt，应放入 `research-prompts/originals/` 并更新：

- `raw/research-reports/cycles/2026Q2-initial/research-prompts/research-prompt-index.md`
- `raw/research-reports/cycles/2026Q2-initial/report-topic-and-prompt-map.md`
- `raw/research-reports/current/current-research-prompts.md`

## 推荐目录结构

```text
raw/research-reports/cycles/2026Q2-initial/research-prompts/
  README.md
  research-prompt-index.md
  originals/
    AI_agent_external_persistent_memory_deep_research_prompt_pro.md
```

## 使用规则

- prompt 原文用于理解研究输入，不代表研究结论。
- report / summary / evidence map 用于理解研究结果或派生证据。
- research motivation 用于理解为什么发起这轮研究。
- prompt、topic mapping、report、summary、motivation 都不是执行源。
- 不得把 inferred topic 说成用户原始 prompt。
