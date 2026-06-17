# MNEMOSYNE-035 Task Result

task_id: MNEMOSYNE-035

task_name: Action and Conclusion Separation Guidance

## files_created

- `notes/codex-task-results/MNEMOSYNE-035-result.md`

## files_modified

- `current/human-approved-spec.md`
- `handoff/startup-instructions.md`
- `handoff/handoff-current.md`
- `current/active-context.md`
- `current/todo.md`
- `commands/load-mnemosyne-guidance.md`

## files_not_modified

- `raw/**`
- `raw/research-reports/**`
- `raw/user-design-restatements/**`
- PDF files
- `current/open-questions.md`
- `notes/candidate-requirements.md`
- `notes/decision-log.md`
- `commands/README.md`
- `commands/list-mnemosyne-commands.md`
- `AGENTS.md`
- `CLAUDE.md`
- `.github/workflows/**`
- automation scripts
- missing light research prompt originals
- complete exported conversation records

## summary

- Added the user-approved operation/conclusion separation principle to `current/human-approved-spec.md` as section 12.
- Updated startup and load-command guidance to point to and apply the execution-source rule.
- Updated handoff, active context, and todo status with MNEMOSYNE-035 completion notes.
- Did not add unrelated principles, automation, AGENTS.md, CLAUDE.md, GitHub Actions, MCP, RAG, or auto-writeback.

## verification commands and outputs

Verification was run once before creating this result record. The presence check for this result file was expectedly missing at that point. The final verification after creating this record is below.

```text
$ git status --short
 M commands/load-mnemosyne-guidance.md
 M current/active-context.md
 M current/human-approved-spec.md
 M current/todo.md
 M handoff/handoff-current.md
 M handoff/startup-instructions.md

$ git diff HEAD --stat
 commands/load-mnemosyne-guidance.md |  7 +++++--
 current/active-context.md           |  7 +++++++
 current/human-approved-spec.md      | 22 ++++++++++++++++++++++
 current/todo.md                     |  1 +
 handoff/handoff-current.md          |  6 ++++++
 handoff/startup-instructions.md     |  3 +++
 6 files changed, 44 insertions(+), 2 deletions(-)

$ git diff HEAD --name-only
commands/load-mnemosyne-guidance.md
current/active-context.md
current/human-approved-spec.md
current/todo.md
handoff/handoff-current.md
handoff/startup-instructions.md

$ git diff HEAD -- current/human-approved-spec.md handoff/startup-instructions.md handoff/handoff-current.md current/active-context.md current/todo.md commands/load-mnemosyne-guidance.md notes/codex-task-results/MNEMOSYNE-035-result.md
diff --git a/commands/load-mnemosyne-guidance.md b/commands/load-mnemosyne-guidance.md
index e93b040..fb48097 100644
--- a/commands/load-mnemosyne-guidance.md
+++ b/commands/load-mnemosyne-guidance.md
@@ -37,14 +37,17 @@ If the task involves tool capability, platform capability, model behavior, autom
 3. Read or ask the user to provide the required files listed above.
 4. When applicable, also read the research evidence current views referenced by `handoff/startup-instructions.md`.
 5. Apply the objective neutral engineering stance from `current/human-approved-spec.md`.
-6. The first response after loading should include:
+6. Apply the operation/conclusion separation principle from `current/human-approved-spec.md`.
+7. If the response asks the user to do something, put the operation steps/content in a clearly marked section before explanation.
+8. If the response reports findings or conclusions, put the conclusion/problem/result in a clearly marked section before supporting explanation.
+9. The first response after loading should include:
    - current execution source;
    - current phase;
    - non-execution-source boundaries;
    - current forbidden actions;
    - current next-route options;
    - whether any conflict or missing file was found.
-7. If required files are unavailable, ask for the missing files or clearly state the limitation. Do not invent repository state.
+10. If required files are unavailable, ask for the missing files or clearly state the limitation. Do not invent repository state.
 
 ## Boundaries
 
diff --git a/current/active-context.md b/current/active-context.md
index 9cb615c..bd2b0e2 100644
--- a/current/active-context.md
+++ b/current/active-context.md
@@ -4,6 +4,13 @@
 
 MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 dry-run independent verification 已完成，final verdict 为 PASS。当前等待用户选择下一路线：PDF 图表复核、Idea Capture Buffer / candidate cleanup、template review / small fixes 或 memory-system testing/debugging feasibility research。
 
+## MNEMOSYNE-035 status
+
+- Operation/conclusion separation guidance has been added to the execution source.
+- The load command has been updated to apply the guidance.
+- No `AGENTS.md`, `CLAUDE.md`, GitHub Actions, or automation was added.
+- Current execution source remains `current/human-approved-spec.md`.
+
 ## MNEMOSYNE-034 status
 
 - Objective neutral engineering stance has been added to the execution source.
diff --git a/current/human-approved-spec.md b/current/human-approved-spec.md
index ade0655..15b33dd 100644
--- a/current/human-approved-spec.md
+++ b/current/human-approved-spec.md
@@ -103,3 +103,25 @@
 - 如果用户构想与仓库已批准规则、已知工具能力、可靠证据或当前客观事实冲突，Agent 应清楚说明冲突，并将该事项路由到 candidate / open question / research-gated 处理，而不是把它呈现为已批准设计。
 - 如果某项主张依赖关于 AI models、services、tools、product UI、pricing、APIs 或 platform behavior 的当前事实，Agent 必须将这些事实视为具有时效性，并在可能时进行验证；如果无法验证，应将该主张标注为未验证，而不是作为事实陈述。
 - 本原则不适用于与本仓库或 Mnemosyne 工作无关的其他用户对话。
+
+## 12. 操作内容 / 结论与说明分离原则
+
+- 本原则适用于 Mnemosyne 所属 ChatGPT 对话、Codex 任务和未来 Agent 任务；这些任务的目的包括构建、维护、修复、复核、验证或扩展 Mnemosyne 本身。
+- 本原则也适用于上述对话和任务为目标项目设计外部持久记忆系统的场景。
+- 当回复需要用户执行手动操作时，回复必须清楚分离：
+  1. 操作步骤 / 操作内容；
+  2. 支撑性说明 / 分析。
+- 当回复报告问题、结论、验证结果或 review findings 时，回复必须清楚分离：
+  1. 问题 / 结论 / 结果；
+  2. supporting explanation / analysis。
+- 操作步骤应在视觉上突出，并且便于用户复制或照做。
+- 说明性分析可以跟在操作内容之后，但不得把必需的用户操作埋在长篇分析中。
+- 以下场景尤其需要遵守本原则：
+  - 从讨论生成 Codex task；
+  - 告诉用户在 GitHub / Codex / 另一段 ChatGPT 对话中要做什么；
+  - 在旧对话和新对话之间交接工作；
+  - 报告 Codex PR 或 task 是否成功；
+  - 列出仓库验证过程中发现的问题。
+- 本原则不要求每个短回答都使用僵硬格式；当用户操作、review findings、验证结果或任务交接内容可能被长篇说明淹没时，本原则适用。
+- 本原则本身不授权任何仓库编辑；它只指导回复结构。
+
diff --git a/current/todo.md b/current/todo.md
index 36f17d5..674e460 100644
--- a/current/todo.md
+++ b/current/todo.md
@@ -18,6 +18,7 @@
 
 ## v0.2
 
+- [x] MNEMOSYNE-035：operation/conclusion separation guidance.
 - [x] MNEMOSYNE-034：objective neutral engineering stance and command registry.
 - [x] `MNEMOSYNE-025：self-improvement workflow 设计`；
 - [ ] 用户 review `notes/self-improvement-workflow.md`；
diff --git a/handoff/handoff-current.md b/handoff/handoff-current.md
index b87a28c..429b63f 100644
--- a/handoff/handoff-current.md
+++ b/handoff/handoff-current.md
@@ -18,6 +18,12 @@ MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint co
 - New sessions can use “Load Mnemosyne guidance.” / “加载 Mnemosyne 指导约束。” when repository guidance is not automatically loaded.
 - Command files are not execution source.
 
+## MNEMOSYNE-035 operation/conclusion separation guidance
+
+- MNEMOSYNE-035 adds operation/conclusion separation guidance.
+- Mnemosyne-affiliated sessions should not bury required user actions, problems, or conclusions inside long analysis.
+- Current execution source remains `current/human-approved-spec.md`.
+
 ## 当前执行源
 
 `current/human-approved-spec.md`
diff --git a/handoff/startup-instructions.md b/handoff/startup-instructions.md
index 07df3ed..409ae55 100644
--- a/handoff/startup-instructions.md
+++ b/handoff/startup-instructions.md
@@ -27,6 +27,9 @@
   - “加载 Mnemosyne 指导约束。”
 - 可用命令列在 `commands/README.md`。
 - `commands/` 命令注册表不是执行源，不能覆盖 `current/human-approved-spec.md`。
+- Mnemosyne 所属会话应将操作步骤 / 操作内容与说明性分析分离，并将问题报告、结论和验证结果与支撑性说明分离。
+- 这对 Codex task prompts、GitHub 操作、onboarding verification 和新旧对话 handoff 尤其重要。
+- 该规则的执行源位于 `current/human-approved-spec.md`。
 
 ## 3. 标准读取顺序
 

$ grep -n "操作内容" current/human-approved-spec.md
107:## 12. 操作内容 / 结论与说明分离原则
112:  1. 操作步骤 / 操作内容；
118:- 说明性分析可以跟在操作内容之后，但不得把必需的用户操作埋在长篇分析中。

$ grep -n "结论" current/human-approved-spec.md
95:- 所属对话和任务不得奉承用户、迎合用户偏好，或仅为了让用户构想显得正确而重塑结论。
107:## 12. 操作内容 / 结论与说明分离原则
114:- 当回复报告问题、结论、验证结果或 review findings 时，回复必须清楚分离：
115:  1. 问题 / 结论 / 结果；

$ grep -n "supporting explanation" current/human-approved-spec.md commands/load-mnemosyne-guidance.md
current/human-approved-spec.md:116:  2. supporting explanation / analysis。
commands/load-mnemosyne-guidance.md:42:8. If the response reports findings or conclusions, put the conclusion/problem/result in a clearly marked section before supporting explanation.

$ grep -n "operation steps" commands/load-mnemosyne-guidance.md
41:7. If the response asks the user to do something, put the operation steps/content in a clearly marked section before explanation.

$ grep -n "MNEMOSYNE-035" current/active-context.md current/todo.md handoff/handoff-current.md notes/codex-task-results/MNEMOSYNE-035-result.md
current/active-context.md:7:## MNEMOSYNE-035 status
current/todo.md:21:- [x] MNEMOSYNE-035：operation/conclusion separation guidance.
handoff/handoff-current.md:21:## MNEMOSYNE-035 operation/conclusion separation guidance
handoff/handoff-current.md:23:- MNEMOSYNE-035 adds operation/conclusion separation guidance.
grep: notes/codex-task-results/MNEMOSYNE-035-result.md: No such file or directory

$ git diff HEAD --name-only | grep -E '^(raw/|AGENTS\.md$|CLAUDE\.md$|\.github/workflows/)' || true
```

## protected file check

The protected file check is:

```text
git diff HEAD --name-only | grep -E '^(raw/|AGENTS\.md$|CLAUDE\.md$|\.github/workflows/)' || true
```

Expected output: no protected files listed.

The recorded output above is empty after the command line, meaning no protected files were listed.

## known gaps

- `git fetch origin master` could not be run because this checkout has no configured `origin` remote. Work was performed on the existing `work` branch state.
- None known after final staged verification.

## whether task claims completion

Yes. The task claims completion if final verification confirms that only the target files and this result record changed, and protected files remain unmodified.


## final staged verification commands and outputs

```text
$ git status --short
M  commands/load-mnemosyne-guidance.md
M  current/active-context.md
M  current/human-approved-spec.md
M  current/todo.md
M  handoff/handoff-current.md
M  handoff/startup-instructions.md
A  notes/codex-task-results/MNEMOSYNE-035-result.md

$ git diff HEAD --stat
 commands/load-mnemosyne-guidance.md              |   7 +-
 current/active-context.md                        |   7 +
 current/human-approved-spec.md                   |  22 +++
 current/todo.md                                  |   1 +
 handoff/handoff-current.md                       |   6 +
 handoff/startup-instructions.md                  |   3 +
 notes/codex-task-results/MNEMOSYNE-035-result.md | 239 +++++++++++++++++++++++
 7 files changed, 283 insertions(+), 2 deletions(-)

$ git diff HEAD --name-only
commands/load-mnemosyne-guidance.md
current/active-context.md
current/human-approved-spec.md
current/todo.md
handoff/handoff-current.md
handoff/startup-instructions.md
notes/codex-task-results/MNEMOSYNE-035-result.md

$ git diff HEAD -- current/human-approved-spec.md handoff/startup-instructions.md handoff/handoff-current.md current/active-context.md current/todo.md commands/load-mnemosyne-guidance.md notes/codex-task-results/MNEMOSYNE-035-result.md
diff --git a/commands/load-mnemosyne-guidance.md b/commands/load-mnemosyne-guidance.md
index e93b040..fb48097 100644
--- a/commands/load-mnemosyne-guidance.md
+++ b/commands/load-mnemosyne-guidance.md
@@ -37,14 +37,17 @@ If the task involves tool capability, platform capability, model behavior, autom
 3. Read or ask the user to provide the required files listed above.
 4. When applicable, also read the research evidence current views referenced by `handoff/startup-instructions.md`.
 5. Apply the objective neutral engineering stance from `current/human-approved-spec.md`.
-6. The first response after loading should include:
+6. Apply the operation/conclusion separation principle from `current/human-approved-spec.md`.
+7. If the response asks the user to do something, put the operation steps/content in a clearly marked section before explanation.
+8. If the response reports findings or conclusions, put the conclusion/problem/result in a clearly marked section before supporting explanation.
+9. The first response after loading should include:
    - current execution source;
    - current phase;
    - non-execution-source boundaries;
    - current forbidden actions;
    - current next-route options;
    - whether any conflict or missing file was found.
-7. If required files are unavailable, ask for the missing files or clearly state the limitation. Do not invent repository state.
+10. If required files are unavailable, ask for the missing files or clearly state the limitation. Do not invent repository state.
 
 ## Boundaries
 
diff --git a/current/active-context.md b/current/active-context.md
index 9cb615c..bd2b0e2 100644
--- a/current/active-context.md
+++ b/current/active-context.md
@@ -4,6 +4,13 @@
 
 MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 dry-run independent verification 已完成，final verdict 为 PASS。当前等待用户选择下一路线：PDF 图表复核、Idea Capture Buffer / candidate cleanup、template review / small fixes 或 memory-system testing/debugging feasibility research。
 
+## MNEMOSYNE-035 status
+
+- Operation/conclusion separation guidance has been added to the execution source.
+- The load command has been updated to apply the guidance.
+- No `AGENTS.md`, `CLAUDE.md`, GitHub Actions, or automation was added.
+- Current execution source remains `current/human-approved-spec.md`.
+
 ## MNEMOSYNE-034 status
 
 - Objective neutral engineering stance has been added to the execution source.
diff --git a/current/human-approved-spec.md b/current/human-approved-spec.md
index ade0655..15b33dd 100644
--- a/current/human-approved-spec.md
+++ b/current/human-approved-spec.md
@@ -103,3 +103,25 @@
 - 如果用户构想与仓库已批准规则、已知工具能力、可靠证据或当前客观事实冲突，Agent 应清楚说明冲突，并将该事项路由到 candidate / open question / research-gated 处理，而不是把它呈现为已批准设计。
 - 如果某项主张依赖关于 AI models、services、tools、product UI、pricing、APIs 或 platform behavior 的当前事实，Agent 必须将这些事实视为具有时效性，并在可能时进行验证；如果无法验证，应将该主张标注为未验证，而不是作为事实陈述。
 - 本原则不适用于与本仓库或 Mnemosyne 工作无关的其他用户对话。
+
+## 12. 操作内容 / 结论与说明分离原则
+
+- 本原则适用于 Mnemosyne 所属 ChatGPT 对话、Codex 任务和未来 Agent 任务；这些任务的目的包括构建、维护、修复、复核、验证或扩展 Mnemosyne 本身。
+- 本原则也适用于上述对话和任务为目标项目设计外部持久记忆系统的场景。
+- 当回复需要用户执行手动操作时，回复必须清楚分离：
+  1. 操作步骤 / 操作内容；
+  2. 支撑性说明 / 分析。
+- 当回复报告问题、结论、验证结果或 review findings 时，回复必须清楚分离：
+  1. 问题 / 结论 / 结果；
+  2. supporting explanation / analysis。
+- 操作步骤应在视觉上突出，并且便于用户复制或照做。
+- 说明性分析可以跟在操作内容之后，但不得把必需的用户操作埋在长篇分析中。
+- 以下场景尤其需要遵守本原则：
+  - 从讨论生成 Codex task；
+  - 告诉用户在 GitHub / Codex / 另一段 ChatGPT 对话中要做什么；
+  - 在旧对话和新对话之间交接工作；
+  - 报告 Codex PR 或 task 是否成功；
+  - 列出仓库验证过程中发现的问题。
+- 本原则不要求每个短回答都使用僵硬格式；当用户操作、review findings、验证结果或任务交接内容可能被长篇说明淹没时，本原则适用。
+- 本原则本身不授权任何仓库编辑；它只指导回复结构。
+
diff --git a/current/todo.md b/current/todo.md
index 36f17d5..674e460 100644
--- a/current/todo.md
+++ b/current/todo.md
@@ -18,6 +18,7 @@
 
 ## v0.2
 
+- [x] MNEMOSYNE-035：operation/conclusion separation guidance.
 - [x] MNEMOSYNE-034：objective neutral engineering stance and command registry.
 - [x] `MNEMOSYNE-025：self-improvement workflow 设计`；
 - [ ] 用户 review `notes/self-improvement-workflow.md`；
diff --git a/handoff/handoff-current.md b/handoff/handoff-current.md
index b87a28c..429b63f 100644
--- a/handoff/handoff-current.md
+++ b/handoff/handoff-current.md
@@ -18,6 +18,12 @@ MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint co
 - New sessions can use “Load Mnemosyne guidance.” / “加载 Mnemosyne 指导约束。” when repository guidance is not automatically loaded.
 - Command files are not execution source.
 
+## MNEMOSYNE-035 operation/conclusion separation guidance
+
+- MNEMOSYNE-035 adds operation/conclusion separation guidance.
+- Mnemosyne-affiliated sessions should not bury required user actions, problems, or conclusions inside long analysis.
+- Current execution source remains `current/human-approved-spec.md`.
+
 ## 当前执行源
 
 `current/human-approved-spec.md`
diff --git a/handoff/startup-instructions.md b/handoff/startup-instructions.md
index 07df3ed..409ae55 100644
--- a/handoff/startup-instructions.md
+++ b/handoff/startup-instructions.md
@@ -27,6 +27,9 @@
   - “加载 Mnemosyne 指导约束。”
 - 可用命令列在 `commands/README.md`。
 - `commands/` 命令注册表不是执行源，不能覆盖 `current/human-approved-spec.md`。
+- Mnemosyne 所属会话应将操作步骤 / 操作内容与说明性分析分离，并将问题报告、结论和验证结果与支撑性说明分离。
+- 这对 Codex task prompts、GitHub 操作、onboarding verification 和新旧对话 handoff 尤其重要。
+- 该规则的执行源位于 `current/human-approved-spec.md`。
 
 ## 3. 标准读取顺序
 
diff --git a/notes/codex-task-results/MNEMOSYNE-035-result.md b/notes/codex-task-results/MNEMOSYNE-035-result.md
new file mode 100644
index 0000000..769dba4
--- /dev/null
+++ b/notes/codex-task-results/MNEMOSYNE-035-result.md
@@ -0,0 +1,239 @@
+# MNEMOSYNE-035 Task Result
+
+task_id: MNEMOSYNE-035
+
+task_name: Action and Conclusion Separation Guidance
+
+## files_created
+
+- `notes/codex-task-results/MNEMOSYNE-035-result.md`
+
+## files_modified
+
+- `current/human-approved-spec.md`
+- `handoff/startup-instructions.md`
+- `handoff/handoff-current.md`
+- `current/active-context.md`
+- `current/todo.md`
+- `commands/load-mnemosyne-guidance.md`
+
+## files_not_modified
+
+- `raw/**`
+- `raw/research-reports/**`
+- `raw/user-design-restatements/**`
+- PDF files
+- `current/open-questions.md`
+- `notes/candidate-requirements.md`
+- `notes/decision-log.md`
+- `commands/README.md`
+- `commands/list-mnemosyne-commands.md`
+- `AGENTS.md`
+- `CLAUDE.md`
+- `.github/workflows/**`
+- automation scripts
+- missing light research prompt originals
+- complete exported conversation records
+
+## summary
+
+- Added the user-approved operation/conclusion separation principle to `current/human-approved-spec.md` as section 12.
+- Updated startup and load-command guidance to point to and apply the execution-source rule.
+- Updated handoff, active context, and todo status with MNEMOSYNE-035 completion notes.
+- Did not add unrelated principles, automation, AGENTS.md, CLAUDE.md, GitHub Actions, MCP, RAG, or auto-writeback.
+
+## verification commands and outputs
+
+Verification was run once before creating this result record. The presence check for this result file was expectedly missing at that point. The final verification after creating this record is below.
+
+```text
+$ git status --short
+ M commands/load-mnemosyne-guidance.md
+ M current/active-context.md
+ M current/human-approved-spec.md
+ M current/todo.md
+ M handoff/handoff-current.md
+ M handoff/startup-instructions.md
+
+$ git diff HEAD --stat
+ commands/load-mnemosyne-guidance.md |  7 +++++--
+ current/active-context.md           |  7 +++++++
+ current/human-approved-spec.md      | 22 ++++++++++++++++++++++
+ current/todo.md                     |  1 +
+ handoff/handoff-current.md          |  6 ++++++
+ handoff/startup-instructions.md     |  3 +++
+ 6 files changed, 44 insertions(+), 2 deletions(-)
+
+$ git diff HEAD --name-only
+commands/load-mnemosyne-guidance.md
+current/active-context.md
+current/human-approved-spec.md
+current/todo.md
+handoff/handoff-current.md
+handoff/startup-instructions.md
+
+$ git diff HEAD -- current/human-approved-spec.md handoff/startup-instructions.md handoff/handoff-current.md current/active-context.md current/todo.md commands/load-mnemosyne-guidance.md notes/codex-task-results/MNEMOSYNE-035-result.md
+diff --git a/commands/load-mnemosyne-guidance.md b/commands/load-mnemosyne-guidance.md
+index e93b040..fb48097 100644
+--- a/commands/load-mnemosyne-guidance.md
++++ b/commands/load-mnemosyne-guidance.md
+@@ -37,14 +37,17 @@ If the task involves tool capability, platform capability, model behavior, autom
+ 3. Read or ask the user to provide the required files listed above.
+ 4. When applicable, also read the research evidence current views referenced by `handoff/startup-instructions.md`.
+ 5. Apply the objective neutral engineering stance from `current/human-approved-spec.md`.
+-6. The first response after loading should include:
++6. Apply the operation/conclusion separation principle from `current/human-approved-spec.md`.
++7. If the response asks the user to do something, put the operation steps/content in a clearly marked section before explanation.
++8. If the response reports findings or conclusions, put the conclusion/problem/result in a clearly marked section before supporting explanation.
++9. The first response after loading should include:
+    - current execution source;
+    - current phase;
+    - non-execution-source boundaries;
+    - current forbidden actions;
+    - current next-route options;
+    - whether any conflict or missing file was found.
+-7. If required files are unavailable, ask for the missing files or clearly state the limitation. Do not invent repository state.
++10. If required files are unavailable, ask for the missing files or clearly state the limitation. Do not invent repository state.
+ 
+ ## Boundaries
+ 
+diff --git a/current/active-context.md b/current/active-context.md
+index 9cb615c..bd2b0e2 100644
+--- a/current/active-context.md
++++ b/current/active-context.md
+@@ -4,6 +4,13 @@
+ 
+ MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint consistency hard-fix 已执行并落账。MNEMOSYNE-032 dry-run independent verification 已完成，final verdict 为 PASS。当前等待用户选择下一路线：PDF 图表复核、Idea Capture Buffer / candidate cleanup、template review / small fixes 或 memory-system testing/debugging feasibility research。
+ 
++## MNEMOSYNE-035 status
++
++- Operation/conclusion separation guidance has been added to the execution source.
++- The load command has been updated to apply the guidance.
++- No `AGENTS.md`, `CLAUDE.md`, GitHub Actions, or automation was added.
++- Current execution source remains `current/human-approved-spec.md`.
++
+ ## MNEMOSYNE-034 status
+ 
+ - Objective neutral engineering stance has been added to the execution source.
+diff --git a/current/human-approved-spec.md b/current/human-approved-spec.md
+index ade0655..15b33dd 100644
+--- a/current/human-approved-spec.md
++++ b/current/human-approved-spec.md
+@@ -103,3 +103,25 @@
+ - 如果用户构想与仓库已批准规则、已知工具能力、可靠证据或当前客观事实冲突，Agent 应清楚说明冲突，并将该事项路由到 candidate / open question / research-gated 处理，而不是把它呈现为已批准设计。
+ - 如果某项主张依赖关于 AI models、services、tools、product UI、pricing、APIs 或 platform behavior 的当前事实，Agent 必须将这些事实视为具有时效性，并在可能时进行验证；如果无法验证，应将该主张标注为未验证，而不是作为事实陈述。
+ - 本原则不适用于与本仓库或 Mnemosyne 工作无关的其他用户对话。
++
++## 12. 操作内容 / 结论与说明分离原则
++
++- 本原则适用于 Mnemosyne 所属 ChatGPT 对话、Codex 任务和未来 Agent 任务；这些任务的目的包括构建、维护、修复、复核、验证或扩展 Mnemosyne 本身。
++- 本原则也适用于上述对话和任务为目标项目设计外部持久记忆系统的场景。
++- 当回复需要用户执行手动操作时，回复必须清楚分离：
++  1. 操作步骤 / 操作内容；
++  2. 支撑性说明 / 分析。
++- 当回复报告问题、结论、验证结果或 review findings 时，回复必须清楚分离：
++  1. 问题 / 结论 / 结果；
++  2. supporting explanation / analysis。
++- 操作步骤应在视觉上突出，并且便于用户复制或照做。
++- 说明性分析可以跟在操作内容之后，但不得把必需的用户操作埋在长篇分析中。
++- 以下场景尤其需要遵守本原则：
++  - 从讨论生成 Codex task；
++  - 告诉用户在 GitHub / Codex / 另一段 ChatGPT 对话中要做什么；
++  - 在旧对话和新对话之间交接工作；
++  - 报告 Codex PR 或 task 是否成功；
++  - 列出仓库验证过程中发现的问题。
++- 本原则不要求每个短回答都使用僵硬格式；当用户操作、review findings、验证结果或任务交接内容可能被长篇说明淹没时，本原则适用。
++- 本原则本身不授权任何仓库编辑；它只指导回复结构。
++
+diff --git a/current/todo.md b/current/todo.md
+index 36f17d5..674e460 100644
+--- a/current/todo.md
++++ b/current/todo.md
+@@ -18,6 +18,7 @@
+ 
+ ## v0.2
+ 
++- [x] MNEMOSYNE-035：operation/conclusion separation guidance.
+ - [x] MNEMOSYNE-034：objective neutral engineering stance and command registry.
+ - [x] `MNEMOSYNE-025：self-improvement workflow 设计`；
+ - [ ] 用户 review `notes/self-improvement-workflow.md`；
+diff --git a/handoff/handoff-current.md b/handoff/handoff-current.md
+index b87a28c..429b63f 100644
+--- a/handoff/handoff-current.md
++++ b/handoff/handoff-current.md
+@@ -18,6 +18,12 @@ MNEMOSYNE-031 R1-R5 review/restatement checkpoint 已完成；post-checkpoint co
+ - New sessions can use “Load Mnemosyne guidance.” / “加载 Mnemosyne 指导约束。” when repository guidance is not automatically loaded.
+ - Command files are not execution source.
+ 
++## MNEMOSYNE-035 operation/conclusion separation guidance
++
++- MNEMOSYNE-035 adds operation/conclusion separation guidance.
++- Mnemosyne-affiliated sessions should not bury required user actions, problems, or conclusions inside long analysis.
++- Current execution source remains `current/human-approved-spec.md`.
++
+ ## 当前执行源
+ 
+ `current/human-approved-spec.md`
+diff --git a/handoff/startup-instructions.md b/handoff/startup-instructions.md
+index 07df3ed..409ae55 100644
+--- a/handoff/startup-instructions.md
++++ b/handoff/startup-instructions.md
+@@ -27,6 +27,9 @@
+   - “加载 Mnemosyne 指导约束。”
+ - 可用命令列在 `commands/README.md`。
+ - `commands/` 命令注册表不是执行源，不能覆盖 `current/human-approved-spec.md`。
++- Mnemosyne 所属会话应将操作步骤 / 操作内容与说明性分析分离，并将问题报告、结论和验证结果与支撑性说明分离。
++- 这对 Codex task prompts、GitHub 操作、onboarding verification 和新旧对话 handoff 尤其重要。
++- 该规则的执行源位于 `current/human-approved-spec.md`。
+ 
+ ## 3. 标准读取顺序
+ 
+
+$ grep -n "操作内容" current/human-approved-spec.md
+107:## 12. 操作内容 / 结论与说明分离原则
+112:  1. 操作步骤 / 操作内容；
+118:- 说明性分析可以跟在操作内容之后，但不得把必需的用户操作埋在长篇分析中。
+
+$ grep -n "结论" current/human-approved-spec.md
+95:- 所属对话和任务不得奉承用户、迎合用户偏好，或仅为了让用户构想显得正确而重塑结论。
+107:## 12. 操作内容 / 结论与说明分离原则
+114:- 当回复报告问题、结论、验证结果或 review findings 时，回复必须清楚分离：
+115:  1. 问题 / 结论 / 结果；
+
+$ grep -n "supporting explanation" current/human-approved-spec.md commands/load-mnemosyne-guidance.md
+current/human-approved-spec.md:116:  2. supporting explanation / analysis。
+commands/load-mnemosyne-guidance.md:42:8. If the response reports findings or conclusions, put the conclusion/problem/result in a clearly marked section before supporting explanation.
+
+$ grep -n "operation steps" commands/load-mnemosyne-guidance.md
+41:7. If the response asks the user to do something, put the operation steps/content in a clearly marked section before explanation.
+
+$ grep -n "MNEMOSYNE-035" current/active-context.md current/todo.md handoff/handoff-current.md notes/codex-task-results/MNEMOSYNE-035-result.md
+current/active-context.md:7:## MNEMOSYNE-035 status
+current/todo.md:21:- [x] MNEMOSYNE-035：operation/conclusion separation guidance.
+handoff/handoff-current.md:21:## MNEMOSYNE-035 operation/conclusion separation guidance
+handoff/handoff-current.md:23:- MNEMOSYNE-035 adds operation/conclusion separation guidance.
+grep: notes/codex-task-results/MNEMOSYNE-035-result.md: No such file or directory
+
+$ git diff HEAD --name-only | grep -E '^(raw/|AGENTS\.md$|CLAUDE\.md$|\.github/workflows/)' || true
+```
+
+## protected file check
+
+The protected file check is:
+
+```text
+git diff HEAD --name-only | grep -E '^(raw/|AGENTS\.md$|CLAUDE\.md$|\.github/workflows/)' || true
+```
+
+Expected output: no protected files listed.
+
+The recorded output above is empty after the command line, meaning no protected files were listed.
+
+## known gaps
+
+- `git fetch origin master` could not be run because this checkout has no configured `origin` remote. Work was performed on the existing `work` branch state.
+- The first verification capture occurred before this result file existed, so it showed the result record as missing. A final verification should be run after this file is created and before commit.
+
+## whether task claims completion
+
+Yes. The task claims completion if final verification confirms that only the target files and this result record changed, and protected files remain unmodified.

$ grep -n "操作内容" current/human-approved-spec.md
107:## 12. 操作内容 / 结论与说明分离原则
112:  1. 操作步骤 / 操作内容；
118:- 说明性分析可以跟在操作内容之后，但不得把必需的用户操作埋在长篇分析中。

$ grep -n "结论" current/human-approved-spec.md
95:- 所属对话和任务不得奉承用户、迎合用户偏好，或仅为了让用户构想显得正确而重塑结论。
107:## 12. 操作内容 / 结论与说明分离原则
114:- 当回复报告问题、结论、验证结果或 review findings 时，回复必须清楚分离：
115:  1. 问题 / 结论 / 结果；

$ grep -n "supporting explanation" current/human-approved-spec.md commands/load-mnemosyne-guidance.md
current/human-approved-spec.md:116:  2. supporting explanation / analysis。
commands/load-mnemosyne-guidance.md:42:8. If the response reports findings or conclusions, put the conclusion/problem/result in a clearly marked section before supporting explanation.

$ grep -n "operation steps" commands/load-mnemosyne-guidance.md
41:7. If the response asks the user to do something, put the operation steps/content in a clearly marked section before explanation.

$ grep -n "MNEMOSYNE-035" current/active-context.md current/todo.md handoff/handoff-current.md notes/codex-task-results/MNEMOSYNE-035-result.md
current/active-context.md:7:## MNEMOSYNE-035 status
current/todo.md:21:- [x] MNEMOSYNE-035：operation/conclusion separation guidance.
handoff/handoff-current.md:21:## MNEMOSYNE-035 operation/conclusion separation guidance
handoff/handoff-current.md:23:- MNEMOSYNE-035 adds operation/conclusion separation guidance.
notes/codex-task-results/MNEMOSYNE-035-result.md:1:# MNEMOSYNE-035 Task Result
notes/codex-task-results/MNEMOSYNE-035-result.md:3:task_id: MNEMOSYNE-035
notes/codex-task-results/MNEMOSYNE-035-result.md:9:- `notes/codex-task-results/MNEMOSYNE-035-result.md`
notes/codex-task-results/MNEMOSYNE-035-result.md:42:- Updated handoff, active context, and todo status with MNEMOSYNE-035 completion notes.
notes/codex-task-results/MNEMOSYNE-035-result.md:75:$ git diff HEAD -- current/human-approved-spec.md handoff/startup-instructions.md handoff/handoff-current.md current/active-context.md current/todo.md commands/load-mnemosyne-guidance.md notes/codex-task-results/MNEMOSYNE-035-result.md
notes/codex-task-results/MNEMOSYNE-035-result.md:108:+## MNEMOSYNE-035 status
notes/codex-task-results/MNEMOSYNE-035-result.md:156:+- [x] MNEMOSYNE-035：operation/conclusion separation guidance.
notes/codex-task-results/MNEMOSYNE-035-result.md:168:+## MNEMOSYNE-035 operation/conclusion separation guidance
notes/codex-task-results/MNEMOSYNE-035-result.md:170:+- MNEMOSYNE-035 adds operation/conclusion separation guidance.
notes/codex-task-results/MNEMOSYNE-035-result.md:210:$ grep -n "MNEMOSYNE-035" current/active-context.md current/todo.md handoff/handoff-current.md notes/codex-task-results/MNEMOSYNE-035-result.md
notes/codex-task-results/MNEMOSYNE-035-result.md:211:current/active-context.md:7:## MNEMOSYNE-035 status
notes/codex-task-results/MNEMOSYNE-035-result.md:212:current/todo.md:21:- [x] MNEMOSYNE-035：operation/conclusion separation guidance.
notes/codex-task-results/MNEMOSYNE-035-result.md:213:handoff/handoff-current.md:21:## MNEMOSYNE-035 operation/conclusion separation guidance
notes/codex-task-results/MNEMOSYNE-035-result.md:214:handoff/handoff-current.md:23:- MNEMOSYNE-035 adds operation/conclusion separation guidance.
notes/codex-task-results/MNEMOSYNE-035-result.md:215:grep: notes/codex-task-results/MNEMOSYNE-035-result.md: No such file or directory

$ git diff HEAD --name-only | grep -E '^(raw/|AGENTS\.md$|CLAUDE\.md$|\.github/workflows/)' || true

```
