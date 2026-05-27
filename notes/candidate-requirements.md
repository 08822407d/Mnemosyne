# Candidate Requirements

> 说明：以下为从本次交接抽取的初始候选需求，不等同于最终实施版。

## CAND-0001
- 内容：Mnemosyne 应被定义为“记忆系统元 Agent”，服务多个项目/研究/团队场景，而非单一项目内部记忆库。
- 状态：reflected
- 备注：已在 `current/human-approved-spec.md` 高层原则中体现。

## CAND-0002
- 内容：采用“模型负责计算，文件负责记忆”的外部持久记忆原则。
- 状态：reflected
- 备注：已在 README 与实施版中体现。

## CAND-0003
- 内容：建立分层结构（raw、candidate、similarity/conflict、human-approved-spec、active-context/handoff）的职责边界。
- 状态：reflected
- 备注：当前仅完成最小结构，细节规则待补充。

## CAND-0004
- 内容：新需求进入实施版前，应执行查重、相似性分析与冲突分析，并提供合并/替换/拒绝/延期选项供用户决策。
- 状态：pending
- 备注：机制存在方向性共识，但流程模板与判定标准尚未定稿。

## CAND-0005
- 内容：引入自动化能力（自动写回、自动查重索引、多 Agent 自动协调等）。
- 状态：pending
- 备注：明确属于后续阶段，不在本次初始化范围。
