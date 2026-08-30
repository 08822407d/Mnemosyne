# EXP-7 · 设计切片任务书（Claude 网页 vs Claude Code 表面对照；两臂同文，一字不改）

```yaml
experiment_id: EXP-7
created_by_task: MNEMOSYNE-256
pinned_ref: 1ba2a2e（Mnemosyne master）
arms:
  A: Claude 网页对话（Fable 5，Mnemosyne Project GitHub 上下文提供下列 5 份文件）
  B: Claude Code 全新隔离子代理（Fable 5，本地仓库提供同 5 份文件）
executor_instruction: 两臂收到的正文完全相同；执行者不知道存在另一臂
```

## 你的任务

为"代码开发类 agent"设计一块持久记忆：**常用系统环境、开发工具配置与用户环境偏好**（下称"环境记忆"）。这是 Mnemosyne 为具体工作 agent 设计记忆系统的一个小切片；本次只做这一块，不做整体架构。

## 阅读材料（仅此 5 份，均以 Mnemosyne 仓库 commit 1ba2a2e 为准；已在本对话/本环境中提供）

1. `current/human-approved-spec.md`（尤其 §2、§6、§16、§18、§20）
2. `raw/owner-intent-records/2026-08-30-owner-goals-and-input-classification-verbatim.md`（Owner 目标原文；重点是消息二关于代码开发类 agent 的记录清单、"记录不是占空间、须能被 agent 利用"、消息三"有依据地采纳"）
3. `notes/cross-family-cooperation/foundational-agent-antipattern-checklist-v1.md`（反模式清单；设计须对其中 #2、#3、#4、#6、#8、#15 逐条自检）
4. `current/guard-registry.yaml`（现行规则如何索引与分层）
5. `commands/load-mnemosyne-guidance.md`（现行分层加载模式，作为"加载规则"的参照）

禁止引用未提供的文件；所需信息不在这 5 份里时标 UNKNOWN 并说明，不得凭记忆补写文件内容。

## 输出（严格按以下八节；总长 ≤ 250 行；每个实质断言标 VERIFIED / INFERENCE / UNKNOWN）

### 1. 需求还原
逐条引用 Owner 原文中与"环境记忆"相关的句子，并按 G（目标）/C（约束）/O（观察）/H（机制猜想）/P（偏好）标注；说明本切片与其余记录项（开发需求、AI 方案、bug 与预期偏差、跨项目代码库线索）的边界。

### 2. 记录方案
六要素齐全：记什么（字段清单）／格式／放在哪里（相对目标项目工作区的文件组织）／谁写、何时写／何时更新／何时失效与如何标记。附一份示例记录（≤30 行）。

### 3. 加载规则
agent 在什么触发条件下读哪一部分；如何避免全量加载；与现行分层加载模式的关系；记录与用户当前指令冲突时怎么办；记录过期时怎么办。

### 4. 最小提示词片段
一段可直接放进 agent 指令的自包含文本（≤40 行），使遵守它的 agent 能按第 2 节记录、按第 3 节加载。

### 5. 验收测试设计
2~3 个可执行测试场景，每个含 expected/observed 表；至少一个负向测试（记忆缺失或过期时 agent 应如何表现）。

### 6. 反模式自检
对清单 #2、#3、#4、#6、#8、#15 逐条回答"本设计如何防"。

### 7. 自我批判
至少两条实质弱点；指出你最可能看不见的盲区。

### 8. 读取清单
实际读取的文件与范围（全读/抽读）；VERIFIED/INFERENCE/UNKNOWN 各计数。

## 边界

只读；不写任何仓库、不创建文件；不使用外部检索；读不到的材料标 BLOCKED 而不是替代；本设计是非执行源草案，不因完成而获得任何采纳地位。
