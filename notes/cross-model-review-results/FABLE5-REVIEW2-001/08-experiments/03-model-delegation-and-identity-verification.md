# Claude Code 模型委派与运行时身份识别 · 实证验证记录

```yaml
track_id: FABLE5-REVIEW2-001
record_type: capability_verification_record
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-23
evidence_class: VERIFIED_BY_LIVE_EXPERIMENT_in_this_environment
authority_level: non_execution_source_advisory_evidence
owner_questions:
  q1: Fable5 能否在 Claude Code 中自己做深度推理工作、把机械工作委派给 Opus 等低成本模型
  q2: Claude Code 会话能否识别自身运行时模型
  q3: （另行检索）Claude 网页端对话完整导出工具
```

## Q1 · 模型委派：**能，已实测**

- [VERIFIED] 本环境的子任务工具带 `model` 参数（可选 sonnet/opus/haiku/fable），主线程（Fable 5）可为每个子任务指定运行模型。本轨道当场验证：主线程 Fable 发射两个子任务，一个指定 opus、一个指定 haiku，各自正确自报运行模型（claude-opus-5 / claude-haiku-4-5-20251001）并正确完成机械校验题（371×289=107,219；483×176=85,008；字符串逆序均对）。
- [VERIFIED] 除逐次指定外，还可在项目的 agent 定义文件（.claude/agents/*.md frontmatter）里为特定 agent 类型固定模型——即可以定义"机械执行员=opus/haiku"的常驻分工，供指南固化。
- [适用面] 本验证在 VSCode 插件环境完成；CLI 与插件同引擎（同一 native binary），桌面 app 同源 [MODEL_INFERENCE，高置信但未逐面实测]。
- [成本注意] 订阅额度对不同模型的折算权重无法从会话内验证——"Opus 更省额度"方向上合理（更小模型单 token 成本更低）但未证实，指南设计时应实测或查官方说明后再写死。

## Q1 附带发现（对指南设计重要）

1. **子任务固定开销 ≈ 1.9 万 tokens**：两个只回答 8 行的探针各耗约 18.6k tokens（子任务自带完整环境提示）。→ 委派只对**有分量的任务**划算；碎活反而亏。指南应设"委派最小粒度"阈值。
2. **提交署名模板跟随主会话而非执行模型**：opus 探针的环境里提交签名指示仍写 "Claude Fable 5"（继承自主会话），它还因此错误推理"Opus 5 和 Fable 5 是同一模型的内部代号"。两层教训：(a) 子任务的提交若不显式改写 Actor 字段，会把 Opus 干的活记在 Fable 名下——**署名方案的 Actor 必须取执行模型而非主会话模型**（应并入联合确认议程 D 项）；(b) 模型自报正确 ≠ 模型对环境的解读正确，自报仍需与记录字段交叉核对。

## Q2 · 运行时身份识别：**能，且有三层，最强一层可事后机械审计**

| 层 | 内容 | 强度 |
|---|---|---|
| 1 运行时声明 | 系统上下文明示模型名与 ID（主会话与子任务各自声明各自的） | 会话内可读 |
| 2 配置/环境 | ~/.claude/settings.json 的 model 字段、环境变量（本轨道 8/22 已验证） | 本机可查 |
| 3 **逐条回复落盘** | 任务记录（JSONL）中每条助手回复带 `model` 字段——本任务实测 481 条全部为 claude-fable-5（另 11 条为系统合成占位） | **服务端返回、逐条持久化、可事后机械核对** |

- 对照意义：ChatGPT 侧的档位失实事件（P-11）之所以可能，是因为那边只有 UI 标签可看；Claude Code 的第 3 层提供了逐回复的机器可查记录，同类失实**可被事后审计发现**。
- 诚实边界（仓库纪律）：三层都是配置与平台元数据，非后端密码学证明；但"逐条落盘+可审计"已是当前各表面里最强的证据形态 [VERIFIED + MODEL_INFERENCE 比较]。

## Q3 · Claude 网页端对话导出工具（检索结果，时效性事实）

按"信息完整第一、简便第二"排序的候选（均声称本地处理不经外部服务器；安装前自行核验权限）：

1. **官方全量导出**（claude.ai 设置 → 隐私/账户 → 导出数据，邮件送 JSON 包）——完整性基线，覆盖全部对话原始数据；缺点：非增量、不便日常、可读性差。建议作为**底档**定期做一次。
2. **[Claude Conversation Exporter（socketteer，GitHub）](https://github.com/socketteer/Claude-Conversation-Exporter)**——JSON/Markdown/纯文本、**批量 ZIP、分支感知**（能导出对话的编辑分支——完整性关键项）、含元数据。
3. **[Claude Chat Exporter（Chrome 商店）](https://chromewebstore.google.com/detail/claude-chat-exporter/fagmaagfcmfdncfgngnbfboohodcofcd)**——TXT/MD/JSON，带**时间戳、YAML 头、思考块**（thinking 块常被别的工具丢掉）。
4. **[Claude Exporter（Chrome 商店）](https://chromewebstore.google.com/detail/claude-exporter/ifigplgihgdedekfaelihglkhdfogbme)**——MD/HTML/ZIP 含媒体文件，支持一键全部对话。
5. 备选：[agoramachina/claude-exporter](https://github.com/agoramachina/claude-exporter)（含 artifacts 导出）、[AI Toolbox](https://www.ai-toolbox.co/export-claude-conversations)。

建议组合：**官方 JSON 全量做底档 + 2 或 3 号做日常增量 Markdown**（2 强在分支与批量，3 强在时间戳与思考块）；先各导一个对话实测完整度再定主力。注：Claude Code 侧会话无需这些工具——本地 JSONL 已天然全量落盘（转换脚本已就绪）。

## 结论与后续

- Q1/Q2 均为"能"，且证据等级是当场实证。Owner 设想的"Fable 主推理 + 低成本模型做机械活"在 Claude Code 全系可落地，**为 Mnemosyne 及各元/业务 Agent 设计 Claude Code 专用模型切换指南**具备事实基础。
- 指南设计建议作为新的设计题立项（天然衔接：#265 TODO 3 的次档可靠性验证、本轨道 EXP-1 跨族对照、署名方案 Actor 字段修正）；按门3 约束，本记录只验证不设计，立项与时机由 Owner 定。
```
