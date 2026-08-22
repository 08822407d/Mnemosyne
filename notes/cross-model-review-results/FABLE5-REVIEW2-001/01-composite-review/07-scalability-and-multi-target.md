# 阶段1 专题07 — 可扩展性与多目标项目评审

```yaml
track_id: FABLE5-REVIEW2-001
record_type: composite_review_theme_report
theme: scalability_and_multi_target
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: mixed_per_claim_labels
authority_level: non_execution_source_advisory_evidence
```

评审问题：若按 Owner 已宣布的方向（Issue #265 TODO 2）同时启动真实需求 A（工作代码库）与 B（外语教师），现有结构、流程与防护是否撑得住"两个以上目标项目并行"。§9/§16 为对照基准。

## R2-SCALE-001 — 单目标全生命周期模式已验证，但单位成本高

- severity: OBSERVATION
- claim: VERIFIED_REPOSITORY_FACT（过程）+ MODEL_INFERENCE（成本判断）
- 证据：Meta-Agent 迁移链（MNEMOSYNE-189~195 + meta-agent-* 任务，共 10+ 任务、约一周）产出的可复用资产：迁移评估设计、taskbook、机械 inventory 的 Codex 任务模式、shadow-copy/rollback/no-dual-writer 验证设计、迁移交接模板（notes/migration-designs/、notes/validation-designs/、notes/templates/ 对应文件）。
- 内容：从 bootstrap 工作区到专属仓库毕业的全流程有了模板。但该流程为"第一次、高防护"设计——若 A/B 两个项目照原样走，仅迁移阶段就是 20+ 任务。§16 工作区模式本身可复用；需要的是**分级版流程**（低风险项目走轻通道）。
- 建议方向：把"目标项目流程分级"（full/standard/light）列为 A/B 立项时的前置小设计，直接取材现有模板做裁剪，而非新建。

## R2-SCALE-002 — 并发安全设计（F2）恰好停在门前，与 A/B 立项形成依赖关系

- severity: REPAIR_RECOMMENDED（依赖排序级）
- claim: VERIFIED_REPOSITORY_FACT（状态）+ MODEL_INFERENCE（依赖判断）
- 证据：MNE-DR-005 的研究对象正是"跨仓库安全并发与有序工作"（display_name 跨仓库并发；amendment candidate 文件名 cross-repository-safe-concurrency-and-ordered-work）；其 V2-A 验证停在 Owner G2A 签发门（D-01）。
- 内容：A/B 同时立项即产生 Mnemosyne + 两个目标仓库（未来）+ 验证仓库的多仓库并发写入场景——正是 F2 要解决的问题。当前防护（single-active-PR guard 等）是**单仓库内**谱系控制；跨仓库的写入排序、无双写者约束只有设计与部分验证，未验收。
- 建议方向（供分诊）：三种可选排序——(a) 先完成 F2 A1 再开 A/B（安全优先，慢）；(b) A/B 先行但限定"同一时刻只动一个仓库"的人工纪律（快，靠自觉）；(c) A/B 先行 + 把 F2 已有的 no-dual-writer 设计降级为轻量 checklist 先用（折中）。这是门3 应呈交 Owner 的结构性选择题。

## R2-SCALE-003 — 工作区与模板基础设施就绪度良好（正面）

- severity: OBSERVATION（正面）
- claim: VERIFIED_REPOSITORY_FACT
- 证据：`target-projects/` 布局与边界规则（§16 + workspace-boundary proposal + skeleton templates v0.1，MNEMOSYNE-063）；intake 表单族（first-target-project-intake-and-approval-forms、filling guide）；交付/manifest/handoff 模板族（PRO-SLICE-01 已把硬契约传播进这 9 个下游模板文件——专题定向 c.4）；per-target schema 原则（§9）。
- 内容：A/B 立项的文书基础设施是现成的，且刚被 PRO-SLICE-01 统一过一轮硬契约。立项的主要成本不在模板缺失，而在 Owner 决策（目标选择、安全边界、材料脱敏——真实需求 B 涉及 Owner 个人学习数据，§16 公开仓库约束将立即生效并可能要求外置存储决策 [MODEL_INFERENCE]）。

## R2-SCALE-004 — 任务号单序列是多写入方并行的碰撞点

- severity: NON_BLOCKING → 随并行度上升
- claim: VERIFIED_REPOSITORY_FACT（现状）+ DESIGN_RECOMMENDATION
- 证据：MNEMOSYNE-NNN 为全局串行序列，分配靠会话自觉（无 registry 锁）；两个月内已出现非 MNEMOSYNE 序列的自然分化：meta-agent-* 任务名、WORK-ULTRA-* 轨道、PRO-SLICE、TLR/OR 系列、本轨道 FABLE5-REVIEW2-001——多序列实践已存在，只是无成文规则。235–239 事故链还显示了同一序列内任务号消耗过快的问题（5 个号消耗于同一次发布重试）。
- 内容：两个 AI 族 + 多项目并行时，"下一个号是几"会成为跨会话协调点与撞号源。现实已经用"轨道自带前缀"解决了一半。
- 建议方向：署名方案联合确认时顺带确认命名规则——全局序列保留给 Mnemosyne 主线维护，长轨道/目标项目用自有前缀（现状追认即可，成本近零）。

## R2-SCALE-005 — 独立验证仓库模式是已验证的可复用资产（正面）

- severity: OBSERVATION（正面）
- claim: VERIFIED_REPOSITORY_FACT
- 证据：`08822407d/mnemosyne-target-lifecycle-validation-002` 承载了 TLR-V1（S1–S9、S11 合成场景）与 F2-A0 sentinel 两轮验证；合成 fixture + 分支隔离 + controller/worker 模式 + owner 门；Mnemosyne 侧只存 receipt 与 blob 锚。
- 内容："在隔离仓库里做危险动作、主仓库只留证据锚"的模式两次成功，天然适配未来 A/B 的记忆系统 dry-run。配套缺口是 D-06 的证据保全设计（外部分支寿命无保障，专题06 R2-SPOF-005）。

## R2-SCALE-006 — 规则层不随项目数扩展（承接专题02/05）

- severity: OBSERVATION（指针）
- claim: MODEL_INFERENCE
- 内容：13 份 guard 几乎全部是"每写入动作"生效，与项目数无关——这意味着规则负担不随项目线性增长（好）；但 per-route status 文件模式**是**线性增长的（每路线一份，现已 ~30 份 status/route 文件），且其过期问题（专题03）会随路线数放大。若 A/B 各带 3~5 份 status 文件，"总览缺位"（R2-FRESH-003）将从不便升级为危害。
- 建议方向：与 R2-FRESH-003 的总路标决策合并处理；在 A/B 立项前定下"每项目 status 文件上限与强制 last_updated 字段"的轻约定。

## 小结

基础设施侧（模板、工作区、验证仓库模式）就绪度好于预期，两条正面发现；真正的扩展瓶颈是三个排序/治理决策：**F2 并发门与 A/B 立项的先后（002，最重要）**、流程分级（001）、状态文件模式的放大效应（006）。无 BLOCKING。
