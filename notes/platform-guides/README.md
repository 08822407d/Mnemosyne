# Platform guides — 平台事实文件族索引

```yaml
record_type: platform_facts_index
created_by_task: MNEMOSYNE-248
authority_level: L3_navigation_non_execution_source
scope_zh: 各写入/工作表面的时效性产品事实层；执行源 §10/§18 所指"经登记的当前平台事实文件"的登记处
execution_source: current/human-approved-spec.md
```

## 定位

- 执行源不维护产品快照（§10/§18，PR #307 起）；产品、模型、连接器、审批卡、权限配置等**时效事实**全部记录在本文件族。
- 本索引与各事实文件均为导航/证据层，不施加义务；行为义务的载体是执行源与 guard。
- 每份事实文件必须带 `observed_and_checked_at` 类日期与逐项证据类别；任务实际依赖某事实并发现其过期时，按执行源 §11 登记上报。

## 文件清单

| 文件 | 表面 | 最近核对 | 说明 |
|---|---|---|---|
| `claude-code-surface-facts.md`（本目录） | Claude Code（CLI / VSCode 插件 / claude.ai/code 远程控制） | 2026-08-26 | 本地 Agent 写入面；模型委派与身份记录实测 |
| `chatgpt-github-app-surface-facts.md`（本目录） | 普通 ChatGPT 对话 + GitHub app | 2026-08-26 | 承接原执行源 §18 移出的表面细节（含逐条去向映射） |
| `codex-surface-facts.md`（本目录） | Codex（Cloud 任务 / CLI） | 2026-08-26 | 历史角色与当前未验证项 |
| `../../current/claude-github-work-surface-facts.md` | Claude 网页（Project + GitHub 持久存储） | 2026-08-15（MNEMOSYNE-219） | 先于本文件族建立，暂留原位；迁入本目录留待整编决定 |

## 维护规则

- 新表面首次成为正式写入面前：bounded capability preflight（执行源 §18）＋建立对应事实文件。
- 更新事实文件属普通维护任务；文件内逐条事实各自带日期与证据类别，不整篇"刷新"。
- 各表面的**身份可信度分级**权威版在 `notes/registries/multi-writer-attribution-convention.md` §6，本文件族记录支撑它的具体事实。
