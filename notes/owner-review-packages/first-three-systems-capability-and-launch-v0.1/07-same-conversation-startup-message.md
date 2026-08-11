# Same-Conversation Next-Tier Startup Message

> Use this message only after the package is merged into `master` and the Owner switches the current conversation from Pro/frontier to the selected next-tier condition. It starts the bounded human owner review; it does not start a new conversation, a handoff, external research, or repository writing.

```yaml
package_id: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-001
execution_timing: after_package_merge_and_model_switch
conversation: current_same_conversation
repository_write: false
```

## Copyable startup message

```text
@GitHub 现在开始执行已经由 Pro 模型准备的人工抉择交互包。不要把当前对话此前的模型记忆或聊天内容当成仓库真相，也不要启动 handoff。

请从执行时最新的 `08822407d/Mnemosyne@master` 按顺序读取：

1. `current/human-approved-spec.md`
2. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.1/README.md`
3. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.1/01-context-and-fixed-boundaries.md`
4. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.1/02-decision-workbook.md`
5. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.1/03-capability-and-qa-reference.md`
6. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.1/04-next-tier-interviewer-contract.md`
7. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.1/05-answer-ledger-and-result-template.md`
8. `notes/owner-review-packages/first-three-systems-capability-and-launch-v0.1/06-source-map-and-on-demand-reading.md`

不要因为它们存在就默认读取根 `README.md`、`current/active-context.md`、`handoff/handoff-current.md`、`current/todo.md`、`current/open-questions.md`、完整历史对话、完整研究报告、旧 handoff、任务结果档案、Meta-Agent 历史 bootstrap 树或暂停的 FCV/Fable 路线材料。

先返回一个简短的 `owner_review_receive`，其中说明：

- package ID；
- 实际读取的 `master` commit；
- 已读取和缺失的必读文件；
- 默认未读取的冷材料；
- 当前执行源仍是 `current/human-approved-spec.md`；
- 当前没有 GitHub 写入、目标仓库写入、Meta-Agent 激活、私人材料导入、研究执行或 quota 授权；
- 当前问题为 `OR-01`。

如果必读文件缺失、package ID 不一致或无法从最新 master 读取，请只返回 `OWNER_REVIEW_PACKAGE_RECEIVE_BLOCKED` 和具体原因，不要依赖此前聊天内容自行补全。

receive 通过后，请用简短自然语言说明这次人工抉择的目标，然后从 `OR-01` 开始，一次只问一个问题或一个紧密相关的小组。我要是提出疑问，你应当优先使用包内 `03-capability-and-qa-reference.md` 解答；只有确实不足时，才按 `06-source-map-and-on-demand-reading.md` 读取指定源文件，并说明你额外读取了哪个文件。

每个重要回答后：

1. 简短复述你对我回答的理解；
2. 让我纠正或确认；
3. 更新一个简洁的可见 answer ledger；
4. 再进入下一题。

不要替我选择；不要把暂定回答写成确认决定；不要修改仓库。涉及新的架构、truth source、authority、privacy、Meta-Agent 激活、自动跨目标传播或高影响迁移时，标记 `FRONTIER_REENTRY_REQUIRED`。涉及当前模型、套餐、quota、价格、ChatGPT/Claude/Fable 产品设置、Skills、Voice、Memory、Project、connector 或隐私行为时，不要凭记忆回答，标记 `CURRENT_PRODUCT_FACT_VERIFICATION_REQUIRED`。

完成 OR-01 至 OR-09 后，按结果模板给出完整人工抉择结果和一份简洁自然语言总结，等待我确认。除非我随后明确授权保存结果并给出写入范围，否则不要创建分支、commit 或 PR。
```

## Expected first response shape

The interviewer should respond in concise natural language, approximately:

```text
## 无需用户操作

owner_review_receive: PASS
- package: MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-001
- master: <commit>
- required files: 8/8 loaded
- cold sources: not read
- execution source: current/human-approved-spec.md
- repository/target/research authorization: none
- current question: OR-01

这次要做的是……

### OR-01 ……
<question with context and options>
```

A large YAML receipt is unnecessary unless a material mismatch exists.

## Stop cases

Do not proceed when:

- package files are unmerged or only on a branch the interviewer was not instructed to use;
- source master is older than the package merge;
- the package ID is missing/inconsistent;
- the execution source cannot be read;
- the interviewer cannot distinguish candidates from approved truth;
- a required question file is truncated or unavailable.

## After the interview

The Owner may keep the next-tier model selected to save the confirmed result through a new exact repository-writing instruction. The save task must use a new task ID, current `master`, a new branch, one draft PR, and only the allowed decision-result/candidate-update paths.

Switch back to Pro/frontier before:

- approving Meta-Agent activation;
- resolving shared capability-library ownership;
- finalizing target truth/repository/privacy architecture;
- adjudicating major catalogue/selection conflicts;
- generating open-ended Fable research design;
- deciding broad migration or impact policy.
