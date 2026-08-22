# 阶段1 专题04 — 验收债台账

```yaml
track_id: FABLE5-REVIEW2-001
record_type: composite_review_theme_report
theme: acceptance_debt_register
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: mixed_per_claim_labels
authority_level: non_execution_source_advisory_evidence
risk_scale: [HIGH, MEDIUM, LOW]
```

定义：验收债 = 仓库中处于 BLOCKED / NOT_RUN / open_uncertain / not_performed / DEFER / 等待 Owner 决定状态、且未被显式关闭或显式接受为永久状态的事项。**如实挂账本身是仓库的优点**；本台账的目的是让 Owner 一览全部欠账并决定"还、销、或显式永久接受"。

## 正面前提：真实 Owner 验收机制已于 8 月建立

[VERIFIED_REPOSITORY_FACT] 第一轮时代的核心验收弱点（F-002/F-004：同族自证、维护者评审无人类逐步核验）已实质改善：OR-01~09 与 TLR-01~05 Owner review 完成（`current/first-three-systems-owner-review-status.md`）；V1 裁定经 Owner 独立复核接受；F2 的每个 package 都有对应 owner-decision 记录（`notes/owner-decision-results/` 14 份）。验收债的性质从"没有人类验收机制"变为"具体事项排队待决"。

## 台账（按风险降序）

| # | 债项 | 状态 | 风险 | 证据 | 处置建议（供分诊） |
|---|---|---|---|---|---|
| D-01 | F2/MNE-DR-005 跨仓库并发停在 Owner G2A 签发门；A1 packages 001–004 已封存、机械校验器已合并、readiness PASS | 等 Owner 决定 | **HIGH**（时间敏感：这是最新活路线，语境最热；且是多目标并发的先决能力，见专题07） | current/fable5-cross-repository-safe-concurrency-research-status.md | Owner 三选一：签发 G2A 执行 A1 / 显式挂起并记录 / 降级关闭。拖延本身就是决定（语境冷却、packages 老化） |
| D-02 | Issue #265 四个 workstream 过窗未结算；真实需求 A/B 零落地 | 部分完成、无结算 | **HIGH**（方向级） | Issue #265；R2-CORE-002 | 轻量结算 + A/B 立项决定（与门3 选题直接相关） |
| D-03 | 机械 no-write 组合门 BLOCKED（Meta-Agent consolidated cleanroom replay：行为 5/5 PASS、机械证明缺） | BLOCKED（§19 合规挂账） | MEDIUM | current/review-and-validation-status.md；current/meta-agent-replay-mechanical-proof-decision.md | 对象已迁出毕业——建议 Owner 显式决定：作废（历史挂账、对象不再存在）或补一次 observer-assisted proof 作为方法学收尾。不建议默认继续挂着 |
| D-04 | HO-GUIDANCE-001：目标项目业务交接是否加载 Mnemosyne 指导 | unresolved（§15 点名的 open question） | MEDIUM（真实需求 A/B 一旦立项立即撞上） | current/handoff-guidance-open-question.md | 在 A/B 立项前决定；或先按 task-local 决定跑、明确不设先例 |
| D-05 | W4 用户验收警告 open_uncertain（源自第一个 dry-run 的验证层） | open_uncertain | MEDIUM→LOW（对象已迁出；warning 语义由分层 canonical 化承载） | review-and-validation-status.md Pro adjudication 节 | 随 D-03 一并处置：显式历史化 |
| D-06 | 16 个 tlr-v1-* 合成证据分支保留中，cleanup 需先设计持久保全 | 保留义务 | MEDIUM（外部仓库依赖，见专题06 R2-SPOF-005） | first-three-systems-owner-review-status.md Evidence retention 节 | 列入"证据保全设计"小任务（该 status 文件自己列的 optional route 3） |
| D-07 | mnemosyne-240-preservation-capsule 分支 RETAIN，待不可变正典替代或 Owner 归档决定 | 保留义务 | LOW | F2 status publication_closeout 节 | 与 D-06 同批处置 |
| D-08 | GF5-TRIAGE-001：FR-01/03 表面 delta 研究 DEFER 后未执行 | DEFER | LOW-MEDIUM | Pro decision-matrix；专题08 复检 | 重定范围或显式销账（原题部分已被现实与新事实文件覆盖） |
| D-09 | artifact-delivery Case 005 NOT_RUN（条件未自然触发） | NOT_RUN | LOW | review-and-validation-status.md | 保持挂账即可；或声明"触发即测"为永久策略 |
| D-10 | Adaptive Explanation Stage B0 smoke 执行未授权；路线待选 | 等选择 | LOW | current/adaptive-explanation-stage-b0-status.md | 与真实需求 B 合并考虑（避免平行两条教学路线） |
| D-11 | Issue #244 教学 Agent 先行使用（08-02）无后续动作 | OPEN | LOW | gh issue list | 并入真实需求 B 立项（R2-CORE-005） |
| D-12 | TLR-03/04 等 Preserved deferrals（变更分类学、parent/meta 最小内容规则等 8 项） | 有意延迟 | LOW（by design） | first-three-systems status Preserved deferrals 节 | 无需动作；已良好登记 |
| D-13 | S10/V2 未跑、S6 import 缺陷未修（仅当选择 runtime supplement 才相关） | 有意不跑 | LOW（by design） | 同上 V1 节 | 无需动作 |
| D-14 | Greenfield GF4-F03…F19 未修、DP01…15 未答 | 架构未采纳，advisory 冻结 | LOW | GF-STEP-5 §23；Pro 裁定 implementation REJECT | 无需动作；仅当某设计题重开时按题取用 |
| D-15 | FCV 路线无限期暂停（$8+$7 沉没、无有效 A1 报告） | Owner 已决定暂停 | LOW（已是显式决定，非欠账；列此为完整性） | current/fable5-research-delivery-status.md | 无需动作 |
| D-16 | §7 死条款冲突未按 §4 登记 open question | 程序债 | MEDIUM（与 R2-CONF-001 同体） | 专题02/03 | 门2 后按 Owner 批示走执行源修订 |
| D-17 | 多写入方署名方案草案待 ChatGPT Pro + Fable5 联合确认；确认前 Claude 产出维持隔离文件夹 | 等联合确认（Owner 已排期下周） | MEDIUM（阻塞 Claude 常态化写入） | 本轨道 00-orientation/03 | 按排期执行即可 |

## 结构观察

- [MODEL_INFERENCE] 债务分布健康度中等偏好：HIGH 两项都是**决策债**而非质量债——不是做坏了没验收，而是做完了等拍板。真正的质量类欠账（D-03/D-05/D-09）都源自已毕业或已关闭的对象，主要价值是方法学收尾而非风险消除。
- [MODEL_INFERENCE] 最大的隐性风险是 D-01 与 D-02 的组合：最新的活路线（并发安全）与最新的方向决定（实用化转向）都停在 Owner 面前，而 Owner 的高强度决策带宽（GPT Pro）按计划下周才恢复。本轨道门3 正好是把这些决策打包呈交的机会。
- 挂账诚实度 [VERIFIED_REPOSITORY_FACT]：抽样核对的全部状态文件都如实标注未完成态（无一处把 BLOCKED 说成 PASS）；§19 的 fail-closed 文化已内化。这是仓库可信度的基石，应在任何流程简化中保留。

## 小结

17 项挂账：2 HIGH（均为决策债）、6 MEDIUM、9 LOW（其中 4 项 by design 无需动作）。无 BLOCKING 级质量债。建议分诊阶段把 D-01/D-02/D-04/D-16/D-17 打包为"门3 Owner 决策清单"。
