# 阶段1 专题01 — 执行源 §1–2 核心需求覆盖评审

```yaml
track_id: FABLE5-REVIEW2-001
record_type: composite_review_theme_report
theme: spec_core_needs_coverage
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: mixed_per_claim_labels
authority_level: non_execution_source_advisory_evidence
severity_scale: [BLOCKING, REPAIR_RECOMMENDED, NON_BLOCKING, OBSERVATION, QUESTION]
```

评审基准：执行源 §1（记忆系统元 Agent 定位：为其他项目、长期研究、学习系统、开发 Agent、多 Agent 团队设计外部持久记忆系统）与 §2（模型负责计算，文件负责记忆；模型可替换；外部文件/Git 是长期记忆与审计基础）。

## R2-CORE-001 — 核心使命已有一次完整生命周期交付证明

- severity: OBSERVATION（正面）
- claim: VERIFIED_REPOSITORY_FACT
- 证据：`README.md`（Meta-Agent cutover 段）；`current/meta-agent-dedicated-repository-pre-migration-status.md`；PR #261（merge c85ebba5，Mnemosyne 侧 writer 退役）；`08822407d/Meta-Agent#3` cutover merge eb71ed35。
- 内容：第一个目标项目 Meta-Agent 走完了"intake → 受控 dry-run → v0.1 七文件构建 → 专属仓库迁移 → 真相源移交 → Mnemosyne 侧退役"的完整链路。§1 的元 Agent 定位不再是纯设计宣言，有了一次端到端实例。
- 限定：`effective_for_operational_use: false` 仍未翻转（Meta-Agent 侧记录）——交付的是结构与移交，不是已运行的记忆系统。

## R2-CORE-002 — 产能失衡：自我治理产出远大于目标项目产出，且 Owner 已决定的转向尚未发生

- severity: REPAIR_RECOMMENDED（方向性）
- claim: VERIFIED_REPOSITORY_FACT（数字）+ MODEL_INFERENCE（失衡判断）
- 证据：
  - 第一轮时点后约 130 个任务（113→243）中，直接服务目标项目的链条主要是 Meta-Agent 迁移（169–172、189–195）与 target-lifecycle/并发验证（205–234），其余大部分为 Mnemosyne 自身 guard、状态修复、评审、发布事故恢复（git log --merges，见定向报告 b.1 时间线）。
  - Owner 已在 Issue #265 TODO 2（2026-08-10）明确决定"从细慢抽象建设转向真实需求驱动的初版实用化"，并点名两个真实需求：A 工作业务功能代码库、B 长期外语教师/陪练。
  - `target-projects/` 目录截至 base_master_sha 只含 `meta-agent/`（历史 bootstrap）；真实需求 A、B 无任何工作区、intake 记录或 raw 摄入（ls target-projects/；notes/ 检索）。
  - 08-16 之后的仓库工作（235–243）内容为发布事故恢复与 AI onboarding，仍属自我治理。
- 内容：仓库的"工厂"角色（§1）目前主要在生产"工厂自身的管理制度"。Owner 判定的转向在仓库中尚无落地痕迹。这不是纪律缺陷（每步都合规），而是投入结构与已声明目标不一致。
- 建议方向（供分诊）：把真实需求 A/B 的 intake 与初版记忆系统设计立为下一个主线任务族；本轮评审其余发现的修复优先级应让位于此（除非阻塞它）。

## R2-CORE-003 — "文件负责记忆"执行优秀，信息保全是仓库最强项

- severity: OBSERVATION（正面）
- claim: VERIFIED_REPOSITORY_FACT
- 证据：每任务 result record（notes/codex-task-results/ 大量文件）；评审轨道逐字/哈希存档（cross-model-review-results 树，含 gzip+base64 精确归档与 SHA-256）；发布事故后专设保全 capsule 分支（mnemosyne-240-preservation-capsule）；`notes/source-artifact-preservation-and-design-rationale-guard.md`（198）确立 preserve-first。
- 内容：§2 的审计基础要求被超额满足。第一轮识别的"保全优先"文化持续强化。代价见专题05（成本）。

## R2-CORE-004 — "模型可替换"直到本月才被真实检验，检验结果初步为正

- severity: OBSERVATION
- claim: VERIFIED_REPOSITORY_FACT（事件）+ MODEL_INFERENCE（评价）
- 证据：MNEMOSYNE-243（PR #305，2026-08-21）建立仓库原生 AI onboarding；本轨道（Claude Code 首次建设类工作）仅凭 4 份入场文件与工作令即完成定向、preflight、合规写入（本轨道 00-orientation/ 全部产出）；Owner 2026-08-22 补充指令确认这是 Claude 首次建设性参与。
- 内容：§2 宣称模型是可替换计算单元，但 2026-05~08 的执行几乎全部在 GPT 工具族内。onboarding 包+本轨道构成第一次跨族替换实测，初步可行。遗留缺口：多写入方作者溯源方案未定（本轨道 00-orientation/03 草案待联合确认）；任务号规范、result record 模板等惯例对非 GPT 写入方的适配未成文。
- 关联：专题06 R2-SPOF-002、专题07 R2-SCALE-004。

## R2-CORE-005 — §1 所列服务对象中"学习系统"需求积累最厚但零落地

- severity: QUESTION
- claim: VERIFIED_REPOSITORY_FACT（积累）+ QUESTION（是否立项）
- 证据：`current/todo.md` 三条用户点名的产品设计研究 TODO（learner-state、跨 Agent 复用、问题解决策略教练，07-26 后加入）；Issue #244（教学 Agent 先行使用，08-02，OPEN 无动作）；Issue #265 真实需求 B（外语教师/陪练）；`notes/learner-state-and-adaptive-explanation-synthesis-v0.1.md`；adaptive-explanation Stage A 完成、Stage B0 设计完成未执行（`current/adaptive-explanation-stage-b0-status.md`）。
- 内容：围绕学习/教学场景已有 4 个独立积累点（研究 TODO、两个 Issue、synthesis 文件、adaptive-explanation 路线），彼此关联但没有一个进入"目标项目工作区 + intake"的正式通道。继续积累研究而不开工作区，重复与漂移风险随时间上升。
- 交 Owner 的问题：真实需求 B 是否即为这些积累的收敛点？若是，建议分诊时把"B 立项 intake"列为高优先级，并把 4 个积累点显式并入。

## 小结

§1–2 的四句核心宣言中："为其他项目设计记忆系统"有一次完整证明但当前产能错配（R2-CORE-002）；"文件负责记忆"执行最好（R2-CORE-003）；"模型可替换"刚获得首次实证（R2-CORE-004）；"服务学习系统"积累最厚、落地最少（R2-CORE-005）。无 BLOCKING 发现。
