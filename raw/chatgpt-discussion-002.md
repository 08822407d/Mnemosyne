---
raw_id: RAW-0002
source_type: user_and_chatgpt_handoff
status: preserved
sensitivity: private
language: zh-CN
---

# RAW-0002：仓库初始化后的操作约定

这不是完整原始对话，而是从当前 ChatGPT 讨论中整理出的第二阶段交接记录。

## 浓缩记录

1. Mnemosyne 当前阶段采用中文作为主要工作语言。
   除文件名、目录名、命令、代码片段、Git/GitHub 固有术语、YAML/JSON key、ID、状态值、工具名和产品名等天然适合英文的内容外，仓库正文内容均使用中文。
   暂不采用中英双语对照，也不为中文正文额外添加英文翻译。

2. 当前阶段优先使用 Codex Cloud。
   用户可能在两台工作机器上并行推进设计、构建、部署和改进，希望先把精力放在核心业务和需求完善，而非本地环境和复杂工具链。

3. Codex Cloud 当前只承担远程 GitHub 文件写入和版本保存助手角色。
   当前阶段不主动设计自动化流程、构建流程、测试流程、GitHub Actions 或复杂平台适配层。

4. 当前自然语言研究与需求讨论仍在手工建立的 ChatGPT 对话中进行。
   待 Mnemosyne 仓库形成稳定的 human-approved-spec、active-context、handoff 等文件后，再评估迁移到正式版 ChatGPT 对话或其他正式 Agent 入口。

5. Codex Cloud 的 Versions / Best-of-N 当前应使用 1x。
   当前任务以保存与小步修改为主，不需要并行生成多候选版本；仅在比较多个架构/模板/路线时临时提高。

6. Codex Cloud 环境中的依赖、代码检查和测试设置当前应保持为空。
   Mnemosyne 当前是 Markdown-first 私有设计仓库，不是传统代码项目；不需要安装依赖、lint、test 或 setup script。

7. 当前阶段不追求一键全自动创建和维护。
   采用流程：ChatGPT 对话研究与澄清需求 -> 用户下发确认任务 -> Codex Cloud 小步修改仓库 -> 用户 review diff/PR -> 合并后仓库逐步成为外部真相源。

8. AGENTS.md、CLAUDE.md、GitHub Actions、自动查重、自动索引、model migration review、delivery manifest、隐私分级等能力属于后续独立 TODO。
   当前阶段不提前实现。
