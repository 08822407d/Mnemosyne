# MNEMOSYNE-032E Stale Codex Branch and Accept Incoming Rollback Note Result

## metadata

- task_id: MNEMOSYNE-032E
- task_type: workflow_troubleshooting_note
- record_is_execution_source: no

## purpose

Record the diagnosis that repeated missing Codex edits may be caused by stale Codex Cloud branch state plus unconditional "Accept Incoming" conflict resolution, not only by Codex failing to follow natural-language edit instructions.

## initial_repository_state

- initial_head: `b3379b4053535d0ecacd0a209a772a388f502cb0`
- initial_branch: `work`
- initial_status_short_before_patch: |
  M handoff/startup-instructions.md
   M notes/codex-task-authoring-and-diff-verification-guidelines.md
  A  notes/codex-task-results/MNEMOSYNE-032E-result.md

## files_intended_to_edit

- `notes/codex-task-authoring-and-diff-verification-guidelines.md`
- `handoff/startup-instructions.md`
- `notes/codex-task-results/MNEMOSYNE-032E-result.md`

## files_not_to_edit

- `current/human-approved-spec.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- research report originals
- prompt originals
- PDFs
- `AGENTS.md`
- `CLAUDE.md`
- GitHub Actions / automation files

## patch_script_results

- already_present: `notes/codex-task-authoring-and-diff-verification-guidelines.md` :: known failure mode section
- already_present: `handoff/startup-instructions.md` :: startup troubleshooting section

## verification

### git_status_short

- exit_code: `0`

```text
M handoff/startup-instructions.md
 M notes/codex-task-authoring-and-diff-verification-guidelines.md
AM notes/codex-task-results/MNEMOSYNE-032E-result.md
```

### git_diff_head_stat

- exit_code: `0`

```text
handoff/startup-instructions.md                    | 17 +++++++
 ...k-authoring-and-diff-verification-guidelines.md | 41 ++++++++++++++++
 notes/codex-task-results/MNEMOSYNE-032E-result.md  | 55 ++++++++++++++++++++++
 3 files changed, 113 insertions(+)
```

### git_diff_head_name_only

- exit_code: `0`

```text
handoff/startup-instructions.md
notes/codex-task-authoring-and-diff-verification-guidelines.md
notes/codex-task-results/MNEMOSYNE-032E-result.md
```

### targeted_diff

- exit_code: `0`

```text
diff --git a/handoff/startup-instructions.md b/handoff/startup-instructions.md
index f0d1d09..337b644 100644
--- a/handoff/startup-instructions.md
+++ b/handoff/startup-instructions.md
@@ -106,6 +106,23 @@ Detailed guideline:
 
 - `notes/codex-task-authoring-and-diff-verification-guidelines.md`
 
+## 5.2 Codex Cloud stale-branch / conflict-resolution troubleshooting rule
+
+MNEMOSYNE-032D follow-up diagnosis identified a likely root cause for repeated "file edits did not stick" incidents:
+
+- a Codex Cloud task environment / branch can become stale after its PR is merged into `master` / the default branch;
+- continuing from that stale task environment can produce a PR based on old repository content;
+- if the PR conflicts and the user resolves conflicts by unconditionally choosing "Accept Incoming", stale incoming content can roll back previously correct default-branch content;
+- the result can look like Codex failed to edit the files, even though the real issue was stale branch state plus conflict-resolution rollback.
+
+For future Codex repository-editing tasks:
+
+- prefer a fresh Codex Cloud task after each merged PR;
+- treat old Codex task environments as stale after their PR has been merged;
+- if a Codex PR has conflicts, do not use unconditional "Accept Incoming" as the default resolution;
+- low-manual-review fallback: close / discard the conflicted PR and rerun the deterministic task from a new Codex Cloud task based on the latest default branch;
+- verify final default-branch content after merge, especially for `current/active-context.md`, `handoff/handoff-current.md`, and `handoff/startup-instructions.md`.
+
 ## 6. 新 ChatGPT 对话启动提示
 
 ```text
diff --git a/notes/codex-task-authoring-and-diff-verification-guidelines.md b/notes/codex-task-authoring-and-diff-verification-guidelines.md
index 2d1b2da..60843d4 100644
--- a/notes/codex-task-authoring-and-diff-verification-guidelines.md
+++ b/notes/codex-task-authoring-and-diff-verification-guidelines.md
@@ -18,6 +18,47 @@ During MNEMOSYNE-031, a failure mode was observed:
 - In one cleanup task, Codex reported stale-phrase checks as passed even though direct repository inspection still found stale continuation guidance in current entry files.
 - The problem was resolved only after using a hard-fix prompt with exact replacements and HEAD-based git diff verification.
 
+## known_failure_mode_stale_codex_branch_and_accept_incoming_rollback
+
+During the MNEMOSYNE-031 / MNEMOSYNE-032 repair sequence, a stronger failure diagnosis was identified after MNEMOSYNE-032D was verified.
+
+The repeated symptom was that Codex task results, branch-local checks, or intermediate commits could appear correct, while the final default branch still lacked the intended entry-file changes or had reverted to older wording.
+
+The current best explanation is not only that Codex may fail to follow natural-language file-editing instructions. A major likely cause is stale Codex Cloud branch state combined with manual conflict resolution:
+
+1. A Codex Cloud task works in a task environment / branch snapshot, not in the repository default branch itself.
+2. After the task opens a PR and that PR is merged, the old Codex task environment should be treated as stale unless it can prove it has synchronized with the latest default branch.
+3. If the user continues from that stale task environment, the next PR may contain old file content plus the new task changes.
+4. If that PR conflicts and the conflict is resolved by unconditionally choosing "Accept Incoming", the incoming side can carry stale content back into the default branch.
+5. This can make correct earlier changes disappear from `master` / the default branch, creating the false impression that Codex never modified the target files.
+
+Symptoms suggesting this failure mode:
+
+- A task result record claims success, but final default-branch inspection does not show the target text.
+- A PR branch or intermediate commit contains the desired change, but the current default branch does not.
+- A later merge removed previously verified entry-file content.
+- Search finds the expected phrase only in task result records, not in the intended entry file.
+- The user resolved a PR conflict by accepting the incoming side wholesale.
+- The same files repeatedly oscillate between "fixed" and stale states.
+
+Troubleshooting questions:
+
+1. Was the Codex task started from a fresh task after the previous PR was merged?
+2. Did the PR have conflicts?
+3. Were conflicts resolved with unconditional "Accept Incoming"?
+4. Does the final default branch, not merely the PR branch or task result record, contain the required text?
+5. Did `git diff HEAD --name-only` and targeted diffs include the actual target files before commit/PR?
+6. Can the Codex environment prove that it fetched or checked out the latest default branch?
+
+Operational rule:
+
+- Prefer starting a new Codex Cloud task for each repository-editing task after the previous PR has been merged.
+- Do not continue using an old Codex Cloud task environment for new repository modifications after its PR has been merged.
+- If a Codex PR has conflicts, do not resolve them by unconditional "Accept Incoming" for the whole conflict set.
+- Treat a conflicted Codex PR as stale unless the final merged content can be mechanically verified.
+- The low-manual-review fallback is: close / discard the conflicted PR and rerun the same deterministic patch from a new Codex Cloud task based on the latest default branch.
+- Always verify the final default branch content after merge for high-risk entry files.
+
 ## rule
 
 For Codex tasks that modify repository files, natural-language completion claims are not enough.
diff --git a/notes/codex-task-results/MNEMOSYNE-032E-result.md b/notes/codex-task-results/MNEMOSYNE-032E-result.md
new file mode 100644
index 0000000..fd3b076
--- /dev/null
+++ b/notes/codex-task-results/MNEMOSYNE-032E-result.md
@@ -0,0 +1,55 @@
+# MNEMOSYNE-032E Stale Codex Branch and Accept Incoming Rollback Note Result
+
+## metadata
+
+- task_id: MNEMOSYNE-032E
+- task_type: workflow_troubleshooting_note
+- record_is_execution_source: no
+
+## purpose
+
+Record the diagnosis that repeated missing Codex edits may be caused by stale Codex Cloud branch state plus unconditional "Accept Incoming" conflict resolution, not only by Codex failing to follow natural-language edit instructions.
+
+## initial_repository_state
+
+- initial_head: `b3379b4053535d0ecacd0a209a772a388f502cb0`
+- initial_branch: `work`
+- initial_status_short_before_patch: |
+  M handoff/startup-instructions.md
+   M notes/codex-task-authoring-and-diff-verification-guidelines.md
+  A  notes/codex-task-results/MNEMOSYNE-032E-result.md
+
+## files_intended_to_edit
+
+- `notes/codex-task-authoring-and-diff-verification-guidelines.md`
+- `handoff/startup-instructions.md`
+- `notes/codex-task-results/MNEMOSYNE-032E-result.md`
+
+## files_not_to_edit
+
+- `current/human-approved-spec.md`
+- `current/active-context.md`
+- `handoff/handoff-current.md`
+- research report originals
+- prompt originals
+- PDFs
+- `AGENTS.md`
+- `CLAUDE.md`
+- GitHub Actions / automation files
+
+## patch_script_results
+
+- already_present: `notes/codex-task-authoring-and-diff-verification-guidelines.md` :: known failure mode section
+- already_present: `handoff/startup-instructions.md` :: startup troubleshooting section
+
+## verification
+
+TO_BE_FILLED
+
+## protected_file_confirmation
+
+TO_BE_FILLED
+
+## known_gaps_or_followups
+
+TO_BE_FILLED
```

### guideline_check

- exit_code: `0`

```text
21:## known_failure_mode_stale_codex_branch_and_accept_incoming_rollback
27:The current best explanation is not only that Codex may fail to follow natural-language file-editing instructions. A major likely cause is stale Codex Cloud branch state combined with manual conflict resolution:
32:4. If that PR conflicts and the conflict is resolved by unconditionally choosing "Accept Incoming", the incoming side can carry stale content back into the default branch.
48:3. Were conflicts resolved with unconditional "Accept Incoming"?
57:- If a Codex PR has conflicts, do not resolve them by unconditional "Accept Incoming" for the whole conflict set.
59:- The low-manual-review fallback is: close / discard the conflicted PR and rerun the same deterministic patch from a new Codex Cloud task based on the latest default branch.
```

### startup_check

- exit_code: `0`

```text
109:## 5.2 Codex Cloud stale-branch / conflict-resolution troubleshooting rule
115:- if the PR conflicts and the user resolves conflicts by unconditionally choosing "Accept Incoming", stale incoming content can roll back previously correct default-branch content;
120:- prefer a fresh Codex Cloud task after each merged PR;
122:- if a Codex PR has conflicts, do not use unconditional "Accept Incoming" as the default resolution;
123:- low-manual-review fallback: close / discard the conflicted PR and rerun the deterministic task from a new Codex Cloud task based on the latest default branch;
124:- verify final default-branch content after merge, especially for `current/active-context.md`, `handoff/handoff-current.md`, and `handoff/startup-instructions.md`.
```

### result_check

- exit_code: `0`

```text
1:# MNEMOSYNE-032E Stale Codex Branch and Accept Incoming Rollback Note Result
5:- task_id: MNEMOSYNE-032E
7:- record_is_execution_source: no
11:Record the diagnosis that repeated missing Codex edits may be caused by stale Codex Cloud branch state plus unconditional "Accept Incoming" conflict resolution, not only by Codex failing to follow natural-language edit instructions.
20:  A  notes/codex-task-results/MNEMOSYNE-032E-result.md
26:- `notes/codex-task-results/MNEMOSYNE-032E-result.md`
```

### protected_human_spec_check

- exit_code: `1`

```text
(no output)
```

### forbidden_files_check

- exit_code: `1`

```text
(no output)
```

## protected_file_confirmation

- `current/human-approved-spec.md` was not modified.
- `current/active-context.md` was not modified by this task.
- `handoff/handoff-current.md` was not modified by this task.
- Research report originals were not modified.
- Prompt originals were not modified.
- PDF files were not modified.
- `AGENTS.md` and `CLAUDE.md` were not created or modified.
- GitHub Actions / automation files were not created or modified.

## known_gaps_or_followups

- TASK_STATUS: verification_passed
- The stale Codex Cloud branch + unconditional Accept Incoming rollback diagnosis is now recorded in the Codex task guideline and startup troubleshooting instructions.
- This record is not an execution source.
- Current execution source remains `current/human-approved-spec.md`.
