# Branch-Backed Same-Conversation Startup Message — Target-Lifecycle Owner Review

> Use after MNEMOSYNE-207 is merged to execution-time latest `08822407d/Mnemosyne@master`. This supersedes `07-same-conversation-startup-message.md` for starting this package.

```text
@GitHub 现在开始执行由 Pro 模型准备的“目标 Agent 承载、演化与依赖责任”人工复核包。不要把当前对话此前的模型记忆或聊天内容当成仓库真相，也不要启动 handoff。

请从执行时最新的 `08822407d/Mnemosyne@master` 按顺序读取：

1. `current/human-approved-spec.md`
2. `current/owner-review-branch-ledger-guard.md`
3. `notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002.md`
4. `notes/owner-decision-results/MNE-FIRST-THREE-SYSTEMS-OWNER-REVIEW-RESULT-002-CORRECTION-001.md`
5. `notes/audits/first-three-systems-owner-review-transcript-audit-v0.1.md`
6. `notes/first-three-system-capability-selection-v0.3.md`
7. `notes/target-agent-container-evolution-and-dependency-model-candidate-v0.1.md`
8. `notes/target-agent-container-evolution-and-dependency-frontier-adjudication-v0.1.md`
9. `notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.1.md`
10. `notes/owner-review-packages/target-agent-lifecycle-v0.1/README.md`
11. `notes/owner-review-packages/target-agent-lifecycle-v0.1/01-context-and-fixed-boundaries.md`
12. `notes/owner-review-packages/target-agent-lifecycle-v0.1/02-decision-workbook.md`
13. `notes/owner-review-packages/target-agent-lifecycle-v0.1/03-qa-guide.md`
14. `notes/owner-review-packages/target-agent-lifecycle-v0.1/04-next-tier-interviewer-contract.md`
15. `notes/owner-review-packages/target-agent-lifecycle-v0.1/05-answer-ledger-and-result-template.md`
16. `notes/owner-review-packages/target-agent-lifecycle-v0.1/06-source-map-and-on-demand-reading.md`
17. `notes/owner-review-packages/target-agent-lifecycle-v0.1/08-branch-backed-interview-amendment.md`

不要默认读取根 `README.md`、loader、active-context、handoff-current、TODO、open questions、完整历史对话、完整研究报告、旧 OR 包、Meta-Agent 历史树、业务目标仓库或暂停的 FCV/Fable 路线材料。完整对话导出已经完成差异审计，但原文件没有发布到公共仓库；普通访谈不得依赖聊天记忆或要求读取该私有原件。

第一步只返回 `target_lifecycle_owner_review_receive`，说明 package ID、最新 master、必读文件、result/correction/candidate/adjudication/validation 身份、未读取冷材料、执行源、禁止动作和当前问题 `TLR-01`。如果身份冲突、文件缺失或包重大过期，只返回 `TARGET_LIFECYCLE_OWNER_REVIEW_RECEIVE_BLOCKED — <原因>`，并且不要创建分支或写文件。

receive 通过后，创建或继续唯一工作分支：

`mnemosyne-tlr-owner-review-001-ledger`

工作目录限定为：

`notes/owner-review-working/MNE-TARGET-LIFECYCLE-OWNER-REVIEW-001/`

先返回 `owner_review_branch_ledger`，列出 base SHA、branch、working root、当前 head、当前问题和写入边界。若同名分支已存在，核验 package/task 身份后继续；不得创建第二分支。所有写入只限人工复核证据，不得修改 execution source、active guards、candidate、validation、Meta-Agent 或目标仓库，也不得创建 PR。

然后一次只问一个问题，从 `TLR-01` 到 `TLR-05`。每个重要回答后：

1. 区分保存用户原话/安全精确引用与 interviewer interpretation；
2. 让我纠正或确认；
3. 更新同一分支中的 `answer-ledger.md`；
4. 再进入下一题。

完成五题后，在同一工作目录形成 `final-result-candidate.md`，给出完整结果和自然语言总结，等待我确认。确认后也不要创建 candidate v0.2、运行验证、修改目标或创建 PR，直到我切换到 Pro 并给出后续授权。

若出现 execution source、target truth、writer authority、自动传播、共享实时状态、无界并发、双亲仓库重新成为 live target、私人/信任边界、目标激活或高影响迁移，标记 `FRONTIER_REENTRY_REQUIRED`，保存当前 ledger 后停止受影响问题。
```

## Execution intent

```yaml
response_role: branch_backed_owner_review
execution_disposition: RUN_AFTER_MNEMOSYNE_207_MERGE_AND_OWNER_SELECTION
external_research_or_quota_authorized: false
```
