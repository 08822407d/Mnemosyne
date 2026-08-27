# 阶段1 专题05 — 成本与流程重量评审

```yaml
track_id: FABLE5-REVIEW2-001
record_type: composite_review_theme_report
theme: cost_and_process_weight
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: mixed_per_claim_labels
authority_level: non_execution_source_advisory_evidence
```

评审问题：治理流程的重量是否与其防护价值成比例；负担落在谁身上（Owner 时间、模型上下文、任务数）。Owner 已两次表达负担关切（Issue #265 评论区，199 §1 引用；2026-08-22 对本轨道的通俗化指令），本专题为该关切提供量化基础。

## R2-COST-001 — 指导加载负担：已确诊、已开方、未服药，且继续加重

- severity: REPAIR_RECOMMENDED（本专题最高优先级）
- claim: VERIFIED_REPOSITORY_FACT
- 证据链（时间序）：
  1. 2026-08-11 MNEMOSYNE-199 utilization review 确诊：loader 要求每次刷新必读 11 文件，"over-broad"（F1）；重复规则解析负担（F4）；并给出处方——核心 3 文件 + 9 个条件模块（§6.1/6.2），存为 `notes/runtime-guidance-load-profile-candidate-v0.1.md`。
  2. 其后 MNEMOSYNE-210（08-14）与 225（08-15）把两份新 guard **加入必读清单**：`commands/load-mnemosyne-guidance.md` 现要求 12 文件+自身=13 必读，写入类任务再加 2~3 份条件文件（git log -- commands/load-mnemosyne-guidance.md；文件 Required files 节）。
  3. load-profile 候选至今停留在 candidate（文件名与状态未变）。
- 量化：13 份 guard 共约 3336 行；加 spec 268 行、loader 194 行、README——一次全量刷新约 **3800+ 行规则文本**，其中大部分与任意给定任务无关（199 F1 的逐项论证）。
- 内容：仓库自己的评审发现了病、开了方，但修复走的是"再加 guard"的老路径——每个新 guard 的创建任务顺手把自己加进必读清单，没人有权限/职责执行 199 的收缩方案。这是流程自增重的机制性实证。
- 建议方向：把"采纳 199 load-profile（或其修订版）"作为独立小任务提交 Owner；同时规定新 guard 默认进条件清单而非必读清单。

## R2-COST-002 — 记账开销：约四分之一的任务在处理其他任务的状态

- severity: OBSERVATION（量化）
- claim: VERIFIED_REPOSITORY_FACT（计数）+ MODEL_INFERENCE（比例解读）
- 证据：第一轮时点后 146 个合并 PR 的标题中，34 个（≈23%）匹配 closeout/post-merge/sync/finalize/repair-residue/reconcile 模式（git log --merges 计数，模式清单见命令记录）；典型链条：实质任务 → PR finalization 任务 → post-merge closeout 任务 → 状态 sync 任务（如 157→159、160→161→162；241→242）。
- 内容：每个实质动作平均拖带 0.3~0.5 个纯记账任务。记账内容本身质量高（这正是专题04 能开出台账的原因），但其**颗粒度**是为"每任务都可能是最后一个任务"的断续工作模式设计的。Claude Code 这类持续会话 + 免打扰权限的工作面出现后，同等保全可以用更低的任务开销达成（本轨道：一个任务号内多次提交+推送，记账在文件头与 commit 尾注中随行完成）。
- 建议方向：不废除 result record，而是允许"同会话连续多步共享一个任务号与一份收尾记录"成为显式合规模式（现行 guard 未禁止但也未确认；单活跃 PR 规则已天然兼容）。

## R2-COST-003 — 发布事故链的成本剖面与通道教训

- severity: OBSERVATION
- claim: VERIFIED_REPOSITORY_FACT
- 证据：MNEMOSYNE-235~239 五个连续任务 BLOCKED_CLOSED_NO_RETRY（2026-08-18~20，F2 status publication_closeout 节）；两次 Pro 法证裁定（dual-failure、execution-surface）；恢复路径 = 240 保全 capsule + 241 本地确定性 git 通道发布（91 文件，PR #303）+ 242 closeout。事故链根因中平台执行面问题占主导（execution-surface 裁定），选定恢复架构明文为 "UBUNTU_24_04_LOCAL_DETERMINISTIC_GIT_PHASE_A"。
- 内容：一次 91 文件的发布花费了 7 个任务号、5 次失败、2 次法证裁定、3 天。教训已资产化（恢复架构、capsule 模式）。成本上最值得注意的是：**最终成功的通道正是本地 git**——与本轨道现在打通的 Claude Code 写入通道同类。这从成本侧支持双通道常态化（详见专题06 R2-SPOF-003）。
- 对照 [VERIFIED_REPOSITORY_FACT]：本轨道至今 5 次推送 0 失败、0 人工干预。

## R2-COST-004 — 外部研究成本纪律良好（正面）

- severity: OBSERVATION（正面）
- claim: VERIFIED_REPOSITORY_FACT
- 证据：FCV 路线 $8+$7 两次失败探针后，成本控制被制度化：禁止重复付费探针、每任务一次 Research 调用、G0 语义覆盖门前置（current/fable5-research-delivery-status.md §4 cost_controls）；Owner 暂停决定本身即成本止损。
- 内容：付费外部动作的成本治理成熟，无需修复。挥霍风险主要在上下文/任务开销侧（001/002），不在付费调用侧。

## R2-COST-005 — Onboarding 层是减负的正确方向，但三层重复未消

- severity: NON_BLOCKING
- claim: VERIFIED_REPOSITORY_FACT
- 证据：MNEMOSYNE-243 onboarding 四件（约 400 行）使本轨道冷启动仅需读 4 份文件即可安全行动（本轨道定向报告验证）；但 onboarding、loader（34 条 high-signal 复述）、13 份 guard 全文三层之间大量内容重复（199 F3/F4 已列举），且 onboarding 与 loader 的关系（谁是入口、何时必须升级读全文）未成文。
- 建议方向：与 R2-COST-001 同一修复任务处理——确立"onboarding=冷启动入口、loader=行为刷新调度表、guard 全文=触发时按需读"的三层分工声明。

## R2-COST-006 — 结构性根因：只有加法机制，没有整合机制

- severity: REPAIR_RECOMMENDED（结构级）
- claim: MODEL_INFERENCE（基于 001/002/005 与 40 天 guard 增长史的归纳）
- 内容：每次事故产生一份新 guard（正确的即时反应），但不存在任何机制回答"现有 guard 是否可合并、降级、退役"。结果是单调增长：13 份 guard、3336 行、必读清单只进不出。199 是第一次整合尝试，其建议因无承载机制而搁浅（001 的证据链）。对比：软件工程中 lint 规则集、法规体系都有定期整编（consolidation）惯例。
- 建议方向（供门3 候选设计题）：设立轻量"guard 整编周期"——每 N 周或每 M 个新 guard 触发一次整合评审，产出合并/降级/退役提案交 Owner 批准。可与 R2-CONF-005（guard 层地位）合并为同一个设计题：**规则层治理设计**。

## 小结

成本问题的主体不是浪费性支出（付费侧纪律良好），而是**规则文本与记账任务的复利式增长**：加载负担已确诊未治（001）、记账占比 23%（002）、增长无整合对冲（006）。两条 REPAIR 级发现都指向同一个门3 候选设计题：规则层治理（与专题02 R2-CONF-005 合流）。
