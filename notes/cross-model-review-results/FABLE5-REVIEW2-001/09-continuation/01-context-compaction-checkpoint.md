# 压缩前续接检查点（2026-08-24，上下文 95% 时固化）

```yaml
track_id: FABLE5-REVIEW2-001
record_type: context_compaction_checkpoint
generated_by_model: claude-fable-5
surface: vscode_via_remote_control
evidence_class: working_state_snapshot
purpose: Owner 即将手动压缩上下文；本文件固化全部活性工作记忆，压缩后的会话以此为第一恢复源
recovery_order_after_compaction: 本文件 → 07-pro-handover/05（Owner 终审）→ 07-pro-handover/04（联合确认记录）→ 各设计稿按需
```

## 一、当前精确状态（截至本检查点）

- **合作方案已确认生效**：Owner 六节全批（05 号记录含逐字批示与三处修正：署名须带逐表面身份可信度分级；Owner 手动切换模型时会明告对话；"可验证严防＋残余风险明示接受"总方针）。
- **两份新设计已交付**：10 号（跨族交替协调四约定）、11 号（对话命名规范 `项目-主线-类型序号 主题`）。
- **等待 Owner 的三件事**（我最后一条回复的原话要点）：
  1. **批次一授权**：MNEMOSYNE-244（三处过期状态修复＋冻结头，写 current/）、245（规范登记表[仅索引不赋权]＋加载分层试点＋跨族四约定并入，写 current/ 与 commands/）、246（署名定稿落地＋命名规范并入登记表，写 notes/registries/）——各单分支单 PR；
  2. **PR #306 处置**（合并=隔离期结束；不合并不阻塞批次一）；
  3. **档案专用仓库命名**（候选：FenShen/XinJing/ZhiYin/MingJian，Owner 说慢慢想）。
- **我方欠的活（无需授权，轨道内）**：执行源修订最终 diff 包（设计稿B 按 Pro 裁定版整合成逐条可批文本）——已承诺未开工。

## 二、实施队列全景（联合确认记录第六节 + Owner 修正）

| # | 任务 | 状态 |
|---|---|---|
| 1 | 署名定稿（含身份可信度分级字段：ClaudeCode=运行时较可靠/ChatGPT=约一月前自称无可靠自识别、现状待复查/Codex=未查证） | 待授权(=246) |
| 2 | 执行源修订（先出 diff 包→Owner 逐条批→单独任务实施） | diff 包待做 |
| 3 | 规范层任务一 | 待授权(=245) |
| 4 | 过期状态修复 | 待授权(=244) |
| 5 | platform-guides 表面事实文件族（含调查项：ChatGPT 当前自识别能力复查、Codex 自识别查证） | 排队 |
| 6 | 两族风险分布登记簿定稿（改题+8 上下文字段） | 排队 |
| 7 | GPT 侧 EXP-3/EXP-5 对照（shadow pilot 一部分） | 排队 |
| 8 | PR #306 | Owner 单独定 |
| ③ | 审核分工形式设计（不单方不均分、按能力特长；衔接 #265 TODO 3 与 EXP-1） | 开放设计题 |

## 三、仍然有效的约束与惯例

- 写入授权：**仍仅轨道目录**（批次一批准后按各任务 scope 扩展）；执行源与既有文件不动；两保留分支不碰。
- 本会话提交已采用新版尾注（Agent-Action-Actor/Agent-Task/Agent-Content-Producer）；commit 前缀 FABLE5-REVIEW2-001:。
- 逐步 commit+push 纪律；证据类标签纪律；同族局限声明纪律。
- 隔离约束的条件已满足但 #306 未合并前，产出仍全部进轨道目录。

## 四、环境与本地资产地图（压缩后易失的操作性细节）

- **远程控制中**：Owner 经 claude.ai/code 网页接管本会话（家中 Ubuntu 为执行机）。
- 本地档案库 `~/projs/mnemosyne-archives/`：chatgpt/（56 份导出+改名日志）、claude-code/（本任务 JSONL 快照+readable/ 可读转录）、condition2-audits/（三份含引文审计原件）、experiments/（EXP-3/5 四臂+两探针原件与预登记细则）、tools/convert_claude_jsonl.py、三份归档索引 YAML。
- Owner 设置已开：免打扰允许清单（git/gh 白名单+危险操作黑名单）、autoContinueAtUsageLimit（**实测未生效**，见 C-13——断了让 Owner 说 Continue）、cleanupPeriodDays 3650。
- gh 已登录（08822407d，keyring）；分类器禁止我改自己的设置文件（两次实证）。
- Pro 两份复核文件已逐字入库（07-pro-handover/received/ 带哈希）。
- 档案缺口清单（待 Owner 继续导出）：235/238/239 执行会话、Meta-Agent 对话系、健康审查对话、F1 纠错接收对话、243 后当前 GPT 主线。

## 五、数字分身线（长期背景，勿丢）

档案库定位已升级为"数字分身原料库"（09 号构想登记）：三类未来数据（引导对话/gpt-live 松散语音/碎片笔记）；与 todo 三研究题+真实需求 B 合流；敏感度最高档（画像类产物默认仅本地）；命名候选见上文。真实需求 A/B 仍挂起（Meta-Agent 建设验证优先，A/B 用于实测它——门3 Q2 批示）。

## 六、压缩后自检清单（给恢复后的我）

1. 先读本文件；若与更新的仓库状态冲突，以 git log 最新为准；
2. 检查是否有 Owner 新批示未处理（批次一/#306/库名三问）；
3. 不要重做已完成工作（44+ 份轨道文件全在库，git log 是完成清单）；
4. 恢复后第一条回复向 Owner 确认恢复完整性（本文件哈希在 git）。
```
