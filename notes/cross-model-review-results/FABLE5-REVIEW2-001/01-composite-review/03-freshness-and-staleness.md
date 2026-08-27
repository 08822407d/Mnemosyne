# 阶段1 专题03 — 新鲜度与过期状态评审

```yaml
track_id: FABLE5-REVIEW2-001
record_type: composite_review_theme_report
theme: freshness_and_staleness
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: mixed_per_claim_labels
authority_level: non_execution_source_advisory_evidence
```

评审对象：三类新鲜度——(A) 会被新会话/新模型读到的**状态文件**是否反映现状；(B) **研究证据**是否老化；(C) **平台事实**是否过期。判定日期基准：2026-08-22。

## R2-FRESH-001 — 章程指定的启动三件套全部过期或弃用

- severity: REPAIR_RECOMMENDED
- claim: VERIFIED_REPOSITORY_FACT
- 证据（git log 逐文件）：

| 文件 | 最后实质更新 | 距今 | 现状 |
|---|---|---|---|
| current/active-context.md | 2026-07-06（MNEMOSYNE-085，d8a9182） | 47 天 | "当前阶段"停在 post-053/post-085；当前门/路线段落全部指向已完结的 Meta-Agent handoff 时代 |
| current/open-questions.md | 2026-07-06（同上） | 47 天 | 未含 07-06 后产生的任何未决问题；新未决问题散落于独立文件（handoff-guidance、model-capability-planning 等） |
| current/todo.md（Active 节） | 085 时代内容；07-26 仅恢复被误动的行（bf36cf3） | ~47 天 | Active 节仍写"等待 inserted long work 完成后恢复 post-084 路线"——该路线的对象 Meta-Agent 已于 08-05 迁出毕业 |
| handoff/handoff-current.md | 08-21 被改为弃用指针（MNEMOSYNE-240/241） | — | 自我声明"不再选择/推荐/描述 live route" |

- 内容：与 R2-CONF-001 同一事实的另一面。此处强调**危害面**：这四个文件是 §7 指定的新会话入口，也是历史上大量 handoff 材料引用的锚点。一个不知情的新会话（尤其非 GPT 族、无对话记忆的模型）照 §7 读它们，会把"恢复 post-084 Meta-Agent 路线"当成安全下一步——而那条路线的对象已经迁出，恢复动作本身会变成错误。过期状态文件不是中性的旧文档，是**指向已拆除桥梁的活路标**。
- 缓解现状：MNEMOSYNE-243 onboarding 与 199 评审已在非执行源层把它们降级为"默认不读"；但执行源 §7 与历史 handoff 包仍指向它们，两套导航并存。

## R2-FRESH-002 — 自称 live 的评审/验证总览文件含大段过期内容

- severity: REPAIR_RECOMMENDED
- claim: VERIFIED_REPOSITORY_FACT
- 证据：`current/review-and-validation-status.md` greenfield_track 段写 `latest_completed_substep: GF-STEP-2C`、`next_proposed_by_Fable: GF-STEP-3`——而 GF-STEP-3A/3B/4/3R/3RV/5 已于 07-17~21 全部完成入库（MNEMOSYNE-132~143），其后 Stage A/B、Pro 裁定、PRO-SLICE-01 实施均已完结（07-26）。该文件其余段落（cleanroom replay、artifact-delivery、DR6）仍准确。
- 内容：文件头写着"live wayfinding"，实际是"部分 live"。半新半旧比全旧更危险：读者无从判断哪段可信。
- 附带 [MODEL_INFERENCE]：该文件由 MNEMOSYNE-113 创建、后续未随 greenfield 进展更新——暴露"live 文件靠人记得去更新"这一机制弱点，见 R2-FRESH-006。

## R2-FRESH-003 — 总路标停在 08-06，此后 46 个任务的状态无汇总视图

- severity: NON_BLOCKING
- claim: VERIFIED_REPOSITORY_FACT
- 证据：`current/post-interruption-live-wayfinding-status.md` last_updated_by_task: MNEMOSYNE-197（08-06），内容止于 FCV 暂停；其后 198–243（owner review 系列、TLR/V1、F2 A1 全链、发布事故、onboarding）无任何总览级路标。当前最接近"总状态"的是 F2 专线状态文件（242 更新）+ git log。
- 内容：单路线状态文件（fable5-cross-repository-…、first-three-systems-…）各自新鲜，但"现在整个仓库有哪些活路线、各停在哪个门"这一总览自 08-06 起缺位。本轨道定向报告事实上临时充当了这个角色。
- 建议方向：要么恢复维护一个极薄的总路标（只列路线名+门+指针，无叙述），要么正式宣布"无总路标、以 per-route status 为准"并让 onboarding 指明枚举方法。

## R2-FRESH-004 — 研究证据分级老化清单

- severity: OBSERVATION（分级）
- claim: VERIFIED_REPOSITORY_FACT（日期）+ MODEL_INFERENCE（风险分级）

| 证据 | 日期 | 老化风险 | 说明 |
|---|---|---|---|
| RC-2026Q2-initial 7 报告 | ~2026-05 下旬 | **高（平台类结论）/低（理论类结论）** | 平台能力边界（ChatGPT/Claude 表面、写回通道）3 个月内已两次被现实推翻（§18 七月修正、Claude 写入面本月成立）；理论/工程依据类结论仍稳 |
| GF5-DR-001 建议的 FR-01/03 表面 delta 研究 | 判 DEFER（07-23 Pro 裁定） | 中 | 至今未执行；但其研究对象（对话表面写入机制）已被 §18 修正与 claude-github-work-surface-facts 部分事实覆盖——原题可能已不值得原样执行，见专题08 复检 |
| RC-2026Q3-platform-context-apps-delta（DR6） | 07-15 | 中 | 五周前的平台快照 |
| current/claude-github-work-surface-facts.md | 08-15（MNEMOSYNE-219） | 低 | 最新平台事实层 |
| 2026Q3 各专题 cycle（并发、能力归属、多模型裁定等） | 07-28~08-15 | 低 | 新鲜 |

- 内容：证据层的**更新机制**运转正常（新 cycle 持续入库、refresh-policy 文件在位）；老化集中在"最老的一批平台类结论仍挂着 active_evidence: yes"（index 表）。§5 的"时效性"原则有声明、缺执行钩子（没有任何文件记录"哪些 Q2 结论已被后续证据取代"的对照表）。

## R2-FRESH-005 — Owner 的高优先级窗口事项单（Issue #265）已过窗且无完成度标注

- severity: NON_BLOCKING
- claim: VERIFIED_REPOSITORY_FACT
- 证据：Issue #265（08-10 创建）设定工作窗 08-11~15、含 4 个 workstream；窗口内仓库实际推进的是 owner review/TLR/F2（对应部分 TODO 2/3 内容）；截至 base_master_sha 该 issue 仍 OPEN、正文与评论区无逐项完成度记录（gh issue view）。TODO 1（Fable 独立研究）正由本轨道执行（Owner 08-22 工作令）；TODO 2 的真实需求 A/B 无落地（R2-CORE-002）；TODO 3（次档模型验证）部分体现于 213 能力归属裁定与 F2 执行分工 [MODEL_INFERENCE]；TODO 4（交接真实效果评估）未见执行记录 [VERIFIED_ABSENT_IN_REPOSITORY]。
- 内容：这份文件是 Owner 意图的最新权威快照，但它自身已过窗未结算。不结算的风险：下一个读它的会话无法区分"已做/部分做/未做"，可能重复立项或误以为已完成。
- 建议方向：一次轻量结算（在 issue 追加一条完成度评论即可，不需要仓库任务）。TODO 4（交接效果评估）与本轮专题高度互补，建议在门3 讨论是否由本轨道或后续 Fable 任务承接。

## R2-FRESH-006 — 机制性根因：live 文件的新鲜度靠"人记得"，无声明式失效规则

- severity: OBSERVATION（结构）
- claim: MODEL_INFERENCE（基于 R2-FRESH-001~003 的归纳）
- 内容：仓库有优秀的**创建纪律**（每任务落盘）但没有**过期纪律**：没有任何机制回答"哪个文件声称 live、它上次被谁确认过、超过多久算 stale"。第一轮 greenfield 设计曾提出 staleness stamps + sweeps（GF3A，AUTO2 段）且 GF5-ENH-CUR-004 建议轻量 staleness-flag 约定，当时判 low priority——两个月后的实况（本专题 3 条 REPAIR 级发现全是 staleness）支持将其升级。最低成本版本：每个自称 live/current 的文件头部强制 `last_updated_by_task` + `stale_after`（或"下一个改变本领域状态的任务必须更新我"的声明），由写入方 checklist 承载，不需要自动化。
- 关联：专题08 复检 GF5-ENH-CUR-004；分诊建议升级为 P2。

## 小结

状态层的新鲜度问题（001–003）比证据层（004）严重：证据老化有标注机制兜底，状态过期则直接误导续接。三条 REPAIR 级发现共享同一根因（006）：只有创建纪律、没有失效纪律。无 BLOCKING。
