# ChatGPT + GitHub App Surface Facts — Current

> 时效性产品事实记录，非执行源。本文件承接执行源 §18 泛化（PR #307）时移出的 ChatGPT 表面细节；行为义务的载体是新 §18 十条与相关 guard，本文件只记事实与操作建议。

```yaml
fact_record_id: MNEMOSYNE-CHATGPT-GITHUB-APP-SURFACE-FACTS-001
created_by_task: MNEMOSYNE-248
observed_and_checked_at: 2026-08-26
fact_classes: [repository_historical_evidence, operator_reported, absence_of_documentation_in_bounded_search, engineering_inference]
exact_backend_identity: unknown_or_not_attestable
supersedes_nothing: 原 §18 表面细节的历史文本仍在 git 历史（PR #307 前的 spec），本文件是其现行去向
```

## 1. 写入能力事实

- 自 2026-07 起（仓库实证）：普通 ChatGPT 对话在连接并选择 GitHub app、且账户/workspace/action 配置支持时，可对关联仓库执行写入类 actions（建分支、建文件、建 PR）。"普通对话只能读 GitHub"自该时点起为过时假设。
- 能力随 app 连接状态、模型、计划、workspace 管理配置变化——**每次涉及时按当前 UI 与 action 列表核验**，不引用本文件替代核验（执行源 §18 时效条款）。

## 2. 授权操作建议（原 §18 移出内容）

- 审批卡默认建议选 `Allow once`（一次性允许）而非 `Always allow`；用户若选持久授权，Agent 仍不得把持久授权视为未来任务授权（平台权限 ≠ 任务授权，执行源 §18 第二条）。
- approval card 出现、app 连接状态、历史授权，都不单独构成 Mnemosyne 写入授权。

## 3. 风险分级操作示例（原 §18 移出内容）

| 档 | 动作示例 | 要求 |
|---|---|---|
| read-only | 读文件、搜索、读 PR/issue 元数据 | 证据引用；不改仓库 |
| low-scope write | 建分支、建/改单个文档、建 PR、普通评论 | 当前任务明确授权＋平台 approval |
| high-scope / sensitive | 合并 PR、删除文件、批量改 issue/label、auto-merge、安全/权限配置 | 动作前 Owner 再次明确批准（执行源 §18 高影响条款） |

## 4. 提交署名支持（Pro 复核裁定口径）

- 部分低层 action path（历史上经 `create_commit` 类动作）支持调用方指定 commit message——**部分可控已实证，跨 action 稳定性未实证**（多行尾注 canary 未跑）。
- 操作规程：写前读 action schema → 首次提交后 readback 验证尾注是否保留 → 不支持或丢失时，PR 来源区块＋run-context 记录为强制 fallback。尾注可行性不构成任何单点门。

## 5. 运行时模型自识别（任务5 调查项复查结果）

- 约 2026-07：Owner 要求下 ChatGPT 自查并声称**无可靠获取自身运行时模型的能力**（operator_reported，转述）。
- 2026-08-26 限定复查：对 OpenAI 官方文档/帮助中心/开发者社区做限定检索，**未发现**任何"对话内模型可获知自身运行时身份"的机制记载（absence_of_documentation_in_bounded_search——不是"证明不存在"）。
- 现行结论：**旧结论未被推翻**。picker 标签是 operator 侧证据；模型自报按 run-context guard 列为 `model_self_report_untrusted`。身份可信度分级：**低**（权威版见署名惯例 §6）。Owner 承诺手动切换模型时尽量明告对话。

## 6. 原 §18 表面细节逐条去向映射（任务2 验收项收尾）

| 原 §18 条目（PR #307 前） | 去向 |
|---|---|
| 适用场景声明 | 新 §18 第 1 条（泛化为任意 Agent） |
| "自 2026-07 起不得假设只读" | 本文件 §1 |
| Codex Cloud 首选写入助手定位 | `codex-surface-facts.md` §1 |
| 能力时效性与查验义务 | 新 §18 第 3 条＋§11 时效钩子＋本文件 §1 |
| 平台权限/任务授权分离 | 新 §18 第 2 条 |
| 两者同时成立；Always allow 不构成授权 | 新 §18 第 2 条＋本文件 §2 |
| 优先分支+PR | 新 §18 第 5 条 |
| 写前声明外部影响＋核对边界 | 新 §18 第 6 条 |
| Allow once 建议 | 本文件 §2 |
| 三档风险分级 | 本文件 §3＋新 §18 第 7 条（高影响授权） |
| result record 最低字段 | 新 §18 第 8 条＋run-context guard §4/§5 |
| 过时能力声明标 stale | §11 时效钩子（修订 7） |
| 不授权自动化清单 | 新 §18 第 10 条 |

核对声明：原 §18 各实质条目（含嵌套小项）均可在上表右列找到落点，无内容丢失 [mechanically_checked_against_git_history_version]。
