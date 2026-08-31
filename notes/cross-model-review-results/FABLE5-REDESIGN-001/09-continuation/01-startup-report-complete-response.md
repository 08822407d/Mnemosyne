# FABLE5-REDESIGN-001 · 启动仪式回报 · 完整回复转移文件

```yaml
record_type: complete_response_transfer_file
content_scope: complete_final_user_visible_response
source_response: 本轨道会话第一条回复（启动仪式回报，2026-08-30/31）
task_id: FABLE5-REDESIGN-001
generated_by_actor: claude-fable-5
generated_on_surface: claude-code-vscode
role: auxiliary_transfer_and_archival_copy
fidelity_note: 以下正文为该回复的逐字保存（Markdown 结构原样）；本 YAML 头是转移文件自身的元数据，不属于原回复内容
```

---

## 无需用户操作

本轮只等你一个字的**门 0 批示**（进 / 改 / 停）；不需要合并、上传或任何仓库操作。

## 启动仪式五步完成情况

**1. 写前预检** — 首跑在旧分支被脚本拒绝（PR #322 已合并，不得续写），切至最新 master 后重跑通过。gh 已登录（08822407d）。**钉住 master：`ccd4243`**（PR #322 合并提交；工作令正文与之逐字一致）。

**2. 指导加载** — 核心集全部读完；条件件按本轨道触发读了 8 份（谱系、run-context、产物交付含完整回复转移文件条款、跨对话、原件保全/设计理由、Ready-PR、下一步写入可见性、分支台账）。4 份未触发（外部研究命名、Deep Research 交付、澄清路由、合并分支处置）到期再读。整编检查：注册表基线后无新增 guard、未满 8 周，**本轮无整编到期**。

```yaml
mnemosyne_guidance_refresh:
  operation: behavior_constraint_refresh
  current_conversation_task_preserved: true   # FABLE5-REDESIGN-001，未导入维护线
  handoff_started: false
  maintenance_live_route_imported: false
  auto_handoff_detection_performed: false
  execution_source: current/human-approved-spec.md
  applied_constraints: 全部 34 项（含 layered_core_conditional_loading_shadow_pilot）
```

**3. 材料完整性核对** — 工作令 §2 共 A1–A8、B1–B8、C 类：

- 全部可读，**BLOCKED：无**。
- 一处需你知悉：**B4**（MNEMOSYNE-253 审核分工设计稿）**不在 master 上**，只存在于未合并的 PR #316 分支。已从该分支读到（78 行，自标"非执行源建议草稿，落点待 Owner 选"）。我将按"未采纳草稿"引用并标注，不替代、不当作已生效。
- A5 Issue #265：正文 TODO 1–4 加 6 条你的评论（TODO 5、三条临时构想补充）都能经 gh 读到。
- A8 Alaya 私档（`~/projs/Alaya` @ 2026-08-28）：谱系起源、GeodataMaster 1 件、MNE 57 件、MA 26 件、索引 4 份，只读可达；阶段 0 会附读取清单，引用 ≤200 字且不含隐私。
- `project-knowledge/` 目录尚不存在，阶段 1 若出 Deep Research 任务书时再建。

**4. 分支与 PR** — 分支 `fable5-redesign-001-workspace`（自 `ccd4243`），**Draft PR #323**：https://github.com/08822407d/Mnemosyne/pull/323。Draft 例外理由已记录（多阶段门控、内容随门变化、工作令明示）。两次提交（启动记录、回填 PR 号）均带四行署名尾注并已推送；写入仅 `09-continuation/00-startup-record.md` 一个文件。与唯一另一个 open PR #316 路径无交集。

**5. 阶段计划** —

| 门 | 交付 | 内容要点 |
|---|---|---|
| 0 | `01-goals-register.md` | 从 A 类抽全你的 G/C/O/H/P 条目，新旧两版分列带出处；一致/演化/矛盾三分，矛盾并列不调和；每条 G 配可验收标准草案（"像同一个对话"给体感＋机械双指标） |
| 1 | `02-…feasibility.md`、`03-research-questions.md` | 逐条自洽与三档可行性；研究问题只列"影响具体决定"的；平台事实引 B8，缺的标 UNKNOWN |
| 2 | `04-redesign-fable.md` | 只对登记表负责的独立重设计（含耐久核心/可再生层、三态循环、需求生命周期状态机、加载投影、目的核查、Owner-touch 预算、交接方案与效果测试、迁移、反模式自检、自我批判） |
| 3 | `05-pro-counterpart-package.md` | 交 GPT-Pro 的对照/盲评任务书（含回传文件要求与专用材料文件夹） |

同族局限声明：工作令与本轨道均为 Claude 族起草/执行；异构对照留待门 3。

## 下一步

- 动作：你批示后进入阶段 0，产出目标登记表；本会话执行。
- 模型要求：下一步**必须使用 Pro**（多源综合、矛盾并列、把目标翻译成可验收标准——属开放式判断）。
- 下一步仓库写入：**是**——Mnemosyne 仓库，分支 `fable5-redesign-001-workspace` / PR #323，新建 `01-goals-register.md`；已由工作令授权；与 #316 路径独立。
- Deep Research：阶段 0 不需要（NOT_NEEDED，材料全在本机）；阶段 1 再评估。
- 平行前沿复核：阶段 0 不需要（DEFER_UNTIL_PRIMARY_RESULT）；门 3 为异构对照专设。

本轮对核心目标推进了什么：零推进设计本身，但完成了"新会话零记忆冷启动"的一次真实样本——从工作令出发，仅凭仓库文件恢复了目标、阶段、边界与安全的下一动作，过程记录在启动记录中，可作阶段 2 交接方案的第一手对照材料。
