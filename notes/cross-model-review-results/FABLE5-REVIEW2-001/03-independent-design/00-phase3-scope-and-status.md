# 阶段3 独立设计 — 范围、进度与最终返回契约

```yaml
track_id: FABLE5-REVIEW2-001
record_type: phase3_scope_and_final_return_contract
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: track_status_record
authority_level: non_execution_source_advisory_evidence
phase: phase_3_independent_design_complete
gate_3_decision_record: ../02-triage/03-gate3-owner-decision-record.md
```

## 范围（门3 批示圈定）

| 交付物 | 状态 | 说明 |
|---|---|---|
| 01 设计稿A 规范层治理 | ✅ 完成 | 含 Q5a 预倾向、Q7a 语言分层、束3 机制并入、自我批判节 |
| 02 设计稿B 章程修订案文 | ✅ 完成 | 7 条独立可批的修订案文、批示表、自我批判节 |
| 03 设计稿E 交接效果评估方案 | ✅ 完成 | 8 个候选样本、三条件设计、成本档位、自我批判节 |
| 04 问题详录（供 Pro 自我检讨） | ✅ 完成 | P-01~P-09 含成因假设与自检问题；Q6 四笔账按批示记录不销 |
| 05 跨模型差异分析与实验方案 | ✅ 完成 | 两族模式对照、Claude 自我记录 C-01~C-08、EXP-1~6 提案 |
| （候选C 状态失效纪律） | 并入 A | 按分诊预案 |
| （候选D 证据保全设计） | 未做 | 门3 未圈选 |
| （候选F 真实需求 intake 包） | 未做 | Q2 挂起（Meta-Agent 建设与验证优先，A/B 用于实测 Meta-Agent） |

## 门3 批示带来的三条总约束（执行状态）

1. **隔离保持**：全部产出仅在本轨道目录；合作方案确认前不并入正式内容——**PR #306 保持 Draft 并注明本约束**（工作令原定门4 转 Ready，被 Owner 08-22 批示修改）。
2. **不修复**：本轨道未执行任何修复；设计稿A/B 均为案文，实施钩子全部标注"待 Pro 检讨与合作方案后另行授权"。
3. **分析与实验前置**：04/05 文件即为此产出；实验均为提案未执行。

## 最终返回契约（全轨道）

```yaml
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce   # 全程未变，master 无移动
branch: fable5-review2-001-workspace
canonical_pr: 306 (Draft, 保持不合并，见总约束1)
total_deliverables: 21_files
structure:
  00-orientation/: 4 files（工作令逐字、定向报告、补充指令逐字、署名方案草案）
  01-composite-review/: 9 files（总摘要 + 8 专题；0 BLOCKING / 9 REPAIR / 17 债项）
  02-triage/: 4 files（分诊摘要、优先级矩阵、决策清单、门3 批示逐字记录）
  03-independent-design/: 6 files（本文件 + 设计稿A/B/E + 问题详录 + 跨模型分析）
protected_paths_untouched:
  - current/**（含执行源与全部 guard/status——零修改）
  - 既有 notes/**、handoff/**、raw/**、target-projects/**、commands/**、README.md
  - 分支 mnemosyne-240-preservation-capsule、mnemosyne-242-post-pr303-closeout-and-handoff
  - 未创建根 CLAUDE.md / AGENTS.md
validation_method:
  - 全部 VERIFIED 主张附证据路径；量化主张来自可重放 shell 计数
  - 每门停等 Owner 批示；批示逐字存档（门3 批示见 02-triage/03）
  - 逐子步骤 commit+push（信息保全优先）；PR 说明随进度同步
known_limitations:
  - 单模型同族产出：对第一轮 Fable 工作的复检非异构；设计稿与 GPT 侧 199 存在锚定可能（已声明）
  - notes/ 深层为抽样读取；会话侧未入库信息不可见
  - 实验与评估均为方案，零执行
next_gates_outside_this_track:
  1. Owner 转交 04+05（及全轨道）给 ChatGPT Pro：自我检讨 + 对本轨道的异构复核
  2. 合作方案联合确认（署名+§18泛化+命名空间+跨族惯例，四合一议程）
  3. 上述完成后：Owner 决定 PR #306 合并与修复任务排期（设计稿A §4 / 设计稿B 批示表待用）
track_status: ALL_PHASES_COMPLETE_HOLDING_AS_DRAFT_PER_OWNER_ISOLATION_CONSTRAINT
```
