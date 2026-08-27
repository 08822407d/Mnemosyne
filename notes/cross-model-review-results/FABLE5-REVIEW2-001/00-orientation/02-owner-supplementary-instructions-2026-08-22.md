# FABLE5-REVIEW2-001 — Owner 补充指令存档（2026-08-22）

```yaml
track_id: FABLE5-REVIEW2-001
record_type: owner_supplementary_instructions_verbatim_preservation
generated_by_model: claude-fable-5
surface: vscode
date: 2026-08-22
base_master_sha: 72b225d6a2faf42639cdc61c8b536439ccfdddce
evidence_class: DIRECT_OWNER_INSTRUCTION
preservation_note: >
  以下两条指令为 Owner 在门1 等待期间于本轨道会话中下达的补充指令，逐字保存。
  第一条在同会话新一轮对话中下达；第二条在执行第一条期间以插入消息方式下达。
  两条指令均不改变工作令的阶段与门结构，也不提前打开门1。
```

## 补充指令一（工具、权限、回复风格与模型验证）

---

我认为应当给你至少和chatgpt网页版相同的github仓库写入权限,不然每次都要我手工创建一堆内容很低效,因此我允许你在本机自动安装所需工具,并且你还得查验一下可靠资料看看我是否应该在github设置和claude用户设置中进行一些操作以达到让你可以免授权自动创建分支创建或修改文件以及创建pr.此外我建议你采用和chatgpt网页端相似的策略,每次最终回复里开头写我现在要进行的操作,结尾写下一步相关的内容,中间是本次工作的描述和解释,尽量不要加入项目自己的各种术语之类的英文单词,因为我不可能细读了解项目内部设计,所以任何需要我阅读的内容必须是人类可以轻松理解的,尤其是那些需要我人工决策的内容,此外当在claude code中工作时输出窗口中会包含大量的过程输出和所执行的命令以及其他内容,你应当假定我不会阅读这些内容.当前对话/任务的运行平台是vscode上的claude code插件,选择的模型是fable,智能程度(effort)是ultra.我曾经在claude网页版里尝试让对话识别自己运行中使用的模型,似乎是成功了,我认为现在你也应该验证一下.

---

## 补充指令二（Claude 产出的放置与作者溯源方案）

---

mnemosyne在之前的建设过程中都是由chatgpt网页端对话/work和codex cloud完成的工作,现在是首次用claude/claude code进行建设类工作,因此你暂时都要把你生成的内容放在单独的文件夹中,然后思考和设计一个方案让你(claude系列产品)生成的内容不必单独放置,但是又能清楚地记录下各内容变动(新增和修改等)都是谁做出的,等下周chatgpt的pro额度恢复后将由chatgpt pro和fable5共同确认这个方案.

---

## 执行侧理解登记（非指令原文）

- [DIRECT_OWNER_INSTRUCTION] 允许在本机自动安装所需工具；本次已安装 GitHub CLI（gh 2.98.0，用户目录级安装，无管理员权限）。
- [DIRECT_OWNER_INSTRUCTION] 查验可靠资料并给出 GitHub 侧与 Claude 侧的免打扰授权设置建议；已完成（官方文档：code.claude.com/docs 权限与设置页、cli.github.com 登录页）。
- [DIRECT_OWNER_INSTRUCTION] 回复格式改为：开头列操作、结尾列下一步、中间为通俗解释；避免项目内部术语；假定 Owner 不读过程输出。自本条起对本轨道所有后续回复生效。
- [DIRECT_OWNER_INSTRUCTION] Claude 产出暂时继续放独立文件夹（当前轨道目录本身即满足）；另行设计作者溯源方案草案，待下周 ChatGPT Pro 配额恢复后由 ChatGPT Pro 与 Fable 5 共同确认。草案见本目录 03 号文件。
- [VERIFIED_REPOSITORY_FACT] 运行环境验证结果：模型标识 claude-fable-5（系统运行环境声明与用户设置 `model: claude-fable-5[1m]` 一致，1M 上下文配置）；effort 配置值为 xhigh（设置枚举 low/medium/high/xhigh 中的最高档，与 Owner 所述 UI 档位 "ultra" 对应关系为界面标签，配置文件中无 "ultra" 取值）；运行入口 claude-vscode（VSCode 插件 2.1.239）。
- [MODEL_INFERENCE] 上述为配置与运行环境标识层面的验证；对后端实际加载模型不构成密码学证明——与仓库既有纪律（可见标签不等于运行时证明）一致。
- 一次权限边界事件：本会话尝试将免打扰权限规则写入 Owner 的 Claude 用户设置文件时，被 Claude Code 的安全分类器拦截（AI 不得自行修改自身权限配置）。已按拦截指引停止该动作，改为准备好配置文件由 Owner 手动应用。此事件如实登记。
