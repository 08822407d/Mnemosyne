# MNEMOSYNE-034 Task Result

## task_id

MNEMOSYNE-034

## task_name

Objective Engineering Stance and Command Registry

## files_created

- `commands/README.md`
- `commands/load-mnemosyne-guidance.md`
- `commands/list-mnemosyne-commands.md`
- `notes/codex-task-results/MNEMOSYNE-034-result.md`

## files_modified

- `current/human-approved-spec.md`
- `handoff/startup-instructions.md`
- `handoff/handoff-current.md`
- `current/active-context.md`
- `current/todo.md`

## files_not_modified

- `raw/**`
- `raw/research-reports/**`
- `raw/user-design-restatements/**`
- PDF files
- `current/open-questions.md`
- `notes/candidate-requirements.md`
- `notes/decision-log.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/workflows/**`
- automation scripts
- missing light research prompt originals
- complete exported conversation records

## summary

- Appended the user-approved objective neutral engineering style principle to `current/human-approved-spec.md` as section 11.
- Added a lightweight `commands/` registry for user-facing invocation shortcuts.
- Added `Load Mnemosyne guidance` and `List Mnemosyne commands` command files.
- Updated startup, handoff, active context, and todo records to reflect MNEMOSYNE-034.
- Did not create `AGENTS.md`, `CLAUDE.md`, GitHub Actions, automation scripts, MCP, RAG, or auto-writeback.

## verification commands and outputs

```text
### git status --short
A  commands/README.md
A  commands/list-mnemosyne-commands.md
A  commands/load-mnemosyne-guidance.md
M  current/active-context.md
M  current/human-approved-spec.md
M  current/todo.md
M  handoff/handoff-current.md
M  handoff/startup-instructions.md
A  notes/codex-task-results/MNEMOSYNE-034-result.md
### git diff HEAD --stat
 commands/README.md                               | 27 ++++++++++++
 commands/list-mnemosyne-commands.md              | 35 +++++++++++++++
 commands/load-mnemosyne-guidance.md              | 54 ++++++++++++++++++++++++
 current/active-context.md                        |  7 +++
 current/human-approved-spec.md                   | 19 +++++++++
 current/todo.md                                  |  1 +
 handoff/handoff-current.md                       |  6 +++
 handoff/startup-instructions.md                  | 10 +++++
 notes/codex-task-results/MNEMOSYNE-034-result.md |  0
 9 files changed, 159 insertions(+)
### git diff HEAD --name-only
commands/README.md
commands/list-mnemosyne-commands.md
commands/load-mnemosyne-guidance.md
current/active-context.md
current/human-approved-spec.md
current/todo.md
handoff/handoff-current.md
handoff/startup-instructions.md
notes/codex-task-results/MNEMOSYNE-034-result.md
### targeted diff
diff --git a/commands/README.md b/commands/README.md
new file mode 100644
index 0000000..0d2ba7e
--- /dev/null
+++ b/commands/README.md
@@ -0,0 +1,27 @@
+# Mnemosyne Command Registry
+
+This directory is a lightweight registry for short user-facing commands.
+
+This file is not an execution source. Command files are not execution sources. Commands are invocation shortcuts only; they do not override `current/human-approved-spec.md`.
+
+Commands help users load Mnemosyne guidance in new ChatGPT conversations, Codex tasks, or future agent sessions when repository guidance is not automatically loaded.
+
+## Available commands
+
+| Command | Invocation examples | Purpose | Command file |
+| --- | --- | --- | --- |
+| Load Mnemosyne guidance | “Load Mnemosyne guidance.” / “加载 Mnemosyne 指导约束。” | Route a new session to the repository execution source, startup guidance, active context, handoff, todo, open questions, and relevant evidence views. | `commands/load-mnemosyne-guidance.md` |
+| List Mnemosyne commands | “List Mnemosyne commands.” / “列出 Mnemosyne commands。” | List available Mnemosyne command shortcuts, purposes, invocation phrases, and required files. | `commands/list-mnemosyne-commands.md` |
+
+## Invocation examples
+
+- “Load Mnemosyne guidance.”
+- “加载 Mnemosyne 指导约束。”
+- “List Mnemosyne commands.”
+- “列出 Mnemosyne commands。”
+
+## Future command convention
+
+- Use one command per file under `commands/`.
+- Each command file should include purpose, invocation examples, required files, behavior, and boundaries.
+- Future command files must remain user-facing shortcuts and must not become execution sources.
diff --git a/commands/list-mnemosyne-commands.md b/commands/list-mnemosyne-commands.md
new file mode 100644
index 0000000..6dda656
--- /dev/null
+++ b/commands/list-mnemosyne-commands.md
@@ -0,0 +1,35 @@
+# List Mnemosyne Commands
+
+This file is not an execution source. It defines how a session should list available Mnemosyne command shortcuts; it does not override `current/human-approved-spec.md`.
+
+## Command names
+
+- List Mnemosyne commands
+- 列出 Mnemosyne commands
+
+## Invocation examples
+
+- “List Mnemosyne commands.”
+- “列出 Mnemosyne commands。”
+
+## Purpose
+
+List the available Mnemosyne user-facing command shortcuts for a ChatGPT conversation, Codex task, or future agent session.
+
+## Required files
+
+- `commands/README.md`
+- Command files under `commands/`
+
+## Behavior
+
+- Read `commands/README.md` and command files under `commands/`.
+- Return a concise list of available commands, invocation phrases, purpose, and required files.
+- Do not modify repository files.
+- If command files are unavailable, state that the command registry cannot be fully listed.
+
+## Boundaries
+
+- The command registry is not an execution source.
+- Command listings do not override `current/human-approved-spec.md`.
+- Listing commands does not authorize repository modifications.
diff --git a/commands/load-mnemosyne-guidance.md b/commands/load-mnemosyne-guidance.md
new file mode 100644
index 0000000..e93b040
--- /dev/null
+++ b/commands/load-mnemosyne-guidance.md
@@ -0,0 +1,54 @@
+# Load Mnemosyne Guidance
+
+This file is not an execution source. It defines a user-facing shortcut for loading Mnemosyne repository guidance; it does not override `current/human-approved-spec.md`.
+
+## Command names
+
+- Load Mnemosyne guidance
+- 加载 Mnemosyne 指导约束
+
+## Invocation examples
+
+- “Load Mnemosyne guidance.”
+- “加载 Mnemosyne 指导约束。”
+
+## Purpose
+
+Use this one-line command at the beginning of a new ChatGPT conversation, Codex task, or future agent session when Mnemosyne repository guidance is not automatically loaded.
+
+## Required files
+
+At minimum, read or ask the user to provide:
+
+- `current/human-approved-spec.md`
+- `current/active-context.md`
+- `handoff/handoff-current.md`
+- `handoff/startup-instructions.md`
+- `current/todo.md`
+- `current/open-questions.md`
+- `notes/codex-task-authoring-and-diff-verification-guidelines.md`
+
+If the task involves tool capability, platform capability, model behavior, automation feasibility, or target-project memory-system design, also read the research evidence current views already referenced by `handoff/startup-instructions.md`.
+
+## Required behavior
+
+1. Do not rely on old conversation context or model memory.
+2. Treat `current/human-approved-spec.md` as the only execution source.
+3. Read or ask the user to provide the required files listed above.
+4. When applicable, also read the research evidence current views referenced by `handoff/startup-instructions.md`.
+5. Apply the objective neutral engineering stance from `current/human-approved-spec.md`.
+6. The first response after loading should include:
+   - current execution source;
+   - current phase;
+   - non-execution-source boundaries;
+   - current forbidden actions;
+   - current next-route options;
+   - whether any conflict or missing file was found.
+7. If required files are unavailable, ask for the missing files or clearly state the limitation. Do not invent repository state.
+
+## Boundaries
+
+- This command is a shortcut for loading existing repository guidance.
+- This command is not an execution source.
+- This command does not approve new design content.
+- This command does not authorize edits, automation, MCP, RAG, auto-writeback, or changes outside the user-approved task scope.
diff --git a/current/active-context.md b/current/active-context.md
index 1554095..9cb615c 100644
--- a/current/active-context.md
+++ b/current/active-context.md
@@ -4,6 +4,13 @@

 MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 dry-run independent verification 已完成，final verdict 为 PASS。当前等待用户选择下一路线：PDF 图表复核、Idea Capture Buffer / candidate cleanup、template review / small fixes 或 memory-system testing/debugging feasibility research。

+## MNEMOSYNE-034 status
+
+- Objective neutral engineering stance has been added to the execution source.
+- `commands/` registry has been added for lightweight user-facing guidance shortcuts.
+- No `AGENTS.md`, `CLAUDE.md`, GitHub Actions, or automation was added.
+- Current execution source remains `current/human-approved-spec.md`.
+
 ## MNEMOSYNE-031 current status

 MNEMOSYNE-031 final writeback checkpoint status:
diff --git a/current/human-approved-spec.md b/current/human-approved-spec.md
index 4d37b9a..ade0655 100644
--- a/current/human-approved-spec.md
+++ b/current/human-approved-spec.md
@@ -84,3 +84,22 @@
 - Codex Cloud 当前主要作为远程 GitHub 文件写入和版本保存助手。
 - v0.1 不包含自动查重、自动索引、自动 ID、自动 schema 校验、自动写回、自动交付、自动 drift 检查、自动模型迁移、GitHub Actions、AGENTS.md、CLAUDE.md、MCP、RAG、多 Agent 自动协调。
 - 这些属于 v0.2 或 future。
+
+## 11. 所属对话和任务的客观中立工程风格原则
+
+- “所属对话和任务”指与本仓库关联的 ChatGPT 对话、Codex 任务或未来 Agent 任务，关联目的包括：
+  - 改进或维护 Mnemosyne 本身；
+  - 为其他目标项目设计、复核或交付外部持久记忆系统。
+- 这些对话和任务均属于工程工作上下文。
+- 所属对话和任务必须使用客观、中立、证据约束的工程风格。
+- 所属对话和任务不得奉承用户、迎合用户偏好，或仅为了让用户构想显得正确而重塑结论。
+- 判断和输出应按以下顺序优先：
+  1. `current/human-approved-spec.md` 和已批准的仓库规则；
+  2. 仓库中已建立的 workflow / process rules；
+  3. 可验证的当前仓库状态；
+  4. 关于 AI models、services、tools 和 platform capabilities 的可验证当前事实；
+  5. 可靠的科学、技术和工程事实；
+  6. 当事实未确认时，明确标注不确定性。
+- 如果用户构想与仓库已批准规则、已知工具能力、可靠证据或当前客观事实冲突，Agent 应清楚说明冲突，并将该事项路由到 candidate / open question / research-gated 处理，而不是把它呈现为已批准设计。
+- 如果某项主张依赖关于 AI models、services、tools、product UI、pricing、APIs 或 platform behavior 的当前事实，Agent 必须将这些事实视为具有时效性，并在可能时进行验证；如果无法验证，应将该主张标注为未验证，而不是作为事实陈述。
+- 本原则不适用于与本仓库或 Mnemosyne 工作无关的其他用户对话。
diff --git a/current/todo.md b/current/todo.md
index d36ed2a..36f17d5 100644
--- a/current/todo.md
+++ b/current/todo.md
@@ -18,6 +18,7 @@

 ## v0.2

+- [x] MNEMOSYNE-034：objective neutral engineering stance and command registry.
 - [x] `MNEMOSYNE-025：self-improvement workflow 设计`；
 - [ ] 用户 review `notes/self-improvement-workflow.md`；
 - [x] 清理 notes/self-improvement-workflow.md 的 Codex Task Result Record 路径，默认占位符路径为 notes/codex-task-results/TASK_ID-result.md；
diff --git a/handoff/handoff-current.md b/handoff/handoff-current.md
index 1d08163..b87a28c 100644
--- a/handoff/handoff-current.md
+++ b/handoff/handoff-current.md
@@ -12,6 +12,12 @@ Mnemosyne 是记忆系统元 Agent 工作仓库，用于设计、演化和交付

 MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 first dry-run independent verification 已完成，final verdict 为 PASS。当前等待用户选择下一路线：PDF 图表复核、Idea Capture Buffer / candidate cleanup、template review / small fixes 或 memory-system testing/debugging feasibility research。

+## MNEMOSYNE-034 objective engineering stance / command registry
+
+- MNEMOSYNE-034 adds an objective neutral engineering stance to the execution source and adds a lightweight `commands/` registry.
+- New sessions can use “Load Mnemosyne guidance.” / “加载 Mnemosyne 指导约束。” when repository guidance is not automatically loaded.
+- Command files are not execution source.
+
 ## 当前执行源

 `current/human-approved-spec.md`
diff --git a/handoff/startup-instructions.md b/handoff/startup-instructions.md
index 8f1c640..07df3ed 100644
--- a/handoff/startup-instructions.md
+++ b/handoff/startup-instructions.md
@@ -18,6 +18,16 @@
 - 不应默认读取全部 raw；
 - 不应默认自动写回。

+
+## 2.1 客观中立工程风格与命令入口
+
+- Mnemosyne 所属 ChatGPT 对话、Codex 任务或未来 Agent 任务应遵循 `current/human-approved-spec.md` 中的客观中立工程风格原则：以执行源、仓库规则、可验证仓库状态、可验证当前工具 / 平台事实、可靠科学技术事实和明确不确定性为依据。
+- 如果新的 ChatGPT 对话或 Codex 任务不能自动加载仓库指导，用户可以说：
+  - “Load Mnemosyne guidance.”
+  - “加载 Mnemosyne 指导约束。”
+- 可用命令列在 `commands/README.md`。
+- `commands/` 命令注册表不是执行源，不能覆盖 `current/human-approved-spec.md`。
+
 ## 3. 标准读取顺序

 1. `README.md`
diff --git a/notes/codex-task-results/MNEMOSYNE-034-result.md b/notes/codex-task-results/MNEMOSYNE-034-result.md
new file mode 100644
index 0000000..e69de29
### presence 1
88:## 11. 所属对话和任务的客观中立工程风格原则
### presence 2
commands/README.md:13:| Load Mnemosyne guidance | “Load Mnemosyne guidance.” / “加载 Mnemosyne 指导约束。” | Route a new session to the repository execution source, startup guidance, active context, handoff, todo, open questions, and relevant evidence views. | `commands/load-mnemosyne-guidance.md` |
commands/README.md:18:- “Load Mnemosyne guidance.”
commands/load-mnemosyne-guidance.md:7:- Load Mnemosyne guidance
commands/load-mnemosyne-guidance.md:12:- “Load Mnemosyne guidance.”
### presence 3
commands/README.md:14:| List Mnemosyne commands | “List Mnemosyne commands.” / “列出 Mnemosyne commands。” | List available Mnemosyne command shortcuts, purposes, invocation phrases, and required files. | `commands/list-mnemosyne-commands.md` |
commands/README.md:20:- “List Mnemosyne commands.”
commands/list-mnemosyne-commands.md:7:- List Mnemosyne commands
commands/list-mnemosyne-commands.md:12:- “List Mnemosyne commands.”
### presence 4
commands/README.md:13:| Load Mnemosyne guidance | “Load Mnemosyne guidance.” / “加载 Mnemosyne 指导约束。” | Route a new session to the repository execution source, startup guidance, active context, handoff, todo, open questions, and relevant evidence views. | `commands/load-mnemosyne-guidance.md` |
commands/README.md:19:- “加载 Mnemosyne 指导约束。”
commands/load-mnemosyne-guidance.md:8:- 加载 Mnemosyne 指导约束
commands/load-mnemosyne-guidance.md:13:- “加载 Mnemosyne 指导约束。”
### protected
```

## protected file check

Command:

```bash
git diff HEAD --name-only | grep -E '^(raw/|AGENTS\.md$|CLAUDE\.md$|\.github/workflows/)' || true
```

Output: no protected files listed.

## known gaps

- `git fetch origin master && git reset --hard origin/master` could not run because this task environment has no configured `origin` remote. Work proceeded on the current branch after confirming the repository state locally.
- Verification output was captured before this result record was populated; the final diff therefore contains this result file content in addition to the recorded verification output.

## task_claims_completion

Yes. The target files were created or updated, and the protected file check listed no protected files.
