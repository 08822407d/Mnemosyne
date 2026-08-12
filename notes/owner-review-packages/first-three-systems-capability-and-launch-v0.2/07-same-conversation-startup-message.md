# Same-Conversation Startup Message — OR-02 through OR-09

> Use only after this package is merged to `08822407d/Mnemosyne@master`. The Owner remains in the same conversation, switches from the Pro planning segment to the intended next-tier model, and sends the message below. Sending it starts only the bounded no-write owner-review interview.

```text
@GitHub 现在开始执行由 Pro 模型准备的 OR-02 至 OR-09 人工抉择交互包。不要把当前对话此前的模型记忆或聊天内容当成仓库真相，也不要启动 handoff。

请从执行时最新的 `08822407d/Mnemosyne@master` 按顺序读取：

1. `current/human-approved-spec.md`
2. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.2/README.md`
3. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.2/01-context-and-fixed-boundaries.md`
4. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.2/02-decision-workbook.md`
5. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.2/03-capability-selection-and-qa-guide.md`
6. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.2/04-next-tier-interviewer-contract.md`
7. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.2/05-answer-ledger-and-result-template.md`
8. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.2/06-source-map-and-on-demand-reading.md`

不要因为它们存在就默认读取根 `README.md`、`commands/load-mnemosyne-guidance.md`、Mnemosyne 的 `current/active-context.md`、`handoff/handoff-current.md`、`current/todo.md`、`current/open-questions.md`、完整历史对话、完整研究报告、旧 handoff、任务结果档案、旧 v0.1 人工抉择包、Meta-Agent 历史 bootstrap 树或暂停的 FCV/Fable 路线材料。

先返回一个简短的 `owner_review_receive_v2`，其中说明：

- package ID 必须是 `MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-002`；
- 实际读取的最新 `master` commit；
- 已读取和缺失的必读文件；
- `OR-01` 已完成，并读取到其结果引用和能力清单 v0.2；
- 默认未读取的冷材料；
- 当前执行源仍是 `current/human-approved-spec.md`；
- 没有启动 handoff 或导入其他维护路线；
- 当前没有 GitHub 写入、目标仓库写入/创建、Meta-Agent 修改或激活、私人材料导入、产品配置、研究执行或 quota 授权；
- 当前问题为 `OR-02-A`。

如果必读文件缺失、package ID 不一致、OR-01 结果或 v0.2 目录不存在、文件不能从最新 master 读取，或包相对最新合并内容出现重大过期，请只返回 `OWNER_REVIEW_PACKAGE_V2_RECEIVE_BLOCKED` 和具体原因，不要依赖此前聊天内容自行补全。

receive 通过后，请用简短自然语言说明：OR-01 已经完成，本轮只选择三个系统的共同最低能力、各自附加能力/对象、仓库与存储方向、准备/首次真实使用顺序以及后续产品事实核验范围。

然后从 `OR-02-A` 开始，一次只问一个能力组、一个目标组或一个紧密相关的小组。每次应先用自然中文解释清楚这些条目解决什么问题、最小实现是什么、为什么该系统需要、删除会有什么后果，以及它属于 required、triggered、experimental、deferred 还是 target-specific object。

我的审阅偏好与 OR-01 相同：如果我要求逐项核对，就将该组的条目按可管理的批次逐项解释，让我对每项说没问题、补充、疑问、延期或拒绝。不要为了节省轮次强迫我一次接受整个组。

当我提出疑问时，优先使用包内 `03-capability-selection-and-qa-guide.md` 回答。只有确实不足时，才按 `06-source-map-and-on-demand-reading.md` 读取指定源文件，并明确说明你额外读取了哪个路径；不要无边界读取仓库或冷历史。

每个重要回答后：

1. 简短复述你对我回答的理解；
2. 让我纠正或确认；
3. 更新一个简洁的可见 answer ledger；
4. 再进入下一题。

不要替我选择；不要把暂定回答写成确认决定；不要修改仓库。不要因为选择某项能力就声称它已在目标中实现。

涉及新的架构、execution source、target truth、writer authority、privacy、trust boundary、Meta-Agent operational activation、公共能力库所有权、自动跨目标传播、共享运行状态或高影响迁移时，标记：

`FRONTIER_REENTRY_REQUIRED — <问题编号和原因>`

涉及当前模型、套餐、quota、价格、ChatGPT/Claude/Fable 产品设置、Skills、Voice、Memory、Project、connector、文件/context 限制、导出、隐私、数据使用或当前模型可靠性时，不要凭记忆回答，标记：

`CURRENT_PRODUCT_FACT_VERIFICATION_REQUIRED — <事实和受影响的问题>`

依赖缺失的目标仓库、源码政策、完整对话、规格或其他精确材料时，标记：

`MISSING_ARTIFACT_BLOCKS_DECISION — <材料和受影响的问题>`

完成 OR-02 至 OR-09 后，按结果模板给出完整人工抉择结果和简洁自然语言总结，等待我纠正与确认。除非我随后明确授权保存结果并给出写入范围，否则不要创建分支、commit、PR、目标仓库、Project、Skill、研究任务或任何外部操作。
```

## Expected first response

A passing first response should contain only a compact receive receipt, a brief statement of purpose, and `OR-02-A`. It should not begin answering later questions, repeat all 41 capabilities, or import another route.

## Boundaries

- This startup message does not authorize a model switch by itself; the Owner performs the visible switch.
- It does not attest the hidden backend.
- It does not authorize repository writes, target creation, activation, private-material intake, product configuration, research, quota use, or target execution.
- It does not convert the package or answers into execution source or target truth.
