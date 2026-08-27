# Codex Surface Facts — Current

> 时效性产品事实记录，非执行源。

```yaml
fact_record_id: MNEMOSYNE-CODEX-SURFACE-FACTS-001
created_by_task: MNEMOSYNE-248
observed_and_checked_at: 2026-08-26
fact_classes: [repository_historical_evidence, official_documentation_bounded_search, absence_of_documentation_in_bounded_search]
exact_backend_identity: unknown_or_not_attestable
```

## 1. 历史角色（仓库实证）

- 2026-06~07 时期，Codex Cloud 曾是本仓库主要的远程 GitHub 写入与版本保存助手（执行源 §10 旧文；PR #307 起产品无关化，历史定性保留于 git 历史与本条）。
- "必须进入 Codex Cloud 才能提交 PR"自 2026-07 起不再成立（ChatGPT app 与 Claude Code 写入面相继建立）。
- 历史提交无署名尾注：按署名惯例 §5 解释为 legacy，不追溯。

## 2. 附件边界（历史动机，现状未验证）

- 2026-06 时期事实：Codex Cloud 任务对话不能假定直接接收非图片附件——此为执行源 §14（人工材料转移边界）的历史动机；PR #307 起该前提移出规则正文。
- **当前附件能力未复核**；如任务实际依赖，按 §11 钩子现场核验并登记。

## 3. 当前文档面（2026-08-26 限定检索）

- OpenAI 开发者站存在 Codex 文档族（cloud environments、environment variables、developer commands 等），支持环境变量/密钥配置、模型供应商配置（`env_key`）。
- 本仓库未对当前 Codex Cloud 能力做过 bounded capability preflight——**它若要恢复为正式写入面，须按执行源 §18 先做预检**。

## 4. 运行时模型自识别（任务5 调查项查证结果）

- 2026-08-26 限定检索：**未发现**任何"运行中的 Codex 任务可获知自身模型身份"的文档化机制（absence_of_documentation_in_bounded_search）。
- 可得的身份证据仅为 operator 侧配置/选择（CLI config 的 model 字段、Cloud 任务的产品标签）；模型自报按 `model_self_report_untrusted` 处理。
- 身份可信度分级：**unknown（未查证到机制）**——权威版见署名惯例 §6。
