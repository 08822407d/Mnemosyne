# 基础 Agent 反模式清单 v1（Meta-Agent 与项目 agent 立项前置检查）

```yaml
record_type: antipattern_checklist
version: 1.0
created_by_task: MNEMOSYNE-254
authority_level: non_execution_source_checklist_owner_adjudication_pending
sources: Fable 五点诊断 v2 + GPT-Pro 独立复盘 Q8 十条 + 双族对照记录（MNEMOSYNE-254）
usage: 新 agent/新机制立项时逐条回答"是否已防"；答"否"须写明理由或对冲；本清单不自动施加义务，采纳后由 Owner 决定落点
evidence_base: 两族对同一档案（Alaya 82 份对话 + Mnemosyne 406 条记录）的独立复盘收敛项；每条附实证锚点
```

| # | 反模式 | 实证锚点 | 立项检查问题 | 已验证或建议的对冲 |
|---|---|---|---|---|
| 1 | 没有产品拉动就建流程（治理证据强于价值证据） | 两个月唯一下线的是交接协议本身；7/2 dry-run 无目标写入 | 本 agent 从第一天起对着哪个真实目标运行？ | 门 3 决定：A/B 作 MA 实测；无真实目标不开工 |
| 2 | 结果验收被格式验收替代 | 6 月百分制测"能否恢复"，8/10 才提"是否更快更省" | 成功标准里有没有"效用/效率/Owner 成本"维度？评分细则是否预冻结？ | EXP-3/5 预冻结细则；三条件交接评估 |
| 3 | 规则/记忆只增不减 | 13 份 guard、3800 行、修订全累加零整编 | 有没有内置合并/降级/退役循环与复杂度预算？ | guard-registry 整编触发；D-10 四问 |
| 4 | 事故→全局规则反射，无局部性判断门 | 每次事故产生更严协议→与执行面不匹配→新事故（G3~G7） | 新问题是否默认记为局部缺陷、升级全局需明确门？ | Pro 硬约束②：新问题默认局部 |
| 5 | 建设期无全局规则冻结窗口 | 7/2 后本可冻结四周跑真实闭环 | 试点期间是否冻结新增全局规则（除隐私/权限/不可逆事故）？ | Pro 硬约束①：冻结窗口 |
| 6 | "活"状态无失效规则 | P-01/02/07，20+ 残留修复 | 每个 live 状态有 canonical 源、last_updated、过期声明吗？ | MNEMOSYNE-244 头部惯例；§11 时效钩子 |
| 7 | 研究由额度调度、无采纳/过期/关闭闭环 | DR9/10/12、MA-DR-08~15 滞留裁定层；平台结论过期仍标有效 | 研究立项时绑定了"可能改变的决定"和到期 disposition 吗？ | loader 第 9 条；valid_as_of/supersession |
| 8 | 人做搬运（Owner 当消息总线） | 交接 4~6→7~9→9~15 步；三对话接力；人肉模型调度 | Owner-touch count 是不是一等指标？agent 间传递走仓库/工具还是走人手？ | Claude Code 直写实证；Owner-touch 计数 |
| 9 | 记账开销无上限 | 26% 记录为 PR 收尾；8/19~21 以保全/发布/收尾为主 | 收尾类占比阈值是多少？超限触发简化而非加流程？ | 建议阈值 15%（校准值） |
| 10 | 主导 agent 无"方向质疑"义务 | 两个月无方向级异议；8/7 获自主权仍选实验包 | agent 每周期是否须回答"本周对核心目标推进了什么"？答不出是否上报？ | 建议入 MA owner rule 与章程 §11 扩展 |
| 11 | 系统对 authority conflict 敏感、对 purpose drift 不敏感 | 规则冲突触发 fail-closed；目的漂移/负担增长/价值为零无停止条件 | 有没有与 fail-closed 同级的"目的核查"停止条件？ | 设计题：purpose-check 机制 |
| 12 | 在未验证执行面上签逐字节过程合同 | 235~239 五连败（大小写/blob/gh/路径长度） | 新表面先 bounded preflight 了吗？合同是终态式还是过程式？ | 执行源 §18 preflight；D-01/D-07 终态合同 |
| 13 | 一条超长主线充当研究路由/发布/验收/交接总线 | 24,755 行单对话仍在末尾靠旧对话核验新对话 | 主线是否按稳定产品对象或任务边界拆线？ | task-bound package + route locality |
| 14 | 同族自证独立性 | 旧 GPT 验新 GPT、Thinking/Pro 同族复核 | 高影响结论是否有异族/机械/人类之一的独立核验？ | §19 独立性声明；设计稿 H 分工 |
| 15 | 平台限制沉淀为核心规则 | P-06 三处时代快照；§14/§18 旧前提 | 平台应对措施是否标为平台事实而非规则？ | platform-guides 事实层 |
| 16 | 把"不知道"当待补字段 | 8/21 BLOCKED_NO_EXACT_TASK 是正确终态 | 安全停止是否被设计为一等结果？ | clean_failure_contract |

## 值得延续（两族一致）

执行源/证据/候选/历史分层；fail-closed + expected/observed + 不编造；任务绑定交接与路线局部性；fresh-context 负向测试；档案重建法评估交接效果；事故保全、可回滚、禁静默修复；挂账诚实与披露文化。
