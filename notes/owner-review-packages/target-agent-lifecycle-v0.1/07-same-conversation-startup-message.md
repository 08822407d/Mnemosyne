# Same-Conversation Startup Message — Target-Lifecycle Owner Review

> Use only after the MNEMOSYNE-206 PR is merged to `08822407d/Mnemosyne@master`. This starts a no-write human review in the same conversation after switching from Pro to the selected next-tier model. It does not start handoff.

```text
@GitHub 现在开始执行由 Pro 模型准备的“目标 Agent 承载、演化与依赖责任”人工复核包。不要把当前对话此前的模型记忆或聊天内容当成仓库真相，也不要启动 handoff。

请从执行时最新的 `08822407d/Mnemosyne@master` 按顺序读取：

1. `current/human-approved-spec.md`
2. `notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002.md`
3. `notes/first-three-system-capability-selection-v0.3.md`
4. `notes/target-agent-container-evolution-and-dependency-model-candidate-v0.1.md`
5. `notes/target-agent-container-evolution-and-dependency-frontier-adjudication-v0.1.md`
6. `notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.1.md`
7. `notes/owner-review-packages/target-agent-lifecycle-v0.1/README.md`
8. `notes/owner-review-packages/target-agent-lifecycle-v0.1/01-context-and-fixed-boundaries.md`
9. `notes/owner-review-packages/target-agent-lifecycle-v0.1/02-decision-workbook.md`
10. `notes/owner-review-packages/target-agent-lifecycle-v0.1/03-qa-guide.md`
11. `notes/owner-review-packages/target-agent-lifecycle-v0.1/04-next-tier-interviewer-contract.md`
12. `notes/owner-review-packages/target-agent-lifecycle-v0.1/05-answer-ledger-and-result-template.md`
13. `notes/owner-review-packages/target-agent-lifecycle-v0.1/06-source-map-and-on-demand-reading.md`

不要默认读取根 `README.md`、`commands/load-mnemosyne-guidance.md`、`current/active-context.md`、`handoff/handoff-current.md`、TODO、open questions、完整历史对话、完整研究报告、旧 OR 人工复核包、Meta-Agent 历史 bootstrap 树、业务目标仓库或暂停的 FCV/Fable 路线材料。

先返回简短的 `target_lifecycle_owner_review_receive`，说明：

- package ID 必须是 `MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001`；
- 实际读取的最新 `master` commit；
- 已读取和缺失的必读文件；
- result 002、candidate v0.1、frontier adjudication 和 validation v0.1 的身份是否一致；
- 默认未读取的冷材料；
- 当前执行源仍是 `current/human-approved-spec.md`；
- 没有启动 handoff 或导入其他维护路线；
- 当前没有 GitHub 写入、目标仓库写入/创建、Meta-Agent 修改或激活、私人材料导入、验证执行、产品配置、研究执行或 quota 授权；
- 当前问题为 `TLR-01`。

如果 package ID 不一致、必读文件缺失、无法从最新 master 读取、result 002 与包发生实质冲突，或 package 已因后续 master 变化而重大过期，请只返回：

`TARGET_LIFECYCLE_OWNER_REVIEW_RECEIVE_BLOCKED — <具体原因>`

不要依赖当前长对话记忆自行补全。

receive 通过后，用简短自然语言说明：OR-01 至 OR-09 已结束，本轮只决定五件事——同仓库并发、共享对象/依赖责任、变化轴及次生影响、双亲元 Agent 可保留的设计记录边界、以及“先形成待验证基线还是验证后再称为基线”。

然后从 `TLR-01` 开始，一次只问一个问题。每题先说明它解决什么问题、最小实现、最强优点、主要风险、延期后果和 Pro/frontier 升级条件。我的审阅偏好与本对话前两轮相同：我可以整体接受、逐项修改、提出疑问、延期或否决问题前提。

我提出疑问时，优先使用包内 `03-qa-guide.md`。只有确实不足时，才按 `06-source-map-and-on-demand-reading.md` 读取指定文件，并明确说明额外读取了哪个路径。不要无边界扫描仓库或冷历史。

每个重要回答后：

1. 简短复述你对我回答的理解；
2. 让我纠正或确认；
3. 更新一个简洁可见的 answer ledger；
4. 再进入下一题。

不要替我选择；不要把暂定回答写成确认决定；不要修改仓库。不要因为我接受某个架构语义，就声称 candidate v0.2、验证、目标采用或 Meta-Agent 激活已经发生。

涉及 execution source、target truth、writer authority、自动跨目标传播、共享实时数据库、无界并发、双亲仓库重新成为 live target、私人/信任边界、目标 operational activation 或高影响迁移时，标记：

`FRONTIER_REENTRY_REQUIRED — <问题编号和原因>`

涉及当前 GitHub、ChatGPT、Claude、Fable、Skills、Project、connector、模型、quota、价格、隐私或产品限制时，不要凭记忆回答，标记：

`CURRENT_PRODUCT_FACT_VERIFICATION_REQUIRED — <事实和受影响的问题>`

完成 `TLR-01` 至 `TLR-05` 后，按结果模板给出完整人工抉择结果和简洁自然语言总结，等待我纠正与确认。除非我随后明确授权保存结果并给出写入范围，否则不要创建分支、commit、PR、候选 v0.2、验证仓库或任何外部任务。
```

## Execution intent

```yaml
response_role: preparation_only
execution_disposition: RUN_AFTER_GATE_OPTIONAL
gate: MNEMOSYNE_206_PR_merged_and_Owner_switches_to_next_tier_for_review
external_execution_or_quota_authorized: false
```
