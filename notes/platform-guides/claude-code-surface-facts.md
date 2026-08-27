# Claude Code Surface Facts — Current

> 时效性产品事实记录，非执行源，不授权任何写入或额度使用。`current/human-approved-spec.md` 是唯一执行源。

```yaml
fact_record_id: MNEMOSYNE-CLAUDE-CODE-SURFACE-FACTS-001
created_by_task: MNEMOSYNE-248
observed_and_checked_at: 2026-08-26
surface_variants: [local_CLI, VSCode_extension, claude_ai_code_remote_control]
product_account_condition: user_reported_Claude_Max_subscription
fact_classes: [live_experiment_in_this_repository, operator_observed, platform_recorded_metadata, engineering_inference]
exact_backend_identity: platform_metadata_not_cryptographic_proof
primary_evidence_roots:
  - notes/cross-model-review-results/FABLE5-REVIEW2-001/08-experiments/03-model-delegation-and-identity-verification.md
  - notes/cross-model-review-results/FABLE5-REVIEW2-001/03-independent-design/07-claude-incident-C13-autocontinue-misattribution.md
```

## 1. 写入能力（实测，2026-08）

- 本地完整 git 工具链＋gh CLI：分支、提交、推送、建 PR、PR 元数据读写全部可用；**commit message 完全由调用方控制**（多行尾注实测于 PR #306~#310 的全部提交）——四行署名尾注在本表面无可行性问题。
- 权限模型：Owner 侧 `settings.json` 允许/拒绝清单（当前配置含 git/gh 白名单与危险操作黑名单：禁 force push、禁删分支、禁 gh api DELETE）。
- 自动模式分类器会**拦截 Agent 修改自身权限配置**（2026-08-22/23 两次实证；已入法为执行源 §18"Agent 不得自行修改其权限配置"）。

## 2. 模型身份与委派（实测，2026-08）

- 运行时模型标识由系统注入（会话可读）；会话记录（`~/.claude/projects/<project>/<session>.jsonl`）含**逐响应 `model` 字段**——平台记录级证据，非密码学证明。
- 子代理委派：Agent 工具 `model` 参数可指定 sonnet/opus/haiku/fable；实测 Opus 子任务可执行并回传。
- **已证坑**：子任务会继承主会话的提交署名模板并可能错误自认同为主会话模型——署名惯例因此规定 Producer 取实际执行模型、不得继承模板（详见署名惯例 §4）。
- 子代理固定开销约 1.9 万 token/次 [engineering_inference from measured runs]——委派只适合有实质工作量的子任务。
- 身份可信度分级：**较可靠（有限实证）**——权威版见署名惯例 §6。

## 3. 会话与连续性（实测）

- 上下文压缩（compaction）：Owner 手动触发；压缩前落盘检查点＋压缩后按检查点恢复的流程已实测有效（2026-08-25）。
- 冷启动恢复：VSCode 崩溃后新会话零对话记忆、纯仓库重建工作状态成功（2026-08-22，门0~门3 全程）——"文件负责记忆"对本表面成立。
- `autoContinueAtUsageLimit` 设置项**实测未生效**（2026-08-24，5h 窗口刷新后未自动继续，Owner 手动输入 Continue 才恢复；C-13 事件，含一次我方归因错误与更正）。
- 6 小时级会话限额会中断后台子代理：**增量落盘纪律**（逐项写盘、短摘要返回）是已验证的对冲（2026-08-24 四代理被杀、数据零丢失）。

## 4. 远程控制（实测 2026-08-26）

- Owner 经 claude.ai/code 网页接管本机会话：双向消息通路正常；**网页端历史回溯可能滞后**（当日观察：滞后约一天，新交互后追上）；本机侧记录与仓库不受影响。

## 5. 导出与归档（实测）

- 会话 JSONL 可直接复制归档；本仓库已有 JSONL→可读 markdown 转换脚本（`~/projs/mnemosyne-archives/tools/convert_claude_jsonl.py`，本地档案库）。
- Claude 网页对话的批量导出工具查证记录见轨道 08-experiments/03。

## 6. 未验证/待复查项

- 子代理 `model` 参数在全部模型档位组合下的行为（仅抽测 opus/haiku）。
- 远程控制在长离线/弱网下的消息可靠性。
- 各设置项语义随版本变化（`autoContinueAtUsageLimit` 失效是否版本性问题）。
