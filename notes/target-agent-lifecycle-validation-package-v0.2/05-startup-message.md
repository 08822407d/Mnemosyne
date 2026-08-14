# Validation Startup Message

> Use only after the package is merged to execution-time latest `master` and the Owner has completed `00-run-scope-and-owner-decision.md`. This message does not itself authorize repository creation, writes, V0, V1 or quota use.

```text
@GitHub 请执行 MNE-TARGET-LIFECYCLE-VALIDATION-PACKAGE-002 的已授权阶段。

从执行时最新的 08822407d/Mnemosyne@master 读取并严格执行：

1. notes/target-agent-container-evolution-and-dependency-model-candidate-v0.2.md
2. notes/validation-designs/target-agent-container-evolution-and-dependency-model-validation-v0.2.md
3. notes/target-agent-lifecycle-validation-package-v0.2/README.md
4. notes/target-agent-lifecycle-validation-package-v0.2/00-run-scope-and-owner-decision.md
5. notes/target-agent-lifecycle-validation-package-v0.2/01-synthetic-fixture-and-scenario-contracts.md
6. notes/target-agent-lifecycle-validation-package-v0.2/02-next-tier-executor-taskbook.md
7. notes/target-agent-lifecycle-validation-package-v0.2/03-mechanical-checks-and-rubric.md
8. notes/target-agent-lifecycle-validation-package-v0.2/04-run-manifest-and-result-template.md
9. 当前消息附带或明确引用的 Owner validation_run_authorization

第一轮只返回 validation_package_receive，列出：

- package / candidate / validation ID；
- execution-time latest master commit；
- required files read / missing；
- Owner authorization ref 和 phase scope；
- 合成仓库/存储位置、可见性、pinned base；
- allowed writes 和 prohibited repositories；
- material class；
- product surface 与用户可见选择原文；
- backend 状态 unknown_or_not_attestable；
- real-repository no-write 证明方法；
- disposition PASS 或 BLOCKED。

如果仓库、材料安全、权限、阶段、文件身份或 no-write 证明方法有任何关键缺失，只返回：

TARGET_LIFECYCLE_VALIDATION_RECEIVE_BLOCKED — <原因>

并且不要创建仓库、分支、文件、fixture 或运行任何场景。

Receive 通过以后，只执行 Owner 明确授权的阶段：

- V0_ONLY：只做表面/身份/材料/权限/no-write 基线和零实质场景 sentinel，然后返回完整 V0 bundle 并停止；
- V0_AND_V1_IF_V0_PASSES：仅当授权原文明确包含该范围且 V0 有效时才进入 V1；
- 其他情况按授权中的 REVISE / DEFER / STOP 处理。

V1 必须使用单独的 public/synthetic repository，不得写 Mnemosyne、Meta-Agent 或真实业务目标；不得使用私有材料、凭据、真实学习记录或客户代码；不得运行 Deep Research/Fable；不得在执行时修改 candidate/validation 语义；不得自行补全 TLR-03/TLR-04 延期项。

执行 S0–S11 时：

- 每个写任务一 task ID、一 canonical branch，先声明 exact write set；
- 保存每次尝试、commit、diff、错误和重试；
- 运行 package 指定的机械检查；
- 缺少事实时停止，不得猜测；
- 结束时提供 Mnemosyne、Meta-Agent 和已列真实目标的 before/after ref 比较；
- 完整最终结果必须出现在最终回答正文中，文件只能是辅助副本。

本启动消息不授权 target adoption、Meta-Agent 修改、execution source 修改、PR/merge、结果写回 Mnemosyne 或任何未在 Owner authorization 中列出的动作。
```

## Execution intent

```yaml
response_role: frozen_public_synthetic_validation_executor
execution_disposition: RUN_ONLY_AFTER_PACKAGE_MERGE_AND_EXPLICIT_OWNER_RUN_AUTHORIZATION
default_phase: V0_ONLY
validation_repository_creation_authorized_by_this_file: false
validation_execution_authorized_by_this_file: false
external_quota_authorized: false
```
