# 多写入方作者溯源方案（草案 v0.1）

```yaml
track_id: FABLE5-REVIEW2-001
record_type: design_draft_pending_joint_confirmation
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: DESIGN_RECOMMENDATION
authority_level: non_execution_source_advisory_draft
confirmation_gate: >
  本草案不生效。按 Owner 2026-08-22 指令，待下周 ChatGPT Pro 配额恢复后，
  由 ChatGPT Pro 与 Fable 5 共同确认（可修改、可否决）后方可采用。
  采用与否不改变执行源；current/human-approved-spec.md 仍是唯一执行源。
```

## 1. 要解决的问题

仓库此前的写入方是 ChatGPT（网页对话 / Work）与 Codex Cloud，全部在 GPT 工具链内。现在 Claude 系列（Claude Code / 未来可能的 Claude 网页端）成为第二个工具族写入方。当前的临时规则是"Claude 产出放独立文件夹"，靠**位置**区分作者。这不可持续：位置应服务于内容组织，不应被作者身份占用。

目标：Claude（及任何未来写入方）可以在仓库任意合适位置新建和修改文件，同时任何人在任何时候能回答三个问题——**这处变动是谁做的？在哪个任务里做的？经谁批准？**

## 2. 仓库已有的溯源机制（方案在其上扩展，不另起炉灶）

- [VERIFIED_REPOSITORY_FACT] git 提交本身记录作者与时间；仓库惯例是 commit message 带任务号前缀（如 `MNEMOSYNE-243:`、`FABLE5-REVIEW2-001:`）。
- [VERIFIED_REPOSITORY_FACT] Claude Code 提交默认带 `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>` 尾注（本轨道两个已有提交均可查证）。
- [VERIFIED_REPOSITORY_FACT] 仓库大量文件已有 YAML 头登记 `created_by_task` / `last_updated_by_task`；本轨道文件头另有 `generated_by_model` / `surface` 字段（工作令要求）。
- [VERIFIED_REPOSITORY_FACT] 已有 run-context 与 PR 来源防护文件（MNEMOSYNE-147/149 建立）要求 ChatGPT 侧仓库写入披露运行上下文；执行源 §18/§19 要求结果记录登记实际执行者。

即：**三层机制都已有雏形，缺的只是跨工具族的统一约定。**

## 3. 方案主体：三层归属登记

### 第一层：git 提交尾注（机器可查，覆盖一切变动）

每个 AI 写入方的每次提交，在 commit message 末尾带两行固定尾注：

```
Actor: <模型标识>@<工作面>
Task: <任务号>
```

取值表（初版，联合确认时可增删）：

| 写入方 | Actor 值示例 |
|---|---|
| Claude Code（VSCode/CLI/桌面） | `claude-fable-5@claude-code-vscode` |
| Claude 网页端（若未来写入） | `claude-<model>@claude-web` |
| ChatGPT 网页/Work（GitHub app 写入） | `gpt-<model>@chatgpt-web` |
| Codex Cloud | `codex@codex-cloud` |
| Owner 本人手工操作 | 不写尾注（无尾注 = 人类或历史提交） |

查询方式：`git log --grep '^Actor:'` 或按值过滤，即可列出任一写入方的全部变动；单文件历史用 `git log -- <文件>` 自然继承。

### 第二层：文件头登记（人可读，覆盖文档类文件）

- 新建文档：YAML 头至少含 `created_by_task`、`generated_by_model`、`surface`、`date`（即本轨道现行做法，推广为通用约定）。
- 修改他人文档：只追加/更新 `last_updated_by_task`、`last_updated_by_model`，**不改** `created_by_*` 字段。
- 不适合加头的文件（脚本、数据 YAML、归档分片）：不强求文件头，由第一层尾注兜底。

### 第三层：PR 说明区块（评审时一眼可见）

PR 描述固定包含一个来源区块：执行者（Actor 同上）、任务号、分支、基准提交、涉及路径概要。与现行 ChatGPT 侧 run-context 披露要求对齐，扩展到所有写入方。

## 4. 边界与不变量

1. 归属登记只回答"**谁执行了写入**"；批准权、合并权、执行源变更权仍完全按现行规则归 Owner。本方案不含任何授权变化。
2. 标签不等于证明：尾注与文件头是自我声明，可被伪造或遗漏；与仓库既有纪律一致（可见标签≠运行时证明）。发现不一致时以 git 历史与 PR 记录交叉核对。
3. 历史不迁移：既有的 Claude 独立文件夹（各评审轨道目录）原地保留，作为历史证据；方案只约束**生效后的新变动**。
4. 单任务单分支单 PR 的现行防护不变；多写入方并发仍靠该防护约束，不靠位置隔离。

## 5. 迁移路径

- 阶段0（现状）：Claude 产出继续进独立轨道文件夹。
- 阶段1（联合确认通过后）：Claude 可在常规路径写入；三层登记强制生效；"独立文件夹"要求解除，但评审/设计类轨道产出按内容性质仍自然归入 cross-model-review-results 树（那是内容归类，不是作者隔离）。
- 阶段2（可选，未来）：若写入方继续增多，可加一页简短的"写入方登记表"（写入方 → Actor 值 → 启用日期），放在非执行源导航区。

## 6. 备选变体 B（更简单，但覆盖不全）

给每个 AI 写入方配置独立的 git 作者身份（如 author 名 "Claude Fable 5 (agent)"），git blame 直接显示作者。优点：零约定成本、行级归属天然可见。缺点：ChatGPT 网页端经 GitHub app 提交时作者身份由平台决定（通常是 Owner 的账号），无法统一控制，导致该变体在最主要的既有写入方上失效。**因此推荐主方案用尾注，变体 B 仅在可控 surface（Claude Code、本地脚本）上作为补充同时启用。**

## 7. 自我批判（按轨道惯例）

- 尾注依赖各写入方自觉遵守，v0.1 阶段无机械强制（仓库明确排除 GitHub Actions 等自动化）；漏写只能靠 PR 评审发现。缓解：把尾注检查加入各工具族的启动指导文件（属非执行源指导更新，需 Owner 批准的独立任务）。
- ChatGPT 网页端能否稳定在 commit message 里带尾注，取决于其 GitHub app 写入时对 message 的控制程度——此点我未验证，标记 UNKNOWN_REQUIRES_EVIDENCE，应由下周 ChatGPT Pro 在确认时自证。
- 文件头字段在长寿命文件上会积累；限定为 created + last_updated 两组字段可控，但"中间修改者"信息只存在于 git 层——接受此取舍，避免文件头膨胀。
- "无尾注 = 人类"的默认解释对历史提交成立，但对**忘写尾注的 AI 提交**会误判为人类。缓解：联合确认时可决定是否要求 Owner 手工提交也带 `Actor: owner@manual`（代价：给 Owner 增加负担，倾向不要求）。
- 本草案由 Claude 单方起草，且起草者是利益相关方（方案直接决定 Claude 产出的放置方式）；这正是 Owner 设置"ChatGPT Pro + Fable 5 联合确认"门的原因，该门必须保留。

## 8. 留给联合确认的问题清单

1. Actor/Task 尾注的字段名与取值表是否接受（或改用其他键名）？
2. 文件头最小字段集是否接受？
3. PR 来源区块是否强制、字段是否够用？
4. 无尾注提交的默认解释（人类）是否接受？Owner 手工提交是否也标注？
5. 既有 Claude 独立文件夹不迁移——确认？
6. ChatGPT 网页端写入能否在 commit message 中稳定携带尾注（需 ChatGPT 侧自证）？
