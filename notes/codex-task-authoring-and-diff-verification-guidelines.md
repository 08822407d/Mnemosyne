# Codex Task Authoring and Diff Verification Guidelines

## file_positioning

- This file records a Mnemosyne workflow guardrail for authoring and reviewing Codex Cloud tasks.
- It is intended to be read by ChatGPT when preparing Codex task prompts and by Codex when executing repository-editing tasks.
- It is not an execution source.
- The current execution source remains `current/human-approved-spec.md`.
- If this file conflicts with `current/human-approved-spec.md`, the human-approved spec wins and the conflict should be recorded as an open question.

## problem_observed

During MNEMOSYNE-031, a failure mode was observed:

- Codex may receive a natural-language description of desired file changes.
- Codex may then produce a plausible task result or summary.
- The actual repository diff may show that not all intended files or sections were modified.
- In one cleanup task, Codex reported stale-phrase checks as passed even though direct repository inspection still found stale continuation guidance in current entry files.
- The problem was resolved only after using a hard-fix prompt with exact replacements and HEAD-based git diff verification.

## rule

For Codex tasks that modify repository files, natural-language completion claims are not enough.

A Codex file-modification task should require actual diff evidence, normally including:

- `git status --short`
- `git diff HEAD --stat`
- `git diff HEAD --name-only`
- targeted `git diff HEAD -- <target files>`
- grep/rg checks for expected additions, removals, or stale phrases when applicable
- protected-file verification
- a task result record comparing intended files with actual changed files

## when_to_use_exact_replacement_or_patch_script

Use exact replacement blocks, a patch script, or another deterministic edit method when the task:

- touches multiple files;
- edits entry files such as `current/active-context.md`, `handoff/handoff-current.md`, or `handoff/startup-instructions.md`;
- removes stale text or stale status;
- modifies task prompts, workflow templates, startup instructions, or handoff guidance;
- requires specific wording to be present or absent;
- has previously failed when described only in natural language;
- involves high-risk protected boundaries such as execution-source status, user confirmation, or forbidden files.

## codex_task_prompt_minimum_requirements

A Codex task prompt that modifies files should normally specify:

1. exact target files;
2. protected files that must not be touched;
3. whether to create, append, replace, or delete;
4. expected final status or exact replacement blocks;
5. verification commands;
6. required `git diff HEAD` output;
7. required grep/rg checks;
8. task result record path;
9. how to handle already-correct files;
10. instruction not to claim success unless the diff proves it.

## codex_execution_requirements

When Codex executes a repository-editing task, it should:

- make the actual file changes before writing a completion summary;
- inspect the diff before claiming success;
- report any target file that was skipped or already correct;
- include `git status --short`;
- include `git diff HEAD --stat`;
- include `git diff HEAD --name-only`;
- include targeted diff hunks for important files or exact replacements;
- verify that protected files were not modified;
- write a Codex Task Result Record for important tasks.

## task_result_record_requirements

For important Codex tasks, the task result record should include:

- task_id;
- task_name;
- files_intended_to_edit;
- files_actually_edited;
- files_created;
- files_modified;
- files_not_modified;
- claimed_completion;
- actual_git_status_short;
- actual_git_diff_stat;
- actual_git_diff_name_only;
- targeted_diff_hunks_or_summary;
- stale_phrase_or_presence_checks;
- protected_file_check;
- known_gaps;
- manual_review_required;
- follow_up_tasks;
- reviewer_notes.

## review_rule_for_chatgpt

When ChatGPT reviews a completed Codex task, it should not rely only on the Codex prose summary.

It should check:

- whether target files actually changed;
- whether expected text exists;
- whether stale text was removed;
- whether forbidden files stayed untouched;
- whether task result claims match repository content;
- whether another hard-fix task is required.

## non_goals

This guideline does not introduce automation.
It does not create AGENTS.md or CLAUDE.md.
It does not modify the execution source.
It does not make Codex task results authoritative over repository files.
