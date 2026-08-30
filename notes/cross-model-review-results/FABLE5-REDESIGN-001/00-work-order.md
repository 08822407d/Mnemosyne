# 工作令 · FABLE5-REDESIGN-001 · Mnemosyne 需求综合分析与独立重新设计

```yaml
track_id: FABLE5-REDESIGN-001
drafted_by: claude-fable-5@claude-code-vscode（MNEMOSYNE-258）
issued_by: Owner（本文件经 Owner 合并即为生效工作令；Owner 可在启动提示中追加或修改任何条款）
executor: 新开 Claude Code 本地会话（Fable 5），执行机 /home/cheyh/projs/Mnemosyne
pinned_base_at_drafting: 82b1093
authority: 本工作令只是任务边界与交付合同；current/human-approved-spec.md 仍是唯一执行源
owner_input_handling: 按 G/C/O/H/P 分级处理 Owner 输入（raw/owner-intent-records/…-verbatim.md 附录为提议标注，待 Owner 确认）
```

## 0. 启动仪式（第一条回复必须完成，未完成不得进入阶段 0）

1. **写前预检**：运行 `scripts/preflight-write.sh`；确认 gh 已登录（`gh auth status`）；记录钉住的 master SHA。
2. **加载指导**：按 `commands/load-mnemosyne-guidance.md` 的分层调度执行并输出刷新确认块。本轨道必然触发的条件件：重大设计选择（source-artifact/design-rationale guard）、材料摄入（同前）、建分支/PR（lineage guard）、重要写入（run-context guard）、跨对话任务设计（cross-conversation guard ＋ artifact-delivery guard 的完整回复转移文件条款）——**不确定就读**。
3. 通读本工作令与 §2 材料清单；对读不到的材料标 BLOCKED，不得替代。
4. 建分支 `fable5-redesign-001-workspace`，建一个 Draft PR（Draft 例外理由：多阶段门控、内容随门变化），**只在** `notes/cross-model-review-results/FABLE5-REDESIGN-001/` 与 `project-knowledge/FABLE5-REDESIGN-001/` 下新建文件。
5. 向 Owner 回报：恢复完整性核对（读到了什么、缺什么）、阶段计划、本轮无需 Owner 操作的声明；**等门 0 批示**。

## 1. 目的（G 类，Owner 原话摘要，原文见材料 A1）

- 核心目标：研究并试验出一套让新旧对话在同一长期工作上尽可能完美交接的方案——"像在同一个对话中进行一样"。
- 第二目标：忠实记录 Owner 各阶段的需求原文与构想（碎片式、多次累积、可能自冲突），并让 agent 真正用得上；具备需求生命周期能力（一致性/可行性分析、知道该做哪些研究、沟通不可行原因与替代、实验验证、新模型可用时回头重评、反馈全材料捕获、定期测试）。
- 元目标：在建设与使用 Mnemosyne 的过程中摸清并形成"如何记录、如何让 agent 简便套用"的经验，供 Meta-Agent 与具体项目 agent 学习套用。
- 本轨道任务：对 Owner **新版**（2026-08-30 三条消息）与**旧版**（2026-05~08 各处叙述）的想法做综合的逻辑自洽分析与可行性研究分析，然后**独立重新设计 Mnemosyne**——允许抛弃任何 H 类（机制猜想）旧架构，只对目标登记表负责。

## 2. 材料（全部本机可读；分级）

**A. Owner 原文（G/C/O/H/P 分类的对象）**

- A1 `raw/owner-intent-records/2026-08-30-owner-goals-and-input-classification-verbatim.md`（新版三条消息＋提议标注）
- A2 `notes/cross-model-review-results/FABLE5-REVIEW2-001/00-orientation/00-owner-work-order-verbatim.md`、`02-owner-supplementary-instructions-2026-08-22.md`
- A3 `notes/cross-model-review-results/FABLE5-REVIEW2-001/02-triage/03-gate3-owner-decision-record.md`、`07-pro-handover/05-owner-final-adjudication-record.md`
- A4 `notes/cross-model-review-results/FABLE5-REVIEW2-001/03-independent-design/09-digital-replica-vision-record-and-naming.md`
- A5 Issue #265 正文（`gh issue view 265`）
- A6 `raw/concept-origin-extract-001.md`、`raw/chatgpt-discussion-057.md`（早期构想抽取）
- A7 `notes/alaya-archive-repository-naming-decision.md`
- A8 **Alaya 私档**（本机 `~/projs/Alaya`，L1 私有材料）：`indexes/project-genealogy-origin.md`（谱系起源口述）；`conversations/chatgpt/GeodataMaster/`（谱系根对话）；`conversations/chatgpt/MNE/` 与 `MA/` 中 6 月早期对话（旧版叙述的第一手原文，按 `indexes/archive-inventory-*.yaml` 导航）。**规则**：可读可分析；引用 ≤200 字/处且不含隐私；不得整段复制进公开仓库；读取范围写进读取清单。

**B. 现状与历史证据**

- B1 `current/human-approved-spec.md`（含 PR #307 的 8 处修订）、`current/guard-registry.yaml`、`commands/load-mnemosyne-guidance.md`
- B2 `notes/cross-family-cooperation/MNEMOSYNE-254-history-self-analysis-receipt-and-comparison.md`（两个月复盘双族对照＋诊断 v2）及 `received/` 两份 Pro 复盘
- B3 `notes/cross-family-cooperation/foundational-agent-antipattern-checklist-v1.md`
- B4 `notes/cross-family-cooperation/MNEMOSYNE-253-review-assignment-policy-design-draft.md`
- B5 `notes/registries/observed-execution-risk-distribution-register.md`、`multi-writer-attribution-convention.md`
- B6 `notes/cross-model-review-results/FABLE5-REVIEW2-001/` 全轨道（评审发现、设计稿 A/B/E/F/G、交接效果三条件评估、406 条考古、族谱、实验）
- B7 `notes/cross-family-experiments/`（EXP-3/5/7 结果；EXP-7 的"片段≠方案"与"§20 盲点"教训）
- B8 `notes/platform-guides/`（表面事实；缺的标 UNKNOWN）

**C. 只作历史、不作路线来源**：`current/active-context.md`、`current/todo.md`、`current/open-questions.md`、`handoff/`（均已冻结）。

## 3. 阶段与门（每门等 Owner 一字批示；未批不得进入下一阶段）

**阶段 0 · 目标登记表（门 0）**
- 从 A 类材料抽全 Owner 的 G/C/O/H/P 条目，新旧两版分列，逐条带出处与日期；
- 新旧对照：一致 / 演化 / 矛盾三类；矛盾项保留双方原文并列，**不调和**，交 Owner 裁；
- 把每条 G 翻译成可验收标准草案（尤其"像同一个对话"的可测定义：建议同时给 Owner 体感指标与机械指标）；
- 交付 `01-goals-register.md`；Owner 逐条 准/改/驳。

**阶段 1 · 逻辑自洽与可行性分析（门 1）**
- 对每条 G/H：与其他条目、与现行章程的逻辑一致性；可行性三档（现在可行 / 需研究 / 当前不可行）＋原因＋替代方案；
- 研究需求清单：只列"影响某个具体决定"的问题，写明该决定、期望证据、到期处置（决策拉动，不按额度排期）；
- 平台事实依赖逐条引用 B8，缺的标 UNKNOWN；
- 交付 `02-consistency-and-feasibility.md`、`03-research-questions.md`；若需 Deep Research，另出单粘贴任务书（材料副本置于 `project-knowledge/FABLE5-REDESIGN-001/` 供一次勾选；末尾**必须**要求执行者以可下载文件交付完整回复）。

**阶段 2 · 独立重新设计（门 2）**
- 只对目标登记表负责；可抛弃任何 H 类旧架构，但每处抛弃须写明理由；
- 必含：架构总览；"耐久核心 / 可再生层"的文件组织（可再生层标注为哪一代模型而建）；"原始资料→经检查构想→实现层"三态循环的记录方案；需求生命周期状态机（含新模型可用触发重评、反馈全材料捕获、定期测试）；加载/投影机制（记录≠加载）；**目的核查机制**（与 fail-closed 同级的停止条件）；Owner-touch 预算；**交接方案**（核心目标）及其预冻结效果测试；自现状的迁移计划；反模式清单逐条自检；自我批判与盲区；
- 每个提示词片段须内嵌全部必填字段与状态枚举（EXP-7 教训）；
- 交付 `04-redesign-fable.md`（＋附件）。

**阶段 3 · 跨族对照准备（门 3）**
- 起草交 GPT-Pro 的对照设计/盲评单粘贴任务书（同上回传要求）；本会话不读 Pro 的对照设计（若已存在）以保持独立；
- 交付 `05-pro-counterpart-package.md`。

## 4. 约束

- 写入仅限本轨道目录与 `project-knowledge/FABLE5-REDESIGN-001/`；不改章程、guard、loader、状态文件、注册表（需要改的写成候选，交后续主线任务）。
- 谱系：单分支、至多一个 open PR；**每个写入批次前运行 `scripts/preflight-write.sh`**；每一逻辑步 commit＋push；四行提交尾注（署名惯例）。
- 证据类别标签（VERIFIED/INFERENCE/UNKNOWN）；同族局限声明；H 类 Owner 想法只能配"验证方案"，不得否决。
- 回复格式：操作内容置顶、正文无内部术语、下一步收尾；每次回复末尾一行"本轮对核心目标推进了什么"（目的核查，从本轨道自身做起）。
- 上下文纪律：每个门结束写续接检查点（`09-continuation/`）；上下文占用达约 70% 时主动提醒 Owner 压缩并先落盘。
- 不执行 Deep Research（只起草）；Alaya 与 Meta-Agent 仓库只读；不建立任何自动化。
- 禁止（本会话前例）：把任何设计当已采纳；起草交他人执行的任务书而不含回传文件要求与专用材料文件夹；在已合并 PR 的分支上继续写；用绝对化二分压扁有梯度的事实。

## 5. 完成定义

四个门全部经 Owner 批示；Draft PR 转 Ready 交 Owner 合并；评审状态文件的登记由后续主线维护任务处理（本轨道不改状态文件）。
