# Platform Guides

This directory stores non-execution-source platform capability and configuration notes used when Mnemosyne prepares prompts, review requests, handoff packages, or cross-model work for external AI products.

These guides are product-research notes, not execution source. They may inform prompt setup and safety preflight, but they do not approve repository edits, target workspace creation, material ingestion, target repository write, regression formalization, operational build, or execution-source updates.

Product capabilities are time-sensitive. Re-verify current product documentation before relying on a guide for high-stakes or workflow-changing decisions.

```yaml
index_extension_by_task: MNEMOSYNE-248
scope_zh: 各写入/工作表面的时效性产品事实与能力研究层；执行源 §10/§18 所指"经登记的当前平台事实文件"的登记处
maintenance_rules:
  - 新表面首次成为正式写入面前：bounded capability preflight（执行源 §18）＋建立对应事实文件
  - 逐条事实各自带日期与证据类别；任务实际依赖某事实并发现过期时按执行源 §11 登记上报
  - 身份可信度分级权威版在 notes/registries/multi-writer-attribution-convention.md §6
```

## Current files

**Surface-facts records（实测事实层，MNEMOSYNE-248 起）：**

- `claude-code-surface-facts.md` — Claude Code（CLI / VSCode / claude.ai/code 远程控制）本地 Agent 写入面；模型委派与身份记录实测（核对日 2026-08-26）。
- `chatgpt-github-app-surface-facts.md` — 普通 ChatGPT + GitHub app；承接原执行源 §18 移出的表面细节（含逐条去向映射）与自识别调查结果（核对日 2026-08-26）。
- `codex-surface-facts.md` — Codex（Cloud / CLI）历史角色与当前未验证项（核对日 2026-08-26）。
- `../../current/claude-github-work-surface-facts.md` — Claude 网页（Project + GitHub 持久存储），先于本目录建立，暂留原位（核对日 2026-08-15，MNEMOSYNE-219）；迁入本目录留待整编决定。

**Capability research guides（能力研究层，2026-07 建立）：**

- `claude-conversation-capabilities-and-settings-guide-v0.1.md` — Claude ordinary conversation settings for Projects, GitHub/connectors, Research, web search, skills, plugins, code execution/file creation, and Mnemosyne prompt-preflight usage（last researched 2026-07-07）.
- `chatgpt-github-app-capabilities-guide-v0.1.md` — ChatGPT ordinary-conversation GitHub app read/write capability update, permission prompts, write-action safety classification, and Mnemosyne prompt-preflight guidance（last researched 2026-07 era）.

两层关系：guides 是研究快照（较旧、覆盖面宽），surface-facts 是实测事实（较新、逐条带证据类别）；同一表面两层并存时，冲突以日期新且证据级高者为准并按 §11 登记差异。
