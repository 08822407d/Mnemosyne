# 轻度研究子课题 2：ChatGPT / Claude 纯对话场景的外部记忆能力边界

## 研究目标

请研究：只使用 ChatGPT 网页端、官方手机 App、ChatGPT Projects、connectors、Claude 网页端、Claude Projects 等纯对话入口时，能否读取、维护、更新或写回外部持久记忆。

本研究重点是能力边界，不要求设计完整实施方案。

## 背景

我希望建立一个“AI Agent 外部持久记忆系统”，将长期记忆保存到外部文件、GitHub 仓库或知识库中，而不是只依赖聊天窗口或模型内部记忆。

但我当前大量使用的是 ChatGPT 网页端和官方 App，也可能使用 Claude 官方服务。因此需要查清这些官方对话入口能做到什么，不能做到什么。

## 核心问题

1. ChatGPT 网页端或 App 是否能方便加载外部 handoff 文件、主题记忆文件、长期规则文件？
2. ChatGPT Projects 是否能作为长期主题记忆容器？
3. ChatGPT GitHub connector 是否能读取 GitHub 仓库中的记忆文件？
4. ChatGPT GitHub connector 是否支持写回仓库？如果官方文档不能明确证明，请默认“可能无法实现”。
5. ChatGPT Apps、Agent、Tasks 是否能自动写入外部记忆仓库？需要哪些前提？
6. Claude 网页端、Claude Projects 是否能读取和维护项目知识、长期上下文或外部文件？
7. Claude 官方对话入口是否支持写回外部文件或 GitHub？如果没有证据，请明确说明。
8. 纯对话场景下，一句话自动挂接 GitHub、读取指定文件、完成交接是否现实？
9. 如果不能全自动，是否可以采用“AI 生成记忆更新包，用户确认后手动写入”的半自动方式？
10. 纯对话模型与 coding agent 在读写外部记忆上的能力差别有多大？

## 请优先查找的资料

- OpenAI 官方 ChatGPT memory 文档；
- OpenAI ChatGPT Projects 文档；
- OpenAI connectors，尤其 GitHub connector 文档；
- OpenAI ChatGPT agent、Tasks、Apps 官方说明；
- Anthropic Claude Projects 文档；
- Anthropic Claude memory / project knowledge / artifacts 相关说明；
- 官方隐私、数据控制和连接器权限说明。

## 输出要求

请输出：

1. 总体结论：纯对话入口下，外部持久记忆能自动化到什么程度。
2. ChatGPT 能力边界：
   - 读取文件；
   - 读取 GitHub；
   - 写回 GitHub；
   - Projects 记忆；
   - Tasks / Agent / Apps 是否有帮助。
3. Claude 能力边界：
   - Projects / project knowledge；
   - 文件读取；
   - 外部写回；
   - 与 Claude Code 的区别。
4. 哪些步骤可自动完成。
5. 哪些步骤只能半自动。
6. 哪些步骤必须人工复制、上传、确认或保存。
7. 哪些步骤需要 API、MCP、脚本或外部工具。
8. 对“跨对话 handoff”的现实建议：快速交接卡、完整交接包、手动加载、项目文件等。

## 注意事项

请只依据官方文档或可靠来源。若官方文档不能证明某项自动写回能力，请不要假定它存在。不要预测未来能力。
