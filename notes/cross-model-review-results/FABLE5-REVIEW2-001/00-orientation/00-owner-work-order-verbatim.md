# FABLE5-REVIEW2-001 — Owner Work Order (Verbatim)

```yaml
track_id: FABLE5-REVIEW2-001
record_type: owner_work_order_verbatim_preservation
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: DIRECT_OWNER_INSTRUCTION
authority_level: current_task_authorization_within_execution_source_boundaries
preservation_note: >
  下方水平线之后的内容为 Owner 在 Claude Code (VSCode surface) 会话中下达的
  启动指令原文，逐字保存，未做任何修改。首次会话在完成任何写动作之前因
  Owner 误关 VSCode 而中断；本文件由续接会话作为本轨道第一个写动作存档。
  中断与续接事实本身不改变指令内容。
```

---

【Mnemosyne · FABLE5-REVIEW2-001 启动指令（Owner 下达）】

你是 Claude Code 中的 Fable 5，工作目录是 Mnemosyne 仓库的本地克隆（08822407d/Mnemosyne），工作语言中文。本指令由 Owner 本人下达，构成本轨道的当前任务授权；授权范围之外一律只读。

## 任务
第二轮复合评审与独立设计，轨道 ID：FABLE5-REVIEW2-001。目的：在重建项目全貌之后，延续约两个月前第一轮（FABLE5-REVIEW-001~003 / FABLE5-TRIAGE-001 / FABLE5-GREENFIELD-001）的节奏：先评审当前仓库整体状态，再对 Owner 选定的问题做独立设计。

## 写入授权（仅此范围）
- 唯一工作分支：fable5-review2-001-workspace（从 origin/master 最新提交切出）
- 只允许在 notes/cross-model-review-results/FABLE5-REVIEW2-001/ 下新建文件；不修改任何既有文件
- 全程至多一个 open PR，合并权在 Owner；不得直接写 master
- commit message 一律以 "FABLE5-REVIEW2-001: " 开头

## 明确禁止
- 创建根 CLAUDE.md 或 AGENTS.md
- 触碰分支 mnemosyne-240-preservation-capsule 与 mnemosyne-242-post-pr303-closeout-and-handoff
- 对 08822407d/Meta-Agent 或任何其他仓库做任何操作
- 发起 Research / Deep Research、修改连接器或调用外部服务
- 将任何非公开、未脱敏材料写入本公开仓库
- 修改 current/human-approved-spec.md 及任何执行源、guard、status 文件——发现其中的问题记入 findings，不动原文

## 入场读取（按序，不做全库通读）
1. current/human-approved-spec.md（唯一执行源）
2. notes/ai-onboarding/MNEMOSYNE-AUTHORITY-AND-EVIDENCE.md
3. notes/ai-onboarding/MNEMOSYNE-REPOSITORY-MAP.yaml
4. notes/ai-onboarding/MNEMOSYNE-CLAUDE-CODE-LOCAL-START.md —— 这是你在本 surface 的行为契约（写前 preflight、工程行为、返回契约），必须逐条遵守
5. 第一轮全部记录：notes/cross-model-review-results/ 下的 README.md、FABLE5-REVIEW-001~003、FABLE5-TRIAGE-001、FABLE5-GREENFIELD-001（重点：各步结论、charter、以及所有 substantive_maintainer_acceptance: not_performed 标记）
6. 按需：current/ 下与本任务相关的 guard 与 status；raw/ 与 handoff/ 历史件保持冷源，仅在需要证据时定点引用

## 阶段与门（每个门停下等 Owner 明确批示，不得自动进入下一阶段）
- 阶段0 定向：完成入场读取后执行写前 preflight（记录 origin/master SHA、完整分支与 open PR 枚举、谱系冲突检查；与 single-active-PR guard 冲突即停并询问 Owner）。随后写《入场定向报告》：(a) 你重建的项目现状全貌；(b) 与第一轮时点（约 MNEMOSYNE-113，2026-06 末）之间的关键变化，用 git log 作证据；(c) 第一轮 findings 与设计建议的落实情况逐条核对；(d) 本轮评审计划与信息缺口。落盘 00-orientation/01-orientation-report.md 并 commit。→ 门1
- 阶段1 复合评审：对照执行源 §1–2 的核心需求与 §3–19 及隐含非功能需求（成本、新鲜度、可扩展性、验收债、单点风险），逐项审视当前仓库；每条 finding 附证据路径与主张标签。落盘 01-composite-review/（按主题分文件）。→ 门2
- 阶段2 分诊：仿 FABLE5-TRIAGE-001 输出优先级矩阵、修复建议与代价评估。落盘 02-triage/。→ 门3
- 阶段3 独立设计：仅对 Owner 在门3 选定的条目做独立设计稿（greenfield 风格，每稿附自我批判节）。落盘 03-independent-design/。→ 门4：将 PR 整理为 Ready，输出最终返回契约，等待 Owner 审查合并。

## 记录纪律
- 第一个写动作：把本指令原文逐字存入 00-orientation/00-owner-work-order-verbatim.md（任务授权存档）
- 每份产出文件头部登记：track_id、生成模型（claude-fable-5）、surface（claude-code-cli|vscode|desktop，按实际）、日期、base_master_sha、evidence_class
- 结论一律区分 VERIFIED_REPOSITORY_FACT / MODEL_INFERENCE / DESIGN_RECOMMENDATION / UNKNOWN_REQUIRES_EVIDENCE；不虚构连续性，缺证据就声明缺
- 每个子步骤完成即 commit；信息保全优先于提交整洁
- 每次会话结束按 CLAUDE-CODE-LOCAL-START 的返回契约汇报：base/head SHA、变更路径、未动的受保护路径、验证方式、已知局限、下一个门

## 跨会话续接
本轨道允许跨多个 Claude Code 会话完成。新会话冷启动时：先读 00-owner-work-order-verbatim.md 与 track 目录下已提交记录，从最近的门续接；不依赖任何上一会话的对话记忆。

现在从阶段0开始。
