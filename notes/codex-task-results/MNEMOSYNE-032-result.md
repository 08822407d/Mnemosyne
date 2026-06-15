# MNEMOSYNE-032 Codex Task Result

## metadata

- task_id: MNEMOSYNE-032
- task_type: workflow_guardrail_documentation_update
- record_is_execution_source: no

## task_purpose

Record the MNEMOSYNE-031 lesson that natural-language Codex file-editing tasks may fail to modify all intended files unless the task requires git diff evidence, exact replacements, and explicit verification.

## files_intended_to_edit

- `notes/codex-task-authoring-and-diff-verification-guidelines.md`
- `handoff/startup-instructions.md`
- `notes/self-improvement-workflow.md`
- `notes/self-improvement-template-pack.md`
- `notes/system-construction-baseline.md`
- `current/active-context.md`
- `handoff/handoff-current.md`
- `notes/candidate-requirements.md`
- `notes/decision-log.md`
- `notes/codex-task-results/MNEMOSYNE-032-result.md`

## files_actually_edited

- `notes/codex-task-authoring-and-diff-verification-guidelines.md` created.
- `handoff/startup-instructions.md` modified.
- `notes/self-improvement-workflow.md` modified.
- `notes/self-improvement-template-pack.md` modified.
- `notes/system-construction-baseline.md` modified.
- `current/active-context.md` modified.
- `handoff/handoff-current.md` modified.
- `notes/candidate-requirements.md` modified.
- `notes/decision-log.md` modified.
- `notes/codex-task-results/MNEMOSYNE-032-result.md` created and filled.

## protected_file_confirmation

Confirmed by `git status --short` and `git diff HEAD --name-only` before staging: only intended target files changed or were newly created.

Required confirmations:
- `current/human-approved-spec.md` was not modified.
- Research report originals were not modified.
- Pro prompt original was not modified.
- Missing light prompts were not created or modified.
- PDF files were not modified.
- `AGENTS.md` and `CLAUDE.md` were not created or modified.
- GitHub Actions / automation files were not created or modified.

## verification

Patch script result:

```text
Patch results:
- written: notes/codex-task-authoring-and-diff-verification-guidelines.md :: create guideline file
- replaced: handoff/startup-instructions.md :: startup standard read order add diff guideline
- inserted: handoff/startup-instructions.md :: startup add 5.1 diff verification section
- replaced: handoff/startup-instructions.md :: startup ChatGPT prompt read list add guideline
- replaced: handoff/startup-instructions.md :: startup Codex prompt read list add guideline
- replaced: handoff/startup-instructions.md :: startup Codex prompt output requires diff plan
- inserted: notes/self-improvement-workflow.md :: workflow add 10.1 diff verification
- replaced: notes/self-improvement-workflow.md :: workflow strengthen failure handling
- replaced: notes/self-improvement-template-pack.md :: template Codex result fields add diff verification
- replaced: notes/self-improvement-template-pack.md :: template Codex result notes add diff rule
- replaced: notes/self-improvement-template-pack.md :: template apply checklist add diff verification items
- replaced: notes/system-construction-baseline.md :: baseline add diff verification convention
- inserted: current/active-context.md :: active add MNEMOSYNE-032 completed/visible note
- replaced: current/active-context.md :: active important files add guideline
- inserted: handoff/handoff-current.md :: handoff add verification reminder
- appended: notes/candidate-requirements.md :: candidate add MNEMOSYNE-032 guardrail
- appended: notes/decision-log.md :: decision add MNEMOSYNE-032 guardrail
- written: notes/codex-task-results/MNEMOSYNE-032-result.md :: create MNEMOSYNE-032 result record placeholder
```

### git status --short

```text
 M current/active-context.md
 M handoff/handoff-current.md
 M handoff/startup-instructions.md
 M notes/candidate-requirements.md
 M notes/decision-log.md
 M notes/self-improvement-template-pack.md
 M notes/self-improvement-workflow.md
 M notes/system-construction-baseline.md
?? notes/codex-task-authoring-and-diff-verification-guidelines.md
?? notes/codex-task-results/MNEMOSYNE-032-result.md
```

### git diff HEAD --stat

```text
 current/active-context.md               |  2 ++
 handoff/handoff-current.md              |  8 ++++++
 handoff/startup-instructions.md         | 49 +++++++++++++++++++++++++--------
 notes/candidate-requirements.md         | 13 +++++++++
 notes/decision-log.md                   |  8 ++++++
 notes/self-improvement-template-pack.md | 14 ++++++++++
 notes/self-improvement-workflow.md      | 26 +++++++++++++++--
 notes/system-construction-baseline.md   |  2 ++
 8 files changed, 108 insertions(+), 14 deletions(-)
```

Note: before staging, untracked created files are visible in `git status --short` but not in `git diff HEAD --stat`.

### git diff HEAD --name-only

```text
current/active-context.md
handoff/handoff-current.md
handoff/startup-instructions.md
notes/candidate-requirements.md
notes/decision-log.md
notes/self-improvement-template-pack.md
notes/self-improvement-workflow.md
notes/system-construction-baseline.md
```

Note: before staging, untracked created files are visible in `git status --short` but not in `git diff HEAD --name-only`.

### visibility checks

`test -f notes/codex-task-authoring-and-diff-verification-guidelines.md` exited with status `0`.

`rg -n "codex-task-authoring-and-diff-verification-guidelines|git diff HEAD|Codex task authoring" handoff/startup-instructions.md` produced matches at lines 29, 88, 98, 99, 100, 107, 126, 161, and 196.

`rg -n "Codex / ChatGPT task verification reminder|git diff HEAD|codex-task-authoring" handoff/handoff-current.md` produced matches at lines 91, 95, and 97.

`rg -n "Codex 文件修改任务的 diff 验证规则|自然语言描述|git diff HEAD|patch script" notes/self-improvement-workflow.md` produced matches at lines 213, 215, 221, 223, 224, 225, and 299.

`rg -n "actual_git_status_short|actual_git_diff_stat|actual_git_diff_name_only|targeted_diff_hunks_or_summary|protected_file_check|claim_vs_diff_consistency" notes/self-improvement-template-pack.md` produced matches at lines 169, 170, 171, 172, 174, and 176.

`rg -n "Codex 文件修改任务不得只依赖自然语言完成声明|git diff HEAD|patch script" notes/system-construction-baseline.md` produced matches at lines 129 and 130.

The result-record placeholder marker check returned no matches after this file was filled.

## known_gaps_or_followups

- This task adds documentation and workflow guardrails only.
- It does not introduce automation.
- It does not modify the current execution source.
- Future Codex file-editing tasks still need to explicitly include and enforce these diff verification rules in their prompts.

## reviewer_correction_after_MNEMOSYNE_032D

A later default-branch inspection found that MNEMOSYNE-032 / MNEMOSYNE-032B / MNEMOSYNE-032C result records were not enough by themselves to prove that the final default branch contained the visible handoff reminder and active-context status correction.

MNEMOSYNE-032D was created as a direct-command master-entry fix. Future review should verify the final default branch files directly, not only the task result prose or an intermediate branch/commit.
