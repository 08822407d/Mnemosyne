# V1 Three-Conversation Operator Flow and Startup Messages

> Prepared operator flow only. **Do not run** until MNEMOSYNE-212 is merged and the Owner explicitly confirms `MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001`, producing an exact V1 authorization record. These messages do not themselves authorize V1, repository writes, model switching or quota use.

```yaml
execution_package_id: MNE-TARGET-LIFECYCLE-V1-EXECUTION-PACKAGE-001
file_role: three_conversation_operator_flow_and_startup_messages
status: prepared_do_not_run
base_display_name: MNE-DR-003 生命周期验证
canonical_run_id: MNE-TARGET-LIFECYCLE-V1-001
```

## 1. Execution intent

```yaml
execution_intent:
  response_role: ANALYSIS_AND_PREPARATION
  task_id: MNE-TARGET-LIFECYCLE-V1-001
  execution_disposition: RUN_AFTER_GATE_OPTIONAL
  prerequisite_gates:
    - MNEMOSYNE_212_Ready_PR_merged
    - Owner_confirms_MNE_TARGET_LIFECYCLE_V1_RUN_DECISION_CANDIDATE_001
    - exact_V1_authorization_record_exists_on_latest_Mnemosyne_master
  external_execution_or_quota_authorized: false_until_gate
```

After those gates, use exactly three conversations:

| Order | Chat/UI name | Model class | Role |
|---:|---|---|---|
| 1 | `MNE-DR-003 Execute` | next-tier | controller, fixture, Core, S7, S11, S8 preparation, later closeout |
| 2 | `MNE-DR-003 S8` | next-tier | **mandatory fresh** negative documentation worker |
| 3 | `MNE-DR-003 Review` | **Pro/frontier** | **mandatory fresh** semantic adjudicator |

Recommended next-tier visible selection, only if still available at launch:

```text
gpt-5.6 sol extra high
```

Record the actual displayed model/mode and any separately displayed reasoning setting verbatim in every conversation. Do not infer backend identity.

## 2. Common preparation

Before launching V1:

1. verify the exact V1 Owner authorization exists on execution-time latest `08822407d/Mnemosyne@master`;
2. verify `08822407d/mnemosyne-target-lifecycle-validation-002@master` still equals the authorized pinned base `e8e3296922185b4b70997c2351d6f39423f2cd4f` before the first V1 write;
3. keep GitHub connected; a separate ChatGPT repository-sync selection is not required when the connector resolves the repository, but every conversation performs an access preflight;
4. do not attach private files or complete old conversations;
5. do not enable Web, Deep Research, Fable or other connected apps;
6. do not supply the Execute conversation transcript or S7 facts to S8;
7. do not delete V1 task branches until fresh Pro adjudication releases them.

If any precondition fails, stop before repository write.

---

# Conversation 1 — `MNE-DR-003 Execute`

## 3. Main execution launch message

```text
@GitHub 请执行已获 Owner 授权的 MNE-TARGET-LIFECYCLE-V1-001 主执行阶段。

从执行时最新的 08822407d/Mnemosyne@master 读取并严格执行：

1. notes/target-agent-container-evolution-and-dependency-model-candidate-v0.2.md
2. notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.2.md
3. notes/target-agent-lifecycle-validation-package-v0.2/README.md
4. notes/target-agent-lifecycle-validation-package-v0.2/01-synthetic-fixture-and-scenario-contracts.md
5. notes/target-agent-lifecycle-validation-package-v0.2/02-next-tier-executor-taskbook.md
6. notes/target-agent-lifecycle-validation-package-v0.2/03-mechanical-checks-and-rubric.md
7. notes/target-agent-lifecycle-validation-package-v0.2/04-run-manifest-and-result-template.md
8. notes/validation-adjudications/MNE-TARGET-LIFECYCLE-V0-ADJUDICATION-001.md
9. notes/validation-run-decisions/MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001.md
10. Owner 已确认的 MNE-TARGET-LIFECYCLE-V1-RUN-AUTHORIZATION-001
11. notes/target-agent-lifecycle-v1-execution-package-001/README.md
12. notes/target-agent-lifecycle-v1-execution-package-001/00-controller-fixture-and-branch-contract.md
13. notes/target-agent-lifecycle-v1-execution-package-001/01-core-cell-s1-s6-s9.md
14. notes/target-agent-lifecycle-v1-execution-package-001/02-positive-documentation-cell-s7.md
15. notes/target-agent-lifecycle-v1-execution-package-001/04-backup-restore-cell-s11.md
16. notes/target-agent-lifecycle-v1-execution-package-001/05-mechanical-closeout-and-return.md
17. notes/target-agent-lifecycle-v1-execution-package-001/07-integrity-checklist.md

当前界面显示的模型/模式原文：<启动时原样填写>。
若另有独立推理设置：<原样填写或写无独立设置>。

第一轮只返回 v1_execute_receive，列出：
- 所有 ID 与 exact source commit/blob；
- Owner V1 authorization ref、selected/excluded scenarios；
- synthetic repository、visibility、当前 master 与授权 pinned base；
- V0 evidence 完整性；
- controller / fixture / task branch map；
- Mnemosyne 与 Meta-Agent before refs；
- S8 sanitized branch 和 knowledge firewall 方法；
- allowed/prohibited writes；
- product surface、可见模型/模式原文、backend unknown_or_not_attestable；
- disposition PASS 或 BLOCKED。

若 receive 通过：

A. Controller/fixture
- 创建 execution package 指定的 controller、fixture 和 task branches；
- 生成冻结 fixture、task contracts、no-write baseline；
- 在运行 S7 以前，从 fixture commit 创建并准备隔离的 S8 branch，只写 sanitized input 和 isolation receipt；
- 不运行 S8。

B. Core logical cell
- 按冻结合同运行 S1、S2、S3、S4、S5、S6、S9；
- 每个 task 只写自己的 canonical branch；
- 保存 exact input/output/blob/commit、失败、重试和 provisional disposition。

C. Positive S7 logical cell
- 先完成 CommonLib v2 library branch 的 API、测试、人类版变化说明、Agent 版迁移说明和文档总览；
- 机械核验充分后，再从 library final commit 执行 Owner 触发的 Alpha migration branch；
- 不把任何 S7 输出写入或发送到 S8 branch。

D. S11 logical cell
- 在 S11 branch 创建 source-identified backup A/B，模拟 primary loss 与 backup A failure，并从 backup B 恢复 Alpha；
- 保存 source/snapshot/failure/restore identity；不配置真实备份。

禁止：运行 S8、S10、V2；创建 scenario PR；写 Mnemosyne、Meta-Agent 或真实目标；使用私有材料、Web/Deep Research/Fable/其他 app 或外部 quota；修改 candidate/package 语义。

完成 A–D 后，返回：
- controller/fixture/core/S7/S11 完整结果与所有 exact refs；
- S8 isolation receipt、branch head、sanitized worker input refs；
- 一段可直接发送到全新 S8 对话的启动消息；
然后停止，等待 S8 返回。不要提前做最终 closeout。
```

## 4. Main-executor pause gate

Before asking the Owner to launch S8, `MNE-DR-003 Execute` must show:

```yaml
S8_launch_gate:
  S8_branch:
  S8_base:
  S8_head:
  S7_commits_not_in_S8_history:
  sufficient_guide_absent:
  sanitized_input_refs: []
  forbidden_paths_absent:
  branch_inventory_ref:
  isolation_receipt_ref:
  disposition: PASS | BLOCKED
```

Only `PASS` permits the fresh S8 launch.

---

# Conversation 2 — `MNE-DR-003 S8`（必须全新）

## 5. Fresh S8 launch message

Create a new chat that has never seen S7, the Execute transcript or the exact synthetic v2 migration facts. Do not paste the whole V1 package. Send only the following, filling the exact refs returned by Execute:

```text
@GitHub 请执行 MNE-TARGET-LIFECYCLE-V1-001 的 S8 Fresh Negative Documentation Cell。

这是全新隔离对话。你不得读取或搜索 S7 branch/output、充分的 Agent 迁移说明、frozen package 的具体 v2 contract 段落或其他包含隐藏迁移答案的材料。

只允许从执行时最新的 08822407d/Mnemosyne@master 读取：
1. MNE-TARGET-LIFECYCLE-V1-RUN-AUTHORIZATION-001
2. notes/target-agent-lifecycle-v1-execution-package-001/README.md
3. notes/target-agent-lifecycle-v1-execution-package-001/03-fresh-negative-documentation-cell-s8.md

只允许从 08822407d/mnemosyne-target-lifecycle-validation-002 读取：
- branch：tlr-v1-s8-insufficient-docs
- exact base/head：<Execute 填写>
- sanitized worker input refs：<Execute 填写>
- Alpha 当前 v1 项目文件；
- S8 isolation receipt：<Execute 填写>。

当前界面模型/模式原文：<启动时原样填写>。

第一轮只返回 s8_fresh_receive，声明：
- 当前对话未接收 S7 或隐藏迁移答案；
- exact allowed files/branch；
- forbidden sources；
- Alpha write prohibition；
- isolation receipt PASS/BLOCKED；
- backend unknown_or_not_attestable。

若隔离不能证明，只返回 S8_RECEIVE_BLOCKED，不写入。

通过后判断现有变化说明是否足以安全迁移 Alpha。不得根据版本号、惯例、名称或外部知识猜测新合同。信息不足时应停止，说明缺少哪些信息类别，并且只写 run-evidence/S8/output/。不得修改 Alpha、CommonLib 或其他路径；不得读取其他 branch；不得创建 PR。

完成后返回完整 negative_documentation_cell_result、Alpha before/after unchanged 证明、输出 blob+commit 和任何 contamination/invention finding，然后停止。
```

If contamination occurs, preserve the attempt and do not retry in the same chat.

---

# Return to Conversation 1 — `MNE-DR-003 Execute`

## 6. Mechanical closeout continuation

After S8 stops, return to the original Execute chat. Supply its complete final response or exact result refs, then send:

```text
@GitHub 现在执行 MNE-TARGET-LIFECYCLE-V1-001 的 Mechanical Closeout。

Fresh S8 exact result refs：<填写>。

严格执行：
- notes/target-agent-lifecycle-v1-execution-package-001/05-mechanical-closeout-and-return.md
- frozen package 03-mechanical-checks-and-rubric.md
- frozen package 04-run-manifest-and-result-template.md

先核验所有 branch/base/head/blob/commit、S8 isolation、incident/retry 和 selected scenario completeness。再执行 M0–M11 适用检查、declared-vs-actual write-set 汇总，以及 Mnemosyne/Meta-Agent exact before/after no-write comparison。

不得修复 scenario 语义、运行 S10/V2、重跑失败 cell、写 Mnemosyne/Meta-Agent/真实目标、创建 PR 或作出全局架构接受结论。

完成后把完整 V1 result bundle 写入 synthetic repository 的授权路径，并在最终回复正文中给出完整 decision-relevant summary 和 fresh Pro return package，然后停止。
```

Required routing result:

- `V1_BUNDLE_COMPLETE_READY_FOR_FRESH_PRO`
- `V1_BUNDLE_COMPLETE_WITH_BLOCKERS_READY_FOR_FRESH_PRO`
- or one frozen blocked/invalid/protocol disposition.

---

# Conversation 3 — `MNE-DR-003 Review`（必须全新 Pro）

## 7. Fresh Pro adjudication launch message

Create a new Pro chat that executed no V1 task. Load GitHub and send:

```text
@GitHub 请作为 fresh Pro adjudicator 复核 MNE-TARGET-LIFECYCLE-V1-001。

从执行时最新的 08822407d/Mnemosyne@master 读取：
1. candidate v0.2
2. validation v0.2
3. frozen package README、03、04
4. MNE-TARGET-LIFECYCLE-V0-ADJUDICATION-001
5. MNE-TARGET-LIFECYCLE-V1-RUN-DECISION-CANDIDATE-001
6. MNE-TARGET-LIFECYCLE-V1-RUN-AUTHORIZATION-001
7. notes/target-agent-lifecycle-v1-execution-package-001/README.md
8. notes/target-agent-lifecycle-v1-execution-package-001/05-mechanical-closeout-and-return.md

然后只从 08822407d/mnemosyne-target-lifecycle-validation-002 读取 Execute return package 列出的 exact V1 result bundle、logical-cell results、task branches/commits/blobs 和争议所必需的具体文件。不要先 broad-read 全仓库。

第一轮只返回 v1_adjudication_receive，列出 exact inputs、review criteria、context independence、缺失项和 PASS/BLOCKED。

通过后区分 candidate defect、validation protocol defect、executor defect、contamination、missing evidence 和 noncritical observation；复核 S8 firewall、no-write proof、S11 restore、全部 baseline-critical scenarios 和 TLR-03/TLR-04 deferral fidelity。

选择冻结 package 允许的一个 Pro disposition，并清楚说明证据、限制、建议 amendments（未采用）和需要 Owner 决定的事项。

不得修改 candidate/validation/execution source/Meta-Agent/真实目标；不得运行 rerun、S10、V2、Deep Research 或 Fable；不得把结果写回 Mnemosyne，除非收到另行明确的 repository-write authorization。
```

## 8. Return and stop contract

The fresh Pro response returns to the Owner/Mnemosyne maintenance route with:

- one exact Pro disposition;
- candidate/protocol/executor findings;
- scenario summary and critical evidence;
- unresolved disputes;
- proposed non-adopted amendments;
- whether an independent heterogeneous review adds non-duplicative value before global acceptance;
- the exact Owner architecture decision required.

No executor or adjudicator may proceed to architecture adoption, real-target migration, S10, V2, cleanup or Mnemosyne ingestion without later explicit gates.