# 阶段1 专题02 — 执行源 §3–19 逐节符合性与规则漂移评审

```yaml
track_id: FABLE5-REVIEW2-001
record_type: composite_review_theme_report
theme: spec_section_conformance_and_rule_drift
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: mixed_per_claim_labels
authority_level: non_execution_source_advisory_evidence
spec_last_modified: 2026-07-13 (1d2799a, 20f83f2)
```

## 0. 逐节符合性总表

| 节 | 主题 | 状态 | 备注/发现 |
|---|---|---|---|
| §3 | 语言策略 | 张力 | R2-CONF-007 |
| §4 | 执行源原则 | 符合但体系不完整 | R2-CONF-005（guard 层地位）、R2-CONF-001（冲突未登记） |
| §5 | 研究证据层 | 文字过期 | R2-CONF-002 |
| §6/§6.1 | 需求进入/自改进 | 符合 | 抽样：Issue #265 → TODO/candidate 路由正确 |
| §7 | handoff/active-context | **条款失效** | R2-CONF-001（本轮最高优先级发现之一） |
| §8 | 模型迁移 | 符合 | Meta-Agent 迁移与 Claude 进场均按其精神执行 |
| §9 | 交付包 | 部分验证 | Meta-Agent 交付含 manifest/handoff；unsupported-assumptions/drift-review TODO 覆盖度未逐项核验 [UNKNOWN_REQUIRES_EVIDENCE] |
| §10 | v0.1 边界 | 边界遵守、事实过期 | R2-CONF-003 |
| §11 | 客观中立工程风格 | 符合 | 各裁定记录均反奉承、证据先行（抽样：TLR/OR/F2 裁定件） |
| §12 | 操作/说明分离 | 符合 | 近期任务与本轨道均执行 |
| §13 | 长内容文件化 | 符合 | guard 层（artifact-delivery）已操作化并验证（Cases 001–004 PASS） |
| §14 | manual-import 边界 | 符合、前提过时 | R2-CONF-004 |
| §15 | 交接正确性 | 符合 | PRO-SLICE-01 已把 receive→guidance 分离传播到模板族 |
| §16 | 目标项目工作区 | 符合 | Meta-Agent 工作区按规迁出退役 |
| §17 | Pro/DR 分阶段 | 符合 | Issue #265 分批、F2 packages 分阶段均合规 |
| §18 | GitHub 写入授权 | 符合、面窄 | R2-CONF-006（Claude 写入面未覆盖） |
| §19 | no-write 证明/复核来源 | 符合 | BLOCKED 状态如实挂账（见专题04）；同族限制被声明（含本轨道） |

以下逐条展开非"符合"项。

## R2-CONF-001 — §7 是失效条款：它指定的启动文件已死，而冲突未按 §4 登记

- severity: REPAIR_RECOMMENDED（执行源级）
- claim: VERIFIED_REPOSITORY_FACT
- 证据：
  - §7 原文："新会话应优先读取 human-approved-spec、active-context 和 handoff-current"。
  - `current/active-context.md` 最后实质更新 2026-07-06（git log：d8a9182 MNEMOSYNE-085），其"当前阶段"停在 post-053/post-085 时代，与现状相差约 158 个任务号。
  - `current/open-questions.md` 同样冻结于 2026-07-06。
  - `handoff/handoff-current.md` 已被 MNEMOSYNE-240 显式改造为 "Deprecated non-execution-source compatibility pointer / no longer selects, recommends or describes a live handoff route"。
  - 实践已改道：MNEMOSYNE-243 的 AI onboarding 与 MNEMOSYNE-199 utilization review §6.3 都把 active-context/todo/open-questions/handoff-current 归为"默认不读的导航/冷料"。
- 内容：执行源要求新会话读的三个文件中，两个冻结在 6 周前、一个自我声明弃用。任何服从 §7 的新会话会恢复出 7 月初的世界观（例如以为当前正处于"Meta-Agent handoff-ready、等待 post-084 路线恢复"）。同时，"其他文件与 spec 冲突应登记 open question"（§4）——本冲突实际存在已数周，却未见登记（open-questions.md 本身就是冻结文件之一，形成自指死锁）。
- 建议方向（供分诊，多选一交 Owner）：(a) 修订 §7，改为指向 onboarding 入口与 per-route status 模式；(b) 恢复 active-context 为薄指针文件并恢复维护；(c) 废止这三个文件并由 §7 指名替代物。任何一项都需 Owner 批准的执行源修订任务。

## R2-CONF-002 — §5 的研究证据层描述已与证据库现状脱节

- severity: REPAIR_RECOMMENDED
- claim: VERIFIED_REPOSITORY_FACT
- 证据：§5 原文"7 份研究报告已经作为 RC-2026Q2-initial 轮次证据入库"；`raw/research-reports/cycles/` 现有 13 个 cycle（5 个 2026Q2、8 个 2026Q3）；`research-report-index.md` 列 6 个 current 轮次。
- 内容：§5 写于只有一个轮次的时代。它对"当前证据层是什么"的描述现在只覆盖不到一半；派生视图（index/summaries）实际承担了 §5 想承担的职能。§5 中"未来通过新 research cycle 和 delta report 更新"的机制条款仍然正确，是快照句过期。
- 建议方向：§5 去快照化——删除具体轮次数字，指向 index 作为 current 视图的权威入口。

## R2-CONF-003 — §10 内嵌的工具链事实过期（Codex Cloud 主写入助手）

- severity: NON_BLOCKING
- claim: VERIFIED_REPOSITORY_FACT
- 证据：§10 "Codex Cloud 当前主要作为远程 GitHub 文件写入和版本保存助手"；实际近期写入以 ChatGPT GitHub app（§18 收录）与本地 Claude Code（本轨道起）为主，git log 中 codex/* 分支近月占比显著下降（git log --merges 分支名分布）；MNEMOSYNE-235–239 发布事故后选择的恢复架构是 "UBUNTU_24_04_LOCAL_DETERMINISTIC_GIT"（本地 git 通道，见 F2 status 文件）。
- 内容：这是 GF5-TRIAGE-008（"过时机制迁出 spec"）当时预言的漂移类型的又一实例：把有时效的平台事实写进执行源，drift 时执行源变错。v0.1 边界清单本身（无自动化等）依然被遵守，过期的是事实句。
- 关联：专题08 复检 GF5-TRIAGE-008 时给出统一处置建议。

## R2-CONF-004 — §14 标题级前提（Codex Cloud 附件限制）同类过期

- severity: NON_BLOCKING
- claim: VERIFIED_REPOSITORY_FACT（标题与规则绑定平台前提）+ UNKNOWN_REQUIRES_EVIDENCE（该平台限制当前是否仍成立——未验证，本轨道禁研究外部平台）
- 内容：§14 的安全内核（可见性 preflight、no-secrets、历史永久性）是持久规则，但其标题与开篇把规则挂在"Codex Cloud 不能收非图附件"这一 2026-06 时代的平台限制上。规则该保留，挂钩该松绑。§14 自己已写"this rule may be revised if Codex Cloud attachment capability changes"——修订钩子在，未被触发核验。

## R2-CONF-005 — 规则漂移主发现：一个执行源未定义的"guard 层"实际统治日常行为

- severity: REPAIR_RECOMMENDED（结构级，建议列为门3 候选设计题）
- claim: VERIFIED_REPOSITORY_FACT（现象）+ MODEL_INFERENCE（定性）
- 证据：
  - `current/` 下 13 份 guard 共约 3336 行（逐文件 wc -l 汇总），全部自称 "user-approved behavior guard / not execution source"。
  - 其中至少五份对**所有**写入类任务施加强制程序：single-active-PR lineage（118）、Ready-vs-Draft 默认（210）、分支保留通知（196/197）、run-context/PR provenance（147/149）、preserve-first（198）。违反它们会被当作事故处理（116 双 PR、PR 277 Draft 误用的处置先例）。
  - 执行源 §4 只定义了二元权威：执行源 vs 非执行源证据。"user-approved guard"这一实际存在的第三层（有强制力、非执行源、修订流程比 spec 轻）在执行源中没有地位定义。唯一接近的钩子是 §11 判断优先级第 2 位"仓库中已建立的 workflow / process rules"——一句话，无定义、无清单、无修订规则。
  - 对照：40 天里 spec 零修改、guard 层新增/修订 10+ 次。规则的实际生长点完全在 spec 之外。
- 内容：这是第一轮 GF5-DIV-001/GF5-TRIAGE-002（单一 spec vs 因式分解）以更成熟形态的回归。当时裁定"P1 修当前问题+因式分解延后用户决定"；两个月的 guard 增生使延后成本显性化：(a) 新会话无法从执行源推导出"哪些规则有强制力"；(b) guard 间与 spec 间的重复/优先级需要每个模型自行解析（199 F4 已证实）；(c) guard 修订不经 §6 需求进入流程，规则治理出现双轨。
- 建议方向（供分诊/门3）：三选一的 Owner 决策——(a) 在 spec 中正式定义 guard 层（地位、清单指针、修订流程）；(b) 把少数全局强制规则吸收入 spec、其余降为指导；(c) 执行源因式分解（第一轮 UD 项的正式重开）。配套：无论选哪个，建立 guard 定期整合机制（见专题05 R2-COST-006）。

## R2-CONF-006 — §18 只覆盖 ChatGPT 写入面；Claude 本地写入面无对应授权条款

- severity: NON_BLOCKING
- claim: VERIFIED_REPOSITORY_FACT
- 证据：§18 通篇以 ChatGPT GitHub app 为对象（approval card、Allow once 等）；本轨道 Claude Code 经 gh CLI + 本地 git 写入，platform_permission 形态完全不同（用户级允许清单 + SSH key）；本轨道依据的是工作令逐字授权 + §18 的精神类推。
- 内容：platform_permission ≠ task_authority 的原则本身表面无关、可直接沿用；但 §18 的操作细则（风险分级中的动作清单、result record 要求）对 Claude 面只能类推适用。多写入方署名方案（本轨道 00-orientation/03 草案）确认时，宜一并决定 §18 是否泛化为"任意 Agent 写入面"条款。
- 关联：R2-CORE-004。

## R2-CONF-007 — §3 语言策略与 guard 层全英文的张力

- severity: QUESTION
- claim: VERIFIED_REPOSITORY_FACT（现象）
- 证据：§3"中文为主要工作语言"；13 份 guard、onboarding 四件、utilization review 全英文；MNEMOSYNE-199 §1 记录 Owner 反馈"long YAML/English-key blocks and verbose explanations impose avoidable human and token burden"；Owner 2026-08-22 对本轨道的指令再次要求人读内容必须通俗中文。
- 内容：面向人的层（需 Owner 读的决策材料）与面向模型的层（guard/onboarding）语言取向已实际分化，但 §3 未作此区分。第一轮 GF5-TRIAGE-010 中语言政策是 P3；Owner 负担证据两个月内两次出现，建议升级讨论优先级（见专题08）。
- 交 Owner 的问题：是否将 §3 细化为"人读材料中文优先、模型规则文件可英文但须附中文摘要"或等价规则。

## 小结

§3–19 中 12 节实质符合。需要修的集中在两类：**快照过期**（§5/§10/§14 内嵌的时代事实，R2-CONF-002/003/004）与**结构失配**（§7 死条款 R2-CONF-001、guard 层无地位 R2-CONF-005）。后者是本轮最重要的执行源级发现。无 BLOCKING。
