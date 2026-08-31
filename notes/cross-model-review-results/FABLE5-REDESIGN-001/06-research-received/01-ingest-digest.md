# 研究消化记录 · MNE-DR-020 / 021 → 对本轨道决定的影响

```yaml
record_type: research_ingest_digest
track_id: FABLE5-REDESIGN-001
date: 2026-08-31
scope: 首轮消化（回收 7 日义务的履行）；深度利用在阶段 1/2 进行
evidence_status: 研究证据；平台类事实按 §11 时效条款对待，执行时以现场 UI 复核为准
```

## A. MNE-DR-020（平台能力刷新）→ 平台事实更新

1. **ChatGPT GitHub app 官方口径现为只读**（写入指向 Codex）——与本仓 2026-07 实测（经 app 建分支/文件/PR，PR #133 链）**冲突**。处置：两者都不当绝对；标 `stale_or_uncertain` 候选交维护线（B8 `chatgpt-github-app-surface-facts.md` §1），执行时以现场 action 列表＋审批卡为准。阶段 2 含义：ChatGPT 侧写入路径按"Codex/手动为主"保守设计。
2. **project-only memory 可原地转换**（未共享存量 Project）——DR6 旧结论过期；洁净室实验成本下降。
3. **deep research 后台模型与配额均官方不可知**（"最新模型"；配额看产品内计数器；agent mode 40/400 是另一配额）——任务书/操作流今后不得写死这两项。
4. **Claude 侧变化大**：网页跨聊天 Memory（topics，Free/Pro/Max 默认开）；Chat 端 Opus5/Sonnet5 = 1M 上下文；Claude Code 多模型 1M（含 Fable 5）；compaction 有损为官方承认；各表面 session 历史不互通。阶段 2 含义：Claude 原生连续层可首次作为**辅助**通道纳入设计（仍不作真相源——报告同时确认三家原生记忆均为抽取式/不透明）。
5. **自识别**：ChatGPT 无官方运行时自识别（旧结论确认成立）；Codex/Claude Code 有客户端级模型元数据但≠自然语言自省。署名惯例 §6 分级维持，Codex 行可补注。
6. **旧结论核对表 9 项：3 过期 / 2 成立 / 4 无法确认**——"无法确认"项（含 synced-app-进-Memory、GitHub 枚举保证、Research 读 GitHub、JSONL 逐响应 model 字段）不得当作已翻转，涉及时现场验证。
   - 其中第 9 项（Claude Code JSONL 含逐响应 model 字段）本仓有 2026-08 委派实验的**本地实测**为据（署名惯例 §4）——报告只是未找到官方文档保证，两者不矛盾；分级维持"平台记录级证据"。

**交维护线的 stale 标记候选**：chatgpt-github-app-surface-facts §1（写能力）；chatgpt-github-app-capabilities-guide-v0.1（2026-07 快照整体）；DR6 结论 #1（project-only 不可转换）。

## B. MNE-DR-021（跨会话连续性实践与评测）→ 设计与验收证据

1. **逐字保存优于抽取替代**（约束探针 91% vs 14%；两基准 +15.9~22pp；69% 失败发生在抽取写入时）→ 直接支持登记表 N-02/N-14 与 raw 层设计（O-13）；阶段 2 铁则候选：摘要/结构/图**叠加**于原文并带回指针，永不替代。
2. **当前态≠历史态**（StateMemBench 显式 supersession +32~67pp；Memora：64% 推荐错误源于未忘过期记忆）→ 我们只有 Git 历史、没有显式 current-state/supersession 机制——阶段 2 必答设计题；验收加"过期状态误用率"。
3. **Handoff Debt**：仅有仓库状态 → 大量重发现（交接上下文减 20~59% 事件、42~63% tokens）→ "像同一个对话"的量化维度之一（rediscovery overhead），也证明交接包不可省。
4. **Handoff Tax**：全量轨迹非单调有益（低→高能力接手时 fresh restart 可更优；高→低时删轨迹显著受损）→ 阶段 2 交接方案应按能力方向分档、可选择表示，反对教条"全history"。
5. **fail-closed 接收协议行业普及度 UNKNOWN**——我们的差异化资产（8/13 伪造 SHA 事故为内部必要性实证）；可按 DreamBench-SWE 思路造对抗评测折（故意坏包测拒收）。
6. **公开描述层面我们缺**：检索层（EKV/dense 最强基线）、supersession 图、执行态 checkpoint 与信息交接分离、分 scope 记忆命名空间 → 阶段 2 设计输入清单四项。
7. **验收指标候选 10 项**（核心：Continuity Retention = 跨会话表现/同会话 oracle 表现，配 Continuation Success、Rediscovery Overhead、Current-State/Stale Error、Constraint Retention 四互补面）→ 待门 0 确认时并入登记表 §4.1 机械指标修订。
8. **记忆投毒为持久攻击面**（Microsoft 2026）→ 支持"authoritative 写入走人审合并"的信任边界；阶段 2 需为记忆条目设计来源/可信度字段。

## C. 处置

- RQ1/RQ2 → 已执行并回收；旧研究时效替换按 03 文件 §2 执行（DR6 平台部分由 020 接替，DR1/DR2 基准格局由 021 接替；方法论部分仍有效）。
- 本记录为首轮消化；阶段 1（自洽与可行性）与阶段 2（重设计）将逐条引用两报告原文。
- 候选交维护线：§A 的 stale 标记三条。
