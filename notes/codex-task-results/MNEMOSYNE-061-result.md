task_id: MNEMOSYNE-061
task_name: Add staged Pro/Deep Research batch-gating guidance
started_from_latest_master: claimed_by_task_premise; initial local worktree status was checked before edits and no pre-existing uncommitted repository changes were observed in the edited paths.
user_instruction_summary: Add minimal execution-source and load-guidance behavior rules requiring dependency-aware staged generation/execution of Pro, Deep Research, cross-conversation, and similar high-cost prompt batches; require explicit execution location, model-strength switch reminder when needed, and preservation of target-project boundaries.
files_intended_to_edit:
  - current/human-approved-spec.md
  - commands/load-mnemosyne-guidance.md
  - current/active-context.md
  - current/todo.md
  - current/open-questions.md
  - handoff/handoff-current.md
files_actually_edited:
  - current/human-approved-spec.md
  - commands/load-mnemosyne-guidance.md
  - current/active-context.md
  - current/todo.md
  - current/open-questions.md
  - handoff/handoff-current.md
files_created:
  - notes/codex-task-results/MNEMOSYNE-061-result.md
files_modified:
  - current/human-approved-spec.md
  - commands/load-mnemosyne-guidance.md
  - current/active-context.md
  - current/todo.md
  - current/open-questions.md
  - handoff/handoff-current.md
files_not_modified:
  - raw/research-reports/**
  - raw/user-design-restatements/**
  - manual-import-inbox/**
  - AGENTS.md
  - CLAUDE.md
  - .github/workflows/**
  - automation scripts
  - target-projects/**
execution_source_update_summary: current/human-approved-spec.md was intentionally modified to add section 17, "Pro / Deep Research 分阶段生成与执行原则". The rule requires dependency checks before multi-prompt/high-cost task generation, staged generation/execution when upstream results may affect downstream prompts, explicit batch scope and result-return instructions, explicit `execute_in`/execution location per cross-conversation prompt, user model-strength switch reminder when needed, Deep Research full-body final-report compliance, and no authorization for asynchronous background work, automatic writeback, real target dry-runs, target material ingestion, or target repository writes.
load_guidance_update_summary: commands/load-mnemosyne-guidance.md now includes a concise required-behavior item for dependency-aware staged Pro/Deep Research/cross-conversation prompt batch-gating, current conversation intelligence/reasoning switch reminder when needed, explicit `execute_in` location, no downstream prompt generation when upstream results may change them, and Deep Research full-body final-answer requirement.
current_state_update_summary: current/active-context.md, current/todo.md, current/open-questions.md, and handoff/handoff-current.md now mention MNEMOSYNE-061 and record staged PRO/DR prompt-batch guidance while preserving no-target/no-dry-run/no-material/no-target-write boundaries and the current next route.
target_workspace_created: false
target_project_selected: false
target_materials_ingested: false
target_repository_written: false
real_target_project_dry_run_started: false
protected_file_check: PASS; protected path grep over git diff --name-only produced no output. No raw research reports, raw user-design restatements, manual-import-inbox files, AGENTS.md, CLAUDE.md, GitHub workflow files, automation scripts, or target-projects files were modified. No target workspace/material/dry-run/target write occurred.
verification_commands_and_outputs:
  - command: git status --short
    output: |
      M  commands/load-mnemosyne-guidance.md
      M  current/active-context.md
      M  current/human-approved-spec.md
      M  current/open-questions.md
      M  current/todo.md
      M  handoff/handoff-current.md
      A  notes/codex-task-results/MNEMOSYNE-061-result.md
  - command: git diff HEAD --stat
    output: |
       commands/load-mnemosyne-guidance.md              |   7 +-
       current/active-context.md                        |   2 +
       current/human-approved-spec.md                   |  15 +++
       current/open-questions.md                        |   6 ++
       current/todo.md                                  |   2 +
       handoff/handoff-current.md                       |   2 +
       notes/codex-task-results/MNEMOSYNE-061-result.md | 118 +++++++++++++++++++++++
       7 files changed, 149 insertions(+), 3 deletions(-)
  - command: git diff HEAD --name-only
    output: |
      commands/load-mnemosyne-guidance.md
      current/active-context.md
      current/human-approved-spec.md
      current/open-questions.md
      current/todo.md
      handoff/handoff-current.md
      notes/codex-task-results/MNEMOSYNE-061-result.md
  - command: grep -n "Pro / Deep Research 分阶段生成与执行原则" current/human-approved-spec.md
    output: "219:## 17. Pro / Deep Research 分阶段生成与执行原则"
  - command: grep -n "分阶段" current/human-approved-spec.md commands/load-mnemosyne-guidance.md
    output: |
      current/human-approved-spec.md:219:## 17. Pro / Deep Research 分阶段生成与执行原则
      current/human-approved-spec.md:222:- 如果前一批结果可能改变后一批 prompt / 课题 / Codex 修补任务，默认必须分阶段生成和执行；不得为了方便一次性生成全部后续 prompt。
      current/human-approved-spec.md:223:- 分阶段任务应明确：
  - command: grep -n "execute_in" current/human-approved-spec.md commands/load-mnemosyne-guidance.md
    output: |
      current/human-approved-spec.md:231:- 每个跨对话 prompt 必须显式写明 `execute_in` / 执行位置，例如当前维护对话、new Pro 扩展 conversation、new Pro Deep Research task、Codex Cloud task 等。
      commands/load-mnemosyne-guidance.md:47:12. When generating multiple Pro / Deep Research / cross-conversation prompts, apply dependency-aware staged batch-gating: remind/ask the user to switch current conversation intelligence/reasoning level before high-risk or high-cost prompt packages when needed, state each prompt's `execute_in` location, and do not generate downstream prompts if upstream batch results may change them. Deep Research prompts must require the full report body in the final answer.
  - command: grep -n "Deep Research 报告输出例外" current/human-approved-spec.md
    output: |
      159:### Deep Research 报告输出例外
      232:- Deep Research prompt 仍必须遵守第 13 节 Deep Research 报告输出例外：完整报告正文必须出现在最终报告 / 最终回答正文中，下载文件只能是辅助备份。
  - command: grep -n "MNEMOSYNE-061" current/active-context.md current/todo.md current/open-questions.md handoff/handoff-current.md notes/codex-task-results/MNEMOSYNE-061-result.md
    output_summary: MNEMOSYNE-061 appears in active context, TODO, open questions, handoff current, and this result record.
  - command: grep -n "No real target-project dry-run has occurred" current/active-context.md current/todo.md handoff/handoff-current.md
    output: |
      current/active-context.md:47:- No real target-project dry-run has occurred.
      current/todo.md:26:- No real target-project dry-run has occurred.
      handoff/handoff-current.md:30:- No real target-project dry-run has occurred.
  - command: grep -n "No target project has been selected" current/active-context.md current/todo.md handoff/handoff-current.md
    output: |
      current/active-context.md:48:- No target project has been selected.
      current/todo.md:28:- No target project has been selected.
      handoff/handoff-current.md:31:- No target project has been selected.
  - command: grep -n "No target materials" current/active-context.md current/todo.md handoff/handoff-current.md
    output: |
      current/active-context.md:49:- No target materials have been uploaded/ingested.
      current/todo.md:29:- No target materials have been uploaded/ingested.
      handoff/handoff-current.md:32:- No target materials have been uploaded/ingested.
  - command: grep -n "No target.*repository.*written" current/active-context.md current/todo.md handoff/handoff-current.md
    output: |
      current/active-context.md:50:- No target repository has been written.
      current/todo.md:30:- No target-project repository has been written.
      handoff/handoff-current.md:33:- No target-project repository has been written.
  - command: git diff HEAD --name-only | grep -E '^(raw/research-reports/|raw/user-design-restatements/|manual-import-inbox/|AGENTS\.md$|CLAUDE\.md$|\.github/workflows/|target-projects/)' || true
    output: "(no output)"
  - command: find target-projects -maxdepth 2 -type f -print 2>/dev/null || true
    output: "(no output)"
known_gaps: None identified for the requested minimal guidance update. The result record necessarily adds itself after the first verification pass and is included in final status/diff verification.
manual_review_required: Review section 17 in current/human-approved-spec.md, the load-guidance Required behavior bullet, and current-state references for acceptance.
completion_claim: MNEMOSYNE-061 added staged Pro/Deep Research prompt-generation guidance to the execution source, reflected it in load guidance and current-state files, created this result record with verification evidence, preserved target boundaries, did not modify protected paths, and did not create/select/ingest/run/write any target project material.
