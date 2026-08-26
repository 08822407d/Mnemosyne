# 实施记录 · 批次一（MNEMOSYNE-244/245/246）三 PR 交付

```yaml
track_id: FABLE5-REVIEW2-001
record_type: implementation_run_record
tasks: [MNEMOSYNE-244, MNEMOSYNE-245, MNEMOSYNE-246]
created_by_task: FABLE5-REVIEW2-001
generated_by_actor: claude-fable-5
generated_on_surface: claude-code-vscode
date: 2026-08-26
evidence_class: VERIFIED_REPOSITORY_FACT_with_noted_inferences
user_decision_recorded: true
owner_decision_evidence: >
  联合确认记录第六节（Owner 终审批准各任务）＋Owner 2026-08-26 开工指令
  "现在可以继续昨晚计划好的任务了"（解读为批次一按既定队列开工；
  解读依据：本机无昨晚新增会话记录或提交，唯一在案计划即批次一队列，
  该解读已在开工回复中向 Owner 显式声明并保留纠正窗口）。
```

## 交付事实（全部已推送，待 Owner 逐个终审合并）

| 任务 | PR | 分支 | 内容一句话 | 提交 |
|---|---|---|---|---|
| MNEMOSYNE-244 | #308 | mnemosyne-244-stale-status-freeze | 三处过期路标冻结头＋todo 分节冻结＋评审总览 greenfield 段修正（R2-FRESH-001/002/003 闭环，§7 配套） | c92780e |
| MNEMOSYNE-245 | #309 | mnemosyne-245-rule-layer-task-one | guard-registry.yaml（13 份登记，仅索引不赋权）＋loader 分层加载 shadow 试点＋跨族四约定并入两 guard | c062a8a |
| MNEMOSYNE-246 | #310 | mnemosyne-246-attribution-and-naming | 署名溯源惯例定稿 v1.0（含逐表面身份可信度分级）＋对话命名规范并入显示名注册表 v0.2.0 | efe02df |

- 三 PR 基线一致（master 5de31a3，含已合并的 #307 执行源修订），文件集两两不相交，合并顺序任意。
- 预检记录、provenance 区块、cross_family_effective 旗标（#309/#310 = yes，#308 = no）均在各 PR 说明内——本批是 245 所立跨族约定的首批实际使用。

## 判断与残留（如实声明）

1. "昨晚计划好的任务"解读为批次一 [MODEL_INFERENCE，已声明]；若 Owner 实际另有安排（如 ChatGPT 侧计划），批次一交付本身仍在既批范围内，无越权。
2. #308 残留：review-and-validation-status.md 的 conversation_routing 历史段未动（超裁定范围）；todo 三研究题判"仍有效"为推断。
3. #309 残留：triggers 完备性靠 shadow pilot 校准；scope_zh 概括为 Fable 措辞（注册表不赋权，失真不改变义务）。
4. #310 残留：ChatGPT 自识别现状与 Codex 查证 → 任务 5 调查项；主线码起步仅登记 M/FR2/B。
5. 遗留队列不变：任务 5（platform-guides）、任务 6（风险分布登记簿定稿）、任务 7（GPT 侧 EXP 对照）、开放设计题③（审核分工）、PR #306 处置、档案库命名。
```
