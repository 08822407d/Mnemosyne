# 多写入方署名与溯源惯例 v1.0（定稿）

```yaml
record_type: multi_writer_attribution_convention
version: 1.0
finalized_by_task: MNEMOSYNE-246
authority_level: non_execution_source_convention_owner_adjudicated
execution_source: current/human-approved-spec.md
scope_zh: 所有向本仓库（及未来关联仓库）写入的 AI Agent、工具与人辅助执行面的署名与溯源规则
adjudication_chain:
  - 草案: notes/cross-model-review-results/FABLE5-REVIEW2-001/00-orientation/03-multi-writer-attribution-scheme-draft.md
  - Pro 异构裁定（议程A MODIFY）: notes/cross-model-review-results/FABLE5-REVIEW2-001/07-pro-handover/received/MNE-FABLE5-REVIEW2-JOINT-COOPERATION-ADJUDICATION-001.md
  - 双方收敛: notes/cross-model-review-results/FABLE5-REVIEW2-001/07-pro-handover/03-receipt-and-fable-response.md
  - Owner 终审（含"逐表面身份可信度分级"修正）: notes/cross-model-review-results/FABLE5-REVIEW2-001/07-pro-handover/05-owner-final-adjudication-record.md
effectiveness_model: 合并后新启动的会话生效；进行中会话不追溯（cross_family_effective 机制）
schema_alignment: 字段与 current/run-context-and-pr-provenance-guard.md 对接，不另建冲突 schema
```

## 1. 提交尾注（重要仓库写入强制）

```text
Agent-Action-Actor: <实际调用 Git/GitHub 写入的执行者>@<表面>
Agent-Task: <canonical 任务号>
Agent-Run-Context: <结果/运行上下文记录的仓库路径>
Agent-Content-Producer: <实际内容生成者 | multiple-see-run-context | unknown>
```

约束：

- 值必须与 run-context 记录的证据等级一致；Consumer Chat 的 picker 标签不得写成后端证明。
- **Producer 取实际执行模型，不得继承主会话模板**（委派实验实证：子任务会错误继承主会话署名——见 §4）；无法确认时写 `unknown`。
- 一个 commit 混合多个子任务产出时，trailer 写 `multiple-see-run-context`，明细入 run-context 记录。
- 机械脚本可写 `mechanical-process@local`，操作者记入 run-context。
- 尾注是索引，不替代完整 provenance 记录。
- 表面标识示例：`@claude-code-vscode`、`@claude-code-cli`、`@chatgpt-github-app`、`@codex-cloud`。ChatGPT 侧更稳妥的 action actor 写法是 `ChatGPT@chatgpt-github-app`；`gpt-<model>@chatgpt-web` 仅当 `<model>` 为 operator-reported 选择且明确标注时可用。

## 2. 文件头（重要文档类文件）

重要新文档最小集（脚本/数据/分片不强制）：

```yaml
created_by_task:
generated_by_actor:
generated_on_surface:
```

复杂委派或多 producer：加 `orchestrated_by_actor` 与 `provenance_ref`（指向 run-context），不无限增长字段。重要修改追加：

```yaml
last_updated_by_task:
last_updated_by_actor:
last_updated_on_surface:
```

`date` 仅在文档语义需要生效/观察日期时写（Git 已保存提交时间）。中间历史由 Git 承担。

## 3. PR 来源区块

重要写入 PR 强制携带 `execution_context` 区块（schema 见 run-context guard §5，含 MNEMOSYNE-245 起的 `cross_family_effective` 旗标），并指向完整 run 记录。低风险机械改动可精简为自然语言，但不得省略 task 与 action source。字段最小集：授权引用、复核状态、机械验证、已知限制。

## 4. 角色模型（一个字段不够，按角色拆分）

```yaml
attribution_roles:
  repository_action_actor: 实际调用 Git/GitHub mutation、组装并提交 commit 的执行者
  substantive_content_producer: 实际生成或实质修改内容的模型/人/子任务（可多值）
  orchestrator: 拆分任务、选择子模型、验收并决定提交内容的主执行者
  semantic_reviewer: 进行语义审查者；与 producer 同源时不得自动视为独立
  mechanical_verifier: 执行 hash/ref/schema/diff 等机械核验的执行者/过程
  owner_authorizer: 授权任务与高影响动作的人类 Owner
```

委派场景实证依据（2026-08 委派实验，轨道 08-experiments/03）：Opus 子任务继承了主 Fable 会话的署名模板并错误自认同为主会话模型。结论入约：模板继承不是身份证据；模型自报不是充分证据；平台逐响应记录（如 Claude Code 会话 JSONL 的 `model` 字段）是平台记录级证据但非密码学证明；orchestrator 提交、subtask 生成时两者都必须记录。

## 5. 无尾注的解释

无尾注只能解释为 `legacy_or_unattributed_or_unknown`，**不推定人类**。Owner 手工普通提交不增加负担（不要求补尾注）；高影响手工动作可在 PR/结果记录标 `human_owner_manual`。Git author 与 Owner 账号是辅助证据，不构成"无尾注即人类"。

## 6. 逐表面身份可信度分级（Owner 终审新增要求）

"记录越多越好，瓶颈在可靠性"——各表面的运行时模型自识别可信度分级如下；引用署名时按此分级解读，不得越级引用。

| 表面 | 自识别机制 | 可信度分级 | 依据与日期 | 复查安排 |
|---|---|---|---|---|
| Claude Code（本地 CLI/VSCode/远程控制） | 系统注入的模型标识＋会话 JSONL 逐响应 `model` 字段＋委派实验交叉验证 | **较可靠**（有限实证，非密码学证明） | 2026-08 委派与身份验证实验（轨道 08-experiments/03） | 平台大版本变化时 |
| Claude 网页对话 | 模型自报＋产品标签 | **初步可靠**（Owner 有限观察） | Owner 2026-08 批示 | 随用随核 |
| ChatGPT 网页/app | operator-reported picker 标签；模型自称**无可靠运行时自识别能力**（约 2026-07，Owner 要求下的研究结论） | **低**（标签≠后端证明） | Owner 批示转述；现状未复查 | 实施任务5 调查项 |
| Codex | 未查证 | **unknown** | — | 实施任务5 调查项 |

通用限定：任何表面的 backend 密码学级证明当前均不可得（`backend.status` 按 run-context guard §2.1 处理）。Owner 承诺手动切换模型时尽量明告对话；对话收到该告知时按 `direct_user_instruction` 类证据记录。

## 7. ChatGPT 侧尾注可行性（限定裁定）

ChatGPT 侧可在明确支持 caller-supplied commit message 的 action path 上使用尾注；写前读取 action schema，首次提交后 readback 验证。action 不支持或尾注丢失时，PR 来源区块＋run-context 为**强制 fallback**，不阻断低风险工作。尾注可行性不构成任何单点门。

## 8. 历史与文件组织

历史提交与文件**不迁移、不补署名**（解释为 §5 的 legacy 类）。新规则生效后按内容组织文件，不按厂商隔离；cross-model-review-results 仍是评审类内容的自然归档位置。

## 9. 生效与修订

- 本惯例自 Owner 批准合并起对新启动的会话生效；修订经 Owner 批准的任务执行并更新本文件头。
- 本文件不是执行源；与执行源（尤其 §18 重要写入记录义务）冲突时以执行源为准并上报。
- 登记：本文件在 guard-registry 之外（它是惯例记录而非行为 guard）；其义务的强制载体是执行源 §18 第八条与 run-context guard。
